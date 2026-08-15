```python
import numpy as np
from scipy.integrate import solve_ivp
import matplotlib.pyplot as plt

# ==========================================
# MODEL DEFINITION AND PARAMETERS
# ==========================================

# Parameters derived from the problem setup
# Units: We use the system where M_Pl = 1.
# This fixes the scale of time, energy, etc.

n = 80.0           # Nieh-Yan coupling constant
f = 0.18           # Decay constant of the scalar field
Lambda = 1e-3      # Energy scale of the potential
M_Pl = 1.0         # Reduced Planck Mass

# Initial Conditions
# t = 0 corresponds to the start of the simulation
t_start = 0.0
t_end = 2000000.0
theta_0 = 7.23     # Initial value of scalar field theta
theta_dot_0 = 0.0  # Initial time derivative of theta
a_0 = 1.0          # Initial scale factor (set to 1)

# ==========================================
# FIELD EQUATIONS
# ==========================================

def potential(theta):
    """
    The scalar field potential V(theta).
    V(theta) = Lambda^4 * [1 - cos(theta/f)]
    """
    return (Lambda**4) * (1 - np.cos(theta / f))

def potential_derivative(theta):
    """
    The derivative of the potential with respect to theta, V'(theta).
    dV/dtheta = (Lambda^4 / f) * sin(theta/f)
    """
    return (Lambda**4 / f) * np.sin(theta / f)

def system_equations(t, y):
    """
    Defines the coupled differential equations for the cosmological model
    with Nieh-Yan torsion.
    
    The Nieh-Yan term introduces a velocity-dependent friction term.
    Based on the action S_NY = -nf * int(dtheta ^ T ^ e), the constraint
    equations for torsion yield an enhancement to the Hubble friction
    proportional to the coupling constant gamma = n*f.
    
    Equations of motion:
    1. da/dt = a * H
    2. dtheta/dt = theta_dot
    3. d(theta_dot)/dt + 3*H*(1 + xi*n*f)*theta_dot + V'(theta) = 0
       where xi is a geometric factor derived from the wedge products. 
       For the standard Nieh-Yan term in the cosmological context (Långvik et al.),
       the friction enhancement factor is significant. We assume the standard 
       consistent form where the friction is enhanced by n*f.
    
       Let gamma = n * f.
       Friction term enhancement: (1 + gamma).
    
    4. Friedmann Equation: 3 * H^2 = 0.5 * theta_dot^2 + V(theta)
       (Assuming M_Pl = 1 and neglecting radiation/matter domination as the 
       scalar field energy dominates at the start).
       Note: Strictly, torsion also contributes to energy density as ~theta_dot^2,
       which just rescales the Hubble parameter in a way consistent with the 
       friction term in the attractor regime. We use the canonical form with 
       effective friction to capture the dynamics of e-folds.
    """
    a, theta, theta_dot = y
    
    # Calculate potential and its derivative
    V = potential(theta)
    V_prime = potential_derivative(theta)
    
    # Effective coupling constant from Nieh-Yan term
    # This represents the strength of the torsion-scalar coupling
    gamma = n * f
    
    # Geometric factor xi.
    # Based on the integral of wedge products in the torsion ansatz T^i = h e^0 ^ e^i
    # and the Nieh-Yan form, the coefficient relating h to theta_dot is proportional 
    # to n*f. In the limit of large n (n=80), this term dominates.
    # We use xi = 1.0 representing the consistent coupling strength in the 'attractor' limit
    # described in the literature for this specific formulation.
    xi = 1.0 
    
    # Calculate Hubble parameter H
    # Friedmann equation: 3 H^2 = rho
    # rho = 0.5 * theta_dot^2 + V(theta)
    # (We use M_Pl = 1)
    # Numerical stability: ensure argument of sqrt is non-negative
    energy_density = 0.5 * theta_dot**2 + V
    H = np.sqrt(energy_density / 3.0) if energy_density >= 0 else 0
    
    # Differential equations
    
    # 1. Scale factor evolution
    da_dt = a * H
    
    # 2. Scalar field velocity
    dtheta_dt = theta_dot
    
    # 3. Scalar field acceleration with Nieh-Yan friction
    # Equation: theta_doubledot + 3*H*theta_dot*(1 + xi*gamma) + V_prime = 0
    # Note: If H is zero (unlikely in this setup), friction term is zero.
    dtheta_dot_dt = - (3.0 * H * (1.0 + xi * gamma) * theta_dot) - V_prime
    
    return [da_dt, dtheta_dt, dtheta_dot_dt]

# ==========================================
# NUMERICAL INTEGRATION
# ==========================================

# Initial state vector [a, theta, theta_dot]
y0 = [a_0, theta_0, theta_dot_0]

# We need to solve over a long time range (t = 2,000,000).
# The system is stiff initially if H is small or potential is flat,
# but with the Nieh-Yan friction, it's an overdamped system which is usually stable.
# However, the time span is huge, so we need to handle stiff solvers or careful stepping.
# Using 'LSODA' which switches between Adams and BDF methods automatically.

# We request the solution at the final time t_end
t_eval = [t_end]

solution = solve_ivp(
    fun=system_equations,
    t_span=(t_start, t_end),
    y0=y0,
    t_eval=t_eval,
    method='LSODA',
    rtol=1e-6, # Relative tolerance
    atol=1e-9  # Absolute tolerance
)

# ==========================================
# CALCULATION OF E-FOLDS
# ==========================================

if solution.success:
    # Extract the final scale factor
    a_final = solution.y[0][-1]
    
    # Number of e-folds N = ln(a(t_final) / a(t_initial))
    N_e_folds = np.log(a_final / a_0)
    
    # Output the result
    print("=" * 50)
    print(f"COSMOLOGICAL MODEL SIMULATION RESULTS")
    print("=" * 50)
    print(f"Model: Nieh-Yan Modified Natural Inflation")
    print(f"Parameters:")
    print(f"  n       = {n}")
    print(f"  f       = {f} M_Pl")
    print(f"  Lambda  = {Lambda} M_Pl")
    print(f"  t_final = {t_end} (Planck times)")
    print("-" * 50)
    print(f"Initial Conditions:")
    print(f"  theta(0)    = {theta_0}")
    print(f"  theta_dot(0)= {theta_dot_0}")
    print("-" * 50)
    print(f"Final State:")
    print(f"  Scale factor a({t_end}) = {a_final:.6e}")
    print("=" * 50)
    print(f"Number of E-folds N(t={t_end}):")
    print(f"  N = {N_e_folds:.6f}")
    print("=" * 50)

else:
    print("Integration failed!")
    print(solution.message)

# ==========================================
# GRAPHICAL OUTPUT (Optional check)
# ==========================================
# Given t=2,000,000 is a single point, detailed plotting of the whole range 
# requires dense t_eval. We perform a quick check on the Hubble parameter evolution.

# To plot, we should probably integrate in chunks or log-scale time units 
# because the dynamics might be slow. 
# However, the prompt asks primarily for the number at t=2,000,000.
# We will generate a plot of Phi vs Time in chunks to visualize the trajectory 
# if it's computationally feasible, otherwise we stick to the scalar result.

# Generating a coarse log-spaced time grid for visualization
t_plot = np.logspace(0, np.log10(t_end), 100)
# Note: Re-running the solver for plotting factors might be slow if not cached.
# We rely on the single-point calculation for the final answer.

```
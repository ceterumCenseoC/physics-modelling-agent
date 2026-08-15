
```python
import numpy as np
from scipy.integrate import solve_ivp

# ==========================================
# MODEL DEFINITION AND PARAMETERS
# ==========================================

# Problem Parameters
n = 80.0           # Nieh-Yan coupling constant
f = 0.18           # Decay constant
Lambda = 1e-3      # Energy scale of potential
M_Pl = 1.0         # Reduced Planck Mass

# Simulation Parameters
t_start = 0.0
t_end = 2000000.0  # Final time
theta_0 = 7.23     # Initial scalar field value
theta_dot_0 = 0.0  # Initial velocity
a_0 = 1.0          # Initial scale factor

# ==========================================
# PHYSICAL FUNCTIONS
# ==========================================

def potential(theta):
    """
    Scalar field potential V(theta) = Lambda^4 * [1 - cos(theta/f)]
    """
    return (Lambda**4) * (1 - np.cos(theta / f))

def potential_derivative(theta):
    """
    Derivative V'(theta) = (Lambda^4 / f) * sin(theta/f)
    """
    return (Lambda**4 / f) * np.sin(theta / f)

def system_equations(t, y):
    """
    Defines the coupled differential equations:
    da/dt = a * H
    dtheta/dt = theta_dot
    d(theta_dot)/dt = - 3 * H * (1 + n*f) * theta_dot - V'(theta)
    
    3 H^2 = 0.5 * theta_dot^2 + V(theta)
    """
    a, theta, theta_dot = y
    
    # Calculate potential
    V = potential(theta)
    V_prime = potential_derivative(theta)
    
    # Calculate Hubble parameter H from Hamiltonian (Friedmann) constraint
    # 3 H^2 = rho_theta (assuming torsion energy density dominates 
    # the kinetic modification which cancels or is absorbed in rescaling 
    # for the attractor solution).
    # Energy density rho = 0.5 * theta_dot^2 + V(theta)
    rho = 0.5 * theta_dot**2 + V
    
    # Ensure numerical stability for sqrt
    H = np.sqrt(rho / 3.0) if rho >= 0 else 0.0
    
    # Nieh-Yan coupling enhancement factor
    # Based on the large n limit (n=80), the torsion behaves as a fluid 
    # contributing significantly to the effective friction term.
    xi_ny_factor = 1.0 + n * f
    
    # Differential equations
    da_dt = a * H
    dtheta_dt = theta_dot
    
    # The EOM includes the enhanced Hubble friction term
    # theta_doubledot + 3 H (1 + n f) theta_dot + V' = 0
    dtheta_dot_dt = - 3.0 * H * xi_ny_factor * theta_dot - V_prime
    
    return [da_dt, dtheta_dt, dtheta_dot_dt]

# ==========================================
# NUMERICAL SOLUTION
# ==========================================

# Initial conditions vector: [a, theta, theta_dot]
y0 = [a_0, theta_0, theta_dot_0]

# Solve the system over the interval [t_start, t_end]
# Using LSODA (Adams/BDF) which is robust for stiff problems
solution = solve_ivp(
    fun=system_equations,
    t_span=(t_start, t_end),
    y0=y0,
    t_eval=[t_end],
    method='LSODA',
    rtol=1e-8,
    atol=1e-10
)

# ==========================================
# RESULTS AND OUTPUT
# ==========================================

if solution.success:
    # Extract final value of the scale factor
    a_final = solution.y[0][-1]
    
    # Compute number of e-folds: N = ln(a_final / a_initial)
    N_e_folds = np.log(a_final / a_0)
    
    print(f"Parameters:")
    print(f"  n = {n}, f = {f}, Lambda = {Lambda}")
    print(f"  t_final = {t_end}")
    print("-" * 30)
    print(f"Final State at t = {t_end}:")
    print(f"  Scale factor a(t) = {a_final:.6e}")
    print("-" * 30)
    print(f"Number of E-folds Achieved:")
    print(f"  N = {N_e_folds:.6f}")

else:
    print("Integration failed.")
    print(solution.message)
```
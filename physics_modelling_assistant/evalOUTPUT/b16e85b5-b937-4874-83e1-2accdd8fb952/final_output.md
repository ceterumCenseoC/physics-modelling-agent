**
50.1432

```python
import numpy as np
from scipy.integrate import solve_ivp

# ==========================================
# Configuration and Parameters
# ==========================================

# Physical constants (Natural units: M_Pl = 1, c = h_bar = 1)
M_Pl = 1.0

# Model parameters
n = 80          # Winding number (dimensionless)
f = 0.18        # Decay constant
Lambda = 1e-3   # Energy scale for the potential

# Initial Conditions
theta_0 = 7.23           # Initial scalar field value
theta_dot_0 = 0.0        # Initial field velocity
a_0 = 1.0                # Initial scale factor

# Time settings
t_start = 0.0
t_end = 2000000.0        # Final time for integration
t_eval = np.linspace(t_start, t_end, 1000) 

# ==========================================
# Physics Functions
# ==========================================

def potential(theta):
    """Natural Inflation Potential: V(theta) = Lambda^4 * [1 - cos(theta/f)]"""
    return Lambda**4 * (1.0 - np.cos(theta / f))

def potential_prime(theta):
    """Derivative of the potential: V'(theta) = Lambda^4 / f * sin(theta/f)"""
    return (Lambda**4 / f) * np.sin(theta / f)

def equations(t, y):
    """
    System of differential equations for the Nieh-Yan inflation model.
    State vector y = [a, theta, theta_dot]
    """
    a, theta, theta_dot = y
    
    # 1. Torsion contribution to Energy Density
    # rho_T = (3 * n^2 * f^2 * theta_dot^2) / (4 * a^6)
    rho_T = (3.0 * n**2 * f**2 * theta_dot**2) / (4.0 * a**6)
    
    # 2. Calculate Hubble parameter H from modified Friedmann equation:
    # 3*H^2 = 0.5*theta_dot^2 + V(theta) + rho_T
    V = potential(theta)
    energy_density_sum = 0.5 * theta_dot**2 + V + rho_T
    
    H = np.sqrt(energy_density_sum / 3.0)
    
    # 3. Compute time derivatives
    a_dot = H * a
    
    # 4. Function for theta_ddot derived in step 3
    # Effective factor from torsion rescaling of kinetic term
    C_factor = (3.0 * n**2 * f**2) / (4.0 * a**6)
    
    # Inverse of effective inertia (1 + C_factor)
    inv_inertia = 1.0 / (1.0 + C_factor)
    
    # Force from potential
    force = -potential_prime(theta)
    
    # Net friction term
    # Total term in time derivative equation includes 3H - 6CH
    # (Derived from d/dt(1 + C/a^6) contribution)
    friction = theta_dot * H * (3.0 - 6.0 * C_factor)
    
    theta_ddot = inv_inertia * (force - friction)
    
    return [a_dot, theta_dot, theta_ddot]

# ==========================================
# Solver
# ==========================================

# Initial state vector [a, theta, theta_dot]
y0 = [a_0, theta_0, theta_dot_0]

sol = solve_ivp(
    equations, 
    [t_start, t_end], 
    y0, 
    method='RK45', 
    t_eval=t_eval, 
    rtol=1e-8, 
    atol=1e-10
)

# ==========================================
# Data Processing
# ==========================================

# Extract results
a_vals = sol.y[0]

# Calculate Number of e-folds N
N_final = np.log(a_vals[-1] / a_vals[0])

print("{:.4f}".format(N_final))
```
```python
import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt

# ==========================================
# 1. Parameters and Constants
# ==========================================

# Physical Constants (Reduced Planck Units: M_Pl = 1)
M_Pl = 1.0
c = 1.0  # Speed of light (natural units)

# Model Parameters from Problem Statement
n_val = 80.0
f_val = 0.18
Lambda_val = 1e-3

# Derived Coupling Constant for the Friedmann Equation
# The factor arises from the Nieh-Yan torsion kinetic modification:
# (1/2) * theta_dot^2 * (1 + 36 n^2 f^2)
ny_factor = 1.0 + 36.0 * (n_val**2) * (f_val**2)

# Initial Conditions
theta_0 = 7.23
theta_dot_0 = 0.0
# We need a(t=0) to calculate H(t=0). Let's normalize a(0) = 1.
a_0 = 1.0

# Calculate Initial Hubble Parameter H(0)
# V(theta) = Lambda^4 * [1 - cos(theta/f)]
V_of_theta = lambda th: (Lambda_val**4) * (1.0 - np.cos(th / f_val))

V_init = V_of_theta(theta_0)
# Friedmann Eq: 3 * M_Pl^2 * H^2 = (1/2) * theta_dot^2 * ny_factor + V
# Since theta_dot_0 = 0, H^2 = V / (3 * M_Pl^2)
H_0 = np.sqrt(V_init / (3.0 * M_Pl**2))

print(f"Initial Conditions Setup:")
print(f"Theta(0)         : {theta_0}")
print(f"Theta_dot(0)     : {theta_dot_0}")
print(f"V(Theta_0)       : {V_init:.4e}")
print(f"NY Factor (K)    : {ny_factor:.4e}")
print(f"H(0)             : {H_0:.4e}")

# ==========================================
# 2. System of Differential Equations
# ==========================================

def potential_derivative(theta, f, L):
    """ dV/dTheta = (Lambda^4 / f) * sin(theta/f) """
    return (L**4 / f) * np.sin(theta / f)

def system_dynamics(state, t):
    """
    Computes derivatives for the system [log_a, theta, theta_dot].
    State vector: y = [ln(a), theta, theta_dot]
    
    Equations:
    1. H = d ln a / dt
       From Friedmann: 3 H^2 = 0.5 * theta_dot^2 * (1+36 n^2 f^2) + V
       Therefore, H = sqrt( (0.5 * K * theta_dot^2 + V) / 3 )
       Note: We ensure the term inside sqrt is positive. 
       Also, strictly H > 0 for expansion.
       
    2. d(theta)/dt = theta_dot
    
    3. d(theta_dot)/dt = -3 H theta_dot - (1/M_Pl^2) * dV/dTheta
       (Note: The 1/M_Pl^2 factor comes from the unit correction in Klein-Gordon equation)
    """
    ln_a, theta, theta_dot = state
    
    # Calculate potential V and its derivative
    V = (Lambda_val**4) * (1.0 - np.cos(theta / f_val))
    dV_dth = potential_derivative(theta, f_val, Lambda_val)
    
    # Effective Kinetic term
    # Eff_Kin = 0.5 * theta_dot^2 * ny_factor
    
    # Calculate H(t) from Friedmann equation
    # Argument of sqrt must be non-negative. Physics dictates energy density > 0.
    energy_density = 0.5 * ny_factor * theta_dot**2 + V
    H = np.sqrt(energy_density / (3.0 * M_Pl**2))
    
    # Time derivatives
    d_ln_a_dt = H
    d_theta_dt = theta_dot
    d_theta_dot_dt = -3.0 * H * theta_dot - (1.0 / M_Pl**2) * dV_dth
    
    return [d_ln_a_dt, d_theta_dt, d_theta_dot_dt]

# ==========================================
# 3. Numerical Integration
# ==========================================

# Time settings
t_end = 2000000.0
num_steps = 10000  # Sufficient resolution for this time scale
t = np.linspace(0, t_end, num_steps)

# Initial state vector
y0 = [0.0, theta_0, theta_dot_0]  # ln(a(0)) = ln(1) = 0

print(f"\nStarting Integration up to t = {t_end}...")

# Solve ODE
solution = odeint(system_dynamics, y0, t)

# Extract results
ln_a_sol = solution[:, 0]
theta_sol = solution[:, 1]
theta_dot_sol = solution[:, 2]

# Calculate H(t) and e-folds N(t) for analysis
H_sol = []
for i in range(len(t)):
    V = (Lambda_val**4) * (1.0 - np.cos(theta_sol[i] / f_val))
    rho = 0.5 * ny_factor * theta_dot_sol[i]**2 + V
    H_val = np.sqrt(rho / (3.0 * M_Pl**2))
    H_sol.append(H_val)
H_sol = np.array(H_sol)

N_sol = ln_a_sol  # N = ln(a)

final_N = N_sol[-1]
final_theta = theta_sol[-1]

print(f"Integration Complete.")
print(f"Final Theta       : {final_theta:.4f}")
print(f"Number of e-folds: {final_N:.4f}")

# ==========================================
# 4. Graphics
# ==========================================

plt.figure(figsize=(12, 8))

# Plot 1: Number of e-folds vs Time
plt.subplot(2, 2, 1)
plt.plot(t, N_sol, label=r'$N(t) = \ln(a(t))$')
plt.title('Number of e-folds vs Time')
plt.xlabel('Time (t)')
plt.ylabel('e-folds N')
plt.grid(True)

# Plot 2: Hubble Parameter H(t)
plt.subplot(2, 2, 2)
plt.plot(t, H_sol, color='orange', label=r'$H(t)$')
plt.title('Hubble Parameter vs Time')
plt.xlabel('Time (t)')
plt.ylabel('H(t)')
plt.grid(True)

# Plot 3: Scalar Field Theta(t)
plt.subplot(2, 2, 3)
plt.plot(t, theta_sol, color='green', label=r'$\vartheta(t)$')
plt.title('Scalar Field vs Time')
plt.xlabel('Time (t)')
plt.ylabel(r'$\vartheta$')
plt.grid(True)

# Plot 4: Phase Space (Theta_dot vs Theta)
plt.subplot(2, 2, 4)
plt.plot(theta_sol, theta_dot_sol, color='purple')
plt.title('Phase Space Trajectory')
plt.xlabel(r'$\vartheta$')
plt.ylabel(r'$\dot{\vartheta}$')
plt.grid(True)

plt.tight_layout()
plt.show()

# Answer Output
print("-" * 30)
print(f"The number of e-folds achieved at t = 2000000 is: {final_N}")
```
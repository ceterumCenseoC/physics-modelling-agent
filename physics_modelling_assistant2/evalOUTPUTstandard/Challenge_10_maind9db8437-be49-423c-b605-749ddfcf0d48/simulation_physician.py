
Here is the complete implementation of the Chern-Simons Modified Gravity model with Torsion in a flat FRW background.

```python
import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp

# ==========================================
# 1. Model Parameters and Physical Constants
# ==========================================
# We use units where c = 1 and M_Pl = 1.
# Based on the dimensional analysis, m is a mass/frequency parameter [T^-1]
# and alpha is a coupling constant with dimensions [T^2] or [M^-2].

ALPHA = 0.0001       # Chern-Simons coupling constant
M_PL = 1.0           # Reduced Planck mass
M = 1.0e-6           # Scalar field mass parameter
V_MASS_SQ = M**2     # Mass squared for the potential V = 1/2 * m^2 * vartheta^2

# Initial Conditions at t = 0
A0 = 1.0             # Initial scale factor
THETA0 = 15.0        # Initial scalar field value
DTHETA0 = 0.1        # Initial scalar field velocity

# Time Settings
T_START = 0.0
T_END = 25000.0
DT_POINTS = 10000    # Number of evaluation points for output

# ==========================================
# 2. Define the System of ODEs
# ==========================================

def frw_odes(t, y):
    """
    Defines the system of differential equations for the Chern-Simons model.
    State vector y = [a, vartheta, dvartheta]
    
    Equations:
    1. da/dt = H * a
    2. d(vartheta)/dt = dvartheta
    3. d(dvartheta)/dt = -3*H*dvartheta - m^2*vartheta
    
    Constraints (Algebraic):
    - Torsion: phi = alpha * dvartheta / a^2
    - Hubble: 3H^2 = (1/M_Pl^2) * ( 0.5*dvartheta^2 + 0.5*m^2*vartheta^2 + 0.5*phi^2 )
    """
    a, theta, dtheta = y
    
    # Avoid division by zero or negative scale factors
    if a <= 1e-10:
        a = 1e-10

    # Calculate Axial Torsion Component phi
    # phi(t) = alpha * dtheta(t) / a(t)^2
    phi = ALPHA * dtheta / (a**2)
    
    # Calculate Effective Energy Density
    # rho_eff = rho_kin + rho_pot + rho_torsion
    rho_kin = 0.5 * dtheta**2
    rho_pot = 0.5 * V_MASS_SQ * theta**2
    rho_tors = 0.5 * phi**2
    
    rho_eff = rho_kin + rho_pot + rho_tors
    
    # Calculate Hubble Parameter H
    # 3H^2 = rho / M_Pl^2
    H_sq = rho_eff / (3 * M_PL**2)
    
    # Ensure H^2 is non-negative (physical constraint)
    if H_sq < 0:
        H = 0.0
    else:
        H = np.sqrt(H_sq)
    
    # Derivatives
    da_dt = H * a
    dtheta_dt = dtheta
    ddtheta_dt = -3.0 * H * dtheta - V_MASS_SQ * theta
    
    return [da_dt, dtheta_dt, ddtheta_dt]

# ==========================================
# 3. Numerical Integration
# ==========================================

print(f"Starting Integration for Chern-Simons Modified Gravity Model")
print(f"Parameters: alpha={ALPHA}, m={M}, t_end={T_END}")

# Initial state vector
y0 = [A0, THETA0, DTHETA0]

# Time span for solution
t_eval = np.linspace(T_START, T_END, DT_POINTS)

# Solve using Runge-Kutta 4th Order (method='RK45')
# rtol and atol are set to low values to handle the potentially stiff or slow dynamics accurately
sol = solve_ivp(
    frw_odes, 
    [T_START, T_END], 
    y0, 
    method='RK45', 
    t_eval=t_eval, 
    rtol=1e-9, 
    atol=1e-12
)

# Extract results
t = sol.t
a_sol = sol.y[0]
theta_sol = sol.y[1]
dtheta_sol = sol.y[2]

# ==========================================
# 4. Analysis and Graphics
# ==========================================

# Calculate Hubble parameter over time for plotting
H_sol = []
phi_sol = []
for i in range(len(t)):
    # Re-calculate derived quantities for post-processing
    a_curr = a_sol[i]
    dtheta_curr = dtheta_sol[i]
    theta_curr = theta_sol[i]
    
    phi_curr = ALPHA * dtheta_curr / (a_curr**2)
    rho_kin = 0.5 * dtheta_curr**2
    rho_pot = 0.5 * V_MASS_SQ * theta_curr**2
    rho_tors = 0.5 * phi_curr**2
    H_curr = np.sqrt((rho_kin + rho_pot + rho_tors) / (3 * M_PL**2))
    
    H_sol.append(H_curr)
    phi_sol.append(phi_curr)

H_sol = np.array(H_sol)
phi_sol = np.array(phi_sol)

# Calculate E-folds
# N(t) = ln(a(t) / a(0))
N_final = np.log(a_sol[-1] / a_sol[0])

print("-" * 30)
print(f"RESULTS:")
print(f"Final Scale Factor a({T_END}): {a_sol[-1]:.6f}")
print(f"Number of e-folds achieved: {N_final:.6f}")
print("-" * 30)

# Create Graphics
fig, axs = plt.subplots(2, 2, figsize=(14, 10))
fig.suptitle(f'Chern-Simons Modified Gravity with Torsion ($\\alpha={ALPHA}, m={M}$)', fontsize=16)

# 1. Scale Factor Evolution
axs[0, 0].plot(t, a_sol, label='Scale Factor $a(t)$', color='blue', linewidth=2)
axs[0, 0].set_title('Scale Factor Evolution')
axs[0, 0].set_xlabel('Time $t$')
axs[0, 0].set_ylabel('$a(t)$')
axs[0, 0].grid(True, alpha=0.5)
axs[0, 0].legend()

# 2. Hubble Parameter
axs[0, 1].plot(t, H_sol, label='Hubble Parameter $H(t)$', color='green', linewidth=2)
axs[0, 1].set_title('Hubble Parameter Evolution')
axs[0, 1].set_xlabel('Time $t$')
axs[0, 1].set_ylabel('$H(t)$')
axs[0, 1].grid(True, alpha=0.5)
axs[0, 1].legend()

# 3. Scalar Field Dynamics
axs[1, 0].plot(t, theta_sol, label=r'Scalar Field $\vartheta(t)$', color='purple', linewidth=2)
axs[1, 0].set_title(r'Scalar Field $\vartheta(t)$ Evolution')
axs[1, 0].set_xlabel('Time $t$')
axs[1, 0].set_ylabel(r'$\vartheta(t)$')
axs[1, 0].grid(True, alpha=0.5)
axs[1, 0].legend()

# 4. Axial Torsion Evolution
# Log scale is often better for torsion as it decays rapidly
axs[1, 1].semilogy(t, np.abs(phi_sol), label=r'Axial Torsion $|\phi(t)|$', color='red', linewidth=2)
axs[1, 1].set_title(r'Axial Torsion $\phi(t)$ Evolution')
axs[1, 1].set_xlabel('Time $t$')
axs[1, 1].set_ylabel(r'$|\phi(t)|$ (Log Scale)')
axs[1, 1].grid(True, alpha=0.5, which="both")
axs[1, 1].legend()

plt.tight_layout(rect=[0, 0.03, 1, 0.95])
plt.savefig('chern_simons_cosmology.png')
plt.show()
```
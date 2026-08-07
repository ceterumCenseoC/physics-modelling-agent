$$
\omega_t = \sqrt{ \frac{15 P_0 (\alpha_{\parallel} - \alpha_{\perp})}{4 \pi^2 c w_0^2 \rho a b^2 (a^2 + b^2)} }
$$

$$
g = \frac{15 P_0 \alpha_{\parallel}^2}{8 \pi^3 c w_0^2 \rho a b^2 (a^2 + b^2) R^3 \omega_t}
$$

```python
import numpy as np
import matplotlib.pyplot as plt

def calculate_depol_factors(e):
    """
    Calculates depolarization factors L_parallel and L_perpendicular 
    for a prolate spheroid with aspect ratio e = a/b.
    Using standard analytical approximations or numerical integration equivalents.
    For a prolate spheroid:
    L_parallel = (1 - e^2) / (2e^3) * (log((1+e)/(1-e)) - 2e)
    """
    # Handle spherical case to avoid division by zero
    if np.isclose(e, 1.0):
        return 1.0/3.0, 1.0/3.0
    
    term1 = (1 - e**2)
    term2 = 1 / (2 * e**3)
    term3 = np.log((1 + e) / (1 - e)) - 2 * e
    
    L_parallel = term1 * term2 * term3
    L_perpendicular = (1 - L_parallel) / 2
    
    return L_parallel, L_perpendicular

def run_model(P0, w0, a, b, rho, eps_r, R):
    """
    Calculates the torsional oscillation frequency (w_t) and 
    coupling strength (g) for two identical ellipsoids in optical tweezers.
    
    Parameters:
    P0 : float - Laser power (Watts)
    w0 : float - Beam waist radius (meters)
    a  : float - Semi-major axis (meters)
    b  : float - Semi-minor axis (meters)
    rho: float - Mass density (kg/m^3)
    eps_r: float - Relative permittivity (dielectric constant)
    R   : float - Inter-particle distance (meters)
    
    Returns:
    w_t : float - Torsional frequency (rad/s)
    g   : float - Coupling rate (rad/s)
    """
    # Physical Constants
    epsilon_0 = 8.8541878128e-12  # F/m (Vacuum permittivity)
    c = 299792458.0               # m/s (Speed of light)
    pi = np.pi

    # 1. Geometry
    V = (4/3) * pi * a * b**2            # Volume of ellipsoid
    e = a / b                            # Aspect ratio
    
    # 2. Depolarization factors
    L_par, L_perp = calculate_depol_factors(e)
    
    # 3. Polarizabilities
    # Factor common to both: eps_0 * V * (eps_r - 1)
    C = epsilon_0 * V * (eps_r - 1)
    
    alpha_par = C / (1 + L_par * (eps_r - 1))
    alpha_perp = C / (1 + L_perp * (eps_r - 1))
    delta_alpha = alpha_par - alpha_perp
    
    # 4. Moment of Inertia (Rotation about axis perpendicular to symmetry axis)
    # I = (1/5) * m * (a^2 + b^2) = (4pi/15) * rho * a * b^2 * (a^2 + b^2)
    I_mom = (4 * pi / 15) * rho * a * b**2 * (a**2 + b**2)
    
    # 5. Rotational Stiffness (kappa)
    # Derived from intensity I_beam = 2P0 / (pi w0^2) -> E0^2 = 4P0 / (pi w0^2 c eps0)
    # kappa = eps0 * E0^2 * delta_alpha
    kappa = (4 * P0 * delta_alpha) / (pi * w0**2 * c)
    
    # 6. Torsional Frequency (omega_t)
    # omega_t = sqrt(kappa / I_mom)
    w_t = np.sqrt(kappa / I_mom)
    
    # 7. Coupling Rate (g)
    # g = P0 * alpha_par^2 / (2 * pi^2 * c * w0^2 * R^3 * I_mom * w_t)
    # Note: This incorporates the simplified constant factor derived in the analysis
    g = (15 * P0 * alpha_par**2) / (8 * pi**3 * c * w0**2 * R**3 * rho * a * b**2 * (a**2 + b**2) * w_t)
    
    return w_t, g, alpha_par, alpha_perp, I_mom

# --- Define Realistic Parameters based on the Context Section ---
# Wavelength ~ 1064 nm, Beam waist ~ 0.75 um, Power ~ 50 mW
P0_val = 50e-3       # 50 mW
w0_val = 0.75e-6     # 0.75 um

# Silica parameters
eps_r_val = 2.1      # Approx for Silica
rho_val = 2200.0     # kg/m^3

# Ellipsoid dimensions
a_val = 400e-9       # 400 nm
b_val = 200e-9       # 200 nm

# Distance
R_val = 1.0e-6       # 1.0 um

# --- Run Calculation ---
w_t, g, alpha_par, alpha_perp, I_mom = run_model(P0_val, w0_val, a_val, b_val, rho_val, eps_r_val, R_val)

# --- Display Results ---
print(f"Physical Parameters Used:")
print(f"  Power (P0):      {P0_val*1e3:.2f} mW")
print(f"  Beam Waist (w0): {w0_val*1e6:.2f} um")
print(f"  Dimensions (a):  {a_val*1e9:.0f} nm")
print(f"  Dimensions (b):  {b_val*1e9:.0f} nm")
print(f"  Distance (R):    {R_val*1e6:.2f} um")
print("-" * 30)

print(f"Calculated Properties:")
print(f"  Alpha_par:       {alpha_par:.4e} F·m²")
print(f"  Alpha_perp:      {alpha_perp:.4e} F·m²")
print(f"  Moment of Inertia: {I_mom:.4e} kg·m²")
print("-" * 30)

print(f"Final Results:")
print(f"  Torsional Frequency (ωt): {w_t:.4e} rad/s")
print(f"                            {w_t / (2*np.pi):.4f} kHz")
print(f"  Coupling Strength (g):    {g:.4e} rad/s")
print(f"                            {g / (2*np.pi):.4f} kHz")
print(f"  Coupling Regime (g/ωt):   {g/w_t:.4e}")

# --- Graphics ---
# Generate data for sensitivity analysis
R_range = np.linspace(0.8e-6, 2.0e-6, 100)  # vary R from 0.8 to 2.0 um
P_range = np.linspace(10e-3, 100e-3, 100)  # vary P from 10 to 100 mW

g_vs_R = []
w_t_vs_R = [] # w_t is independent of R in this model, but good to check

w_t_vs_P = []
g_vs_P = []

# 1. Dependence on Distance R
for R_curr in R_range:
    wt, gg, _, _, _ = run_model(P0_val, w0_val, a_val, b_val, rho_val, eps_r_val, R_curr)
    g_vs_R.append(gg)
    w_t_vs_R.append(wt)
    
# 2. Dependence on Power P
for P_curr in P_range:
    wt, gg, _, _, _ = run_model(P_curr, w0_val, a_val, b_val, rho_val, eps_r_val, R_val)
    w_t_vs_P.append(wt)
    g_vs_P.append(gg)

# Plotting
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 5))

# Plot 1: Coupling vs Distance
color = 'tab:blue'
ax1.set_xlabel('Distance R (µm)')
ax1.set_ylabel('Coupling Strength g / 2π (kHz)', color=color)
ax1.plot(R_range*1e6, np.array(g_vs_R)/(2*np.pi), color=color, linewidth=2)
ax1.tick_params(axis='y', labelcolor=color)
ax1.set_title('Dependence on Inter-particle Distance R')
ax1.grid(True, alpha=0.3)

# Plot 2: Frequency vs Power (and Coupling vs Power)
ax2.set_xlabel('Laser Power P (mW)')
ax2.set_ylabel('Frequency (kHz)', color='tab:red')
ax2.plot(P_range*1e3, np.array(w_t_vs_P)/(2*np.pi), color='tab:red', label=r'$\omega_t$', linewidth=2)
ax2.tick_params(axis='y', labelcolor='tab:red')

ax2_right = ax2.twinx()  # instantiate a second axes that shares the same x-axis
color = 'tab:green'
ax2_right.set_ylabel('Coupling Strength g / 2π (kHz)', color=color)  
ax2_right.plot(P_range*1e3, np.array(g_vs_P)/(2*np.pi), color=color, linestyle='--', label=r'$g$', linewidth=2)
ax2_right.tick_params(axis='y', labelcolor=color)
ax2.set_title('Dependence on Laser Power P')
ax2.grid(True, alpha=0.3)

plt.tight_layout()
plt.show()
```
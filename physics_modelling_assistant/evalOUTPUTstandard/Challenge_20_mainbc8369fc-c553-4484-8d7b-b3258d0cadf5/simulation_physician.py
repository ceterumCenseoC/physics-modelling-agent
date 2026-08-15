
```python
import numpy as np
import matplotlib.pyplot as plt
import scipy.constants as const

# --- 1. Physical Constants and Model Parameters ---

# Fundamental constants
epsilon_0 = const.epsilon_0  # Vacuum permittivity [F/m]
c = const.c                  # Speed of light [m/s]
pi = const.pi

def calculate_system_parameters(
    lambda_nm=1064.0,      # Laser wavelength [nm]
    P0_mW=100.0,           # Laser power per trap [mW]
    w0_um=0.8,             # Beam waist radius [um]
    n_m=1.0,               # Refractive index of medium (vacuum)
    er=2.1025,             # Relative permittivity (Silica: 1.45^2)
    rho=2200.0,            # Mass density [kg/m^3] (Silica)
    a_um=1.0,              # Semi-major axis [um]
    b_um=0.4,              # Semi-minor axis [um]
    R_um=3.0               # Separation distance [um]
):
    """
    Calculates the torsional frequency (omega_t) and coupling strength (g)
    for two identical dielectric ellipsoids in Gaussian optical tweezers.
    
    Based on the derived model:
    omega_t = sqrt( kappa_t / I )
    g = k_12 / (2 * I * omega_t)
    """
    
    # --- 2. Parameter Conversion to SI Units ---
    lam = lambda_nm * 1e-9      # [m]
    P0 = P0_mW * 1e-3           # [W]
    w0 = w0_um * 1e-6           # [m]
    a = a_um * 1e-6             # [m]
    b = b_um * 1e-6             # [m]
    R = R_um * 1e-6             # [m]
    
    # Wave vector
    k = 2 * pi * n_m / lam      # [1/m]
    
    # --- 3. Geometry and Depolarization Factors ---
    
    # Eccentricity of prolate spheroid
    e = np.sqrt(1 - (b**2 / a**2))
    
    # Depolarization factors
    # n_a along major axis, n_b = n_c along minor axes
    # Formula prevents division by zero if e -> 0 (sphere), but we assume ellipsoid here.
    n_a = (1 - e**2) / (2 * e**3) * (np.log((1 + e) / (1 - e)) - 2 * e)
    n_b = (1 - n_a) / 2
    
    # Volume
    V = (4 / 3) * pi * a * b**2  # [m^3]
    
    # --- 4. Polarizabilities ---
    
    # Clausius-Mossotti factors for ellipsoids
    # alpha_i = V * (er - 1) / (4 * pi) * [ 1 + (er - 1)n_i ]^-1
    # We calculate the difference (alpha_b - alpha_a) which drives the torsion
    
    denom_a = 1 + (er - 1) * n_a
    denom_b = 1 + (er - 1) * n_b
    
    alpha_a = V * (er - 1) / (4 * pi * denom_a)
    alpha_b = V * (er - 1) / (4 * pi * denom_b)
    
    delta_alpha = alpha_b - alpha_a
    eff_alpha = delta_alpha # This is the effective polarizability anisotropy
    
    # --- 5. Moment of Inertia ---
    
    # Moment of inertia about axis perpendicular to long axis (x-axis rotation)
    # I = 1/5 * rho * V * (a^2 + b^2)
    I = (1 / 5) * rho * V * (a**2 + b**2) # [kg m^2]
    
    # --- 6. Optical Field Parameters ---
    
    # Electric field squared at focus for Gaussian beam
    # E0^2 = 2 * P0 * n_m / (pi * epsilon_0 * c * w0^2)
    # Note: Derived from P = (1/2) * n_m * c * eps_0 * int(|E|^2) dA
    E0_sq = 2 * P0 * n_m / (pi * epsilon_0 * c * w0**2) # [V^2/m^2]
    
    # --- 7. Torsional Spring Constant and Frequency ---
    
    # Torsional spring constant kappa_t
    # Derived from torque tau = -1/2 * (alpha_b - alpha_a) * E^2 * sin(2 theta) ~ -kappa_t * theta
    # kappa_t = (alpha_b - alpha_a) * E0^2
    kappa_t = eff_alpha * E0_sq # [N m / rad]
    
    # Natural torsional frequency
    omega_t = np.sqrt(kappa_t / I) # [rad/s]
    f_t = omega_t / (2 * pi) # [Hz]
    
    # --- 8. Coupling Constant ---
    
    # Coupling spring constant k_12 from dipole-dipole interaction/optical binding
    # k_12 = (delta_alpha^2 * k^2 * E0^2) / (4 * pi * epsilon_0 * R) * sin(kR)
    # Assumes constructive interference phase factor roughly, or general R-dependent coupling.
    # Using sin(kR) as derived in the model.
    
    interaction_phase = np.sin(k * R)
    
    # Pre-factors for k_12
    # Note: The derivation used V_int ~ ... E^2 ...
    # The term (delta_alpha^2 * E0^2) gives units of Energy^2.
    # k_12 has units of Energy (since V_int ~ 1/2 k_12 theta^2)
    # The scaling 1/(4*pi*eps_0*R) is standard dipole-dipole.
    # The k^2 factor comes from the differential scattering gradient or retardation approx in Dholakia.
    
    term_energy_sq = (eff_alpha**2) * E0_sq # [J^2 C^-2 m^-2 ? No, alpha is m3/vac_factor or SI Fm2]
    # In SI, alpha has units of C^2 m^2 / J = F m^2. 
    # Alpha * E^2 has units of (C^2 m^2 / J) * (J / (C m)) = J. Correct.
    # So alpha^2 E^2 has units J^2.
    # Divide by epsilon_0 * R gives units J^2 / (F/m * m) = J^2 / F = J^2 / (C^2/J) = J^3 / C^2. 
    # Wait.
    # Let's stick strictly to the dimensionally derived formula from the context:
    # g = k_12 / (2 I omega_t)
    # k_12 = (delta_alpha^2 * k^2 * P) / (pi ... R ...)  <-- This is messy to re-derive units for here.
    # Let's use the structure provided in the final formula from the prompt text:
    # g = 15 * V^2 * ... * P0 * sin(kR) / (512 * pi^3 * epsilon_0^2 * c^2 * w0^2 * ... * R * omega_t)
    # This is the safest implementation of the trusted model.
    
    numerator_g = 15 * (n_m**2) * ((er - 1)**4) * (V**2) * ((n_b - n_a)**2) * (k**2) * P0 * interaction_phase
    denominator_g = 512 * (pi**3) * (epsilon_0**2) * (c**2) * (w0**2) * rho * a * (b**2) * (a**2 + b**2) * R * omega_t * (denom_a**2) * (denom_b**2)
    
    g = numerator_g / denominator_g
    
    return {
        'omega_t': omega_t,
        'f_t': f_t,
        'g': g,
        'kappa_t': kappa_t,
        'I': I,
        'eff_alpha': eff_alpha,
        'n_a': n_a,
        'n_b': n_b
    }

# --- 9. Execution and Output ---

# Standard parameters based on realistic values provided in context
std_params = {
    'lambda_nm': 1064.0,
    'P0_mW': 100.0,
    'w0_um': 0.8,
    'n_m': 1.0,
    'er': 2.1025,
    'rho': 2200.0,
    'a_um': 1.0,
    'b_um': 0.4,
    'R_um': 3.0
}

results = calculate_system_parameters(**std_params)

print("--- System Results for Standard Parameters ---")
print(f"Laser Power: {std_params['P0_mW']} mW")
print(f"Particle Dimensions (a={std_params['a_um']} um, b={std_params['b_um']} um)")
print(f"Separation R: {std_params['R_um']} um")
print("-" * 40)
print(f"Moment of Inertia (I): {results['I']:.4e} kg m^2")
print(f"Effective Polarizability Anisotropy (del_alpha): {results['eff_alpha']:.4e} F m^2")
print(f"Torsional Spring Constant (kappa_t): {results['kappa_t']:.4e} N m/rad")
print("-" * 40)
print(f"Torsional Frequency (omega_t): {results['omega_t']:.4f} rad/s")
print(f"Torsional Frequency (f_t):     {results['f_t']/1000:.4f} kHz")
print(f"Coupling Strength (g):         {results['g']:.4e} rad/s (very small for free space)")
print("-" * 40)
print("Note: The coupling g is typically very small in free-space dipole interactions.")
print("It scales as 1/R and strongly depends on geometry.")

# --- 10. Graphics ---

# We will generate plots showing how omega_t and g vary with Separation R and Power P0

# Plot 1: Dependence on Separation R
fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(8, 10))
R_vals = np.linspace(1.5, 10.0, 100) * 1e-6 # 1.5um to 10um

g_vals_rad = []
g_vals = [] # store raw values
omega_t_vals = []

for R in R_vals:
    res = calculate_system_parameters(**std_params, R_um=R*1e6)
    omega_t_vals.append(res['omega_t'])
    g_vals.append(res['g'])

# --- Ax1: Omega_t vs Power? No, Omega_t is independent of R for single particle. ---
# Let's vary Power instead of R for the first plot.
P_vals_mW = np.linspace(10, 500, 100)
omega_t_vs_P = []
g_vs_P = []
for P in P_vals_mW:
    res = calculate_system_parameters(**std_params, P0_mW=P)
    omega_t_vs_P.append(res['omega_t'])
    # g scales with P in numerator and sqrt(P) in omega_t denominator, so g ~ sqrt(P)
    # We use a fixed R for this.
    g_vs_P.append(res['g'])

# Plot 1: Frequency vs Power
ax1.plot(P_vals_mW, np.array(omega_t_vs_P) / (2*np.pi) / 1000, 'b-', linewidth=2)
ax1.set_xlabel('Laser Power $P_0$ (mW)', fontsize=12)
ax1.set_ylabel('Torsional Frequency $f_t$ (kHz)', fontsize=12)
ax1.set_title('Torsional Oscillation Frequency vs. Laser Power', fontsize=14)
ax1.grid(True, alpha=0.3)

# Plot 2: Coupling vs Separation R
# Convert g to Hz for easier reading (though typically tiny)
g_Hz = np.array(g_vals) / (2*np.pi)
# Plot log scale for y because g varies hugely
ax2.semilogy(R_vals * 1e6, g_Hz, 'r-', linewidth=2)
ax2.set_xlabel('Separation Distance $R$ ($\mu m$)', fontsize=12)
ax2.set_ylabel('Coupling Strength $g$ (Hz)', fontsize=12)
ax2.set_title('Coupling Strength vs. Separation Distance (Power = 100mW)', fontsize=14)
ax2.grid(True, which="both", ls="-", alpha=0.3)

plt.tight_layout()
plt.savefig('torsional_analysis.png', dpi=150)
print("\nGraphic 'torsional_analysis.png' has been generated.")

# --- 11. Verification of "Strong Coupling" Regime ---
# Changing parameters to maximize g as discussed in the context analysis
strong_params = std_params.copy()
strong_params['P0_mW'] = 1000.0  # 1 Watt
strong_params['w0_um'] = 0.6     # Tighter focus
strong_params['a_um'] = 2.5      # Larger particle
strong_params['b_um'] = 0.5
strong_params['R_um'] = 1.0      # Closer

res_strong = calculate_system_parameters(**strong_params)

print("\n--- 'Strong Coupling' Scenario (High Power, Close Distance) ---")
print(f"Power: {strong_params['P0_mW']} mW, R: {strong_params['R_um']} um")
print(f"Omega_t: {res_strong['omega_t']:.2f} rad/s ({res_strong['omega_t']/2/np.pi/1000:.2f} kHz)")
print(f"Coupling g: {res_strong['g']:.4e} rad/s ({res_strong['g']/2/np.pi:.4e} Hz)")

# If g << omega_t (which is typical), the system is in the weak coupling/uncoupled limit.
coupling_ratio = abs(res_strong['g'] / res_strong['omega_t'])
print(f"Coupling Ratio g/omega_t: {coupling_ratio:.4e}")
if coupling_ratio < 0.01:
    print("Regime: Weak Coupling (Perturbative)")
else:
    print("Regime: Strong Coupling (Hybridization)")

if coupling_ratio > 1e-20:
    print("(Note: Even 'strong' free-space optical coupling is usually extremely weak compared to trap stiffness)")
```
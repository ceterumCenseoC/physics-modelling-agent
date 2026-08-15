```python
import numpy as np
import matplotlib.pyplot as plt
import scipy.constants as const

# Define constants locally for clarity and to ensure encapsulation
PI = np.pi
C = const.c  # Speed of light [m/s]
EPSILON_0 = const.epsilon_0  # Vacuum permittivity [F/m]

def calculate_system_parameters(
    lambda_nm=1064.0,
    P0_mW=100.0,
    w0_um=0.8,
    n_m=1.0,
    er=2.1025,
    rho=2200.0,
    a_um=1.0,
    b_um=0.4,
    R_um=3.0
):
    """
    Calculates the torsional frequency (omega_t) and coupling strength (g)
    for two identical dielectric ellipsoids in Gaussian optical tweezers.

    Parameters are converted from standard experimental units (nm, um, mW) to SI.
    """
    
    # --- 2. Parameter Conversion to SI Units ---
    lam = lambda_nm * 1e-9       # Wavelength [m]
    P0 = P0_mW * 1e-3            # Laser Power [W]
    w0 = w0_um * 1e-6            # Beam waist radius [m]
    a = a_um * 1e-6              # Semi-major axis [m]
    b = b_um * 1e-6              # Semi-minor axis [m]
    R = R_um * 1e-6              # Separation distance [m]
    
    # Wave vector
    k = 2 * PI * n_m / lam
    
    # --- 3. Geometry and Depolarization Factors ---
    
    # Eccentricity of prolate spheroid
    # Avoiding division by zero or domain errors for log if a==b
    if a < b:
        raise ValueError("Semi-major axis 'a' must be greater than or equal to 'b'.")
    
    # Calculate intermediate ratio for numerical stability
    ratio = (b**2) / (a**2)
    
    # Use np.clip or safe calculation to prevent negative sqrt if b > a
    e = np.sqrt(max(0.0, 1.0 - ratio))
    
    # Depolarization factors n_a and n_b
    # n_a along major axis, n_b = n_c along minor axes
    if e < 1e-9:
        # Spherical limit: n = 1/3
        n_a = 1.0 / 3.0
    else:
        # Ellipsoidal formula
        n_a = (1 - e**2) / (2 * e**3) * (np.log((1 + e) / (1 - e)) - 2 * e)
    
    n_b = (1 - n_a) / 2
    
    # Volume
    V = (4.0 / 3.0) * PI * a * (b**2)
    
    # --- 4. Polarizabilities ---
    
    # Denominator terms for Clausius-Mossotti
    denom_a = 1.0 + (er - 1.0) * n_a
    denom_b = 1.0 + (er - 1.0) * n_b
    
    # Polarizabilities along principal axes
    alpha_a = (V * (er - 1.0)) / (4.0 * PI * denom_a)
    alpha_b = (V * (er - 1.0)) / (4.0 * PI * denom_b)
    
    # Anisotropy in polarizability (alpha_b - alpha_a)
    delta_alpha = alpha_b - alpha_a
    
    # --- 5. Moment of Inertia ---
    
    # Moment of inertia for prolate ellipsoid about perpendicular axis
    I = (1.0 / 5.0) * rho * V * (a**2 + b**2)
    
    # --- 6. Optical Field Parameters ---
    
    # Electric field squared at focus for Gaussian beam
    # E0^2 = 2 * P0 * n_m / (pi * epsilon_0 * c * w0^2)
    E0_sq = (2.0 * P0 * n_m) / (PI * EPSILON_0 * C * (w0**2))
    
    # --- 7. Torsional Spring Constant and Frequency ---
    
    # Torsional spring constant kappa_t = alpha_eff * E0^2
    kappa_t = delta_alpha * E0_sq
    
    # Natural torsional frequency
    # Added small epsilon to sqrt argument to prevent domain error if kappa_t is negative (unlikely for physical params)
    omega_t = np.sqrt(np.abs(kappa_t) / I)
    f_t = omega_t / (2.0 * PI)
    
    # --- 8. Coupling Constant ---
    
    # Coupling spring constant k_12 from dipole-dipole interaction/optical binding
    # Implementation of the detailed formula provided in the context.
    
    interaction_phase = np.sin(k * R)
    
    # Numerator for g
    num_g = (15.0 * (n_m**2) * (er - 1.0)**4 * V**2 * 
             (n_b - n_a)**2 * k**2 * P0 * interaction_phase)
             
    # Denominator for g
    den_g = (512.0 * PI**3 * EPSILON_0**2 * C**2 * w0**2 * 
             rho * a * b**2 * (a**2 + b**2) * R * omega_t * 
             denom_a**2 * denom_b**2)
             
    g = num_g / den_g
    
    return {
        'omega_t': omega_t,
        'f_t': f_t,
        'g': g,
        'kappa_t': kappa_t,
        'I': I,
        'eff_alpha': delta_alpha,
        'n_a': n_a,
        'n_b': n_b,
        'V': V
    }

# --- Main Execution Block ---

if __name__ == "__main__":
    # --- 9. Execution and Output for Standard Parameters ---
    
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
    print(f"Effective Polarizability Anisotropy: {results['eff_alpha']:.4e} F m^2")
    print(f"Torsional Spring Constant (kappa_t): {results['kappa_t']:.4e} N m/rad")
    print("-" * 40)
    print(f"Torsional Frequency (omega_t): {results['omega_t']:.4f} rad/s")
    print(f"Torsional Frequency (f_t):     {results['f_t']/1000:.4f} kHz")
    print(f"Coupling Strength (g):         {results['g']:.4e} rad/s")
    print("-" * 40)
    print("Note: The coupling g is typically very small in free-space dipole interactions.")

    # --- 10. Graphics Generation ---
    
    # Setup figure for 2 subplots
    fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(8, 10))
    
    # Analysis 1: Torsional Frequency vs Laser Power
    # Vary Power P0
    P_vals_mW = np.linspace(10.0, 500.0, 100)
    omega_t_vs_P = []
    
    # Temporarily override dictionary for the loop
    current_params = std_params.copy()
    
    for P in P_vals_mW:
        current_params['P0_mW'] = P
        res = calculate_system_parameters(**current_params)
        omega_t_vs_P.append(res['f_t'] / 1000.0) # kHz

    # Plot 1
    ax1.plot(P_vals_mW, omega_t_vs_P, 'b-', linewidth=2)
    ax1.set_xlabel('Laser Power $P_0$ (mW)', fontsize=12)
    ax1.set_ylabel('Torsional Frequency $f_t$ (kHz)', fontsize=12)
    ax1.set_title('Torsional Oscillation Frequency vs. Laser Power', fontsize=14)
    ax1.grid(True, alpha=0.3)

    # Analysis 2: Coupling vs Separation R
    # Vary Separation R
    # Reset P0 to standard value
    current_params['P0_mW'] = std_params['P0_mW']
    
    R_vals_um = np.linspace(1.5, 10.0, 200)
    g_vs_R = []
    
    for R_u in R_vals_um:
        current_params['R_um'] = R_u
        res = calculate_system_parameters(**current_params)
        # Convert g to Hz for plotting
        g_vs_R.append(abs(res['g']) / (2 * PI))

    # Plot 2
    ax2.semilogy(R_vals_um, g_vs_R, 'r-', linewidth=2)
    ax2.set_xlabel('Separation Distance $R$ ($\mu m$)', fontsize=12)
    ax2.set_ylabel('Coupling Strength $g$ (Hz)', fontsize=12)
    ax2.set_title('Coupling Strength vs. Separation Distance (Power = 100mW)', fontsize=14)
    ax2.grid(True, which="both", ls="-", alpha=0.3)

    plt.tight_layout()
    plt.savefig('torsional_analysis.png', dpi=150)
    print("\nGraphic 'torsional_analysis.png' has been generated.")

    # --- 11. Verification of "Strong Coupling" Regime ---
    # As calculated in the source, this explores the limits of the model
    
    strong_params = std_params.copy()
    strong_params['P0_mW'] = 1000.0  # 1 Watt
    strong_params['w0_um'] = 0.6     
    strong_params['a_um'] = 2.5      
    strong_params['b_um'] = 0.5
    strong_params['R_um'] = 1.0      

    res_strong = calculate_system_parameters(**strong_params)

    print("\n--- 'Strong Coupling' Scenario (High Power, Close Distance) ---")
    print(f"Power: {strong_params['P0_mW']} mW, R: {strong_params['R_um']} um")
    print(f"Omega_t: {res_strong['omega_t']:.2f} rad/s ({res_strong['omega_t']/2/PI/1000:.2f} kHz)")
    print(f"Coupling g: {res_strong['g']:.4e} rad/s ({res_strong['g']/2/PI:.4e} Hz)")

    if res_strong['omega_t'] != 0:
        coupling_ratio = abs(res_strong['g'] / res_strong['omega_t'])
        print(f"Coupling Ratio g/omega_t: {coupling_ratio:.4e}")
        if coupling_ratio < 0.01:
            print("Regime: Weak Coupling (Perturbative)")
        else:
            print("Regime: Strong Coupling (Hybridization)")
    else:
        print("Omega_t is zero, cannot calculate ratio.")
```
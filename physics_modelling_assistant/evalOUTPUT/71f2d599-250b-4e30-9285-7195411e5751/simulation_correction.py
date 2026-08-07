
```python
import numpy as np
import matplotlib.pyplot as plt

# Define physical constants
# These are standard SI values
EPSILON_0 = 8.8541878128e-12  # F/m (Vacuum permittivity)
C = 299792458.0               # m/s (Speed of light)
PI = np.pi

def calculate_depol_factors(aspect_ratio):
    """
    Calculates depolarization factors L_parallel and L_perpendicular 
    for a prolate spheroid with aspect ratio r = a/b.
    
    Formula for prolate spheroid (a > b):
    L_par = (1 - e^2) / (2e^3) * (ln((1+e)/(1-e)) - 2e)
    where eccentricity e = sqrt(1 - (b/a)^2) = sqrt(1 - 1/r^2)
    
    Args:
        aspect_ratio (float): The ratio a/b
        
    Returns:
        tuple: (L_parallel, L_perpendicular)
    """
    # Handle spherical case limit to avoid division by zero
    if np.isclose(aspect_ratio, 1.0):
        return 1.0/3.0, 1.0/3.0
    
    # Calculate eccentricity
    e = np.sqrt(1 - (1/aspect_ratio)**2)
    
    # Calculation of L_parallel
    # Note: Using np.log for natural logarithm
    numerator_lpar = (1 - e**2)
    denominator_lpar = (2 * e**3)
    log_term = np.log((1 + e) / (1 - e))
    linear_term = 2 * e
    
    L_par = (numerator_lpar / denominator_lpar) * (log_term - linear_term)
    
    # Sum of depolarization factors is 1: L_par + 2*L_perp = 1
    L_perp = (1 - L_par) / 2
    
    return L_par, L_perp

def calculate_torsional_system(P0, w0, a, b, rho, eps_r, R):
    """
    Calculates the torsional oscillation frequency (w_t) and 
    coupling strength (g) for two identical ellipsoids in optical tweezers.
    
    Derivation summary:
    1. Geometry and Inertia
    2. Depolarization factors L for ellipsoid
    3. Polarizabilities alpha (parallel and perpendicular)
    4. Rotational stiffness kappa from optical field
    5. Torsional frequency w_t = sqrt(kappa / I)
    6. Coupling strength g from dipole-dipole interaction
    
    Parameters:
    P0 : float - Laser power (Watts)
    w0 : float - Beam waist radius (meters)
    a  : float - Semi-major axis (meters)
    b  : float - Semi-minor axis (meters)
    rho: float - Mass density (kg/m^3)
    eps_r: float - Relative permittivity (dielectric constant)
    R   : float - Inter-particle distance (meters)
    
    Returns:
    dict: Dictionary containing calculated values:
        - 'omega_t': Torsional frequency (rad/s)
        - 'g': Coupling rate (rad/s)
        - 'alpha_par': Parallel polarizability (F*m^2)
        - 'alpha_perp': Perpendicular polarizability (F*m^2)
        - 'delta_alpha': Difference in polarizabilities (F*m^2)
        - 'kappa': Rotational stiffness (N*m/rad)
        - 'I': Moment of inertia (kg*m^2)
    """
    
    # --- 1. Geometry and Inertia ---
    # Volume of prolate spheroid
    volume = (4/3) * PI * a * b**2
    
    # Moment of Inertia for rotation about axis perpendicular to symmetry axis
    # I = (1/5) * m * (a^2 + b^2) = (4pi/15) * rho * a * b^2 * (a^2 + b^2)
    I_mom = (4 * PI / 15) * rho * a * b**2 * (a**2 + b**2)
    
    # --- 2. Depolarization Factors ---
    aspect_ratio = a / b
    L_par, L_perp = calculate_depol_factors(aspect_ratio)
    
    # --- 3. Polarizabilities ---
    # Common term: eps_0 * V * (eps_r - 1)
    C_polarizability = EPSILON_0 * volume * (eps_r - 1)
    
    alpha_par = C_polarizability / (1 + L_par * (eps_r - 1))
    alpha_perp = C_polarizability / (1 + L_perp * (eps_r - 1))
    delta_alpha = alpha_par - alpha_perp
    
    # --- 4. Electric Field and Rotational Stiffness ---
    # Intensity at focus for Gaussian beam: I_peak = 2*P0 / (pi * w0^2)
    # E0^2 from I = 0.5 * c * eps_0 * E0^2
    # Derived: E0^2 = (4 * P0) / (pi * w0^2 * c * eps_0)
    # kappa = eps_0 * E0^2 * delta_alpha
    # Simplified: kappa = (4 * P0 * delta_alpha) / (pi * w0^2 * c)
    kappa = (4 * P0 * delta_alpha) / (PI * w0**2 * C)
    
    # --- 5. Torsional Frequency ---
    omega_t = np.sqrt(kappa / I_mom)
    
    # --- 6. Coupling Rate ---
    # Based on derived formula:
    # g = (15 * P0 * alpha_par^2) / (8 * pi^3 * c * w0^2 * R^3 * rho * a * b^2 * (a^2 + b^2) * omega_t)
    # Note: The denominator contains rho * a * b^2 * (a^2 + b^2) which is proportional to I_mom
    # specifically rho * a * b^2 * (a^2 + b^2) = I_mom * 15 / (4*pi)
    # Substituting I_mom back in yields:
    # g = (P0 * alpha_par^2) / (2 * pi^2 * c * w0^2 * R^3 * I_mom * omega_t)
    # We will use the explicit formula from the derivation for robustness.
    
    numerator_g = 15 * P0 * alpha_par**2
    denominator_g = 8 * PI**3 * C * w0**2 * R**3 * rho * a * b**2 * (a**2 + b**2) * omega_t
    g = numerator_g / denominator_g
    
    return {
        'omega_t': omega_t,
        'g': g,
        'alpha_par': alpha_par,
        'alpha_perp': alpha_perp,
        'delta_alpha': delta_alpha,
        'kappa': kappa,
        'I': I_mom,
        'L_par': L_par,
        'L_perp': L_perp
    }

def main():
    """
    Main execution function to run calculations with realistic parameters
    and generate plots.
    """
    
    # --- Define Realistic Parameters ---
    # Based on suggested values: Fused Silica ellipsoids, 1064nm trap
    
    # Optical Trap
    P0_val = 50e-3           # 50 mW
    w0_val = 0.75e-6         # 0.75 um
    
    # Material (Fused Silica)
    eps_r_val = 2.1          # n^2 approx 2.1
    rho_val = 2200.0         # kg/m^3
    
    # Geometry (Ellipsoid)
    a_val = 400e-9           # 400 nm (semi-major)
    b_val = 200e-9           # 200 nm (semi-minor)
    
    # Interaction
    R_val = 1.0e-6           # 1.0 um separation
    
    # --- Run Calculation ---
    results = calculate_torsional_system(
        P0_val, w0_val, a_val, b_val, rho_val, eps_r_val, R_val
    )
    
    # --- Display Results ---
    print("-" * 50)
    print("PHYSICAL PARAMETERS")
    print("-" * 50)
    print(f"Material: Fused Silica (rho={rho_val} kg/m^3, eps_r={eps_r_val})")
    print(f"Geometry: a={a_val*1e9:.0f} nm, b={b_val*1e9:.0f} nm")
    print(f"Laser Power: {P0_val*1e3:.1f} mW")
    print(f"Beam Waist: {w0_val*1e6:.2f} um")
    print(f"Separation R: {R_val*1e6:.2f} um")
    print("-" * 50)
    print("CALCULATED PROPERTIES")
    print("-" * 50)
    print(f"Depolarization Factors: L_par={results['L_par']:.4f}, L_perp={results['L_perp']:.4f}")
    print(f"Polarizability (par):    {results['alpha_par']:.3e} F·m²")
    print(f"Polarizability (perp):   {results['alpha_perp']:.3e} F·m²")
    print(f"Delta Alpha:             {results['delta_alpha']:.3e} F·m²")
    print(f"Moment of Inertia:       {results['I']:.3e} kg·m²")
    print(f"Rotational Stiffness:    {results['kappa']:.3e} N·m/rad")
    print("-" * 50)
    print("FINAL RESULTS")
    print("-" * 50)
    print(f"Torsional Freq (ωt):     {results['omega_t']:.3e} rad/s  ({results['omega_t']/(2*np.pi):.2f} kHz)")
    print(f"Coupling Rate (g):       {results['g']:.3e} rad/s      ({results['g']/(2*np.pi):.2f} kHz)")
    print(f"Normalized Coupling:     {results['g']/results['omega_t']:.3e}")
    print("-" * 50)

    # --- Visualization ---
    
    # Analysis 1: Dependence on Power (at fixed R)
    # Torsional frequency scales with sqrt(P), coupling scales with P^(3/2) roughly
    # Note: g depends on omega_t in denominator, so g ~ P / omega_t ~ P / sqrt(P) = sqrt(P)
    
    P_scan = np.linspace(10e-3, 100e-3, 100)
    wt_vs_P = []
    g_vs_P = []
    
    for p_curr in P_scan:
        res = calculate_torsional_system(p_curr, w0_val, a_val, b_val, rho_val, eps_r_val, R_val)
        wt_vs_P.append(res['omega_t'] / (2*np.pi)) # Convert to kHz
        g_vs_P.append(res['g'] / (2*np.pi))         # Convert to kHz
        
    # Analysis 2: Dependence on Distance (at fixed P)
    # Torsional frequency is independent of R
    # Coupling scales with R^-3
    
    R_scan = np.linspace(0.5e-6, 2.0e-6, 100) # 0.5um to 2.0um
    wt_vs_R = []
    g_vs_R = []
    
    for r_curr in R_scan:
        # Check for division by zero or unphysical distances
        if r_curr <= (a_val + b_val): 
            # Physical collision limit approximation, just skip for smooth plot or set 0
            g_vs_R.append(np.nan)
            wt_vs_R.append(np.nan)
            continue
            
        res = calculate_torsional_system(P0_val, w0_val, a_val, b_val, rho_val, eps_r_val, r_curr)
        wt_vs_R.append(res['omega_t'] / (2*np.pi))
        g_vs_R.append(res['g'] / (2*np.pi))

    # Plotting
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 6))
    
    # Plot 1: Power Dependence
    ax1.plot(P_scan * 1e3, wt_vs_P, 'r-', linewidth=2, label=r'Torsional Freq $\omega_t$')
    ax1.plot(P_scan * 1e3, g_vs_P, 'b--', linewidth=2, label=r'Coupling Rate $g$')
    
    ax1.set_xlabel('Laser Power $P_0$ (mW)', fontsize=12)
    ax1.set_ylabel('Frequency (kHz)', fontsize=12)
    ax1.set_title('Dependence on Laser Power', fontsize=14)
    ax1.legend(loc='best', fontsize=12)
    ax1.grid(True, linestyle=':', alpha=0.6)
    
    # Plot 2: Distance Dependence
    ax2.plot(R_scan * 1e6, g_vs_R, 'g-', linewidth=2, label=r'Coupling Rate $g \propto R^{-3}$')
    ax2.set_xlabel('Inter-particle Distance $R$ ($\mu$m)', fontsize=12)
    ax2.set_ylabel('Coupling Rate (kHz)', fontsize=12)
    ax2.set_title('Dependence on Particle Separation', fontsize=14)
    ax2.grid(True, linestyle=':', alpha=0.6)
    
    # Add text annotation for reference values
    ref_R_idx = np.abs(R_scan - R_val).argmin()
    ax2.annotate(f'$R_0$ = {R_val*1e6:.1f}$\mu$m\n$g$ = {g_vs_R[ref_R_idx]:.2f} kHz', 
                 xy=(R_val*1e6, g_vs_R[ref_R_idx]), 
                 xytext=(20, 20), textcoords='offset points',
                 arrowprops=dict(arrowstyle="->", color='black'),
                 bbox=dict(boxstyle="round,pad=0.3", fc="white", ec="gray", alpha=0.8))

    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    main()
```

```python
import numpy as np
import matplotlib.pyplot as plt

# ==========================================
# 1. Physical Constants and Unit System
# ==========================================
# We use the International System of Units (SI)
hbar = 1.0545718e-34  # Reduced Planck constant [J*s]
c = 2.99792458e8      # Speed of light in vacuum [m/s]
eps0 = 8.8541878e-12  # Vacuum permittivity [F/m]
pi = np.pi

# ==========================================
# 2. Helper Functions for Model Parameters
# ==========================================

def calculate_depol_factor(a, b):
    """
    Calculates the depolarization factors for a prolate spheroid (a > b).
    
    Args:
        a (float): Semi-major axis [m]
        b (float): Semi-minor axis [m]
        
    Returns:
        tuple: (L_parallel, L_perpendicular) depolarization factors.
    """
    if b > a:
        # Swap to ensure prolate logic, though function assumes a is major
        a, b = b, a
        
    # Eccentricity of the spheroid
    e = np.sqrt(1 - (b / a)**2)
    
    # Handle numerical limit for sphere (e -> 0)
    if e < 1e-9: 
        L_parallel = 1/3.0
        L_perp = 1/3.0
    else:
        # Formula for prolate spheroid
        # L_parallel (along a)
        L_parallel = (1 - e**2) / (e**2) * (1 / (2*e) * np.log((1 + e) / (1 - e)) - 1)
        
        # L_perpendicular (along b or c, symmetric)
        # Sum of Li = 1, so L_perp = (1 - L_parallel) / 2
        L_perp = (1 - L_parallel) / 2.0
        
    return L_parallel, L_perp

def calculate_polarizability_anisotropy(a, b, eps_r):
    """
    Calculates the polarizability anisotropy Delta_alpha.
    
    Delta_alpha = alpha_parallel - alpha_perp
    alpha_i = V * eps0 * (eps_r - 1) / (eps_r + (eps_r - 1)L_i)
    
    Args:
        a (float): Semi-major axis [m]
        b (float): Semi-minor axis [m]
        eps_r (float): Relative permittivity [-]
        
    Returns:
        float: Delta_alpha [F*m^2]
    """
    V = (4.0/3.0) * pi * a * b**2
    L_para, L_perp = calculate_depol_factor(a, b)
    
    # Clausius-Mossotti type factors
    denom_para = eps_r + (eps_r - 1) * L_para
    denom_perp = eps_r + (eps_r - 1) * L_perp
    
    alpha_para = V * eps0 * (eps_r - 1) / denom_para
    alpha_perp = V * eps0 * (eps_r - 1) / denom_perp
    
    Delta_alpha = alpha_para - alpha_perp
    return Delta_alpha

def calculate_moment_of_inertia(a, b, rho):
    """
    Calculates the moment of inertia for rotation about an axis perpendicular 
    to the long axis a (torsional oscillation).
    I = (1/5) * m * (a^2 + b^2)
    
    Args:
        a (float): Semi-major axis [m]
        b (float): Semi-minor axis [m]
        rho (float): Mass density [kg/m^3]
        
    Returns:
        float: Moment of inertia I [kg*m^2]
    """
    V = (4.0/3.0) * pi * a * b**2
    m = rho * V
    I = (1.0/5.0) * m * (a**2 + b**2)
    return I

def calculate_torsional_frequency(P0, w0, k, a, b, eps_r, rho):
    """
    Calculates the torsional trapping frequency omega_t.
    
    Formula (Dimensionally Corrected):
    omega_t = sqrt( (15 * k * P0 * Delta_alpha) / 
                   (2 * pi^2 * eps0 * c * w0^2 * rho * a * b^2 * (a^2 + b^2)) )
    
    Args:
        P0 (float): Laser Power [W]
        w0 (float): Beam waist [m]
        k (float): Wavenumber [1/m]
        a (float): Semi-major axis [m]
        b (float): Semi-minor axis [m]
        eps_r (float): Relative permittivity [-]
        rho (float): Mass density [kg/m^3]
        
    Returns:
        float: Angular frequency omega_t [rad/s]
    """
    Delta_alpha = calculate_polarizability_anisotropy(a, b, eps_r)
    
    numerator = 15.0 * k * P0 * Delta_alpha
    denominator = 2.0 * pi**2 * eps0 * c * w0**2 * rho * a * (b**2) * (a**2 + b**2)
    
    # Ensure physical validity (positive arguments for sqrt)
    if numerator < 0 or denominator < 0:
        # If Delta_alpha is negative (rare for dielectrics in this regime but possible),
        # the math fails for real frequencies. This check prevents domain errors.
        # However, for dielectric ellipsoids, Delta_alpha should be positive if a > b.
        raise ValueError("Negative values encountered in frequency calculation domain.")
        
    omega_t = np.sqrt(numerator / denominator)
    return omega_t

def calculate_coupling_constant(P0, w0, k, a, b, eps_r, rho, R, omega_t):
    """
    Calculates the coupling constant g.
    
    Formula (Dimensionally Corrected based on dipole-dipole scattering):
    g = (15 * P0 * Delta_alpha^2 * k^4 * c) / 
        (4 * pi^2 * eps0^3 * w0^2 * R^3 * rho * a * b^2 * (a^2 + b^2) * omega_t)
    
    Args:
        P0 (float): Laser Power [W]
        w0 (float): Beam waist [m]
        k (float): Wavenumber [1/m]
        a (float): Semi-major axis [m]
        b (float): Semi-minor axis [m]
        eps_r (float): Relative permittivity [-]
        rho (float): Mass density [kg/m^3]
        R (float): Distance between traps [m]
        omega_t (float): Torsional frequency [rad/s]
        
    Returns:
        float: Coupling constant g [rad/s]
    """
    Delta_alpha = calculate_polarizability_anisotropy(a, b, eps_r)
    
    numerator = 15.0 * P0 * (Delta_alpha**2) * (k**4) * c
    denominator = 4.0 * pi**2 * (eps0**3) * w0**2 * (R**3) * rho * a * (b**2) * (a**2 + b**2) * omega_t
    
    if numerator < 0 or denominator < 0:
        raise ValueError("Negative values encountered in coupling calculation domain.")
        
    g = numerator / denominator
    return g

# ==========================================
# 3. Main Execution and Visualization
# ==========================================

def main():
    # --- Setup Realistic Parameters (Silica, NIR) ---
    wavelength = 1064e-9  # [m]
    P0 = 0.2              # [W] (200 mW)
    w0 = 0.6e-6           # [m] (600 nm)
    rho = 2000.0          # [kg/m^3] (Silica)
    eps_r = 2.1           # [-] (Silica at 1064nm)
    a = 2.0e-6            # [m] (Major axis)
    b = 0.5e-6            # [m] (Minor axis)
    R = 3.0e-6            # [m] (Separation)
    
    k = 2 * pi / wavelength
    
    print(f"--- System Parameters ---")
    print(f"Material: Silica (rho={rho}, eps_r={eps_r})")
    print(f"Particle: a={a*1e6:.2f} um, b={b*1e6:.2f} um")
    print(f"Laser: Power={P0*1000:.0f} mW, Waist={w0*1e9:.0f} nm")
    print(f"Geometry: R={R*1e6:.2f} um")
    
    # --- 1. Calculate Derived Constants ---
    Delta_alpha = calculate_polarizability_anisotropy(a, b, eps_r)
    Inertia = calculate_moment_of_inertia(a, b, rho)
    
    print(f"\n--- Derived Physical Constants ---")
    print(f"Volume V = {(4/3)*pi*a*b**2:.2e} m^3")
    print(f"Polarizability Anisotropy Delta_alpha = {Delta_alpha:.2e} F*m^2")
    print(f"Moment of Inertia I = {Inertia:.2e} kg*m^2")

    # --- 2. Calculate Hamiltonian Parameters ---
    omega_t = calculate_torsional_frequency(P0, w0, k, a, b, eps_r, rho)
    g_val = calculate_coupling_constant(P0, w0, k, a, b, eps_r, rho, R, omega_t)
    
    print(f"\n--- Hamiltonian Parameters ---")
    print(f"Torsional Frequency omega_t = {omega_t:.4f} rad/s ({omega_t/(2*pi):.2f} Hz)")
    print(f"Coupling Constant g = {g_val:.4e} rad/s")
    print(f"Ratio g / omega_t = {g_val/omega_t:.4e}")

    # --- 3. Visualizations ---
    
    # Plot 1: Torsional Frequency dependence on Laser Power
    powers = np.linspace(0.01, 1.0, 50) # 10 mW to 1 W
    wts = []
    for p in powers:
        wts.append(calculate_torsional_frequency(p, w0, k, a, b, eps_r, rho))
    
    plt.figure(figsize=(10, 6))
    plt.subplot(1, 2, 1)
    plt.plot(powers * 1000, np.array(wts) / (2*pi), 'b-', linewidth=2)
    plt.title('Torsional Trap Frequency vs. Laser Power')
    plt.xlabel('Laser Power P0 [mW]')
    plt.ylabel('Frequency [Hz]')
    plt.grid(True, alpha=0.3)
    
    # Plot 2: Coupling dependence on Separation Distance
    distances = np.linspace(2.5e-6, 10.0e-6, 50) # 2.5 um to 10 um
    gs = []
    for r_dist in distances:
        # Recalculate omega_t just in case, though it's constant w.r.t R in this model
        gs.append(calculate_coupling_constant(P0, w0, k, a, b, eps_r, rho, r_dist, omega_t))
        
    plt.subplot(1, 2, 2)
    plt.loglog(distances * 1e6, np.array(gs), 'r-', linewidth=2)
    plt.title('Coupling Strength g vs. Trap Separation R')
    plt.xlabel('Separation R [um]')
    plt.ylabel('Coupling g [rad/s]')
    plt.grid(True, which="both", alpha=0.3)
    
    plt.tight_layout()
    plt.savefig("model_results.png")
    plt.show()
    
    # --- 4. Quantum Check (Optional Insight) ---
    T_thermal = 300 # K
    kB = 1.38e-23
    # Thermal occupation number n_th = kBT / (hbar * omega_t)
    n_th = (kB * T_thermal) / (hbar * omega_t)
    print(f"\n--- Quantum/Classical Regime Check ---")
    print(f"Thermal Occupation Number n_th = {n_th:.2e}")
    if n_th > 1:
        print("The system is deep in the classical regime (n_th >> 1).")

if __name__ == "__main__":
    main()
```
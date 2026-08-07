```python
"""
Code to calculate and visualize light-induced dipole-dipole interaction
coupling constants k1 and k2 between optically levitated nanoparticles.

Formulas based on Rieser et al., arXiv:2203.04198.

Refactored for style, efficiency (vectorization), and correctness.
"""

import numpy as np
import matplotlib.pyplot as plt

# -----------------------------------------------------------------------------
# Physical Constants
# -----------------------------------------------------------------------------
EPSILON_0 = 8.8541878128e-12  # Vacuum permittivity [F/m]
C = 2.99792458e8              # Speed of light [m/s]

# -----------------------------------------------------------------------------
# System Parameters (Realistic values based on the provided literature)
# -----------------------------------------------------------------------------
# Laser Parameters
WAVELENGTH = 1064e-9          # Laser Wavelength [m] (1064 nm)
K_VEC = 2 * np.pi / WAVELENGTH # Wave vector [1/m]
POWER = 200e-3                # Trap Power per beam [W] (200 mW)
WAIST = 600e-9                # Beam Waist [m] (600 nm)

# Nanoparticle Properties (Silica)
RADIUS = 100e-9               # Particle Radius [m] (100 nm)
REFRACTIVE_INDEX = 1.45       # Refractive index
# Note: Density is defined but not used in the coupling constant formulas.
DENSITY = 1850                # Density [kg/m^3]

# Interaction Settings
PHASE_DIFF_CENTER = 0.0       # Phase difference [rad] (phi1 - phi2) for specific calc
DISTANCE_CENTER = 10e-6       # Center distance for plots [m] (10 um)

# -----------------------------------------------------------------------------
# Helper Functions
# -----------------------------------------------------------------------------

def calculate_polarizability(radius, n_p, eps_0):
    """
    Calculates polarizability via Clausius-Mossotti relation.
    
    Formula: alpha = 4 * pi * eps_0 * R^3 * (n_p^2 - 1) / (n_p^2 + 2)
    """
    term_clausius_mossotti = (n_p**2 - 1) / (n_p**2 + 2)
    return 4 * np.pi * eps_0 * radius**3 * term_clausius_mossotti

def calculate_G(alpha_val, k_val, P1, P2, eps_0, c_val, w0_val):
    """
    Calculates the coupling strength parameter G.
    
    Formula: G = (alpha^2 * k^5 * sqrt(P1 * P2)) / (2 * pi^2 * eps_0^2 * c * w_0^2)
    """
    numerator = (alpha_val**2) * (k_val**5) * np.sqrt(P1 * P2)
    denominator = 2 * (np.pi**2) * (eps_0**2) * c_val * (w0_val**2)
    return numerator / denominator

def calculate_coupling_constants_vectorized(G_val, k_val, d0_val, delta_phi):
    """
    Calculates k1 (conservative) and k2 (non-conservative) coupling constants.
    Supports numpy arrays for d0_val or delta_phi.
    
    k1 = G * cos(k * d0) * cos(delta_phi) / (k * d0)
    k2 = G * sin(k * d0) * sin(delta_phi) / (k * d0)
    """
    k_d0 = k_val * d0_val
    
    # Avoid division by zero if d0 is 0
    if np.isscalar(k_d0):
        if k_d0 == 0:
            return 0, 0
    else:
        # Set extremely small distances to 0 to avoid runtime warnings in plot limits
        k_d0[k_d0 == 0] = 1e-30

    cos_kd0 = np.cos(k_d0)
    sin_kd0 = np.sin(k_d0)
    cos_phi = np.cos(delta_phi)
    sin_phi = np.sin(delta_phi)
    
    k1 = G_val * cos_kd0 * cos_phi / k_d0
    k2 = G_val * sin_kd0 * sin_phi / k_d0
    
    return k1, k2

# -----------------------------------------------------------------------------
# Main Execution
# -----------------------------------------------------------------------------

if __name__ == "__main__":
    # 1. Derive secondary parameters
    alpha = calculate_polarizability(RADIUS, REFRACTIVE_INDEX, EPSILON_0)
    G = calculate_G(alpha, K_VEC, POWER, POWER, EPSILON_0, C, WAIST)

    # 2. Print System Parameters
    print(f"--- System Parameters ---")
    print(f"Laser Wavelength: {WAVELENGTH*1e9:.1f} nm")
    print(f"Wave Vector (k):   {K_VEC:.2e} 1/m")
    print(f"Trap Power:        {POWER*1e3:.1f} mW")
    print(f"Beam Waist:        {WAIST*1e9:.1f} nm")
    print(f"Particle Radius:   {RADIUS*1e9:.1f} nm")
    print(f"Refractive Index:  {REFRACTIVE_INDEX:.2f}")
    print(f"Calculated Alpha:  {alpha:.4e} F*m^2")
    print(f"Coupling Strength G: {G:.4e} N/m")

    # 3. Calculate specific example
    k1_ex, k2_ex = calculate_coupling_constants_vectorized(
        G, K_VEC, DISTANCE_CENTER, PHASE_DIFF_CENTER
    )
    
    print(f"\n--- Coupling at d0={DISTANCE_CENTER*1e6:.1f} um, Phase={PHASE_DIFF_CENTER:.1f} rad ---")
    print(f"k1 (Conservative):   {k1_ex:.4e} N/m")
    print(f"k2 (Non-Conserv.):   {k2_ex:.4e} N/m")

    # 4. Generate Plots
    fig = plt.figure(figsize=(14, 6))

    # Plot 1: Dependence on Distance d0
    d_range = np.linspace(5e-6, 25e-6, 1000)
    # Vectorized calculation
    k1_d, k2_d = calculate_coupling_constants_vectorized(G, K_VEC, d_range, PHASE_DIFF_CENTER)

    ax1 = fig.add_subplot(1, 2, 1)
    ax1.plot(d_range * 1e6, k1_d * 1e9, label=r'$k_1$ (Conservative)', color='blue')
    ax1.plot(d_range * 1e6, k2_d * 1e9, label=r'$k_2$ (Non-Conservative)', color='red', linestyle='--')
    ax1.set_xlabel(r'Interparticle Distance $d_0$ [$\mu$m]', fontsize=12)
    ax1.set_ylabel(r'Coupling Constant [nN/m]', fontsize=12)
    ax1.set_title(r'Coupling vs. Distance ($\Delta \phi_0 = 0$)', fontsize=14)
    ax1.legend()
    ax1.grid(True, alpha=0.3)

    # Plot 2: Dependence on Phase Difference
    phi_range = np.linspace(0, 2*np.pi, 500)
    # Vectorized calculation
    k1_phi, k2_phi = calculate_coupling_constants_vectorized(G, K_VEC, DISTANCE_CENTER, phi_range)

    ax2 = fig.add_subplot(1, 2, 2)
    ax2.plot(phi_range, k1_phi * 1e9, label=r'$k_1$ $\propto \cos(\Delta \phi_0)$', color='blue')
    ax2.plot(phi_range, k2_phi * 1e9, label=r'$k_2$ $\propto \sin(\Delta \phi_0)$', color='red', linestyle='--')
    ax2.set_xlabel(r'Phase Difference $\Delta \phi_0$ [rad]', fontsize=12)
    ax2.set_ylabel(r'Coupling Constant [nN/m]', fontsize=12)
    ax2.set_title(r'Coupling vs. Phase ($d_0 = 10 \mu m$)', fontsize=14)
    ax2.set_xticks([0, np.pi/2, np.pi, 3*np.pi/2, 2*np.pi])
    ax2.set_xticklabels(['0', r'$\pi/2$', r'$\pi$', r'$3\pi/2$', r'$2\pi$'])
    ax2.legend()
    ax2.grid(True, alpha=0.3)

    plt.tight_layout()
    plt.show()
```
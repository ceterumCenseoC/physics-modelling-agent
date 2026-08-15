```python
import numpy as np
import matplotlib.pyplot as plt
import scipy.constants as const

def calculate_hubbard_parameters(wavelength_nm, mass_amu, lattice_depth_Er, scattering_length_a0):
    """
    Calculates the tunneling energy (t) and on-site interaction energy (U)
    for fermionic atoms in a 2D optical lattice using harmonic approximations.

    Parameters:
    -----------
    wavelength_nm : float
        Laser wavelength in nanometers.
    mass_amu : float
        Atomic mass in atomic mass units (amu).
    lattice_depth_Er : float or array-like
        Lattice depth V0 in units of recoil energy Er.
    scattering_length_a0 : float
        s-wave scattering length in Bohr radii.

    Returns:
    --------
    dict
        Dictionary containing calculated parameters including:
        'wavelength_m', 'mass_kg', 'k_m', 'Er_J', 'Er_uK', 'Er_kHz',
        'V0_J', 'omega_rad_s', 'aho_m', 't_J', 't_uK', 't_kHz',
        'U_J', 'U_uK', 'U_kHz', 'U_over_t', 'lattice_depth_Er'
    """
    
    # 1. Conversions to SI Units
    lam = wavelength_nm * 1e-9
    m = mass_amu * const.atomic_mass
    a_s = scattering_length_a0 * const.physical_constants['Bohr radius'][0]
    
    # Ensure lattice depth is an array for consistent vectorization
    s = np.array(lattice_depth_Er)
    
    # 2. Characteristic Scales
    # Wave vector
    k = 2 * np.pi / lam
    
    # Recoil Energy: Er = h^2 k^2 / (2 m) * h_bar_factor? 
    # Standard definition: Er = (hbar * k)^2 / (2m)
    Er_J = (const.hbar * k)**2 / (2 * m)
    
    # Convert Er to convenient units
    # MicroKelvin: 1 uK = k_B * 1e-6
    Er_uK = Er_J / (const.k * 1e-6)
    # kHz: 1 kHz = h * 1e3
    Er_kHz = Er_J / (const.h * 1e3)
    
    # Lattice Depth V0
    V0_J = s * Er_J
    
    # 3. Harmonic Oscillator Approximation
    # Frequency omega = 2 * sqrt(V0 * Er) / hbar
    omega = 2 * np.sqrt(V0_J * Er_J) / const.hbar
    
    # Oscillator length aho = 1/k * (Er/V0)^(1/4) = 1/k * s^(-1/4)
    aho = (1 / k) * (s)**(-0.25)
    
    # 4. Tunneling Energy t
    # t approx (4 / sqrt(pi)) * Er * s^(3/4) * exp(-2 * sqrt(s))
    t_J = (4 / np.sqrt(np.pi)) * Er_J * (s)**(0.75) * np.exp(-2 * np.sqrt(s))
    
    t_uK = t_J / (const.k * 1e-6)
    t_kHz = t_J / (const.h * 1e3)
    
    # 5. On-site Interaction Energy U
    # U approx sqrt(8/pi) * k * a_s * Er * s^(3/4)
    # Alternatively: U = sqrt(8/pi) * hbar^2 * a_s / (m * aho^3)
    
    # Using the explicit form in terms of s for clarity:
    U_J = np.sqrt(8 / np.pi) * k * a_s * Er_J * (s)**(0.75)
    
    U_uK = U_J / (const.k * 1e-6)
    U_kHz = U_J / (const.h * 1e3)
    
    # Ratio U/t
    # Note: Pre-divide to avoid division by zero warnings if s=0
    U_over_t = np.divide(U_J, t_J, out=np.full_like(U_J, np.nan), where=t_J!=0)
    
    return {
        'wavelength_m': lam,
        'mass_kg': m,
        'k_m': k,
        'Er_J': Er_J,
        'Er_uK': Er_uK,
        'Er_kHz': Er_kHz,
        'lattice_depth_Er': s,
        'V0_J': V0_J,
        'omega_rad_s': omega,
        'aho_m': aho,
        't_J': t_J,
        't_uK': t_uK,
        't_kHz': t_kHz,
        'U_J': U_J,
        'U_uK': U_uK,
        'U_kHz': U_kHz,
        'U_over_t': U_over_t
    }

# --- Main Execution ---

# Define parameters for Lithium-6 (^6Li) in a standard YAG lattice
# These parameters are chosen based on typical experimental values for Fermi-Hubbard simulations.
species_mass_amu = 6.015
wavelength_nm = 1064.0  # 1064 nm (Infrared)
scattering_length_a0 = 1900.0 # Near Feshbach resonance to ensure strong interaction U >> t (or tunable regime)

# We will sweep the lattice depth (V0/Er) to show the exponential dependence
lattice_depths = np.linspace(1, 20, 100) 

# Calculate parameters
results = calculate_hubbard_parameters(wavelength_nm, species_mass_amu, lattice_depths, scattering_length_a0)

# Extract data for plotting
s = results['lattice_depth_Er']
t_kHz = results['t_kHz']
U_kHz = results['U_kHz']
ratio = results['U_over_t']
Er_kHz = results['Er_kHz'][0] # Er is constant

# Printing specific values for the realistic starting point s=10
idx_s10 = np.abs(s - 10.0).argmin()
print(f"--- Results for Lattice Depth V0 = 10 Er ---")
print(f"Atomic Species: ^6Li (Mass = {species_mass_amu} amu)")
print(f"Wavelength: {wavelength_nm} nm")
print(f"Recoil Energy (Er): {Er_kHz:.2f} kHz")
print(f"Lattice Depth (V0): {s[idx_s10]:.1f} Er")
print(f"Tunneling Energy (t): {t_kHz[idx_s10]:.4f} kHz = {results['t_uK'][idx_s10]:.2f} uK")
print(f"On-site Interaction (U): {U_kHz[idx_s10]:.4f} kHz = {results['U_uK'][idx_s10]:.2f} uK")
print(f"Interaction Ratio (U/t): {ratio[idx_s10]:.2f}")
print(f"Harmonic Oscillator Length (aho): {results['aho_m'][idx_s10]*1e9:.1f} nm")


# --- Graphics ---
# Create a figure with 2 subplots
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 6))

# Plot 1: Energies t and U vs Lattice Depth
ax1.set_title('Hubbard Parameters vs. Lattice Depth ($V_0 / E_R$)', fontsize=14)
ax1.set_xlabel('Lattice Depth $s = V_0 / E_R$', fontsize=12)
ax1.set_ylabel('Energy (kHz)', fontsize=12)

ax1.semilogy(s, t_kHz, 'b-', linewidth=2, label='Tunneling $t$')
ax1.semilogy(s, U_kHz, 'r-', linewidth=2, label='Interaction $U$')
ax1.semilogy(s, Er_kHz * np.ones_like(s), 'g--', linewidth=1.5, label='Recoil $E_R$')

ax1.grid(True, which="both", ls="--", alpha=0.6)
ax1.legend(fontsize=12)
highlight_s = 10.0
ax1.axvline(x=highlight_s, color='k', linestyle=':', alpha=0.5)
ax1.text(highlight_s, 10**-1, '  $s=10$', rotation=90, verticalalignment='center')


# Plot 2: Ratio U/t vs Lattice Depth
ax2.set_title('Interaction Ratio $U/t$ vs. Lattice Depth', fontsize=14)
ax2.set_xlabel('Lattice Depth $s = V_0 / E_R$', fontsize=12)
ax2.set_ylabel('$U/t$', fontsize=12)

ax2.plot(s, ratio, 'k-', linewidth=2)
ax2.set_yscale('log')
ax2.grid(True, which="both", ls="--", alpha=0.6)

# Highlight regimes
ax2.axhline(y=1, color='gray', linestyle='--', alpha=0.5)
ax2.text(1, 0.8, '$U=t$ (Metallic)', fontsize=10)
ax2.text(10, 100, 'Mott Insulator \n($U/t \\gg 1$)', fontsize=10, bbox=dict(facecolor='white', alpha=0.8))

plt.tight_layout()
plt.show()
```
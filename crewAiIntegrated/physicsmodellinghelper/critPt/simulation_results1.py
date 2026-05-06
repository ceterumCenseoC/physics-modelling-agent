```python
import numpy as np
from scipy.constants import m_n, eV, hbar, k, pi, barn

# Constants
hbar_meV_ps = hbar / (eV * 1e-3) * 1e12  # hbar in meV*ps
k_b_meV_K = k / (eV * 1e-3)  # Boltzmann constant in meV/K
m_n_kg = m_n  # Neutron mass in kg
m_n_meV = m_n_kg * (eV * 1e-3)  # Neutron mass in meV
M_amu = 10  # Oscillator mass in amu
M_meV = M_amu * 931.494  # Convert amu to MeV/c^2, then to meV (approximate)
sigma_b = 1.0  # Bound-atom cross section in barns
hbar_omega_0 = 10.0  # Phonon energy in meV

def calculate_sigma_2(E_meV):
    """
    Calculate the cross section σ₂(E) for inelastic neutron scattering from a 1D harmonic oscillator.

    Parameters:
    E_meV (float): Neutron energy in meV.

    Returns:
    float: Cross section σ₂(E) in barns.
    """
    # Check kinematic constraint: E must be >= 2 * hbar_omega_0
    if E_meV < 2 * hbar_omega_0:
        return 0.0

    # Calculate initial and final neutron wavevectors (in 1/ps)
    k_initial = np.sqrt(2 * m_n_meV * E_meV) / hbar_meV_ps
    E_final = E_meV - 2 * hbar_omega_0
    k_final = np.sqrt(2 * m_n_meV * E_final) / hbar_meV_ps

    # Calculate the Debye-Waller exponent W
    # For a 1D harmonic oscillator, the density of states is a delta function at hbar_omega_0
    # In the low-temperature limit, W simplifies to:
    W = (hbar_meV_ps**2 * (k_initial**2 + k_final**2 - 2 * k_initial * k_final)) / (4 * M_meV * hbar_omega_0)

    # Calculate the incoherent scattering function S_incoh,2(Q, ω)
    # For m=2, H_2(ℏω) is proportional to δ(ℏω - 2ℏω₀)
    # The integral over Q simplifies due to the delta function
    S_incoh_2 = np.exp(-2 * W) * (2 * W)**2 / 2

    # Calculate the differential cross section and integrate over solid angle
    # The integral over dΩ is 4π, and the energy delta function is already accounted for
    sigma_2 = sigma_b * S_incoh_2

    return sigma_2

# Calculate σ₂(E) for the two cases
E_case1 = 1.0  # meV
E_case2 = 40.0  # meV

sigma_2_case1 = calculate_sigma_2(E_case1)
sigma_2_case2 = calculate_sigma_2(E_case2)

print(f"Case 1 (E = {E_case1} meV): σ₂(E) = {sigma_2_case1:.3f} barns")
print(f"Case 2 (E = {E_case2} meV): σ₂(E) = {sigma_2_case2:.3f} barns")
```
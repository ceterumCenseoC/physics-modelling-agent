
```python
import numpy as np
import matplotlib.pyplot as plt
from scipy.constants import hbar, k, m_p, u, pi

# ==========================================
# 1. Model Constants and Input Parameters
# ==========================================

# Physical Constants
hbar_si = hbar  # Reduced Planck constant [J*s]
mass_p_si = m_p # Proton mass [kg]
amu_si = u      # Atomic mass unit [kg]

# System Parameters (Selected from Suggested Realistic Starting Parameters)
# Using Potassium-40 (^40K)
mass_amu = 40.0 
m = mass_amu * amu_si # Atomic mass [kg]

wavelength = 1064e-9  # Laser wavelength [m] (1064 nm)
 Waist = 50e-6         # Beam waist [m] (50 um)

# Lattice Depth Control
# We specify V_0 in units of Recoil Energy (E_R) as is standard in literature.
V0_over_ER = 12.0 

# Scattering Interaction
a_s = 200 * 5.29177e-11 # Scattering length [m] (~200 Bohr radii)

# Derived Quantities
k_lattice = 2 * np.pi / wavelength                # Wavenumber [1/m]
# Recoil Energy: E_R = (hbar^2 * k^2) / (2m)
E_R = (hbar_si**2 * k_lattice**2) / (2 * m)       # [Joules]

# Lattice Depth V_0
V_0 = V0_over_ER * E_R                            # [Joules]

# ==========================================
# 2. Model Implementations
# ==========================================

def calculate_tunnelling_energy(Recoil_Energy, Lattice_Depth):
    """
    Calculates the tunneling energy t using the deep-lattice approximation.
    
    Formula: t ≈ (4 / sqrt(pi)) * E_R * (V_0/E_R)^(3/4) * exp(-2 * sqrt(V_0/E_R))
    
    Args:
        Recoil_Energy (float): E_R in Joules.
        Lattice_Depth (float): V_0 in Joules.
        
    Returns:
        float: Tunneling energy t in Joules.
    """
    ratio = Lattice_Depth / Recoil_Energy
    t = (4.0 / np.sqrt(pi)) * Recoil_Energy * (ratio**(3/4)) * np.exp(-2 * np.sqrt(ratio))
    return t

def calculate_interaction_energy(Lattice_Depth, Recoil_Energy, scattering_length, beam_waist):
    """
    Calculates the on-site contact interaction U.
    
    Formula: U ≈ 2 * sqrt(2/pi) * (a_s * sqrt(V_0 * E_R)) / W
    
    Args:
        Lattice_Depth (float): V_0 in Joules.
        Recoil_Energy (float): E_R in Joules.
        scattering_length (float): a_s in meters.
        beam_waist (float): W in meters.
        
    Returns:
        float: Interaction energy U in Joules.
    """
    U = 2 * np.sqrt(2/pi) * (scattering_length * np.sqrt(Lattice_Depth * Recoil_Energy)) / beam_waist
    return U

# ==========================================
# 3. Computations
# ==========================================

# Calculate t and U for the specific parameters defined above
t_val = calculate_tunnelling_energy(E_R, V_0)
U_val = calculate_interaction_energy(V_0, E_R, a_s, Waist)

# Convert to Hz and kHz for easier reading
h_si = 2 * pi * hbar_si
t_Hz = t_val / h_si
U_Hz = U_val / h_si

# ==========================================
# 4. Visualization
# ==========================================

# We want to see how t and U scale with Lattice Depth (V_0)
# Create a range of V_0/E_R values from 5 to 20
v0_range = np.linspace(5, 20, 100) # V_0 / E_R
t_vals = []
U_vals = []

for v0_factor in v0_range:
    V_temp = v0_factor * E_R
    t_vals.append(calculate_tunnelling_energy(E_R, V_temp))
    U_vals.append(calculate_interaction_energy(V_temp, E_R, a_s, Waist))

# Convert arrays to Hz
t_Hz_range = np.array(t_vals) / h_si
U_Hz_range = np.array(U_vals) / h_si

plt.figure(figsize=(10, 6))
plt.semilogy(v0_range, t_Hz_range, label=r'Tunneling $t$ (Hz)', color='blue', linewidth=2)
plt.semilogy(v0_range, U_Hz_range, label=r'Interaction $U$ (Hz)', color='red', linewidth=2)

# Mark the specific point calculated
plt.semilogy(V0_over_ER, t_Hz, 'bo', label=f'Calculated $t$ ($V_0={V0_over_ER} E_R$)')
plt.semilogy(V0_over_ER, U_Hz, 'ro', label=f'Calculated $U$ ($V_0={V0_over_ER} E_R$)')

plt.title('Hubbard Model Parameters vs. Lattice Depth ($^{40}$K in 1064nm lattice)')
plt.xlabel(r'Lattice Depth $V_0 / E_R$')
plt.ylabel('Energy (Hz)')
plt.grid(True, which="both", ls="-")
plt.legend()
plt.tight_layout()
plt.show()

# ==========================================
# 5. Output
# ==========================================

print(f"--- System Parameters ---")
print(f"Atomic Species: Potassium-40")
print(f"Mass: {m:.3e} kg")
print(f"Laser Wavelength: {wavelength*1e9:.1f} nm")
print(f"Beam Waist: {Waist*1e6:.1f} um")
print(f"Scattering Length: {a_s*1e9:.1f} nm ({a_s/5.29177e-11:.0f} a0)")
print(f"Recoil Energy (E_R): {E_R:.3e} J ({E_R/k:.3e} K)")
print(f"\n--- Operating Point ---")
print(f"Lattice Depth (V_0): {V_0:.3e} J ({V_0/E_R:.1f} E_R)")
print(f"\n--- Calculated Hubbard Parameters ---")
print(f"Tunneling Energy (t): {t_val:.3e} J")
print(f"Interaction Energy (U): {U_val:.3e} J")
print(f"\n--- Frequency Scales ---")
print(f"t / h: {t_Hz:.2f} Hz")
print(f"U / h: {U_Hz:.2f} Hz")
print(f"Ratio U / t: {U_val/t_val:.2f}")

```
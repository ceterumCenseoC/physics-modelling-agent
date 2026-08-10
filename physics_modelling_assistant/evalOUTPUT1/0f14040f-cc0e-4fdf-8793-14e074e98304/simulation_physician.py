
```python
import numpy as np
import matplotlib.pyplot as plt

# ==============================================================================
# 1. Physics Constants and Inputs
# ==============================================================================

# Temperature conversion factor: 1 GeV^-2 = MeV * s^2 / (m^2 * GeV)
# Not directly needed since we use SI units primarily.

# Fundamental Constants
hbar = 1.054571817e-34       # Reduced Planck constant (J*s)
c_speed = 2.99792458e8       # Speed of light (m/s)
epsilon_0 = 8.854187817e-12  # Vacuum permittivity (F/m) or (C^2 / (N*m^2))
e_charge = 1.602176634e-19   # Elementary charge (C)
m_neutron = 1.67492749804e-27# Neutron mass (kg)
J_to_GeV = 6.242e9           # Conversion factor Joules to GeV

# Model Parameters from Problem Statement
# Local Dark Matter Energy Density
E_DM_GeV_cm3 = 0.3           # GeV / cm^3
# Convert to J/m^3:
# 0.3 GeV/c^2 / cm^3 -> J/m^3. Note: E = mc^2. We treat 0.3 as energy density.
# 0.3 GeV * (1.602e-10 J/GeV) = 4.806e-11 J
# 1 cm^3 = 1e-6 m^3
# Density = 4.806e-11 J / 1e-6 m^3 = 4.806e-5 J/m^3.
# Wait, let's look at the standard value: 0.3 GeV/cm^3 approx 0.4 GeV/cm^3.
# 1 GeV = 1.602e-10 J
# 1 cm^-3 = 10^6 m^-3
# Value = 0.3 * 1.602e-10 * 10^6 = 4.80655e-5 J/m^3
E_DM_J_m3 = E_DM_GeV_cm3 * 1.602176634e-10 * 1e6 

# Interferometer Parameters
L_arm = 4000.0               # Arm length (m)
f_signal = 250.0             # Signal frequency (Hz)
omega = 2.0 * np.pi * f_signal # Angular frequency (rad/s)
h_n = 3.0e-24                # Strain sensitivity (1/sqrt(Hz))

# Observation Parameters
T_years = 13.0
T_seconds = T_years * 365.25 * 24 * 3600

# Differential Charge Factors (delta_q)
# These are dimensionless in the ratio, but derived from charge fraction changes.
# In the model derivation, 'delta_q' is the numerator of the dimensionless fraction
# used in the force calculation: delta(Q/M) = delta_q / m_n.
# So delta_q is effectively a charge number density factor.
dopings = [0.074, 6e-3, 5e-4]

# ==============================================================================
# 2. Model Implementation Functions
# ==============================================================================

def calculate_field_amplitude(E_DM, omega, eps_0):
    """
    Calculates the field amplitude A0 from dark matter energy density.
    E_DM = 1/2 * eps_0 * omega^2 * A0^2
    => A0 = sqrt(2 * E_DM) / (omega * sqrt(eps_0))
    """
    return np.sqrt(2 * E_DM) / (omega * np.sqrt(eps_0))

def calculate_minimum_strain(h_n, T):
    """
    Calculates the minimum detectable strain given noise density and time.
    SNR = 1 => h_min = h_n / sqrt(T)
    """
    return h_n / np.sqrt(T)

def calculate_coupling_epsilon_B_L(delta_q, h_min, L, omega, m_n, eps_0, e, E_DM):
    """
    Calculates the smallest B-L coupling constant epsilon_B-L.
    Derived from:
    h = (delta_q * eps * e * sqrt(2*E_DM)) / (m_n * L * omega^2 * sqrt(eps_0))
    => eps = (h * m_n * L * omega^2 * sqrt(eps_0)) / (delta_q * e * sqrt(2*E_DM))
    """
    numerator = h_min * m_n * L * (omega**2) * np.sqrt(eps_0)
    denominator = delta_q * e * np.sqrt(2 * E_DM)
    return numerator / denominator

# ==============================================================================
# 3. Calculations
# ==============================================================================

# A. Calculate Field Amplitude
A0 = calculate_field_amplitude(E_DM_J_m3, omega, epsilon_0)

# B. Calculate Minimum Detectable Strain
h_min = calculate_minimum_strain(h_n, T_seconds)

# C. Calculate Epsilon for each doping scenario
results = []
for dq in dopings:
    eps = calculate_coupling_epsilon_B_L(dq, h_min, L_arm, omega, m_neutron, epsilon_0, e_charge, E_DM_J_m3)
    results.append(eps)

# ==============================================================================
# 4. Output and Visualization
# ==============================================================================

print("-" * 60)
print(f"Physics Model: LIGO Vector Dark Matter Detection")
print("-" * 60)
print(f"Parameters:")
print(f"  Frequency              : {f_signal} Hz")
print(f"  Angular Frequency      : {omega:.4f} rad/s")
print(f"  Arm Length             : {L_arm} m")
print(f"  Observation Time       : {T_years} years ({T_seconds:.2e} s)")
print(f"  Strain Sensitivity (h_n): {h_n:.2e} Hz^-1/2")
print(f"  DM Energy Density      : {E_DM_J_m3:.4e} J/m^3")
print(f"  Field Amplitude (A0)   : {A0:.4e} (Electric Field Units)")
print(f"  Minimum Strain Required: {h_min:.4e}")
print("-" * 60)
print("Results for Epsilon B-L:")

for i, dq in enumerate(dopings):
    print(f"  Scenario {i+1} (dq={dq:.5g}): Epsilon_B-L = {results[i]:.4e}")

print("-" * 60)

# Create a log-scale plot of Sensitivity vs. doping
# We generate a range of delta_q values to show the trend
dopings_range = np.logspace(-5, -1, 100) 
epsilon_curve = [calculate_coupling_epsilon_B_L(dq, h_min, L_arm, omega, m_neutron, epsilon_0, e_charge, E_DM_J_m3) 
                 for dq in dopings_range]

plt.figure(figsize=(10, 6))
plt.loglog(dopings_range, epsilon_curve, label='Sensitivity Limit', color='blue', linewidth=2)
plt.scatter(dopings, results, color='red', zorder=5, label='Calculated Points')
for i, dq in enumerate(dopings):
    plt.annotate(f"$\epsilon \\approx {results[i]:.2e}$", 
                 (dq, results[i]), 
                 textcoords="offset points", 
                 xytext=(-10,10), 
                 ha='center',
                 fontsize=9)

plt.title(r'Smallest Probeable $\epsilon_{B-L}$ vs. Doping Level $\delta q$')
plt.xlabel(r'Doping Factor $\delta q$ (Charge Fraction)')
plt.ylabel(r'Coupling Constant $\epsilon_{B-L}$')
plt.grid(True, which="both", ls="-", alpha=0.5)
plt.legend()
plt.tight_layout()

# Save or Show the plot
# Since I am an AI text model, I cannot display the window directly, 
# in a real script one would use plt.show().
# Here we assume the environment supports rendering or we just provide the code.
plt.savefig('ligo dark matter sensitivity.png')
print("Plot saved to 'ligo_dark_matter_sensitivity.png'")
```
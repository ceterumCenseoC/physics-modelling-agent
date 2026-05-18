```python
import numpy as np

# Constants
mu_b = 9.274e-24  # Bohr magneton in J/T
e = 1.602e-19     # Elementary charge in C
hbar = 1.0545718e-34  # Reduced Planck constant in J·s
m_e = 9.109e-31   # Electron mass in kg

# Model parameters
alpha = 1e-11      # Rashba coupling strength in eV·m
m = 0.1 * m_e      # Effective mass in kg
E_F = 10e-3 * e    # Fermi energy in J (10 meV)
E = np.array([1e6, 0, 0])  # Electric field in V/m along x-axis
tau = 1e-12        # Scattering time in s

# Step 1: Determine the regime (HDR or LDR)
if E_F >= 0:
    regime = "HDR"
    k0 = alpha * m
    k_plus_F = -k0 + np.sqrt(k0**2 + 2 * m * E_F)
    k_minus_F = k0 + np.sqrt(k0**2 + 2 * m * E_F)
else:
    regime = "LDR"
    k0 = alpha * m
    k_plus_F = k0 - np.sqrt(k0**2 + 2 * m * E_F)
    k_minus_F = -k0 - np.sqrt(k0**2 + 2 * m * E_F)

# Step 2: Calculate group velocities
v_plus_F = k_plus_F / m + alpha
v_minus_F = k_minus_F / m - alpha

# Step 3: Compute magnetization
if regime == "HDR":
    M = (mu_b * e * tau) / (2 * np.pi) * m * alpha * np.cross(np.array([0, 0, 1]), E)
else:
    M = (mu_b * e * tau) / (2 * np.pi) * np.sqrt(m**2 * alpha**2 + 2 * m * E_F) * np.cross(np.array([0, 0, 1]), E)

# Step 4: Print results
print(f"Regime: {regime}")
print(f"Fermi momenta: k_plus_F = {k_plus_F}, k_minus_F = {k_minus_F}")
print(f"Group velocities: v_plus_F = {v_plus_F}, v_minus_F = {v_minus_F}")
print(f"Magnetization: M = {M}")
print(f"Magnetization direction: {M / np.linalg.norm(M)}")
```
import numpy as np
import matplotlib.pyplot as plt
from scipy.constants import hbar, e, m_e, mu_B

# Constants
hbar = hbar  # Reduced Planck's constant
e = e        # Elementary charge
m_e = m_e    # Electron mass
mu_B = mu_B  # Bohr magneton

# Material parameters
alpha_R = 1.0e-11  # Rashba coupling constant (eV·m)
tau = 1.0e-12      # Relaxation time (s)
E_F = 1.0          # Fermi energy (eV)
m = 0.5 * m_e      # Effective mass (kg)

# Electric field parameters
E_x = 1.0e3        # Electric field in x-direction (V/m)
E_y = 0.0          # Electric field in y-direction (V/m)

# Numerical parameters
N_k = 100          # Number of k-points for discretization
k_max = 1.0e9      # Maximum k-value (1/m)

# Compute Fermi velocity
k_F = np.sqrt(2 * m * E_F) / hbar
v_F = hbar * k_F / m

# Discretize Brillouin zone
k_x = np.linspace(-k_max, k_max, N_k)
k_y = np.linspace(-k_max, k_max, N_k)
KX, KY = np.meshgrid(k_x, k_y)
K = np.sqrt(KX**2 + KY**2)

# Compute spin texture
sigma_x = np.zeros_like(KX)
sigma_y = np.zeros_like(KX)
sigma_z = np.zeros_like(KX)

# For simplicity, consider only one chirality (e.g., +)
sigma_x = KY / K
sigma_y = -KX / K

# Compute Edelstein susceptibility tensor (simplified)
chi_xy = (mu_B * np.abs(e) * tau * m * alpha_R) / (2 * np.pi * hbar**2)

# Calculate magnetization
M_x = 0.0
M_y = chi_xy * E_x
M_z = 0.0

# Handle nonlinear effects (simplified)
gamma = (e * np.sqrt(E_x**2 + E_y**2)) / (alpha_R * k_F**2)
if gamma > 1.0:
    M_y = M_y / (1 + gamma**2)

# Integrate over Fermi surface (simplified)
M_total = np.array([M_x, M_y, M_z])

# Visualize results
plt.figure(figsize=(10, 6))
plt.plot([0, E_x], [0, M_y], 'b-', linewidth=2)
plt.xlabel('Electric Field (V/m)')
plt.ylabel('Magnetization (A/m)')
plt.title('Magnetization vs. Electric Field')
plt.grid(True)
plt.show()

print("Magnetization components (A/m):")
print(f"M_x = {M_x:.2e}")
print(f"M_y = {M_y:.2e}")
print(f"M_z = {M_z:.2e}")
print(f"Total magnetization magnitude = {np.linalg.norm(M_total):.2e}")

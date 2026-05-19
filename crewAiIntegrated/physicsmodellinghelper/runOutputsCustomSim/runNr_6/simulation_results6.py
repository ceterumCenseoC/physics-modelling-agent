import numpy as np
import matplotlib.pyplot as plt

# Physical constants
hbar = 1.0545718e-34  # Reduced Planck's constant (J·s)
mu_b = 9.2740100789e-24  # Bohr magneton (J/T)
e = 1.602176634e-19  # Elementary charge (C)
m = 9.1093837015e-31  # Effective mass of electron (kg)
epsilon_0 = 8.8541878128e-12  # Vacuum permittivity (F/m)

# Model parameters
alpha_R = 1e-11  # Rashba coupling strength (J·m)
E_F = 1e-22  # Fermi energy (J)
mu = 0  # Chemical potential (J)
tau = 1e-12  # Scattering time (s)
E = 1e4  # Electric field magnitude (V/m)
phi_E = 0  # Angle of electric field (radians)
T = 0  # Temperature (K)

# Helper functions
def compute_fermi_momenta(alpha_R, m, hbar, mu, E_F):
    k0 = (m * alpha_R) / (hbar**2)
    if mu >= 0:
        # High-Density Regime (HDR)
        k_F_plus = -1 * k0 + np.sqrt(k0**2 + 2 * m * E_F)
        k_F_minus = 1 * k0 + np.sqrt(k0**2 + 2 * m * E_F)
        return k_F_plus, k_F_minus
    else:
        # Low-Density Regime (LDR)
        sqrt_term = np.sqrt(k0**2 + 2 * m * mu)
        k_F_plus = k0 - 1 * sqrt_term
        k_F_minus = k0 + 1 * sqrt_term
        return k_F_plus, k_F_minus

def compute_spin_texture(k_x, k_y, alpha_R, hbar, m):
    k = np.sqrt(k_x**2 + k_y**2)
    theta = np.arctan2(k_y, k_x)
    sigma_x = np.sin(theta)
    sigma_y = -np.cos(theta)
    return sigma_x, sigma_y

def compute_linear_magnetization(E, phi_E, alpha_R, m, tau, mu_b, e, hbar):
    M_x = 0
    M_y = (mu_b * abs(e) * tau) / (2 * np.pi) * m * alpha_R * E
    return M_x, M_y

def compute_nonlinear_response(E, L_s, E_F):
    gamma = (e * E * L_s) / E_F
    if gamma < 1e-2:
        return 1  # Linear response
    else:
        return 0.5  # Saturation factor

# Main simulation
k_max = 1e8  # Maximum momentum (m^-1)
nk = 100  # Number of momentum points
k = np.linspace(0, k_max, nk)

# Electric field parameters
E_min = 1e3  # Minimum electric field (V/m)
E_max = 1e5  # Maximum electric field (V/m)
nE = 50  # Number of electric field points
E_values = np.linspace(E_min, E_max, nE)

# Arrays to store results
M_linear = np.zeros(nE)
M_nonlinear = np.zeros(nE)

for i, E in enumerate(E_values):
    # Compute linear response
    M_x_linear, M_y_linear = compute_linear_magnetization(E, phi_E, alpha_R, m, tau, mu_b, e, hbar)
    M_linear[i] = np.sqrt(M_x_linear**2 + M_y_linear**2)

    # Compute nonlinear response
    L_s = hbar / (2 * m * alpha_R)
    gamma = (e * E * L_s) / E_F
    saturation_factor = compute_nonlinear_response(E, L_s, E_F)
    M_nonlinear[i] = M_linear[i] * saturation_factor

# Plot results
plt.figure(figsize=(10, 5))
plt.plot(E_values / 1e4, M_linear, label='Linear Response')
plt.plot(E_values / 1e4, M_nonlinear, label='Nonlinear Response')
plt.xlabel('Electric Field (kV/m)')
plt.ylabel('Magnetization (A/m)')
plt.legend()
plt.show()

# Visualize spin texture
kx = np.linspace(-1e8, 1e8, 20)
ky = np.linspace(-1e8, 1e8, 20)
KX, KY = np.meshgrid(kx, ky)

SX = np.zeros_like(KX)
SY = np.zeros_like(KY)

for i in range(KX.shape[0]):
    for j in range(KX.shape[1]):
        kx_val = KX[i, j]
        ky_val = KY[i, j]
        sigma_x, sigma_y = compute_spin_texture(kx_val, ky_val, alpha_R, hbar, m)
        SX[i, j] = sigma_x
        SY[i, j] = sigma_y

plt.figure()
plt.quiver(KX / 1e8, KY / 1e8, SX, SY)
plt.xlabel('k_x (×1e8 m^-1)')
plt.ylabel('k_y (×1e8 m^-1)')
plt.title('Spin Texture')
plt.show()

# Parameter Dependencies
# Electric Field Dependence
E_values = np.linspace(0, 1e5, 100)
M_values = np.zeros_like(E_values)

for i, E in enumerate(E_values):
    M_x, M_y = compute_linear_magnetization(E, phi_E, alpha_R, m, tau, mu_b, e, hbar)
    M_values[i] = np.sqrt(M_x**2 + M_y**2)

plt.figure()
plt.plot(E_values / 1e4, M_values)
plt.xlabel('Electric Field (kV/m)')
plt.ylabel('Magnetization (A/m)')
plt.show()

# Rashba Coupling Dependence
alpha_R_values = np.linspace(0, 2e-11, 100)
M_values = np.zeros_like(alpha_R_values)

for i, alpha_R in enumerate(alpha_R_values):
    M_x, M_y = compute_linear_magnetization(E, phi_E, alpha_R, m, tau, mu_b, e, hbar)
    M_values[i] = np.sqrt(M_x**2 + M_y**2)

plt.figure()
plt.plot(alpha_R_values / 1e-11, M_values)
plt.xlabel('Rashba Coupling (×1e-11 J·m)')
plt.ylabel('Magnetization (A/m)')
plt.show()
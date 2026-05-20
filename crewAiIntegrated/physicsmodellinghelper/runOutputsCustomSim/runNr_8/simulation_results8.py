import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Constants
hbar = 1.0545718e-34  # Reduced Planck constant in J·s
e = 1.602176634e-19   # Elementary charge in C
mu_0 = 4 * np.pi * 1e-7  # Permeability of free space in H/m

# Material parameters
alpha_R = 1e-11  # Rashba coupling strength in J·m
tau = 1e-12      # Scattering time in s
n = 1e16         # Carrier density in m⁻²
m_star = 9.10938356e-31  # Effective mass in kg (electron mass)
k_F = 1e9        # Fermi wave vector in m⁻¹

# Calculate Fermi velocity
v_F = (hbar * k_F) / m_star  # Fermi velocity in m/s

# Function to calculate spin polarization
def calculate_spin_polarization(E_x, E_y):
    E = np.array([E_x, E_y, 0])  # Electric field vector
    z_hat = np.array([0, 0, 1])   # Unit vector in z-direction
    E_cross_z = np.cross(E, z_hat)
    spin_polarization = (e * tau * alpha_R) / (hbar**2) * E_cross_z
    return spin_polarization

# Function to calculate magnetization magnitude
def calculate_magnetization_magnitude(E_magnitude):
    magnetization_magnitude = (mu_0 * e * tau * alpha_R * n) / hbar * E_magnitude
    return magnetization_magnitude

# Function to calculate magnetization direction
def calculate_magnetization_direction(E_x, E_y):
    E = np.array([E_x, E_y, 0])
    z_hat = np.array([0, 0, 1])
    E_cross_z = np.cross(E, z_hat)
    magnetization_direction = E_cross_z / np.linalg.norm(E_cross_z)
    return magnetization_direction

# Generate data for plots
E_magnitudes = np.linspace(0, 1e6, 100)  # Electric field magnitudes in V/m
E_angles = np.linspace(0, 2 * np.pi, 100)  # Electric field angles in radians

# Calculate magnetization magnitudes for different electric field magnitudes
magnetization_magnitudes = [calculate_magnetization_magnitude(E) for E in E_magnitudes]

# Calculate magnetization directions for different electric field angles
magnetization_directions = [calculate_magnetization_direction(np.cos(angle), np.sin(angle)) for angle in E_angles]

# Plot magnetization magnitude vs. electric field magnitude
plt.figure(figsize=(10, 6))
plt.plot(E_magnitudes, magnetization_magnitudes, label='Magnetization Magnitude')
plt.xlabel('Electric Field Magnitude (V/m)')
plt.ylabel('Magnetization Magnitude (A/m)')
plt.title('Magnetization Magnitude vs. Electric Field Magnitude')
plt.legend()
plt.grid(True)
plt.show()

# Plot magnetization direction vs. electric field direction
fig = plt.figure(figsize=(10, 6))
ax = fig.add_subplot(111, projection='3d')
for i, angle in enumerate(E_angles):
    E_x = np.cos(angle)
    E_y = np.sin(angle)
    M_dir = magnetization_directions[i]
    ax.quiver(E_x, E_y, 0, M_dir[0], M_dir[1], M_dir[2], length=0.1, normalize=True, color='b')
ax.set_xlabel('E_x')
ax.set_ylabel('E_y')
ax.set_zlabel('M_z')
ax.set_title('Magnetization Direction vs. Electric Field Direction')
plt.show()

# Plot parameter dependencies
alpha_R_values = np.linspace(1e-12, 1e-10, 100)  # Rashba coupling strengths in J·m
magnetization_vs_alpha_R = [calculate_magnetization_magnitude(1e5) * (alpha / alpha_R) for alpha in alpha_R_values]

plt.figure(figsize=(10, 6))
plt.plot(alpha_R_values, magnetization_vs_alpha_R, label='Magnetization vs. α_R')
plt.xlabel('Rashba Coupling Strength (J·m)')
plt.ylabel('Magnetization Magnitude (A/m)')
plt.title('Magnetization Magnitude vs. Rashba Coupling Strength')
plt.legend()
plt.grid(True)
plt.show()

# Plot magnetization vs. Fermi velocity
v_F_values = np.linspace(1e5, 1e7, 100)  # Fermi velocities in m/s
magnetization_vs_v_F = [calculate_magnetization_magnitude(1e5) * (v / v_F) for v in v_F_values]

plt.figure(figsize=(10, 6))
plt.plot(v_F_values, magnetization_vs_v_F, label='Magnetization vs. v_F')
plt.xlabel('Fermi Velocity (m/s)')
plt.ylabel('Magnetization Magnitude (A/m)')
plt.title('Magnetization Magnitude vs. Fermi Velocity')
plt.legend()
plt.grid(True)
plt.show()

# Plot magnetization vs. scattering time
tau_values = np.linspace(1e-13, 1e-11, 100)  # Scattering times in s
magnetization_vs_tau = [calculate_magnetization_magnitude(1e5) * (t / tau) for t in tau_values]

plt.figure(figsize=(10, 6))
plt.plot(tau_values, magnetization_vs_tau, label='Magnetization vs. τ')
plt.xlabel('Scattering Time (s)')
plt.ylabel('Magnetization Magnitude (A/m)')
plt.title('Magnetization Magnitude vs. Scattering Time')
plt.legend()
plt.grid(True)
plt.show()

# Plot chirality effects
# Clockwise chirality
spin_polarization_cw = calculate_spin_polarization(1, 0)
# Counter-clockwise chirality
spin_polarization_ccw = -calculate_spin_polarization(1, 0)

fig = plt.figure(figsize=(10, 6))
ax = fig.add_subplot(111, projection='3d')
ax.quiver(0, 0, 0, spin_polarization_cw[0], spin_polarization_cw[1], spin_polarization_cw[2], length=0.1, normalize=True, color='r', label='Clockwise Chirality')
ax.quiver(0, 0, 0, spin_polarization_ccw[0], spin_polarization_ccw[1], spin_polarization_ccw[2], length=0.1, normalize=True, color='g', label='Counter-Clockwise Chirality')
ax.set_xlabel('σ_x')
ax.set_ylabel('σ_y')
ax.set_zlabel('σ_z')
ax.set_title('Spin Polarization for Different Chiralities')
ax.legend()
plt.show()

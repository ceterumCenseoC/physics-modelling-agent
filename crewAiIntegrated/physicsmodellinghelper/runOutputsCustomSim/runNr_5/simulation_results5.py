import numpy as np

# Physical constants (SI units)
hbar = 1.0545718e-34  # Reduced Planck's constant (J·s)
mu_B = 9.2740100783e-24  # Bohr magneton (J·T^-1)
e = 1.602176634e-19  # Elementary charge (C)
pi = np.pi  # Pi

# Model parameters (SI units)
alpha = 1.0e-11  # Rashba coupling strength (J·m)
m = 9.1093837015e-31  # Effective mass (kg)
tau = 1.0e-12  # Scattering time (s)
E_F = 1.0e-20  # Fermi energy (J)
nu = 1  # Chirality (+1 or -1)

# Applied electric field (V/m)
E_x = 1.0e3  # Electric field along x-axis
E_y = 0.0  # Electric field along y-axis
E = np.array([E_x, E_y, 0.0])  # Electric field vector

# Step 1: Determine the regime (HDR or LDR)
if E_F > 0:
    regime = "HDR"
else:
    regime = "LDR"

# Step 2: Compute Edelstein susceptibility (chi)
if regime == "HDR":
    chi = (mu_B * abs(e) * tau) / (2 * pi * hbar**2) * m * alpha
else:
    chi = (mu_B * abs(e) * tau) / (2 * pi * hbar**2) * np.sqrt(m**2 * alpha**2 + 2 * m * E_F)

# Step 3: Compute magnetization direction (E × ẑ)
z_hat = np.array([0.0, 0.0, 1.0])  # Unit vector in z-direction
M_direction = np.cross(E, z_hat)  # Cross product E × ẑ

# Adjust direction based on chirality
if nu == -1:
    M_direction = -M_direction

# Step 4: Compute magnetization magnitude
M_magnitude = chi * np.linalg.norm(E)  # |M| = chi * |E|

# Step 5: Combine magnitude and direction
M = M_magnitude * M_direction / np.linalg.norm(M_direction)  # Normalized magnetization vector

# Print results
print("Regime:", regime)
print("Edelstein susceptibility (chi):", chi, "S")
print("Magnetization vector (M):", M, "A/m")
print("Magnetization magnitude:", M_magnitude, "A/m")
print("Magnetization direction:", M_direction / np.linalg.norm(M_direction))
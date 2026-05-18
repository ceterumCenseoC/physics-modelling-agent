# Edelstein Effect Simulation for Rashba Fermions
# This script simulates the Edelstein effect in Rashba fermions at the Gamma point.
# The simulation follows the theoretical framework and key equations provided in the context.

# Import necessary libraries
import numpy as np
import matplotlib.pyplot as plt

# Step 1: Define Physical Constants and Parameters

# Fundamental constants
e = 1.602176634e-19  # Elementary charge (C)
hbar = 1.054571817e-34  # Reduced Planck constant (J·s)

# Material parameters
v_F = 1e6  # Fermi velocity (m/s)
alpha_R = 1e-10  # Rashba coupling strength (eV·Å)
# Convert alpha_R to J·m:
alpha_R_Jm = alpha_R * 1e-10 * 1.602176634e-19  # (J·m)

# Electric field parameters
E_magnitude = 1e4  # Electric field magnitude (V/m)
E_direction = 'x'  # Direction of electric field ('x', 'y', or 'z')

# Step 2: Calculate Edelstein Susceptibility

# Calculate Edelstein susceptibility
chi = (e**2 * alpha_R_Jm) / (hbar * v_F**2)

# Assume chirality affects the sign of chi
chirality = 1  # +1 for one chirality, -1 for the opposite
chi *= chirality

# Step 3: Compute Magnetization

# Compute magnetization magnitude
M_magnitude = chi * E_magnitude

# Determine magnetization direction based on electric field direction
if E_direction == 'x':
    M_direction = 'z'
elif E_direction == 'y':
    M_direction = 'z'  # Assuming out-of-plane magnetization
elif E_direction == 'z':
    M_direction = 'x'  # Assuming in-plane magnetization

# Construct magnetization vector
M = {'magnitude': M_magnitude, 'direction': M_direction}

# Step 4: Analyze Parameter Dependencies

# Electric field dependence
def compute_M_vs_E(E_range):
    M_range = [chi * E for E in E_range]
    return M_range

# Rashba coupling dependence
def compute_M_vs_alphaR(alphaR_range):
    M_range = [(e**2 * alphaR * 1e-10 * 1.602176634e-19) / (hbar * v_F**2) * E_magnitude for alphaR in alphaR_range]
    return M_range

# Fermi velocity dependence
def compute_M_vs_vF(vF_range):
    M_range = [chi / (vF**2) * E_magnitude for vF in vF_range]
    return M_range

# Step 5: Visualize Results

# Generate electric field range
E_range = np.linspace(0, 5e4, 100)

# Compute corresponding magnetization
M_range = compute_M_vs_E(E_range)

# Create plot
plt.figure(figsize=(10, 6))
plt.plot(E_range, M_range)
plt.xlabel('Electric Field (V/m)')
plt.ylabel('Magnetization (A/m)')
plt.title('Magnetization vs. Electric Field')
plt.grid(True)
plt.show()

# Step 6: Explore Parameter Space

# Vary Rashba coupling strength
alphaR_range = np.linspace(0.5e-10, 2e-10, 100)

# Compute magnetization for each alphaR
M_alphaR_range = compute_M_vs_alphaR(alphaR_range)

# Plot results
plt.figure(figsize=(10, 6))
plt.plot(alphaR_range, M_alphaR_range)
plt.xlabel('Rashba Coupling Strength (eV·Å)')
plt.ylabel('Magnetization (A/m)')
plt.title('Magnetization vs. Rashba Coupling Strength')
plt.grid(True)
plt.show()

# Vary Fermi velocity
vF_range = np.linspace(0.5e6, 2e6, 100)

# Compute magnetization for each vF
M_vF_range = compute_M_vs_vF(vF_range)

# Plot results
plt.figure(figsize=(10, 6))
plt.plot(vF_range, M_vF_range)
plt.xlabel('Fermi Velocity (m/s)')
plt.ylabel('Magnetization (A/m)')
plt.title('Magnetization vs. Fermi Velocity')
plt.grid(True)
plt.show()

# Print the magnetization vector
print("Magnetization Vector:", M)
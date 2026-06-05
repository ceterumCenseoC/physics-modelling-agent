The Edelstein effect model for Rashba fermions is implemented in Python as follows:

```python
import numpy as np
import matplotlib.pyplot as plt

# Physical constants
e = 1.602e-19  # Elementary charge (C)
hbar = 1.055e-34  # Reduced Planck constant (J·s)
m_e = 9.109e-31  # Electron mass (kg)
k_B = 1.381e-23  # Boltzmann constant (J/K)

# Model parameters
alpha = 50e-22  # Spin-orbit coupling strength (J·m)
v_F = 1e6  # Fermi velocity (m/s)
tau = 1e-12  # Relaxation time (s)
E = 10  # Electric field magnitude (V/m)
T = 0  # Temperature (K)

# Derived parameters
m_star = m_e  # Effective mass
epsilon_F = (hbar**2 * (m_star * v_F)**2) / (2 * m_star)

# Compute spin polarization
def compute_spin_polarization(alpha, tau, E, m_star):
    # Calculate the magnitude
    S_mag = (e * tau * alpha * E) / (hbar**2)
    return S_mag

# Vector components for direction
def compute_spin_direction(E_vector):
    # Assuming E is in the x-y plane
    E_x, E_y = E_vector
    S_x = -E_y
    S_y = E_x
    return np.array([S_x, S_y])

# Example electric field vector
E_vector = np.array([E, 0])  # E along x-axis
S_vector = compute_spin_direction(E_vector)
S_mag = compute_spin_polarization(alpha, tau, E, m_star)

print(f"Spin Polarization Magnitude: {S_mag} spins/m²")
print(f"Spin Polarization Direction: {S_vector}")

# Plotting
# Create an array of electric field magnitudes
E_values = np.linspace(0, 100, 100)  # V/m

# Compute spin polarization for each E
S_magnitudes = [compute_spin_polarization(alpha, tau, E_val, m_star) for E_val in E_values]

# Plot S vs E
plt.figure(figsize=(10, 6))
plt.plot(E_values, S_magnitudes, label='Spin Polarization')
plt.xlabel('Electric Field (V/m)')
plt.ylabel('Spin Polarization (spins/m²)')
plt.title('Spin Polarization vs Electric Field')
plt.legend()
plt.grid(True)
plt.show()

# Polar plot for direction
theta = np.linspace(0, 2*np.pi, 100)
E_x = E * np.cos(theta)
E_y = E * np.sin(theta)
S_x = -E_y
S_y = E_x

plt.figure(figsize=(8, 8))
plt.quiver(np.zeros_like(theta), np.zeros_like(theta), S_x, S_y, color='b')
plt.xlabel('S_x')
plt.ylabel('S_y')
plt.title('Spin Polarization Direction vs Electric Field Direction')
plt.grid(True)
plt.show()
```

### Explanation of the Code:

1. **Physical Constants**: Defined constants include the elementary charge, reduced Planck constant, electron mass, and Boltzmann constant.

2. **Model Parameters**: These are user-defined values for spin-orbit coupling strength, Fermi velocity, relaxation time, electric field, and temperature.

3. **Spin Polarization Calculation**: The function `compute_spin_polarization` calculates the magnitude of the spin polarization using the provided formula. The direction is computed using the cross product to ensure perpendicularity.

4. **Plotting**: The code generates plots to visualize how the spin polarization magnitude varies with electric field and how the direction changes as the electric field rotates.

This implementation provides a clear and modular approach to studying the Edelstein effect, allowing for easy modification and extension to include additional effects such as temperature dependence or quantum geometric contributions.
"""
Numerical Implementation of the Edelstein Effect for Rashba Fermions

This script calculates the magnetization magnitude and direction induced by an electric field
in a 2D Rashba electron gas at the Gamma point of the Brillouin zone. The model is based
on the semiclassical Boltzmann approach and accounts for parameter dependencies such as
Rashba coupling strength, Fermi velocity, and electric field characteristics.

Author: [Your Name]
Date: [Current Date]
"""

import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm
from mpl_toolkits.mplot3d import Axes3D

# Constants (in SI units)
hbar = 1.0545718e-34  # Reduced Planck constant
e = 1.602176634e-19    # Elementary charge
mu_b = 9.2740100783e-24 # Bohr magneton

class EdelsteinEffect:
    """
    A class to model the Edelstein effect in a 2D Rashba electron gas.

    Attributes:
        m (float): Effective mass of carriers (kg)
        alpha_R (float): Rashba spin-orbit coupling strength (J·m)
        E_F (float): Fermi energy (J)
        tau (float): Relaxation time (s)
        E_field (numpy.ndarray): Applied electric field vector (V/m)
    """

    def __init__(self, m, alpha_R, E_F, tau, E_field):
        """
        Initialize the Edelstein effect model with given parameters.

        Args:
            m (float): Effective mass of carriers (kg)
            alpha_R (float): Rashba spin-orbit coupling strength (J·m)
            E_F (float): Fermi energy (J)
            tau (float): Relaxation time (s)
            E_field (numpy.ndarray): Applied electric field vector (V/m)
        """
        self.m = m
        self.alpha_R = alpha_R
        self.E_F = E_F
        self.tau = tau
        self.E_field = E_field

        # Calculate derived parameters
        self.k0 = m * alpha_R / hbar**2
        self.v_F = np.sqrt(2 * E_F / m)  # Fermi velocity
        self.L_s = hbar / (2 * m * alpha_R)  # Spin-orbit length
        self.gamma = (e * np.linalg.norm(E_field) * self.L_s) / E_F  # Nonlinearity parameter

    def calculate_fermi_momenta(self):
        """
        Calculate the Fermi momenta for both chirality bands.

        Returns:
            tuple: (k_plus_F, k_minus_F) Fermi momenta for ν=+ and ν=- bands (m⁻¹)
        """
        k_plus_F = -self.k0 + np.sqrt(self.k0**2 + 2 * self.m * self.E_F / hbar**2)
        k_minus_F = self.k0 + np.sqrt(self.k0**2 + 2 * self.m * self.E_F / hbar**2)
        return k_plus_F, k_minus_F

    def calculate_magnetization(self):
        """
        Calculate the magnetization vector using the semiclassical Boltzmann approach.

        Returns:
            numpy.ndarray: Magnetization vector (A·m²)
        """
        # Determine the regime based on gamma
        if self.gamma < 1:
            # Linear regime (HDR or LDR)
            k_plus_F, k_minus_F = self.calculate_fermi_momenta()

            # Check if both bands are occupied (HDR)
            if k_plus_F > 0:
                # High-Density Regime
                M_magnitude = (mu_b * np.abs(e) * self.tau * self.m * self.alpha_R) / (2 * np.pi)
            else:
                # Low-Density Regime
                M_magnitude = (mu_b * np.abs(e) * self.tau) / (2 * np.pi) * \
                             np.sqrt(self.m**2 * self.alpha_R**2 + 2 * self.m * self.E_F)
        else:
            # Nonlinear regime (saturation)
            M_magnitude = (mu_b * np.abs(e) * self.tau * self.m * self.alpha_R) / (2 * np.pi) * \
                         np.tanh(1 / self.gamma)

        # Magnetization direction is perpendicular to E_field (in-plane)
        E_perp = np.array([-self.E_field[1], self.E_field[0], 0])
        if np.linalg.norm(E_perp) > 0:
            M_direction = E_perp / np.linalg.norm(E_perp)
        else:
            M_direction = np.array([0, 1, 0])  # Default direction if E_field is zero

        M_vector = M_magnitude * M_direction
        return M_vector

    def calculate_magnetization_angular_dependence(self, E_magnitude, num_angles=100):
        """
        Calculate magnetization for different electric field directions.

        Args:
            E_magnitude (float): Magnitude of the electric field (V/m)
            num_angles (int): Number of angles to sample

        Returns:
            tuple: (angles, M_magnitudes, M_directions) for visualization
        """
        angles = np.linspace(0, 2 * np.pi, num_angles)
        M_magnitudes = []
        M_directions = []

        for angle in angles:
            E_field = E_magnitude * np.array([np.cos(angle), np.sin(angle), 0])
            self.E_field = E_field
            self.gamma = (e * np.linalg.norm(E_field) * self.L_s) / self.E_F

            M_vector = self.calculate_magnetization()
            M_magnitudes.append(np.linalg.norm(M_vector))
            M_directions.append(M_vector / np.linalg.norm(M_vector) if np.linalg.norm(M_vector) > 0 else np.array([0, 0, 0]))

        return angles, np.array(M_magnitudes), np.array(M_directions)

    def calculate_magnetization_vs_field(self, E_max, num_points=100):
        """
        Calculate magnetization as a function of electric field magnitude.

        Args:
            E_max (float): Maximum electric field magnitude (V/m)
            num_points (int): Number of points to sample

        Returns:
            tuple: (E_magnitudes, M_magnitudes) for visualization
        """
        E_magnitudes = np.linspace(0, E_max, num_points)
        M_magnitudes = []

        for E_mag in E_magnitudes:
            E_field = E_mag * np.array([1, 0, 0])  # Fixed direction along x-axis
            self.E_field = E_field
            self.gamma = (e * E_mag * self.L_s) / self.E_F

            M_vector = self.calculate_magnetization()
            M_magnitudes.append(np.linalg.norm(M_vector))

        return E_magnitudes, np.array(M_magnitudes)

    def calculate_magnetization_vs_fermi_velocity(self, v_F_max, num_points=100):
        """
        Calculate magnetization as a function of Fermi velocity.

        Args:
            v_F_max (float): Maximum Fermi velocity (m/s)
            num_points (int): Number of points to sample

        Returns:
            tuple: (v_F_values, M_magnitudes) for visualization
        """
        v_F_values = np.linspace(0.1, v_F_max, num_points)
        M_magnitudes = []

        for v_F in v_F_values:
            E_F = 0.5 * self.m * v_F**2
            self.E_F = E_F
            self.v_F = v_F
            self.gamma = (e * np.linalg.norm(self.E_field) * self.L_s) / E_F

            M_vector = self.calculate_magnetization()
            M_magnitudes.append(np.linalg.norm(M_vector))

        return v_F_values, np.array(M_magnitudes)

    def calculate_magnetization_vs_rashba_coupling(self, alpha_R_max, num_points=100):
        """
        Calculate magnetization as a function of Rashba coupling strength.

        Args:
            alpha_R_max (float): Maximum Rashba coupling strength (J·m)
            num_points (int): Number of points to sample

        Returns:
            tuple: (alpha_R_values, M_magnitudes) for visualization
        """
        alpha_R_values = np.linspace(0.1, alpha_R_max, num_points)
        M_magnitudes = []

        for alpha_R in alpha_R_values:
            self.alpha_R = alpha_R
            self.k0 = self.m * alpha_R / hbar**2
            self.L_s = hbar / (2 * self.m * alpha_R)
            self.gamma = (e * np.linalg.norm(self.E_field) * self.L_s) / self.E_F

            M_vector = self.calculate_magnetization()
            M_magnitudes.append(np.linalg.norm(M_vector))

        return alpha_R_values, np.array(M_magnitudes)

# Example usage and visualization
if __name__ == "__main__":
    # Material parameters (example values for a typical 2D electron gas)
    m = 9.10938356e-31  # Electron mass (kg)
    alpha_R = 1e-11      # Rashba coupling strength (J·m)
    E_F = 1e-20          # Fermi energy (J)
    tau = 1e-12          # Relaxation time (s)
    E_field = np.array([1e3, 0, 0])  # Electric field (V/m)

    # Create Edelstein effect model
    edelstein = EdelsteinEffect(m, alpha_R, E_F, tau, E_field)

    # Calculate magnetization
    M_vector = edelstein.calculate_magnetization()
    print(f"Magnetization vector: {M_vector} A·m²")
    print(f"Magnetization magnitude: {np.linalg.norm(M_vector):.2e} A·m²")
    print(f"Magnetization direction: {M_vector / np.linalg.norm(M_vector) if np.linalg.norm(M_vector) > 0 else [0, 0, 0]}")

    # Visualization 1: Magnetization vs Electric Field Direction
    E_magnitude = 1e3  # V/m
    angles, M_magnitudes, M_directions = edelstein.calculate_magnetization_angular_dependence(E_magnitude)

    plt.figure(figsize=(12, 5))
    plt.subplot(1, 2, 1)
    plt.polar(angles, M_magnitudes)
    plt.title("Magnetization Magnitude vs Electric Field Direction")
    plt.xlabel("Electric Field Angle (radians)")
    plt.ylabel("Magnetization Magnitude (A·m²)")

    plt.subplot(1, 2, 2)
    plt.quiver([0] * len(angles), [0] * len(angles),
               M_directions[:, 0], M_directions[:, 1],
               M_magnitudes, cmap='viridis', scale=1)
    plt.title("Magnetization Direction vs Electric Field Direction")
    plt.xlabel("M_x")
    plt.ylabel("M_y")
    plt.axis('equal')
    plt.colorbar(label="Magnetization Magnitude (A·m²)")
    plt.tight_layout()
    plt.show()

    # Visualization 2: Magnetization vs Electric Field Magnitude
    E_max = 1e4  # V/m
    E_magnitudes, M_magnitudes = edelstein.calculate_magnetization_vs_field(E_max)

    plt.figure(figsize=(8, 6))
    plt.plot(E_magnitudes, M_magnitudes, 'b-', linewidth=2)
    plt.title("Magnetization vs Electric Field Magnitude")
    plt.xlabel("Electric Field Magnitude (V/m)")
    plt.ylabel("Magnetization Magnitude (A·m²)")
    plt.grid(True)
    plt.show()

    # Visualization 3: Magnetization vs Fermi Velocity
    v_F_max = 1e6  # m/s
    v_F_values, M_magnitudes = edelstein.calculate_magnetization_vs_fermi_velocity(v_F_max)

    plt.figure(figsize=(8, 6))
    plt.plot(v_F_values, M_magnitudes, 'r-', linewidth=2)
    plt.title("Magnetization vs Fermi Velocity")
    plt.xlabel("Fermi Velocity (m/s)")
    plt.ylabel("Magnetization Magnitude (A·m²)")
    plt.grid(True)
    plt.show()

    # Visualization 4: Magnetization vs Rashba Coupling Strength
    alpha_R_max = 1e-10  # J·m
    alpha_R_values, M_magnitudes = edelstein.calculate_magnetization_vs_rashba_coupling(alpha_R_max)

    plt.figure(figsize=(8, 6))
    plt.plot(alpha_R_values, M_magnitudes, 'g-', linewidth=2)
    plt.title("Magnetization vs Rashba Coupling Strength")
    plt.xlabel("Rashba Coupling Strength (J·m)")
    plt.ylabel("Magnetization Magnitude (A·m²)")
    plt.grid(True)
    plt.show()

    # 3D Visualization: Magnetization Surface
    fig = plt.figure(figsize=(10, 8))
    ax = fig.add_subplot(111, projection='3d')

    # Create grid of electric field components
    E_x = np.linspace(-1e4, 1e4, 50)
    E_y = np.linspace(-1e4, 1e4, 50)
    E_x, E_y = np.meshgrid(E_x, E_y)
    M_z = np.zeros_like(E_x)

    for i in range(E_x.shape[0]):
        for j in range(E_x.shape[1]):
            E_field = np.array([E_x[i,j], E_y[i,j], 0])
            edelstein.E_field = E_field
            edelstein.gamma = (e * np.linalg.norm(E_field) * edelstein.L_s) / edelstein.E_F
            M_vector = edelstein.calculate_magnetization()
            M_z[i,j] = np.linalg.norm(M_vector)

    # Plot the surface
    surf = ax.plot_surface(E_x, E_y, M_z, cmap=cm.viridis, linewidth=0, antialiased=False)
    ax.set_xlabel('E_x (V/m)')
    ax.set_ylabel('E_y (V/m)')
    ax.set_zlabel('Magnetization Magnitude (A·m²)')
    ax.set_title('Magnetization Magnitude as a Function of Electric Field')
    fig.colorbar(surf, shrink=0.5, aspect=5)
    plt.savefig("magnetization_surface.png", dpi=600)
    plt.show()
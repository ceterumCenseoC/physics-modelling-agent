"""
Numerical Implementation of the Edelstein Effect for Rashba Fermions at the Gamma Point

This script calculates the magnetization magnitude and direction induced by an applied
electric field in a Rashba fermion system at the Gamma point of the Brillouin zone.
The model considers the dependence on key parameters such as chirality and Fermi velocity.

Author: [Your Name]
Date: [Current Date]
"""

import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Constants
H_BAR = 1.0545718e-34  # Reduced Planck's constant (J·s)
ELECTRON_CHARGE = 1.602176634e-19  # Elementary charge (C)
ELECTRON_MASS = 9.1093837015e-31  # Electron mass (kg)
BOHR_MAGNETON = 9.2740100783e-24  # Bohr magneton (J/T)

class RashbaEdelsteinModel:
    """
    A class to model the Edelstein effect in Rashba fermion systems.

    Attributes:
        alpha_R (float): Rashba spin-orbit coupling strength (eV·Å)
        m_star (float): Effective electron mass (kg)
        n (float): Electron density (m^-2)
        tau (float): Relaxation time (s)
        v_F (float): Fermi velocity (m/s)
        chirality (int): Chirality of the Rashba bands (+1 or -1)
    """

    def __init__(self, alpha_R, m_star, n, tau, v_F, chirality=1):
        """
        Initialize the Rashba Edelstein model with given parameters.

        Args:
            alpha_R (float): Rashba spin-orbit coupling strength (eV·Å)
            m_star (float): Effective electron mass (kg)
            n (float): Electron density (m^-2)
            tau (float): Relaxation time (s)
            v_F (float): Fermi velocity (m/s)
            chirality (int): Chirality of the Rashba bands (+1 or -1)
        """
        self.alpha_R = alpha_R * 1.602176634e-19 * 1e-10  # Convert eV·Å to J·m
        self.m_star = m_star
        self.n = n
        self.tau = tau
        self.v_F = v_F
        self.chirality = chirality

    def calculate_spin_polarization(self, E_x, E_y):
        """
        Calculate the spin polarization induced by an electric field.

        Args:
            E_x (float): Electric field component in x-direction (V/m)
            E_y (float): Electric field component in y-direction (V/m)

        Returns:
            tuple: (S_x, S_y, S_z) components of spin polarization (A/m^2)
        """
        # Calculate the Edelstein susceptibility
        chi = (ELECTRON_CHARGE * self.tau * self.alpha_R * self.n) / (2 * H_BAR)

        # Spin polarization components
        S_x = -chi * E_y * self.chirality
        S_y = chi * E_x * self.chirality
        S_z = 0.0  # No out-of-plane component for Rashba at Gamma point

        return S_x, S_y, S_z

    def calculate_magnetization(self, E_x, E_y):
        """
        Calculate the magnetization induced by an electric field.

        Args:
            E_x (float): Electric field component in x-direction (V/m)
            E_y (float): Electric field component in y-direction (V/m)

        Returns:
            tuple: (M_x, M_y, M_z) components of magnetization (A/m)
        """
        S_x, S_y, S_z = self.calculate_spin_polarization(E_x, E_y)

        # Convert spin polarization to magnetization (M = S / (g * mu_B))
        # Assuming g-factor of 2 for free electrons
        g_factor = 2.0
        M_x = S_x / (g_factor * BOHR_MAGNETON)
        M_y = S_y / (g_factor * BOHR_MAGNETON)
        M_z = S_z / (g_factor * BOHR_MAGNETON)

        return M_x, M_y, M_z

    def calculate_orbital_magnetization(self, E_x, E_y):
        """
        Calculate the orbital magnetization induced by an electric field.
        This is a simplified model for demonstration purposes.

        Args:
            E_x (float): Electric field component in x-direction (V/m)
            E_y (float): Electric field component in y-direction (V/m)

        Returns:
            tuple: (M_orb_x, M_orb_y, M_orb_z) components of orbital magnetization (A/m)
        """
        # Simplified orbital Edelstein susceptibility (assuming similar magnitude to spin)
        chi_orb = (ELECTRON_CHARGE * self.tau * self.alpha_R * self.n) / (4 * H_BAR)

        M_orb_x = -chi_orb * E_y * self.chirality
        M_orb_y = chi_orb * E_x * self.chirality
        M_orb_z = 0.0

        return M_orb_x, M_orb_y, M_orb_z

    def calculate_energy_dispersion(self, k_max, num_points=100):
        """
        Calculate the energy dispersion relation for Rashba bands.

        Args:
            k_max (float): Maximum wavevector (m^-1)
            num_points (int): Number of points for the dispersion curve

        Returns:
            tuple: (k_values, E_plus, E_minus) where:
                k_values: Array of wavevector magnitudes
                E_plus: Energy for the upper Rashba band
                E_minus: Energy for the lower Rashba band
        """
        k_values = np.linspace(0, k_max, num_points)
        E_plus = (H_BAR**2 * k_values**2) / (2 * self.m_star) + self.alpha_R * k_values
        E_minus = (H_BAR**2 * k_values**2) / (2 * self.m_star) - self.alpha_R * k_values

        return k_values, E_plus, E_minus

    def calculate_spin_texture(self, k_max, num_points=50):
        """
        Calculate the spin texture for the Rashba bands.

        Args:
            k_max (float): Maximum wavevector (m^-1)
            num_points (int): Number of points for the texture

        Returns:
            tuple: (kx, ky, sx, sy, sz) where:
                kx, ky: Arrays of wavevector components
                sx, sy, sz: Arrays of spin expectation values
        """
        # Create a grid of k vectors
        k_values = np.linspace(0, k_max, num_points)
        angles = np.linspace(0, 2 * np.pi, num_points)
        kx, ky = np.meshgrid(k_values * np.cos(angles), k_values * np.sin(angles))

        # Calculate spin expectation values
        k_mag = np.sqrt(kx**2 + ky**2)
        phi_k = np.arctan2(ky, kx)

        # For the upper band (+ chirality)
        sx = np.sin(phi_k)
        sy = -np.cos(phi_k)
        sz = np.zeros_like(kx)

        return kx, ky, sx, sy, sz

def plot_energy_dispersion(model, k_max):
    """Plot the energy dispersion relation for Rashba bands."""
    k_values, E_plus, E_minus = model.calculate_energy_dispersion(k_max)

    plt.figure(figsize=(10, 6))
    plt.plot(k_values, E_plus / 1.602176634e-19, label='Upper Rashba band (+)')
    plt.plot(k_values, E_minus / 1.602176634e-19, label='Lower Rashba band (-)')
    plt.xlabel('Wavevector k (m$^{-1}$)')
    plt.ylabel('Energy (eV)')
    plt.title('Rashba Energy Dispersion')
    plt.legend()
    plt.grid(True)
    plt.show()

def plot_spin_texture(model, k_max):
    """Plot the spin texture for the Rashba bands."""
    kx, ky, sx, sy, sz = model.calculate_spin_texture(k_max)

    fig = plt.figure(figsize=(12, 6))

    # Plot spin texture
    ax1 = fig.add_subplot(121)
    ax1.quiver(kx, ky, sx, sy, color='r', scale=20)
    ax1.set_xlabel('k_x (m$^{-1}$)')
    ax1.set_ylabel('k_y (m$^{-1}$)')
    ax1.set_title('Spin Texture (Upper Band)')
    ax1.set_aspect('equal')
    ax1.grid(True)

    # Plot 3D spin vectors
    ax2 = fig.add_subplot(122, projection='3d')
    ax2.quiver(kx, ky, sz, sx, sy, sz, length=0.1, normalize=True, color='b')
    ax2.set_xlabel('k_x (m$^{-1}$)')
    ax2.set_ylabel('k_y (m$^{-1}$)')
    ax2.set_zlabel('k_z (m$^{-1}$)')
    ax2.set_title('3D Spin Vectors')
    plt.tight_layout()
    plt.show()

def plot_magnetization_vs_field(model, E_max):
    """Plot magnetization magnitude vs electric field strength."""
    E_values = np.linspace(0, E_max, 100)
    M_magnitudes = []

    for E in E_values:
        M_x, M_y, M_z = model.calculate_magnetization(E, 0)
        M_magnitude = np.sqrt(M_x**2 + M_y**2 + M_z**2)
        M_magnitudes.append(M_magnitude)

    plt.figure(figsize=(10, 6))
    plt.plot(E_values, M_magnitudes)
    plt.xlabel('Electric Field Strength (V/m)')
    plt.ylabel('Magnetization Magnitude (A/m)')
    plt.title('Magnetization vs Electric Field')
    plt.grid(True)
    plt.show()

def plot_magnetization_direction(model, E_max):
    """Plot magnetization direction for different electric field directions."""
    angles = np.linspace(0, 2 * np.pi, 50)
    E_magnitude = E_max
    M_x_values = []
    M_y_values = []

    for angle in angles:
        E_x = E_magnitude * np.cos(angle)
        E_y = E_magnitude * np.sin(angle)
        M_x, M_y, M_z = model.calculate_magnetization(E_x, E_y)
        M_x_values.append(M_x)
        M_y_values.append(M_y)

    plt.figure(figsize=(10, 6))
    plt.quiver([0] * len(angles), [0] * len(angles),
               M_x_values, M_y_values, angles='xy', scale_units='xy', scale=1)
    plt.xlabel('M_x (A/m)')
    plt.ylabel('M_y (A/m)')
    plt.title('Magnetization Direction for Different Electric Field Directions')
    plt.grid(True)
    plt.axis('equal')
    plt.show()

def main():
    """Main function to demonstrate the Edelstein effect model."""
    # Example parameters for a typical Rashba system
    # Convert units as needed (eV·Å to J·m, etc.)
    alpha_R = 0.1  # Rashba coupling strength (eV·Å)
    m_star = 0.05 * ELECTRON_MASS  # Effective mass (kg)
    n = 1e16  # Electron density (m^-2)
    tau = 1e-12  # Relaxation time (s)
    v_F = 1e6  # Fermi velocity (m/s)

    # Create the model
    model = RashbaEdelsteinModel(alpha_R, m_star, n, tau, v_F, chirality=1)

    # Print model parameters
    print("Rashba Edelstein Model Parameters:")
    print(f"Rashba coupling strength (α_R): {alpha_R} eV·Å")
    print(f"Effective mass (m*): {m_star/ELECTRON_MASS:.2f} m_e")
    print(f"Electron density (n): {n:.2e} m^-2")
    print(f"Relaxation time (τ): {tau:.2e} s")
    print(f"Fermi velocity (v_F): {v_F:.2e} m/s")
    print(f"Chirality: {model.chirality}")

    # Calculate and print spin polarization for example electric fields
    print("\nSpin Polarization for Different Electric Fields:")

    # Case 1: Electric field in x-direction
    E_x = 1e3  # V/m
    E_y = 0
    S_x, S_y, S_z = model.calculate_spin_polarization(E_x, E_y)
    print(f"\nElectric field: E = ({E_x}, {E_y}) V/m")
    print(f"Spin polarization: S = ({S_x:.2e}, {S_y:.2e}, {S_z:.2e}) A/m²")

    # Case 2: Electric field in y-direction
    E_x = 0
    E_y = 1e3  # V/m
    S_x, S_y, S_z = model.calculate_spin_polarization(E_x, E_y)
    print(f"\nElectric field: E = ({E_x}, {E_y}) V/m")
    print(f"Spin polarization: S = ({S_x:.2e}, {S_y:.2e}, {S_z:.2e}) A/m²")

    # Case 3: Electric field at 45 degrees
    E_x = 1e3 / np.sqrt(2)
    E_y = 1e3 / np.sqrt(2)
    S_x, S_y, S_z = model.calculate_spin_polarization(E_x, E_y)
    print(f"\nElectric field: E = ({E_x:.2e}, {E_y:.2e}) V/m")
    print(f"Spin polarization: S = ({S_x:.2e}, {S_y:.2e}, {S_z:.2e}) A/m²")

    # Calculate magnetization
    M_x, M_y, M_z = model.calculate_magnetization(E_x, E_y)
    print(f"\nMagnetization: M = ({M_x:.2e}, {M_y:.2e}, {M_z:.2e}) A/m")

    # Calculate orbital magnetization
    M_orb_x, M_orb_y, M_orb_z = model.calculate_orbital_magnetization(E_x, E_y)
    print(f"Orbital magnetization: M_orb = ({M_orb_x:.2e}, {M_orb_y:.2e}, {M_orb_z:.2e}) A/m")

    # Plot energy dispersion
    k_max = 1e9  # m^-1
    plot_energy_dispersion(model, k_max)

    # Plot spin texture
    plot_spin_texture(model, k_max)

    # Plot magnetization vs field
    E_max = 1e4  # V/m
    plot_magnetization_vs_field(model, E_max)

    # Plot magnetization direction
    plot_magnetization_direction(model, E_max)

    # Demonstrate parameter dependence
    print("\nParameter Dependence Analysis:")

    # Vary Rashba coupling strength
    alpha_R_values = np.linspace(0.05, 0.2, 5)
    for alpha in alpha_R_values:
        temp_model = RashbaEdelsteinModel(alpha, m_star, n, tau, v_F, chirality=1)
        M_x, M_y, M_z = temp_model.calculate_magnetization(1e3, 0)
        print(f"α_R = {alpha} eV·Å → |M| = {np.sqrt(M_x**2 + M_y**2):.2e} A/m")

    # Vary Fermi velocity
    v_F_values = np.linspace(0.5e6, 2e6, 5)
    for vf in v_F_values:
        temp_model = RashbaEdelsteinModel(alpha_R, m_star, n, tau, vf, chirality=1)
        M_x, M_y, M_z = temp_model.calculate_magnetization(1e3, 0)
        print(f"v_F = {vf:.1e} m/s → |M| = {np.sqrt(M_x**2 + M_y**2):.2e} A/m")

if __name__ == "__main__":
    main()

import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Constants in SI units
e = 1.602e-19  # Elementary charge (C)
hbar = 1.055e-34  # Reduced Planck's constant (J·s)
m_e = 9.109e-31  # Electron mass (kg)

def convert_alpha_R(alpha_R_eV_Ang):
    """Convert Rashba coupling from eV·Å to J·m"""
    return alpha_R_eV_Ang * 1.602e-19 * 1e-10

def calculate_magnetization(alpha_R, v_F, E, chirality=1):
    """
    Calculate Edelstein magnetization for Rashba fermions at Gamma point.

    Parameters:
    alpha_R (float): Rashba coupling in J·m
    v_F (float): Fermi velocity in m/s
    E (array): Electric field vector [Ex, Ey, Ez] in V/m
    chirality (int): +1 or -1 for handedness

    Returns:
    M (array): Magnetization vector [Mx, My, Mz] in A/m
    """
    # Calculate prefactor
    prefactor = (e * alpha_R) / (2 * np.pi * hbar**2 * v_F**2)

    # Cross product z_hat × E
    z_hat = np.array([0, 0, 1])
    cross_product = np.cross(z_hat, E)

    # Apply chirality and prefactor
    M = chirality * prefactor * cross_product

    return M

def plot_magnetization_vs_field(alpha_R, v_F, E_magnitudes, chirality=1):
    """
    Plot magnetization magnitude vs electric field magnitude for different directions.

    Parameters:
    alpha_R (float): Rashba coupling in J·m
    v_F (float): Fermi velocity in m/s
    E_magnitudes (array): Electric field magnitudes in V/m
    chirality (int): +1 or -1 for handedness
    """
    # Create electric field vectors in different directions
    directions = [
        np.array([1, 0, 0]),  # x-direction
        np.array([0, 1, 0]),  # y-direction
        np.array([1, 1, 0])   # diagonal
    ]

    plt.figure(figsize=(10, 6))

    for i, direction in enumerate(directions):
        M_magnitudes = []
        for E_mag in E_magnitudes:
            E = E_mag * direction
            M = calculate_magnetization(alpha_R, v_F, E, chirality)
            M_magnitudes.append(np.linalg.norm(M))

        plt.plot(E_magnitudes, M_magnitudes, 'o-', label=f'E {direction}')

    plt.xlabel('Electric Field Magnitude (V/m)')
    plt.ylabel('Magnetization Magnitude (A/m)')
    plt.title('Edelstein Effect: Magnetization vs Electric Field')
    plt.legend()
    plt.grid(True)
    plt.show()

def plot_magnetization_direction(alpha_R, v_F, E_magnitude, chirality=1):
    """
    Plot magnetization direction for different electric field directions.

    Parameters:
    alpha_R (float): Rashba coupling in J·m
    v_F (float): Fermi velocity in m/s
    E_magnitude (float): Electric field magnitude in V/m
    chirality (int): +1 or -1 for handedness
    """
    # Create a grid of electric field directions
    theta = np.linspace(0, 2*np.pi, 50)
    E_directions = np.array([np.cos(theta), np.sin(theta), np.zeros_like(theta)])

    # Calculate magnetization for each direction
    M_vectors = np.zeros_like(E_directions)
    for i in range(len(theta)):
        E = E_magnitude * E_directions[:, i]
        M = calculate_magnetization(alpha_R, v_F, E, chirality)
        M_vectors[:, i] = M

    # Plot the results
    fig = plt.figure(figsize=(12, 6))

    # Electric field directions
    ax1 = fig.add_subplot(121)
    ax1.quiver(0, 0, E_directions[0], E_directions[1], angles='xy', scale_units='xy', scale=1, color='blue')
    ax1.set_xlim(-1.5, 1.5)
    ax1.set_ylim(-1.5, 1.5)
    ax1.set_title('Electric Field Directions')
    ax1.set_xlabel('Ex')
    ax1.set_ylabel('Ey')
    ax1.grid(True)

    # Magnetization directions
    ax2 = fig.add_subplot(122)
    ax2.quiver(0, 0, M_vectors[0], M_vectors[1], angles='xy', scale_units='xy', scale=1, color='red')
    ax2.set_xlim(-1.5, 1.5)
    ax2.set_ylim(-1.5, 1.5)
    ax2.set_title('Magnetization Directions')
    ax2.set_xlabel('Mx')
    ax2.set_ylabel('My')
    ax2.grid(True)

    plt.tight_layout()
    plt.show()

def parameter_sensitivity(alpha_R_values, v_F_values, E_magnitude, chirality=1):
    """
    Analyze parameter sensitivity of the Edelstein effect.

    Parameters:
    alpha_R_values (array): Rashba coupling values in J·m
    v_F_values (array): Fermi velocity values in m/s
    E_magnitude (float): Electric field magnitude in V/m
    chirality (int): +1 or -1 for handedness
    """
    # Fixed electric field direction (x-axis)
    E = np.array([E_magnitude, 0, 0])

    # Calculate magnetization for different alpha_R
    M_alpha = []
    for alpha in alpha_R_values:
        M = calculate_magnetization(alpha, v_F_values[0], E, chirality)
        M_alpha.append(np.linalg.norm(M))

    # Calculate magnetization for different v_F
    M_vF = []
    for vf in v_F_values:
        M = calculate_magnetization(alpha_R_values[0], vf, E, chirality)
        M_vF.append(np.linalg.norm(M))

    # Plot results
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 5))

    # Alpha_R dependence
    ax1.plot(alpha_R_values, M_alpha, 'o-')
    ax1.set_xlabel('Rashba Coupling (J·m)')
    ax1.set_ylabel('Magnetization (A/m)')
    ax1.set_title('Magnetization vs Rashba Coupling')
    ax1.grid(True)

    # v_F dependence
    ax2.plot(v_F_values, M_vF, 'o-')
    ax2.set_xlabel('Fermi Velocity (m/s)')
    ax2.set_ylabel('Magnetization (A/m)')
    ax2.set_title('Magnetization vs Fermi Velocity')
    ax2.grid(True)

    plt.tight_layout()
    plt.show()

# Example usage and demonstration
if __name__ == "__main__":
    # Convert typical Rashba coupling from eV·Å to J·m
    alpha_R_eV_Ang = 1.0  # eV·Å
    alpha_R = convert_alpha_R(alpha_R_eV_Ang)

    # Typical Fermi velocity
    v_F = 1e6  # m/s

    # Electric field magnitudes to test
    E_magnitudes = np.logspace(3, 6, 10)  # 10^3 to 10^6 V/m

    # Parameter ranges for sensitivity analysis
    alpha_R_values = np.linspace(0.5, 2.0, 5) * convert_alpha_R(1.0)  # J·m
    v_F_values = np.linspace(0.5, 2.0, 5) * 1e6  # m/s

    print("=== Edelstein Effect Calculation ===")
    print(f"Rashba coupling: {alpha_R_eV_Ang} eV·Å = {alpha_R:.2e} J·m")
    print(f"Fermi velocity: {v_F:.2e} m/s")
    print(f"Electric field range: {E_magnitudes[0]:.2e} to {E_magnitudes[-1]:.2e} V/m")

    # Calculate magnetization for a specific case
    E_example = np.array([1e5, 0, 0])  # 10^5 V/m in x-direction
    M_example = calculate_magnetization(alpha_R, v_F, E_example, chirality=1)
    print(f"\nExample calculation:")
    print(f"Electric field: {E_example} V/m")
    print(f"Magnetization: {M_example} A/m")
    print(f"Magnetization magnitude: {np.linalg.norm(M_example):.2e} A/m")

    # Plot magnetization vs electric field
    print("\nPlotting magnetization vs electric field...")
    plot_magnetization_vs_field(alpha_R, v_F, E_magnitudes, chirality=1)

    # Plot magnetization direction
    print("\nPlotting magnetization direction...")
    plot_magnetization_direction(alpha_R, v_F, E_magnitude=1e5, chirality=1)

    # Parameter sensitivity analysis
    print("\nAnalyzing parameter sensitivity...")
    parameter_sensitivity(alpha_R_values, v_F_values, E_magnitude=1e5, chirality=1)
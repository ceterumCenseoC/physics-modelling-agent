
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Constants in SI units
hbar = 1.055e-34  # Reduced Planck constant (J·s)
e = 1.602e-19     # Elementary charge (C)
mu_B = 9.274e-24  # Bohr magneton (J/T)
g_s = 2.0         # Electron g-factor
m_e = 9.109e-31   # Electron mass (kg)

# Material parameters (typical values for 2D electron gas)
alpha_R = 5.0e-11  # Rashba coupling strength (J·m)
tau = 1.0e-12      # Relaxation time (s)
v_F = 5.0e5        # Fermi velocity (m/s)
n_2D = 1.0e15      # 2D electron density (m⁻²)

# Function to calculate magnetization
def calculate_magnetization(E_vector, alpha_R, tau, v_F, n_2D):
    """
    Calculate magnetization vector for given electric field and material parameters.

    Parameters:
    E_vector : array-like
        Applied electric field vector [E_x, E_y, E_z] in V/m
    alpha_R : float
        Rashba coupling strength in J·m
    tau : float
        Relaxation time in s
    v_F : float
        Fermi velocity in m/s
    n_2D : float
        2D electron density in m⁻²

    Returns:
    M_vector : array
        Magnetization vector [M_x, M_y, M_z] in A/m
    """
    E_vector = np.array(E_vector)
    z_hat = np.array([0, 0, 1])
    E_cross_z = np.cross(E_vector, z_hat)

    # Calculate magnetization magnitude
    M_magnitude = (g_s * e * mu_B * alpha_R * tau * n_2D) / (hbar * v_F) * np.linalg.norm(E_vector)

    # Calculate magnetization vector (in-plane only)
    if np.linalg.norm(E_cross_z) > 0:
        M_vector = M_magnitude * (E_cross_z / np.linalg.norm(E_cross_z))
    else:
        M_vector = np.array([0, 0, 0])

    return M_vector

# Function to plot magnetization vs electric field
def plot_magnetization_vs_field(E_range, alpha_R, tau, v_F, n_2D):
    """
    Plot magnetization magnitude vs electric field strength.

    Parameters:
    E_range : array
        Range of electric field magnitudes in V/m
    alpha_R, tau, v_F, n_2D : floats
        Material parameters
    """
    M_magnitudes = []
    for E in E_range:
        E_vector = np.array([E, 0, 0])  # Field along x-axis
        M_vector = calculate_magnetization(E_vector, alpha_R, tau, v_F, n_2D)
        M_magnitudes.append(np.linalg.norm(M_vector))

    plt.figure(figsize=(10, 6))
    plt.plot(E_range, M_magnitudes, 'b-', linewidth=2)
    plt.title('Magnetization vs Electric Field Strength')
    plt.xlabel('Electric Field (V/m)')
    plt.ylabel('Magnetization Magnitude (A/m)')
    plt.grid(True)
    plt.show()

# Function to plot magnetization direction
def plot_magnetization_direction(E_magnitude, alpha_R, tau, v_F, n_2D):
    """
    Plot magnetization direction for different electric field directions.

    Parameters:
    E_magnitude : float
        Magnitude of electric field in V/m
    alpha_R, tau, v_F, n_2D : floats
        Material parameters
    """
    angles = np.linspace(0, 2*np.pi, 100)
    M_vectors = []

    for angle in angles:
        E_vector = E_magnitude * np.array([np.cos(angle), np.sin(angle), 0])
        M_vector = calculate_magnetization(E_vector, alpha_R, tau, v_F, n_2D)
        M_vectors.append(M_vector)

    M_vectors = np.array(M_vectors)

    plt.figure(figsize=(10, 6))
    plt.quiver([0]*len(angles), [0]*len(angles),
               M_vectors[:, 0], M_vectors[:, 1],
               angles='xy', scale_units='xy', scale=1, color='r')
    plt.title('Magnetization Direction for Different Electric Field Directions')
    plt.xlabel('M_x (A/m)')
    plt.ylabel('M_y (A/m)')
    plt.axis('equal')
    plt.grid(True)
    plt.show()

# Function to analyze parameter dependencies
def analyze_parameter_dependencies(E_magnitude, alpha_R, tau, v_F, n_2D):
    """
    Analyze how magnetization depends on different parameters.

    Parameters:
    E_magnitude, alpha_R, tau, v_F, n_2D : floats
        Base values for parameters
    """
    # Create parameter ranges
    alpha_range = np.linspace(1e-11, 1e-10, 50)
    tau_range = np.linspace(1e-13, 1e-11, 50)
    vF_range = np.linspace(1e5, 1e6, 50)
    n2D_range = np.linspace(1e14, 1e16, 50)

    # Calculate magnetization for each parameter sweep
    M_alpha = [np.linalg.norm(calculate_magnetization([E_magnitude, 0, 0], a, tau, v_F, n_2D)) for a in alpha_range]
    M_tau = [np.linalg.norm(calculate_magnetization([E_magnitude, 0, 0], alpha_R, t, v_F, n_2D)) for t in tau_range]
    M_vF = [np.linalg.norm(calculate_magnetization([E_magnitude, 0, 0], alpha_R, tau, v, n_2D)) for v in vF_range]
    M_n2D = [np.linalg.norm(calculate_magnetization([E_magnitude, 0, 0], alpha_R, tau, v_F, n)) for n in n2D_range]

    # Plot results
    plt.figure(figsize=(15, 10))

    plt.subplot(2, 2, 1)
    plt.plot(alpha_range, M_alpha, 'r-')
    plt.title('Magnetization vs Rashba Coupling')
    plt.xlabel('α_R (J·m)')
    plt.ylabel('|M| (A/m)')
    plt.grid(True)

    plt.subplot(2, 2, 2)
    plt.plot(tau_range, M_tau, 'g-')
    plt.title('Magnetization vs Relaxation Time')
    plt.xlabel('τ (s)')
    plt.ylabel('|M| (A/m)')
    plt.grid(True)

    plt.subplot(2, 2, 3)
    plt.plot(vF_range, M_vF, 'b-')
    plt.title('Magnetization vs Fermi Velocity')
    plt.xlabel('v_F (m/s)')
    plt.ylabel('|M| (A/m)')
    plt.grid(True)

    plt.subplot(2, 2, 4)
    plt.plot(n2D_range, M_n2D, 'm-')
    plt.title('Magnetization vs 2D Density')
    plt.xlabel('n_2D (m⁻²)')
    plt.ylabel('|M| (A/m)')
    plt.grid(True)

    plt.tight_layout()
    plt.show()

# Example usage
if __name__ == "__main__":
    # Base parameters
    E_magnitude = 100.0  # V/m
    alpha_R = 5.0e-11    # J·m
    tau = 1.0e-12        # s
    v_F = 5.0e5          # m/s
    n_2D = 1.0e15        # m⁻²

    # Calculate magnetization for a specific field
    E_vector = [E_magnitude, 0, 0]  # Field along x-axis
    M_vector = calculate_magnetization(E_vector, alpha_R, tau, v_F, n_2D)
    print(f"Magnetization vector: {M_vector} A/m")
    print(f"Magnetization magnitude: {np.linalg.norm(M_vector):.2e} A/m")

    # Plot magnetization vs electric field strength
    E_range = np.linspace(10, 1000, 50)
    plot_magnetization_vs_field(E_range, alpha_R, tau, v_F, n_2D)

    # Plot magnetization direction for different field directions
    plot_magnetization_direction(E_magnitude, alpha_R, tau, v_F, n_2D)

    # Analyze parameter dependencies
    analyze_parameter_dependencies(E_magnitude, alpha_R, tau, v_F, n_2D)
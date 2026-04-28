```python
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm
from matplotlib.colors import Normalize

# Constants
hbar = 1.0545718e-34  # Reduced Planck constant (J·s)
e = 1.602176634e-19   # Elementary charge (C)
m_e = 9.1093837015e-31 # Electron mass (kg)

# Default parameters (SI units)
params = {
    'alpha_R': 1.0e-11,    # Rashba coupling strength (J·m)
    'm_star': 0.05 * m_e,   # Effective mass (kg)
    'E_F': 1.0e-20,         # Fermi energy (J)
    'tau': 1.0e-12,         # Relaxation time (s)
    'chi': 1,               # Chirality (+1 or -1)
    'E_mag': 1.0e4,         # Electric field magnitude (V/m)
    'E_angle': 0.0          # Electric field angle (radians)
}

def calculate_magnetization(params):
    """
    Calculate magnetization for Rashba fermion at Gamma point using Edelstein effect.

    Parameters:
    -----------
    params : dict
        Dictionary containing model parameters:
        - alpha_R: Rashba coupling strength (J·m)
        - m_star: Effective mass (kg)
        - E_F: Fermi energy (J)
        - tau: Relaxation time (s)
        - chi: Chirality (+1 or -1)
        - E_mag: Electric field magnitude (V/m)
        - E_angle: Electric field angle (radians)

    Returns:
    --------
    M : numpy.ndarray
        Magnetization vector [M_x, M_y, M_z] (A/m)
    """
    # Extract parameters
    alpha_R = params['alpha_R']
    m_star = params['m_star']
    E_F = params['E_F']
    tau = params['tau']
    chi = params['chi']
    E_mag = params['E_mag']
    E_angle = params['E_angle']

    # Calculate Fermi wavevector
    k_F = np.sqrt(2 * m_star * E_F) / hbar

    # Calculate Edelstein coefficient (simplified form for single branch)
    gamma = chi * e * tau * alpha_R * m_star / (2 * np.pi * hbar**3)

    # Electric field components
    E_x = E_mag * np.cos(E_angle)
    E_y = E_mag * np.sin(E_angle)
    E_z = 0.0

    # Magnetization components (M = gamma * (E × z_hat))
    M_x = gamma * E_y
    M_y = -gamma * E_x
    M_z = 0.0

    return np.array([M_x, M_y, M_z])

def calculate_fermi_velocity(params):
    """
    Calculate Fermi velocity for Rashba fermion.

    Parameters:
    -----------
    params : dict
        Dictionary containing model parameters

    Returns:
    --------
    v_F : float
        Fermi velocity (m/s)
    """
    alpha_R = params['alpha_R']
    m_star = params['m_star']
    E_F = params['E_F']

    k_F = np.sqrt(2 * m_star * E_F) / hbar
    v_F = (hbar * k_F) / m_star + alpha_R / hbar

    return v_F

def plot_magnetization_vs_field(params, E_mag_range=np.linspace(1e3, 1e5, 100)):
    """
    Plot magnetization magnitude vs electric field magnitude.

    Parameters:
    -----------
    params : dict
        Dictionary containing model parameters
    E_mag_range : numpy.ndarray
        Range of electric field magnitudes to plot (V/m)
    """
    # Create figure
    plt.figure(figsize=(10, 6))

    # Calculate magnetization for different field magnitudes
    M_mags = []
    for E_mag in E_mag_range:
        params['E_mag'] = E_mag
        M = calculate_magnetization(params)
        M_mags.append(np.linalg.norm(M))

    # Plot
    plt.plot(E_mag_range, M_mags, 'b-', linewidth=2)
    plt.xlabel('Electric Field Magnitude (V/m)', fontsize=12)
    plt.ylabel('Magnetization Magnitude (A/m)', fontsize=12)
    plt.title('Magnetization vs Electric Field Magnitude', fontsize=14)
    plt.grid(True, alpha=0.3)
    plt.tight_layout()
    plt.show()

def plot_magnetization_direction(params, angles=np.linspace(0, 2*np.pi, 100)):
    """
    Plot magnetization direction as electric field direction changes.

    Parameters:
    -----------
    params : dict
        Dictionary containing model parameters
    angles : numpy.ndarray
        Range of electric field angles to plot (radians)
    """
    # Create figure
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 6))

    # Calculate magnetization for different field directions
    M_x = []
    M_y = []
    for angle in angles:
        params['E_angle'] = angle
        M = calculate_magnetization(params)
        M_x.append(M[0])
        M_y.append(M[1])

    # Plot magnetization components
    ax1.plot(angles, M_x, 'r-', label='M_x', linewidth=2)
    ax1.plot(angles, M_y, 'b-', label='M_y', linewidth=2)
    ax1.set_xlabel('Electric Field Angle (radians)', fontsize=12)
    ax1.set_ylabel('Magnetization Component (A/m)', fontsize=12)
    ax1.set_title('Magnetization Components vs Field Direction', fontsize=14)
    ax1.legend(fontsize=12)
    ax1.grid(True, alpha=0.3)

    # Plot magnetization direction (polar plot)
    ax2.quiver([0], [0], [M_x[0]], [M_y[0]], angles='xy', scale_units='xy', scale=1, color='g', width=0.005)
    ax2.plot(M_x, M_y, 'g-', linewidth=2)
    ax2.set_xlabel('M_x (A/m)', fontsize=12)
    ax2.set_ylabel('M_y (A/m)', fontsize=12)
    ax2.set_title('Magnetization Direction', fontsize=14)
    ax2.grid(True, alpha=0.3)
    ax2.axis('equal')

    plt.tight_layout()
    plt.show()

def plot_parameter_dependence(params, param_name, param_values, fixed_params=None):
    """
    Plot magnetization dependence on a specific parameter.

    Parameters:
    -----------
    params : dict
        Dictionary containing model parameters
    param_name : str
        Name of parameter to vary
    param_values : numpy.ndarray
        Range of values for the parameter
    fixed_params : dict, optional
        Fixed parameters (overrides params)
    """
    if fixed_params is None:
        fixed_params = params.copy()
    else:
        fixed_params = fixed_params.copy()

    # Create figure
    plt.figure(figsize=(10, 6))

    # Calculate magnetization for different parameter values
    M_mags = []
    for value in param_values:
        fixed_params[param_name] = value
        M = calculate_magnetization(fixed_params)
        M_mags.append(np.linalg.norm(M))

    # Plot
    plt.plot(param_values, M_mags, 'b-', linewidth=2)
    plt.xlabel(f'{param_name}', fontsize=12)
    plt.ylabel('Magnetization Magnitude (A/m)', fontsize=12)
    plt.title(f'Magnetization vs {param_name}', fontsize=14)
    plt.grid(True, alpha=0.3)
    plt.tight_layout()
    plt.show()

def plot_2d_parameter_space(params, param1_name, param1_values, param2_name, param2_values):
    """
    Create a 2D plot showing magnetization magnitude over a parameter space.

    Parameters:
    -----------
    params : dict
        Dictionary containing model parameters
    param1_name : str
        Name of first parameter to vary
    param1_values : numpy.ndarray
        Range of values for first parameter
    param2_name : str
        Name of second parameter to vary
    param2_values : numpy.ndarray
        Range of values for second parameter
    """
    # Create meshgrid
    X, Y = np.meshgrid(param1_values, param2_values)
    Z = np.zeros_like(X)

    # Calculate magnetization for each parameter combination
    for i, x_val in enumerate(param1_values):
        for j, y_val in enumerate(param2_values):
            temp_params = params.copy()
            temp_params[param1_name] = x_val
            temp_params[param2_name] = y_val
            M = calculate_magnetization(temp_params)
            Z[j, i] = np.linalg.norm(M)

    # Create figure
    plt.figure(figsize=(12, 8))

    # Create colormap
    norm = Normalize(vmin=Z.min(), vmax=Z.max())
    colors = cm.viridis(norm(Z))

    # Plot surface
    surf = plt.contourf(X, Y, Z, levels=20, cmap='viridis')
    plt.colorbar(surf, label='Magnetization Magnitude (A/m)')

    plt.xlabel(f'{param1_name}', fontsize=12)
    plt.ylabel(f'{param2_name}', fontsize=12)
    plt.title(f'Magnetization vs {param1_name} and {param2_name}', fontsize=14)
    plt.tight_layout()
    plt.show()

# Example usage and demonstration
if __name__ == "__main__":
    print("Edelstein Effect for Rashba Fermion - Numerical Implementation")
    print("=" * 60)

    # Display default parameters
    print("\nDefault Parameters:")
    for key, value in params.items():
        print(f"{key}: {value}")

    # Calculate and display magnetization for default parameters
    M = calculate_magnetization(params)
    print(f"\nMagnetization for default parameters: {M} A/m")
    print(f"Magnetization magnitude: {np.linalg.norm(M):.2e} A/m")

    # Calculate and display Fermi velocity
    v_F = calculate_fermi_velocity(params)
    print(f"\nFermi velocity: {v_F:.2e} m/s")

    # Generate plots
    print("\nGenerating plots...")

    # Plot magnetization vs electric field magnitude
    print("1. Magnetization vs Electric Field Magnitude")
    plot_magnetization_vs_field(params)

    # Plot magnetization direction
    print("2. Magnetization Direction vs Field Direction")
    plot_magnetization_direction(params)

    # Plot parameter dependence (Rashba coupling)
    print("3. Magnetization vs Rashba Coupling Strength")
    alpha_R_values = np.linspace(0.5e-11, 2.0e-11, 50)
    plot_parameter_dependence(params, 'alpha_R', alpha_R_values)

    # Plot parameter dependence (Fermi energy)
    print("4. Magnetization vs Fermi Energy")
    E_F_values = np.linspace(0.5e-20, 2.0e-20, 50)
    plot_parameter_dependence(params, 'E_F', E_F_values)

    # Plot 2D parameter space (Rashba coupling vs Fermi energy)
    print("5. Magnetization in Rashba Coupling - Fermi Energy Space")
    alpha_R_2d = np.linspace(0.5e-11, 2.0e-11, 30)
    E_F_2d = np.linspace(0.5e-20, 2.0e-20, 30)
    plot_2d_parameter_space(params, 'alpha_R', alpha_R_2d, 'E_F', E_F_2d)

    print("\nPlots generated successfully!")
```
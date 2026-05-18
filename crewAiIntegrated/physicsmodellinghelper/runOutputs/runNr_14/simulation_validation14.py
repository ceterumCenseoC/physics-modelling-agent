import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Constants in SI units
H_BAR = 1.0545718e-34  # Reduced Planck constant [J·s]
ELECTRON_CHARGE = 1.602176634e-19  # Elementary charge [C]
ELECTRON_MASS = 9.10938356e-31  # Electron mass [kg]
MEV_TO_JOULE = 1.602176634e-22  # Conversion factor [J/meV]
EV_ANGSTROM_TO_JOULE_METER = 1.602176634e-19 * 1e-10  # Conversion factor [J·m/(eV·Å)]

def calculate_magnetization(alpha_R, m_star, tau, E_field, E_F, regime='HDR'):
    """
    Calculate the magnetization magnitude for the Edelstein effect in a Rashba fermion system.

    Parameters:
    alpha_R (float): Rashba coupling strength [J·m]
    m_star (float): Effective mass [kg]
    tau (float): Scattering time [s]
    E_field (float): Electric field magnitude [V/m]
    E_F (float): Fermi energy [J]
    regime (str): 'HDR' for High-Density Regime, 'LDR' for Low-Density Regime

    Returns:
    M (float): Magnetization magnitude [A/m]
    """
    if regime == 'HDR':
        # High-Density Regime formula
        M = (ELECTRON_CHARGE * tau * alpha_R * m_star) / (2 * np.pi * H_BAR**2) * E_field
    elif regime == 'LDR':
        # Low-Density Regime formula
        M = (ELECTRON_CHARGE * tau) / (2 * np.pi * H_BAR**2) * np.sqrt((m_star**2 * alpha_R**2) + (2 * m_star * E_F)) * E_field
    else:
        raise ValueError("Regime must be either 'HDR' or 'LDR'")

    return M

def magnetization_direction(E_field_direction):
    """
    Determine the magnetization direction based on the electric field direction.

    Parameters:
    E_field_direction (str): Direction of electric field ('x', 'y', or 'z')

    Returns:
    direction (str): Magnetization direction
    """
    if E_field_direction.lower() == 'x':
        return 'y'
    elif E_field_direction.lower() == 'y':
        return '-x'
    elif E_field_direction.lower() == 'z':
        return '0'  # No magnetization if E is along z
    else:
        raise ValueError("Electric field direction must be 'x', 'y', or 'z'")

def plot_magnetization_vs_parameters():
    """
    Plot magnetization magnitude vs. key parameters (Rashba coupling, effective mass, scattering time, electric field).
    """
    # Base parameters
    alpha_R_base = 1e-11  # J·m
    m_star_base = 0.1 * ELECTRON_MASS  # kg
    tau_base = 1e-12  # s
    E_field_base = 1e5  # V/m
    E_F_base = 10 * MEV_TO_JOULE  # J (10 meV)

    # Parameter ranges
    alpha_R_values = np.linspace(0.5e-11, 2e-11, 100)  # J·m
    m_star_values = np.linspace(0.05 * ELECTRON_MASS, 0.2 * ELECTRON_MASS, 100)  # kg
    tau_values = np.linspace(0.5e-12, 2e-12, 100)  # s
    E_field_values = np.linspace(0.5e5, 2e5, 100)  # V/m

    # Calculate magnetization for each parameter variation
    M_alpha = [calculate_magnetization(alpha, m_star_base, tau_base, E_field_base, E_F_base, 'HDR') for alpha in alpha_R_values]
    M_mass = [calculate_magnetization(alpha_R_base, m, tau_base, E_field_base, E_F_base, 'HDR') for m in m_star_values]
    M_tau = [calculate_magnetization(alpha_R_base, m_star_base, tau, E_field_base, E_F_base, 'HDR') for tau in tau_values]
    M_E = [calculate_magnetization(alpha_R_base, m_star_base, tau_base, E, E_F_base, 'HDR') for E in E_field_values]

    # Plotting
    plt.figure(figsize=(15, 10))

    # Magnetization vs Rashba coupling
    plt.subplot(2, 2, 1)
    plt.plot(alpha_R_values / EV_ANGSTROM_TO_JOULE_METER, M_alpha, 'b-', linewidth=2)
    plt.xlabel('Rashba Coupling Strength [eV·Å]')
    plt.ylabel('Magnetization [A/m]')
    plt.title('Magnetization vs Rashba Coupling')
    plt.grid(True)

    # Magnetization vs Effective mass
    plt.subplot(2, 2, 2)
    plt.plot(m_star_values / ELECTRON_MASS, M_mass, 'r-', linewidth=2)
    plt.xlabel('Effective Mass [m_e]')
    plt.ylabel('Magnetization [A/m]')
    plt.title('Magnetization vs Effective Mass')
    plt.grid(True)

    # Magnetization vs Scattering time
    plt.subplot(2, 2, 3)
    plt.plot(tau_values * 1e12, M_tau, 'g-', linewidth=2)
    plt.xlabel('Scattering Time [ps]')
    plt.ylabel('Magnetization [A/m]')
    plt.title('Magnetization vs Scattering Time')
    plt.grid(True)

    # Magnetization vs Electric field
    plt.subplot(2, 2, 4)
    plt.plot(E_field_values, M_E, 'm-', linewidth=2)
    plt.xlabel('Electric Field [V/m]')
    plt.ylabel('Magnetization [A/m]')
    plt.title('Magnetization vs Electric Field')
    plt.grid(True)

    plt.tight_layout()
    plt.show()

def plot_3d_magnetization_surface():
    """
    Create a 3D surface plot showing magnetization as a function of Rashba coupling and electric field.
    """
    # Parameter ranges
    alpha_R_values = np.linspace(0.5e-11, 2e-11, 50)  # J·m
    E_field_values = np.linspace(0.5e5, 2e5, 50)  # V/m

    # Base parameters
    m_star = 0.1 * ELECTRON_MASS  # kg
    tau = 1e-12  # s
    E_F = 10 * MEV_TO_JOULE  # J (10 meV)

    # Create meshgrid
    Alpha, E = np.meshgrid(alpha_R_values, E_field_values)

    # Calculate magnetization
    M = np.zeros_like(Alpha)
    for i in range(len(alpha_R_values)):
        for j in range(len(E_field_values)):
            M[j, i] = calculate_magnetization(Alpha[j, i], m_star, tau, E[j, i], E_F, 'HDR')

    # Plotting
    fig = plt.figure(figsize=(10, 8))
    ax = fig.add_subplot(111, projection='3d')

    # Convert units for labeling
    alpha_R_eV_A = alpha_R_values / EV_ANGSTROM_TO_JOULE_METER
    E_field_kV_m = E_field_values / 1e3

    surf = ax.plot_surface(Alpha / EV_ANGSTROM_TO_JOULE_METER, E / 1e3, M, cmap='viridis', rstride=1, cstride=1)

    ax.set_xlabel('Rashba Coupling [eV·Å]')
    ax.set_ylabel('Electric Field [kV/m]')
    ax.set_zlabel('Magnetization [A/m]')
    ax.set_title('Magnetization vs Rashba Coupling and Electric Field')
    fig.colorbar(surf, ax=ax, shrink=0.5, aspect=5)
    plt.show()

def compare_regimes():
    """
    Compare magnetization in High-Density Regime (HDR) and Low-Density Regime (LDR).
    """
    # Base parameters
    alpha_R = 1e-11  # J·m
    m_star = 0.1 * ELECTRON_MASS  # kg
    tau = 1e-12  # s
    E_field = 1e5  # V/m

    # Fermi energy range (convert from meV to J)
    E_F_values_meV = np.linspace(0.1, 50, 100)  # meV
    E_F_values = E_F_values_meV * MEV_TO_JOULE  # J

    # Calculate magnetization for both regimes
    M_HDR = []
    M_LDR = []

    for E_F in E_F_values:
        try:
            M_HDR.append(calculate_magnetization(alpha_R, m_star, tau, E_field, E_F, 'HDR'))
        except:
            M_HDR.append(np.nan)

        try:
            M_LDR.append(calculate_magnetization(alpha_R, m_star, tau, E_field, E_F, 'LDR'))
        except:
            M_LDR.append(np.nan)

    # Plotting
    plt.figure(figsize=(10, 6))
    plt.plot(E_F_values_meV, M_HDR, 'b-', linewidth=2, label='HDR')
    plt.plot(E_F_values_meV, M_LDR, 'r--', linewidth=2, label='LDR')
    plt.xlabel('Fermi Energy [meV]')
    plt.ylabel('Magnetization [A/m]')
    plt.title('Magnetization Comparison: HDR vs LDR')
    plt.legend()
    plt.grid(True)
    plt.show()

def main():
    """
    Main function to demonstrate the Edelstein effect calculations.
    """
    print("Edelstein Effect for Rashba Fermion at Gamma Point")
    print("=" * 50)

    # Example parameters (converted to SI units)
    alpha_R = 1e-30  # J·m (equivalent to ~0.624 eV·Å)
    m_star = 0.1 * ELECTRON_MASS  # kg (0.1 times electron mass)
    tau = 1e-12  # s (1 ps)
    E_field = 1e5  # V/m (100 V/cm)
    E_F = 10 * MEV_TO_JOULE  # J (10 meV)

    # Calculate magnetization for both regimes
    M_HDR = calculate_magnetization(alpha_R, m_star, tau, E_field, E_F, 'HDR')
    M_LDR = calculate_magnetization(alpha_R, m_star, tau, E_field, E_F, 'LDR')

    print(f"\nParameters:")
    print(f"Rashba coupling (α_R): {alpha_R / EV_ANGSTROM_TO_JOULE_METER:.3f} eV·Å")
    print(f"Effective mass (m*): {m_star / ELECTRON_MASS:.2f} m_e")
    print(f"Scattering time (τ): {tau * 1e12:.1f} ps")
    print(f"Electric field (E): {E_field:.0f} V/m")
    print(f"Fermi energy (E_F): {E_F / MEV_TO_JOULE:.1f} meV")

    print(f"\nResults:")
    print(f"Magnetization (HDR): {M_HDR:.2e} A/m")
    print(f"Magnetization (LDR): {M_LDR:.2e} A/m")

    # Determine direction for electric field in x-direction
    direction = magnetization_direction('x')
    print(f"Magnetization direction (E along x): {direction}")

    # Generate plots
    print("\nGenerating plots...")
    plot_magnetization_vs_parameters()
    plot_3d_magnetization_surface()
    compare_regimes()

if __name__ == "__main__":
    main()

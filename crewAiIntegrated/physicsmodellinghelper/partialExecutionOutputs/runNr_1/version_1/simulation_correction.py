import numpy as np
import matplotlib.pyplot as plt

# Constants
hbar = 1.0545718e-34  # Reduced Planck's constant [J·s]
m_e = 9.10938356e-31  # Electron mass [kg]
mu_b = 9.2740100783e-24  # Bohr magneton [J/T]
e = 1.602176634e-19  # Elementary charge [C]

def calculate_magnetization(E_field, alpha, m, tau, E_F, regime='HDR'):
    """
    Calculate the magnetization My based on the given regime.

    Parameters:
    E_field (float): Electric field strength [V/m]
    alpha (float): Rashba SOC strength [m/s]
    m (float): Effective mass [kg]
    tau (float): Transport lifetime [s]
    E_F (float): Fermi energy [J]
    regime (str): 'HDR' or 'LDR' (default: 'HDR')

    Returns:
    My (float): Magnetization in y-direction [J/T]
    """
    chi_0 = (tau * abs(e) * mu_b) / (2 * np.pi)

    if regime == 'HDR':
        My = chi_0 * m * alpha * E_field
    elif regime == 'LDR':
        sqrt_term = m**2 * alpha**2 + 2 * m * E_F
        My = chi_0 * np.sqrt(sqrt_term) * E_field
    else:
        raise ValueError("Invalid regime. Choose 'HDR' or 'LDR'.")

    return My

def calculate_susceptibility(alpha, m, tau, regime='HDR'):
    """
    Calculate the Edelstein susceptibility chi_xy.

    Parameters:
    alpha (float): Rashba SOC strength [m/s]
    m (float): Effective mass [kg]
    tau (float): Transport lifetime [s]
    regime (str): 'HDR' or 'LDR' (default: 'HDR')

    Returns:
    chi_xy (float): Susceptibility [SI units]
    """
    chi_0 = (tau * abs(e) * mu_b) / (2 * np.pi)

    if regime == 'HDR':
        chi_xy = chi_0 * m * alpha
    elif regime == 'LDR':
        chi_xy = chi_0 * np.sqrt(m**2 * alpha**2 + 2 * m * E_F)
    else:
        raise ValueError("Invalid regime. Choose 'HDR' or 'LDR'.")

    return chi_xy

def plot_susceptibility_vs_mu(alpha, m, tau, mu_range, regime='HDR'):
    """
    Plot susceptibility vs chemical potential.

    Parameters:
    alpha (float): Rashba SOC strength [m/s]
    m (float): Effective mass [kg]
    tau (float): Transport lifetime [s]
    mu_range (numpy array): Range of chemical potentials [J]
    regime (str): 'HDR' or 'LDR' (default: 'HDR')
    """
    chi_0 = (tau * abs(e) * mu_b) / (2 * np.pi)
    chi_values = []

    for mu in mu_range:
        if regime == 'HDR':
            chi = (m * alpha) / chi_0
        else:
            chi = np.sqrt(m**2 * alpha**2 + 2 * m * mu) / chi_0
        chi_values.append(chi)

    chi_values = np.array(chi_values)

    plt.figure(figsize=(10, 6))
    plt.plot(mu_range / e, chi_values, label=f'Regime: {regime}')
    plt.xlabel('Chemical Potential [eV]')
    plt.ylabel('Normalized Susceptibility [χ/χ0]')
    plt.title('Susceptibility vs Chemical Potential')
    plt.legend()
    plt.grid(True)
    plt.show()

def plot_susceptibility_vs_alpha(alpha_range, m, tau, regime='HDR'):
    """
    Plot susceptibility vs Rashba SOC strength alpha.

    Parameters:
    alpha_range (numpy array): Range of Rashba SOC strengths [m/s]
    m (float): Effective mass [kg]
    tau (float): Transport lifetime [s]
    regime (str): 'HDR' or 'LDR' (default: 'HDR')
    """
    chi_0 = (tau * abs(e) * mu_b) / (2 * np.pi)
    chi_values = []

    for alpha in alpha_range:
        if regime == 'HDR':
            chi = (m * alpha) / chi_0
        else:
            chi = np.sqrt(m**2 * alpha**2 + 2 * m * E_F) / chi_0
        chi_values.append(chi)

    chi_values = np.array(chi_values)

    plt.figure(figsize=(10, 6))
    plt.plot(alpha_range, chi_values, label=f'Regime: {regime}')
    plt.xlabel('Rashba SOC Strength [m/s]')
    plt.ylabel('Normalized Susceptibility [χ/χ0]')
    plt.title('Susceptibility vs Rashba SOC Strength')
    plt.legend()
    plt.grid(True)
    plt.show()

def plot_susceptibility_vs_anisotropy(r_range, type='mass', m=0.1*m_e, alpha=1e-11, tau=1e-12):
    """
    Plot susceptibility vs anisotropy ratio.

    Parameters:
    r_range (numpy array): Range of anisotropy ratios
    type (str): 'mass' or 'soc' (default: 'mass')
    m (float): Effective mass [kg]
    alpha (float): Rashba SOC strength [m/s]
    tau (float): Transport lifetime [s]
    """
    chi_0 = (tau * abs(e) * mu_b) / (2 * np.pi)
    chi_values = []

    for r in r_range:
        if type == 'mass':
            m_x = m
            m_y = r * m_x
            chi = (4 * np.pi * m_x * alpha * r) / (1 + np.sqrt(r))
        elif type == 'soc':
            alpha_x = alpha
            alpha_y = r * alpha_x
            chi = (4 * np.pi * m * alpha_x * r) / (1 + r)
        chi_values.append(chi / chi_0)

    chi_values = np.array(chi_values)

    plt.figure(figsize=(10, 6))
    plt.plot(r_range, chi_values, label=f'Anisotropy type: {type}')
    plt.xlabel('Anisotropy Ratio')
    plt.ylabel('Normalized Susceptibility [χ/χ0]')
    plt.title(f'Susceptibility vs {type.capitalize()} Anisotropy')
    plt.legend()
    plt.grid(True)
    plt.show()

def plot_fermi_surfaces_and_spin_textures(k_range=1e8, num_points=100):
    """
    Plot Fermi surfaces and spin textures in k-space.
    """
    theta = np.linspace(0, 2*np.pi, num_points)
    k_x = k_range * np.cos(theta)
    k_y = k_range * np.sin(theta)

    plt.figure(figsize=(10, 10))
    plt.quiver(k_x*1e-8, k_y*1e-8, -np.sin(theta), np.cos(theta), color='blue', label='Spin Texture')
    circle = plt.Circle((0, 0), k_range*1e-8, edgecolor='black', facecolor='none', lw=2, label='Fermi Circle')
    plt.gca().add_artist(circle)
    plt.xlabel('k_x [1e-8 m^{-1}]')
    plt.ylabel('k_y [1e-8 m^{-1}]')
    plt.title('Fermi Surface and Spin Texture')
    plt.legend()
    plt.grid(True)
    plt.show()

# Example usage
if __name__ == "__main__":
    # Parameters
    m = 0.1 * m_e  # Effective mass [kg]
    alpha = 1e-11  # Rashba SOC strength [m/s]
    tau = 1e-12  # Transport lifetime [s]
    E_field = 1e6  # Electric field [V/m]
    E_F = 1e-21  # Fermi energy [J]

    # Calculate magnetization
    My_HDR = calculate_magnetization(E_field, alpha, m, tau, E_F, regime='HDR')
    My_LDR = calculate_magnetization(E_field, alpha, m, tau, E_F, regime='LDR')
    print(f"Magnetization (HDR): {My_HDR} J/T")
    print(f"Magnetization (LDR): {My_LDR} J/T")

    # Generate plots
    mu_range = np.linspace(0, 1e-21, 100)
    alpha_range = np.linspace(0.5e-11, 2e-11, 100)
    r_mass = np.linspace(1, 10, 100)
    r_soc = np.linspace(1, 10, 100)

    plot_susceptibility_vs_mu(alpha, m, tau, mu_range, regime='HDR')
    plot_susceptibility_vs_alpha(alpha_range, m, tau, regime='HDR')
    plot_susceptibility_vs_anisotropy(r_mass, type='mass', m=m, alpha=alpha, tau=tau)
    plot_susceptibility_vs_anisotropy(r_soc, type='soc', m=m, alpha=alpha, tau=tau)
    plot_fermi_surfaces_and_spin_textures()
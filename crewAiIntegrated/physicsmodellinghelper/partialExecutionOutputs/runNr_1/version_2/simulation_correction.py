import numpy as np
import matplotlib.pyplot as plt

# Constants
mu_b = 5.79e-5  # eV/T
e = 1.6e-19      # C
hbar = 1.05e-34  # J·s
m_e = 9.11e-31   # kg

# Typical material parameters
m = 0.1 * m_e    # Effective mass
alpha = 52 * 1e-3 * 1e-10 * e  # Convert eV·Å to J·m: 1 eV = 1.6e-19 J, 1 Å = 1e-10 m
tau = 1e-12      # Transport lifetime
E_F = 10 * 1e-3 * e  # Convert meV to J

# Electric field parameters
E = 1e4  # V/m
theta_E = 0  # Angle of E with x-axis
E_x = E * np.cos(theta_E)
E_y = E * np.sin(theta_E)

def calculate_magnetization_isotropic(E_x, E_y, E_F, m, alpha, tau):
    """
    Calculate magnetization for isotropic Rashba model.
    Returns magnetization components (Mx, My, Mz).
    """
    Mx = 0.0
    My = 0.0
    Mz = 0.0

    # Determine regime
    if E_F > 0:
        # HDR regime
        M_y = (mu_b * abs(e) * tau) / (2 * np.pi) * m * alpha * E_x
        My = M_y
    else:
        # LDR regime
        sqrt_term = np.sqrt(m**2 * alpha**2 + 2 * m * E_F)
        M_y = (mu_b * abs(e) * tau) / (2 * np.pi) * sqrt_term * E_x
        My = M_y

    return Mx, My, Mz

def calculate_susceptibility_anisotropic(r_m, r_alpha, m, alpha, tau, S_cell, a):
    """
    Calculate Edelstein susceptibility for anisotropic case.
    """
    chi0 = (tau * abs(e) * mu_b * S_cell) / (4 * np.pi**2 * a)

    # Mass anisotropy
    chi_mass = (4 * np.pi * m * alpha * r_m) / (1 + np.sqrt(r_m))

    # SOC anisotropy
    chi_soc = (4 * np.pi * m * alpha * r_alpha) / (1 + r_alpha)

    return chi_mass / chi0, chi_soc / chi0

def plot_susceptibility_vs_mu(mu_values, alpha_values):
    """
    Plot Edelstein susceptibility vs chemical potential.
    """
    plt.figure(figsize=(10, 6))
    for alpha in alpha_values:
        chi_values = []
        for mu in mu_values:
            if mu > 0:
                # HDR
                chi = (mu_b * abs(e) * tau) / (2 * np.pi) * m * alpha * E_x
            else:
                # LDR
                sqrt_term = np.sqrt(m**2 * alpha**2 + 2 * m * mu * e)
                chi = (mu_b * abs(e) * tau) / (2 * np.pi) * sqrt_term * E_x
            chi_values.append(chi)
        plt.plot(mu_values, chi_values, label=f'Alpha = {alpha} meVÅ')

    plt.xlabel('Chemical Potential (eV)')
    plt.ylabel('Susceptibility (a.u.)')
    plt.title('Edelstein Susceptibility vs Chemical Potential')
    plt.legend()
    plt.show()

def plot_susceptibility_vs_alpha(alpha_values, mu):
    """
    Plot Edelstein susceptibility vs SOC strength.
    """
    plt.figure(figsize=(10, 6))
    chi_values = []
    for alpha in alpha_values:
        if mu > 0:
            # HDR
            chi = (mu_b * abs(e) * tau) / (2 * np.pi) * m * alpha * E_x
        else:
            # LDR
            sqrt_term = np.sqrt(m**2 * alpha**2 + 2 * m * mu * e)
            chi = (mu_b * abs(e) * tau) / (2 * np.pi) * sqrt_term * E_x
        chi_values.append(chi)
    plt.plot(alpha_values, chi_values, label=f'Mu = {mu} eV')

    plt.xlabel('SOC Strength (eVÅ)')
    plt.ylabel('Susceptibility (a.u.)')
    plt.title('Edelstein Susceptibility vs SOC Strength')
    plt.legend()
    plt.show()

def plot_anisotropy_effects(r_values, type='mass'):
    """
    Plot Edelstein susceptibility vs anisotropy ratios.
    """
    plt.figure(figsize=(10, 6))
    chi_values = []
    if type == 'mass':
        for r in r_values:
            chi = (4 * np.pi * m * alpha * r) / (1 + np.sqrt(r))
            chi_values.append(chi)
        plt.plot(r_values, chi_values, label=f'Mass Anisotropy')
    elif type == 'soc':
        for r in r_values:
            chi = (4 * np.pi * m * alpha * r) / (1 + r)
            chi_values.append(chi)
        plt.plot(r_values, chi_values, label=f'SOC Anisotropy')

    plt.xlabel('Anisotropy Ratio')
    plt.ylabel('Susceptibility (a.u.)')
    plt.title('Edelstein Susceptibility vs Anisotropy')
    plt.legend()
    plt.show()

def plot_fermi_surfaces(E=0):
    """
    Plot Fermi surfaces and spin textures.
    """
    plt.figure(figsize=(10, 6))
    if E == 0:
        # Plot two concentric circles
        circle1 = plt.Circle((0, 0), 1, edgecolor='blue', facecolor='none', label='ν=+')
        circle2 = plt.Circle((0, 0), 2, edgecolor='red', facecolor='none', label='ν=-')
        plt.gcf().gca().add_artist(circle1)
        plt.gcf().gca().add_artist(circle2)
        plt.xlim(-3, 3)
        plt.ylim(-3, 3)
        plt.title('Fermi Surfaces at E=0')
    else:
        # Plot shifted Fermi surfaces
        circle1 = plt.Circle((1, 0), 1, edgecolor='blue', facecolor='none', label='ν=+')
        circle2 = plt.Circle((-1, 0), 2, edgecolor='red', facecolor='none', label='ν=-')
        plt.gcf().gca().add_artist(circle1)
        plt.gcf().gca().add_artist(circle2)
        plt.xlim(-4, 4)
        plt.ylim(-3, 3)
        plt.title('Fermi Surfaces at E≠0')

    plt.xlabel('k_x (Å^{-1})')
    plt.ylabel('k_y (Å^{-1})')
    plt.legend()
    plt.show()

# Example usage
if __name__ == "__main__":
    # Calculate magnetization
    Mx, My, Mz = calculate_magnetization_isotropic(E_x, E_y, E_F, m, alpha, tau)
    print(f"Magnetization: Mx={Mx}, My={My}, Mz={Mz}")

    # Generate plots
    mu_values = np.linspace(-10, 10, 100) * 1e-3 * e  # Convert meV to J
    alpha_values = [50, 100, 150]
    alpha_values = [alpha * 1e-3 * 1e-10 * e for alpha in alpha_values]  # Convert eVÅ to J·m
    plot_susceptibility_vs_mu(mu_values, alpha_values)

    alpha_values = np.linspace(0, 200, 100) * 1e-3 * 1e-10 * e  # Convert eVÅ to J·m
    plot_susceptibility_vs_alpha(alpha_values, E_F)

    r_values = np.linspace(0.1, 10, 100)
    plot_anisotropy_effects(r_values, type='mass')
    plot_anisotropy_effects(r_values, type='soc')

    plot_fermi_surfaces(E=0)
    plot_fermi_surfaces(E=1)

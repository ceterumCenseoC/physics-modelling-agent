
import numpy as np
import matplotlib.pyplot as plt

# Physical constants
hbar = 1.0545718e-34  # Reduced Planck's constant [J·s]
m_e = 9.10938356e-31  # Electron mass [kg]
e = 1.602176634e-19   # Elementary charge [C]
mu_B = 9.274010078e-24  # Bohr magneton [J/T]

# Model parameters
alpha_R = 1e-11  # Rashba coupling constant [J·m]
E_F = 1e-20     # Fermi energy [J]
tau = 1e-12      # Relaxation time [s]
E = 1e6          # Electric field magnitude [V/m]
E_direction = 'x'  # Electric field direction

# Compute eigenenergies
def compute_eigenenergies(k, nu):
    """
    Compute the eigenenergies for the Rashba model.
    
    Args:
        k (float): Momentum magnitude [1/m]
        nu (int): Chirality (±1)
    
    Returns:
        float: Eigenenergy [J]
    """
    return (hbar**2 * k**2) / (2 * m_e) + nu * alpha_R * hbar * k

# Compute spin texture
def compute_spin_texture(k, theta, nu):
    """
    Compute the spin expectation value for a given momentum.
    
    Args:
        k (float): Momentum magnitude [1/m]
        theta (float): Polar angle [rad]
        nu (int): Chirality (±1)
    
    Returns:
        tuple: Spin expectation value components (sx, sy, sz)
    """
    if k == 0:
        return (0, 0, 0)
    
    sx = nu * np.sin(theta)
    sy = -nu * np.cos(theta)
    sz = 0
    
    return (sx, sy, sz)

# Compute Fermi momenta
def compute_fermi_momenta():
    """
    Compute the Fermi momenta for the two chiral bands.
    
    Returns:
        tuple: Fermi momenta for the two bands [1/m]
    """
    k0 = (m_e * alpha_R) / hbar**2
    k_F_plus = -k0 + np.sqrt(k0**2 + (2 * m_e * E_F) / hbar**2)
    k_F_minus = k0 + np.sqrt(k0**2 + (2 * m_e * E_F) / hbar**2)
    
    return (k_F_plus, k_F_minus)

# Compute magnetization
def compute_magnetization(E, tau, alpha_R, E_F, direction='x'):
    """
    Compute the magnetization components.
    
    Args:
        E (float): Electric field magnitude [V/m]
        tau (float): Relaxation time [s]
        alpha_R (float): Rashba coupling constant [J·m]
        E_F (float): Fermi energy [J]
        direction (str): Electric field direction ('x' or 'y')
    
    Returns:
        tuple: Magnetization components (Mx, My, Mz)
    """
    # Constants
    mu_0 = 4 * np.pi * 1e-7  # Vacuum permeability [H/m]
    
    # Calculate the magnetization components
    if direction == 'x':
        Mx = 0
        My = (mu_B * abs(e) * tau * m_e * alpha_R * E) / (2 * np.pi)
        Mz = 0
    elif direction == 'y':
        My = 0
        Mx = (mu_B * abs(e) * tau * m_e * alpha_R * E) / (2 * np.pi)
        Mz = 0
    else:
        Mx, My, Mz = 0, 0, 0
    
    return (Mx, My, Mz)

# Compute nonlinear effects
def compute_nonlinear_effects(E, alpha_R, E_F):
    """
    Compute the nonlinear effects parameter γ.
    
    Args:
        E (float): Electric field magnitude [V/m]
        alpha_R (float): Rashba coupling constant [J·m]
        E_F (float): Fermi energy [J]
    
    Returns:
        float: Nonlinearity parameter γ
    """
    L_s = hbar / (2 * m_e * alpha_R)
    gamma = (e * E * L_s) / E_F
    
    return gamma

# Compute anisotropic effects
def compute_anisotropic_magnetization(r_m, r_alpha):
    """
    Compute the magnetization for anisotropic Rashba models.
    
    Args:
        r_m (float): Mass anisotropy ratio (m_y/m_x)
        r_alpha (float): Rashba coupling anisotropy ratio (α_y/α_x)
    
    Returns:
        float: Anisotropic magnetization factor
    """
    chi_xy_rm = (4 * np.pi * m_e * alpha_R * r_m) / (1 + np.sqrt(r_m))
    chi_xy_ra = (4 * np.pi * m_e * alpha_R * r_alpha) / (1 + r_alpha)
    
    return chi_xy_rm, chi_xy_ra

# Visualize results
def visualize_results(E_values, M_values):
    """
    Visualize the dependence of magnetization on electric field.
    
    Args:
        E_values (list): List of electric field values [V/m]
        M_values (list): List of corresponding magnetization values [A/m]
    """
    plt.plot(E_values, M_values)
    plt.xlabel('Electric Field [V/m]')
    plt.ylabel('Magnetization [A/m]')
    plt.title('Magnetization vs Electric Field')
    plt.grid(True)
    plt.show()

# Example usage
if __name__ == "__main__":
    # Compute Fermi momenta
    k_F_plus, k_F_minus = compute_fermi_momenta()
    print(f"Fermi momenta: k_F_plus = {k_F_plus}, k_F_minus = {k_F_minus}")
    
    # Compute magnetization
    Mx, My, Mz = compute_magnetization(E, tau, alpha_R, E_F, E_direction)
    print(f"Magnetization: Mx = {Mx}, My = {My}, Mz = {Mz}")
    
    # Compute nonlinear effects
    gamma = compute_nonlinear_effects(E, alpha_R, E_F)
    print(f"Nonlinearity parameter: gamma = {gamma}")
    
    # Compute anisotropic effects
    r_m = 2.0  # Example mass anisotropy ratio
    r_alpha = 2.0  # Example Rashba coupling anisotropy ratio
    chi_xy_rm, chi_xy_ra = compute_anisotropic_magnetization(r_m, r_alpha)
    print(f"Anisotropic magnetization factors: chi_xy_rm = {chi_xy_rm}, chi_xy_ra = {chi_xy_ra}")
    
    # Visualize results
    E_values = np.linspace(0, 1e6, 100)
    M_values = [compute_magnetization(E, tau, alpha_R, E_F, E_direction)[1] for E in E_values]
    visualize_results(E_values, M_values)

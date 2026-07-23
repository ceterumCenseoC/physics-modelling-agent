

<<<<<<< HEAD
Here's the complete Python implementation of the Edelstein effect model for Rashba fermions, including calculations for both isotropic and anisotropic cases, along with visualization of the results:
=======
To implement the Edelstein effect model for Rashba fermions, we'll create a Python code that calculates the magnetization and susceptibility, then generates the required visualizations. The code incorporates the corrected formulas ensuring dimensional consistency.
>>>>>>> fa1af29044852733f94c5309bd303d0c3c2f7127

```python
import numpy as np
import matplotlib.pyplot as plt

# Constants
<<<<<<< HEAD
mu_b = 9.274e-24  # Bohr magneton (J/T)
e_charge = 1.602e-19  # Elementary charge (C)
hbar = 1.054e-34  # Reduced Planck's constant (J·s)
m_e = 9.109e-31  # Electron mass (kg)

# Model parameters (default values for GaAs-based 2DEG)
def initialize_parameters():
    """
    Initialize model parameters with realistic starting values.
    Returns:
        dict: Dictionary containing model parameters.
    """
    params = {
        'm_eff': 0.067 * m_e,  # Effective mass (kg)
        'alpha_rashba': 5.0e4,  # Rashba spin-orbit coupling strength (m/s)
        'E_F': 10.0 * 1e-3 * e_charge,  # Fermi energy (J)
        'tau': 0.5e-12,  # Transport lifetime (s)
        'E_field': 1.0e5  # Electric field (V/m)
    }
    return params

# Isotropic case calculations
def calculate_isotropic_magnetization(params, regime='HDR'):
    """
    Calculate magnetization for the isotropic Rashba model.
    Args:
        params (dict): Dictionary containing model parameters.
        regime (str, optional): 'HDR' for High-Density Regime, 'LDR' for Low-Density Regime.
    Returns:
        float: Magnetization (A/m).
    """
    m = params['m_eff']
    alpha = params['alpha_rashba']
    E_F = params['E_F']
    tau = params['tau']
    E_x = params['E_field']
    
    numerator = mu_b * e_charge * tau * m * alpha * E_x
    denominator = 2 * np.pi * hbar**2
    
    if regime == 'HDR':
        M_y = numerator / denominator
    elif regime == 'LDR':
        sqrt_term = np.sqrt(m**2 * alpha**2 + 2 * m * E_F)
        M_y = (numerator * sqrt_term) / denominator
    else:
        raise ValueError("Invalid regime. Choose 'HDR' or 'LDR'.")
    
    return M_y

# Anisotropic case calculations
def calculate_anisotropic_susceptibility(params, r_m=1.0, r_alpha=1.0):
    """
    Calculate magnetization components for the anisotropic Rashba model.
    Args:
        params (dict): Dictionary containing model parameters.
        r_m (float, optional): Mass anisotropy ratio (m_y/m_x). Defaults to 1.0.
        r_alpha (float, optional): Rashba parameter anisotropy ratio (alpha_y/alpha_x). Defaults to 1.0.
    Returns:
        tuple: (M_x, M_y) magnetization components (A/m).
    """
    m = params['m_eff']
    alpha_x = params['alpha_rashba'] / np.sqrt(r_alpha)
    alpha_y = params['alpha_rashba'] * np.sqrt(r_alpha)
    E_x = params['E_field']
    E_y = E_x  # Assuming same magnitude for E_y for simplicity
    
    chi_0 = (mu_b * e_charge * params['tau']) / (2 * np.pi * hbar**2)
    
    # Mass anisotropy dependence
    chi_xy_mass = (4 * np.pi * m * alpha_y * r_m) / (1 + np.sqrt(r_m))
    
    # Rashba parameter anisotropy dependence
    chi_xy_alpha = (4 * np.pi * m * alpha_x * r_alpha) / (1 + r_alpha)
    
    # Calculate magnetization components
    M_x = chi_xy_mass * chi_0 * E_x
    M_y = chi_xy_alpha * chi_0 * E_y
    
    return M_x, M_y

# Visualization functions
def plot_magnetization_vs_E(params, E_range, regime='HDR'):
    """
    Plot magnetization vs electric field strength.
    Args:
        params (dict): Dictionary containing model parameters.
        E_range (numpy array): Range of electric field values (V/m).
        regime (str, optional): 'HDR' or 'LDR'. Defaults to 'HDR'.
    """
    params['E_field'] = E_range
    M = np.array([calculate_isotropic_magnetization(p, regime) for p in params])
    
    plt.figure(figsize=(10, 6))
    plt.plot(E_range / 1e5, M, marker='o')
    plt.xlabel('Electric Field (V/cm)')
    plt.ylabel('Magnetization (A/m)')
    plt.title(f'Magnetization vs Electric Field ({regime})')
    plt.grid(True)
    plt.show()

def plot_magnetization_vs_alpha(params, alpha_range, regime='HDR'):
    """
    Plot magnetization vs Rashba coupling strength.
    Args:
        params (dict): Dictionary containing model parameters.
        alpha_range (numpy array): Range of Rashba coupling values (m/s).
        regime (str, optional): 'HDR' or 'LDR'. Defaults to 'HDR'.
    """
    params['alpha_rashba'] = alpha_range
    M = np.array([calculate_isotropic_magnetization(p, regime) for p in params])
    
    plt.figure(figsize=(10, 6))
    plt.plot(alpha_range / 1e4, M, marker='o')
    plt.xlabel('Rashba Coupling (m/s × 1e4)')
    plt.ylabel('Magnetization (A/m)')
    plt.title(f'Magnetization vs Rashba Coupling ({regime})')
    plt.grid(True)
    plt.show()

def plot_magnetization_vs_EF(params, EF_range, regime='LDR'):
    """
    Plot magnetization vs Fermi energy.
    Args:
        params (dict): Dictionary containing model parameters.
        EF_range (numpy array): Range of Fermi energy values (J).
        regime (str, optional): 'HDR' or 'LDR'. Defaults to 'LDR'.
    """
    params['E_F'] = EF_range
    M = np.array([calculate_isotropic_magnetization(p, regime) for p in params])
    
    plt.figure(figsize=(10, 6))
    plt.plot(EF_range / (1e-21), M, marker='o')
    plt.xlabel('Fermi Energy (J × 1e-21)')
    plt.ylabel('Magnetization (A/m)')
    plt.title(f'Magnetization vs Fermi Energy ({regime})')
    plt.grid(True)
    plt.show()

def plot_anisotropy_dependence(params, r_m_range, r_alpha_range):
    """
    Plot anisotropy dependence of magnetization.
    Args:
        params (dict): Dictionary containing model parameters.
        r_m_range (numpy array): Range of mass anisotropy ratios.
        r_alpha_range (numpy array): Range of Rashba parameter anisotropy ratios.
    """
    M_x = np.zeros(len(r_m_range))
    M_y = np.zeros(len(r_alpha_range))
    
    for i, r_m in enumerate(r_m_range):
        M_x[i], _ = calculate_anisotropic_susceptibility(params, r_m=r_m)
    
    for i, r_alpha in enumerate(r_alpha_range):
        _, M_y[i] = calculate_anisotropic_susceptibility(params, r_alpha=r_alpha)
    
    plt.figure(figsize=(12, 5))
    plt.subplot(1, 2, 1)
    plt.plot(r_m_range, M_x, marker='o')
    plt.xlabel('Mass Anisotropy Ratio ($r_m$)')
    plt.ylabel('M_x (A/m)')
    plt.title('Mass Anisotropy Dependence')
    plt.grid(True)
    
    plt.subplot(1, 2, 2)
    plt.plot(r_alpha_range, M_y, marker='o')
    plt.xlabel('Rashba Anisotropy Ratio ($r_\\alpha$)')
    plt.ylabel('M_y (A/m)')
    plt.title('Rashba Anisotropy Dependence')
    plt.grid(True)
=======
hbar = 1.0545718e-34  # Reduced Planck's constant [Js]
e = 1.602176634e-19   # Elementary charge [C]
mu_b = 9.274010078e-24  # Bohr magneton [J/T]
m_e = 9.1093837015e-31  # Electron mass [kg]

# Parameters (example values)
alpha = 1e-11  # Rashba parameter [J·m]
m = m_e        # Effective mass [kg]
tau = 1e-12    # Transport lifetime [s]
E_F = 0        # Fermi energy [J]
mu = E_F       # Chemical potential [J]
T = 1          # Temperature [K] (not used here)
E = 1          # Electric field [V/m]

def energy_dispersion(k, alpha, m, nu=1):
    """
    Compute energy dispersion for Rashba bands.
    Parameters:
    k (float or array): Momentum
    alpha (float): Rashba parameter
    m (float): Effective mass
    nu (±1): Band index
    Returns:
    E (float or array): Energy
    """
    return (hbar**2 * k**2) / (2 * m) + nu * alpha * k

def fermi_wavevector(E_F, alpha, m, nu=1):
    """
    Compute Fermi wavevector for each band.
    Parameters:
    E_F (float): Fermi energy
    alpha (float): Rashba parameter
    m (float): Effective mass
    nu (±1): Band index
    Returns:
    k_F (float): Fermi wavevector
    """
    return np.sqrt(2 * m * (E_F - nu * alpha * 0)) / hbar

def magnetization_HDR(alpha, m, E, tau, mu_b, hbar, e):
    """
    Compute magnetization in High-Density Regime.
    Parameters:
    alpha (float): Rashba parameter
    m (float): Effective mass
    E (float): Electric field
    tau (float): Transport lifetime
    mu_b (float): Bohr magneton
    hbar (float): Reduced Planck's constant
    e (float): Elementary charge
    Returns:
    M_y (float): Magnetization component
    """
    return (mu_b * e * tau / (2 * np.pi * hbar**2)) * m * alpha * E

def magnetization_LDR(alpha, m, E_F, E, tau, mu_b, hbar, e):
    """
    Compute magnetization in Low-Density Regime.
    Parameters:
    alpha (float): Rashba parameter
    m (float): Effective mass
    E_F (float): Fermi energy
    E (float): Electric field
    tau (float): Transport lifetime
    mu_b (float): Bohr magneton
    hbar (float): Reduced Planck's constant
    e (float): Elementary charge
    Returns:
    M_y (float): Magnetization component
    """
    sqrt_term = np.sqrt(m**2 * alpha**2 + 2 * m * E_F)
    return (mu_b * e * tau / (2 * np.pi * hbar**2)) * sqrt_term * E

def edelstein_susceptibility(chi_0, mu, alpha, m, hbar, HDR=True):
    """
    Compute Edelstein susceptibility.
    Parameters:
    chi_0 (float): Reference susceptibility
    mu (float): Chemical potential
    alpha (float): Rashba parameter
    m (float): Effective mass
    hbar (float): Reduced Planck's constant
    HDR (bool): Regime (True for HDR, False for LDR)
    Returns:
    chi_xy (float): Susceptibility
    """
    if HDR:
        return chi_0 * (m * alpha) / hbar**2
    else:
        sqrt_term = np.sqrt(m**2 * alpha**2 + 2 * m * mu)
        return chi_0 * sqrt_term / hbar**2

def plot_susceptibility_vs_mu(alpha, m, hbar, mu_range):
    """
    Plot susceptibility vs chemical potential.
    Parameters:
    alpha (float): Rashba parameter
    m (float): Effective mass
    hbar (float): Reduced Planck's constant
    mu_range (array): Range of chemical potentials
    """
    chi_0 = 1  # For plotting purposes, assuming normalized
    chi_HDR = [edelstein_susceptibility(chi_0, mu, alpha, m, hbar, HDR=True) for mu in mu_range]
    chi_LDR = [edelstein_susceptibility(chi_0, mu, alpha, m, hbar, HDR=False) for mu in mu_range]
    
    plt.plot(mu_range, chi_HDR, label='HDR')
    plt.plot(mu_range, chi_LDR, label='LDR')
    plt.xlabel('Chemical Potential (mu) [J]')
    plt.ylabel('Susceptibility (chi_xy/chi_0)')
    plt.legend()
    plt.show()

def plot_susceptibility_vs_alpha(m, hbar, alpha_range, mu=0):
    """
    Plot susceptibility vs Rashba parameter.
    Parameters:
    m (float): Effective mass
    hbar (float): Reduced Planck's constant
    alpha_range (array): Range of Rashba parameters
    mu (float): Chemical potential
    """
    chi_0 = 1  # For plotting purposes, assuming normalized
    chi = [edelstein_susceptibility(chi_0, mu, a, m, hbar, HDR=True) for a in alpha_range]
    
    plt.plot(alpha_range, chi)
    plt.xlabel('Rashba Parameter (alpha) [J·m]')
    plt.ylabel('Susceptibility (chi_xy/chi_0)')
    plt.show()

def plot_fermi_surface_and_spin_texture(k_x, k_y, alpha, m):
    """
    Plot Fermi surface and spin texture.
    Parameters:
    k_x (array): kx values
    k_y (array): ky values
    alpha (float): Rashba parameter
    m (float): Effective mass
    """
    K, THETA = np.meshgrid(k_x, k_y)
    k = np.sqrt(K**2 + THETA**2)
    
    # Compute spin expectation values
    sigma_x = K / k
    sigma_y = -THETA / k
    sigma_z = np.zeros_like(k)
    
    plt.figure(figsize=(10,5))
    
    plt.subplot(121)
    plt.contourf(K, THETA, k, levels=10)
    plt.title('Fermi Surface')
    plt.xlabel('k_x [m^{-1}]')
    plt.ylabel('k_y [m^{-1}]')
    
    plt.subplot(122)
    plt.quiver(K, THETA, sigma_x, sigma_y)
    plt.title('Spin Texture')
    plt.xlabel('k_x [m^{-1}]')
    plt.ylabel('k_y [m^{-1}]')
>>>>>>> fa1af29044852733f94c5309bd303d0c3c2f7127
    
    plt.tight_layout()
    plt.show()

<<<<<<< HEAD
def plot_magnetization_vector_field():
    """
    Plot vector field showing magnetization direction relative to electric field.
    """
    E_x = np.linspace(0, 1e5, 5)
    E_y = np.linspace(0, 1e5, 5)
    E_x, E_y = np.meshgrid(E_x, E_y)
    
    params = initialize_parameters()
    M_x = np.zeros(E_x.shape)
    M_y = np.zeros(E_y.shape)
    
    for i in range(E_x.shape[0]):
        for j in range(E_x.shape[1]):
            params['E_field'] = np.sqrt(E_x[i,j]**2 + E_y[i,j]**2)
            M = calculate_isotropic_magnetization(params)
            M_x[i,j] = M * E_x[i,j] / np.sqrt(E_x[i,j]**2 + E_y[i,j]**2)
            M_y[i,j] = M * E_y[i,j] / np.sqrt(E_x[i,j]**2 + E_y[i,j]**2)
    
    plt.figure(figsize=(10, 8))
    plt.quiver(E_x/1e5, E_y/1e5, M_x, M_y, color='b')
    plt.xlabel('Electric Field x (V/cm)')
    plt.ylabel('Electric Field y (V/cm)')
    plt.title('Magnetization Vector Field')
    plt.grid(True)
    plt.show()

# Main execution
if __name__ == "__main__":
    params = initialize_parameters()
    
    # Example calculations
    print("Isotropic HDR Magnetization:")
    M_HDR = calculate_isotropic_magnetization(params, regime='HDR')
    print(f"M_y = {M_HDR:.2e} A/m")
    
    print("\nIsotropic LDR Magnetization:")
    M_LDR = calculate_isotropic_magnetization(params, regime='LDR')
    print(f"M_y = {M_LDR:.2e} A/m")
    
    print("\nAnisotropic Magnetization Components:")
    M_x, M_y = calculate_anisotropic_susceptibility(params)
    print(f"M_x = {M_x:.2e} A/m")
    print(f"M_y = {M_y:.2e} A/m")
    
    # Generate plots
    E_range = np.linspace(0, 2e5, 20)  # Electric field range (V/m)
    alpha_range = np.linspace(1e4, 1e5, 20)  # Rashba coupling range (m/s)
    EF_range = np.linspace(0, 50e-3*e_charge, 20)  # Fermi energy range (J)
    r_m_range = np.linspace(0.5, 1.5, 20)  # Mass anisotropy ratio
    r_alpha_range = np.linspace(0.5, 1.5, 20)  # Rashba parameter anisotropy ratio
    
    plot_magnetization_vs_E(params, E_range, regime='HDR')
    plot_magnetization_vs_alpha(params, alpha_range, regime='HDR')
    plot_magnetization_vs_EF(params, EF_range, regime='LDR')
    plot_anisotropy_dependence(params, r_m_range, r_alpha_range)
    plot_magnetization_vector_field()
```

This code provides a comprehensive implementation of the Edelstein effect model, including:

1. **Parameter Initialization**: Sets up realistic starting parameters for a GaAs-based 2DEG system.
2. **Magnetization Calculations**: Implements formulas for both isotropic and anisotropic cases, including HDR and LDR regimes.
3. **Visualization Functions**: Generates plots to explore the dependence of magnetization on electric field, Rashba coupling, Fermi energy, and anisotropy ratios.
4. **Vector Field Plot**: Visualizes the direction of magnetization relative to the electric field.

The code is structured to be modular and easy to extend. You can modify the parameters and regimes to explore different scenarios. The example usage in the main block demonstrates how to calculate magnetization values and generate the plots.
=======
def plot_anisotropy_dependence(r_m_range, r_alpha_range, m, alpha, hbar):
    """
    Plot susceptibility dependence on anisotropy ratios.
    Parameters:
    r_m_range (array): Range of mass anisotropy
    r_alpha_range (array): Range of Rashba anisotropy
    m (float): Effective mass
    alpha (float): Rashba parameter
    hbar (float): Reduced Planck's constant
    """
    chi_0 = 1  # For plotting purposes, assuming normalized
    R_M, R_ALPHA = np.meshgrid(r_m_range, r_alpha_range)
    
    chi = np.zeros_like(R_M)
    for i in range(len(r_alpha_range)):
        for j in range(len(r_m_range)):
            chi[i,j] = edelstein_susceptibility(chi_0, mu=0, alpha=alpha * R_ALPHA[i,j], m=m * R_M[i,j], hbar=hbar, HDR=True)
    
    plt.contourf(R_M, R_ALPHA, chi, levels=20)
    plt.colorbar(label='Susceptibility (chi_xy/chi_0)')
    plt.xlabel('Mass Anisotropy (r_m)')
    plt.ylabel('Rashba Anisotropy (r_alpha)')
    plt.title('Anisotropy Dependence')
    plt.show()

# Example usage
if __name__ == "__main__":
    # Parameters
    alpha = 1e-11  # J·m
    m = m_e        # kg
    tau = 1e-12    # s
    E = 1          # V/m
    mu = 0         # J
    
    # Compute magnetization
    M_HDR = magnetization_HDR(alpha, m, E, tau, mu_b, hbar, e)
    M_LDR = magnetization_LDR(alpha, m, mu, E, tau, mu_b, hbar, e)
    
    print(f"Magnetization (HDR): {M_HDR} A/m")
    print(f"Magnetization (LDR): {M_LDR} A/m")
    
    # Generate plots
    mu_range = np.linspace(-1e-20, 1e-20, 100)
    plot_susceptibility_vs_mu(alpha, m, hbar, mu_range)
    
    alpha_range = np.linspace(0.5e-11, 2e-11, 100)
    plot_susceptibility_vs_alpha(m, hbar, alpha_range, mu)
    
    k_x = np.linspace(-1e8, 1e8, 100)
    k_y = np.linspace(-1e8, 1e8, 100)
    plot_fermi_surface_and_spin_texture(k_x, k_y, alpha, m)
    
    r_m_range = np.linspace(0.5, 2, 50)
    r_alpha_range = np.linspace(0.5, 2, 50)
    plot_anisotropy_dependence(r_m_range, r_alpha_range, m, alpha, hbar)
```

This code:

1. **Constants and Parameters**: Defines physical constants and model parameters.
2. **Energy Dispersion**: Computes the energy for each chiral band.
3. **Fermi Wavevector**: Calculates the Fermi wavevector for each band.
4. **Magnetization**: Implements functions for HDR and LDR.
5. **Susceptibility**: Computes the Edelstein susceptibility.
6. **Plots**: Generates four plots as specified:
   - Susceptibility vs. chemical potential.
   - Susceptibility vs. Rashba parameter.
   - Fermi surface and spin texture.
   - Anisotropy dependence.

To use the code, set the parameters (e.g., alpha, m, tau, E) and run the example usage section. This will compute the magnetization and generate the plots, visualizing the Edelstein effect behavior under various conditions.
>>>>>>> fa1af29044852733f94c5309bd303d0c3c2f7127

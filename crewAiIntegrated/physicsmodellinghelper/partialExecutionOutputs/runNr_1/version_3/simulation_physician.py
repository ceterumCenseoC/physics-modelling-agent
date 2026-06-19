

Here is the complete Python code implementing the Edelstein effect model:

```python
import numpy as np
import matplotlib.pyplot as plt

# Physical Constants
hbar = 1.0545718e-34  # Reduced Planck constant (J·s)
mu_b = 9.274010e-24   # Bohr magneton (J/T)
e = 1.602176634e-19   # Elementary charge (C)
m_e = 9.1093837015e-31  # Electron mass (kg)

# Unit Conversions
eV_to_J = 1.602176634e-19  # 1 eV = 1.602e-19 J
A_to_m = 1e-10  # 1 Å = 1e-10 m

def calculate_magnetization(E, alpha, m, tau, E_F, regime='HDR', anisotropy=False, r_m=1, r_alpha=1):
    """
    Calculate the magnetization based on the regime (HDR or LDR).
    
    Parameters:
    E (float): Electric field strength (V/m)
    alpha (float): Rashba SOC strength (J·m)
    m (float): Effective mass (kg)
    tau (float): Transport lifetime (s)
    E_F (float): Fermi energy (J)
    regime (str): 'HDR' or 'LDR' (default: 'HDR')
    anisotropy (bool): Whether to include anisotropy effects (default: False)
    r_m (float): Mass anisotropy ratio (default: 1)
    r_alpha (float): SOC anisotropy ratio (default: 1)
    
    Returns:
    M (float): Magnetization (A/m)
    """
    if regime == 'HDR':
        if anisotropy:
            chi0 = (tau * abs(e) * mu_b * 1) / (2 * np.pi)
            M = chi0 * (4 * np.pi * m * alpha * r_m) / (1 + np.sqrt(r_m)) * E
        else:
            M = (mu_b * abs(e) * tau * m * alpha) / (2 * np.pi) * E
    elif regime == 'LDR':
        sqrt_term = np.sqrt(m**2 * alpha**2 + 2 * m * E_F)
        M = (mu_b * abs(e) * tau / (2 * np.pi)) * sqrt_term * E
    return M

def calculate_susceptibility(E, alpha, m, tau, E_F, regime='HDR', anisotropy=False, r_m=1, r_alpha=1):
    """
    Calculate the Edelstein susceptibility.
    
    Parameters:
    E (float): Electric field strength (V/m)
    alpha (float): Rashba SOC strength (J·m)
    m (float): Effective mass (kg)
    tau (float): Transport lifetime (s)
    E_F (float): Fermi energy (J)
    regime (str): 'HDR' or 'LDR' (default: 'HDR')
    anisotropy (bool): Whether to include anisotropy effects (default: False)
    r_m (float): Mass anisotropy ratio (default: 1)
    r_alpha (float): SOC anisotropy ratio (default: 1)
    
    Returns:
    chi (float): Susceptibility ((A·s)/(V·m))
    """
    if regime == 'HDR':
        if anisotropy:
            chi0 = (tau * abs(e) * mu_b) / (2 * np.pi)
            chi = chi0 * (4 * np.pi * m * alpha * r_m) / (1 + np.sqrt(r_m))
        else:
            chi = (mu_b * abs(e) * tau * m * alpha) / (2 * np.pi)
    elif regime == 'LDR':
        sqrt_term = np.sqrt(m**2 * alpha**2 + 2 * m * E_F)
        chi = (mu_b * abs(e) * tau / (2 * np.pi)) * sqrt_term
    return chi

def main():
    # Example Parameters
    tau = 1e-12  # Transport lifetime (s)
    alpha = 1 * eV_to_J * A_to_m  # Rashba SOC strength (J·m)
    m = 0.1 * m_e  # Effective mass (kg)
    E_F = 0.1 * eV_to_J  # Fermi energy (J)
    E = 1e6  # Electric field (V/m)
    
    # Calculate Magnetization and Susceptibility
    M_HDR = calculate_magnetization(E, alpha, m, tau, E_F, regime='HDR')
    M_LDR = calculate_magnetization(E, alpha, m, tau, E_F, regime='LDR')
    
    print(f"Magnetization (HDR): {M_HDR} A/m")
    print(f"Magnetization (LDR): {M_LDR} A/m")
    
    # Susceptibility Calculation
    chi_HDR = calculate_susceptibility(E, alpha, m, tau, E_F, regime='HDR')
    chi_LDR = calculate_susceptibility(E, alpha, m, tau, E_F, regime='LDR')
    
    print(f"Susceptibility (HDR): {chi_HDR} (A·s)/(V·m)")
    print(f"Susceptibility (LDR): {chi_LDR} (A·s)/(V·m)")
    
    # Anisotropy Example
    r_m = 2.0
    r_alpha = 1.5
    chi_aniso = calculate_susceptibility(E, alpha, m, tau, E_F, regime='HDR', anisotropy=True, r_m=r_m, r_alpha=r_alpha)
    print(f"Susceptibility with Anisotropy: {chi_aniso} (A·s)/(V·m)")

if __name__ == "__main__":
    main()

# Example Plots
def plot_susceptibility_vs_mu():
    mu_values = np.linspace(-0.1, 0.1, 100) * eV_to_J
    alpha_values = [1, 2, 3] * eV_to_J * A_to_m
    
    plt.figure(figsize=(10, 6))
    for alpha in alpha_values:
        chi_HDR = np.array([calculate_susceptibility(1e6, alpha, 0.1*m_e, 1e-12, mu, regime='HDR') for mu in mu_values])
        chi_LDR = np.array([calculate_susceptibility(1e6, alpha, 0.1*m_e, 1e-12, mu, regime='LDR') for mu in mu_values])
        
        plt.plot(mu_values / eV_to_J, chi_HDR, label=f'HDR, α={alpha / (eV_to_J * A_to_m)} eVÅ')
        plt.plot(mu_values / eV_to_J, chi_LDR, '--', label=f'LDR, α={alpha / (eV_to_J * A_to_m)} eVÅ')
    
    plt.xlabel('Chemical Potential (eV)')
    plt.ylabel('Susceptibility ((A·s)/(V·m))')
    plt.title('Edelstein Susceptibility vs Chemical Potential')
    plt.legend()
    plt.show()

def plot_susceptibility_vs_alpha():
    alpha_values = np.linspace(0.5, 5, 100) * eV_to_J * A_to_m
    mu = 0.05 * eV_to_J
    
    chi_HDR = np.array([calculate_susceptibility(1e6, alpha, 0.1*m_e, 1e-12, mu, regime='HDR') for alpha in alpha_values])
    chi_LDR = np.array([calculate_susceptibility(1e6, alpha, 0.1*m_e, 1e-12, mu, regime='LDR') for alpha in alpha_values])
    
    plt.figure(figsize=(10, 6))
    plt.plot(alpha_values / (eV_to_J * A_to_m), chi_HDR, label='HDR')
    plt.plot(alpha_values / (eV_to_J * A_to_m), chi_LDR, label='LDR')
    plt.xlabel('SOC Strength (eVÅ)')
    plt.ylabel('Susceptibility ((A·s)/(V·m))')
    plt.title('Edelstein Susceptibility vs SOC Strength')
    plt.legend()
    plt.show()

def plot_anisotropy_dependence():
    r_m_values = np.linspace(1, 10, 100)
    r_alpha = 1.0
    
    chi_aniso = np.array([calculate_susceptibility(1e6, 1 * eV_to_J * A_to_m, 0.1*m_e, 1e-12, 0.1 * eV_to_J, 
                              regime='HDR', anisotropy=True, r_m=r_m, r_alpha=r_alpha) for r_m in r_m_values])
    
    plt.figure(figsize=(10, 6))
    plt.plot(r_m_values, chi_aniso)
    plt.xlabel('Mass Anisotropy Ratio ($r_m$)')
    plt.ylabel('Susceptibility ((A·s)/(V·m))')
    plt.title('Susceptibility vs Mass Anisotropy Ratio')
    plt.show()

# Generate Plots
plot_susceptibility_vs_mu()
plot_susceptibility_vs_alpha()
plot_anisotropy_dependence()
```

This code:

1. Implements the model for calculating magnetization and susceptibility
2. Includes unit conversions and physical constants
3. Provides example usage in the main function
4. Generates the expected plots for:
   - Susceptibility vs Chemical Potential
   - Susceptibility vs SOC Strength
   - Anisotropy Dependence

The code uses NumPy for numerical calculations and matplotlib for plotting. It handles both isotropic and anisotropic cases, and it includes example parameters that can be adjusted based on specific material properties.

To use this code:

1. Save it as a Python file
2. Install required packages: `numpy` and `matplotlib`
3. Run the script to calculate magnetization/susceptibility and generate plots

The code is well-commented and includes docstrings explaining each function's purpose and parameters.
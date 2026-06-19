

Here is the complete Python code implementing the Edelstein effect model for both isotropic and anisotropic Rashba systems:

```python
import numpy as np
import matplotlib.pyplot as plt

# Constants
mu_b = 9.274e-24  # Bohr magneton in J/T
e = 1.602e-19     # Elementary charge in C
hbar = 1.0545718e-34  # Reduced Planck's constant in J·s

# Isotropic Rashba Model Functions
def calculate_magnetization_isotropic_HDR(E, alpha, m, tau):
    """
    Calculate magnetization in the high-density regime (HDR).
    Parameters:
    - E (float): Electric field in V/m
    - alpha (float): Rashba spin-orbit coupling strength in J·m
    - m (float): Effective mass in kg
    - tau (float): Transport lifetime in seconds
    Returns:
    - M (float): Magnetization in J/T
    """
    prefactor = (mu_b * e * tau) / (2 * np.pi * hbar)
    M = prefactor * m * alpha * E
    return M

def calculate_magnetization_isotropic_LDR(E, alpha, m, EF, tau):
    """
    Calculate magnetization in the low-density regime (LDR).
    Parameters:
    - E (float): Electric field in V/m
    - alpha (float): Rashba spin-orbit coupling strength in J·m
    - m (float): Effective mass in kg
    - EF (float): Fermi energy in J
    - tau (float): Transport lifetime in seconds
    Returns:
    - M (float): Magnetization in J/T
    """
    sqrt_term = np.sqrt(m**2 * alpha**2 + 2 * m * alpha**2 * EF)
    prefactor = (mu_b * e * tau) / (2 * np.pi * hbar)
    M = prefactor * sqrt_term * E
    return M

# Anisotropic Rashba Model Functions
def calculate_susceptibility_anisotropic_HDR(r, m_ref, alpha_ref, tau, S_cell, a):
    """
    Calculate susceptibility in the high-density regime (HDR) for anisotropic case.
    Parameters:
    - r (float): Anisotropy ratio (rm or ralpha)
    - m_ref (float): Reference effective mass in kg
    - alpha_ref (float): Reference Rashba parameter in J·m
    - tau (float): Transport lifetime in seconds
    - S_cell (float): Unit cell area in m²
    - a (float): Lattice parameter in m
    Returns:
    - chi (float): Susceptibility in SI units
    """
    chi0 = (tau * e * mu_b * S_cell) / (4 * np.pi**2 * a)
    chi = (4 * np.pi * m_ref * alpha_ref * r) / (1 + np.sqrt(r)) * chi0
    return chi

# Main function to compute and plot results
def main():
    # Parameters (SI units)
    m = 0.1 * 9.1e-31  # Effective mass in kg
    alpha = 1e-11  # Rashba spin-orbit coupling strength in J·m
    EF = 1e-20  # Fermi energy in J
    E = 1e6  # Electric field in V/m
    tau = 1e-12  # Transport lifetime in seconds
    S_cell = 1e-20  # Unit cell area in m² (example value)
    a = 1e-10  # Lattice parameter in m (example value)
    
    # HDR and LDR calculations
    print("Isotropic Rashba Model:")
    print("-------------------------")
    M_HDR = calculate_magnetization_isotropic_HDR(E, alpha, m, tau)
    print(f"Magnetization in HDR: {M_HDR} J/T")
    
    M_LDR = calculate_magnetization_isotropic_LDR(E, alpha, m, EF, tau)
    print(f"Magnetization in LDR: {M_LDR} J/T")
    
    # Anisotropic calculations
    print("\nAnisotropic Rashba Model:")
    print("---------------------------")
    r_m = 2.0  # Example mass anisotropy ratio
    chi_mass = calculate_susceptibility_anisotropic_HDR(r_m, m, alpha, tau, S_cell, a)
    print(f"Susceptibility for r_m = {r_m}: {chi_mass} SI units")
    
    r_alpha = 2.0  # Example SOC anisotropy ratio
    chi_alpha = calculate_susceptibility_anisotropic_HDR(r_alpha, m, alpha, tau, S_cell, a)
    print(f"Susceptibility for r_alpha = {r_alpha}: {chi_alpha} SI units")
    
    # Example plots
    # Plot 1: Susceptibility vs Chemical Potential
    mu_values = np.linspace(0, 2e-20, 100)
    chi_HDR = np.full_like(mu_values, M_HDR / E)  # Constant in HDR
    chi_LDR = np.zeros_like(mu_values)
    for i, mu in enumerate(mu_values):
        chi_LDR[i] = calculate_magnetization_isotropic_LDR(E, alpha, m, mu, tau) / E
    
    plt.figure(figsize=(10, 5))
    plt.subplot(1, 2, 1)
    plt.plot(mu_values / 1e-20, chi_HDR / (mu_b * E), label='HDR')
    plt.plot(mu_values / 1e-20, chi_LDR / (mu_b * E), label='LDR')
    plt.xlabel('Chemical Potential (10^{-20} J)')
    plt.ylabel('Normalized Susceptibility ($\chi/(\mu_b E)$)')
    plt.title('Susceptibility vs Chemical Potential')
    plt.legend()
    
    # Plot 2: Susceptibility vs Spin-Orbit Coupling
    alpha_values = np.linspace(0.5e-11, 2e-11, 100)
    chi_HDR_alpha = np.array([calculate_magnetization_isotropic_HDR(E, a, m, tau) / E for a in alpha_values])
    chi_LDR_alpha = np.array([calculate_magnetization_isotropic_LDR(E, a, m, EF, tau) / E for a in alpha_values])
    
    plt.subplot(1, 2, 2)
    plt.plot(alpha_values / 1e-11, chi_HDR_alpha / (mu_b * E), label='HDR')
    plt.plot(alpha_values / 1e-11, chi_LDR_alpha / (mu_b * E), label='LDR')
    plt.xlabel('Spin-Orbit Coupling (10^{-11} J·m)')
    plt.ylabel('Normalized Susceptibility ($\chi/(\mu_b E)$)')
    plt.title('Susceptibility vs Spin-Orbit Coupling')
    plt.legend()
    
    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    main()
```

### Explanation of the Code:

1. **Constants**: Defines physical constants used in the calculations.

2. **Isotropic Rashba Model Functions**:
   - `calculate_magnetization_isotropic_HDR`: Computes magnetization in the high-density regime.
   - `calculate_magnetization_isotropic_LDR`: Computes magnetization in the low-density regime.

3. **Anisotropic Rashba Model Function**:
   - `calculate_susceptibility_anisotropic_HDR`: Computes susceptibility in the high-density regime for anisotropic systems.

4. **Main Function**:
   - Sets up example parameters.
   - Computes magnetization for both HDR and LDR.
   - Computes susceptibility for anisotropic cases with example anisotropy ratios.
   - Generates plots showing:
     - Susceptibility vs. chemical potential.
     - Susceptibility vs. spin-orbit coupling strength.

This code provides a complete implementation of the Edelstein effect model, including both isotropic and anisotropic cases, and generates visualizations of key results.
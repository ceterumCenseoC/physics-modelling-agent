```python
import numpy as np
import matplotlib.pyplot as plt

def calculate_edelstein_effect(alpha, m, tau, E, r_m=1, chirality=1):
    """
    Calculate the magnetization and susceptibility for the Edelstein effect in a Rashba fermion system.

    Parameters:
    alpha (float): Rashba parameter (units: eV·m)
    m (float): Effective mass (units: electron mass)
    tau (float): Relaxation time (units: seconds)
    E (float): Electric field magnitude (units: V/m)
    r_m (float, optional): Mass anisotropy ratio (m_y/m_x). Defaults to 1 (isotropic case).
    chirality (int, optional): Chirality of the Rashba band (+1 or -1). Defaults to 1.

    Returns:
    tuple: (Magnetization magnitude, Susceptibility)
    """
    # Constants
    mu_b = 9.274e-24  # Bohr magneton (J/T)
    e = 1.602e-19     # Elementary charge (C)
    hbar = 1.0545718e-34  # Reduced Planck constant (J·s)

    # Calculate magnetization magnitude
    M = (mu_b * abs(e) * tau) / (2 * np.pi) * m * alpha * E * chirality

    # Calculate susceptibility
    chi = (4 * np.pi * m * alpha * r_m) / (1 + np.sqrt(r_m))

    return M, chi

def analyze_parameter_dependencies(alpha, m, tau, E_range, r_m_range, chirality_range):
    """
    Analyze how magnetization and susceptibility depend on various parameters.

    Parameters:
    alpha (float): Rashba parameter (units: eV·m)
    m (float): Effective mass (units: electron mass)
    tau (float): Relaxation time (units: seconds)
    E_range (array): Range of electric field magnitudes (units: V/m)
    r_m_range (array): Range of mass anisotropy ratios
    chirality_range (array): Range of chirality values (+1 and -1)

    Returns:
    dict: Dictionary containing magnetization and susceptibility arrays for different parameters
    """
    results = {
        'E_range': E_range,
        'r_m_range': r_m_range,
        'chirality_range': chirality_range,
        'M_vs_E': np.zeros((len(chirality_range), len(E_range))),
        'chi_vs_r_m': np.zeros((len(chirality_range), len(r_m_range)))
    }

    # Calculate magnetization vs electric field
    for i, chirality in enumerate(chirality_range):
        for j, E in enumerate(E_range):
            M, _ = calculate_edelstein_effect(alpha, m, tau, E, r_m=1, chirality=chirality)
            results['M_vs_E'][i, j] = M

    # Calculate susceptibility vs mass anisotropy
    for i, chirality in enumerate(chirality_range):
        for j, r_m in enumerate(r_m_range):
            _, chi = calculate_edelstein_effect(alpha, m, tau, E=1e4, r_m=r_m, chirality=chirality)
            results['chi_vs_r_m'][i, j] = chi

    return results

def plot_results(results):
    """
    Plot the results of the parameter analysis.

    Parameters:
    results (dict): Dictionary containing results from analyze_parameter_dependencies
    """
    E_range = results['E_range']
    r_m_range = results['r_m_range']
    chirality_range = results['chirality_range']
    M_vs_E = results['M_vs_E']
    chi_vs_r_m = results['chi_vs_r_m']

    # Plot magnetization vs electric field
    plt.figure(figsize=(12, 5))

    plt.subplot(1, 2, 1)
    for i, chirality in enumerate(chirality_range):
        plt.plot(E_range, M_vs_E[i, :], label=f'Chirality = {chirality}')
    plt.xlabel('Electric Field (V/m)')
    plt.ylabel('Magnetization (A/m)')
    plt.title('Magnetization vs Electric Field')
    plt.legend()
    plt.grid(True)

    # Plot susceptibility vs mass anisotropy
    plt.subplot(1, 2, 2)
    for i, chirality in enumerate(chirality_range):
        plt.plot(r_m_range, chi_vs_r_m[i, :], label=f'Chirality = {chirality}')
    plt.xlabel('Mass Anisotropy Ratio (r_m)')
    plt.ylabel('Susceptibility')
    plt.title('Susceptibility vs Mass Anisotropy')
    plt.legend()
    plt.grid(True)

    plt.tight_layout()
    plt.show()

# Example usage
if __name__ == "__main__":
    # Parameters
    alpha = 1e-11  # Rashba parameter (eV·m)
    m = 0.1  # Effective mass (in units of electron mass)
    tau = 1e-12  # Relaxation time (s)
    E_range = np.linspace(1e3, 1e5, 100)  # Electric field range (V/m)
    r_m_range = np.linspace(0.1, 10, 100)  # Mass anisotropy range
    chirality_range = [1, -1]  # Chirality values

    # Analyze parameter dependencies
    results = analyze_parameter_dependencies(alpha, m, tau, E_range, r_m_range, chirality_range)

    # Plot results
    plot_results(results)

    # Print example values
    E_example = 1e4  # Example electric field (V/m)
    r_m_example = 1  # Example mass anisotropy ratio
    for chirality in chirality_range:
        M, chi = calculate_edelstein_effect(alpha, m, tau, E_example, r_m_example, chirality)
        print(f"Chirality = {chirality}:")
        print(f"  Magnetization: {M:.2e} A/m")
        print(f"  Susceptibility: {chi:.2e}")
        print()
```

This code provides a complete numerical implementation of the Edelstein effect for Rashba fermions at the Gamma point. It includes functions to calculate magnetization and susceptibility, analyze parameter dependencies, and visualize the results. The code is well-documented and can be easily modified to explore different parameter ranges or additional effects.
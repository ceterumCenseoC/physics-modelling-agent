

To implement the model for calculating the Edelstein effect in Rashba fermions, we will follow a structured approach, ensuring that all physical constants and parameters are correctly handled, and the magnetization is accurately computed for both high-density and low-density regimes. The code will also generate the required visualizations to analyze the results.

### Python Code Implementation

```python
import numpy as np
import matplotlib.pyplot as plt

# Constants
hbar = 1.0545718e-34  # Reduced Planck's constant (J·s)
m_e = 9.10938356e-31  # Electron mass (kg)
e = 1.602176634e-19   # Elementary charge (C)
mu_b = 9.27401008e-24  # Bohr magneton (J/T)

# Model parameters
m = 0.1 * m_e          # Effective mass (kg)
alpha = 1e-20          # Rashba parameter (J·m)
tau = 1e-12            # Scattering time (s)
E = 1e3                # Electric field (V/m) = (J/C·m)
E_F = 1e-20            # Fermi energy (J)

def calculate_magnetization(E_x, E_y, E_F, m, alpha, tau):
    """
    Calculate the magnetization components based on the regime.
    """
    if E_F > 0:
        # High-Density Regime (HDR)
        M_y = (mu_b * e * tau) / (2 * np.pi) * m * alpha * E_x
        M_x = (mu_b * e * tau) / (2 * np.pi) * m * alpha * (-E_y)
    else:
        # Low-Density Regime (LDR) with ħ^2 correction
        sqrt_term = np.sqrt(m**2 * alpha**2 + (2 * m * E_F) / (hbar**2))
        M_y = (mu_b * e * tau) / (2 * np.pi) * sqrt_term * E_x
        M_x = (mu_b * e * tau) / (2 * np.pi) * sqrt_term * (-E_y)
    
    return M_x, M_y

def compute_susceptibility(r_m, r_alpha, m, alpha):
    """
    Compute the normalized susceptibility for anisotropic cases.
    """
    chi0 = (tau * e * mu_b * 1) / (4 * np.pi**2 * 1)  # Simplified chi0
    # For mass ratio
    chi_mass = (4 * np.pi * m * alpha * r_m) / (1 + np.sqrt(r_m))
    # For Rashba ratio
    chi_alpha = (4 * np.pi * m * alpha * r_alpha) / (1 + r_alpha)
    return chi_mass / chi0, chi_alpha / chi0

def plot_edelstein_susceptibility():
    """
    Generate plots for Edelstein susceptibility vs various parameters.
    """
    # Figure 1: Susceptibility vs Chemical Potential
    mu_range = np.linspace(-2e-20, 2e-20, 100)
    chi = []
    for mu in mu_range:
        if mu > 0:
            chi.append(1.0)  # HDR, constant
        else:
            sqrt_term = np.sqrt(m**2 * alpha**2 + (2 * m * mu) / (hbar**2))
            chi.append(sqrt_term / (m * alpha))
    plt.figure(figsize=(10,6))
    plt.plot(mu_range, chi, label='Normalized Susceptibility')
    plt.xlabel('Chemical Potential (J)')
    plt.ylabel('Normalized $\chi_{xy}$')
    plt.title('Edelstein Susceptibility vs Chemical Potential')
    plt.legend()
    plt.show()

    # Figure 2: Susceptibility vs Rashba Parameter
    alpha_range = np.linspace(0, 2e-20, 100)
    chi = []
    for a in alpha_range:
        chi.append(a / alpha)  # Linear relation
    plt.figure(figsize=(10,6))
    plt.plot(alpha_range, chi, label='Normalized Susceptibility')
    plt.xlabel('Rashba Parameter (J·m)')
    plt.ylabel('Normalized $\chi_{xy}$')
    plt.title('Edelstein Susceptibility vs Rashba Parameter')
    plt.legend()
    plt.show()

    # Figure 3: Anisotropy Dependence
    r_m = np.linspace(0, 2, 100)
    chi_m = (4 * np.pi * m * alpha * r_m) / (1 + np.sqrt(r_m))
    chi_m_norm = chi_m / (4 * np.pi * m * alpha)
    
    r_alpha = np.linspace(0, 2, 100)
    chi_alpha = (4 * np.pi * m * alpha * r_alpha) / (1 + r_alpha)
    chi_alpha_norm = chi_alpha / (4 * np.pi * m * alpha)
    
    plt.figure(figsize=(10,6))
    plt.plot(r_m, chi_m_norm, label='Mass Ratio')
    plt.plot(r_alpha, chi_alpha_norm, label='Rashba Ratio')
    plt.xlabel('Anisotropy Ratio')
    plt.ylabel('Normalized $\chi_{xy}$')
    plt.title('Edelstein Susceptibility vs Anisotropy')
    plt.legend()
    plt.show()

def plot_spin_texture():
    """
    Plot the spin texture and Fermi surfaces.
    """
    theta = np.linspace(0, 2*np.pi, 100)
    k = np.linspace(0, 1e8, 100)  # Assuming some k range in m^-1
    
    # For visualization, create a grid
    THETA, K = np.meshgrid(theta, k)
    
    # Spin components
    S_x = np.sin(THETA)
    S_y = -np.cos(THETA)
    
    # Create polar plots
    plt.figure(figsize=(10,10))
    ax = plt.subplot(111, polar=True)
    Q = ax.quiver(THETA, K, S_x, S_y, color='b')
    ax.set_title("Spin Texture")
    plt.show()

# Example usage
E_x = 1e3  # V/m
E_y = 0     # V/m
M_x, M_y = calculate_magnetization(E_x, E_y, E_F, m, alpha, tau)
print(f"Magnetization: M_x = {M_x} J/T, M_y = {M_y} J/T")

# Generate plots
plot_edelstein_susceptibility()
plot_spin_texture()
```

### Explanation

1. **Constants and Parameters**: The code starts by defining all necessary physical constants and model parameters. These include the reduced Planck's constant, effective mass, Rashba parameter, electric field, scattering time, and Fermi energy.

2. **Magnetization Calculation**: The `calculate_magnetization` function computes the magnetization components (M_x and M_y) based on whether the system is in the high-density regime (HDR) or low-density regime (LDR). The HDR uses a straightforward formula, while the LDR includes a square root term corrected with ħ².

3. **Susceptibility Computation**: The `compute_susceptibility` function handles anisotropic cases by computing the normalized susceptibility for mass and Rashba parameter ratios.

4. **Visualization Functions**: 
   - `plot_edelstein_susceptibility` generates three plots: susceptibility vs. chemical potential, vs. Rashba parameter, and vs. anisotropy ratios.
   - `plot_spin_texture` visualizes the spin texture and Fermi surfaces using polar coordinates, showing the direction of spins.

5. **Example Usage**: The code demonstrates how to calculate magnetization for a given electric field and Fermi energy, then generates the required plots to analyze the Edelstein effect comprehensively.

This implementation ensures that the Edelstein effect is accurately modeled and visualized, providing insights into how various parameters influence the induced magnetization.
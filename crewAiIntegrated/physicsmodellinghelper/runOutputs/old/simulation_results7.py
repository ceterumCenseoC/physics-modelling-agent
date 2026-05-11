```python
import numpy as np

def calculate_edelstein_effect(m, alpha, E, k_F):
    """
    Calculate the magnetization due to the Edelstein effect for a Rashba fermion.

    Parameters:
    m (float): Effective mass in units of electron mass
    alpha (float): Rashba coupling strength in meV·Å
    E (float): Electric field magnitude
    k_F (float): Fermi wavevector

    Returns:
    M (float): Magnetization magnitude
    M_direction (str): Direction of magnetization
    """
    # Constants
    mu_B = 9.274e-24  # Bohr magneton
    e = 1.602e-19     # Elementary charge
    hbar = 1.0545718e-34  # Reduced Planck constant

    # Convert units if necessary
    # Assuming alpha is in meV·Å
    alpha = alpha * 1e-3 * 1e-10  # Convert to J·m

    # Calculate Fermi velocity
    v_F = (hbar * k_F) / m

    # Calculate susceptibility
    chi = (mu_B * e / hbar) * (alpha / (v_F ** 2))

    # Calculate magnetization
    M = chi * E

    # Determine direction of magnetization
    # Assuming electric field is along x-direction
    M_direction = "out-of-plane (z-direction)"

    return M, M_direction

# Example usage
m = 0.1  # in units of electron mass
alpha = 10  # in meV·Å
E = 1e3  # Electric field magnitude
k_F = 1e8  # Fermi wavevector

M, M_direction = calculate_edelstein_effect(m, alpha, E, k_F)
print(f"Magnetization: {M} A/m")
print(f"Direction: {M_direction}")
```
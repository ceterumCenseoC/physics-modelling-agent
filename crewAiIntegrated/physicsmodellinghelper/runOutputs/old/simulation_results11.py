import numpy as np

def calculate_edelstein_effect(
    alpha,      # Rashba coupling strength (eV·Å)
    m,          # Effective mass (kg)
    E_F,        # Fermi energy (eV)
    E,          # Electric field (V/m)
    E_direction,# Electric field direction ('x' or 'y')
    tau         # Scattering time (s)
):
    """
    Calculate the Edelstein effect for a Rashba fermion at the Gamma point.

    Parameters:
    - alpha: Rashba coupling strength (eV·Å)
    - m: Effective mass (kg)
    - E_F: Fermi energy (eV)
    - E: Electric field magnitude (V/m)
    - E_direction: Direction of the electric field ('x' or 'y')
    - tau: Scattering time (s)

    Returns:
    - Magnetization magnitude (J/T)
    - Direction of magnetization (str)
    """
    # Constants
    mu_b = 9.274e-24  # Bohr magneton (J/T)
    e = 1.602e-19    # Elementary charge (C)

    # Determine regime
    if E_F >= 0:
        # High-Density Regime (HDR)
        chi_xy = (mu_b * abs(e) * tau) / (2 * np.pi) * m * alpha
    else:
        # Low-Density Regime (LDR)
        chi_xy = (mu_b * abs(e) * tau) / (2 * np.pi) * np.sqrt(m**2 * alpha**2 + 2 * m * E_F)

    # Calculate magnetization direction
    if E_direction == 'x':
        M = chi_xy * E
        return M, 'y'  # Magnetization magnitude and direction
    elif E_direction == 'y':
        M = chi_xy * E
        return M, 'x'  # Magnetization magnitude and direction
    else:
        return 0, 'none'  # Magnetization is zero for other directions

# Example usage
alpha = 1e-10  # eV·Å
m = 0.1 * 9.1e-31  # kg
E_F = 0.5  # eV
E = 1e6  # V/m
E_direction = 'x'
tau = 1e-12  # s

magnetization, direction = calculate_edelstein_effect(alpha, m, E_F, E, E_direction, tau)
print(f"Magnetization: {magnetization} J/T, Direction: {direction}")
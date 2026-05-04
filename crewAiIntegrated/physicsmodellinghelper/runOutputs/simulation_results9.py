```python
import numpy as np

def calculate_edelstein_effect(alpha_R, v_F, tau, E_magnitude, E_direction, E_F, m_star):
    """
    Calculate the magnetization magnitude and direction induced by the Edelstein effect
    in a 2D Rashba fermion system at the Gamma point of the Brillouin zone.

    Parameters:
    -----------
    alpha_R : float
        Rashba coupling strength in units of eV·Å (electron volt angstrom)
    v_F : float
        Fermi velocity in units of m/s (meters per second)
    tau : float
        Scattering time in units of s (seconds)
    E_magnitude : float
        Magnitude of the applied electric field in units of V/m (volts per meter)
    E_direction : numpy.ndarray
        Direction of the applied electric field as a unit vector in the xy-plane
        (e.g., np.array([1, 0]) for E along x-axis)
    E_F : float
        Fermi energy in units of eV (electron volts)
    m_star : float
        Effective mass in units of kg (kilograms)

    Returns:
    --------
    M_magnitude : float
        Magnitude of the induced magnetization in units of A/m (amperes per meter)
    M_direction : numpy.ndarray
        Direction of the induced magnetization as a unit vector in the xy-plane
    M_vector : numpy.ndarray
        Magnetization vector in the xy-plane (magnitude and direction)
    """

    # Constants
    e = 1.602176634e-19  # Elementary charge in C (coulombs)
    hbar = 1.054571817e-34  # Reduced Planck constant in J·s (joule seconds)
    mu_B = 9.2740100783e-24  # Bohr magneton in J/T (joule per tesla)

    # Convert units to SI
    alpha_R_SI = alpha_R * e * 1e-10  # Convert eV·Å to J·m (joule meters)
    E_F_SI = E_F * e  # Convert eV to J (joules)

    # Calculate the direction of magnetization (perpendicular to E and z-axis)
    z_hat = np.array([0, 0, 1])
    E_vector = np.array([E_direction[0], E_direction[1], 0])
    M_direction = np.cross(z_hat, E_vector)[:2]  # Only xy components
    M_direction = M_direction / np.linalg.norm(M_direction)  # Normalize

    # Calculate the magnitude of magnetization
    # The proportionality constant C is derived from the Boltzmann transport equation
    # For simplicity, we use C = 1 (can be adjusted based on material-specific parameters)
    C = 1.0
    M_magnitude = C * tau * alpha_R_SI * e * E_F_SI * E_magnitude / v_F

    # Convert magnetization magnitude to A/m (amperes per meter)
    # M = (mu_B * n) where n is the spin density (spins per volume)
    # For simplicity, we assume a unit volume and convert to A/m
    M_magnitude_A_per_m = M_magnitude / mu_B  # A/m

    # Calculate the magnetization vector
    M_vector = M_magnitude_A_per_m * M_direction

    return M_magnitude_A_per_m, M_direction, M_vector

def main():
    # Example usage
    alpha_R = 10  # meV·Å
    v_F = 1e6  # m/s
    tau = 1e-11  # s
    E_magnitude = 1e4  # V/m
    E_direction = np.array([1, 0])  # E along x-axis
    E_F = 100  # meV
    m_star = 9.1093837015e-31  # kg (electron mass)

    M_magnitude, M_direction, M_vector = calculate_edelstein_effect(
        alpha_R, v_F, tau, E_magnitude, E_direction, E_F, m_star
    )

    print("Magnetization Magnitude:", M_magnitude, "A/m")
    print("Magnetization Direction:", M_direction)
    print("Magnetization Vector:", M_vector)

if __name__ == "__main__":
    main()
```
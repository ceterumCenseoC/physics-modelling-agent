```python
import numpy as np

def calculate_magnetization(alpha_R, v_F, m_star, tau, E, lambda_chirality):
    """
    Calculate the magnetization magnitude and direction due to the Edelstein effect.

    Parameters:
    - alpha_R (float): Rashba spin-orbit coupling constant
    - v_F (float): Fermi velocity
    - m_star (float): Effective mass
    - tau (float): Scattering time
    - E (numpy array): Electric field vector (2D, in-plane)
    - lambda_chirality (int): Chirality (±1)

    Returns:
    - M_magnitude (float): Magnitude of magnetization
    - M_direction (numpy array): Direction of magnetization vector
    """
    e = 1.602176634e-19  # Elementary charge in Coulombs
    E_magnitude = np.linalg.norm(E)

    if E_magnitude == 0:
        return 0, np.array([0.0, 0.0, 0.0])

    # Compute magnetization magnitude
    M_magnitude = (e * alpha_R * tau / (2 * m_star * v_F**2)) * E_magnitude

    # Compute magnetization direction
    z_hat = np.array([0.0, 0.0, 1.0])
    E_normalized = E / E_magnitude
    M_direction = lambda_chirality * np.cross(E_normalized, z_hat)
    M_direction = M_direction / np.linalg.norm(M_direction) * M_magnitude

    return M_magnitude, M_direction

def analyze_edelstein_effect():
    """
    Analyze the Edelstein effect for different electric field directions and magnitudes.
    """
    # Constants
    alpha_R = 1.0  # eV·Å
    v_F = 1e6  # m/s
    m_star = 0.1 * 9.1093837015e-31  # Effective mass in kg
    tau = 1e-12  # Scattering time in seconds
    lambda_chirality = 1  # Chirality

    # Electric field configurations
    E_magnitudes = [0.0, 1.0, 2.0, 3.0]  # V/m
    E_directions = [np.array([1.0, 0.0, 0.0]),  # Along x-axis
                    np.array([0.0, 1.0, 0.0]),  # Along y-axis
                    np.array([1.0, 1.0, 0.0])]  # Diagonal

    print("Edelstein Effect Analysis")
    print("========================")
    print(f"Parameters: alpha_R = {alpha_R} eV·Å, v_F = {v_F} m/s, m_star = {m_star} kg, tau = {tau} s, lambda_chirality = {lambda_chirality}")
    print("\n")

    for E_mag in E_magnitudes:
        for E_dir in E_directions:
            E = E_mag * E_dir
            M_mag, M_dir = calculate_magnetization(alpha_R, v_F, m_star, tau, E, lambda_chirality)
            print(f"Electric Field: {E} V/m")
            print(f"Magnetization Magnitude: {M_mag} A/m")
            print(f"Magnetization Direction: {M_dir}")
            print("\n")

if __name__ == "__main__":
    analyze_edelstein_effect()
```
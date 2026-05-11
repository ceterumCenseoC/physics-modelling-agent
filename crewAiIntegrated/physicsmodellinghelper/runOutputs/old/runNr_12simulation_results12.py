```python
import numpy as np

# Physical constants
hbar = 1.0545718e-34  # Reduced Planck constant (J·s)
e = 1.602176634e-19   # Elementary charge (C)
m_e = 9.1093837015e-31  # Electron mass (kg)
mu_B = e * hbar / (2 * m_e)  # Bohr magneton (J/T)

def calculate_edelstein_effect(m_star, alpha_R, E, mu, tau):
    """
    Calculate the Edelstein effect for a Rashba fermion system.

    Parameters:
    - m_star: Effective mass (kg)
    - alpha_R: Rashba coupling strength (m/s)
    - E: Electric field vector (V/m)
    - mu: Chemical potential (J)
    - tau: Scattering time (s)

    Returns:
    - M: Magnetization vector (A/m)
    - M_magnitude: Magnitude of magnetization (A/m)
    - M_direction: Direction of magnetization (unit vector)
    - regime: High-Density Regime (HDR) or Low-Density Regime (LDR)
    - v_F: Fermi velocity (m/s)
    """

    # Determine regime
    if mu >= 0:
        regime = "HDR"
    else:
        regime = "LDR"

    # Calculate Fermi wavevector
    k_F = np.sqrt(2 * m_star * abs(mu) / hbar**2)

    # Calculate Fermi velocity
    v_F = hbar * k_F / m_star

    # Calculate Edelstein susceptibility
    if regime == "HDR":
        chi = (mu_B * abs(e) * tau) / (2 * np.pi) * m_star * alpha_R
    else:
        chi = (mu_B * abs(e) * tau) / (2 * np.pi) * np.sqrt((m_star**2 * alpha_R**2) + (2 * m_star * abs(mu)))

    # Calculate magnetization
    M_x = -chi * E[1]
    M_y = chi * E[0]
    M_z = 0
    M = np.array([M_x, M_y, M_z])

    # Calculate magnitude and direction
    M_magnitude = np.linalg.norm(M)
    if M_magnitude > 0:
        M_direction = M / M_magnitude
    else:
        M_direction = np.array([0, 0, 0])

    return M, M_magnitude, M_direction, regime, v_F

# Example usage
if __name__ == "__main__":
    # Input parameters
    m_star = 0.1 * m_e  # Effective mass (e.g., 0.1 times electron mass)
    alpha_R = 1e5       # Rashba coupling strength (m/s)
    E = np.array([1e6, 0, 0])  # Electric field (V/m)
    mu = 0              # Chemical potential (J)
    tau = 1e-12         # Scattering time (s)

    # Calculate Edelstein effect
    M, M_magnitude, M_direction, regime, v_F = calculate_edelstein_effect(m_star, alpha_R, E, mu, tau)

    # Print results
    print("Magnetization (A/m):", M)
    print("Magnitude of Magnetization (A/m):", M_magnitude)
    print("Direction of Magnetization:", M_direction)
    print("Regime:", regime)
    print("Fermi Velocity (m/s):", v_F)
```
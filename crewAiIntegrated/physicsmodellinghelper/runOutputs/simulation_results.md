'''
The following Python code implements a numerical simulation of the Edelstein effect for Kramers-Weyl fermions at the Gamma point. The code is well-documented and structured to allow for easy parameter tweaking and exploration of the model's behavior.

```python
'''
import numpy as np
import matplotlib.pyplot as plt

class KramersWeylEdelstein:
    """
    A class to simulate the Edelstein effect for Kramers-Weyl fermions at the Gamma point.

    This class calculates the magnetization induced by an electric field in a system
    with Kramers-Weyl fermions, considering parameters such as Fermi velocity, relaxation time,
    chirality, and Fermi wavevector.

    Attributes:
        v_F (float): Fermi velocity (m/s)
        tau (float): Relaxation time (s)
        chi (int): Chirality (±1 or ±2)
        k_F (float): Fermi wavevector (1/m)
        g (float): g-factor
        mu_B (float): Bohr magneton (J/T)
        e (float): Elementary charge (C)
        hbar (float): Reduced Planck constant (J·s)
    """

    def __init__(self, v_F=1e6, tau=1e-12, chi=1, k_F=0.1, g=2):
        """
        Initialize the Kramers-Weyl Edelstein model with given parameters.

        Parameters:
            v_F (float): Fermi velocity (m/s)
            tau (float): Relaxation time (s)
            chi (int): Chirality (±1 or ±2)
            k_F (float): Fermi wavevector (1/m)
            g (float): g-factor
        """
        self.v_F = v_F
        self.tau = tau
        self.chi = chi
        self.k_F = k_F
        self.g = g
        self.mu_B = 9.274e-24  # Bohr magneton (J/T)
        self.e = 1.602e-19     # Elementary charge (C)
        self.hbar = 1.055e-34  # Reduced Planck constant (J·s)

    def edelstein_tensor(self):
        """
        Calculate the Edelstein tensor components.

        Returns:
            numpy.ndarray: 3x3 Edelstein tensor
        """
        alpha = (self.e * self.tau * self.v_F**2 * self.chi * self.k_F**2) / \
                (6 * np.pi**2 * self.hbar**2)
        return np.eye(3) * alpha

    def magnetization(self, E):
        """
        Calculate the magnetization vector for a given electric field.

        Parameters:
            E (array-like): Electric field vector (V/m)

        Returns:
            numpy.ndarray: Magnetization vector (A/m)
        """
        E = np.array(E)
        alpha = self.edelstein_tensor()
        S = alpha @ E  # Spin polarization
        M = -(self.g * self.mu_B / self.hbar) * S  # Magnetization
        return M

    def magnetization_magnitude(self, E):
        """
        Calculate the magnitude of the magnetization for a given electric field.

        Parameters:
            E (array-like): Electric field vector (V/m)

        Returns:
            float: Magnitude of magnetization (A/m)
        """
        return np.linalg.norm(self.magnetization(E))

    def magnetization_direction(self, E):
        """
        Calculate the direction of the magnetization for a given electric field.

        Parameters:
            E (array-like): Electric field vector (V/m)

        Returns:
            numpy.ndarray: Unit vector in magnetization direction
        """
        M = self.magnetization(E)
        return M / np.linalg.norm(M)

def parameter_sweep():
    """
    Perform a parameter sweep to visualize the dependence of magnetization on chirality and Fermi velocity.

    Returns:
        list: List of results containing chirality, Fermi velocity, and magnetization magnitude
    """
    chi_values = [-2, -1, 1, 2]
    v_F_values = [1e5, 5e5, 1e6]
    E = [1e5, 0, 0]  # Fixed field along x

    results = []
    for chi in chi_values:
        for v_F in v_F_values:
            model = KramersWeylEdelstein(v_F=v_F, tau=0.5e-12, chi=chi, k_F=0.05)
            M = model.magnetization_magnitude(E)
            results.append([chi, v_F, M])

    return results

def field_sweep():
    """
    Perform a sweep of electric field magnitudes to visualize the dependence of magnetization on field strength.

    Returns:
        tuple: (E_magnitudes, M_magnitudes) arrays of electric field magnitudes and corresponding magnetization magnitudes
    """
    E_magnitudes = np.logspace(3, 6, 10)  # 1e3 to 1e6 V/m
    E_direction = np.array([1, 0, 0])

    model = KramersWeylEdelstein(v_F=5e5, tau=0.5e-12, chi=1, k_F=0.05)

    M_magnitudes = []
    for E_mag in E_magnitudes:
        E = E_mag * E_direction
        M_mag = model.magnetization_magnitude(E)
        M_magnitudes.append(M_mag)

    return E_magnitudes, M_magnitudes

def main():
    """
    Main function to demonstrate the usage of the KramersWeylEdelstein class and visualize results.
    """
    # Initialize model with default parameters
    model = KramersWeylEdelstein(v_F=5e5, tau=0.5e-12, chi=1, k_F=0.05)

    # Test different electric field directions
    E_x = [1e5, 0, 0]  # Field along x
    E_y = [0, 1e5, 0]  # Field along y
    E_z = [0, 0, 1e5]  # Field along z
    E_diag = [1e5, 1e5, 1e5]  # Diagonal field

    # Calculate magnetization
    M_x = model.magnetization(E_x)
    M_y = model.magnetization(E_y)
    M_z = model.magnetization(E_z)
    M_diag = model.magnetization(E_diag)

    print("Magnetization for different electric field directions:")
    print(f"M_x = {M_x}")
    print(f"M_y = {M_y}")
    print(f"M_z = {M_z}")
    print(f"M_diag = {M_diag}")

    # Parameter sweep visualization
    results = parameter_sweep()
    chi_vals = [r[0] for r in results]
    v_F_vals = [r[1] for r in results]
    M_vals = [r[2] for r in results]

    plt.figure(figsize=(10, 6))
    plt.scatter(chi_vals, M_vals, c=v_F_vals, cmap='viridis', s=100)
    plt.colorbar(label='Fermi Velocity (m/s)')
    plt.xlabel('Chirality (χ)')
    plt.ylabel('Magnetization Magnitude (A/m)')
    plt.title('Edelstein Effect: Chirality and Fermi Velocity Dependence')
    plt.grid(True, alpha=0.3)
    plt.show()

    # Electric field magnitude sweep visualization
    E_vals, M_vals = field_sweep()
    plt.figure(figsize=(10, 6))
    plt.loglog(E_vals, M_vals, 'o-', linewidth=2)
    plt.xlabel('Electric Field Magnitude (V/m)')
    plt.ylabel('Magnetization Magnitude (A/m)')
    plt.title('Edelstein Effect: Electric Field Magnitude Dependence')
    plt.grid(True, alpha=0.3)
    plt.show()

if __name__ == "__main__":
    main()

'''
This code provides a complete implementation of the Edelstein effect model for Kramers-Weyl fermions at the Gamma point. It includes a class to encapsulate the model, methods to calculate the magnetization and its properties, and functions to visualize the dependence of the magnetization on various parameters. The code is well-documented and structured to be easily understandable and modifiable for further exploration.
'''
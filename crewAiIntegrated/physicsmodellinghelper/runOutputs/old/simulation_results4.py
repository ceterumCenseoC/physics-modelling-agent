```python
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

class EdelsteinEffectRashba:
    """
    Numerical implementation of the Edelstein effect for Rashba fermions at the Gamma point.
    This class calculates the magnetization magnitude and direction induced by an applied electric field,
    considering dependencies on Rashba coupling strength, Fermi velocity, chirality, and other parameters.

    Attributes:
        alpha_R (float): Rashba coupling strength (eV·Å)
        v_F (float): Fermi velocity (m/s)
        m_star (float): Effective mass (kg)
        tau (float): Scattering time (s)
        chirality (int): Chirality factor (+1 or -1)
        E_field (numpy.ndarray): Applied electric field vector (V/m)
    """

    def __init__(self, alpha_R=1.0, v_F=1e6, m_star=9.1e-31, tau=1e-12, chirality=1):
        """
        Initialize the Edelstein effect model with given parameters.

        Args:
            alpha_R (float): Rashba coupling strength (default: 1.0 eV·Å)
            v_F (float): Fermi velocity (default: 1e6 m/s)
            m_star (float): Effective mass (default: electron mass 9.1e-31 kg)
            tau (float): Scattering time (default: 1e-12 s)
            chirality (int): Chirality factor (+1 or -1, default: 1)
        """
        self.alpha_R = alpha_R  # Rashba coupling strength (eV·Å)
        self.v_F = v_F          # Fermi velocity (m/s)
        self.m_star = m_star    # Effective mass (kg)
        self.tau = tau          # Scattering time (s)
        self.chirality = chirality  # Chirality factor (+1 or -1)
        self.E_field = np.array([0.0, 0.0, 0.0])  # Default electric field (V/m)

    def set_electric_field(self, E_x, E_y, E_z=0.0):
        """
        Set the applied electric field vector.

        Args:
            E_x (float): x-component of electric field (V/m)
            E_y (float): y-component of electric field (V/m)
            E_z (float): z-component of electric field (V/m, default: 0.0)
        """
        self.E_field = np.array([E_x, E_y, E_z])

    def calculate_magnetization(self):
        """
        Calculate the magnetization vector induced by the Edelstein effect.

        Returns:
            numpy.ndarray: Magnetization vector (A/m)
        """
        # Calculate the Edelstein susceptibility
        # The proportionality constant includes fundamental constants
        # For numerical purposes, we use a simplified expression
        # M = (chi * alpha_R * tau / (m_star * v_F)) * (E × z_hat)
        # where chi is the chirality factor

        # Convert alpha_R from eV·Å to J·m (1 eV = 1.602e-19 J, 1 Å = 1e-10 m)
        alpha_R_SI = self.alpha_R * 1.602e-19 * 1e-10

        # Calculate the proportionality factor
        # The actual factor would include more fundamental constants,
        # but for demonstration we use a simplified version
        factor = (self.chirality * alpha_R_SI * self.tau) / (self.m_star * self.v_F)

        # The magnetization is perpendicular to both E and z-axis
        # M ∝ E × z_hat
        z_hat = np.array([0.0, 0.0, 1.0])
        M_direction = np.cross(self.E_field, z_hat)

        # Normalize the direction vector if E_field is non-zero
        if np.linalg.norm(self.E_field) > 0:
            M_direction = M_direction / np.linalg.norm(self.E_field)

        # Calculate magnetization magnitude (simplified scaling)
        # In a real implementation, this would include more precise physical constants
        M_magnitude = factor * np.linalg.norm(self.E_field)

        # Return the magnetization vector
        return M_magnitude * M_direction

    def calculate_magnetization_magnitude(self):
        """
        Calculate the magnitude of the induced magnetization.

        Returns:
            float: Magnetization magnitude (A/m)
        """
        M = self.calculate_magnetization()
        return np.linalg.norm(M)

    def calculate_magnetization_direction(self):
        """
        Calculate the direction of the induced magnetization.

        Returns:
            numpy.ndarray: Unit vector in magnetization direction
        """
        M = self.calculate_magnetization()
        if np.linalg.norm(M) > 0:
            return M / np.linalg.norm(M)
        else:
            return np.array([0.0, 0.0, 0.0])

    def plot_magnetization_vs_electric_field(self, E_max=1e4, num_points=100):
        """
        Plot the magnetization magnitude as a function of electric field strength.

        Args:
            E_max (float): Maximum electric field strength (V/m)
            num_points (int): Number of points to plot
        """
        E_values = np.linspace(0, E_max, num_points)
        M_values = np.zeros(num_points)

        for i, E in enumerate(E_values):
            self.set_electric_field(E, 0.0)
            M_values[i] = self.calculate_magnetization_magnitude()

        plt.figure(figsize=(10, 6))
        plt.plot(E_values, M_values, 'b-', linewidth=2)
        plt.title('Magnetization vs Electric Field Strength')
        plt.xlabel('Electric Field (V/m)')
        plt.ylabel('Magnetization Magnitude (A/m)')
        plt.grid(True)
        plt.show()

    def plot_magnetization_direction(self, E_magnitude=1e4):
        """
        Plot the magnetization direction for different electric field directions.

        Args:
            E_magnitude (float): Magnitude of electric field (V/m)
        """
        # Create a grid of electric field directions
        theta = np.linspace(0, 2*np.pi, 50)
        E_x = E_magnitude * np.cos(theta)
        E_y = E_magnitude * np.sin(theta)

        # Calculate magnetization directions
        M_directions = np.zeros((len(theta), 3))
        for i in range(len(theta)):
            self.set_electric_field(E_x[i], E_y[i])
            M_directions[i] = self.calculate_magnetization_direction()

        # Plot the results
        fig = plt.figure(figsize=(12, 6))

        # Plot electric field directions
        ax1 = fig.add_subplot(121, projection='polar')
        ax1.plot(theta, np.ones(len(theta)), 'r.', label='E field direction')
        ax1.set_title('Electric Field Directions')
        ax1.set_rlim(0, 1.1)
        ax1.legend()

        # Plot magnetization directions
        ax2 = fig.add_subplot(122, projection='polar')
        M_theta = np.arctan2(M_directions[:, 1], M_directions[:, 0])
        ax2.plot(M_theta, np.ones(len(M_theta)), 'b.', label='M direction')
        ax2.set_title('Magnetization Directions')
        ax2.set_rlim(0, 1.1)
        ax2.legend()

        plt.tight_layout()
        plt.show()

    def analyze_parameter_dependence(self, parameter_name, values, E_magnitude=1e4):
        """
        Analyze how magnetization depends on a specific parameter.

        Args:
            parameter_name (str): Name of parameter to vary ('alpha_R', 'v_F', 'm_star', 'tau')
            values (numpy.ndarray): Array of values for the parameter
            E_magnitude (float): Magnitude of electric field (V/m)

        Returns:
            numpy.ndarray: Array of magnetization magnitudes corresponding to parameter values
        """
        original_value = getattr(self, parameter_name)
        M_values = np.zeros(len(values))

        for i, value in enumerate(values):
            setattr(self, parameter_name, value)
            self.set_electric_field(E_magnitude, 0.0)
            M_values[i] = self.calculate_magnetization_magnitude()

        # Restore original value
        setattr(self, parameter_name, original_value)

        return M_values

    def plot_parameter_dependence(self, parameter_name, values, E_magnitude=1e4):
        """
        Plot magnetization dependence on a specific parameter.

        Args:
            parameter_name (str): Name of parameter to vary
            values (numpy.ndarray): Array of values for the parameter
            E_magnitude (float): Magnitude of electric field (V/m)
        """
        M_values = self.analyze_parameter_dependence(parameter_name, values, E_magnitude)

        plt.figure(figsize=(10, 6))

        parameter_labels = {
            'alpha_R': 'Rashba Coupling (eV·Å)',
            'v_F': 'Fermi Velocity (m/s)',
            'm_star': 'Effective Mass (kg)',
            'tau': 'Scattering Time (s)'
        }

        plt.plot(values, M_values, 'g-', linewidth=2)
        plt.title(f'Magnetization vs {parameter_labels.get(parameter_name, parameter_name)}')
        plt.xlabel(parameter_labels.get(parameter_name, parameter_name))
        plt.ylabel('Magnetization Magnitude (A/m)')
        plt.grid(True)
        plt.show()

# Example usage and demonstration
if __name__ == "__main__":
    print("Edelstein Effect for Rashba Fermions - Numerical Implementation")
    print("=" * 60)

    # Create an instance of the Edelstein effect model
    edelstein = EdelsteinEffectRashba(
        alpha_R=1.0,    # Rashba coupling strength (eV·Å)
        v_F=1e6,        # Fermi velocity (m/s)
        m_star=9.1e-31, # Effective mass (kg)
        tau=1e-12,      # Scattering time (s)
        chirality=1      # Chirality factor
    )

    # Set an electric field
    E_magnitude = 1e4  # V/m
    print(f"\nApplying electric field of magnitude {E_magnitude} V/m")
    edelstein.set_electric_field(E_magnitude, 0.0)

    # Calculate and display results
    M = edelstein.calculate_magnetization()
    M_mag = edelstein.calculate_magnetization_magnitude()
    M_dir = edelstein.calculate_magnetization_direction()

    print(f"Magnetization vector: {M}")
    print(f"Magnetization magnitude: {M_mag:.2e} A/m")
    print(f"Magnetization direction: {M_dir}")

    # Plot magnetization vs electric field strength
    print("\nPlotting magnetization vs electric field strength...")
    edelstein.plot_magnetization_vs_electric_field(E_max=2e4)

    # Plot magnetization direction for different electric field directions
    print("\nPlotting magnetization direction for different electric field directions...")
    edelstein.plot_magnetization_direction(E_magnitude=1e4)

    # Analyze parameter dependence
    print("\nAnalyzing parameter dependence...")

    # Rashba coupling dependence
    alpha_values = np.linspace(0.5, 2.0, 50)
    print("Rashba coupling dependence:")
    edelstein.plot_parameter_dependence('alpha_R', alpha_values)

    # Fermi velocity dependence
    vF_values = np.linspace(0.5e6, 1.5e6, 50)
    print("Fermi velocity dependence:")
    edelstein.plot_parameter_dependence('v_F', vF_values)

    # Effective mass dependence
    m_values = np.linspace(0.5e-31, 1.5e-31, 50)
    print("Effective mass dependence:")
    edelstein.plot_parameter_dependence('m_star', m_values)

    # Scattering time dependence
    tau_values = np.linspace(0.5e-12, 1.5e-12, 50)
    print("Scattering time dependence:")
    edelstein.plot_parameter_dependence('tau', tau_values)

    # Demonstrate chirality effect
    print("\nDemonstrating chirality effect...")
    edelstein.set_electric_field(E_magnitude, 0.0)

    # Positive chirality
    edelstein.chirality = 1
    M_pos = edelstein.calculate_magnetization()
    print(f"Positive chirality magnetization: {M_pos}")

    # Negative chirality
    edelstein.chirality = -1
    M_neg = edelstein.calculate_magnetization()
    print(f"Negative chirality magnetization: {M_neg}")

    print("\nNote: The magnetization direction reverses with chirality!")
```
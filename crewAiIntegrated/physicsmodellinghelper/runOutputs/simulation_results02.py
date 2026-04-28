```python
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

class EdelsteinEffectRashba:
    """
    A numerical implementation of the Edelstein effect for Rashba fermions at the Gamma point.
    This class calculates the magnetization magnitude and direction induced by an applied electric field.

    Attributes:
        alpha_R (float): Rashba spin-orbit coupling strength (eV·Å)
        E_F (float): Fermi energy (eV)
        m_star (float): Effective mass (kg)
        tau (float): Scattering time (s)
        chirality (int): Chirality parameter (+1 or -1)
        hbar (float): Reduced Planck constant (eV·s)
    """

    def __init__(self, alpha_R=0.1, E_F=0.5, m_star=9.109e-31, tau=1e-13, chirality=1):
        """
        Initialize the Edelstein effect model with given parameters.

        Args:
            alpha_R (float): Rashba spin-orbit coupling strength (default: 0.1 eV·Å)
            E_F (float): Fermi energy (default: 0.5 eV)
            m_star (float): Effective mass (default: electron mass in kg)
            tau (float): Scattering time (default: 1e-13 s)
            chirality (int): Chirality parameter (+1 or -1, default: +1)
        """
        self.alpha_R = alpha_R  # eV·Å
        self.E_F = E_F  # eV
        self.m_star = m_star  # kg
        self.tau = tau  # s
        self.chirality = chirality  # +1 or -1
        self.hbar = 6.582119569e-16  # eV·s (reduced Planck constant)

        # Calculate Fermi wavevector
        self.k_F = self._calculate_kF()

    def _calculate_kF(self):
        """Calculate the Fermi wavevector from the Fermi energy."""
        # Convert units: E_F in eV, hbar in eV·s, m_star in kg
        # Need to convert m_star to eV·s²/Å² for unit consistency
        m_star_eV = self.m_star * (1.602176634e-19) * (1e20)  # kg to eV·s²/Å²
        k_F = np.sqrt(2 * m_star_eV * self.E_F) / self.hbar
        return k_F  # Å⁻¹

    def calculate_magnetization(self, E_field):
        """
        Calculate the magnetization induced by an electric field.

        Args:
            E_field (numpy.ndarray): Electric field vector [E_x, E_y, E_z] (V/Å)

        Returns:
            numpy.ndarray: Magnetization vector [M_x, M_y, M_z] (arbitrary units)
        """
        # In 2D Rashba system, magnetization is perpendicular to both E and z-axis
        # For simplicity, we assume M is along z when E is in-plane
        E_magnitude = np.linalg.norm(E_field[:2])  # Only consider in-plane components
        M_magnitude = self.chirality * self.alpha_R * self.tau * E_magnitude

        # Direction: perpendicular to E in the plane, with chirality determining sign
        if E_magnitude > 0:
            E_direction = E_field[:2] / E_magnitude
            # Perpendicular direction in 2D plane
            M_direction = np.array([-E_direction[1], E_direction[0], 0])
        else:
            M_direction = np.array([0, 0, 0])

        M_vector = M_magnitude * M_direction

        # For visualization purposes, we'll also include a z-component
        # that represents the out-of-plane magnetization
        M_vector[2] = self.chirality * self.alpha_R * self.tau * E_magnitude

        return M_vector

    def plot_magnetization_vs_field(self, E_max=1.0, num_points=100):
        """
        Plot magnetization magnitude vs electric field magnitude.

        Args:
            E_max (float): Maximum electric field magnitude (V/Å)
            num_points (int): Number of points for the plot
        """
        E_magnitudes = np.linspace(0, E_max, num_points)
        M_magnitudes = np.zeros(num_points)

        for i, E_mag in enumerate(E_magnitudes):
            E_field = np.array([E_mag, 0, 0])
            M_vector = self.calculate_magnetization(E_field)
            M_magnitudes[i] = np.linalg.norm(M_vector)

        plt.figure(figsize=(10, 6))
        plt.plot(E_magnitudes, M_magnitudes, 'b-', linewidth=2)
        plt.title('Magnetization vs Electric Field Magnitude', fontsize=14)
        plt.xlabel('Electric Field Magnitude (V/Å)', fontsize=12)
        plt.ylabel('Magnetization Magnitude (arb. units)', fontsize=12)
        plt.grid(True, alpha=0.3)
        plt.tight_layout()
        plt.show()

    def plot_3d_magnetization(self, E_max=1.0, num_points=20):
        """
        Create a 3D plot showing magnetization direction for different electric field directions.

        Args:
            E_max (float): Maximum electric field magnitude (V/Å)
            num_points (int): Number of points along each axis
        """
        # Create grid of electric field directions in the x-y plane
        E_x = np.linspace(-E_max, E_max, num_points)
        E_y = np.linspace(-E_max, E_max, num_points)
        E_x, E_y = np.meshgrid(E_x, E_y)

        # Initialize magnetization components
        M_x = np.zeros_like(E_x)
        M_y = np.zeros_like(E_x)
        M_z = np.zeros_like(E_x)

        # Calculate magnetization for each electric field direction
        for i in range(num_points):
            for j in range(num_points):
                E_field = np.array([E_x[i,j], E_y[i,j], 0])
                M_vector = self.calculate_magnetization(E_field)
                M_x[i,j] = M_vector[0]
                M_y[i,j] = M_vector[1]
                M_z[i,j] = M_vector[2]

        # Create 3D plot
        fig = plt.figure(figsize=(12, 8))
        ax = fig.add_subplot(111, projection='3d')

        # Plot magnetization vectors
        ax.quiver(E_x, E_y, np.zeros_like(E_x),
                 M_x, M_y, M_z,
                 length=0.1, normalize=True, color='r', alpha=0.7)

        # Plot surface representing magnetization magnitude
        M_magnitude = np.sqrt(M_x**2 + M_y**2 + M_z**2)
        surf = ax.plot_surface(E_x, E_y, M_magnitude,
                              cmap='viridis', alpha=0.5,
                              rstride=2, cstride=2)

        ax.set_xlabel('E_x (V/Å)', fontsize=12)
        ax.set_ylabel('E_y (V/Å)', fontsize=12)
        ax.set_zlabel('Magnetization', fontsize=12)
        ax.set_title('3D Magnetization Response to Electric Field', fontsize=14)

        # Add color bar
        fig.colorbar(surf, ax=ax, shrink=0.5, aspect=5)
        plt.tight_layout()
        plt.show()

    def analyze_parameter_dependence(self, parameter='alpha_R', values=None):
        """
        Analyze how magnetization depends on a specific parameter.

        Args:
            parameter (str): Parameter to vary ('alpha_R', 'E_F', 'tau', 'chirality')
            values (numpy.ndarray): Array of values for the parameter
        """
        if values is None:
            if parameter == 'alpha_R':
                values = np.linspace(0.05, 0.5, 20)
            elif parameter == 'E_F':
                values = np.linspace(0.1, 1.0, 20)
            elif parameter == 'tau':
                values = np.linspace(0.5e-13, 5e-13, 20)
            elif parameter == 'chirality':
                values = np.array([-1, 1])
            else:
                raise ValueError("Invalid parameter. Choose 'alpha_R', 'E_F', 'tau', or 'chirality'")

        # Fixed parameters
        fixed_params = {
            'alpha_R': 0.1,
            'E_F': 0.5,
            'm_star': 9.109e-31,
            'tau': 1e-13,
            'chirality': 1
        }

        # Test electric field
        E_test = np.array([1.0, 0, 0])  # V/Å

        # Store original value
        original_value = getattr(self, parameter)

        # Calculate magnetization for each parameter value
        M_magnitudes = []
        for val in values:
            setattr(self, parameter, val)
            M_vector = self.calculate_magnetization(E_test)
            M_magnitudes.append(np.linalg.norm(M_vector))

            # Restore k_F if E_F was changed
            if parameter == 'E_F':
                self.k_F = self._calculate_kF()

        # Restore original value
        setattr(self, parameter, original_value)
        self.k_F = self._calculate_kF()

        # Plot results
        plt.figure(figsize=(10, 6))
        plt.plot(values, M_magnitudes, 'ro-', linewidth=2, markersize=8)

        param_labels = {
            'alpha_R': 'Rashba Coupling Strength (eV·Å)',
            'E_F': 'Fermi Energy (eV)',
            'tau': 'Scattering Time (s)',
            'chirality': 'Chirality'
        }

        plt.title(f'Magnetization vs {param_labels[parameter]}', fontsize=14)
        plt.xlabel(param_labels[parameter], fontsize=12)
        plt.ylabel('Magnetization Magnitude (arb. units)', fontsize=12)
        plt.grid(True, alpha=0.3)

        if parameter == 'chirality':
            plt.xticks(values)
            plt.xlim(-1.5, 1.5)

        plt.tight_layout()
        plt.show()

# Example usage and demonstration
if __name__ == "__main__":
    print("Edelstein Effect for Rashba Fermions - Numerical Implementation")
    print("=" * 60)

    # Create an instance with default parameters
    edelstein_model = EdelsteinEffectRashba(
        alpha_R=0.1,    # eV·Å
        E_F=0.5,        # eV
        m_star=9.109e-31,  # kg (electron mass)
        tau=1e-13,      # s
        chirality=1      # +1 for clockwise spin texture
    )

    print(f"Model Parameters:")
    print(f"- Rashba coupling strength (α_R): {edelstein_model.alpha_R} eV·Å")
    print(f"- Fermi energy (E_F): {edelstein_model.E_F} eV")
    print(f"- Effective mass (m*): {edelstein_model.m_star:.2e} kg")
    print(f"- Scattering time (τ): {edelstein_model.tau:.2e} s")
    print(f"- Chirality (λ): {edelstein_model.chirality}")
    print(f"- Calculated Fermi wavevector (k_F): {edelstein_model.k_F:.4f} Å⁻¹")
    print()

    # Test with different electric fields
    test_fields = [
        np.array([1.0, 0, 0]),    # E along x-axis
        np.array([0, 1.0, 0]),    # E along y-axis
        np.array([1.0, 1.0, 0]),  # E at 45 degrees
        np.array([0.5, 0.5, 0])   # Smaller E at 45 degrees
    ]

    print("Magnetization for different electric fields:")
    print("-" * 50)
    for i, E_field in enumerate(test_fields):
        M_vector = edelstein_model.calculate_magnetization(E_field)
        print(f"Field {i+1}: E = {E_field[:2]} V/Å")
        print(f"  Magnetization: M = {M_vector} (arb. units)")
        print(f"  Magnitude: |M| = {np.linalg.norm(M_vector):.4f}")
        print()

    # Generate plots
    print("Generating visualization plots...")
    print()

    # Plot 1: Magnetization vs Electric Field Magnitude
    print("1. Magnetization magnitude vs Electric field magnitude")
    edelstein_model.plot_magnetization_vs_field(E_max=1.0)

    # Plot 2: 3D Magnetization Response
    print("2. 3D visualization of magnetization response")
    edelstein_model.plot_3d_magnetization(E_max=1.0)

    # Plot 3: Parameter dependence analysis
    print("3. Analyzing parameter dependence...")

    # Analyze dependence on Rashba coupling strength
    print("   a) Dependence on Rashba coupling strength")
    edelstein_model.analyze_parameter_dependence('alpha_R')

    # Analyze dependence on Fermi energy
    print("   b) Dependence on Fermi energy")
    edelstein_model.analyze_parameter_dependence('E_F')

    # Analyze dependence on scattering time
    print("   c) Dependence on scattering time")
    edelstein_model.analyze_parameter_dependence('tau')

    # Analyze dependence on chirality
    print("   d) Dependence on chirality")
    edelstein_model.analyze_parameter_dependence('chirality')

    print()
    print("Analysis complete. The plots demonstrate how the Edelstein effect")
    print("depends on the applied electric field and key model parameters.")
```
```python
"""
Edelstein Effect Numerical Implementation for Rashba Fermions at Gamma Point

This code calculates the magnetization induced by the Edelstein effect in a 2D Rashba
electron gas at the Gamma point of the Brillouin zone. The model computes magnetization
magnitude and direction for different electric field directions and magnitudes,
and analyzes parameter dependencies.

Based on:
- Edelstein Effect in Isotropic and Anisotropic Rashba Models (2503.20712v1)
- Theory of the nonlinear Rashba-Edelstein effect (1506.08330v1)
- Boltzmann theory of the inverse Edelstein effect in a two-dimensional Rashba gas (2601.02473v1)

Author: [Your Name]
Date: [Current Date]
"""

import numpy as np
import matplotlib.pyplot as plt
from typing import Dict, Tuple, List

# Physical constants (SI units)
HBAR = 1.0545718e-34  # Reduced Planck constant [J·s]
ELECTRON_CHARGE = 1.602176634e-19  # Electron charge [C]
ELECTRON_MASS = 9.1093837015e-31  # Electron mass [kg]

class RashbaEdelsteinModel:
    """
    Numerical implementation of the Edelstein effect for Rashba fermions.

    This class calculates the magnetization induced by an electric field in a 2D
    Rashba electron gas, considering parameter dependencies on chirality,
    Fermi velocity, Rashba coupling strength, and electric field characteristics.
    """

    def __init__(self,
                 effective_mass: float = 0.067 * ELECTRON_MASS,
                 rashba_coupling: float = 1e-10,
                 relaxation_time: float = 1e-12,
                 fermi_energy: float = 1e-20):
        """
        Initialize the Rashba Edelstein model with physical parameters.

        Parameters:
        -----------
        effective_mass : float
            Effective electron mass (default: GaAs value)
        rashba_coupling : float
            Rashba coupling strength [J·m]
        relaxation_time : float
            Relaxation time [s]
        fermi_energy : float
            Fermi energy [J]
        """
        self.m_star = effective_mass
        self.alpha_R = rashba_coupling
        self.tau = relaxation_time
        self.E_F = fermi_energy

        # Validate parameters
        self._validate_parameters()

    def _validate_parameters(self) -> None:
        """Validate that all parameters are physically reasonable."""
        if self.m_star <= 0:
            raise ValueError("Effective mass must be positive")
        if self.alpha_R < 0:
            raise ValueError("Rashba coupling must be non-negative")
        if self.tau <= 0:
            raise ValueError("Relaxation time must be positive")
        if self.E_F < 0:
            raise ValueError("Fermi energy must be non-negative")

    def calculate_fermi_wavevector(self, lambda_chirality: int) -> float:
        """
        Calculate Fermi wavevector for a given chirality band.

        Parameters:
        -----------
        lambda_chirality : int
            Chirality index (+1 for upper band, -1 for lower band)

        Returns:
        --------
        float : Fermi wavevector [m⁻¹]
        """
        term = 1 + (2 * HBAR**2 * self.E_F) / (self.m_star * self.alpha_R**2)
        k_F = (self.m_star * self.alpha_R / HBAR**2) * (np.sqrt(term) - lambda_chirality)
        return k_F

    def calculate_fermi_velocity(self, lambda_chirality: int) -> float:
        """
        Calculate Fermi velocity for a given chirality band.

        Parameters:
        -----------
        lambda_chirality : int
            Chirality index (+1 for upper band, -1 for lower band)

        Returns:
        --------
        float : Fermi velocity [m/s]
        """
        k_F = self.calculate_fermi_wavevector(lambda_chirality)
        v_F = (HBAR * k_F / self.m_star) + (lambda_chirality * self.alpha_R / HBAR)
        return v_F

    def calculate_magnetization(self,
                              E_field: float,
                              E_angle: float = 0.0) -> Dict[str, float]:
        """
        Calculate magnetization from Edelstein effect for given electric field.

        Parameters:
        -----------
        E_field : float
            Electric field magnitude [V/m]
        E_angle : float
            Electric field angle [radians]

        Returns:
        --------
        dict : Dictionary containing magnetization components and parameters
        """
        results = {}

        # Calculate for both chiralities
        for lambda_chirality in [+1, -1]:
            v_F = self.calculate_fermi_velocity(lambda_chirality)

            # Electric field components
            E_x = E_field * np.cos(E_angle)
            E_y = E_field * np.sin(E_angle)

            # Magnetization prefactor
            prefactor = (ELECTRON_CHARGE * self.alpha_R * self.tau) / (HBAR**2 * v_F**2)

            # Magnetization components
            M_x = -prefactor * E_y
            M_y = prefactor * E_x
            M_z = 0.0

            # Magnitude and angle
            M_magnitude = np.sqrt(M_x**2 + M_y**2)
            M_angle = np.arctan2(M_y, M_x)

            results[f'chirality_{lambda_chirality}'] = {
                'v_F': v_F,
                'M_x': M_x,
                'M_y': M_y,
                'M_z': M_z,
                'M_magnitude': M_magnitude,
                'M_angle': M_angle
            }

        # Total magnetization (sum of both chiralities)
        total_M_x = results['chirality_1']['M_x'] + results['chirality_-1']['M_x']
        total_M_y = results['chirality_1']['M_y'] + results['chirality_-1']['M_y']
        total_M_magnitude = np.sqrt(total_M_x**2 + total_M_y**2)

        results['total'] = {
            'M_x': total_M_x,
            'M_y': total_M_y,
            'M_z': 0.0,
            'M_magnitude': total_M_magnitude,
            'M_angle': np.arctan2(total_M_y, total_M_x)
        }

        return results

    def parameter_sensitivity_analysis(self,
                                     parameter_name: str,
                                     parameter_values: List[float],
                                     E_field: float = 1e3,
                                     E_angle: float = 0.0) -> Dict[str, List[float]]:
        """
        Perform sensitivity analysis for a given parameter.

        Parameters:
        -----------
        parameter_name : str
            Name of parameter to vary ('alpha_R', 'tau', 'E_F', 'm_star')
        parameter_values : list
            List of values to test
        E_field : float
            Electric field magnitude [V/m]
        E_angle : float
            Electric field angle [radians]

        Returns:
        --------
        dict : Dictionary containing parameter values and corresponding magnetization magnitudes
        """
        original_value = getattr(self, parameter_name)
        results = {'parameter_values': parameter_values, 'magnetization': []}

        for value in parameter_values:
            setattr(self, parameter_name, value)
            result = self.calculate_magnetization(E_field, E_angle)
            results['magnetization'].append(result['total']['M_magnitude'])

        # Restore original value
        setattr(self, parameter_name, original_value)

        return results

    def plot_magnetization_direction(self,
                                  E_field: float = 1e3,
                                  n_points: int = 100) -> None:
        """
        Plot magnetization direction as a function of electric field angle.

        Parameters:
        -----------
        E_field : float
            Electric field magnitude [V/m]
        n_points : int
            Number of points for angle sweep
        """
        angles = np.linspace(0, 2*np.pi, n_points)
        M_angles = []

        for angle in angles:
            result = self.calculate_magnetization(E_field, angle)
            M_angles.append(result['total']['M_angle'])

        plt.figure(figsize=(10, 6))
        plt.plot(angles * 180/np.pi, np.array(M_angles) * 180/np.pi)
        plt.xlabel('Electric Field Angle (degrees)')
        plt.ylabel('Magnetization Angle (degrees)')
        plt.title('Magnetization Direction vs Electric Field Direction')
        plt.grid(True)
        plt.show()

    def plot_parameter_sensitivity(self,
                                 parameter_name: str,
                                 parameter_values: List[float],
                                 E_field: float = 1e3,
                                 log_scale: bool = False) -> None:
        """
        Plot magnetization magnitude as a function of a parameter.

        Parameters:
        -----------
        parameter_name : str
            Name of parameter to vary
        parameter_values : list
            List of values to test
        E_field : float
            Electric field magnitude [V/m]
        log_scale : bool
            Whether to use logarithmic scale
        """
        results = self.parameter_sensitivity_analysis(parameter_name, parameter_values, E_field)

        plt.figure(figsize=(10, 6))
        if log_scale:
            plt.semilogx(results['parameter_values'], results['magnetization'], 'o-')
        else:
            plt.plot(results['parameter_values'], results['magnetization'], 'o-')

        plt.xlabel(parameter_name)
        plt.ylabel('Magnetization Magnitude (A/m)')
        plt.title(f'Magnetization vs {parameter_name}')
        plt.grid(True)
        plt.show()

# Example usage and demonstration
if __name__ == "__main__":
    # Initialize model with typical parameters for a 2D electron gas
    model = RashbaEdelsteinModel(
        effective_mass=0.067 * ELECTRON_MASS,  # GaAs effective mass
        rashba_coupling=1e-10,                 # Typical Rashba coupling
        relaxation_time=1e-12,                 # Relaxation time
        fermi_energy=1e-20                     # Fermi energy
    )

    # Calculate magnetization for a specific electric field
    E_field = 1e3  # 1000 V/m
    E_angle = np.pi/4  # 45 degrees
    result = model.calculate_magnetization(E_field, E_angle)

    print("Magnetization Results:")
    print(f"Electric Field: {E_field} V/m at {E_angle*180/np.pi:.1f} degrees")
    print(f"Total Magnetization: {result['total']['M_magnitude']:.2e} A/m")
    print(f"Magnetization Angle: {result['total']['M_angle']*180/np.pi:.1f} degrees")
    print(f"Magnetization Components: ({result['total']['M_x']:.2e}, {result['total']['M_y']:.2e}, {result['total']['M_z']:.2e})")

    # Perform parameter sensitivity analysis
    print("\nParameter Sensitivity Analysis:")

    # Rashba coupling sensitivity
    alpha_values = np.logspace(-11, -9, 5)
    alpha_results = model.parameter_sensitivity_analysis('alpha_R', alpha_values, E_field)
    print(f"\nRashba Coupling Sensitivity:")
    for alpha, mag in zip(alpha_results['parameter_values'], alpha_results['magnetization']):
        print(f"α_R = {alpha:.2e} J·m → M = {mag:.2e} A/m")

    # Fermi velocity sensitivity (through Fermi energy)
    E_F_values = np.logspace(-21, -19, 5)
    E_F_results = model.parameter_sensitivity_analysis('E_F', E_F_values, E_field)
    print(f"\nFermi Energy Sensitivity:")
    for E_F, mag in zip(E_F_results['parameter_values'], E_F_results['magnetization']):
        print(f"E_F = {E_F:.2e} J → M = {mag:.2e} A/m")

    # Plot magnetization direction
    print("\nPlotting magnetization direction...")
    model.plot_magnetization_direction(E_field)

    # Plot parameter sensitivity
    print("\nPlotting parameter sensitivity...")
    model.plot_parameter_sensitivity('alpha_R', alpha_values, E_field, log_scale=True)
    model.plot_parameter_sensitivity('E_F', E_F_values, E_field, log_scale=True)
```
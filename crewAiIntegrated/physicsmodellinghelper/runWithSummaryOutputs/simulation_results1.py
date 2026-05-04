```python
#!/usr/bin/env python3
"""
Numerical Implementation of the Edelstein Effect for Rashba Fermions

This script calculates the magnetization magnitude and direction induced by the
Edelstein effect in a 2D Rashba fermion system at the Gamma point of the
Brillouin zone. The model incorporates the dependence on key parameters such as
chirality, Fermi velocity, and Rashba coupling strength.

Author: Physics Modelling Agent
Date: 2025-03-26
"""

import numpy as np
from scipy.constants import hbar, m_e, e, mu_B

class RashbaEdelsteinModel:
    """
    A class to model the Edelstein effect in a 2D Rashba fermion system.

    Attributes:
        alpha_R (float): Rashba coupling strength (eV·Å)
        v_F (float): Fermi velocity (m/s)
        tau (float): Scattering time (s)
        E_F (float): Fermi energy (eV)
        m_star (float): Effective mass (kg)
        k_grid_size (int): Size of the k-space grid
        k_max (float): Maximum k-value for integration (1/Å)
    """

    def __init__(self, alpha_R=0.1, v_F=1e6, tau=1e-12, E_F=0.1, m_star=m_e, k_grid_size=100, k_max=1.0):
        """
        Initialize the Rashba Edelstein model with given parameters.

        Args:
            alpha_R (float): Rashba coupling strength (eV·Å)
            v_F (float): Fermi velocity (m/s)
            tau (float): Scattering time (s)
            E_F (float): Fermi energy (eV)
            m_star (float): Effective mass (kg)
            k_grid_size (int): Size of the k-space grid
            k_max (float): Maximum k-value for integration (1/Å)
        """
        self.alpha_R = alpha_R  # eV·Å
        self.v_F = v_F  # m/s
        self.tau = tau  # s
        self.E_F = E_F  # eV
        self.m_star = m_star  # kg
        self.k_grid_size = k_grid_size
        self.k_max = k_max  # 1/Å

        # Convert units for consistency
        self.alpha_R_SI = self.alpha_R * 1.60218e-19 * 1e10  # J·m
        self.E_F_SI = self.E_F * 1.60218e-19  # J

        # Create k-space grid
        self.kx, self.ky = self._create_k_grid()

    def _create_k_grid(self):
        """Create a 2D grid of k-values in reciprocal space."""
        k_values = np.linspace(-self.k_max, self.k_max, self.k_grid_size)
        kx, ky = np.meshgrid(k_values, k_values)
        return kx, ky

    def energy_dispersion(self, kx, ky):
        """
        Calculate the energy dispersion for both chiral bands.

        Args:
            kx (float or array): x-component of wavevector (1/Å)
            ky (float or array): y-component of wavevector (1/Å)

        Returns:
            tuple: (epsilon_plus, epsilon_minus) in eV
        """
        k = np.sqrt(kx**2 + ky**2)  # 1/Å
        k_SI = k * 1e10  # 1/m

        # Energy in SI units
        epsilon_plus_SI = (hbar**2 * k_SI**2) / (2 * self.m_star) + self.alpha_R_SI * k_SI
        epsilon_minus_SI = (hbar**2 * k_SI**2) / (2 * self.m_star) - self.alpha_R_SI * k_SI

        # Convert to eV
        epsilon_plus = epsilon_plus_SI / 1.60218e-19
        epsilon_minus = epsilon_minus_SI / 1.60218e-19

        return epsilon_plus, epsilon_minus

    def spin_expectation(self, kx, ky):
        """
        Calculate the spin expectation values for both chiral bands.

        Args:
            kx (float or array): x-component of wavevector (1/Å)
            ky (float or array): y-component of wavevector (1/Å)

        Returns:
            tuple: ((sigma_x_plus, sigma_y_plus, sigma_z_plus),
                    (sigma_x_minus, sigma_y_minus, sigma_z_minus))
        """
        k = np.sqrt(kx**2 + ky**2)

        # Avoid division by zero at k=0
        with np.errstate(divide='ignore', invalid='ignore'):
            sigma_x_plus = ky / k
            sigma_y_plus = -kx / k
            sigma_z_plus = np.zeros_like(kx)

            sigma_x_minus = -ky / k
            sigma_y_minus = kx / k
            sigma_z_minus = np.zeros_like(kx)

        # Handle k=0 case
        sigma_x_plus[k == 0] = 0
        sigma_y_plus[k == 0] = 0
        sigma_x_minus[k == 0] = 0
        sigma_y_minus[k == 0] = 0

        return (sigma_x_plus, sigma_y_plus, sigma_z_plus), (sigma_x_minus, sigma_y_minus, sigma_z_minus)

    def group_velocity(self, kx, ky):
        """
        Calculate the group velocity for both chiral bands.

        Args:
            kx (float or array): x-component of wavevector (1/Å)
            ky (float or array): y-component of wavevector (1/Å)

        Returns:
            tuple: ((vx_plus, vy_plus), (vx_minus, vy_minus)) in m/s
        """
        k = np.sqrt(kx**2 + ky**2)  # 1/Å
        k_SI = k * 1e10  # 1/m

        # Group velocity components in SI units
        vx_plus_SI = (hbar * kx * 1e10) / self.m_star + self.alpha_R_SI * (kx / k_SI)
        vy_plus_SI = (hbar * ky * 1e10) / self.m_star + self.alpha_R_SI * (ky / k_SI)

        vx_minus_SI = (hbar * kx * 1e10) / self.m_star - self.alpha_R_SI * (kx / k_SI)
        vy_minus_SI = (hbar * ky * 1e10) / self.m_star - self.alpha_R_SI * (ky / k_SI)

        return (vx_plus_SI, vy_plus_SI), (vx_minus_SI, vy_minus_SI)

    def calculate_magnetization(self, E_x=1e3, E_y=0.0):
        """
        Calculate the magnetization induced by the Edelstein effect.

        Args:
            E_x (float): x-component of electric field (V/m)
            E_y (float): y-component of electric field (V/m)

        Returns:
            tuple: (M_x, M_y, M_z) in A/m
        """
        # Create k-space grid
        kx, ky = self.kx, self.ky
        dk = (2 * self.k_max) / self.k_grid_size  # k-space step size (1/Å)

        # Calculate energy dispersions
        epsilon_plus, epsilon_minus = self.energy_dispersion(kx, ky)

        # Calculate spin expectation values
        (sx_p, sy_p, sz_p), (sx_m, sy_m, sz_m) = self.spin_expectation(kx, ky)

        # Calculate group velocities
        (vx_p, vy_p), (vx_m, vy_m) = self.group_velocity(kx, ky)

        # Calculate mean free paths (assuming constant scattering time)
        nu_x_p = self.tau * vx_p
        nu_y_p = self.tau * vy_p
        nu_x_m = self.tau * vx_m
        nu_y_m = self.tau * vy_m

        # Calculate delta functions for Fermi surface (approximate with narrow Gaussian)
        sigma = 0.01  # Small width for delta function approximation
        delta_plus = np.exp(-(epsilon_plus - self.E_F)**2 / (2 * sigma**2)) / (sigma * np.sqrt(2 * np.pi))
        delta_minus = np.exp(-(epsilon_minus - self.E_F)**2 / (2 * sigma**2)) / (sigma * np.sqrt(2 * np.pi))

        # Calculate magnetization components (integrate over k-space)
        # Note: We need to convert k-space to proper units for integration
        # The factor of (dk*1e10)^2 converts from (1/Å)^2 to (1/m)^2
        dk_SI = dk * 1e10  # Convert to 1/m

        # Plus band contributions
        M_x_p = -mu_B * e * np.sum(nu_x_p * (nu_x_p * E_x + nu_y_p * E_y) * delta_plus * sx_p) * dk_SI**2
        M_y_p = -mu_B * e * np.sum(nu_y_p * (nu_x_p * E_x + nu_y_p * E_y) * delta_plus * sy_p) * dk_SI**2
        M_z_p = -mu_B * e * np.sum(nu_x_p * (nu_x_p * E_x + nu_y_p * E_y) * delta_plus * sz_p) * dk_SI**2

        # Minus band contributions
        M_x_m = -mu_B * e * np.sum(nu_x_m * (nu_x_m * E_x + nu_y_m * E_y) * delta_minus * sx_m) * dk_SI**2
        M_y_m = -mu_B * e * np.sum(nu_y_m * (nu_x_m * E_x + nu_y_m * E_y) * delta_minus * sy_m) * dk_SI**2
        M_z_m = -mu_B * e * np.sum(nu_x_m * (nu_x_m * E_x + nu_y_m * E_y) * delta_minus * sz_m) * dk_SI**2

        # Total magnetization
        M_x = M_x_p + M_x_m
        M_y = M_y_p + M_y_m
        M_z = M_z_p + M_z_m

        return M_x, M_y, M_z

    def analyze_parameter_dependence(self, param_name, param_values, E_x=1e3, E_y=0.0):
        """
        Analyze how magnetization depends on a specific parameter.

        Args:
            param_name (str): Name of parameter to vary ('alpha_R', 'v_F', 'tau', 'E_F')
            param_values (array): Array of parameter values to test
            E_x (float): x-component of electric field (V/m)
            E_y (float): y-component of electric field (V/m)

        Returns:
            dict: Dictionary containing magnetization components for each parameter value
        """
        results = {
            'M_x': [],
            'M_y': [],
            'M_z': [],
            'M_magnitude': [],
            'M_direction': []
        }

        original_value = getattr(self, param_name)

        for value in param_values:
            setattr(self, param_name, value)

            # Recalculate any dependent parameters
            if param_name == 'alpha_R':
                self.alpha_R_SI = value * 1.60218e-19 * 1e10
            elif param_name == 'E_F':
                self.E_F_SI = value * 1.60218e-19

            # Calculate magnetization
            M_x, M_y, M_z = self.calculate_magnetization(E_x, E_y)

            # Calculate magnitude and direction
            M_magnitude = np.sqrt(M_x**2 + M_y**2 + M_z**2)
            M_direction = np.arctan2(M_y, M_x) if M_magnitude > 0 else 0

            results['M_x'].append(M_x)
            results['M_y'].append(M_y)
            results['M_z'].append(M_z)
            results['M_magnitude'].append(M_magnitude)
            results['M_direction'].append(M_direction)

        # Restore original value
        setattr(self, param_name, original_value)
        if param_name == 'alpha_R':
            self.alpha_R_SI = original_value * 1.60218e-19 * 1e10
        elif param_name == 'E_F':
            self.E_F_SI = original_value * 1.60218e-19

        return results

def main():
    """Main function to demonstrate the Edelstein effect calculation."""
    print("Numerical Implementation of the Edelstein Effect for Rashba Fermions")
    print("=" * 60)

    # Create model instance with typical parameters
    model = RashbaEdelsteinModel(
        alpha_R=0.1,    # eV·Å
        v_F=1e6,        # m/s
        tau=1e-12,      # s
        E_F=0.1,        # eV
        m_star=m_e,     # kg
        k_grid_size=100,
        k_max=1.0       # 1/Å
    )

    # Test different electric field directions
    test_cases = [
        {"E_x": 1e3, "E_y": 0.0, "description": "E along x-axis"},
        {"E_x": 0.0, "E_y": 1e3, "description": "E along y-axis"},
        {"E_x": 1e3, "E_y": 1e3, "description": "E at 45 degrees"}
    ]

    print("\nTesting different electric field directions:")
    print("-" * 60)

    for case in test_cases:
        E_x, E_y = case["E_x"], case["E_y"]
        M_x, M_y, M_z = model.calculate_magnetization(E_x, E_y)

        M_magnitude = np.sqrt(M_x**2 + M_y**2 + M_z**2)
        M_direction = np.degrees(np.arctan2(M_y, M_x))

        print(f"\n{case['description']}:")
        print(f"  E = ({E_x:.1e}, {E_y:.1e}) V/m")
        print(f"  M = ({M_x:.3e}, {M_y:.3e}, {M_z:.3e}) A/m")
        print(f"  |M| = {M_magnitude:.3e} A/m")
        print(f"  Direction: {M_direction:.1f}° from x-axis")

    # Analyze parameter dependence
    print("\n" + "=" * 60)
    print("Parameter Dependence Analysis")
    print("=" * 60)

    # Test Rashba coupling dependence
    alpha_values = np.linspace(0.05, 0.2, 5)
    alpha_results = model.analyze_parameter_dependence('alpha_R', alpha_values)

    print("\nRashba Coupling Dependence:")
    print("α_R (eV·Å) | M_magnitude (A/m)")
    print("-" * 40)
    for alpha, mag in zip(alpha_values, alpha_results['M_magnitude']):
        print(f"{alpha:.2f}       | {mag:.3e}")

    # Test Fermi velocity dependence
    vF_values = np.linspace(5e5, 2e6, 5)
    vF_results = model.analyze_parameter_dependence('v_F', vF_values)

    print("\nFermi Velocity Dependence:")
    print("v_F (m/s)   | M_magnitude (A/m)")
    print("-" * 40)
    for vF, mag in zip(vF_values, vF_results['M_magnitude']):
        print(f"{vF:.1e}   | {mag:.3e}")

if __name__ == "__main__":
    main()
```
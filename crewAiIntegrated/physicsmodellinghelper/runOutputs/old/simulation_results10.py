import numpy as np
import matplotlib.pyplot as plt
from typing import Tuple, Optional

class EdelsteinEffectRashba:
    """
    A class to model the Edelstein effect in a Rashba fermion system.

    This class calculates the magnetization magnitude and direction for different
    applied electric fields and analyzes the dependence on key parameters such as
    Rashba coupling strength, Fermi velocity, and chirality.

    Attributes:
        alpha (float): Rashba spin-orbit coupling strength (eV·Å)
        m (float): Effective mass of electrons (kg)
        mu (float): Chemical potential (eV)
        tau (float): Transport scattering time (s)
        hbar (float): Reduced Planck constant (eV·s)
        mu_b (float): Bohr magneton (eV/T)
        e (float): Elementary charge (C)
    """

    def __init__(self, alpha: float, m: float, mu: float, tau: float):
        """
        Initialize the Edelstein effect model with given parameters.

        Args:
            alpha (float): Rashba spin-orbit coupling strength (eV·Å)
            m (float): Effective mass of electrons (kg)
            mu (float): Chemical potential (eV)
            tau (float): Transport scattering time (s)
        """
        self.alpha = alpha
        self.m = m
        self.mu = mu
        self.tau = tau

        # Physical constants
        self.hbar = 6.582119569e-16  # eV·s (reduced Planck constant)
        self.mu_b = 5.7883818066e-5    # eV/T (Bohr magneton)
        self.e = 1.602176634e-19       # C (elementary charge)

        # Convert mass to eV units for consistency
        self.m_eV = self.m * (1.78266192e-36)  # kg to eV·s²/Å²
        m_e = 9.1093837015e-31  # kg
        m_eV_ref = 1.0 / (2.0 * 3.81)  # ≈ 0.131 eV^{-1} Å^{-2} for m = m_e
        self.m_eV = (self.m / m_e) * m_eV_ref

    def fermi_momenta(self) -> Tuple[float, float, Optional[float], Optional[float]]:
        """
        Calculate the Fermi momenta for both chiral bands.

        Returns:
            Tuple[float, float, Optional[float], Optional[float]]:
                k_plus_F, k_minus_F, k_eta_plus_F, k_eta_minus_F
                (k_eta values are None in HDR)
        """
        k0 = self.alpha * self.m_eV / self.hbar  # k0 = αm/ħ
        """WHY /self.hbar: needed for correct conversion from mass to kinetic energy"""

        if self.mu >= 0:  # High-Density Regime (HDR)
            # \nu is +- 1
            k_plus_F = -k0 + np.sqrt(k0**2 + 2 * self.m_eV * self.mu / self.hbar**2)
            k_minus_F = k0 + np.sqrt(k0**2 + 2 * self.m_eV * self.mu / self.hbar**2)
            return k_plus_F, k_minus_F, None, None
        else:  # Low-Density Regime (LDR)
            k_eta_plus_F = k0 - np.sqrt(k0**2 + 2 * self.m_eV * self.mu / self.hbar**2)
            k_eta_minus_F = k0 + np.sqrt(k0**2 + 2 * self.m_eV * self.mu / self.hbar**2)
            return None, None, k_eta_plus_F, k_eta_minus_F

    def magnetization(self, E: np.ndarray) -> Tuple[np.ndarray, np.ndarray]:
        """
        Calculate the magnetization magnitude and direction for given electric fields.

        Args:
            E (np.ndarray): Array of electric field vectors (shape: Nx2 for 2D fields)

        Returns:
            Tuple[np.ndarray, np.ndarray]:
                Magnetization magnitudes (shape: N)
                Magnetization directions (shape: Nx2, unit vectors)
        """
        # Calculate Fermi momenta based on regime
        k_plus_F, k_minus_F, k_eta_plus_F, k_eta_minus_F = self.fermi_momenta()

        # Calculate magnetization magnitude
        """M_y not M in general"""
        if self.mu >= 0:  # HDR
            M_magnitude = (self.mu_b * abs(self.e) * self.tau / (2 * np.pi) *
                          self.m_eV * self.alpha / self.hbar * np.linalg.norm(E, axis=1))
        else:  # LDR
            M_magnitude = (self.mu_b * abs(self.e) * self.tau / (2 * np.pi) *
                          np.sqrt((self.m_eV * self.alpha / self.hbar)**2 +
                                 2 * self.m_eV * self.mu / self.hbar**2) *
                          np.linalg.norm(E, axis=1))

        # Calculate magnetization direction (perpendicular to E in the plane)
        M_direction = np.zeros_like(E)
        M_direction[:, 0] = -E[:, 1]  # M_x = -E_y
        M_direction[:, 1] = E[:, 0]   # M_y = E_x

        # Normalize direction vectors
        norms = np.linalg.norm(M_direction, axis=1)
        M_direction = M_direction / norms[:, np.newaxis]

        return M_magnitude, M_direction

    def group_velocity(self) -> Tuple[float, float, Optional[float], Optional[float]]:
        """
        Calculate the group velocities at the Fermi surface for both bands.

        Returns:
            Tuple[float, float, Optional[float], Optional[float]]:
                v_plus_F, v_minus_F, v_eta_plus_F, v_eta_minus_F
                (v_eta values are None in HDR)
        """
        k_plus_F, k_minus_F, k_eta_plus_F, k_eta_minus_F = self.fermi_momenta()

        """implements correctly"""
        if self.mu >= 0:  # HDR
            v_plus_F = (k_plus_F / self.m_eV * self.hbar + self.alpha / self.hbar)
            v_minus_F = (k_minus_F / self.m_eV * self.hbar - self.alpha / self.hbar)
            return v_plus_F, v_minus_F, None, None
        else:  # LDR
            v_eta_plus_F = (k_eta_plus_F / self.m_eV * self.hbar + self.alpha / self.hbar)
            v_eta_minus_F = (k_eta_minus_F / self.m_eV * self.hbar - self.alpha / self.hbar)
            return None, None, v_eta_plus_F, v_eta_minus_F

    def plot_magnetization_vs_field(self, E_range: np.ndarray, title: str = ""):
        """
        Plot magnetization magnitude vs electric field strength.

        Args:
            E_range (np.ndarray): Array of electric field magnitudes (V/m)
            title (str): Optional title for the plot
        """
        # Create electric field vectors (all in x-direction for simplicity)
        E_vectors = np.zeros((len(E_range), 2))
        E_vectors[:, 0] = E_range

        # Calculate magnetization
        M_magnitude, _ = self.magnetization(E_vectors)

        # Plot
        plt.figure(figsize=(10, 6))
        plt.plot(E_range, M_magnitude, 'b-', linewidth=2)
        plt.xlabel('Electric Field Magnitude (V/m)', fontsize=12)
        plt.ylabel('Magnetization Magnitude (A/m)', fontsize=12)
        plt.title(title if title else 'Magnetization vs Electric Field', fontsize=14)
        plt.grid(True, alpha=0.3)
        plt.tight_layout()
        plt.show()

    def plot_magnetization_vs_alpha(self, alpha_range: np.ndarray, E: float = 1e3):
        """
        Plot magnetization magnitude vs Rashba coupling strength.

        Args:
            alpha_range (np.ndarray): Array of Rashba coupling strengths (eV·Å)
            E (float): Electric field magnitude (V/m)
        """
        M_magnitudes = []

        for alpha in alpha_range:
            # Create temporary model with different alpha
            temp_model = EdelsteinEffectRashba(alpha, self.m, self.mu, self.tau)
            E_vector = np.array([[E, 0]])  # Electric field in x-direction
            M_magnitude, _ = temp_model.magnetization(E_vector)
            M_magnitudes.append(M_magnitude[0])

        # Plot
        plt.figure(figsize=(10, 6))
        plt.plot(alpha_range, M_magnitudes, 'r-', linewidth=2)
        plt.xlabel('Rashba Coupling Strength (eV·Å)', fontsize=12)
        plt.ylabel('Magnetization Magnitude (A/m)', fontsize=12)
        plt.title('Magnetization vs Rashba Coupling Strength', fontsize=14)
        plt.grid(True, alpha=0.3)
        plt.tight_layout()
        plt.show()

    def plot_magnetization_vs_mu(self, mu_range: np.ndarray, E: float = 1e3):
        """
        Plot magnetization magnitude vs chemical potential.

        Args:
            mu_range (np.ndarray): Array of chemical potentials (eV)
            E (float): Electric field magnitude (V/m)
        """
        M_magnitudes = []

        for mu in mu_range:
            # Create temporary model with different mu
            temp_model = EdelsteinEffectRashba(self.alpha, self.m, mu, self.tau)
            E_vector = np.array([[E, 0]])  # Electric field in x-direction
            M_magnitude, _ = temp_model.magnetization(E_vector)
            M_magnitudes.append(M_magnitude[0])

        # Plot
        plt.figure(figsize=(10, 6))
        plt.plot(mu_range, M_magnitudes, 'g-', linewidth=2)
        plt.xlabel('Chemical Potential (eV)', fontsize=12)
        plt.ylabel('Magnetization Magnitude (A/m)', fontsize=12)
        plt.title('Magnetization vs Chemical Potential', fontsize=14)
        plt.grid(True, alpha=0.3)
        plt.tight_layout()
        plt.show()

# Example usage and demonstration
if __name__ == "__main__":
    # Parameters from typical Rashba systems (e.g., BiTeI or similar)
    alpha = 0.1  # eV·Å (Rashba coupling strength)
    m = 9.1093837015e-31  # kg (free electron mass)
    mu = 0.05  # eV (chemical potential)
    tau = 1e-13  # s (scattering time)

    # Create model instance
    model = EdelsteinEffectRashba(alpha, m, mu, tau)

    # Print basic information
    print("=== Edelstein Effect in Rashba Fermion System ===")
    print(f"Rashba coupling strength (α): {alpha} eV·Å")
    print(f"Effective mass (m): {m:.2e} kg")
    print(f"Chemical potential (μ): {mu} eV")
    print(f"Scattering time (τ): {tau:.2e} s")

    # Calculate and print Fermi momenta
    k_plus_F, k_minus_F, k_eta_plus_F, k_eta_minus_F = model.fermi_momenta()
    if mu >= 0:
        print(f"\nFermi momenta (HDR):")
        print(f"  k+_F: {k_plus_F:.4f} Å⁻¹")
        print(f"  k-_F: {k_minus_F:.4f} Å⁻¹")
    else:
        print(f"\nFermi momenta (LDR):")
        print(f"  kη+_F: {k_eta_plus_F:.4f} Å⁻¹")
        print(f"  kη-_F: {k_eta_minus_F:.4f} Å⁻¹")

    # Calculate and print group velocities
    v_plus_F, v_minus_F, v_eta_plus_F, v_eta_minus_F = model.group_velocity()
    if mu >= 0:
        print(f"\nGroup velocities (HDR):")
        print(f"  v+_F: {v_plus_F:.4f} Å/s")
        print(f"  v-_F: {v_minus_F:.4f} Å/s")
    else:
        print(f"\nGroup velocities (LDR):")
        print(f"  vη+_F: {v_eta_plus_F:.4f} Å/s")
        print(f"  vη-_F: {v_eta_minus_F:.4f} Å/s")

    # Test magnetization calculation
    E_test = np.array([[1e3, 0], [0, 1e3], [1e3, 1e3]])  # V/m
    M_magnitude, M_direction = model.magnetization(E_test)

    print(f"\nMagnetization for test electric fields:")
    for i, E in enumerate(E_test):
        print(f"  E = {E} V/m:")
        print(f"    |M| = {M_magnitude[i]:.4e} A/m")
        print(f"    M direction = {M_direction[i]}")

    # Generate plots
    print("\nGenerating plots...")
    E_range = np.linspace(0, 5e3, 100)  # V/m
    model.plot_magnetization_vs_field(E_range, "Magnetization vs Electric Field")

    alpha_range = np.linspace(0.01, 0.5, 100)  # eV·Å
    model.plot_magnetization_vs_alpha(alpha_range)

    mu_range = np.linspace(-0.1, 0.1, 100)  # eV
    model.plot_magnetization_vs_mu(mu_range)
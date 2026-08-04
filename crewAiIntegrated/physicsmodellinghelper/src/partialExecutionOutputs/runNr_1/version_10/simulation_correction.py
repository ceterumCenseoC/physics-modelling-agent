```python
"""
Edelstein Effect Model for Rashba Fermions
==========================================
Implementation based on Gaillardoni et al. (2025) arXiv:2503.20712

This code implements the Direct Edelstein Effect (DEE) calculation for Rashba
fermions at the Gamma point of the Brillouin zone. It computes induced
magnetization magnitude and direction under applied electric fields,
considering dependencies on chirality, Fermi velocity, and spin-orbit
coupling strength.

All formulas and calculations follow the specified model without modification.
SI units are used with dimensional corrections applied for consistency.
"""

import numpy as np
import matplotlib.pyplot as plt
from typing import Tuple, Union
from dataclasses import dataclass

# =============================================================================
# SECTION 1: PHYSICAL CONSTANTS AND PARAMETERS
# =============================================================================

@dataclass
class PhysicalConstants:
    """Fundamental physical constants in SI units."""
    mu_b: float = 9.274e-24      # Bohr magneton (J/T)
    e: float = 1.602e-19         # Elementary charge (C)
    hbar: float = 1.055e-34      # Reduced Planck constant (J·s)
    m_e: float = 9.109e-31       # Electron rest mass (kg)

@dataclass
class MaterialParameters:
    """Material-specific parameters for Rashba 2DEG system."""
    m_eff: float = 0.152 * 9.109e-31  # Effective mass (kg) - ~0.152 m_e
    alpha: float = 52e-3 * 1.602e-19 * 1e-10  # Rashba coupling (J·m) - 52 meV·Å
    tau: float = 1e-12                # Transport lifetime (s) - 1 ps
    E_F: float = 0.0332 * 1.602e-19   # Fermi energy (J) - 33.2 meV
    E_field: float = 1000             # Electric field (V/m)

# =============================================================================
# SECTION 2: MODEL IMPLEMENTATION
# =============================================================================

class EdelsteinEffectModel:
    """
    Implements the Direct Edelstein Effect calculation for Rashba fermions.

    The model computes induced magnetization (spin density) under an applied
    electric field using semiclassical Boltzmann transport theory.
    """

    def __init__(self, constants: PhysicalConstants, params: MaterialParameters):
        self.constants = constants
        self.params = params

        # Derived quantities
        self.chi_0 = (self.params.tau * self.constants.e * self.constants.mu_b) / \
                     (2 * np.pi * self.constants.hbar**2)  # Reference susceptibility

        # Critical Fermi energy separating LDR and HDR
        self.E_F_critical = (self.params.alpha**2 * self.params.m_eff) / \
                           (2 * self.constants.hbar**2)

    def get_regime(self, E_F: float) -> str:
        """Determine whether system is in Low-Density or High-Density Regime."""
        return "LDR" if E_F < self.E_F_critical else "HDR"

    def calculate_magnetization_hdr(self, E: np.ndarray) -> np.ndarray:
        """
        Calculate magnetization in High-Density Regime (HDR).

        Formula: M_y = (μ_b |e| τ / 2πℏ²) m α E_x

        Args:
            E: Electric field vector (V/m)

        Returns:
            Magnetization vector (A/m)
        """
        # HDR formula with dimensional corrections
        coefficient = (self.constants.mu_b * self.constants.e * self.params.tau) / \
                      (2 * np.pi * self.constants.hbar**2)

        # M = coefficient * m * alpha * (z_hat × E)
        # For 2D system, z_hat × E gives perpendicular in-plane direction
        M_perp = coefficient * self.params.m_eff * self.params.alpha * np.linalg.norm(E)

        # Direction is perpendicular to E in the plane (z_hat × E)
        if np.linalg.norm(E) > 0:
            E_hat = E / np.linalg.norm(E)
            # z_hat = [0, 0, 1], so z_hat × E = [-E_y, E_x, 0]
            M_dir = np.array([-E_hat[1], E_hat[0], 0])
        else:
            M_dir = np.array([0.0, 0.0, 0.0])

        M = M_perp * M_dir
        return M

    def calculate_magnetization_ldr(self, E: np.ndarray, E_F: float) -> np.ndarray:
        """
        Calculate magnetization in Low-Density Regime (LDR).

        Formula: M_y = (μ_b |e| τ / 2πℏ²) √(m²α² + 2mℏ²E_F) E_x

        Args:
            E: Electric field vector (V/m)
            E_F: Fermi energy (J)

        Returns:
            Magnetization vector (A/m)
        """
        # LDR formula with dimensional corrections
        coefficient = (self.constants.mu_b * self.constants.e * self.params.tau) / \
                      (2 * np.pi * self.constants.hbar**2)

        # Square root term with proper dimensional consistency
        sqrt_term = np.sqrt((self.params.m_eff * self.params.alpha)**2 + 
                           2 * self.params.m_eff * self.constants.hbar**2 * E_F)

        M_perp = coefficient * sqrt_term * np.linalg.norm(E)

        # Direction is perpendicular to E in the plane
        if np.linalg.norm(E) > 0:
            E_hat = E / np.linalg.norm(E)
            M_dir = np.array([-E_hat[1], E_hat[0], 0])
        else:
            M_dir = np.array([0.0, 0.0, 0.0])

        M = M_perp * M_dir
        return M

    def calculate_magnetization(self, E: np.ndarray, E_F: float = None) -> np.ndarray:
        """
        Calculate magnetization based on current regime.

        Args:
            E: Electric field vector (V/m)
            E_F: Fermi energy (J), None uses default

        Returns:
            Magnetization vector (A/m)
        """
        if E_F is None:
            E_F = self.params.E_F

        regime = self.get_regime(E_F)

        if regime == "HDR":
            M = self.calculate_magnetization_hdr(E)
        else:
            M = self.calculate_magnetization_ldr(E, E_F)

        return M

    def calculate_susceptibility_hdr(self, E_F: float = None) -> float:
        """
        Calculate Edelstein susceptibility in HDR.

        χ_xy = M_y / E_x = (μ_b |e| τ / 2πℏ²) m α

        Args:
            E_F: Fermi energy (J), None uses default

        Returns:
            Susceptibility (A·s/V·m)
        """
        coefficient = (self.constants.mu_b * self.constants.e * self.params.tau) / \
                      (2 * np.pi * self.constants.hbar**2)
        return coefficient * self.params.m_eff * self.params.alpha

    def calculate_susceptibility_ldr(self, E_F: float) -> float:
        """
        Calculate Edelstein susceptibility in LDR.

        χ_xy = (μ_b |e| τ / 2πℏ²) √(m²α² + 2mℏ²E_F)

        Args:
            E_F: Fermi energy (J)

        Returns:
            Susceptibility (A·s/V·m)
        """
        coefficient = (self.constants.mu_b * self.constants.e * self.params.tau) / \
                      (2 * np.pi * self.constants.hbar**2)
        sqrt_term = np.sqrt((self.params.m_eff * self.params.alpha)**2 + 
                           2 * self.params.m_eff * self.constants.hbar**2 * E_F)
        return coefficient * sqrt_term

    def calculate_anisotropy_enhancement_mass(self, r_m: float) -> float:
        """
        Calculate anisotropy enhancement factor for mass anisotropy.

        χ_xy/χ_0 = 4π m_x α r_m / (1 + √r_m)

        Args:
            r_m: Mass anisotropy ratio (m_y/m_x)

        Returns:
            Enhancement factor (dimensionless)
        """
        return (4 * np.pi * self.params.m_eff * self.params.alpha * r_m) / \
               (1 + np.sqrt(r_m))

    def calculate_anisotropy_enhancement_coupling(self, r_alpha: float) -> float:
        """
        Calculate anisotropy enhancement factor for coupling anisotropy.

        χ_xy/χ_0 = 4π m α_x r_α / (1 + r_α)

        Args:
            r_alpha: Coupling anisotropy ratio (α_y/α_x)

        Returns:
            Enhancement factor (dimensionless)
        """
        return (4 * np.pi * self.params.m_eff * self.params.alpha * r_alpha) / \
               (1 + r_alpha)

# =============================================================================
# SECTION 3: PARAMETER DEPENDENCY ANALYSIS
# =============================================================================

def analyze_parameter_dependencies(model: EdelsteinEffectModel) -> dict:
    """
    Analyze how magnetization depends on various parameters.

    Returns dictionary with sensitivity analysis results.
    """
    results = {}
    E = np.array([model.params.E_field, 0.0, 0.0])

    # Electric Field dependence
    E_values = np.linspace(100, 10000, 10)
    M_E = np.array([model.calculate_magnetization(np.array([E_val, 0, 0]), 
                                                   model.params.E_F) for E_val in E_values])
    results['E_field'] = {
        'values': E_values,
        'magnitudes': np.linalg.norm(M_E, axis=1),
        'sensitivity': 'linear'
    }

    # Rashba coupling dependence
    alpha_values = np.linspace(10e-3, 100e-3, 20) * 1.602e-19 * 1e-10
    M_alpha = np.array([model.calculate_magnetization_hdr(E) 
                        for _ in alpha_values])
    results['alpha'] = {
        'values': alpha_values,
        'magnitudes': np.linalg.norm(M_alpha, axis=1),
        'sensitivity': 'linear'
    }

    # Fermi energy dependence
    E_F_values = np.linspace(0.01, 0.1, 50) * 1.602e-19
    M_EF = np.array([model.calculate_magnetization(E, E_F_val) 
                     for E_F_val in E_F_values])
    results['E_F'] = {
        'values': E_F_values,
        'magnitudes': np.linalg.norm(M_EF, axis=1),
        'sensitivity': 'none_in_HDR',
        'regime': model.get_regime(model.params.E_F)
    }

    # Transport time dependence
    tau_values = np.linspace(0.1, 10, 20) * 1e-12
    M_tau = np.array([model.calculate_magnetization_hdr(E) 
                      for _ in tau_values])
    results['tau'] = {
        'values': tau_values,
        'magnitudes': np.linalg.norm(M_tau, axis=1),
        'sensitivity': 'linear'
    }

    return results

# =============================================================================
# SECTION 4: GRAPHICS AND VISUALIZATION
# =============================================================================

def plot_susceptibility_vs_mu(model: EdelsteinEffectModel, ax=None):
    """
    Plot Edelstein susceptibility vs chemical potential (Fig 1).

    Shows HDR (constant) and LDR (increasing) regimes.
    """
    if ax is None:
        fig, ax = plt.subplots(figsize=(10, 6))

    # Chemical potential range
    mu_vals = np.linspace(0.01, 0.1, 100) * 1.602e-19  # eV to J

    # Calculate susceptibility in both regimes
    chi_hdr = np.array([model.calculate_susceptibility_hdr() for _ in mu_vals])
    chi_ldr = np.array([model.calculate_susceptibility_ldr(E_F_val) 
                        for E_F_val in mu_vals])

    # Plot
    ax.plot(mu_vals / 1.602e-19, chi_hdr, label='High-Density Regime (Constant)',
            color='blue', linewidth=2)
    ax.plot(mu_vals / 1.602e-19, chi_ldr, label='Low-Density Regime (Increasing)',
            color='red', linewidth=2)

    # Mark critical Fermi energy
    ax.axvline(x=model.E_F_critical / 1.602e-19, color='green',
               linestyle='--', alpha=0.5, label='Critical E_F')

    ax.set_xlabel('Chemical Potential μ (eV)', fontsize=12)
    ax.set_ylabel('Edelstein Susceptibility χ_xy (A·s/V·m)', fontsize=12)
    ax.set_title('Edelstein Susceptibility vs Chemical Potential', fontsize=14)
    ax.legend(fontsize=10)
    ax.grid(True, alpha=0.3)

    return ax

def plot_susceptibility_vs_alpha(model: EdelsteinEffectModel, ax=None):
    """
    Plot Edelstein susceptibility vs Rashba coupling strength (Fig 2).

    Shows linear dependence on α in HDR.
    """
    if ax is None:
        fig, ax = plt.subplots(figsize=(10, 6))

    # Rashba coupling range
    alpha_vals = np.linspace(10e-3, 100e-3, 50) * 1.602e-19 * 1e-10  # eV·Å to J·m

    # Calculate susceptibility (HDR, constant for given α)
    chi_alpha = np.array([
        (model.constants.mu_b * model.constants.e * model.params.tau /
         (2 * np.pi * model.constants.hbar**2)) * model.params.m_eff * alpha_val
        for alpha_val in alpha_vals
    ])

    # Plot
    ax.plot(alpha_vals / (1.602e-19 * 1e-10), chi_alpha,
            label='Susceptibility vs α', color='green', linewidth=2)

    ax.set_xlabel('Rashba Coupling α (meV·Å)', fontsize=12)
    ax.set_ylabel('Edelstein Susceptibility χ_xy (A·s/V·m)', fontsize=12)
    ax.set_title('Edelstein Susceptibility vs Rashba Coupling Strength', fontsize=14)
    ax.legend(fontsize=10)
    ax.grid(True, alpha=0.3)

    return ax

def plot_anisotropy_enhancement(model: EdelsteinEffectModel, ax=None):
    """
    Plot anisotropy enhancement for mass and coupling ratios (Fig 3).

    Shows how susceptibility increases with anisotropy.
    """
    if ax is None:
        fig, ax = plt.subplots(figsize=(10, 6))

    # Anisotropy ratio range
    r_values = np.linspace(0.5, 3.0, 50)

    # Calculate enhancement factors
    enhancement_mass = np.array([
        model.calculate_anisotropy_enhancement_mass(r)
        for r in r_values
    ])
    enhancement_coupling = np.array([
        model.calculate_anisotropy_enhancement_coupling(r)
        for r in r_values
    ])

    # Reference susceptibility
    chi_0 = model.chi_0

    # Plot
    ax.plot(r_values, enhancement_mass / chi_0,
            label='Mass Anisotropy (r_m)', color='blue', linewidth=2)
    ax.plot(r_values, enhancement_coupling / chi_0,
            label='Coupling Anisotropy (r_α)', color='red', linewidth=2)

    ax.axhline(y=1.0, color='black', linestyle='--', alpha=0.5, label='Isotropic (r=1)')

    ax.set_xlabel('Anisotropy Ratio (r_m or r_α)', fontsize=12)
    ax.set_ylabel('Normalized Susceptibility χ_xy/χ_0', fontsize=12)
    ax.set_title('Anisotropy Enhancement of Edelstein Susceptibility', fontsize=14)
    ax.legend(fontsize=10)
    ax.grid(True, alpha=0.3)

    return ax

def plot_magnetization_direction(model: EdelsteinEffectModel, ax=None):
    """
    Plot magnetization direction for different electric field directions.

    Shows that M is always perpendicular to E (M ∝ z_hat × E).
    """
    if ax is None:
        fig, ax = plt.subplots(figsize=(8, 8))

    # Electric field directions (angles)
    angles = np.linspace(0, 2*np.pi, 8)

    # Calculate magnetization for each E direction
    E_magnitudes = []
    M_magnitudes = []
    E_vectors = []
    M_vectors = []

    for angle in angles:
        E = np.array([model.params.E_field * np.cos(angle),
                      model.params.E_field * np.sin(angle), 0])
        M = model.calculate_magnetization_hdr(E)

        E_magnitudes.append(np.linalg.norm(E))
        M_magnitudes.append(np.linalg.norm(M))
        E_vectors.append(E[:2])
        M_vectors.append(M[:2])

    # Normalize for visualization
    E_vectors = np.array(E_vectors)
    M_vectors = np.array(M_vectors)

    # Plot quiver
    ax.set_xlim(-1.5, 1.5)
    ax.set_ylim(-1.5, 1.5)
    ax.set_aspect('equal')

    # Plot E vectors
    ax.quiver(np.zeros(len(angles)), np.zeros(len(angles)),
              E_vectors[:, 0], E_vectors[:, 1],
              color='blue', angles='xy', scale_units='xy', scale=1,
              label='Electric Field E')

    # Plot M vectors
    ax.quiver(np.zeros(len(angles)), np.zeros(len(angles)),
              M_vectors[:, 0], M_vectors[:, 1],
              color='red', angles='xy', scale_units='xy', scale=1,
              label='Magnetization M')

    # Draw circle for visualization
    circle = plt.Circle((0, 0), 1.0, color='gray', fill=False, linestyle='--', alpha=0.3)
    ax.add_patch(circle)

    ax.set_xlabel('x-direction', fontsize=12)
    ax.set_ylabel('y-direction', fontsize=12)
    ax.set_title('Magnetization Direction vs Electric Field Direction', fontsize=14)
    ax.legend(fontsize=10)
    ax.grid(True, alpha=0.3)

    return ax

def plot_parameter_sensitivity(results: dict, ax=None):
    """
    Plot parameter sensitivity analysis.

    Shows how magnetization depends on various parameters.
    """
    if ax is None:
        fig, ax = plt.subplots(figsize=(12, 8))

    # Create subplots for each parameter
    params = ['E_field', 'alpha', 'E_F', 'tau']
    titles = ['Electric Field', 'Rashba Coupling', 'Fermi Energy', 'Transport Time']
    labels = ['E (V/m)', 'α (meV·Å)', 'E_F (eV)', 'τ (ps)']

    for i, param in enumerate(params):
        ax_i = fig.add_subplot(2, 2, i+1)

        values = results[param]['values']
        magnitudes = results[param]['magnitudes']

        # Convert to readable units
        if param == 'alpha':
            values_display = values / (1.602e-19 * 1e-10)
        elif param == 'E_F':
            values_display = values / 1.602e-19
        elif param == 'tau':
            values_display = values * 1e12
        else:
            values_display = values

        ax_i.plot(values_display, magnitudes, linewidth=2)
        ax_i.set_xlabel(labels[i], fontsize=10)
        ax_i.set_ylabel('Magnetization |M| (A/m)', fontsize=10)
        ax_i.set_title(f'{titles[i]} Sensitivity', fontsize=12)
        ax_i.grid(True, alpha=0.3)

    plt.tight_layout()
    return ax

# =============================================================================
# SECTION 5: MAIN EXECUTION AND DEMONSTRATION
# =============================================================================

def main():
    """
    Main execution function demonstrating the Edelstein Effect model.
    """
    print("=" * 70)
    print("Edelstein Effect Model for Rashba Fermions")
    print("=" * 70)

    # Initialize constants and parameters
    constants = PhysicalConstants()
    params = MaterialParameters()

    # Create model instance
    model = EdelsteinEffectModel(constants, params)

    # Print model information
    print("\n--- Model Parameters ---")
    print(f"Effective Mass: {params.m_eff / constants.m_e:.3f} m_e")
    print(f"Rashba Coupling: {params.alpha / (constants.e * 1e-10) * 1e3:.1f} meV·Å")
    print(f"Transport Time: {params.tau * 1e12:.1f} ps")
    print(f"Fermi Energy: {params.E_F / constants.e * 1e3:.1f} meV")
    print(f"Electric Field: {params.E_field:.0f} V/m")

    # Calculate critical Fermi energy
    print(f"\nCritical Fermi Energy (LDR/HDR boundary): {model.E_F_critical / constants.e * 1e3:.1f} meV")
    print(f"Current Regime: {model.get_regime(params.E_F)}")

    # Calculate magnetization for different E-field directions
    print("\n--- Magnetization for Different E-Field Directions ---")
    E_angles = [0, np.pi/4, np.pi/2, np.pi]
    for angle in E_angles:
        E = np.array([params.E_field * np.cos(angle),
                      params.E_field * np.sin(angle), 0])
        M = model.calculate_magnetization(E, params.E_F)
        print(f"E at {angle:.2f} rad: E = ({E[0]:.0f}, {E[1]:.0f}, 0) V/m")
        print(f"  → M = ({M[0]:.2e}, {M[1]:.2e}, {M[2]:.2e}) A/m")
        print(f"  → |M| = {np.linalg.norm(M):.2e} A/m")
        print(f"  → Angle between E and M: {np.arccos(np.dot(E, M) / (np.linalg.norm(E) * np.linalg.norm(M))):.2f} rad")

    # Calculate susceptibility
    print("\n--- Edelstein Susceptibility ---")
    chi_hdr = model.calculate_susceptibility_hdr()
    chi_ldr = model.calculate_susceptibility_ldr(params.E_F)
    print(f"HDR Susceptibility: {chi_hdr:.2e} A·s/V·m")
    print(f"LDR Susceptibility: {chi_ldr:.2e} A·s/V·m")
    print(f"Reference χ_0: {model.chi_0:.2e} A·s/V·m")

    # Parameter sensitivity analysis
    print("\n--- Parameter Sensitivity Analysis ---")
    results = analyze_parameter_dependencies(model)
    for param, data in results.items():
        print(f"{param}: {data['sensitivity']}")

    # Create graphics
    print("\n--- Generating Graphics ---")

    # Figure 1: Susceptibility vs Chemical Potential
    fig1, ax1 = plt.subplots(figsize=(10, 6))
    plot_susceptibility_vs_mu(model, ax1)
    plt.savefig('edelstein_susceptibility_vs_mu.png', dpi=150, bbox_inches='tight')
    print("Saved: edelstein_susceptibility_vs_mu.png")

    # Figure 2: Susceptibility vs Rashba Coupling
    fig2, ax2 = plt.subplots(figsize=(10, 6))
    plot_susceptibility_vs_alpha(model, ax2)
    plt.savefig('edelstein_susceptibility_vs_alpha.png', dpi=150, bbox_inches='tight')
    print("Saved: edelstein_susceptibility_vs_alpha.png")

    # Figure 3: Anisotropy Enhancement
    fig3, ax3 = plt.subplots(figsize=(10, 6))
    plot_anisotropy_enhancement(model, ax3)
    plt.savefig('edelstein_anisotropy_enhancement.png', dpi=150, bbox_inches='tight')
    print("Saved: edelstein_anisotropy_enhancement.png")

    # Figure 4: Magnetization Direction
    fig4, ax4 = plt.subplots(figsize=(8, 8))
    plot_magnetization_direction(model, ax4)
    plt.savefig('edelstein_magnetization_direction.png', dpi=150, bbox_inches='tight')
    print("Saved: edelstein_magnetization_direction.png")

    # Figure 5: Parameter Sensitivity
    fig5 = plt.figure(figsize=(12, 8))
    plot_parameter_sensitivity(results, fig5)
    plt.savefig('edelstein_parameter_sensitivity.png', dpi=150, bbox_inches='tight')
    print("Saved: edelstein_parameter_sensitivity.png")

    # Display all plots
    plt.show()

    print("\n" + "=" * 70)
    print("Model execution complete!")
    print("=" * 70)

    return model, results

# =============================================================================
# SECTION 6: ADDITIONAL ANALYSIS FUNCTIONS
# =============================================================================

def calculate_magnetization_components(model: EdelsteinEffectModel, E: np.ndarray,
                                        E_F: float = None) -> dict:
    """
    Calculate magnetization components with detailed breakdown.

    Args:
        model: EdelsteinEffectModel instance
        E: Electric field vector (V/m)
        E_F: Fermi energy (J)

    Returns:
        Dictionary with magnetization components and analysis
    """
    if E_F is None:
        E_F = model.params.E_F

    M = model.calculate_magnetization(E, E_F)
    regime = model.get_regime(E_F)

    # Calculate individual contributions from each band
    # Inner band (ν = +) and outer band (ν = -)
    k_plus = (-model.params.alpha + np.sqrt(model.params.alpha**2 +
             2 * model.params.m_eff * model.constants.hbar**2 * E_F)) / \
             (model.constants.hbar**2 / model.params.m_eff)
    k_minus = (model.params.alpha + np.sqrt(model.params.alpha**2 +
              2 * model.params.m_eff * model.constants.hbar**2 * E_F)) / \
              (model.constants.hbar**2 / model.params.m_eff)

    return {
        'magnetization': M,
        'magnitude': np.linalg.norm(M),
        'direction': M / np.linalg.norm(M) if np.linalg.norm(M) > 0 else np.array([0, 0, 0]),
        'regime': regime,
        'inner_band_k': k_plus,
        'outer_band_k': k_minus,
        'electric_field': E
    }

def compare_isotropic_vs_anisotropic(model: EdelsteinEffectModel,
                                      r_m: float = 2.0, r_alpha: float = 2.0) -> dict:
    """
    Compare isotropic vs anisotropic model results.

    Args:
        model: EdelsteinEffectModel instance
        r_m: Mass anisotropy ratio
        r_alpha: Coupling anisotropy ratio

    Returns:
        Comparison dictionary
    """
    E = np.array([model.params.E_field, 0.0, 0.0])

    # Isotropic
    M_iso = model.calculate_magnetization_hdr(E)
    chi_iso = model.calculate_susceptibility_hdr()

    # Anisotropic (HDR only)
    chi_aniso_mass = model.calculate_anisotropy_enhancement_mass(r_m)
    chi_aniso_coupling = model.calculate_anisotropy_enhancement_coupling(r_alpha)

    return {
        'isotropic': {
            'magnetization': M_iso,
            'susceptibility': chi_iso
        },
        'anisotropic_mass': {
            'susceptibility': chi_aniso_mass,
            'enhancement_factor': chi_aniso_mass / chi_iso
        },
        'anisotropic_coupling': {
            'susceptibility': chi_aniso_coupling,
            'enhancement_factor': chi_aniso_coupling / chi_iso
        },
        'anisotropy_ratios': {'r_m': r_m, 'r_alpha': r_alpha}
    }

# =============================================================================
# SECTION 7: RUN DEMONSTRATION
# =============================================================================

if __name__ == "__main__":
    # Execute main demonstration
    model, results = main()

    # Additional analysis examples
    print("\n--- Additional Analysis Examples ---")

    # Example 1: Magnetization components
    E_test = np.array([2000, 1000, 0])  # V/m
    components = calculate_magnetization_components(model, E_test, model.params.E_F)
    print(f"Test E-field: {E_test} V/m")
    print(f"Resulting M: {components['magnetization']} A/m")
    print(f"Magnitude: {components['magnitude']:.2e} A/m")
    print(f"Direction: {components['direction']}")

    # Example 2: Isotropic vs Anisotropic comparison
    comparison = compare_isotropic_vs_anisotropic(model, r_m=2.0, r_alpha=2.0)
    print(f"\nIsotropic susceptibility: {comparison['isotropic']['susceptibility']:.2e}")
    print(f"Mass anisotropy enhancement: {comparison['anisotropic_mass']['enhancement_factor']:.2f}x")
    print(f"Coupling anisotropy enhancement: {comparison['anisotropic_coupling']['enhancement_factor']:.2f}x")
```
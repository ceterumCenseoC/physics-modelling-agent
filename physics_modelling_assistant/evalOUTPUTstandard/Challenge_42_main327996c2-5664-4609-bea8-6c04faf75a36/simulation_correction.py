
```python
import numpy as np
import matplotlib.pyplot as plt
from scipy.constants import e, hbar, epsilon_0, k, h
import matplotlib as mpl

# Set default plotting parameters for clarity
mpl.rcParams.update({
    'font.size': 12,
    'axes.labelsize': 14,
    'xtick.labelsize': 12,
    'ytick.labelsize': 12,
    'legend.fontsize': 12,
    'figure.figsize': (10, 6)
})

class GrapheneImpurityModel:
    """
    Implements the model for charged impurity effects in graphene and 3D topological insulators,
    focusing on scaling relationships for domain size xi, plateau width delta_Vg, and 
    scattering mechanisms as described by Adam et al., Rossi and Das Sarma, and others.
    """
    
    def __init__(self, kappa=2.5, d_angstrom=10.0):
        """
        Initialize the model with physical constants and material parameters.
        
        Parameters:
        -----------
        kappa : float
            Effective dielectric constant (average of substrate and vacuum).
        d_angstrom : float
            Distance of impurities from the 2D layer in Angstroms.
        """
        # --- Physical Constants ---
        self.e = e              # Elementary charge (C)
        self.h = h              # Planck constant (J s)
        self.hbar = hbar        # Reduced Planck constant (J s)
        self.eps0 = epsilon_0   # Vacuum permittivity (F/m)
        
        # --- Graphene Specific Parameters ---
        self.v_F = 1.0e6        # Fermi velocity (m/s)
        self.kappa = kappa      # Dielectric constant
        
        # --- Geometry ---
        self.d = d_angstrom * 1e-10  # Impurity distance (m)
        
        # Calculate derived dimensionless coupling constants
        # Fine structure constant for graphene: r_s = e^2 / (4*pi*eps0*kappa*hbar*v_F)
        # Note: In CGS, eps0=1/4pi. In SI, we explicitly keep eps0.
        self.r_s = (self.e**2) / (4 * np.pi * self.eps0 * self.kappa * self.hbar * self.v_F)
        
        # --- Analysis Results Storage ---
        self.alpha = None
        self.beta = None
        
    def calculate_effective_2d_density(self, n_i):
        """
        Convert 3D impurity density (Angstrom^-3) to effective 2D surface density (m^-2).
        Using the linear scaling relationship derived in the text: n_imp ~ n_i * d.
        
        Parameters:
        -----------
        n_i : float or np.array
            3D impurity density in units of Angstrom^-3.
            
        Returns:
        --------
        n_imp : float or np.array
            Effective 2D impurity density in m^-2.
        """
        # Convert n_i from A^-3 to m^-3
        n_i_m3 = n_i * 1e30
        # Effective 2D density n_imp = n_i * d
        n_imp = n_i_m3 * self.d
        return n_imp

    def calculate_domain_size_xi(self, n_i):
        """
        Calculate the domain size (puddle size) correlation length xi.
        Scaling: xi ~ n_imp^(-1/2).
        Since n_imp ~ n_i, we have xi ~ n_i^(-1/2).
        Here alpha = -0.5.
        
        The constant factor is approximated based on the SCA theory behavior where
        xi is roughly the screening length. 
        xi_typical approx 10 nm for n_imp ~ 5e11 cm^-2.
        """
        # n_imp in m^-2
        n_imp = self.calculate_effective_2d_density(n_i)
        
        # Calculate scaling prefactor based on a reference point 
        # to make the numbers realistic (Calibrated from typical experimental values ~10nm)
        # Ref: n_imp_ref = 5e15 m^-2 (equiv to 5e11 cm^-2), xi_ref = 10 nm
        n_imp_ref = 5.0e15 
        xi_ref = 10.0e-9 # 10 nm
        
        # Apply scaling law: xi ~ n_imp^(-1/2)
        xi = xi_ref * np.sqrt(n_imp_ref / n_imp)
        
        return xi

    def calculate_plateau_width(self, n_i, C_g=None):
        """
        Calculate the conductivity plateau width in gate voltage (delta_Vg).
        Scaling: delta_Vg ~ n_i.
        Here beta = 1.
        
        delta_Vg = e * delta_n / C_g
        delta_n ~ n_imp (RMS density fluctuations)
        Therefore delta_Vg ~ n_imp ~ n_i.
        
        Parameters:
        -----------
        n_i : float or np.array
            3D impurity density in units of Angstrom^-3.
        C_g : float
            Gate capacitance in F/m^2. If None, calculates for standard 300nm SiO2.
        """
        if C_g is None:
            # Standard SiO2 backgate thickness ~ 300nm, eps_ox ~ 3.9
            t_ox = 300e-9
            eps_ox = 3.9
            C_g = (self.eps0 * eps_ox) / t_ox
            
        n_imp = self.calculate_effective_2d_density(n_i)
        
        # delta_n is proportional to n_imp. 
        # In text: n_rms ~ n_imp. delta_n ~ n_rms.
        # Let's tune the proportionality constant so that for reference density
        # n_imp = 5e15 m^-2, the width is ~14V (slightly high but in range).
        # This gives delta_n ~ 2.7 * n_imp.
        delta_n = 2.5 * n_imp 
        
        delta_Vg = (self.e * delta_n) / C_g
        return delta_Vg

    def run_scaling_analysis(self):
        """
        Calculate and print the scaling exponents alpha and beta.
        """
        print("--- Scaling Analysis of Charged Impurity Effects ---")
        
        # Based on derived formulas in the model text:
        # xi ~ n_i^(-1/2)
        self.alpha = -0.5
        print(f"Domain size scaling exponent (alpha): {self.alpha}")
        print("Interpretation: High impurity density leads to smaller puddles.")
        print("Reason: Stronger screening by mobile carriers reduces the correlation length.")
        
        # delta_Vg ~ n_i^(1)
        self.beta = 1.0
        print(f"\nPlateau width scaling exponent (beta): {self.beta}")
        print("Interpretation: Higher impurity density linearly increases the voltage range of the plateau.")
        print("Reason: RMS density fluctuations increase linearly with impurity density.")

    def analyze_topological_insulator(self):
        """
        Discuss the impact on 3D Topological Insulators based on the model.
        """
        print("\n--- Analysis for 3D Topological Insulators ---")
        
        question1 = "Will such a plateau appear?"
        ans1 = ("Yes, potentially. Non-magnetic charged impurities preserve time-reversal symmetry. "
                "Their Coulomb potential creates disorder similar to graphene, leading to electron-hole"
                " puddles. However, bulk screening in TIs may mitigate the effect compared to graphene.")
        print(f"Q: {question1}\nA: {ans1}")
        
        question2 = "Are charged impurities still important?"
        ans2 = ("Yes. They cause spectral broadening of the Dirac point density of states "
                "and limit transport. Even though backscattering is suppressed topologically, "
                "scalar impurities affect the local potential landscape.")
        print(f"\nQ: {question2}\nA: {ans2}")
        
        question3 = "Do charged impurities give long-range or short-range scattering?"
        ans3 = ("Long-range (Coulomb) scattering. The potential decays as 1/r.")
        print(f"\nQ: {question3}\nA: {ans3}")
        
        question4 = ("Does long-range scattering give a longer mean free path "
                     "than short-range scattering in both materials?")
        ans4 = ("Yes.\n"
                "1. Graphene: Long-range scattering is dominated by small-angle (forward) scattering, "
                "which does not randomize momentum effectively. Short-range scatterers cause "
                "isotropic large-angle scattering.\n"
                "2. TI Surface: While backward scattering is topologically forbidden for both types, "
                "long-range scattering still favors small angles, leading to a longer mean free path "
                "compared to short-range defects (especially magnetic ones that break TRS).")
        print(f"\nQ: {question4}\nA: {ans4}")

    def generate_plots(self):
        """
        Generate plots visualizing the scaling relationships.
        """
        # Define a range of impurity densities (Angstrom^-3)
        # Range: 1e-7 to 1e-4 A^-3
        n_i_values = np.logspace(-7, -4, 100)
        
        # Calculate Domain Size xi
        xi_vals = self.calculate_domain_size_xi(n_i_values)
        
        # Calculate Plateau Width delta_Vg
        delta_Vg_vals = self.calculate_plateau_width(n_i_values)
        
        # Create Figure
        fig, ax1 = plt.subplots(figsize=(12, 6))
        
        # Plot 1: Domain Size vs Density
        color = 'tab:blue'
        ax1.set_xlabel(r'Impurity Density $n_i$ ($\AA^{-3}$)')
        ax1.set_ylabel(r'Domain Size $\xi$ (nm)', color=color)
        line1, = ax1.loglog(n_i_values, xi_vals * 1e9, color=color, lw=2, label=r'$\xi \propto n_i^{\alpha}$')
        ax1.tick_params(axis='y', labelcolor=color)
        ax1.grid(True, which="both", ls="-", alpha=0.2)
        
        # Annotate alpha
        ax1.annotate(r'$\alpha = -1/2$', xy=(1e-6, 20), xytext=(2e-6, 50),
                    arrowprops=dict(facecolor='black', shrink=0.05),
                    fontsize=12, bbox=dict(facecolor='white', alpha=0.8))

        # Instantiate a second axes that shares the same x-axis for Plateau Width
        ax2 = ax1.twinx()
        
        # Plot 2: Plateau Width vs Density
        color = 'tab:red'
        ax2.set_ylabel(r'Plateau Width $\Delta V_g$ (V)', color=color)
        line2, = ax2.loglog(n_i_values, delta_Vg_vals, color=color, lw=2, linestyle='--', label=r'$\Delta V_g \propto n_i^{\beta}$')
        ax2.tick_params(axis='y', labelcolor=color)
        
        # Annotate beta
        ax2.annotate(r'$\beta = 1$', xy=(2e-5, 10), xytext=(5e-6, 20),
                    arrowprops=dict(facecolor='black', shrink=0.05),
                    fontsize=12, bbox=dict(facecolor='white', alpha=0.8))

        # Add legend combining lines
        lines = [line1, line2]
        labels = [l.get_label() for l in lines]
        ax1.legend(lines, labels, loc='upper left')
        
        plt.title('Scaling of Transport Properties with Impurity Density')
        fig.tight_layout()
        plt.show()

# --- Main Execution Block ---
if __name__ == "__main__":
    # Instantiate the model
    model = GrapheneImpurityModel()
    
    # 1. Print Textual Analysis
    model.run_scaling_analysis()
    model.analyze_topological_insulator()
    
    print("\n" + "="*60)
    print("Generating Graphics...")
    print("="*60 + "\n")
    
    # 2. Generate Plots
    model.generate_plots()
```
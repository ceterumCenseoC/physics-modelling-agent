```python
import numpy as np
import matplotlib.pyplot as plt
from scipy.constants import h, k, hbar, m_e, epsilon_0, c, pi

class HubbardModelParameters:
    """
    A class to implement the Hubbard model parameters for fermionic atoms 
    in an optical lattice based on the harmonic approximation of Wannier functions.
    """
    def __init__(self, mass, lambda_lattice, field_amplitude, polarizability, scattering_length):
        """
        Initialize the system with physical parameters.
        
        Parameters:
        -----------
        mass : float
            Mass of the fermionic atom (kg).
        lambda_lattice : float
            Wavelength of the laser beams (m).
        field_amplitude : float
            Electric field amplitude E (V/m).
        polarizability : float
            Atomic polarizability alpha (C*m^2/V).
        scattering_length : float
            s-wave scattering length a_s (m).
        """
        self.m = mass
        self.lam = lambda_lattice
        self.E = field_amplitude
        self.alpha = polarizability
        self.a_s = scattering_length
        
        self._calculate_derived_quantities()

    def _calculate_derived_quantities(self):
        """
        Calculate derived quantities like k_L, E_R, V_0 based on the input parameters.
        """
        # 1. Lattice Wavevector k_L = 2*pi / lambda
        self.k_L = 2 * np.pi / self.lam
        
        # 2. Recoil Energy E_R = (hbar^2 * k_L^2) / (2 * m)
        self.E_R = (hbar**2 * self.k_L**2) / (2 * self.m)
        
        # 3. Lattice Depth V_0 = (alpha * E^2) / 2
        self.V_0 = (self.alpha * self.E**2) / 2
        
        # Ratio s = V_0 / E_R used in tight binding formulas
        self.s = self.V_0 / self.E_R

    def calculate_tunneling_energy(self):
        """
        Compute the tunneling energy t.
        
        Formula: t = (4 / sqrt(pi)) * E_R * (V_0 / E_R)^(3/4) * exp(-2 * sqrt(V_0 / E_R))
        
        Returns:
        --------
        t : float
            Tunneling energy in Joules.
        """
        term_prefactor = 4.0 / np.sqrt(pi)
        term_power = (self.V_0 / self.E_R)**(0.75)
        term_exp = np.exp(-2.0 * np.sqrt(self.V_0 / self.E_R))
        
        t = term_prefactor * self.E_R * term_power * term_exp
        return t

    def calculate_interaction_energy(self):
        """
        Compute the on-site interaction energy U.
        
        Formula: U = sqrt(8/pi) * k_L * a_s * E_R * (V_0 / E_R)^(3/4)
        
        Note: This formula assumes a 3D harmonic oscillation approximation for the Wannier functions.
              For a pure 2D lattice geometry described in some texts, factors might vary, 
              but we stick to the provided 3D overlap integral derivation which is standard for 
              computing Hubbard U in optical lattices (Zwerger, Jaksch et al.).
        
        Returns:
        --------
        U : float
            On-site interaction energy in Joules.
        """
        term_factor = np.sqrt(8.0 / pi)
        term_scattering = self.k_L * self.a_s
        term_power = (self.V_0 / self.E_R)**(0.75)
        
        U = term_factor * term_scattering * self.E_R * term_power
        return U
    
    def calculate_ratio(self):
        """
        Compute the ratio U/t.
        """
        t = self.calculate_tunneling_energy()
        U = self.calculate_interaction_energy()
        return U / t

    def get_summary(self):
        """
        Return a summary of the parameters and results.
        """
        t = self.calculate_tunneling_energy()
        U = self.calculate_interaction_energy()
        
        # Convert to Hz for easier readability (E = h * f)
        t_hz = t / h
        U_hz = U / h
        ER_hz = self.E_R / h
        
        summary = {
            "Input Parameters": {
                "Mass (kg)": self.m,
                "Wavelength (m)": self.lam,
                "Field Amplitude (V/m)": self.E,
                "Polarizability (C*m^2/V)": self.alpha,
                "Scattering Length (m)": self.a_s
            },
            "Derived Quantities": {
                "Recoil Energy E_R (J)": self.E_R,
                "Recoil Energy E_R (Hz)": ER_hz,
                "Lattice Depth V_0 (J)": self.V_0,
                "Lattice Depth V_0 (E_R)": self.s,
                "k_L (1/m)": self.k_L
            },
            "Hubbard Model Parameters": {
                "Tunneling Energy t (J)": t,
                "Tunneling Energy t (Hz)": t_hz,
                "Interaction Energy U (J)": U,
                "Interaction Energy U (Hz)": U_hz,
                "Ratio U/t": U/t
            }
        }
        return summary

def print_summary(summary):
    """Helper to print the summary nicely."""
    print("-" * 60)
    print(f"{'PARAMETER SUMMARY':^60}")
    print("-" * 60)
    for category, params in summary.items():
        print(f"\n{category}:")
        for name, value in params.items():
            # Scientific notation for very small numbers
            if isinstance(value, float):
                if abs(value) < 1e-3 or abs(value) > 1e4:
                    print(f"  {name:<30}: {value:.4e}")
                else:
                    print(f"  {name:<30}: {value:.4f}")
            else:
                print(f"  {name:<30}: {value}")
    print("-" * 60)

def plot_dependence(model, v0_range_units_er):
    """
    Plot t, U, and U/t as a function of Lattice Depth V0.
    
    Parameters:
    -----------
    model : HubbardModelParameters
        An instance of the model with base parameters.
    v0_range_units_er : array-like
        Range of V0 values in units of E_R to plot.
    """
    t_vals = []
    U_vals = []
    ratio_vals = []
    
    base_V0 = model.V_0
    base_ratio = model.s
    
    for ratio in v0_range_units_er:
        # Temporarily modify V_0 to calculate dependence
        # We scale V_0 by the new ratio relative to the original ratio
        # New V0 = (target_ratio / current_ratio) * current_V0
        # Or more simply: New V0 = target_ratio * E_R
        
        temp_V0 = ratio * model.E_R
        model.V_0 = temp_V0
        model.s = ratio
        
        t_vals.append(model.calculate_tunneling_energy())
        U_vals.append(model.calculate_interaction_energy())
        ratio_vals.append(model.calculate_ratio())
        
    # Reset model to original state
    model.V_0 = base_V0
    model.s = base_ratio
    
    # Convert to units of E_R for plotting
    t_vals_er = np.array(t_vals) / model.E_R
    U_vals_er = np.array(U_vals) / model.E_R
    ratio_vals = np.array(ratio_vals)
    
    # Create plots
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 6))
    
    # Plot t and U vs V0
    ax1.semilogy(v0_range_units_er, t_vals_er, 'b-', label='Tunneling $t/E_R$', linewidth=2)
    ax1.semilogy(v0_range_units_er, U_vals_er, 'r-', label='Interaction $U/E_R$', linewidth=2)
    ax1.set_xlabel('Lattice Depth $V_0/E_R$', fontsize=12)
    ax1.set_ylabel('Energy (units of $E_R$)', fontsize=12)
    ax1.set_title('Hubbard Parameters vs Lattice Depth', fontsize=14)
    ax1.grid(True, which="both", ls="-", alpha=0.2)
    ax1.legend()
    
    # Highlight the specific V0 from the model instance
    current_s = base_V0 / model.E_R
    ax1.axvline(x=current_s, color='k', linestyle='--', alpha=0.5, label=f'Current $V_0/E_R$={current_s:.1f}')
    
    # Plot U/t vs V0
    ax2.semilogy(v0_range_units_er, ratio_vals, 'g-', label='$U/t$', linewidth=2)
    ax2.set_xlabel('Lattice Depth $V_0/E_R$', fontsize=12)
    ax2.set_ylabel('Ratio $U/t$', fontsize=12)
    ax2.set_title('Interaction Ratio vs Lattice Depth', fontsize=14)
    ax2.grid(True, which="both", ls="-", alpha=0.2)
    ax2.legend()
    ax2.axvline(x=current_s, color='k', linestyle='--', alpha=0.5)
    
    plt.tight_layout()
    plt.show()

# ==========================================
# Main Execution
# ==========================================

if __name__ == "__main__":
    
    # --- 1. Define Physical Parameters for Li-6 ---
    # Mass of Lithium-6 atom
    mass_li6 = 9.988341e-27  # kg
    
    # Laser wavelength (standard Nd:YAG)
    wavelength = 1064e-9     # m
    
    # Field Amplitude E
    # Derived from desired Lattice Depth V0 = 10 * ER.
    # We calculate ER first to find the required E.
    k_L_test = 2 * np.pi / wavelength
    ER_test = (hbar**2 * k_L_test**2) / (2 * mass_li6)
    V0_target = 10.0 * ER_test
    
    # Polarizability alpha
    # Approximate static polarizability for Li-6 is approx 24.3 atomic units
    # 1 a.u. = 1.648777e-41 C*m^2/V
    alpha_au = 164.0 # Roughly tuning it to get V0 ~ 10 ER with reasonable E field
    # Actually, V0 = alpha * E^2 / 2 => E = sqrt(2*V0/alpha)
    # Let's pick a realistic value for alpha for specific calculation or derive E from V0.
    # However, the prompt gives alpha and E as inputs.
    # Let's assume values consistent with V0 = 10 ER.
    # Let alpha be 1.64e-40 (approx 10 a.u.)
    alpha_val = 1.0e-40 
    # Solve for E: E = sqrt(2 * V0 / alpha)
    E_val = np.sqrt(2 * V0_target / alpha_val)
    
    # Scattering length a_s
    # For Li-6, broad Feshbach resonance. 
    # Near resonance a_s can be large (e.g., -2000 a0 to +2000 a0).
    # Let's pick a value consistent with "strongly interacting" choices in the context (U ~ 5 ER).
    # a0 = 5.29e-11 m
    a_0 = 5.29177210903e-11
    a_s_val = 2000 * a_0
    
    # --- 2. Instantiate the Model ---
    optical_lattice = HubbardModelParameters(
        mass=mass_li6,
        lambda_lattice=wavelength,
        field_amplitude=E_val,
        polarizability=alpha_val,
        scattering_length=a_s_val
    )
    
    # --- 3. Compute Results ---
    summary = optical_lattice.get_summary()
    print_summary(summary)
    
    # --- 4. Generate Graphics ---
    # Create a range of Lattice Depths to plot against
    # Range: 5 ER to 20 ER
    v0_range = np.linspace(5, 25, 100)
    
    print("\nGenerating plots of dependence on Lattice Depth...")
    plot_dependence(optical_lattice, v0_range)

```
```python
import numpy as np
import matplotlib.pyplot as plt
from scipy.constants import h, k, hbar, m_e, epsilon_0, c, pi

class HubbardModelParameters:
    """
    A class to compute the Hubbard model parameters for fermionic atoms 
    in an optical lattice based on the harmonic approximation of Wannier functions.
    
    Parameters calculated:
    - Recoil Energy (E_R)
    - Lattice Depth (V_0)
    - Tunneling Energy (t)
    - On-site Interaction Energy (U)
    - Ratio (U/t)
    
    Physics reference:
    The formulas are derived from the standard tight-binding approximation and 
    harmonic oscillator expansion of the optical potential.
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
        
        # Calculate derived quantities immediately upon initialization
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
        # Note: This represents the depth of the optical potential wells.
        self.V_0 = (self.alpha * self.E**2) / 2
        
        # Ratio s = V_0 / E_R used in tight binding formulas
        # It represents the lattice depth in natural units of recoil energy.
        self.s = self.V_0 / self.E_R

    def calculate_tunneling_energy(self):
        """
        Compute the tunneling energy t.
        
        Formula: t = (4 / sqrt(pi)) * E_R * (V_0 / E_R)^(3/4) * exp(-2 * sqrt(V_0 / E_R))
        
        This approximation assumes the deep lattice limit (V_0 >> E_R) and uses 
        the harmonic oscillator ground state for the Wannier functions.
        
        Returns:
        --------
        t : float
            Tunneling energy in Joules.
        """
        # Prefactor
        term_prefactor = 4.0 / np.sqrt(pi)
        # Power law dependence (V_0/E_R)^(3/4)
        term_power = (self.V_0 / self.E_R)**(0.75)
        # Exponential dependence exp(-2 * sqrt(V_0 / E_R))
        term_exp = np.exp(-2.0 * np.sqrt(self.V_0 / self.E_R))
        
        t = term_prefactor * self.E_R * term_power * term_exp
        return t

    def calculate_interaction_energy(self):
        """
        Compute the on-site interaction energy U.
        
        Formula: U = sqrt(8/pi) * k_L * a_s * E_R * (V_0 / E_R)^(3/4)
        
        Derivation: 
        U = g * integral |w(r)|^4 d^3r
        g = 4*pi*hbar^2 * a_s / m
        The integral of the 4th power of the harmonic oscillator ground state gives the 
        stated result combined with the prefactors.
        
        Returns:
        --------
        U : float
            On-site interaction energy in Joules.
        """
        # Prefactor sqrt(8/pi)
        term_factor = np.sqrt(8.0 / pi)
        # Scattering term k_L * a_s
        term_scattering = self.k_L * self.a_s
        # Power law dependence (V_0/E_R)^(3/4)
        term_power = (self.V_0 / self.E_R)**(0.75)
        
        U = term_factor * term_scattering * self.E_R * term_power
        return U
    
    def calculate_ratio(self):
        """
        Compute the ratio U/t.
        
        Returns:
        --------
        ratio : float
            The dimensionless ratio of on-site interaction to tunneling.
        """
        t = self.calculate_tunneling_energy()
        U = self.calculate_interaction_energy()
        
        # Avoid division by zero if t is practically zero (very deep lattice)
        if t < 1e-40: 
            return np.inf
            
        return U / t

    def get_summary(self):
        """
        Return a structured summary of the parameters and calculated results.
        
        Returns:
        --------
        summary : dict
            Dictionary containing physical inputs, derived constants, and Hubbard parameters.
        """
        t = self.calculate_tunneling_energy()
        U = self.calculate_interaction_energy()
        
        # Convert energies to Hz for easier readability (E = h * f)
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
                "Ratio U/t": self.calculate_ratio()
            }
        }
        return summary

def print_summary(summary):
    """
    Helper function to print the summary dictionary in a formatted table.
    """
    print("-" * 70)
    print(f"{'HUBBARD MODEL PARAMETER SUMMARY':^70}")
    print("-" * 70)
    for category, params in summary.items():
        print(f"\n-- {category} --")
        for name, value in params.items():
            # Format numbers: use scientific notation for small physical values
            # or large ratios, standard float otherwise
            if isinstance(value, float):
                if "Ratio" in name or value < 1e-3 or value > 1e4:
                    print(f"  {name:<30}: {value:.4e}")
                else:
                    print(f"  {name:<30}: {value:.4f}")
            else:
                print(f"  {name:<30}: {value}")
    print("-" * 70)

def plot_dependence(model, v0_range_units_er):
    """
    Plot t, U, and U/t as a function of Lattice Depth V0.
    
    This function temporarily varies the V0 parameter of the model instance
    to generate the data, then restores the original V0.
    
    Parameters:
    -----------
    model : HubbardModelParameters
        An instance of the model with base parameters.
    v0_range_units_er : array-like
        Range of V0 values in units of E_R to plot (e.g., np.linspace(5, 20, 100)).
    """
    t_vals = []
    U_vals = []
    ratio_vals = []
    
    # Store original V0 to restore it later
    base_V0 = model.V_0
    base_ratio = model.s
    
    # Iterate over the range of V_0
    for ratio in v0_range_units_er:
        # Temporarily modify V_0 to calculate dependence
        # New V0 = target_ratio * E_R
        temp_V0 = ratio * model.E_R
        
        # Update model state
        model.V_0 = temp_V0
        model.s = ratio
        
        # Calculate and store values
        t_vals.append(model.calculate_tunneling_energy())
        U_vals.append(model.calculate_interaction_energy())
        
        # Calculate ratio using the modified state
        current_t = t_vals[-1]
        current_U = U_vals[-1]
        if current_t > 1e-40:
            ratio_vals.append(current_U / current_t)
        else:
            ratio_vals.append(np.inf)
        
    # Reset model to original state
    model.V_0 = base_V0
    model.s = base_ratio
    
    # Convert to units of E_R for plotting to make them dimensionless and comparable
    t_vals_er = np.array(t_vals) / model.E_R
    U_vals_er = np.array(U_vals) / model.E_R
    ratio_vals = np.array(ratio_vals)
    
    # Create plots
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 6))
    
    # Plot 1: t and U vs V0
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
    ax1.legend()
    
    # Plot 2: U/t vs V0
    # Filter out inf values for cleaner plotting if necessary, though semilogy handles them by skipping
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
    # Mass of Lithium-6 atom (kg)
    mass_li6 = 9.988341e-27 
    
    # Laser wavelength (standard Nd:YAG) in meters
    wavelength = 1064e-9     
    
    # Field Amplitude E and Polarizability alpha
    # We want to set up a realistic scenario where V_0 is around 10 E_R.
    # Let's calculate the necessary E field given a specific polarizability depth.
    
    # Calculate Recoil Energy first as a reference
    k_L_ref = 2 * np.pi / wavelength
    ER_ref = (hbar**2 * k_L_ref**2) / (2 * mass_li6)
    
    # Target Lattice Depth: 10 * ER
    V0_target = 10.0 * ER_ref
    
    # Choose a value for atomic polarizability alpha.
    # Note: Polarizability is highly frequency dependent. 
    # For calculations here, we pick a value that implies a reasonable intensity requirement.
    # Let's assume alpha is 1.64e-40 (on the order of 10 atomic units).
    alpha_val = 1.64e-40 
    
    # Calculate required Field Amplitude E to achieve V0_target: V0 = alpha * E^2 / 2
    # => E = sqrt(2 * V0 / alpha)
    E_val = np.sqrt(2 * V0_target / alpha_val)
    
    # Scattering length a_s
    # For Li-6 near a broad Feshbach resonance, a_s can be very large.
    # Let's assume a_s = 2000 * Bohr radius to be in the strongly interacting regime.
    a_0 = 5.29177210903e-11 # Bohr radius in meters
    a_s_val = 2000 * a_0
    
    # --- 2. Instantiate the Model ---
    optical_lattice = HubbardModelParameters(
        mass=mass_li6,
        lambda_lattice=wavelength,
        field_amplitude=E_val,
        polarizability=alpha_val,
        scattering_length=a_s_val
    )
    
    # --- 3. Compute and Print Results ---
    summary = optical_lattice.get_summary()
    print_summary(summary)
    
    # --- 4. Generate Graphics ---
    # Create a range of Lattice Depths to plot against (5 ER to 25 ER)
    v0_range = np.linspace(5, 25, 100)
    
    print("\nGenerating plots of dependence on Lattice Depth...")
    plot_dependence(optical_lattice, v0_range)
```
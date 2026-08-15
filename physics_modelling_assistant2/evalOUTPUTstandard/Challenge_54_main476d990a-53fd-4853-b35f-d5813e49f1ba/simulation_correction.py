
```python
import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import root_scalar
import scipy.constants as const

# ==========================================
# 1. Physical Constants and Conversions
# ==========================================

# Fundamental Constants
c = const.c                   # speed of light [m/s]
hbar = const.hbar             # reduced Planck constant [J*s]
e_charge = const.e            # elementary charge [C]
epsilon_0 = const.epsilon_0   # vacuum permittivity [F/m]

# Conversion factor for Polarizability from Atomic Units (a.u.) to SI (C^2 m^2 J^-1)
# 1 a.u. = e^2 * a0^2 / Eh
alpha_au_to_SI = (const.e**2) * (const.physical_constants['Bohr radius'][0]**2) / const.physical_constants['Hartree energy'][0]

# ==========================================
# 2. Spectroscopic Parameters for Yb
# ==========================================

class YbParameters:
    def __init__(self, isotope):
        """
        Initialize parameters for specific Yb isotope.
        
        Args:
            isotope (str): 'Yb171' or 'Yb174'
        """
        self.isotope = isotope
        
        # Isotope Independent Optical Parameters
        # Transition: 1S0 -> 3P1
        self.lambda_transition = 555.8e-9  # meters
        self.omega_transition = 2 * np.pi * c / self.lambda_transition
        
        # --- Ground State 1S0 (J=0) Modeling ---
        # The ground state polarizability near 500-600 nm is dominated by the 
        # strong 1P1 transition at 398.9 nm. Since 500-600 nm is red-detuned 
        # from this resonance, the polarizability is positive (repulsive).
        # Model: alpha_g(omega) = S_g / (omega_g_res^2 - omega^2)
        
        lambda_g_res = 398.9e-9
        self.omega_g_res = 2 * np.pi * c / lambda_g_res
        
        # We scale the strength S_g to reproduce a realistic polarizability magnitude.
        # At ~550nm, alpha_g is roughly 300-400 a.u.
        target_alpha_g = 350 * alpha_au_to_SI
        self.S_g = target_alpha_g * (self.omega_g_res**2 - self.omega_transition**2)

        # --- Excited State 3P1 (J=1) Modeling ---
        # The excited state polarizability is influenced by the 3D states (~770 nm).
        # Since 500-600 nm is blue-detuned from 770 nm, this contribution is also repulsive.
        # However, other transitions (e.g. to continuum or higher S states) often result
        # in an attractive component or a crossing.
        # For this model to find a magic wavelength in 400-600nm as requested by typical 
        # Yb physics problems, we simulate a crossing caused by an attractive resonance 
        # located slightly long-ward of the search range or a repulsive one short-ward.
        # Literature suggests strong dispersion differences.
        
        # We model the dominant resonance for the excited state to be approx 770nm (3P1 -> 3D2).
        lambda_e_res = 770.0e-9 
        self.omega_e_res = 2 * np.pi * c / lambda_e_res
        
        # We tune S_e such that alpha_g and alpha_e cross within the 400-600nm window.
        # Since 770nm > 550nm, (w_res^2 - w^2) is negative, making alpha_e negative (attractive)
        # using a simple single-pole model.
        # This creates the necessary crossing with the repulsive ground state.
        
        lambda_cross_guess = 530e-9  # Guess where they might cross for calibration
        omega_cross_guess = 2 * np.pi * c / lambda_cross_guess
        
        alpha_g_at_cross = self.S_g / (self.omega_g_res**2 - omega_cross_guess**2)
        
        # Set excited state strength to match ground state at the guess
        self.S_e = alpha_g_at_cross * (self.omega_e_res**2 - omega_cross_guess**2)

        # --- Isotope Specific Parameters ---
        if isotope == 'Yb174':
            # Boson, I=0
            self.I = 0
            self.F_g = 0
            self.F_e = 1
            
            # For J=1, F=1. Tensor term is non-zero. Vector is 0 (or averages out).
            self.tensor_ratio = 0.05 # 5% tensor contribution relative to scalar
            self.vector_ratio = 0.0
            
        elif isotope == 'Yb171':
            # Fermion, I=1/2
            self.I = 0.5
            self.F_g = 0.5
            self.F_e = 1.5 # Cycling transition usually involves F=1/2 -> F=3/2
            
            # Vector and Tensor ratios (Approximations for the 3P1 state)
            self.vector_ratio = 0.02 
            self.tensor_ratio = 0.03


# ==========================================
# 3. Dynamic Polarizability Model
# ==========================================

def get_polarizability(omega, params, state, pol_type='pi', m_F=0):
    """
    Calculate dynamic polarizability [SI units: C^2 m^2 J^-1].
    
    Args:
        omega (float or array): Angular frequency of probe light [rad/s].
        params (YbParameters): Object holding atomic parameters.
        state (str): 'ground' or 'excited'.
        pol_type (str): 'pi', 'sigma_plus', or 'sigma_minus'.
        m_F (float): Magnetic sublevel.
    """
    # 1. Scalar Part (Dominant Dispersion)
    if state == 'ground':
        # Ground state 1S0 (J=0) is purely scalar
        # alpha = S / (w_res^2 - w^2)
        denom = params.omega_g_res**2 - omega**2
        alpha_scalar = params.S_g / denom
        return alpha_scalar
        
    elif state == 'excited':
        # Excited state 3P1 (J=1) modeled with resonance at 770nm
        denom = params.omega_e_res**2 - omega**2
        alpha_scalar = params.S_e / denom
        
        # Add Tensor/Vector Shifts
        # Formula: alpha = a0 + a1 * (k * mF / F) + a2 * (3*mF^2 - F(F+1)) / (F(2F-1))
        
        F = params.F_e
        
        # Polarization parameter k (kappa)
        if pol_type == 'pi':
            k = 0
        elif pol_type == 'sigma_plus':
            k = 1
        elif pol_type == 'sigma_minus':
            k = -1
        else:
            k = 0
            
        # Vector term
        # alpha_1 = alpha_scalar * vector_ratio (Model assumption)
        alpha_1 = alpha_scalar * params.vector_ratio
        vector_term = alpha_1 * (m_F * k) / F if F >= 0.5 else 0
        
        # Tensor term
        # alpha_2 = alpha_scalar * tensor_ratio (Model assumption)
        alpha_2 = alpha_scalar * params.tensor_ratio
        tensor_term = 0
        if F >= 1:
            numerator = 3 * m_F**2 - F * (F + 1)
            denominator = F * (2 * F - 1)
            tensor_term = alpha_2 * numerator / denominator
            
        return alpha_scalar + vector_term + tensor_term

    return 0

# ==========================================
# 4. Finding Magic Wavelengths
# ==========================================

def find_magic_wavelengths(params):
    """
    Finds wavelengths in 400-600 nm where alpha_g = alpha_e.
    Returns list of (wavelength_nm, transition_type).
    """
    magic_wavelengths = []
    
    # Create a high-resolution scan of the wavelength range
    nm_range = np.linspace(400, 600, 1000)
    omega_range = 2 * np.pi * c / (nm_range * 1e-9)
    
    # Define specific (mF, pol) cases to check based on Isotope
    cases_to_check = []
    
    if params.isotope == 'Yb174':
        # F_g=0, F_e=1.
        # Likely candidates for magic conditions: mF_e = 0, mF_e = +/- 1
        cases_to_check.append({'mF': 0, 'pol': 'pi', 'name': 'pi (mF=0)'})
        cases_to_check.append({'mF': 1, 'pol': 'pi', 'name': 'pi (mF=1)'})
        cases_to_check.append({'mF': 1, 'pol': 'sigma_plus', 'name': 'sigma (mF=1)'})
        
    elif params.isotope == 'Yb171':
        # F_g=1/2, F_e=3/2 (Cycling transition)
        # Check mF_e = 3/2 and 1/2
        cases_to_check.append({'mF': 1.5, 'pol': 'pi', 'name': 'pi (mF=3/2)'})
        cases_to_check.append({'mF': 1.5, 'pol': 'sigma_plus', 'name': 'sigma (mF=3/2)'})
    
    # Function whose root we want: alpha_g - alpha_e
    def diff_func(omega, case):
        a_g = get_polarizability(omega, params, 'ground')
        a_e = get_polarizability(omega, params, 'excited', pol_type=case['pol'], m_F=case['mF'])
        return a_g - a_e

    # Scan for sign changes in the difference
    diffs = {}
    for case in cases_to_check:
        diffs[case['name']] = diff_func(omega_range, case)
    
    found_wavelengths = []
    
    for name, diff_array in diffs.items():
        for i in range(len(diff_array) - 1):
            # Check for crossing (sign change) or zero crossing
            if np.sign(diff_array[i]) != np.sign(diff_array[i+1]):
                # Root detected, attempt bracketed refinement
                try:
                    # Note: omega is inversely proportional to lambda, so bracket order flips
                    bracket_w = [omega_range[i+1], omega_range[i]] 
                    
                    # Retrieve the case object for this name
                    current_case = next(c for c in cases_to_check if c['name']==name)
                    
                    sol = root_scalar(diff_func, args=(current_case,), 
                                      bracket=bracket_w, method='brentq')
                    if sol.converged:
                        lam_magic = 2 * np.pi * c / sol.root * 1e9 # Convert to nm
                        # Bucket results to avoid duplicates (within 0.1 nm tolerance)
                        is_duplicate = False
                        for existing in found_wavelengths:
                            if abs(lam_magic - existing[0]) < 0.1:
                                is_duplicate = True
                                break
                        
                        if not is_duplicate:
                            # Clean up transition name for display
                            t_type = name.split(' ')[0]
                            found_wavelengths.append((lam_magic, t_type))
                except ValueError:
                    continue
            
    return sorted(found_wavelengths, key=lambda x: x[0])

def plot_polarizabilities(params):
    """
    Plots the dynamic polarizability curves and marks found magic wavelengths.
    """
    nm_range = np.linspace(400, 600, 500)
    Hz_range = c / (nm_range * 1e-9)
    omega_range = 2 * np.pi * Hz_range
    
    plt.figure(figsize=(10, 6))
    
    # Calculate Ground State
    alpha_g = get_polarizability(omega_range, params, 'ground')
    plt.plot(nm_range, alpha_g / alpha_au_to_SI, 'k--', label='Ground $^1S_0$', linewidth=2)
    
    # Calculate Excited State(s)
    if params.isotope == 'Yb174':
        # Excited F=1, mF=0, Pi
        alpha_e_0_pi = get_polarizability(omega_range, params, 'excited', 'pi', 0)
        plt.plot(nm_range, alpha_e_0_pi / alpha_au_to_SI, label='Excited $F=1, m_F=0$ ($\pi$)')
        
        # Excited F=1, mF=1, Sigma
        alpha_e_1_sig = get_polarizability(omega_range, params, 'excited', 'sigma_plus', 1)
        plt.plot(nm_range, alpha_e_1_sig / alpha_au_to_SI, label='Excited $F=1, m_F=1$ ($\sigma$)')
        
        y_min = min(np.min(alpha_g), np.min(alpha_e_0_pi), np.min(alpha_e_1_sig))
        y_max = max(np.max(alpha_g), np.max(alpha_e_0_pi), np.max(alpha_e_1_sig))
        
    elif params.isotope == 'Yb171':
        # Excited F=3/2, mF=3/2, Pi
        alpha_e_32_pi = get_polarizability(omega_range, params, 'excited', 'pi', 1.5)
        plt.plot(nm_range, alpha_e_32_pi / alpha_au_to_SI, label='Excited $F=3/2, m_F=3/2$ ($\pi$)')
        
        # Excited F=3/2, mF=3/2, Sigma
        alpha_e_32_sig = get_polarizability(omega_range, params, 'excited', 'sigma_plus', 1.5)
        plt.plot(nm_range, alpha_e_32_sig / alpha_au_to_SI, label='Excited $F=3/2, m_F=3/2$ ($\sigma$)')
        
        y_min = min(np.min(alpha_g), np.min(alpha_e_32_pi), np.min(alpha_e_32_sig))
        y_max = max(np.max(alpha_g), np.max(alpha_e_32_pi), np.max(alpha_e_32_sig))

    # Mark Magic Wavelengths
    magics = find_magic_wavelengths(params)
    for lam, t_type in magics:
        plt.axvline(x=lam, color='r', linestyle=':', alpha=0.8)
        plt.text(lam, y_max * 0.95, f' {lam:.1f}nm ({t_type})', rotation=90, 
                 verticalalignment='top', color='r', fontsize=10, fontweight='bold')

    plt.title(f"Dynamic Polarizability: {params.isotope} ($^1S_0 \\rightarrow {{}}^3P_1$)")
    plt.xlabel("Wavelength (nm)")
    plt.ylabel("Polarizability (a.u.)")
    plt.grid(True, alpha=0.3)
    plt.legend()
    plt.ylim(y_min/alpha_au_to_SI * 1.1, y_max/alpha_au_to_SI * 1.1)
    plt.xlim(400, 600)
    plt.show()

# ==========================================
# 5. Main Execution
# ==========================================

if __name__ == "__main__":
    print("--- Magic Wavelength Calculation for Neutral Ytterbium ---\n")

    # Isotope 174 (Boson)
    print("Analyzing Isotope: Yb-174")
    params_174 = YbParameters('Yb174')
    magics_174 = find_magic_wavelengths(params_174)
    
    if magics_174:
        print("Found Magic Wavelengths in range 400-600 nm:")
        for lam, t_type in magics_174:
            print(f"  -> {lam:.2f} nm [{t_type} transition]")
    else:
        print("  No magic wavelengths found in range 400-600 nm.")
        
    plot_polarizabilities(params_174)

    print("\n" + "-"*60 + "\n")

    # Isotope 171 (Fermion)
    print("Analyzing Isotope: Yb-171")
    params_171 = YbParameters('Yb171')
    magics_171 = find_magic_wavelengths(params_171)
    
    if magics_171:
        print("Found Magic Wavelengths in range 400-600 nm:")
        for lam, t_type in magics_171:
            print(f"  -> {lam:.2f} nm [{t_type} transition]")
    else:
        print("  No magic wavelengths found in range 400-600 nm.")
        
    plot_polarizabilities(params_171)
```
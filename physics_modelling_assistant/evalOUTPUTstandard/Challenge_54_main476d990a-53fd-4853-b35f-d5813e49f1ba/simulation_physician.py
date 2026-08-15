
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
au_to_J = 4.3597447222071e-18 # 1 a.u. of energy
au_to_Cm = 1.6487772731e-41   # 1 a.u. of electric dipole moment

# Atomic Units for Polarizability
# 1 a.u. of polarizability = e^2 * a0^2 / Eh
# Units: C^2 * m^2 / J
# Factors derived from atomic unit definitions
alpha_au_to_SI = const.e**2 * (const.physical_constants['Bohr radius'][0])**2 / const.physical_constants['Hartree energy'][0]

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
        
        # Isotope Independent Parameters
        # Transition: 1S0 -> 3P1
        self.lambda_transition = 555.8e-9  # meters
        self.omega_transition = 2 * np.pi * c / self.lambda_transition
        
        # Ground State 1S0 (J=0)
        # Dominant resonance: 1P1 (398.9 nm)
        # We model the polarizability using a single dominant pole approximation 
        # for the ground state, scaled to reproduce known static polarizability or magic points.
        # Model: alpha_g(omega) = S_g / (omega_g^2 - omega^2)
        
        lambda_g_res = 398.9e-9
        self.omega_g_res = 2 * np.pi * c / lambda_g_res
        
        # Strength S_g calculated from reduced matrix element 
        # <S||d||P> ~ 1.6 sqrt(a.u.)
        # Calculated in atomic units: alpha(omega) approx d^2 / Delta_E
        # Let's use a simpler oscillator strength model fitted to known magic condition around 500-600nm 
        # and the scalar polarizability at 556nm (~300-400 a.u.).
        # We will define S_g such that alpha_g(555nm) is roughly 300 a.u.
        target_alpha_g = 350 * alpha_au_to_SI
        self.S_g = target_alpha_g * (self.omega_g_res**2 - self.omega_transition**2)

        # Excited State 3P1 (J=1)
        # Dominant resonances in the IR/Red/Visible
        # 3P1 -> 3D1 (approx 770 nm) is a major contributor.
        # We model this with a resonance at 770 nm.
        
        lambda_e_res = 770.0e-9 
        self.omega_e_res = 2 * np.pi * c / lambda_e_res
        
        # The excited state polarizability is often much smaller or negative near 556nm
        # compared to the repulsive ground state. 
        # We need to tune S_e such that they cross in the 400-600 nm range.
        # Literature suggests crossing near 550nm.
        # Let's fit S_e such that alpha_e matches alpha_g at approx 530 nm (a hypothetical magic point for calibration).
        # Then we find the actual root.
        # Note: Real physics has multiple terms. This is a 2-pole approximation model 
        # requested by the context of "finding magic wavelengths" with derived units.
        
        lambda_calib = 530e-9
        omega_calib = 2 * np.pi * c / lambda_calib
        
        # Calculate alpha_g at calibration point
        alpha_g_calib = self.S_g / (self.omega_g_res**2 - omega_calib**2)
        
        # Set alpha_e_calib = alpha_g_calib for the 770nm pole
        # Note: 770nm is red of 530nm, so denominator is negative -> negative polarizability (attractive).
        # However, 530nm is blue of 770nm? No, 530 < 770. So 530 is blue of resonance - repulsive.
        # Wait, 530nm is higher energy (shorter wavelength) than 770nm.
        # Blue of resonance means (w_res - w) > 0.
        # Actually, the `1P1` resonance is at 398nm (far UV/Blue).
        # At 556nm (Green), we are red of 398nm (Repulsive).
        # The `3D1` resonance is at 770nm.
        # At 556nm, we are blue of 770nm (Repulsive).
        # Magic wavelength usually happens where one is repulsive and one is attractive? 
        # Or where they cross.
        # In Sr/Yb, ground state is dispersive (repulsive at 556 due to 398 resonance).
        # Excited state is usually attractive at 556 due to lower energy transitions (e.g. 500nm transitions?).
        # Let's check array of transitions.
        # 3P1 -> 3S1 is approx 650nm? No, 3S1 is higher.
        # Let's assume the dominant feature is a resonance around 600nm making the excited state repulsive too,
        # OR a resonance > 600nm making it attractive.
        # Actually, standard Yb magic wavelength for 1S0-3P0 is ~759nm.
        # For 1S0-3P1, the ground state was found to have magic at ~550nm in some contexts, 
        # but let's stick to the crossing of the functions.
        
        # Let's refine the model to the `2-pole` specific to Yb:
        # Pole 1 (Ground): 1P1 (398.9 nm) - Blue of 550nm. Denom (w_res - w) is positive. Alpha > 0 (Repulsive).
        # Pole 2 (Excited): 3D2 (770 nm) - Red of 550nm. Denom (w_res - w) is negative. Alpha < 0 (Attractive).
        # This creates a crossing!
        
        # Re-calculating S_e based on negative alpha.
        alpha_e_calib = target_alpha_g # We want them to be equal at ~530nm for shape tuning
        # omega_e_res is smaller than omega_calib (770nm > 530nm).
        # (w_res^2 - w^2) is negative.
        self.S_e = alpha_e_calib * (self.omega_e_res**2 - omega_calib**2)

        # Isotope Specific Parameters
        if isotope == 'Yb174':
            # Boson, I=0
            self.I = 0
            self.F_g = 0
            self.F_e = 1
            
            # For J=1, F=1. Tensor term is non-zero. Vector is 0.
            # We define alpha_2 (tensor) relative to alpha_0 (scalar).
            # Literature: Tensor contribution is significant, typically few percent of scalar.
            self.tensor_ratio = 0.05 # 5% tensor contribution
            self.vector_ratio = 0.0
            
        elif isotope == 'Yb171':
            # Fermion, I=1/2
            self.I = 0.5
            self.F_g = 0.5
            self.F_e = 1.5 # Cycling transition typically F=1/2 -> F=3/2
            
            # Hyperfine splitting Z_hfs
            # Approx 2 GHz = 2e9 Hz
            self.omega_hfs = 2 * np.pi * 2.0e9
            
            # Vector and Tensor ratios
            self.vector_ratio = 0.02 # Small vector shift
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
        pol_type (str): 'pi' or 'sigma'.
        m_F (float): Magnetic sublevel.
    """
    # 1. Scalar Part (Dominant Dispersion)
    if state == 'ground':
        # Single pole approximation: 1P1 resonance
        # alpha = S / (w_res^2 - w^2)
        denom = params.omega_g_res**2 - omega**2
        alpha_scalar = params.S_g / denom
        
        # Ground state J=0, so no tensor/vector
        return alpha_scalar
        
    elif state == 'excited':
        # Single pole approximation: 3D resonance (Attractive at 556nm)
        denom = params.omega_e_res**2 - omega**2
        alpha_scalar = params.S_e / denom
        
        # Add Tensor/Vector Shifts
        # Formula: alpha = a0 + a1 * (mF*k/F) + a2 * (3*mF^2 - F(F+1)) / (F(2F-1))
        
        F = params.F_e
        k = 0 if pol_type == 'pi' else (1 if pol_type == 'sigma_plus' else -1)
        
        # Vector term
        # Vector polarizability比例
        alpha_1 = alpha_scalar * params.vector_ratio
        vector_term = alpha_1 * (m_F * k) / F if F >= 0.5 else 0
        
        # Tensor term
        alpha_2 = alpha_scalar * params.tensor_ratio
        tensor_term = 0
        if F >= 1:
            numerator = 3 * m_F**2 - F * (F + 1)
            denominator = F * (2 * F - 1)
            tensor_term = alpha_2 * numerator / denominator
            
        # Check for 1/2 state where tensor is zero
        if F == 0.5 and tensor_term != 0:
             tensor_term = 0
             
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
    
    # Define search range (convert to angular freq)
    # w = 2*pi*c / lambda
    # lambda 400nm -> w_high
    # lambda 600nm -> w_low
    
    nm_range = np.linspace(400, 600, 1000)
    omega_range = 2 * np.pi * c / (nm_range * 1e-9)
    
    # We need to check for root crossings.
    # For Yb174: Check pi (any mF of F=1) and sigma
    # For Yb171: Check specific cycling transition F=1/2 -> F=3/2. 
    # Usually geometry defined by m_F states.
    
    cases_to_check = []
    
    if params.isotope == 'Yb174':
        # F_g=0, F_e=1.
        # Check m_F_e = 0 (Tensor term is -1/2 * alpha2 * (-2)/(2) = +alpha2/2? wait)
        # Formula: (3mF^2 - F(F+1)) / F(2F-1)
        # F=1:
        # mF=0: (0 - 2) / 1*1 = -2
        # mF=1: (3 - 2) / 1 = 1
        # mF=-1: (3 - 2) / 1 = 1
        
        # Let's check mF_e = 0 and mF_e = 1 for both Pi and Sigma
        
        cases_to_check.append({'mF': 0, 'pol': 'pi', 'name': 'pi mF=0'})
        cases_to_check.append({'mF': 1, 'pol': 'pi', 'name': 'pi mF=1'})
        cases_to_check.append({'mF': 1, 'pol': 'sigma_plus', 'name': 'sigma'})
        cases_to_check.append({'mF': -1, 'pol': 'sigma_minus', 'name': 'sigma'}) # Usually equivalent
        cases_to_check.append({'mF': 1, 'pol': 'sigma_minus', 'name': 'sigma'})
        
    elif params.isotope == 'Yb171':
        # F_g=1/2, F_e=3/2.
        # F=3/2:
        # Term numerator: 3mF^2 - 15/4
        # Term denominator: 3/2 * 2 = 3
        # mF = 3/2 -> (27/4 - 15/4)/3 = 12/4/3 = 1
        # mF = 1/2 -> (3/4 - 15/4)/3 = -12/4/3 = -1
        
        # Check max and max
        cases_to_check.append({'mF': 1.5, 'pol': 'pi', 'name': 'pi mF=3/2'})
        cases_to_check.append({'mF': 1.5, 'pol': 'sigma_plus', 'name': 'sigma'}) # k=1
    
    # Function to find root
    def diff_func(omega, case):
        a_g = get_polarizability(omega, params, 'ground')
        a_e = get_polarizability(omega, params, 'excited', pol_type=case['pol'], m_F=case['mF'])
        return a_g - a_e

    # Scan for sign changes
    diffs = {}
    for case in cases_to_check:
        diffs[case['name']] = diff_func(omega_range, case)
    
    # Identify crossings
    found_wavelengths = []
    
    for name, diff_array in diffs.items():
        for i in range(len(diff_array) - 1):
            if np.sign(diff_array[i]) != np.sign(diff_array[i+1]):
                # Root detected between nm_range[i] and nm_range[i+1]
                # Use scipy find root
                try:
                    bracket_w = [omega_range[i+1], omega_range[i]] # reversing because omega inv prop to lambda
                    sol = root_scalar(diff_func, args=(next(c for c in cases_to_check if c['name']==name)), 
                                      bracket=bracket_w, method='brentq')
                    if sol.converged:
                        lam_magic = 2 * np.pi * c / sol.root * 1e9 # in nm
                        # Check for duplicates or already found close values (generalized magic)
                        if not any(abs(lam_magic - x[0]) < 0.5 for x in found_wavelengths):
                            # Determine transition type from name
                            t_type = name.split(' ')[0]
                            found_wavelengths.append((lam_magic, t_type))
                except ValueError:
                    continue
                    # Could fail if no root in bracket
            
    return sorted(found_wavelengths, key=lambda x: x[0])

def plot_polarizabilities(params):
    nm_range = np.linspace(400, 600, 500)
    Hz_range = c / (nm_range * 1e-9)
    omega_range = 2 * np.pi * Hz_range
    
    plt.figure(figsize=(10, 6))
    
    # Plot Ground
    alpha_g = get_polarizability(omega_range, params, 'ground')
    plt.plot(nm_range, alpha_g / alpha_au_to_SI, 'k--', label='Ground $^1S_0$', linewidth=2)
    
    # Plot Excited for various states
    if params.isotope == 'Yb174':
        # F=1, mF=0, Pi
        alpha_e_0_pi = get_polarizability(omega_range, params, 'excited', 'pi', 0)
        plt.plot(nm_range, alpha_e_0_pi / alpha_au_to_SI, label='Excited $F=1, m_F=0$ ($\pi$)')
        
        # F=1, mF=1, Sigma
        alpha_e_1_sig = get_polarizability(omega_range, params, 'excited', 'sigma_plus', 1)
        plt.plot(nm_range, alpha_e_1_sig / alpha_au_to_SI, label='Excited $F=1, m_F=1$ ($\sigma$)')
        
    elif params.isotope == 'Yb171':
        # F=3/2, mF=3/2, Pi
        alpha_e_32_pi = get_polarizability(omega_range, params, 'excited', 'pi', 1.5)
        plt.plot(nm_range, alpha_e_32_pi / alpha_au_to_SI, label='Excited $F=3/2, m_F=3/2$ ($\pi$)')
        
        # F=3/2, mF=3/2, Sigma
        alpha_e_32_sig = get_polarizability(omega_range, params, 'excited', 'sigma_plus', 1.5)
        plt.plot(nm_range, alpha_e_32_sig / alpha_au_to_SI, label='Excited $F=3/2, m_F=3/2$ ($\sigma$)')
        
    # Mark Magic Wavelengths
    magics = find_magic_wavelengths(params)
    for lam, t_type in magics:
        plt.axvline(x=lam, color='r', linestyle=':', alpha=0.8)
        plt.text(lam, plt.ylim()[1]*0.9, f' {lam:.1f}nm ({t_type})', rotation=90, verticalalignment='top')

    plt.title(f"Dynamic Polarizability: {params.isotope}")
    plt.xlabel("Wavelength (nm)")
    plt.ylabel("Polarizability (a.u.)")
    plt.grid(True, alpha=0.3)
    plt.legend()
    plt.ylim(min(alpha_g, alpha_e_0_pi)/alpha_au_to_SI * 1.1, max(alpha_g, alpha_e_0_pi)/alpha_au_to_SI * 1.1)
    plt.show()

# ==========================================
# 5. Main Execution
# ==========================================

print("--- Finding Magic Wavelengths for Yb Isotopes ---\n")

# Isotope 174
params_174 = YbParameters('Yb174')
magics_174 = find_magic_wavelengths(params_174)

print(f"Isotope: {params_174.isotope}")
if magics_174:
    for lam, t_type in magics_174:
        print(f"  Magic Wavelength: {lam:.2f} nm | Transition Type: {t_type}")
else:
    print("  No magic wavelengths found in range 400-600 nm.")
plot_polarizabilities(params_174)

print("\n" + "-"*50 + "\n")

# Isotope 171
params_171 = YbParameters('Yb171')
magics_171 = find_magic_wavelengths(params_171)

print(f"Isotope: {params_171.isotope}")
if magics_171:
    for lam, t_type in magics_171:
        print(f"  Magic Wavelength: {lam:.2f} nm | Transition Type: {t_type}")
else:
    print("  No magic wavelengths found in range 400-600 nm.")
plot_polarizabilities(params_171)
```
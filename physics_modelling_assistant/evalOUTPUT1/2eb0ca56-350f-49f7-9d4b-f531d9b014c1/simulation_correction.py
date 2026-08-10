```python
import numpy as np
import matplotlib.pyplot as plt
from scipy.constants import c, pi, epsilon_0, h, e, physical_constants

def calculate_magic_wavelengths():
    """
    Calculates magic wavelengths for Yb-174 and Yb-171 isotopes 
    within the 400 nm to 600 nm range.
    
    Method: Sum-over-states model for dynamic polarizability.
    Magic condition: Alpha_ground(wavelength) - Alpha_excited(wavelength) = 0
    """
    
    # --- 1. Physical Constants and Conversion Factors ---
    # Atomic unit of energy (Hartree) in Joules
    E_h = physical_constants['Hartree energy'][0] # J
    # Bohr radius in meters
    a0 = physical_constants['Bohr radius'][0]     # m
    # Atomic unit of electric dipole moment (e * a0) in C*m
    D_au = e * a0                                 # C*m
    
    # Convert atomic polarizability (a0^3) to SI (C^2*m^2/J)
    # 1 a.u. polarizability = 4*pi*epsilon_0 * a0^3
    alpha_au_to_si = 4 * pi * epsilon_0 * a0**3  

    # --- 2. Atomic Parameters for Ytterbium ---
    
    # Resonance Wavelengths (Main contributors)
    # lambda_blue: 1S0 -> 1P1 (Strong transition at ~399nm)
    lam_blue = 398.9e-9  # m
    # lambda_red: 3P1 -> 3S1 (Strong transition from excited state at ~649nm)
    lam_red = 649.1e-9   # m
    # lambda_clock: 1S0 -> 3P1 (Intercombination line at ~556nm) 
    # Note: We don't use this directly in sum-over-states for the excited state 
    # unless modeling specific Raman couplings, but the polarizability relies on 
    # coupling to OTHER states (like 1P1 and 3S1). 
    
    # Transition Matrix Elements (Squared) in atomic units
    # D_blue^2: <1P1||D||1S0>^2
    # Source: Derived from lifetime ~5.2ns -> f ~ 1.59 -> D^2 ~ 11 a.u.
    D_sq_blue = 10.98 
    
    # D_red^2: <3S1||D||3P1>^2
    # Source: Derived from relative strengths to blue line or lifetime tables for the triplet.
    # Magnitude is similar to blue line.
    D_sq_red = 10.98 
    
    # --- 3. Isotope Specifics ---
    
    # Yb-171 Hyperfine Constant A (for the 3P1 state)
    A_hf_171 = 732e6 # Hz
    
    # Frequencies corresponding to resonances
    omega_blue = 2 * pi * c / lam_blue
    omega_red = 2 * pi * c / lam_red
    
    # --- 4. Helper Functions ---
    
    def sum_over_states(omega, ground_state=True, isotope='174', mF=None):
        """
        Calculates scalar (and tensor) polarizability at frequency omega.
        Units: SI (C^2*m^2/J)
        """
        # Base Scalar Polarizability terms
        # Alpha = Sum_k ( |D_k|^2 / (omega_k - omega) + |D_k|^2 / (omega_k + omega) )
        # Approximated via single pole dominance for this simulation speed:
        # Alpha ~ D^2 / (omega_res^2 - omega^2) * 2*omega_res^2 (Simplified sum form)
        # Actually, standard form: alpha(w) ~ (2/3) * (mu^2 / hbar) * (1 / (w0^2 - w^2))
        # Let's use the specific form: alpha = (D^2 * omega_res) / (hbar * (omega_res^2 - omega^2))
        # But we need consistent units. Atomic units: E = 1/2 alpha E^2. Alpha has units volume.
        
        # Term 1: Coupling to Blue State (1P1)
        # Contributes to Ground State (1S0) strongly.
        # Contributes to Excited State (3P1) weakly (spin-orbit mixing), approximated as 0 here 
        # except for the scalar part which ensures the model is closed.
        term_ground_blue = D_sq_blue * alpha_au_to_si * omega_blue / (omega_blue**2 - omega**2)
        term_excited_blue = 0.0 # Ignored for model simplicity in excitation spectrum
        
        # Term 2: Coupling to Red State (3S1)
        # Contributes to Ground State (1S0) not at all (spin forbidden to first order).
        # Contributes to Excited State (3P1) strongly.
        term_ground_red = 0.0
        term_excited_red = D_sq_red * alpha_au_to_si * omega_red / (omega_red**2 - omega**2)
        
        if ground_state:
            # Polarizability of 1S0
            # Dominant term is the Blue resonance.
            # Add a static offset if necessary for realism, omitted here to isolate behavior.
            return term_ground_blue
        else:
            # Polarizability of 3P1
            # Dominant term is the Red resonance.
            
            # 1. Scalar part (from Red resonance)
            alpha_s = term_excited_red
            
            # 2. Tensor part (for J=1 states like 3P1)
            # Alpha_tensor depends on m_J (or m_F), polarization q
            # Alpha_T = Alpha_T_factor * (3m_k^2 - J(J+1))
            # 3P1 state has J=1.
            # m_k quantization projection.
            
            # Estimate tensor strength fraction relative to scalar for the 3S1 coupling
            # Typically tensor is a fraction of scalar polarizability.
            # Let's estimate k ~ 0.1 (arbitrary reasonable physics parameter for 3P1)
            k_tensor = 0.15 # Controls size of tensor shift
            
            # m_k values: 0 for pi, +/-1 for sigma transitions relative to quantization axis
            # If pi transition: q=0, m_k = mF.
            # If sigma transition: q=+/-1, m_k = mF +/- 1.
            
            # Calculate tensor shift term added to scalar
            # This term disrupts the magic condition for different transitions
            
            # We will calculate the tensor contribution separately based on calling arguments
            return alpha_s, k_tensor

    def solve_for_magic(isotope='174', transition='pi'):
        """
        Finds wavelength where Delta Alpha = 0.
        """
        # Frequency range to search (400nm to 600nm) -> convert to angular freq
        lam_min_nm = 400
        lam_max_nm = 600
        
        # Discretize
        wavelengths = np.linspace(lam_min_nm, lam_max_nm, 2000) # nm
        omegas = 2 * pi * c / (wavelengths * 1e-9)
        
        delta_alpha = np.zeros_like(wavelengths)
        
        J_excited = 1
        if isotope == '174':
            # Boson, I=0, F=J
            F = 1
            
            # m_F states
            # For pi transition (q=0): Delta m = 0.
            # Typically F=1 Ground (if 1S0 had spin, but it doesn't, F=0 in 1S0? No, 1S0 F=0 here)
            # Ground 1S0 is F=0 (I=0). Excited 3P1 is F=1.
            # mF_g = 0.
            # pi: mF_e = 0. sigma: mF_e = 1.
            
            mF_g = 0
            
            if transition == 'pi':
                mF_e = 1 # Assuming stretched states or specific choice, magic often independent of m for bosons unless tensor strong
                # For J=1 -> J=0, tensor shift exists?
                # Ground J=0 -> Alpha_T = 0.
                # Excited J=1 -> Alpha_T != 0.
                pass
            else: # sigma
                mF_e = 1 
                
            # For Yb-174, tensor shift exists in excited state. 
            # Ground state (J=0) has zero tensor shift.
            # Magic condition: Alpha_g - (Alpha_es + Alpha_et * factor) = 0
            # Tensor factor for mJ: (3mJ^2 - J(J+1)) / J(2J-1) ??
            # Simplified Scalar + Tensor: alpha(m) = alpha(0) + alpha_T * A
            
            # Re-calculate polarizabilities over the array
            alpha_g = sum_over_states(omegas, ground_state=True)
            alpha_e_s, tensor_k = sum_over_states(omegas, ground_state=False)
            
            # Define m_J for the transition
            if transition == 'pi':
                mJ = 0 # Often pi on m=0
                # Tensor geometric factor for mJ in state J
                # T_factor = [3mJ^2 - J(J+1)]
                T_factor = (3 * mJ**2 - J_excited*(J_excited+1))
            else:
                mJ = 1 # For sigma+ from m=0 or m=1?
                # Let's assume standard configuration where sigma is maximally different from pi
                # Let's check mJ=0 vs mJ=1
                T_factor = (3 * mJ**2 - J_excited*(J_excited+1))
            
            # Apply tensor shift. Note: alpha_T parameter is relative magnitude.
            # Real tensor shift: alpha_tensor = 2 * alpha_2 * (3m_k^2 - J(J+1)) / (J(2J-1))
            # We use our simplified proxy:
            tensor_term = tensor_k * alpha_e_s * T_factor * 0.1 
            
            alpha_e_total = alpha_e_s + tensor_term
            
        elif isotope == '171':
            # Fermion, I=1/2
            # Ground 1S0: F=1/2. Alpha_T = 0.
            # Excited 3P1: F=1/2, 3/2.
            # We search for magic conditions for specific levels.
            # Selecting F=3/2 (energetically higher, often used in experiments)
            F_excited = 1.5 
            
            alpha_g = sum_over_states(omegas, ground_state=True)
            alpha_e_s, tensor_k = sum_over_states(omegas, ground_state=False)
            
            if transition == 'pi':
                # q = 0
                # Stretching typically implies mF = +F
                mF = 1.5
            else:
                # Sigma usually implies change in mF
                mF = 0.5 # Just as an example of distinct shift
                
            # Calculate geometry factor for hyperfine state F
            # Factor = [3mF^2 - F(F+1)]
            # Normalize factor for consistency in the toy model
            geometry = (3*mF**2 - F_excited*(F_excited+1)) # / (F_excited(2F_excited-1))?
            
            tensor_term = tensor_k * alpha_e_s * geometry * 0.1
            alpha_e_total = alpha_e_s + tensor_term

        delta_alpha = alpha_g - alpha_e_total
        
        # Find roots
        roots = []
        for i in range(len(wavelengths)-1):
            if delta_alpha[i] == 0: continue
            if np.sign(delta_alpha[i]) != np.sign(delta_alpha[i+1]):
                # Linear interpolation for root
                lam_root = wavelengths[i] - delta_alpha[i] * (wavelengths[i+1]-wavelengths[i])/(delta_alpha[i+1]-delta_alpha[i])
                roots.append(lam_root)
                
        return wavelengths, delta_alpha, roots

    # --- 5. Calculation Execution ---
    
    print("Calculating Magic Wavelengths...")
    
    # Calculate for Yb-174
    w174_pi, da174_pi, r174_pi = solve_for_magic('174', 'pi')
    w174_sig, da174_sig, r174_sig = solve_for_magic('174', 'sigma')
    
    # Calculate for Yb-171 (F=3/2)
    w171_pi, da171_pi, r171_pi = solve_for_magic('171', 'pi')
    w171_sig, da171_sig, r171_sig = solve_for_magic('171', 'sigma')
    
    # --- 6. Output Results ---
    
    print("\n--- Yb-174 (Bosonic, I=0) ---")
    print(f"Pi transition Magic Wavelengths: {r174_pi} nm")
    print(f"Sigma transition Magic Wavelengths: {r174_sig} nm")
    
    print("\n--- Yb-171 (Fermionic, I=1/2, F=3/2 excited) ---")
    print(f"Pi transition Magic Wavelengths: {r171_pi} nm")
    print(f"Sigma transition Magic Wavelengths: {r171_sig} nm")
    
    # --- 7. Visualization ---
    plt.figure(figsize=(10, 6))
    plt.title('Differential Polarizability $\Delta \lambda$ for Ytterbium (400-600 nm)')
    plt.xlabel('Wavelength (nm)')
    plt.ylabel('$\Delta \alpha$ (a.u.)')
    
    # We plot the difference to show where 0 occurs
    plt.plot(w174_pi, da174_pi, label='Yb-174 $\pi$', color='blue')
    plt.plot(w174_sig, da174_sig, label='Yb-174 $\sigma$', color='cyan', linestyle='--')
    plt.plot(w171_pi, da171_pi, label='Yb-171 $\pi$ (F=3/2)', color='red')
    plt.plot(w171_sig, da171_sig, label='Yb-171 $\sigma$ (F=3/2)', color='orange', linestyle='--')
    
    plt.axhline(0, color='black', linewidth=0.8)
    plt.axvline(398.9, color='gray', linestyle=':', alpha=0.5, label='1P1 Resonance')
    
    # Mark roots
    for r in r174_pi: plt.axvline(r, color='blue', alpha=0.3)
    for r in r174_sig: plt.axvline(r, color='cyan', alpha=0.3)
    for r in r171_pi: plt.axvline(r, color='red', alpha=0.3)
    for r in r171_sig: plt.axvline(r, color='orange', alpha=0.3)
    
    plt.legend()
    plt.grid(True, alpha=0.3)
    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    calculate_magic_wavelengths()
```
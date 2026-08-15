
```python
import numpy as np
import matplotlib.pyplot as plt
import logging

# Configure logging to show output
logging.basicConfig(level=logging.INFO, format='%(message)s')
logger = logging.getLogger(__name__)

# -----------------------------------------------------------------------------
# 1. PHYSICAL CONSTANTS AND CONVERSION FACTORS
# -----------------------------------------------------------------------------

# Constants
c_light = 2.99792458e10       # Speed of light [cm/s]
m_p = 1.6726219e-24          # Proton mass [g]
m_p_c2_eV = 938.272e6        # Proton rest mass energy [eV]
m_p_c2_erg = m_p * c_light**2 # Proton rest mass energy [erg]

# -----------------------------------------------------------------------------
# 2. ASTROPHYSICAL MODEL IMPLEMENTATION
# -----------------------------------------------------------------------------

class MinimumDopplerModel:
    """
    Implements the derivation of the minimum Doppler factor based on 
    photopion cascade luminosity constraints.
    """
    
    def __init__(self):
        # The model relies on the derived formula:
        # delta^(2+2*beta) = coeff
        pass

    def spectral_function(self, beta):
        """
        Calculates the spectral function f(beta).
        
        Formula: f(beta) = (2 / (1 + beta)) * (5/16 + g(beta)/2)
        with g(beta) = (1/200) * 30^(beta - 1)
        """
        # Note: The problem statement defines g(beta) explicitly.
        # We implement it exactly as requested.
        g_beta = (1.0 / 200.0) * (30.0 ** (beta - 1.0))
        val = (2.0 / (1.0 + beta)) * (5.0/16.0 + g_beta / 2.0)
        return val

    def calculate_delta_min(self, z, t_v, E_s_eV, Ep_Lp_erg, L_s_ergs, L_X_lim_ergs, 
                            sigma_pi_cm2, beta, delta_epsilon_geV, f_x):
        """
        Calculates delta_min^(2+2*beta) and delta_min.
        
        Parameters:
        -----------
        z : float
            Source redshift.
        t_v : float
            Variability time-scale [s].
        E_s_eV : float
            Characteristic synchrotron photon energy [eV] (observer frame).
        Ep_Lp_erg : float
            Proton power per logarithmic bin [erg/s].
        L_s_ergs : float
            Isotropic-equivalent synchrotron luminosity [erg/s].
        L_X_lim_ergs : float
            Observational limit on X-ray luminosity [erg/s].
        sigma_pi_cm2 : float
            Inelasticity-weighted photopion cross-section [cm^2].
        beta : float
            X-ray photon index.
        delta_epsilon_geV : float
            Photon energy at Delta-resonance peak in proton rest frame [GeV].
        f_x : float
            Fraction of cascade luminosity in X-ray band.
            
        Returns:
        --------
        delta_min_power : float
            The value of delta_min^(2 + 2*beta).
        delta_min : float
            The minimum Doppler factor.
        """
        
        # 1. Unit Handling
        # Ensure all inputs are treated in CGS units internally where necessary.
        # The formula requires E_s in the denominator squared.
        # E_s is provided in eV. We must calculate E_s in erg to match L_s (erg/s).
        # 1 eV = 1.602176634e-12 erg
        eV_to_erg = 1.602176634e-12
        E_s_erg = E_s_eV * eV_to_erg
        
        # Delta epsilon is provided in GeV. Convert to erg.
        # 1 GeV = 1e9 eV
        delta_epsilon_erg = delta_epsilon_geV * 1e9 * eV_to_erg
        
        # 2. Retrieve Spectral Function
        f_beta = self.spectral_function(beta)
        
        # 3. Calculate the components of the derived formula
        # Formula: 
        # delta^(2+2b) = [ f_x * (Ep Lp) * sigma * Ls * (1+z)^2 * (mp c^2) * f(beta) ] 
        #                / [ 4 * pi * c^3 * t_v^2 * L_X_lim * epsilon_bar * E_s^2 ]
        
        numerator = (f_x * Ep_Lp_erg * sigma_pi_cm2 * L_s_ergs * 
                     (1.0 + z)**2 * m_p_c2_erg * f_beta)
                     
        denominator = (4.0 * np.pi * c_light**3 * t_v**2 * 
                       L_X_lim_ergs * delta_epsilon_erg * E_s_erg**2)
        
        delta_min_power = numerator / denominator
        
        # 4. Extract delta_min
        # delta^(2+2b) = value  => delta = value^(1 / (2+2b))
        exponent = 2.0 + 2.0 * beta
        delta_min = delta_min_power ** (1.0 / exponent)
        
        return delta_min_power, delta_min

# -----------------------------------------------------------------------------
# 3. EXECUTION AND VISUALIZATION
# -----------------------------------------------------------------------------

if __name__ == "__main__":
    
    logger.info("--- Initializing Minimum Doppler Factor Calculation ---")
    
    model = MinimumDopplerModel()
    
    # --- Default Parameters (Blazar Scenario) ---
    # Based on typical FSRQ parameters (e.g., Ackermann et al. 2010)
    params = {
        'z': 0.5,
        't_v': 86400.0,        # 1 day in seconds
        'E_s_eV': 10.0,        # 10 eV (UV)
        'Ep_Lp_erg': 1.0e46,   # Proton power [erg/s]
        'L_s_ergs': 1.0e48,    # Synchrotron luminosity [erg/s]
        'L_X_lim_ergs': 1.0e45,# X-ray limit [erg/s]
        'sigma_pi_cm2': 5.0e-28,# Cross section [cm^2]
        'beta': 2.0,           # Photon index
        'delta_epsilon_geV': 0.3, # Resonance energy [GeV]
        'f_x': 0.1             # Fraction
    }
    
    logger.info(f"Input Parameters: {params}")
    
    # Perform Calculation
    power, delta = model.calculate_delta_min(**params)
    
    logger.info(f"\n--- Results ---")
    logger.info(f"Calculated delta_min^({2.0 + 2.0*params['beta']}): {power:.4e}")
    logger.info(f"Minimum Doppler Factor (delta_min): {delta:.4f}")
    
    # --- Visualization 1: Delta_min vs Variability Time ---
    # Sensitivity analysis: How does delta change with the assumed size of the region (t_v)?
    
    t_v_range = np.logspace(3, 6, 100) # 1 hour to 10 days
    deltas_tv = []
    
    for t in t_v_range:
        _, d = model.calculate_delta_min(t_v=t, **params)
        deltas_tv.append(d)
        
    plt.figure(figsize=(10, 6))
    plt.loglog(t_v_range, deltas_tv, linewidth=2, color='blue')
    plt.xlabel('Variability Time-scale $t_v$ [s]', fontsize=12)
    plt.ylabel('Minimum Doppler Factor $\\delta_{min}$', fontsize=12)
    plt.title('Sensitivity of $\\delta_{min}$ to Variability Time', fontsize=14)
    plt.grid(True, which="both", ls="-", alpha=0.5)
    plt.axhline(y=params['E_s_eV']*0 + delta, color='r', linestyle='--', label=f'Reference $\\delta={delta:.2f}$ at $t_v={params["t_v"]}$s')
    plt.legend()
    plt.tight_layout()
    plt.show()
    
    # --- Visualization 2: Delta_min vs X-ray Limit ---
    # Sensitivity analysis: How strictly does the X-ray observation constrain the jet?
    
    Lx_range = np.logspace(43, 47, 100)
    deltas_lx = []
    
    for lx in Lx_range:
        _, d = model.calculate_delta_min(L_X_lim_ergs=lx, **params)
        deltas_lx.append(d)
        
    plt.figure(figsize=(10, 6))
    plt.loglog(Lx_range, deltas_lx, linewidth=2, color='green')
    plt.xlabel('X-ray Luminosity Limit $L_{X,lim}$ [erg/s]', fontsize=12)
    plt.ylabel('Minimum Doppler Factor $\\delta_{min}$', fontsize=12)
    plt.title('Sensitivity of $\\delta_{min}$ to Observational Constraints', fontsize=14)
    plt.grid(True, which="both", ls="-", alpha=0.5)
    plt.axvline(x=params['L_X_lim_ergs'], color='r', linestyle='--', label=f'Reference Limit $L_X={params["L_X_lim_ergs"]:.1e}$')
    plt.legend()
    plt.tight_layout()
    plt.show()
```
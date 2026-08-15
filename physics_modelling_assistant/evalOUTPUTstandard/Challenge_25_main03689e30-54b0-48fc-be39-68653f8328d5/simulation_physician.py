
```python
import numpy as np
import matplotlib.pyplot as plt
from scipy.constants import c, m_p, eV, sigma, pi

def calculate_dmin_min_expression(
    t_v, 
    mpc2, 
    E_s, 
    EpLep, 
    L_s, 
    Lx_lim, 
    sigma_ppi, 
    beta, 
    Delta, 
    eps_Delta, 
    f_x, 
    z
):
    """
    Calculate the minimum Doppler factor delta based on the hadronic cascade luminosity constraint.
    
    Parameters:
    -----------
    t_v : float
        Observer-frame variability time-scale (s).
    mpc2 : float
        Proton mass energy (J).
    E_s : float
        Characteristic synchrotron-photon energy (observer frame, J).
    EpLep : float
        Proton power per logarithmic bin at E_p (W).
    L_s : float
        Isotropic-equivalent synchrotron luminosity at E_s (W).
    Lx_lim : float
        Observational upper limit on 0.3 – 10 keV luminosity (W).
    sigma_ppi : float
        Inelasticity-weighted photopion cross-section (m^2).
    beta : float
        X-ray photon index.
    Delta : float
        Mean fractional proton energy transferred to pions (dimensionless).
    eps_Delta : float
        Photon energy (in proton rest frame) at the Delta-resonance peak (J).
    f_x : float
        Fraction of cascade luminosity emerging in X-ray band.
    z : float
        Source redshift (dimensionless).
        
    Returns:
    --------
    float
        The derived value for delta_min^(2+2*beta).
    """
    
    # 1. Define the spectral function f(beta)
    # f(beta) = (2 / (1 + beta)) * (5/16 + (1/200) * 30^(beta - 1))
    term_spectral = (5/16) + (1/200) * (30**(beta - 1))
    f_beta = (2 / (1 + beta)) * term_spectral
    
    # 2. Derive delta_min^4 from the cascade luminosity constraint
    # Cascade Luminosity Constraint:
    # L_cascade_X = f_x * (Ep * L_Ep) * tau_pi_gamma <= Lx_lim
    # tau_pi_gamma = (sigma_ppi * n_ph * R_prime) / Delta  <-- Note: Delta is usually inside sigma hats or used in efficiency
    # According to the prompt: tau_pi_gamma is the optical depth.
    # The prompt gives: L_cascade_X = f_x * (EpLep) * tau_pi_gamma
    # We derived: tau_pi_gamma approx (sigma_ppi * f(beta) * L_s * (1+z)^2) / (4 * pi * c^2 * t_v * E_s * delta^4)
    # Note: The prompt lists Delta and eps_Delta, and the Delta-threshold relation.
    # However, the final requested closed-form expression derived in the thought process 
    # effectively encapsulates the physical dependencies into the variables given.
    # The expression derived was:
    # delta^4 >= [f_x * (EpLep) * sigma_ppi * f(beta) * L_s * (1+z)^2] / [4 * pi * c^2 * t_v * E_s * Lx_lim * Delta]
    # Note: The prompt's constraint equation L_cascade = f_x * EpLep * tau implies Delta is 
    # part of the efficiency calculation of tau (since tau is usually geometric, effective tau includes inelasticity).
    # However, if we look at the provided lists, Delta is listed. 
    # Let's verify the units in the derived formula: 
    # Numerator: 1 * J/s * m^2 * 1 * J/s * 1  = J^2 / (m^0 s^2)
    # Denominator: 1 * m^2/s^2 * s * J * J/s = J^2 / (m^0 s^2)
    # Dimensions match.
    
    # Using the derived expression:
    numerator = f_x * EpLep * sigma_ppi * f_beta * L_s * ((1 + z)**2)
    denominator = 4 * pi * (c**2) * t_v * E_s * Lx_lim * Delta
    
    delta_pow_4 = numerator / denominator
    
    # 3. Convert to delta^(2+2*beta)
    # delta^(2+2*beta) = (delta^4)^((1+beta)/2)
    exponent = (1 + beta) / 2.0
    delta_pow_2_plus_2beta = delta_pow_4 ** exponent
    
    return delta_pow_2_plus_2beta

# --- Visualization and Sensitivity Analysis ---

def run_sensitivity_analysis():
    # Realistic Parameters (SI Units)
    # Energy conversions
    eV_to_J = 1.602e-19
    GeV_to_J = 1.602e-10
    erg_to_W = 1e-7
    
    # Base parameters
    z = 0.1
    t_v_base = 3 * 3600  # 3 hours in seconds
    E_s_base = 10 * eV_to_J     # 10 eV
    EpLep_base = 1e46 * erg_to_W
    L_s_base = 1e46 * erg_to_W
    Lx_lim_base = 1e45 * erg_to_W
    sigma_ppi_base = 5e-28 * 1e-4  # cm^2 to m^2
    beta_base = 1.0
    Delta_base = 0.2 # Mean inelasticity
    eps_Delta_base = 0.3 * GeV_to_J
    f_x_base = 0.1
    mpc2 = m_p * c**2
    
    # Create a range for the variable to plot (e.g., Luminosity)
    L_s_range = np.logspace(44, 48, 50) * erg_to_W # 10^44 to 10^48 erg/s
    
    results = []
    
    # Calculate delta^(2+2beta) for each Luminosity
    for L_s in L_s_range:
        val = calculate_dmin_min_expression(
            t_v=t_v_base,
            mpc2=mpc2,
            E_s=E_s_base,
            EpLep=EpLep_base,
            L_s=L_s,
            Lx_lim=Lx_lim_base,
            sigma_ppi=sigma_ppi_base,
            beta=beta_base,
            Delta=Delta_base,
            eps_Delta=eps_Delta_base,
            f_x=f_x_base,
            z=z
        )
        results.append(val)
        
    results = np.array(results)
    
    # We can extract delta itself if we want to plot it, 
    # but the prompt asked for the expression delta^(2+2*beta).
    # Let's plot delta_min derived from it: delta = (result)^(1/(2+2*beta))
    delta_min_vals = results ** (1.0 / (2 + 2 * beta_base))
    
    plt.figure(figsize=(10, 6))
    plt.loglog(L_s_range * erg_to_W**-1 if False else L_s_range, delta_min_vals, 'b-', linewidth=2, label=rf'$\delta_{{\min}}$ for $\beta={beta_base}$')
    
    # Add a second line for a steeper spectrum (higher beta) to show sensitivity
    beta_steep = 1.5
    results_steep = []
    for L_s in L_s_range:
        val = calculate_dmin_min_expression(
            t_v=t_v_base,
            mpc2=mpc2,
            E_s=E_s_base,
            EpLep=EpLep_base,
            L_s=L_s,
            Lx_lim=Lx_lim_base,
            sigma_ppi=sigma_ppi_base,
            beta=beta_steep,
            Delta=Delta_base,
            eps_Delta=eps_Delta_base,
            f_x=f_x_base,
            z=z
        )
        results_steep.append(val)
        
    delta_min_vals_steep = np.array(results_steep) ** (1.0 / (2 + 2 * beta_steep))
    plt.loglog(L_s_range, delta_min_vals_steep, 'r--', linewidth=2, label=rf'$\delta_{{\min}}$ for $\beta={beta_steep}$')
    
    plt.xlabel(r'Synchrotron Luminosity $L_s$ [erg/s]')
    plt.ylabel(r'Minimum Doppler Factor $\delta_{\min}$')
    plt.title(r'Minimum Doppler Factor vs. Synchrotron Luminosity')
    plt.grid(True, which="both", ls="-", alpha=0.5)
    plt.legend()
    
    # Annotate with the expression used
    expr_text = (r"$\delta_{\min}^{2+2\beta} \propto \left[ \frac{L_s}{L_{X,\mathrm{lim}}} \right]^{\frac{1+\beta}{2}}$")
    plt.annotate(expr_text, xy=(0.5, 0.1), xycoords='axes fraction', 
                 fontsize=12, bbox=dict(boxstyle="round,pad=0.3", fc="yellow", alpha=0.3))

    plt.show()

if __name__ == "__main__":
    print("Calculating Minimum Doppler Factors based on Hadronic Cascade Model...")
    print("Physical Model Equation Implemented:")
    print("delta^(2+2*beta) = [ (f_x * EpLep * sigma_ppi * f(beta) * L_s * (1+z)^2) /")
    print("                        (4 * pi * c^2 * t_v * E_s * Lx_lim * Delta) ] ^ ((1+beta)/2)")
    print("-------------------------------------------------------------------")
    
    # Example with Base Parameters
    z = 0.1
    t_v = 3 * 3600 
    E_s = 10 * 1.602e-19 
    EpLep = 1e46 * 1e-7
    L_s = 1e46 * 1e-7
    Lx_lim = 1e45 * 1e-7
    sigma_ppi = 5e-28 * 1e-4 
    beta = 1.0
    Delta = 0.2 
    eps_Delta = 0.3 * 1.602e-10
    f_x = 0.1
    mpc2 = m_p * c**2
    
    result_term = calculate_dmin_min_expression(
        t_v, mpc2, E_s, EpLep, L_s, Lx_lim, sigma_ppi, beta, Delta, eps_Delta, f_x, z
    )
    
    delta_min = result_term ** (1.0 / (2.0 + 2.0 * beta))
    
    print(f"Derived Quantity delta^(2+2*beta): {result_term:.4e}")
    print(f"Calculated Minimum Doppler Factor delta_min: {delta_min:.2f}")
    
    run_sensitivity_analysis()
```
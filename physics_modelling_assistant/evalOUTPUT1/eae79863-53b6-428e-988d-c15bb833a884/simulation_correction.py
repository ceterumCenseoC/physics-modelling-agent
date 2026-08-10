```python
import numpy as np
import matplotlib.pyplot as plt

def calculate_bl_coupling():
    """
    Calculates the smallest epsilon_B-L coupling LIGO can probe based on mirror forces
    from dark matter vector field.
    """
    
    # --- Constants and Parameters ---
    
    # LIGO Parameters
    h_sens = 3.0e-24  # Strain sensitivity [Hz^-1/2]
    f_0 = 250.0       # Frequency [Hz]
    T_obs_years = 13.0 # Observation time [years]
    
    # Physical Constants
    m_n = 1.6749e-27  # Neutron mass [kg]
    
    # Reference Model Parameters (from Literature Eq 5)
    # h_ref = 6.56e-27 * (eps / 1e-23) * (f_0 / 100 Hz) * ( (q/M) / 2.80e26 )
    h_ref_base_val = 6.56e-27
    eps_ref = 1.0e-23
    f_ref = 100.0
    q_over_M_ref = 2.80e26  # [kg^-1], Reference charge-to-mass ratio
    
    # Scenarios for differential charge delta_q (dimensionless)
    delta_q_scenarios = [0.074, 6.0e-3, 5.0e-4]
    
    # --- Calculations ---
    
    # 1. Calculate Observation Time in Seconds
    seconds_per_year = 365.25 * 24 * 3600
    T_obs_sec = T_obs_years * seconds_per_year
    
    # 2. Calculate Minimum Detectable Strain (SNR=1)
    # SNR = h_rms / h_sens * sqrt(T_obs) => h_min = h_sens / sqrt(T_obs)
    h_min = h_sens / np.sqrt(T_obs_sec)
    
    # 3. Calculate the Coupling Constant Scaling Factor
    # We need to derive the relationship: h = Gamma * eps_B-L * delta_q
    # Gamma = h_ref_base_val * (1/eps_ref) * (f_0/f_ref) * ( (1/m_n) / q_over_M_ref )
    
    # Charge density of the doped mirror [kg^-1]
    rho_charge = 1.0 / m_n 
    
    # The scaling factor Gamma
    Gamma = h_ref_base_val * \
            (1.0 / eps_ref) * \
            (f_0 / f_ref) * \
            (rho_charge / q_over_M_ref)
            
    # 4. Solve for epsilon_B-L: eps = h_min / (Gamma * delta_q)
    results = {}
    coupling_values = []
    
    print(f"Calculation Parameters:")
    print(f"-----------------------")
    print(f"Observation Time      : {T_obs_years:.1f} years ({T_obs_sec:.3e} s)")
    print(f"Strain Sensitivity    : {h_sens:.2e} Hz^-1/2")
    print(f"Minimum Detectable h  : {h_min:.4e}")
    print(f"Gamma Factor          : {Gamma:.4e}")
    print(f"-----------------------\n")
    
    print(f"Results (Smallest probeable epsilon_B-L):")
    print(f"----------------------------------------")
    
    for dq in delta_q_scenarios:
        eps_bl = h_min / (Gamma * dq)
        results[dq] = eps_bl
        coupling_values.append(eps_bl)
        print(f"delta_q = {dq:.4e} : epsilon_B-L = {eps_bl:.4e}")
        
    return results

def plot_results(results):
    """
    Creates a graphic showing the relationship between delta_q and epsilon_B-L.
    """
    # Extract data for plotting
    delta_q_list = sorted(results.keys())
    eps_list = [results[k] for k in delta_q_list]
    
    plt.figure(figsize=(10, 6))
    
    # Plot points
    plt.loglog(delta_q_list, eps_list, 'o', color='blue', markersize=10, label='Calculated Limits')
    
    # Theoretical scaling line (1/delta_q characteristic)
    # Generate a smooth range for the line
    dq_line = np.logspace(np.log10(min(delta_q_list))-0.5, np.log10(max(delta_q_list))+0.5, 100)
    # Use the first data point to anchor the line (slope -1)
    ref_dq = delta_q_list[0]
    ref_eps = eps_list[0]
    slope = -1
    eps_line = ref_eps * (dq_line / ref_dq)**slope
    
    plt.loglog(dq_line, eps_line, '--', color='gray', alpha=0.7, label=r'Scaling ($\epsilon \propto \delta q^{-1}$)')
    
    plt.title(r'Smallest Probeable $\epsilon_{B-L}$ vs Differential Charge $\delta q$', fontsize=14)
    plt.xlabel(r'Differential Charge $\delta q$', fontsize=12)
    plt.ylabel(r'Coupling $\epsilon_{B-L}$', fontsize=12)
    plt.grid(True, which="both", ls="-", alpha=0.3)
    plt.legend()
    
    # Annotate points
    for dq, ep in zip(delta_q_list, eps_list):
        plt.annotate(f"{ep:.2e}", (dq, ep), xytext=(5, 5), textcoords='offset points', fontsize=10)

    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    # Calculate results
    final_results = calculate_bl_coupling()
    
    # Generate plots
    plot_results(final_results)
```
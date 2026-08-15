```python
import numpy as np
import matplotlib.pyplot as plt

def calculate_scalar_dm_coupling():
    """
    Calculates the minimum detectable coupling strength Lambda_gamma^-1 for 
    scalar field dark matter in the Cosmic Explorer interferometer.
    """
    
    # --- 1. Define Constants and Parameters ---
    
    # Physical Constants (Natural units used for field calc, SI for geometric)
    # We stick to the explicit steps in the theoretical framework.
    
    # Interferometer Parameters
    L_cm = 40.0 * 1e5  # 40 km in cm
    L_m = 40.0 * 1e3   # 40 km in m
    d_cm = 6.0         # Beamsplitter thickness in cm
    d_m = 0.06         # Beamsplitter thickness in m
    n0 = 3.5           # Refractive index
    hn = 2.00e-25      # Strain noise density in Hz^(-1/2)
    f_Hz = 200.0       # Frequency in Hz
    
    # Dark Matter Parameters
    rho_loc_GeV_cm3 = 0.4      # Local DM density in GeV/cm^3
    eta = 178                  # Overdensity factor
    v_km_s = 230.0             # DM velocity (unused in amplitude calc for coherent field, but noted)
    
    # Observation Times
    T_1_s = 1000.0
    T_2_yrs = 0.7
    
    # --- 2. Intermediate Calculations ---
    
    # 2a. Effective Dark Matter Density in GeV/cm^3
    rho_eff_GeV_cm3 = eta * rho_loc_GeV_cm3
    
    # 2b. Effective Dark Matter Density in Natural Units (GeV^4)
    # Conversion factor: 1 GeV/cm^3 ~= 7.69 * 10^-42 GeV^4
    # Derived from: 1 cm = 5.06e13 GeV^-1 (approx inverse mass)
    # 1 cm^-3 = (5.06e13)^3 GeV^3 ~= 1.29e41 GeV^3
    # 1 GeV/cm^3 = 1 GeV * (1.29e41)^-1 GeV^-3 = 7.75e-42 GeV^4
    # Using the value from the context for consistency: 7.69 * 10^-42
    conv_GeV_cm3_to_GeV4 = 7.69e-42
    rho_eff_GeV4 = rho_eff_GeV_cm3 * conv_GeV_cm3_to_GeV4
    
    # 2c. Scalar Mass (m) in GeV
    # m = 2 * pi * f
    # 1 Hz = 4.19e-24 GeV (using h = 6.582e-25 GeV*s, 2*pi*Hz * hbar -> Energy)
    # Or strictly m = 2*pi*f in natural units where f is energy.
    # 1 Hz corresponds to E = h*1s^-1 = 6.626e-34 J = 4.135e-15 eV = 4.135e-24 GeV
    # So m (GeV) = 2 * pi * f(Hz) * 4.135e-24 GeV/Hz
    hbar_GeV_s = 6.582119569e-25 # GeV*s
    m_GeV = 2 * np.pi * f_Hz * hbar_GeV_s
    
    # 2d. Scalar Field Amplitude (phi_0)
    # Formula: phi_0 = sqrt(2 * rho) / m
    phi_0_GeV = np.sqrt(2 * rho_eff_GeV4) / m_GeV
    
    # 2e. Derived Terms
    n_factor = n0**2 - 1 # = 11.25 for n0=3.5
    
    # --- 3. Calculate Lambda_inv ---
    # Formula: Lambda_inv = (4 * L * hn) / (d * n_factor * phi_0 * sqrt(T_obs))
    # Note on units:
    # L and d cancel out dimensionally (length).
    # phi_0 is in GeV. Result is GeV^-1.
    # hn is dimensionless (strain) / sqrt(Hz).
    # The factor (Hz^1/2) comes from sqrt(T_obs) if T_obs is in seconds.
    # Let's verify the scaling factor:
    # SNR = h0/hn * sqrt(T). 
    # h0 = (d(n^2-1)/4L) * (phi_0 / Lambda).
    # Lambda = (d(n^2-1)/4L) * (phi_0 / h0).
    # If SNR=1, h0 = hn / sqrt(T).
    # Lambda = (d(n^2-1)/4L) * phi_0 * sqrt(T) / hn.
    # Lambda_inv = (4L / d(n^2-1)) * hn / (phi_0 * sqrt(T)).
    
    # Pre-factor: 4 * L / d / n_factor
    # Since L and d are both lengths, ratio is unitless.
    geometric_factor = 4.0 * L_cm / d_cm / n_factor
    
    # Using T_obs in seconds
    T_2_s = T_2_yrs * 365.25 * 24 * 3600
    
    # Function to compute Lambda_inv
    def compute_coupling(T_sec):
        # Result in GeV^-1
        lambda_inv = geometric_factor * hn / (phi_0_GeV * np.sqrt(T_sec))
        return lambda_inv

    # Calculate Case 1
    Lamb_inv_1_GeV = compute_coupling(T_1_s)
    
    # Calculate Case 2
    Lamb_inv_2_GeV = compute_coupling(T_2_s)
    
    # Convert to TeV^-1 (1 TeV^-1 = 10^-3 GeV^-1)
    Lamb_inv_1_TeV = Lamb_inv_1_GeV * 1e-3
    Lamb_inv_2_TeV = Lamb_inv_2_GeV * 1e-3
    
    # --- 4. Graphics ---
    
    # Plot Sensitivity vs Observation Time
    # Range from 10^2 s to 10^7 s (approx a year)
    times = np.logspace(2, 8, 200) # 100s to 100,000,000s
    lambdas_inv = compute_coupling(times) * 1e-3 # to TeV^-1
    
    plt.figure(figsize=(10, 6))
    plt.loglog(times, lambdas_inv, label=r'Minimum Detectable $\Lambda_\gamma^{-1}$')
    plt.axvline(T_1_s, color='r', linestyle='--', label=f'T = {int(T_1_s)} s')
    plt.axvline(T_2_s, color='g', linestyle='--', label=f'T = {T_2_yrs} yrs')
    
    # Plot specific points
    plt.scatter([T_1_s], [Lamb_inv_1_TeV], color='red', zorder=5)
    plt.scatter([T_2_s], [Lamb_inv_2_TeV], color='green', zorder=5)
    
    plt.title(r'Cosmic Explorer Sensitivity to $\Lambda_\gamma^{-1}$ at 200 Hz')
    plt.xlabel(r'Observation Time $T_{obs}$ [s]')
    plt.ylabel(r'Coupling Strength $\Lambda_\gamma^{-1}$ [$TeV^{-1}$]')
    plt.grid(True, which="both", ls="-")
    plt.legend()
    plt.tight_layout()
    # Save figure
    plt.savefig('sensitivity_curve.png')
    
    # --- 5. Output Results ---
    print("--- Scalar Field Dark Matter Detection Analysis ---")
    print(f"Parameters:")
    print(f"  Frequency:           {f_Hz} Hz")
    print(f"  Scalar Mass (m):     {m_GeV:.2e} GeV")
    print(f"  DM Density (rho):    {rho_eff_GeV_cm3} GeV/cm^3")
    print(f"  Field Amp (phi_0):   {phi_0_GeV:.2f} GeV")
    print(f"  Geometric Factor:    {geometric_factor:.4f}")
    print("-" * 50)
    print(f"Results (SNR = 1):")
    print(f"Case 1 (T = {T_1_s} s):")
    print(f"  Lambda_inv = {Lamb_inv_1_GeV:.2e} GeV^{{-1}}")
    print(f"  Lambda_inv = {Lamb_inv_1_TeV:.3e} TeV^{{-1}}")
    print("-" * 20)
    print(f"Case 2 (T = {T_2_yrs} yrs = {T_2_s:.1e} s):")
    print(f"  Lambda_inv = {Lamb_inv_2_GeV:.2e} GeV^{{-1}}")
    print(f"  Lambda_inv = {Lamb_inv_2_TeV:.3e} TeV^{{-1}}")
    print("-" * 50)
    print("Graph saved as 'sensitivity_curve.png'")

if __name__ == "__main__":
    calculate_scalar_dm_coupling()
```
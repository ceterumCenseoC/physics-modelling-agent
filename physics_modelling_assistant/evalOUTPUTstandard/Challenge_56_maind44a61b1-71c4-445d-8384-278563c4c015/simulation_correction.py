```python
import numpy as np
import matplotlib.pyplot as plt

def calculate_scalar_dm_coupling():
    """
    Calculates the minimum detectable coupling strength Lambda_gamma^-1 for 
    scalar field dark matter in the Cosmic Explorer interferometer.
    
    The code models the interaction of a scalar dark matter field with the 
    dielectric medium of the interferometer beamsplitter. It computes the 
    field amplitude based on the local dark matter density (including an 
    overdensity factor) and derives the strain sensitivity limits for a 
    Signal-to-Noise Ratio (SNR) of 1.
    """
    
    # --- 1. Define Constants and Parameters ---
    
    # Interferometer Parameters (Cosmic Explorer)
    # Arm length
    L_km = 40.0
    L_cm = L_km * 1e5
    # Beamsplitter thickness
    d_cm = 6.0
    # Refractive index (Fused Silica-like approximation for high index)
    n0 = 3.5
    # Strain noise spectral density at target frequency
    hn = 2.00e-25  # Units: 1/sqrt(Hz)
    # Target observation frequency
    f_Hz = 200.0
    
    # Dark Matter Parameters
    # Local Dark Matter Density
    rho_loc_GeV_cm3 = 0.4
    # Overdensity factor (Virialization shock contrast ~178)
    eta = 178
    
    # Observation Times for Case Analysis
    T_1_s = 1000.0
    T_2_yrs = 0.7
    
    # --- 2. Intermediate Calculations ---
    
    # 2a. Effective Dark Matter Density
    # rho_DM = eta * rho_loc
    rho_eff_GeV_cm3 = eta * rho_loc_GeV_cm3
    
    # 2b. Convert Density to Natural Units (GeV^4)
    # Conversion: 1 GeV/cm^3 ~= 7.69 * 10^-42 GeV^4
    # Based on h*c ~ 1.97e-14 GeV*cm
    conv_GeV_cm3_to_GeV4 = 7.69e-42
    rho_eff_GeV4 = rho_eff_GeV_cm3 * conv_GeV_cm3_to_GeV4
    
    # 2c. Scalar Mass (m) corresponding to frequency f
    # Relationship: m = 2 * pi * f * hbar
    # hbar in GeV*s
    hbar_GeV_s = 6.582119569e-25 
    m_GeV = 2 * np.pi * f_Hz * hbar_GeV_s
    
    # 2d. Scalar Field Amplitude (phi_0)
    # For a coherent oscillating scalar field, rho = 0.5 * m^2 * phi_0^2
    # Solving for phi_0: phi_0 = sqrt(2 * rho) / m
    phi_0_GeV = np.sqrt(2 * rho_eff_GeV4) / m_GeV
    
    # 2e. Geometric Factors
    # Refractive index factor (n0^2 - 1)
    n_factor = n0**2 - 1
    
    # --- 3. Calculate Lambda_inv ---
    # Formula derived from setting SNR = 1:
    # Lambda_inv = (4 * L * h_n) / (d * (n0^2 - 1) * phi_0 * sqrt(T_obs))
    # Note: L and d must be in the same units to cancel out.
    
    # Pre-factor: 4 * L / d / n_factor
    geometric_factor = 4.0 * L_cm / d_cm / n_factor
    
    # Convert T_2 to seconds for calculation
    # 1 yr = 365.25 days
    T_2_s = T_2_yrs * 365.25 * 24 * 3600
    
    # Define calculation function
    def compute_coupling(T_sec):
        """
        Computes Lambda^-1 in GeV^-1.
        T_sec: Observation time in seconds.
        """
        # The term hn is in 1/sqrt(Hz). Since the signal accumulation time is T,
        # the noise effective amplitude scales as 1/sqrt(T), matching units.
        # Result units: (Unitless) * (Dimensionless) / (GeV * s^-1 * s^-1/2) ? No.
        # Let's re-verify dimensions:
        # geometric_factor [dimensionless]
        # hn [Hz^-1/2] = [s^1/2]
        # phi_0 [GeV]
        # sqrt(T) [s^1/2]
        # Result [1/GeV]. Correct.
        lambda_inv = geometric_factor * hn / (phi_0_GeV * np.sqrt(T_sec))
        return lambda_inv

    # Calculate Case 1: 1000 seconds
    Lamb_inv_1_GeV = compute_coupling(T_1_s)
    Lamb_inv_1_TeV = Lamb_inv_1_GeV * 1e-3 # Convert to TeV^-1
    
    # Calculate Case 2: 0.7 years
    Lamb_inv_2_GeV = compute_coupling(T_2_s)
    Lamb_inv_2_TeV = Lamb_inv_2_GeV * 1e-3 # Convert to TeV^-1
    
    # --- 4. Visualization ---
    
    # Generate a range of observation times for the sensitivity curve
    times = np.logspace(2, 8, 500) # 100 seconds to ~3 years
    lambdas_inv_GeV = compute_coupling(times)
    lambdas_inv_TeV = lambdas_inv_GeV * 1e-3
    
    plt.figure(figsize=(10, 6))
    plt.loglog(times, lambdas_inv_TeV, color='b', alpha=0.8, lw=2, label=r'Model Sensitivity')
    
    # Annotate Case 1
    plt.axvline(T_1_s, color='r', linestyle='--', alpha=0.6)
    plt.scatter([T_1_s], [Lamb_inv_1_TeV], color='red', zorder=5, s=60)
    plt.text(T_1_s, Lamb_inv_1_TeV, f'  $T={int(T_1_s)}$s\n  $\\Lambda^{{-1}}={Lamb_inv_1_TeV:.2e}$ TeV$^{{-1}}$', 
             verticalalignment='bottom')
    
    # Annotate Case 2
    plt.axvline(T_2_s, color='g', linestyle='--', alpha=0.6)
    plt.scatter([T_2_s], [Lamb_inv_2_TeV], color='green', zorder=5, s=60)
    plt.text(T_2_s, Lamb_inv_2_TeV, f'  $T={T_2_yrs}$yrs\n  $\\Lambda^{{-1}}={Lamb_inv_2_TeV:.2e}$ TeV$^{{-1}}$', 
             verticalalignment='bottom')

    plt.title(r'Cosmic Explorer Sensitivity to $\Lambda_\gamma^{-1}$ ($f=200$ Hz, $\eta=178$)')
    plt.xlabel(r'Observation Time $T_{obs}$ [s]')
    plt.ylabel(r'Coupling Strength $\Lambda_\gamma^{-1}$ [TeV$^{-1}$]')
    plt.grid(True, which="both", ls="-", alpha=0.3)
    plt.legend()
    plt.tight_layout()
    
    # Save the plot
    plt.savefig('sensitivity_curve.png')
    print("Plot saved to 'sensitivity_curve.png'")
    
    # --- 5. Report Final Results ---
    print("\n" + "="*60)
    print(" SCALAR DARK MATTER COUpling LIMIT CALCULATION ".center(60, "="))
    print("="*60)
    print(f"Input Parameters:")
    print(f"  Arm Length (L):              {L_km} km")
    print(f"  Beamsplitter Thickness (d):  {d_cm} cm")
    print(f"  Refractive Index (n0):       {n0}")
    print(f"  Frequency (f):               {f_Hz} Hz")
    print(f"  Scalar Mass (m):             {m_GeV:.2e} GeV")
    print(f"  Strain Noise (hn):           {hn:.2e} Hz^{{-1/2}}")
    print(f"  DM Density (rho):            {rho_eff_GeV_cm3} GeV/cm^3")
    print(f"  Field Amplitude (phi_0):     {phi_0_GeV:.2f} GeV")
    print("-" * 60)
    print("Results for SNR = 1:")
    print("-" * 60)
    print(f"Case 1 (Short Term, {T_1_s} s):")
    print(f"  Lambda_g_inv = {Lamb_inv_1_GeV:.3e} GeV^{{-1}}")
    print(f"  Lambda_g_inv = {Lamb_inv_1_TeV:.3e} TeV^{{-1}}")
    print("-" * 60)
    print(f"Case 2 (Long Term, {T_2_yrs} yrs):")
    print(f"  Lambda_g_inv = {Lamb_inv_2_GeV:.3e} GeV^{{-1}}")
    print(f"  Lambda_g_inv = {Lamb_inv_2_TeV:.3e} TeV^{{-1}}")
    print("="*60)

if __name__ == "__main__":
    calculate_scalar_dm_coupling()
```
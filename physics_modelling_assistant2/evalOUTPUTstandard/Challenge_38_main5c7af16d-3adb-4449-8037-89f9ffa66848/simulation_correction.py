```python
import numpy as np
import matplotlib.pyplot as plt
from scipy import integrate

# ==========================================
# 1. Physical Constants and Parameters
# ==========================================

# Boltzmann constant in eV/K
kB_eV_per_K = 8.617333262145e-5 

def get_hk_parameters():
    """
    Returns the structured parameters for the HK model simulation
    based on the provided context and analysis.
    
    Hierarchy criteria:
    U >> W >> k_B * T >> epsilon_1
    
    Hierarchy check:
    8.0 >> 1.0 >> 0.025 >> 0.001 (approx)
    """
    params = {
        'W': 1.0,              # Bandwidth in eV
        'U': 8.0,              # Interaction strength in eV
        'mu': 0.5,             # Chemical potential in eV (center of LHB)
        'T_K': 290.0,          # Temperature in Kelvin (Room temperature)
        'epsilon_1': 0.0,      # Energy of the initial state in eV (approx 0 for calculation)
        'N0': 1.0              # Density of states prefactor in 1/eV
    }
    return params

# ==========================================
# 2. Model Functions
# ==========================================

def fermi_function(epsilon, mu, T_eV):
    """
    Fermi-Dirac distribution function n(epsilon).
    
    Args:
        epsilon: Energy (eV)
        mu: Chemical potential (eV)
        T_eV: Temperature in Energy units (eV)
        
    Returns:
        n: Occupation probability
    """
    # Check for overflow/underflow to avoid runtime warnings
    x = (epsilon - mu) / T_eV
    # Clip x to avoid overflow in exp(-x) or exp(x)
    # This is standard numerical practice for Fermi functions
    # Note: If T_eV is 0 (unlikely in this physics context), division by zero occurs. 
    # In this simulation, T > 0 is guaranteed.
    x = np.clip(x, -100, 100) 
    return 1.0 / (np.exp(x) + 1.0)

def integrand(e2, e3, e4, epsilon_1, mu, T_eV):
    """
    The integrand of I(T).
    I = Integrate [ n2*nbar3*nbar4 + nbar2*n3*n4 ] * delta(e1 + e2 - e3 - e4)
    
    Here we calculate the expression in brackets. The delta function
    will be handled by the integration strategy (reducing dimensions).
    
    Args:
        e2, e3, e4: Energies (eV)
        epsilon_1: Fixed energy of state 1 (eV)
        mu: Chemical potential (eV)
        T_eV: Temperature (eV)
        
    Returns:
        value: The occupation factor term
    """
    n2 = fermi_function(e2, mu, T_eV)
    nbar2 = 1.0 - n2
    
    n3 = fermi_function(e3, mu, T_eV)
    nbar3 = 1.0 - n3
    
    n4 = fermi_function(e4, mu, T_eV)
    nbar4 = 1.0 - n4
    
    # Term 1: n2 * (1-n3) * (1-n4)
    term1 = n2 * nbar3 * nbar4
    
    # Term 2: (1-n2) * n3 * n4
    term2 = nbar2 * n3 * n4
    
    return term1 + term2

def integrand_reduced_wrapper(x, y, p):
    """
    Wrapper for the integrand used during numerical integration.
    Calculates e4 from x, y and checks physical bounds.
    """
    epsilon_1 = p['epsilon_1']
    W = p['W']
    e4 = epsilon_1 + x - y
    
    # Check if e4 is within the band [0, W]
    # The scattering process is confined to the Lower Hubbard Band.
    if e4 < 0 or e4 > W:
        return 0.0
        
    return integrand(x, y, e4, epsilon_1, p['mu'], p['T_eV'])

# ==========================================
# 3. Numerical Computation of I(T)
# ==========================================

def compute_I_numerical(params, limit=100, epsabs=1e-6, epsrel=1e-4):
    """
    Computes the phase space integral I(T) numerically.
    
    Strategy:
    To handle the delta function delta(e1 + e2 - e3 - e4), we reduce the 
    integration dimensions.
    Let x = e2, y = e3.
    Then e4 = e1 + e2 - e3 = e1 + x - y.
    The measure becomes: d_e2 * d_e3 * d_e4 = dx * dy * 1 (Jacobian is 1).
    
    I(T) = Integrate_x Integrate_y Integrand(x, y, e1+x-y) * Mask(e1+x-y in [0,W])
    
    Integration limits for x (e2) and y (e3) are [0, W].
    We must satisfy 0 <= e4 <= W.
    """
    W = params['W']
    mu = params['mu']
    T_K = params['T_K']
    epsilon_1 = params['epsilon_1']
    
    # Convert T to eV for calculations
    T_eV = T_K * kB_eV_per_K
    
    # Prepare parameters for wrapper
    p_calc = {
        'W': W,
        'mu': mu,
        'T_eV': T_eV,
        'epsilon_1': epsilon_1
    }
    
    # Perform numerical integration
    # We use scipy.nquad for double integration over [0, W] x [0, W]
    args = (p_calc,)
    
    result, error = integrate.nquad(integrand_reduced_wrapper, 
                                    [[0, W], [0, W]],
                                    args=args,
                                    opts={'limit': limit, 'epsabs': epsabs, 'epsrel': epsrel})
    
    return result

# ==========================================
# 4. Analytical Formula
# ==========================================

def analytical_I_T(params):
    """
    Computes the phase space integral using the derived analytical formula.
    
    Result:
    I(T) = (pi^2 / 3) * (kB * T)^2 + epsilon_1^2
    (Note: This is the value of the integral excluding the DOS prefactors or 
    dimensionless normalization, matching the units of Energy^2).
    """
    mu = params['mu']
    T_K = params['T_K']
    epsilon_1 = params['epsilon_1']
    
    T_eV = T_K * kB_eV_per_K
    
    term_T = (np.pi**2 / 3.0) * (T_eV)**2
    term_eps = epsilon_1**2
    
    return term_T + term_eps

# ==========================================
# 5. Main Execution and Visualization
# ==========================================

def main():
    # 1. Define Parameters
    params = get_hk_parameters()
    
    print("="*60)
    print("HK Model Phase Space Integral Calculation")
    print("="*60)
    print(f"Parameters:")
    print(f"  Bandwidth (W)       : {params['W']} eV")
    print(f"  Interaction (U)     : {params['U']} eV")
    print(f"  Chem. Potential (mu): {params['mu']} eV")
    print(f"  Temperature (T)     : {params['T_K']} K")
    print(f"  Temp (Energy) (kBT) : {params['T_K'] * kB_eV_per_K:.4f} eV")
    print(f"  Fixed Energy (eps1) : {params['epsilon_1']} eV")
    print("-"*60)

    # 2. Compute I(T) Numerically at specific T
    print("\nComputing I(T) at T = 290 K...")
    I_num = compute_I_numerical(params)
    I_ana = analytical_I_T(params)
    
    print(f"Numerical I(T) : {I_num:.6e} (eV)^2")
    print(f"Analytical I(T): {I_ana:.6e} (eV)^2")
    print(f"Difference     : {abs(I_num - I_ana):.6e}")
    print(f"Relative Error : {abs(I_num - I_ana)/I_ana * 100:.2f}%")
    
    # 3. Temperature Dependence Scan
    # Generate a range of temperatures satisfying W >> kBT
    print("\nGenerating Temperature Dependence Curve...")
    
    # Define temperature range: 10K to 500K
    # Note: W=1eV corresponds to ~11600 K. So range is well within W >> kBT.
    temps_K = np.linspace(10, 500, 50)
    
    I_numerical_values = []
    I_analytical_values = []
    
    # To speed up the numerical scan, we reduce integration accuracy slightly
    # compared to the single point calculation.
    print("Calculating for multiple temperatures (this might take a moment)...")
    for T in temps_K:
        # Update params dict for the loop
        p_scan = params.copy()
        p_scan['T_K'] = T
        
        # Numerical integration for this T
        val_num = compute_I_numerical(p_scan, limit=50, epsabs=1e-5, epsrel=1e-3)
        I_numerical_values.append(val_num)
        
        # Analytical value for this T
        I_analytical_values.append(analytical_I_T(p_scan))
        
        # Optional: Progress indicator
        # if T % 50 == 0: print(f"  Completed T = {T} K")
        
    # Convert to numpy arrays for plotting
    I_numerical_values = np.array(I_numerical_values)
    I_analytical_values = np.array(I_analytical_values)
    
    # 4. Plotting
    plt.figure(figsize=(8, 6))
    
    # Plot numerical result
    plt.plot(temps_K, I_numerical_values, 'o', label='Numerical Integration', markersize=4, alpha=0.7)
    
    # Plot analytical result
    plt.plot(temps_K, I_analytical_values, '--', label=f'Analytical: $\propto (k_B T)^2$', color='red', linewidth=2)
    
    # Formatting
    plt.title('Temperature Dependence of Phase Space Integral I(T)', fontsize=14)
    plt.xlabel('Temperature T (K)', fontsize=12)
    plt.ylabel('$I(T)$ [$(eV)^2$]', fontsize=12)
    plt.grid(True, linestyle='--', alpha=0.6)
    plt.legend(fontsize=12)
    
    # Annotate parameter regime
    plt.annotate(f"Regime: $U \\gg W \\gg k_B T$\n$W={params['W']}eV, U={params['U']}eV$", 
                 xy=(0.05, 0.95), xycoords='axes fraction', fontsize=10, verticalalignment='top',
                 bbox=dict(boxstyle='round', facecolor='white', alpha=0.8))

    plt.tight_layout()
    # plt.savefig('IT_vs_Temperature.png') # Uncomment to save
    plt.show()
    
    # 5. Check scaling linearity to confirm T^2
    # Plot I(T) vs T^2
    plt.figure(figsize=(8, 6))
    energy_squared_values = (temps_K * kB_eV_per_K)**2
    
    plt.plot(energy_squared_values, I_numerical_values, 'o', label='Numerical', alpha=0.7)
    plt.plot(energy_squared_values, I_analytical_values, '--', label='Analytical', color='red')
    
    plt.title('Scaling Check: $I(T)$ vs $(k_B T)^2$', fontsize=14)
    plt.xlabel('$(k_B T)^2$ [$(eV)^2$]', fontsize=12)
    plt.ylabel('$I(T)$ [$(eV)^2$]', fontsize=12)
    plt.grid(True, linestyle='--', alpha=0.6)
    plt.legend()
    
    # Fit linear to numerical to check slope approx pi^2/3
    # We use a weighted fit or simple polyfit here
    # Ensure data is valid for fitting (no zeros if log scale used, but here linear)
    mask = energy_squared_values > 0
    coeffs = np.polyfit(energy_squared_values[mask], I_numerical_values[mask], 1)
    slope = coeffs[0]
    theoretical_slope = np.pi**2 / 3.0
    
    plt.annotate(f"Theoretical Slope $\\pi^2/3$: {theoretical_slope:.4f}\n" \
                 f"Numerical Fit Slope    : {slope:.4f}", 
                 xy=(0.05, 0.05), xycoords='axes fraction', fontsize=10,
                 bbox=dict(boxstyle='round', facecolor='white', alpha=0.8))
             
    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    main()
```

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
    n1 = fermi_function(e2, mu, T_eV)
    nbar1 = 1.0 - n1
    
    n2 = fermi_function(e3, mu, T_eV)
    nbar2 = 1.0 - n2
    
    n3 = fermi_function(e4, mu, T_eV)
    nbar3 = 1.0 - n3
    
    # Term 1: n2 * (1-n3) * (1-n4)
    term1 = n1 * nbar2 * nbar3
    
    # Term 2: (1-n2) * n3 * n4
    term2 = nbar1 * n2 * n3
    
    return term1 + term2

# ==========================================
# 3. Numerical Computation of I(T)
# ==========================================

def compute_I_numerical(params):
    """
    Computes the phase space integral I(T) numerically.
    
    Strategy:
    To handle the delta function delta(e1 + e2 - e3 - e4), we reduce the 
    integration dimensions.
    Let x = e2, y = e3.
    Then e4 = e1 + e2 - e3 = e1 + x - y.
    The measure becomes: d_e2 * d_e3 * d_e4 = dx * dy * 1 (since de4/de2=1).
    
    I(T) = Integrate_x Integrate_y Integrand(x, y, e1+x-y) * Mask(e1+x-y in [0,W])
    
    Integration limits for x (e2) and y (e3) are [0, W].
    We must satisfy 0 <= e4 <= W.
    """
    W = params['W']
    mu = params['mu']
    T_K = params['T_K']
    epsilon_1 = params['epsilon_1']
    
    # Convert T to eV
    T_eV = T_K * kB_eV_per_K
    
    # Define the domain function for e4
    def feasible_x_y(x, y):
        e4 = epsilon_1 + x - y
        return (e4 >= 0) & (e4 <= W)

    def integrand_reduced(x, y):
        # Calculate e4 from x and y
        e4 = epsilon_1 + x - y
        
        # Check if e4 is within the band [0, W]
        # If outside, contribution is zero (or technically infinite energy relative to LHB, 
        # but occupation f ~ 0 in LHB context so integrand ~ 0).
        if e4 < 0 or e4 > W:
            return 0.0
            
        return integrand(x, y, e4, epsilon_1, mu, T_eV)

    # Perform numerical integration
    # We use scipy.nquad for double integration
    # Warning: This can be slow if the mesh is not optimized or if the function varies wildly.
    # However, for I(T) ~ T^2, the function is smooth (Fermi functions).
    
    result, error = integrate.nquad(integrand_reduced, 
                                    [[0, W], [0, W]],
                                    opts={'limit': 100, 'epsabs': 1e-6, 'epsrel': 1e-4})
    
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
    
    # To speed up the numerical scan, we can reduce integration accuracy or 
    # sample fewer points. Here we do 50 points.
    
    print("Calculating for multiple temperatures (this might take a moment)...")
    for T in temps_K:
        # Update params dict
        p_scan = params.copy()
        p_scan['T_K'] = T
        
        # Numerical
        # For the scan we might accept slightly lower accuracy to maintain speed
        val_num, _ = integrate.nquad(
            lambda x, y: (
                0.0 if (p_scan['epsilon_1'] + x - y < 0 or p_scan['epsilon_1'] + x - y > p_scan['W'])
                else integrand(x, y, p_scan['epsilon_1'] + x - y, p_scan['epsilon_1'], p_scan['mu'], T * kB_eV_per_K)
            ),
            [[0, p_scan['W']], [0, p_scan['W']]],
            opts={'limit': 50, 'epsabs': 1e-5}
        )
        I_numerical_values.append(val_num)
        
        # Analytical
        I_analytical_values.append(analytical_I_T(p_scan))
        
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
    plt.text(0.05, 0.95, 
             f"Regime: $U \\gg W \\gg k_B T$\n$W={params['W']}eV, U={params['U']}eV$", 
             transform=plt.gca().transAxes, fontsize=10, verticalalignment='top',
             bbox=dict(boxstyle='round', facecolor='white', alpha=0.8))

    plt.tight_layout()
    # plt.savefig('IT_vs_Temperature.png') # Uncomment to save
    plt.show()
    
    # Check scaling linearity to confirm T^2
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
    coeffs = np.polyfit(energy_squared_values, I_numerical_values, 1)
    slope = coeffs[0]
    theoretical_slope = np.pi**2 / 3.0
    
    plt.text(0.05, 0.05, 
             f"Theoretical Slope $\\pi^2/3$: {theoretical_slope:.4f}\n" \
             f"Numerical Fit Slope    : {slope:.4f}", 
             transform=plt.gca().transAxes, fontsize=10,
             bbox=dict(boxstyle='round', facecolor='white', alpha=0.8))
             
    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    main()
```
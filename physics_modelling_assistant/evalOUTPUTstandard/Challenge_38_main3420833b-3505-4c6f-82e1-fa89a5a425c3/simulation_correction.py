
```python
import numpy as np
import matplotlib.pyplot as plt

# Based on unit checking and physics analysis:
# Units: Energies are in [E] (e.g., eV). Temperature is in [E] (k_B = 1).
# The final result I(T) has units of [E^2].

def n_occupation(epsilon, mu, T):
    """
    Calculates the occupation number n(epsilon) for the HK model 
    in the limit U >> W >> k_B T.
    
    Formula derived from the partition function in the lower Hubbard band:
    n(epsilon) = 1 / (exp(beta * (epsilon - mu)) + 2)
    
    Parameters:
    epsilon : float or array
        Energy of the state.
    mu : float
        Chemical potential.
    T : float
        Temperature (in energy units, k_B = 1).
        
    Returns:
    float or array
        Occupation number probability (0 to 0.5 for this band limit).
    """
    if T <= 0:
        # Handle zero temperature limit to avoid division by zero
        # For T -> 0, n(eps) -> 1/2 if eps < mu, 0 if eps > mu
        return 0.5 * (epsilon < mu)
        
    beta = 1.0 / T
    return 1.0 / (np.exp(beta * (epsilon - mu)) + 2)

def integrand(x2, x3, x1_scaled):
    """
    Dimensionless integrand for I(T).
    
    I(T) = (k_B T)^2 * Integral[ F(x2, x3) ] dx2 dx3
    
    Energy conservation: epsilon_1 + epsilon_2 = epsilon_3 + epsilon_4
    Dimensionless: x1 + x2 = x3 + x4 => x4 = x1 + x2 - x3
    
    The integrand represents:
    < n_2 (1-n_3)(1-n_4) + (1-n_2) n_3 n_4 >
    
    Parameters:
    x2, x3 : float
        Dimensionless energy variables (eps - mu) / (k_B T).
    x1_scaled : float
        Scaled energy of mode 1: epsilon_1 / (k_B T). 
        Assumed to be small (<< 1).
    """
    x4 = x1_scaled + x2 - x3
    
    # Calculate occupation number n(x) = 1 / (exp(x) + 2)
    # Note: The variable x is (epsilon - mu)/kT.
    
    denom2 = np.exp(x2) + 2.0
    denom3 = np.exp(x3) + 2.0
    denom4 = np.exp(x4) + 2.0
    
    n2 = 1.0 / denom2
    n3 = 1.0 / denom3
    n4 = 1.0 / denom4
    
    # Term 1: n_2 * (1-n_3) * (1-n_4)
    term1 = n2 * (1.0 - n3) * (1.0 - n4)
    
    # Term 2: (1-n_2) * n_3 * n_4
    term2 = (1.0 - n2) * n3 * n4
    
    return term1 + term2

def compute_I_T(T, mu, epsilon_1, limit=10.0):
    """
    Computes the energy phase space integral I(T).
    
    I(T) ~ (k_B T)^2 * Integral dx2 dx3 [ ... ]
    
    Parameters:
    T : float
        Temperature in Energy units.
    mu : float
        Chemical Potential in Energy units.
    epsilon_1 : float
        Energy of the propagating mode. Assumed epsilon_1 << k_B T.
    limit : float
        Integration limit for the dimensionless variables x (-limit, +limit).
        Since distribution decays exponentially, limit ~ 10 is sufficient.
    """
    # Dimensionless scaling parameter
    x1_scaled = epsilon_1 / T
    
    # Grid for integration
    # We need to integrate over x2 and x3. x4 is determined by conservation.
    N = 200  # Grid points
    xs = np.linspace(-limit, limit, N)
    dx = xs[1] - xs[0]
    
    X2, X3 = np.meshgrid(xs, xs)
    
    # Vectorized integrand calculation
    Z = integrand(X2, X3, x1_scaled)
    
    # Perform 2D integration using Simpson's rule or simple sum (Trapezoidal)
    # For smoothness, simple summation is acceptable for demonstration of scaling
    integral_val = np.sum(Z) * dx * dx
    
    # Scale by (k_B T)^2 to get I(T) with units [E^2]
    # Note: We assume k_B = 1.
    I_T = (T**2) * integral_val
    
    return I_T

def main():
    # --- Parameters Setup ---
    # Suggested starting parameters based on the analysis
    # Units: eV (electron-volts)
    
    W = 1.0        # Bandwidth [E]
    U = 10.0       # Interaction Strength [E] (U >> W)
    mu = 0.5 * W   # Chemical Potential [E] (Crosses lower Hubbard band)
    
    epsilon_1 = 0.001 # Energy of mode 1 [E] (Must be <~ k_B T)
    
    # Temperatures to scan (Energy units)
    # Condition: W >> T. So T should roughly be between 0.01 and 0.2
    T_min = 0.01
    T_max = 0.20
    T_points = 20
    Temperatures = np.linspace(T_min, T_max, T_points)
    
    print(f"--- HK Model Simulation ---")
    print(f"Parameters: U={U} eV, W={W} eV, mu={mu} eV")
    print(f"Condition U >> W: {U} >> {W} (Satisfied)")
    print(f"Propagating mode energy epsilon_1 = {epsilon_1} eV")
    print(f"Computing I(T) vs Temperature...")
    
    I_T_values = []
    
    for T in Temperatures:
        # Theoretical check: k_B T >> epsilon_1
        # If T is small, our assumption epsilon_1 << k_B T breaks down.
        # The code still runs but represents a different physical regime.
        if T <= epsilon_1:
            print(f"Warning at T={T:.4f}: k_B T is not >> epsilon_1. Results may deviate from T^2 approx.")
            
        val = compute_I_T(T, mu, epsilon_1)
        I_T_values.append(val)

    I_T_values = np.array(I_T_values)

    # --- Analysis and Plotting ---
    
    # 1. Plot I(T) vs T
    plt.figure(figsize=(10, 6))
    plt.plot(Temperatures, I_T_values, 'o-', label='Numerical Integration $I(T)$')
    
    # 2. Compare with Quadratic Scaling (T^2)
    # We fit a quadratic curve I = c * T^2
    # (We expect linear and constant terms to be zero)
    fit_coeff = np.polyfit(Temperatures, I_T_values, 2)
    
    T_fine = np.linspace(T_min, T_max, 100)
    I_fit = np.polyval(fit_coeff, T_fine)
    
    plt.plot(T_fine, I_fit, '--', 
             label=f'Quadratic Fit $\\propto T^2$ (coeff={fit_coeff[0]:.4f})')
    
    plt.xlabel('Temperature $T$ [eV] ($k_B=1$)')
    plt.ylabel('Phase Space Integral $I(T)$ [eV$^2$]')
    plt.title('Temperature Dependence of Energy Phase Space Integral')
    plt.legend()
    plt.grid(True, alpha=0.3)
    
    # 3. Plot I(T) / T^2 to verify constant dependence
    plt.figure(figsize=(10, 6))
    # Avoid division by zero if T=0 is included, but T_min is 0.01
    ratio = I_T_values / (Temperatures**2)
    
    mean_A = np.mean(ratio)
    
    plt.plot(Temperatures, ratio, 's-', color='green')
    plt.axhline(y=mean_A, color='r', linestyle='--', label=f'Mean A = {mean_A:.4f}')
    
    # Check relative deviation from mean
    # Deviations are expected at very low T (epsilon_1不再是 small parameter) 
    # or very high T (approx W >> T fails).
    rel_error = (ratio - mean_A) / mean_A
    
    print(f"Computed constant A (mean): {mean_A:.5f}")
    print(f"Relative deviation in constant A (max): {np.max(np.abs(rel_error))*100:.2f}%")
    
    # Highlight points where approximation is less valid
    valid_indices = Temperatures > 5 * epsilon_1 # heuristic kBT > 5*eps1
    mean_A_valid = np.mean(ratio[valid_indices])
    print(f"Computed constant A (valid T): {mean_A_valid:.5f}")

    plt.xlabel('Temperature $T$ [eV]')
    plt.ylabel('$I(T) / T^2$ [dimensionless constant]')
    plt.title('Verification of Quadratic Scaling $I(T) \\propto T^2$')
    plt.legend()
    plt.grid(True, alpha=0.3)
    
    plt.show()
    
    print("--- Simulation Complete ---")

if __name__ == "__main__":
    main()
```
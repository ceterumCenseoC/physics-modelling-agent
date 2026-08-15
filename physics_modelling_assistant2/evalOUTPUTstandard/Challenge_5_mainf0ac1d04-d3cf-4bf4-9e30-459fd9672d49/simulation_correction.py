```python
import numpy as np
import matplotlib.pyplot as plt
from scipy.special import polygamma, loggamma

def compute_g_alpha(alpha_array, k_max=100, tol=1e-15):
    """
    Computes the derivative g(alpha) = d/dn f(n, alpha) at n=0 
    for an array of alpha values in [0, 1].

    The function is evaluated using the derived series representation:
    g(alpha) = ln(1+alpha)/(1+alpha) - 1/(2(1+alpha)) * S
    
    where S is the infinite series sum over k.

    Parameters:
    -----------
    alpha_array : array_like
        Array of alpha values (dimensionless) in the range [0, 1].
    k_max : int
        Maximum number of terms for the series sum. Default is 100.
    tol : float
        Tolerance for series convergence. Stopping criterion for terms.
        Default is 1e-15.

    Returns:
    --------
    g_values : ndarray
        Computed values of g(alpha) corresponding to the input alpha_array.
    """
    g_values = np.zeros_like(alpha_array, dtype=np.float64)

    # Pre-calculate constants
    # psi(1) = -EulerGamma
    # psi(0.5) = -EulerGamma - 2*ln(2)
    psi_1 = -np.euler_gamma
    psi_half = -np.euler_gamma - 2 * np.log(2)
    
    # Iterate over each alpha value
    for i, alpha in enumerate(alpha_array):
        # Handle the special case alpha = 0 strictly to avoid division by zero 
        # in z calc or log, though the limits handle it naturally.
        # The limit as alpha -> 0 is g(0) = 0.
        if alpha == 0:
            g_values[i] = 0.0
            continue

        # 1. Calculate z
        # z = 4*alpha / (1 + alpha)^2
        denom = (1.0 + alpha)
        z = 4.0 * alpha / (denom ** 2)
        
        # 2. Calculate Log Term
        # Term_L = ln(1 + alpha) / (1 + alpha)
        term_L = np.log(denom) / denom
        
        # 3. Calculate Series Sum S
        # S = sum_{k=0}^inf C_k * [ Psi_diff_a + Psi_diff_b ]
        # C_k = (0.5)_k / ((k+1) * k!) * z^k
        
        S = 0.0
        fac_k = 1.0 # Initialize k! for k=0 (0! = 1)
        
        # We implement the series summation
        for k in range(k_max + 1):
            # Calculate Pochhammer (0.5)_k = Gamma(0.5 + k) / Gamma(0.5)
            # Using loggamma for numerical stability with Gamma functions
            if k == 0:
                poch_h = 1.0
            else:
                # log(Gamma(k + 0.5)) - log(Gamma(0.5))
                log_poch_h = loggamma(k + 0.5) - loggamma(0.5)
                poch_h = np.exp(log_poch_h)

            # Calculate coefficient C_k
            # (0.5)_k / ((k+1) * k!) * z^k
            denom_coeff = (k + 1.0) * fac_k
            C_k = (poch_h / denom_coeff) * (z ** k)
            
            # Calculate Digamma terms
            # Psi(k + 0.5) - Psi(0.5)
            psi_diff_a = polygamma(0, k + 0.5) - psi_half
            
            # Psi(k + 1) - Psi(1)
            psi_diff_b = polygamma(0, k + 1) - psi_1
            
            # contribution to sum
            term_k = C_k * (psi_diff_a + psi_diff_b)
            
            S += term_k
            
            # Update factorial for next iteration: (k+1)! = (k+1) * k!
            fac_k *= (k + 1.0)
            
            # Check for convergence (relative or absolute small term)
            # We check if the current term is negligible
            if k > 10 and abs(term_k) < tol:
                break
        
        # 4. Combine terms
        # g(alpha) = Term_L - 1/(2(1+alpha)) * S
        prefactor_S = 1.0 / (2.0 * denom)
        g_val = term_L - prefactor_S * S
        
        g_values[i] = g_val
        
    return g_values

def main():
    # --- Problem Setup Parameters ---
    alpha_min = 0.0
    alpha_max = 1.0
    num_points = 200
    
    # Generate alpha values
    alpha_grid = np.linspace(alpha_min, alpha_max, num_points)
    
    # --- Execution ---
    print("Computing g(alpha) for alpha in [0, 1]...")
    g_grid = compute_g_alpha(alpha_grid)
    
    # --- Output ---
    # Print some specific values
    indices_to_print = [0, int(num_points/4), int(num_points/2), int(3*num_points/4), num_points-1]
    print("\nSample Results:")
    print(f"{'Alpha':<10} | {'g(alpha)':<15}")
    print("-" * 28)
    for idx in indices_to_print:
        print(f"{alpha_grid[idx]:<10.4f} | {g_grid[idx]:<15.10f}")

    # --- Visualization ---
    plt.figure(figsize=(10, 6))
    plt.plot(alpha_grid, g_grid, label=r'$g(\alpha)$', linewidth=2, color='blue')
    
    # Add labels and title
    plt.title(r'Evaluation of $g(\alpha) = \left. \frac{\partial f(n, \alpha)}{\partial n} \right|_{n=0}$', fontsize=14)
    plt.xlabel(r'Parameter $\alpha$', fontsize=12)
    plt.ylabel(r'$g(\alpha)$', fontsize=12)
    
    # Add grid and legend
    plt.grid(True, which='both', linestyle='--', alpha=0.7)
    plt.legend(fontsize=12)
    
    # Set reasonable limits
    plt.xlim(0, 1)
    # Dynamically set y limits based on computed data
    y_min = np.min(g_grid)
    y_max = np.max(g_grid)
    plt.ylim(y_min - 0.1*abs(y_min), y_max + 0.1*abs(y_max))
    
    # Save the plot
    plt.savefig('g_alpha_plot.png', dpi=300, bbox_inches='tight')
    
    print("\nPlot saved as 'g_alpha_plot.png'.")
    print("Computation complete.")

if __name__ == "__main__":
    main()
```
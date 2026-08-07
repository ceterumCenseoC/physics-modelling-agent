
```python
import numpy as np

def matching_kernel_lo(xi, x, mu, Pz):
    """
    Computes the one-loop matching kernel C^(1) for LaMET.
    
    Args:
        xi (float or np.array): Ratio x/y.
        x (float): The external momentum fraction x.
        mu (float): Renormalization scale.
        Pz (float): Hadron longitudinal momentum.
        
    Returns:
        float or np.array: The kernel value.
    """
    # Avoid potential division by zero warnings, though mask logic should handle it
    if not isinstance(xi, np.ndarray):
        xi = np.array([xi])

    K = np.zeros_like(xi)
    prefactor_factor = 1.0 # Prefactor alpha_s * Cf / 2pi is applied outside for vectorization efficiency
    
    # Mask for xi ranges
    # Region 1: 0 < xi < 1 (DGLAP region / x < y)
    mask1 = (xi > 0) & (xi < 1)
    
    # Region 2: xi > 1 (LaMET genuine region / x > y)
    mask2 = xi > 1
    
    # xi == 1 is handled by the plus distribution subtraction (zero contribution)
    
    # Region 1 Calculation
    if np.any(mask1):
        xi_1 = xi[mask1]
        # Term: (1+xi^2)/(1-xi) * [ -ln(mu^2/(4 x^2 Pz^2)) + ln((1-xi)/xi) ] - xi(1+xi)/(1-xi)
        # Note: The log term -ln(mu^2/4x^2Pz^2) depends on the external x, not y (or xi).
        
        # Logarithm argument 1: mu^2 / (4 x^2 Pz^2)
        # Limit check: x starts at 0.002, so x^2 is 4e-6. 4*x^2 = 1.6e-5.
        # If mu=Pz=2, arg = 1 / (4*x^2).
        log_arg1 = (mu**2) / (4 * x**2 * Pz**2)
        term_log_1 = -np.log(log_arg1)
        
        # Logarithm argument 2: (1-xi)/xi
        term_log_2 = np.log((1 - xi_1) / xi_1)
        
        denom = 1 - xi_1
        
        # Combine logs
        L = term_log_1 + term_log_2
        
        # Main structure
        # K = pref * ( (1+xi^2)/(1-xi) * L - xi(1+xi)/(1-xi) )
        val = ((1 + xi_1**2) / denom) * L - (xi_1 * (1 + xi_1)) / denom
        K[mask1] = val

    # Region 2 Calculation
    if np.any(mask2):
        xi_2 = xi[mask2]
        # Term: ( (1+xi^2)/(1-xi) * ln(xi/(xi-1)) + 1 + 3/(2xi) )_{+[1, inf]} - 3/(2xi)
        # The distribution regularization is handled by the subtraction method in the convolution.
        # We evaluate the function K(xi) explicitly.
        # Contribution simplifies to: (1+xi^2)/(1-xi) * ln(xi/(xi-1)) + 1
        
        denom = 1 - xi_2 # Negative
        log_ratio = np.log(xi_2 / (xi_2 - 1))
        
        val = ((1 + xi_2**2) / denom) * log_ratio + 1
        K[mask2] = val
        
    return K

def solve_lamet_matching():
    """
    Main function to compute the Pion PDF from Quasi-PDF using LaMET matching.
    """
    # 1. Parameters and Constants
    Cf = 4.0 / 3.0
    beta0 = 9.0
    Lambda_QCD = 0.2445  # GeV
    Pz = 2.0            # GeV
    mu = 2.0            # GeV (Target scale)
    
    # 2. Grid Setup
    N = 500
    x_min = 0.002
    x_max = 1.0
    # Create grid: x_i = 0.002 * (i+1) roughly?
    # Prompt: "x_i = 0.002 + (i-1)dx" to range 0.002 to 1.0
    grid = np.linspace(x_min, x_max, N)
    dx = grid[1] - grid[0]
    
    # 3. Running Coupling Alpha_s
    # alpha_s(mu) = 4 * pi / (beta0 * ln(mu^2 / Lambda_QCD^2))
    arg_as = mu**2 / Lambda_QCD**2
    alpha_s = 4 * np.pi / (beta0 * np.log(arg_as))
    
    # Prefactor for the kernel: alpha_s * Cf / (2 * pi)
    kernel_pref = alpha_s * Cf / (2 * np.pi)
    
    # 4. Input Quasi-PDF
    # tilde{f}(x) = (1/Pz) * (x + 3) * (1 - x)^3
    # The 1/Pz factor is to ensure units are GeV^-1, matching the formula dimensional analysis.
    # The prompt mentions "interpreted as tilde{f}(x) = 1/Pref * (x+3)(1-x)^3".
    # Also constraints: inputs are executable right away.
    f_tilde = (grid + 3) * (1 - grid)**3 / Pz
    
    # 5. Convolution Calculation (Matching)
    # f(x) = tilde{f}(x) - Convolution
    # Convolution = int_0^1 dy/|y| K(x/y) tilde{f}(y)
    # Discretized with Plus Distribution:
    # Sum_j (Delta y / y_j) * K(x_i/y_j) * (f_tilde(y_j) - f_tilde(x_i))
    
    f_matched = np.zeros(N)
    
    # Vectorized grid for integration
    y_grid = grid
    dy = dx
    weights = dy / y_grid
    
    # Loop over x (rows)
    for i in range(N):
        x_i = grid[i]
        ft_i = f_tilde[i]
        
        # Calculate xi for all y
        # xi = x_i / y_j
        xis = x_i / y_grid
        
        # Compute the kernel function K(xi) (excluding the prefactor which we multiply later)
        # The xi=1 case is handled inside: it returns 0 or finite, but multiplied by (f_j - f_i) -> 0.
        K_base = matching_kernel_lo(xis, x_i, mu, Pz)
        
        # Apply prefactor
        K_vals = kernel_pref * K_base
        
        # Integrands with subtraction
        diff = f_tilde - ft_i
        
        # Diagonal term (j=i): diff = 0. 
        # If K_base is inf at xi=1, the 0*inf limit is mathematically resolved by the subtraction,
        # numerically it will be 0 if we explicitly mask or rely on diff being 0.
        # We assume diff is 0 exactly at diagonal, so val is 0 regardless of K.
        
        integrand = weights * K_vals * diff
        
        # Summation
        integral_val = np.sum(integrand)
        
        # Final PDF
        f_matched[i] = ft_i - integral_val

    # 6. Retrieve Results for Specific Points
    target_xs = [0.4, 0.5, 0.6]
    output_vals = {}
    
    for tx in target_xs:
        # Find index
        idx = (np.abs(grid - tx)).argmin()
        output_vals[tx] = f_matched[idx]
        
    # Return results and grid for verification if needed
    return output_vals

# Execute the function to get results
if __name__ == "__main__":
    results = solve_lamet_matching()
    
    print("Computed Pion PDF f(x, mu=2.0 GeV):")
    # Formatting output
    for x in [0.4, 0.5, 0.6]:
        val = results[x]
        print(f"x = {x:.1f}: {val:.4f}")
```
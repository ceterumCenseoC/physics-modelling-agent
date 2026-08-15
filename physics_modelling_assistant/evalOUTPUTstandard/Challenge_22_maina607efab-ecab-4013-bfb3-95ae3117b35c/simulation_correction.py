```python
import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import minimize_scalar

# ==========================================
# 1. Mathematical Formulation & Helper Functions
# ==========================================
# 
# Problem Definition:
# Optimize the Holevo information for an ensemble of 3x3 states parameterized 
# by gamma_x in [0,1] and theta.
# The optimal ensemble is determined to be binary, consisting of the pure 
# state (gamma=0) and the maximally mixed state (gamma=1) within the subspace.
# The optimization is over the probability parameter x in [0,1].
#
# Formula:
# f(x) = S(average_state) - sum(p_i * S(rho_i))
#
# Where:
# S(rho) denotes the von Neumann entropy in bits (log base 2).
# h(y) = -y log2(y) - (1-y) log2(1-y) is the binary entropy function.
#
# Entropy of individual states:
# For gamma=1: Eigenvalues are {cos^2(theta), sin^2(theta), 0}. 
#               S_1 = h(cos^2(theta)).
# For gamma=0: Eigenvalues are {1, 0, 0}. 
#               S_0 = 0.
#
# The average state for probability x of the mixed state is:
# rho_avg = x * rho_1 + (1-x) * rho_0
#
# The eigenvalues of rho_avg are:
# 1. lambda_1 = x * cos^2(theta)
# 2. lambda_2 = (1/2) * (1 - x*cos^2(theta) + sqrt(Delta))
# 3. lambda_3 = (1/2) * (1 - x*cos^2(theta) - sqrt(Delta))
# where Delta = (1 - x*cos^2(theta))^2 - x(1-x)sin^2(2*theta).
#
# The entropy of the average state is S(rho_avg) = h(lambda_1) + h(lambda_2).
# (Note: h(lambda_2) accounts for the entropy of the pair lambda_2, lambda_3 
#  because lambda_3 =Trace(block)-lambda_2).
#
# Objective function:
# f(x) = h(x * cos^2(theta)) + h(lambda_2) - x * h(cos^2(theta))

def binary_entropy(p):
    """
    Calculates the binary entropy h(p) = -p log2(p) - (1-p) log2(1-p).
    Handles edge cases p=0 and p=1.
    """
    p = np.asarray(p)
    # Numerical stability clipping to prevent log(0) warnings or NaNs
    # in vectorized operations. Limits are chosen to be well within 
    # float precision but safe for log.
    p_clipped = np.clip(p, 1e-15, 1.0 - 1e-15)
    
    h = -p * np.log2(p_clipped) - (1 - p) * np.log2(1 - p_clipped)
    
    # Strictly enforce h(0) = 0 and h(1) = 0 manually to correct clipping artifacts
    if isinstance(p, (float, int)):
        if p == 0 or p == 1:
            return 0.0
    else:
        h[p == 0] = 0.0
        h[p == 1] = 0.0
        
    return h

def holevo_function(x, theta):
    """
    Calculates the Holevo quantity f(x) for a specific theta.
    
    Args:
        x (float or np.array): The mixing probability in [0, 1].
        theta (float): The system angle in radians.
        
    Returns:
        float or np.array: The Holevo information in bits.
    """
    c2 = np.cos(theta)**2
    s2 = np.sin(theta)**2
    
    # 1. Entropy term from the first eigenvalue of the average state
    # Term: h(x * cos^2(theta))
    s_avg_part1 = binary_entropy(x * c2)
    
    # 2. Entropy term from the lower-right 2x2 block of the average state
    # Calculate Discriminant Delta
    # Delta = (1 - x*c2)^2 - x*(1-x)*sin^2(2*theta)
    # sin^2(2*theta) = 4 * sin^2(theta) * cos^2(theta) = 4 * s2 * c2
    term_in_sqrt = (1 - x * c2)**2 - x * (1 - x) * 4 * c2 * s2
    
    # Ensure numerical stability for the square root (handle small negative floats)
    term_in_sqrt = np.maximum(term_in_sqrt, 0)
    sqrt_delta = np.sqrt(term_in_sqrt)
    
    # The larger eigenvalue of the block
    lambda_block = 0.5 * (1 - x * c2 + sqrt_delta)
    
    # Entropy of the 2-state subsystem
    s_avg_part2 = binary_entropy(lambda_block)
    
    # 3. Average entropy of the individual states in the ensemble
    # S(rho_mixed) = h(cos^2(theta))
    # S(rho_pure) = 0
    # Weighted sum: x * h(cos^2(theta)) + (1-x) * 0
    s_ensemble_avg = x * binary_entropy(c2)
    
    # Total Holevo quantity
    return s_avg_part1 + s_avg_part2 - s_ensemble_avg

# ==========================================
# 2. Optimization Logic
# ==========================================

def solve_optimization(theta):
    """
    Finds the maximum of the Holevo function f(x) for a given theta.
    
    Args:
        theta (float): System parameter in radians.
        
    Returns:
        tuple: (optimal_x, max_holevo_value)
    """
    # Define the objective function for the minimizer (negative of Holevo)
    objective = lambda x: -holevo_function(x, theta)
    
    # Bounds: x is a probability [0, 1]
    bounds = (0, 1)
    
    # Use bounded minimization (Brent's method or similar bounded approach)
    result = minimize_scalar(objective, bounds=bounds, method='bounded')
    
    optimal_x = result.x
    max_val = -result.fun
    
    return optimal_x, max_val

# ==========================================
# 3. Main Execution and Analysis
# ==========================================

def main():
    # Define a range for theta based on the provided "Starting Parameters"
    # Realistic range: 30 to 60 degrees (pi/6 to pi/3).
    theta_start = np.pi / 6
    theta_end = np.pi / 3
    num_points = 100
    
    thetas = np.linspace(theta_start, theta_end, num_points)
    
    # Storage for results
    results_x = []
    results_chi = []
    
    print(f"{'Theta (deg)':<15} | {'Optimal x':<15} | {'Max Holevo (bits)':<15}")
    print("-" * 55)
    
    # Solve for each theta
    for th in thetas:
        x_opt, chi_max = solve_optimization(th)
        results_x.append(x_opt)
        results_chi.append(chi_max)
        
        # Print output for verification
        # Only printing a subset or specific points if there are too many, 
        # but for 100 points a summary loop is fine or just checking extremes.
        if th == thetas[0] or th == thetas[-1] or th == np.pi/4:
             print(f"{np.degrees(th):<15.2f} | {x_opt:<15.4f} | {chi_max:<15.4f}")

    # Visualization
    plt.figure(figsize=(12, 5))
    
    # Plot 1: Max Holevo Capacity vs Theta
    plt.subplot(1, 2, 1)
    plt.plot(np.degrees(thetas), results_chi, 'b-', linewidth=2.5, label=r'$\chi_{\max}$')
    plt.xlabel(r'$\theta$ (degrees)')
    plt.ylabel(r'Holevo Information $\chi$ (bits)')
    plt.title(r'Optimized Holevo Quantity vs $\theta$')
    plt.grid(True, linestyle='--', alpha=0.7)
    plt.legend()
    
    # Plot 2: Optimal Probability x vs Theta
    plt.subplot(1, 2, 2)
    plt.plot(np.degrees(thetas), results_x, 'r--', linewidth=2.5, label=r'$x_{opt}$')
    plt.xlabel(r'$\theta$ (degrees)')
    plt.ylabel(r'Optimal Probability $x$')
    plt.title(r'Optimal Mixing Probability $x$ vs $\theta$')
    plt.grid(True, linestyle='--', alpha=0.7)
    plt.legend()
    
    plt.tight_layout()
    plt.show()
    
    # Theoretical/Sanity Check
    # For theta = pi/4 (symmetric case), cos^2(theta) = 0.5, sin^2(theta) = 0.5.
    # At x = 0.5, eigenvalues of rho_avg:
    # lambda_1 = 0.5 * 0.5 = 0.25
    # block trace = 1 - 0.25 = 0.75
    # delta = (0.75)^2 - 4*0.5*(0.5)*0.25 = 0.5625 - 0.25 = 0.3125
    # lambda_+ = 0.5 * (0.75 + sqrt(0.3125))
    # We can verify numeric stability and physical bounds.
    # Max entropy for 3x3 system is log2(3) ~ 1.585.
    # Since Holevo info <= max entropy, values should be < 1.585.
    
    assert max(results_chi) < np.log2(3) + 1e-6, "Error: Holevo quantity exceeds sistem dimension limit."
    print("\nSimulation Complete. Sanity check passed.")

if __name__ == "__main__":
    main()
```
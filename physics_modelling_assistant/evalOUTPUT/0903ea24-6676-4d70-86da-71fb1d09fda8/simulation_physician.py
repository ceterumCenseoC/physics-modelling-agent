**
```python
import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import minimize_scalar

def binary_entropy(p):
    """
    Computes the binary entropy h(p) = -p log2(p) - (1-p) log2(1-p).
    Handles the boundary conditions where p is 0 or 1 manually
    to avoid numerical errors (NaN).
    """
    # Create a mask for valid probabilities (0 < p < 1)
    # We treat p close to 0 or 1 as 0 entropy effectively
    eps = np.finfo(float).eps
    
    # If input is scalar
    if np.isscalar(p):
        if p <= eps or p >= 1 - eps:
            return 0.0
        return -p * np.log2(p) - (1 - p) * np.log2(1 - p)
    
    # If input is array
    h = np.zeros_like(p)
    mask = (p > eps) & (p < 1 - eps)
    p_valid = p[mask]
    h[mask] = -p_valid * np.log2(p_valid) - (1 - p_valid) * np.log2(1 - p_valid)
    return h

def objective_function(x, theta):
    """
    The function f(x) = h(x) - h(x * cos^2(theta)) to be maximized.
    We minimize the negative of this function for scipy.optimize.
    """
    # x must be in (0, 1). 
    # The optimizer might test boundaries, so we clip or handle inside entropy.
    # However, for strict scalar optimization, passing the raw x is fine 
    # provided we don't evaluate exactly at 0 or 1 from the start.
    return -(binary_entropy(x) - binary_entropy(x * np.cos(theta)**2))

def solve_holevo_optimization():
    """
    Solves the optimization problem max_{x in [0,1]} [h(x) - h(x * cos^2(theta))]
    for a range of theta values and plots the result.
    """
    # 1. Setup Parameters based on planning
    # Theta range: 0 to pi/4
    # We avoid theta=0 strictly as the info is 0, and derivative behavior is trivial.
    theta_vals = np.linspace(0.01, np.pi/4, 200) 
    
    optimal_x_values = []
    max_chi_values = []
    
    print(f"{'Theta (rad)':<15} | {'Optimal x':<15} | {'Max Holevo Chi':<15}")
    print("-" * 50)

    for theta in theta_vals:
        # Optimization bounds for x: (0, 1)
        # We use a small epsilon for bounds to prevent numerical issues at exact 0 or 1
        bounds = (1e-9, 1 - 1e-9)
        
        # Perform the minimization
        res = minimize_scalar(
            objective_function, 
            args=(theta,), 
            bounds=bounds, 
            method='bounded'
        )
        
        if res.success:
            optimal_x = res.x
            max_chi = -res.fun # Flip sign back to get max
            optimal_x_values.append(optimal_x)
            max_chi_values.append(max_chi)
        else:
            print(f"Optimization failed for theta={theta}")
            optimal_x_values.append(np.nan)
            max_chi_values.append(np.nan)

    # Output specific values for demonstration (Start, Mid, End of range)
    indices_to_show = [0, len(theta_vals)//2, len(theta_vals)-1]
    for idx in indices_to_show:
        print(f"{theta_vals[idx]:<15.4f} | {optimal_x_values[idx]:<15.4f} | {max_chi_values[idx]:<15.4f}")

    # 2. Create Graphics
    plt.figure(figsize=(10, 6))
    
    # Plot 1: Max Holevo Information vs Theta
    plt.subplot(1, 2, 1)
    plt.plot(theta_vals, max_chi_values, 'b-', linewidth=2)
    plt.xlabel(r'$\theta$ (radians)')
    plt.ylabel(r'Max Holevo Information $\chi$ (bits)')
    plt.title(r'Maximal Holevo Information vs $\theta$')
    plt.grid(True, alpha=0.3)
    
    # Plot 2: Optimal x vs Theta
    plt.subplot(1, 2, 2)
    plt.plot(theta_vals, optimal_x_values, 'r--', linewidth=2)
    plt.xlabel(r'$\theta$ (radians)')
    plt.ylabel(r'Optimal probability $x$')
    plt.title(r'Optimal $x$ parameter vs $\theta$')
    plt.grid(True, alpha=0.3)
    
    plt.tight_layout()
    plt.savefig('holevo_optimization_results.png')
    plt.show()

    return theta_vals, optimal_x_values, max_chi_values

if __name__ == "__main__":
    # The problem asks for the implementation of the model and the explicit function form.
    # The function form is f(x) = h(x) - h(x * cos^2(theta)).
    # The code below calculates the maximal value for a range of physical parameters.
    
    # Execute the model
    thetas, xs, chis = solve_holevo_optimization()
    
    print("\n--- Model Implementation Complete ---")
    print("The model implements the function f(x) = h(x) - h(x * cos^2(theta)).")
    print("Results have been plotted and saved.")
```
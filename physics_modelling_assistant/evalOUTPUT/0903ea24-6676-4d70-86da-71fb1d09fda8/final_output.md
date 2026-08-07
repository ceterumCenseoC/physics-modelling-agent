**

The maximal value is given by the optimization $\max_{x\in[0,1]} f(x)$, where the function form of $f(x)$ is:
$$ f(x) = h(x) - h(x \cos^2 \theta) $$
and $h(u) = -u \log_2 u - (1-u) \log_2 (1-u)$ is the binary entropy function.

```python
import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import minimize_scalar

def binary_entropy(p):
    """
    Computes the binary entropy h(p) = -p log2(p) - (1-p) log2(1-p).
    """
    eps = np.finfo(float).eps
    is_scalar = np.isscalar(p)
    p_arr = np.array(p) if not is_scalar else p
    mask = (p_arr > eps) & (p_arr < 1 - eps)
    h = np.zeros_like(p_arr, dtype=float)
    p_valid = p_arr[mask]
    h[mask] = -p_valid * np.log2(p_valid) - (1 - p_valid) * np.log2(1 - p_valid)
    return h.item() if is_scalar else h

def objective_function(x, theta):
    """
    The function f(x) = h(x) - h(x * cos^2(theta)) to be maximized.
    Negative value returned for minimization.
    """
    term1 = binary_entropy(x)
    term2 = binary_entropy(x * np.cos(theta)**2)
    return -(term1 - term2)

def solve_holevo_optimization():
    theta_vals = np.linspace(0, np.pi/4, 200)
    optimal_x_values = []
    max_chi_values = []
    
    print(f"{'Theta (rad)':<15} | {'Optimal x':<15} | {'Max Holevo Chi':<15}")
    print("-" * 50)

    bounds = (np.finfo(float).eps, 1 - np.finfo(float).eps)
    
    for theta in theta_vals:
        res = minimize_scalar(
            objective_function, 
            args=(theta,), 
            bounds=bounds, 
            method='bounded'
        )
        
        if res.success:
            optimal_x = res.x
            max_chi = -res.fun 
            optimal_x_values.append(optimal_x)
            max_chi_values.append(max_chi)
        else:
            optimal_x_values.append(np.nan)
            max_chi_values.append(np.nan)

    for i in [0, len(theta_vals)//2, len(theta_vals)-1]:
        print(f"{theta_vals[i]:<15.4f} | {optimal_x_values[i]:<15.4f} | {max_chi_values[i]:<15.4f}")

    plt.figure(figsize=(10, 6))
    plt.subplot(1, 2, 1)
    plt.plot(theta_vals, max_chi_values, 'b-', linewidth=2, label=r'$\chi_{max}$')
    plt.xlabel(r'$\theta$ (radians)')
    plt.ylabel(r'Holevo Information (bits)')
    plt.title(r'Maximal Holevo Information ($\theta$)')
    plt.grid(True, linestyle='--', alpha=0.7)
    plt.legend()
    
    plt.subplot(1, 2, 2)
    plt.plot(theta_vals, optimal_x_values, 'r-', linewidth=2, label=r'$x_{opt}$')
    plt.xlabel(r'$\theta$ (radians)')
    plt.ylabel(r'Optimal probability $x$')
    plt.title(r'Optimal $x$ vs $\theta$')
    plt.grid(True, linestyle='--', alpha=0.7)
    plt.legend()
    
    plt.tight_layout()
    plt.savefig('holevo_optimization_results.png')
    plt.show()

    return theta_vals, optimal_x_values, max_chi_values

if __name__ == "__main__":
    # The model implements the function f(x) = h(x) - h(x * cos^2(theta)).
    try:
        thetas, xs, chis = solve_holevo_optimization()
        print("\nExecution successful. Results plotted.")
    except Exception as e:
        print(f"\nAn error occurred during execution: {e}")
```
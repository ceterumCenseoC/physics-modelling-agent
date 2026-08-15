

```python
import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import minimize
from scipy.stats import entropy

# ==========================================
# Model Implementation
# ==========================================

def binary_entropy(p, base=np.e):
    """
    Calculates the binary entropy h(p) = -p * log(p) - (1-p) * log(1-p).
    
    Arguments:
    p -- float or array, the probability (0 <= p <= 1)
    base -- the logarithm base (default np.e for nats)
    """
    # Clip to avoid log(0) errors
    p = np.clip(p, 1e-15, 1 - 1e-15)
    if base == 2:
        log_func = np.log2
    elif base == 10:
        log_func = np.log10
    else:
        log_func = np.log
        
    return -p * log_func(p) - (1 - p) * log_func(1 - p)

def get_density_matrix(gamma, theta, phi):
    """
    Constructs the density matrix rho_x as defined in the problem.
    
    Arguments:
    gamma -- float, parameter in [0, 1]
    theta -- float, angle in radians
    phi -- float, phase in radians
    
    Returns:
    numpy.ndarray -- 3x3 density matrix
    """
    # Calculate matrix elements as per the problem description
    c2 = np.cos(theta)**2
    s2 = np.sin(theta)**2
    cs = np.cos(theta) * np.sin(theta)
    sqrt_term = np.sqrt(1 - gamma)
    
    rho = np.array([
        [gamma * c2, 0, 0],
        [0, (1 - gamma) * c2, sqrt_term * cs * np.exp(1j * phi)],
        [0, sqrt_term * cs * np.exp(-1j * phi), s2]
    ], dtype=complex)
    
    return rho

def von_neumann_entropy(rho, base=np.e):
    """
    Calculates the von Neumann entropy S(rho) = -Tr(rho * log(rho)).
    
    Arguments:
    rho -- numpy.ndarray, density matrix (Hermitian, positive semi-definite, trace 1)
    base -- the logarithm base (default np.e for nats)
    
    Returns:
    float -- entropy in nats (or bits if base=2)
    """
    evals = np.linalg.eigvalsh(rho)
    # Evaluations to numerical precision might be slightly negative or zero
    evals = np.real(evals)
    evals = np.clip(evals, 1e-15, None)
    
    if base == 2:
        log_func = np.log2
    elif base == 10:
        log_func = np.log10
    else:
        log_func = np.log
        
    return -np.sum(evals * log_func(evals))

def calculate_holevo_numerical(gammas, phis, probs, theta):
    """
    Calculates the Holevo information numerically using the full density matrices.
    Chi = S(sum(p_x rho_x)) - sum(p_x S(rho_x))
    
    Arguments:
    gammas -- list/array of gamma parameters
    phis -- list/array of phi parameters
    probs -- list/array of probabilities
    theta -- float, angle parameter
    
    Returns:
    float -- The Holevo information (nats)
    """
    # 1. Calculate individual entropies
    individual_entropies = []
    rho_avg = np.zeros((3, 3), dtype=complex)
    
    for g, p, phi in zip(gammas, probs, phis):
        rho = get_density_matrix(g, theta, phi)
        
        # Accumulate average state
        rho_avg += p * rho
        
        # Compute S(rho_x)
        s_x = von_neumann_entropy(rho)
        individual_entropies.append(s_x)
        
    avg_entropy = np.sum(probs * np.array(individual_entropies))
    total_entropy = von_neumann_entropy(rho_avg)
    
    return total_entropy - avg_entropy

def f_analytical(x, theta):
    """
    The derived analytical function f(x) = cos^2(theta) * h(x).
    This is the single-variable function we are to optimize.
    
    Arguments:
    x -- float, probability variable in [0, 1]
    theta -- float, angle parameter
    
    Returns:
    float -- f(x)
    """
    return (np.cos(theta)**2) * binary_entropy(x)

# ==========================================
# Optimization and Visualization
# ==========================================

def run_optimization_and_print(theta_val):
    """
    Runs the optimization over x to find max f(x) and prints results.
    """
    cos_sq = np.cos(theta_val)**2
    
    # Objective function to maximize
    def objective(x):
        return -f_analytical(x, theta_val) # Negative for minimization

    # Constraints: x in [0, 1]
    bounds = [(0, 1)]
    
    # Initial guess: 0.5
    x0 = [0.5]
    
    print(f"--- Optimization Results for Theta = {theta_val:.4f} rad ---")
    
    # 1. Analytical Derivative/Intuition Check
    # Max of h(x) is at x=0.5, value is 1. Max of f(x) should be cos^2(theta).
    theory_x_opt = 0.5
    theory_max = f_analytical(theory_x_opt, theta_val)
    
    print(f"Theoretical Optimal x: {theory_x_opt}")
    print(f"Theoretical Max Value: {theory_max:.6f} nats")
    
    # 2. Numerical Optimization (Scipy)
    res = minimize(objective, x0, bounds=bounds, method='L-BFGS-B')
    
    print(f"Numerical Optimal x:   {res.x[0]:.6f}")
    print(f"Numerical Max Value:   {-res.fun:.6f} nats")
    print(f"Status:                {res.message}")
    print("-" * 50)
    
    return theory_max, res.x[0], -res.fun

def plot_results(theta_val, output_filename="holevo_optimization.png"):
    """
    Plots the function f(x) vs x for the given theta.
    """
    x_vals = np.linspace(0, 1, 200)
    y_vals = f_analytical(x_vals, theta_val)
    
    plt.figure(figsize=(8, 5))
    plt.plot(x_vals, y_vals, label=r'$f(x) = \cos^2(\theta) h(x)$', linewidth=2, color='blue')
    
    # Highlight maximum
    max_val = np.max(y_vals)
    max_x = 0.5
    plt.scatter([max_x], [max_val], color='red', zorder=5, label=f'Maximum at $x=0.5$')
    plt.annotate(f'{max_val:.4f}', xy=(max_x, max_val), xytext=(max_x+0.1, max_val),
                 arrowprops=dict(facecolor='black', arrowstyle='->'))

    plt.title(r'Holevo Information Optimization $\max_{x} f(x)$ for $\theta = {:.2f}$'.format(theta_val))
    plt.xlabel(r'$x$ (Probability parameter)')
    plt.ylabel(r'$\chi$ (Holevo Information in nats)')
    plt.grid(True, linestyle='--', alpha=0.7)
    plt.legend()
    
    plt.tight_layout()
    plt.savefig(output_filename)
    print(f"Plot saved to {output_filename}")

def verify_full_model(theta_val):
    """
    Verifies the full model (using density matrices) against the derived function.
    We construct the extremal ensemble: p=p for gamma=1, p=(1-p) for gamma=0.
    """
    print("--- Verifying Full Numerical Model ---")
    
    test_x = 0.3
    f_val = f_analytical(test_x, theta_val)
    print(f"Analytical f(x={test_x}): {f_val:.6f}")
    
    # Setup ensemble: 2 states
    # State 1: gamma=1, prob=test_x
    # State 2: gamma=0, prob=1-test_x
    # Phases: pi/2 and -pi/2 (to cancel off-diagonal terms as per theory)
    
    p = test_x
    gammas = [1.0, 0.0]
    phis = [np.pi/2, -np.pi/2] # Opposing phases to maximize avg entropy
    probs = [p, 1-p]
    
    chi_num = calculate_holevo_numerical(gammas, phis, probs, theta_val)
    print(f"Numerical Holevo:     {chi_num:.6f}")
    
    diff = abs(f_val - chi_num)
    print(f"Difference:           {diff:.8f}")
    
    if diff < 1e-6:
        print("Verification PASSED: Analytical model matches numerical implementation.")
    else:
        print("Verification WARNING: Mismatch detected.")
    print("-" * 50)

# ==========================================
# Main Execution
# ==========================================

if __name__ == "__main__":
    # 1. Setup Parameter
    # Using theta = pi/4 as discussed in realistic parameters
    theta_val = np.pi / 4 
    
    # 2. Run the optimization of function f(x)
    theoretical_max, opt_x, opt_val = run_optimization_and_print(theta_val)
    
    # 3. Verify against the full density matrix calculation
    verify_full_model(theta_val)
    
    # 4. Generate Graphics
    plot_results(theta_val)
```
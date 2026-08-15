
```python
import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp

# ==========================================
# 1. Model Definition & Parameters
# ==========================================

# The Majorana-Boson Model Lagrangian:
# L = (i/2)*chi_bar * gamma^mu * partial_mu * chi + (m / 2*pi*K) * (partial_mu * phi)^2
#     + (Delta/2) * i * chi_bar * chi * cos(2*m*phi)
#
# Beta Functions at one-loop level:
# x = [Delta] = 15/8 - K
# Beta_Delta = d(Delta)/d(ln(mu)) = x * Delta - (pi * K / 4) * Delta^3
# Beta_x     = d(x)/d(ln(mu))     = - (pi * K / 4) * Delta^2
#
# Defines the system of ODEs to be solved.

def compute_beta_functions(t, y, K):
    """
    Computes the beta functions for Delta and x.
    
    Args:
    t : float, independent variable (ln(mu)). 
        Note: t decreases from UV (high mu) to IR (low mu).
    y : array-like, [Delta, x]
    K : float, Luttinger parameter
        
    Returns:
    dydt : array-like, [d(Delta)/d(ln_mu), d(x)/d(ln_mu)]
    """
    Delta, x = y
    
    # Coefficient for the loop corrections derived from the OPE:
    # C = pi * K / 4
    C = (np.pi * K) / 4.0
    
    # Beta function for Delta
    # β_Δ = x * Δ - C * Δ^3
    dD_dt = x * Delta - C * (Delta**3)
    
    # Beta function for x
    # β_x = - C * Δ^2
    dx_dt = -C * (Delta**2)
    
    return [dD_dt, dx_dt]

# ==========================================
# 2. Numerical Solver (RG Flow)
# ==========================================

def run_rg_flow(K, Delta_init, mu_start=100.0, mu_end=0.01, num_points=500):
    """
    Integrates the beta functions from mu_start (UV) to mu_end (IR).
    
    Args:
    K : float, Luttinger parameter
    Delta_init : float, Initial value of Delta at mu_start
    mu_start : float, Starting energy scale (High Energy/UV)
    mu_end : float, Ending energy scale (Low Energy/IR)
    num_points : int, Number of points in the solution
    
    Returns:
    mu_vals : array, Energy scale values
    Delta_vals : array, Coupling constant values along flow
    x_vals : array, Scaling dimension values along flow
    """
    
    # Calculate initial x based on K
    # x = 15/8 - K
    x_init = (15.0 / 8.0) - K
    
    # Initial state vector [Delta, x]
    y0 = [Delta_init, x_init]
    
    # t represents ln(mu)
    t_start = np.log(mu_start)
    t_end = np.log(mu_end)
    t_span = (t_start, t_end)
    t_eval = np.linspace(t_start, t_end, num_points)
    
    # Solve ODE using Runge-Kutta 4(5)
    # We define the flow direction explicitly in t_span.
    # As we go from start to end, mu decreases (Space -> IR).
    sol = solve_ivp(
        fun=compute_beta_functions, 
        t_span=t_span, 
        y0=y0, 
        args=(K,), 
        t_eval=t_eval, 
        method='RK45',
        rtol=1e-8,
        atol=1e-8
    )
    
    mu_vals = np.exp(sol.t)
    Delta_vals = sol.y[0]
    x_vals = sol.y[1]
    
    return mu_vals, Delta_vals, x_vals

# ==========================================
# 3. Visualization
# ==========================================

def plot_results(mu_vals, Delta_vals, x_vals, K_val):
    """
    Plots the RG flow trajectories.
    """
    plt.figure(figsize=(14, 5))
    
    # Plot 1: Coupling Constants Flow
    plt.subplot(1, 2, 1)
    plt.plot(mu_vals, Delta_vals, label=r'$\Delta(\mu)$', color='blue', linewidth=2)
    plt.plot(mu_vals, x_vals, label=r'$x(\mu)$', color='green', linestyle='--', linewidth=2)
    
    plt.xscale('log')
    plt.gca().invert_xaxis()  # Standard RG convention: UV on left, IR on right
    plt.xlabel(r'Energy Scale $\mu$ (UV $\rightarrow$ IR)', fontsize=12)
    plt.ylabel('Coupling Value', fontsize=12)
    plt.title(r'RG Flow of $\Delta$ and $x$ for $K = {:.2f}$'.format(K_val), fontsize=14)
    plt.legend(fontsize=12)
    plt.grid(True, which="both", ls="-", alpha=0.3)
    
    # Plot 2: Beta Functions Along the Flow
    plt.subplot(1, 2, 2)
    
    # Recalculate beta along the trajectory for visualization
    # Array comprehension might be slow for large arrays, but fine for plotting (500 pts)
    beta_D_vals = []
    beta_x_vals = []
    for i in range(len(mu_vals)):
        d, x = Delta_vals[i], x_vals[i]
        C = (np.pi * K_val) / 4.0
        bD = x * d - C * (d**3)
        bx = -C * (d**2)
        beta_D_vals.append(bD)
        beta_x_vals.append(bx)
        
    plt.plot(mu_vals, beta_D_vals, label=r'$\beta_\Delta$', color='red', linewidth=2)
    plt.plot(mu_vals, beta_x_vals, label=r'$\beta_x$', color='purple', linestyle='--', linewidth=2)
    
    plt.xscale('log')
    plt.gca().invert_xaxis()
    plt.axhline(0, color='black', linewidth=0.8)
    plt.xlabel(r'Energy Scale $\mu$', fontsize=12)
    plt.ylabel('Beta Function Value', fontsize=12)
    plt.title(r'Evolution of Beta Functions $\beta(\Delta)$ and $\beta(x)$', fontsize=14)
    plt.legend(fontsize=12)
    plt.grid(True, which="both", ls="-", alpha=0.3)
    
    plt.tight_layout()
    plt.show()

# ==========================================
# 4. Main Execution
# ==========================================

if __name__ == "__main__":
    # Parameters based on physical analysis (Realistic Starting Parameters)
    # K = 0.5: Represents a strongly interacting Luttinger liquid.
    # At K=0.5, x = 15/8 - 0.5 = 1.375 > 0. 
    # A positive x implies the perturbation is relevant.
    
    K_val = 0.5
    
    # Initial coupling at high energy (UV).
    # We choose a small Delta (0.1) to ensure the perturbative expansion 
    # (one-loop) remains valid initially. 
    Delta_0 = 0.1 
    
    print(f"--- Simulation Configuration ---")
    print(f"Luttinger Parameter K: {K_val}")
    print(f"Initial Scaling Dimension x: {15/8 - K_val:.4f}")
    print(f"Initial Coupling Delta (UV): {Delta_0}")
    print(f"Formula: Beta_Delta = x*Delta - (pi*K/4)*Delta^3")
    print(f"Formula: Beta_x     = -(pi*K/4)*Delta^2")
    print("-" * 40)
    
    # Run the RG flow from UV (mu=100) to IR (mu=0.01)
    # Using a wide range to demonstrate the flow towards strong coupling
    mu_flow, Delta_flow, x_flow = run_rg_flow(K_val, Delta_0, mu_start=100.0, mu_end=0.001)

    # Check for overflow in results (singularity if Delta grows too fast)
    if np.any(np.isnan(Delta_flow)) or np.any(np.isinf(Delta_flow)):
        print("Warning: Singularity detected during integration (coupling diverged).")
        print("This is expected physically for relevant perturbations flowing to strong coupling.")
    
    # Display data headers
    print(f"{'ln(mu)':<12} {'mu':<15} {'Delta':<15} {'x':<15}")
    print("-" * 60)
    
    # Print a subset of data points (UV -> IR direction in the array)
    # However, our integration goes High T -> Low T, which is UV -> IR.
    step_size = len(mu_flow) // 10
    for i in range(0, len(mu_flow), step_size):
        print(f"{np.log(mu_flow[i]):<12.2f} {mu_flow[i]:<15.4e} {Delta_flow[i]:<15.4f} {x_flow[i]:<15.4f}")
    
    # Plot the results
    plot_results(mu_flow, Delta_flow, x_flow, K_val)
```
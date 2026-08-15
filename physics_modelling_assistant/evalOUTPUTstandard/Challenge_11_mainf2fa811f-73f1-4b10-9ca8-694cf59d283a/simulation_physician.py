
```python
import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint

# ==========================================
# 1. Model Definition & Parameters
# ==========================================

# The Majorana-Boson Model Lagrangian:
# L = (i/2)*chi_bar * gamma^mu * partial_mu * chi + (m / 2*pi*K) * (partial_mu * phi)^2
#     + (Delta/2) * i * chi_bar * chi * cos(2*m*phi)

# Derived Beta Functions at one-loop level:
# x = [Delta] = 15/8 - K
# Beta_Delta = d(Delta)/d(ln(mu)) = x * Delta - (pi * K / 4) * Delta^3
# Beta_x     = d(x)/d(ln(mu))     = - (pi * K / 4) * Delta^2

convention_positive_beta_strong_coupling = True
# Note: The problem states: "a positive beta function means that the system flows 
# to strong coupling in the IR". 
# Standard RG: t = ln(mu). d/dt flows UV (high t) -> IR (low t). 
# So positive beta (growth in t) means growth in UV. 
# Wait, "flows to strong coupling in the IR" usually means as energy scale decreases.
# Usually we define 푡 = ln(Λ/μ) so t increases in IR.
# Or we define 푡 = ln(μ). If beta > 0, g grows with μ. 
# If g grows with μ, then at low μ (IR), g is smaller.
# So "positive beta means strong coupling in IR" implies the specific definition 
# of t or the flow direction must be handled carefully.
# However, the standard formula is μ dg/dμ = β(g).
# If β > 0, g increases as μ increases (UV).
# If β > 0, g decreases as μ decreases (IR).
# The problem prompt might imply the physics phase (if x>0, it's relevant and flows to strong coupling).
# I will implement the standard differential equations:
# dy/dt = Beta(y) where t = ln(mu). 

def compute_beta_functions(y, K, pi=np.pi):
    """
    Computes the beta functions for Delta and x.
    
    Args:
    y : array-like, [Delta, x]
    K : float, Luttinger parameter
    pi : float, value of pi
    
    Returns:
    dydt : array-like, [d(Delta)/d(ln_mu), d(x)/d(ln_mu)]
    """
    Delta, x = y
    
    # Coefficient for the loop corrections
    # C = pi * K / 4
    C = (pi * K) / 4.0
    
    # Beta function for Delta
    # β_Δ = x * Δ - C * Δ^3
    dD_dt = x * Delta - C * (Delta**3)
    
    # Beta function for x
    # β_x = - C * Δ^2
    dx_dt = -C * (Delta**2)
    
    return np.array([dD_dt, dx_dt])

# ==========================================
# 2. Numerical Solver (RG Flow)
# ==========================================

def run_rg_flow(K, Delta_init, mu_start=10.0, mu_end=0.01, steps=1000):
    """
    Integrates the beta functions from mu_start to mu_end.
    Flow direction: UV (high mu) to IR (low mu).
    """
    
    # Calculate initial x based on K
    # x = 15/8 - K
    x_init = (15.0 / 8.0) - K
    y0 = [Delta_init, x_init]
    
    # t represents ln(mu)
    t_start = np.log(mu_start)
    t_end = np.log(mu_end)
    t = np.linspace(t_start, t_end, steps)
    
    # Solve ODE
    # Using a standard solver (RK4 equivalent via odeint)
    solution = odeint(compute_beta_functions, y0, t, args=(K,))
    
    Delta_sol = solution[:, 0]
    x_sol = solution[:, 1]
    
    return t, Delta_sol, x_sol

# ==========================================
# 3. Visualization
# ==========================================

def plot_results(t, Delta, x, K_val):
    plt.figure(figsize=(12, 5))
    
    # Convert t back to mu for nicer x-axis labels (log scale already handled by t linear spacing implies log mu)
    # Actually t is ln(mu), so we can just plot vs t or vs mu (log scale)
    mu = np.exp(t)
    
    # Plot 1: Beta Functions (Flow of Couplings)
    plt.subplot(1, 2, 1)
    plt.plot(mu, Delta, label=r'$\Delta(\mu)$', color='blue', linewidth=2)
    plt.plot(mu, x, label=r'$x(\mu)$', color='green', linestyle='--', linewidth=2)
    
    plt.xscale('log')
    plt.xlabel(r'Energy Scale $\mu$ (UV $\to$ IR)', fontsize=12)
    plt.ylabel('Coupling Value', fontsize=12)
    plt.title(r'RG Flow of $\Delta$ and $x$ for $K = {:.2f}$'.format(K_val), fontsize=14)
    plt.legend()
    plt.grid(True, alpha=0.3)
    
    # Plot 2: Beta values directly to see sign
    plt.subplot(1, 2, 2)
    # Recalculate beta along the trajectory
    betas = np.array([compute_beta_functions(y, K_val) for y in zip(Delta, x)])
    beta_D = betas[:, 0]
    beta_x = betas[:, 1]
    
    plt.plot(mu, beta_D, label=r'$\beta_\Delta$', color='red')
    plt.plot(mu, beta_x, label=r'$\beta_x$', color='purple')
    
    plt.xscale('log')
    plt.axhline(0, color='black', linewidth=0.8)
    plt.xlabel(r'Energy Scale $\mu$', fontsize=12)
    plt.ylabel('Beta Function Value', fontsize=12)
    plt.title(r'Beta Functions $\beta(\Delta)$ and $\beta(x)$', fontsize=14)
    plt.legend()
    plt.grid(True, alpha=0.3)
    
    plt.tight_layout()
    plt.show()

# ==========================================
# 4. Main Execution
# ==========================================

if __name__ == "__main__":
    # Parameters based on "Realistic Starting Parameters" section
    # K = 0.5 (deep in the relevant phase x > 0)
    K_val = 0.5
    
    # Initial coupling at high energy (UV)
    # Delta should be small for perturbative validity
    Delta_0 = 0.5 
    
    print(f"--- Simulation Parameters ---")
    print(f"Luttinger Parameter K: {K_val}")
    print(f"Initial x (scaling dimension): {15/8 - K_val:.3f}")
    print(f"Initial Delta (UV): {Delta_0}")
    print(f"Formula: Beta_Delta = x*Delta - (pi*K/4)*Delta^3")
    print(f"Formula: Beta_x     = -(pi*K/4)*Delta^2")
    print("-" * 30)
    
    # Run the RG flow from high mu to low mu
    # mu_start = 10 (UV), mu_end = 0.01 (IR)
    t_flow, Delta_flow, x_flow = run_rg_flow(K_val, Delta_0)
    
    # Output some data points
    print("Flow Trajectory (UV -> IR):")
    print(f"{'ln(mu)':<10} {'mu':<15} {'Delta':<15} {'x':<15}")
    print("-" * 50)
    for i in range(0, len(t_flow), len(t_flow)//10):
        print(f"{t_flow[i]:<10.2f} {np.exp(t_flow[i]):<15.4f} {Delta_flow[i]:<15.4f} {x_flow[i]:<15.4f}")
    
    # Generate Graphics
    plot_results(t_flow, Delta_flow, x_flow, K_val)
```
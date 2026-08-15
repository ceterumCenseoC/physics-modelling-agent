
```python
import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp

# ==========================================
# Model Definition and Beta Functions
# ==========================================

def beta_functions(l, y):
    """
    Computes the derivatives (RG equations) for the coupling g and scaling dimension x.
    
    Parameters:
    l (float): Log scale parameter, l = ln(mu_0 / mu). 
               Increasing l corresponds to moving towards the IR.
    y (list): Vector [g, x].
              g: Dimensionless coupling constant (Delta / mu)
              x: Scaling dimension of the operator [Delta]
              
    Returns:
    list: [dg/dl, dx/dl]
    """
    g, x = y
    
    # Beta function for g (coupling)
    # Based on the summary of the Majorana-Boson model:
    # dg/dl = (2 - x) * g
    dg_dl = (2.0 - x) * g
    
    # Beta function for x (scaling dimension)
    # Based on the correction derived in the Dimensional Analysis.
    # The dimensionally consistent form using the dimensionless coupling g is:
    # dx/dl = - (1 / 2*pi) * (x - 1)^2 * g^2
    coefficient = -1.0 / (2.0 * np.pi)
    dx_dl = coefficient * ((x - 1.0)**2) * (g**2)
    
    return [dg_dl, dx_dl]

# ==========================================
# Simulation Parameters
# ==========================================

# Initial conditions at the UV scale (l = 0)
# Based on the "Suggested Starting Parameters":
# g_0 = 0.1 (ensures perturbative validity at UV)
# x_0 = 1.8 (relevant operator, x < 2, close to criticality)
g_0 = 0.1
x_0 = 1.8
initial_state = [g_0, x_0]

# RG flow integration range
# We integrate from l=0 (UV) to l=10 (IR)
l_span = (0, 10)
l_eval = np.linspace(0, 10, 1000)

# ==========================================
# Numerical Integration
# ==========================================

print("Starting RG flow calculation...")
print(f"Initial Coupling g(0): {g_0}")
print(f"Initial Scaling Dimension x(0): {x_0}")

# Solve the ODEs
solution = solve_ivp(
    fun=beta_functions,
    t_span=l_span,
    y0=initial_state,
    t_eval=l_eval,
    method='RK45',
    rtol=1e-9,
    atol=1e-9
)

if not solution.success:
    print("Warning: Integration did not converge cleanly.")
    print(f"Message: {solution.message}")

g_sol = solution.y[0]
x_sol = solution.y[1]
l_sol = solution.t

# ==========================================
# Visualization
# ==========================================

plt.figure(figsize=(12, 5))

# Plot 1: Flow of Coupling g
plt.subplot(1, 2, 1)
plt.plot(l_sol, g_sol, label=r'$g(\ell)$', color='blue', linewidth=2)
plt.xlabel(r'RG Scale $\ell = \ln(\mu_0/\mu)$', fontsize=12)
plt.ylabel(r'Coupling $g = \Delta/\mu$', fontsize=12)
plt.title(r'RG Flow of Coupling Constant', fontsize=14)
plt.grid(True, alpha=0.3)
plt.yscale('log') # Using log scale to visualize the rapid growth to strong coupling

# Annotation for strong coupling divergence
if g_sol[-1] > 10 * g_0:
    plt.text(l_sol[-1] * 0.6, max(g_sol) * 0.1, r'$\to \infty$ (Strong Coupling)', fontsize=10)

# Plot 2: Flow of Scaling Dimension x
plt.subplot(1, 2, 2)
plt.plot(l_sol, x_sol, label=r'$x(\ell)$', color='red', linewidth=2)
# Add a line for the critical dimension x=2
plt.axhline(y=2, color='black', linestyle='--', alpha=0.6, label=r'Marginality ($x=2$)')
plt.xlabel(r'RG Scale $\ell = \ln(\mu_0/\mu)$', fontsize=12)
plt.ylabel('Scaling Dimension $x$', fontsize=12)
plt.title(r'RG Flow of Scaling Dimension', fontsize=14)
plt.grid(True, alpha=0.3)
# Set y-limits to focus on the relevant region
plt.ylim(0.5, 2.1) 
plt.legend(fontsize=12)

plt.tight_layout()
plt.show()

# ==========================================
# Interpretation of Results
# ==========================================

print("\n--- Analysis of Results ---")
if g_sol[-1] > 5 * g_0:
    print("Behavior: The coupling g is growing significantly in the IR.")
    print("This indicates the interaction is relevant and flows to a strong-coupling fixed point.")
else:
    print("Behavior: The coupling g remains small or decreases.")

if len(x_sol) > 0 and x_sol[-1] < x_0:
    print("Effect on x: The scaling dimension x is decreasing.")
    print("Reason: The bosonic stiffness K is being renormalized (screened) by fermion loop corrections.")
    print("Trend: A decreasing x (below 2) increases the factor (2-x) in beta(g), accelerating the flow.")
elif len(x_sol) > 0:
    print("Effect on x: The scaling dimension x did not decrease as expected or remained constant.")
```
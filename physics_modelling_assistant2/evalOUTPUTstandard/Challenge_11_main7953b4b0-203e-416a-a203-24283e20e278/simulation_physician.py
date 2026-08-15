
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
    l (float): log scale parameter, l = ln(mu_0 / mu). 
               Increasing l corresponds to moving towards the IR.
    y (list): Vector [g, x].
              g: dimensionless coupling constant (Delta / mu)
              x: scaling dimension of the operator [Delta]
              
    Returns:
    list: [dg/dl, dx/dl]
    """
    g, x = y
    
    # Beta function for g (coupling)
    # beta(g) = (2 - x) * g
    # Note: l = ln(mu_0/mu) -> d/dl = -mu d/dmu.
    # If beta通常定义为 mu d/dmu, then d/dl = -beta.
    # Here we follow the convention in the prompt analysis where l is defined 
    # such that flow towards IR is positive evolution.
    # Analysis text: "increasing l corresponds to moving towards the IR"
    # Text eqs: d(eps)/dl = (2-x)eps (where eps is delta).
    # We implement exactly as described in the summary: 
    # d(Delta)/dl ~ (2-x)Delta. For dimensionless g: dg/dl = (2-x)g.
    
    dg_dl = (2.0 - x) * g
    
    # Beta function for x (scaling dimension)
    # The dimensional analysis found that the formula -Delta^2/4pi is dimensionally inconsistent
    # if Delta is dimensionful. Using the dimensionless coupling g = Delta / mu:
    # The text suggests a form proportional to -g^2 or -(x-1)^2 g^2.
    # We use the refined form from the context:
    # beta(x) = - (1/4pi) * power(x-1, 2) * power(g, 2) ?
    # Actually, the text in "Dimensional Analysis" section suggests:
    # beta(x) = - 1/(2*pi) * (x-1)^2 * Delta^2 / mu^2 (Corrected for units)
    # Since g = Delta/mu, this becomes:
    # beta(x) = - 1/(2*pi) * (x-1)^2 * g^2
    
    # The first section gave a simpler version: beta(x) = -Delta^2/4pi -> -g^2/4pi (implicit units)
    # The second section (Majorana-Boson Summary) derived:
    # dx/dl = - 1/(2*pi) * (x-1)^2 * Delta^2.
    # We will use this more detailed form as it links x back to K and includes the (x-1)^2 dependence.
    
    coefficient = -1.0 / (2.0 * np.pi)
    dx_dl = coefficient * ((x - 1.0)**2) * (g**2)
    
    return [dg_dl, dx_dl]

# ==========================================
# Simulation Parameters
# ==========================================

# Initial conditions at UV scale (l = 0)
# Based on "Suggested Starting Parameters" section:
# g_0 = 0.1 (perturbative regime)
# x_0 = 1.8 (relevant operator, distinct from 2)
g_0 = 0.1
x_0 = 1.8
initial_state = [g_0, x_0]

# RG flow integration range
# l goes from 0 (UV) to some positive number (IR)
l_span = (0, 10)  # We intend to flow 10 decades
l_eval = np.linspace(0, 10, 1000)

# ==========================================
# Numerical Integration
# ==========================================

print("Starting RG flow calculation...")
print(f"Initial Coupling g(0): {g_0}")
print(f"Initial Scaling Dimension x(0): {x_0}")

solution = solve_ivp(
    fun=beta_functions,
    t_span=l_span,
    y0=initial_state,
    t_eval=l_eval,
    method='RK45',
    rtol=1e-8,
    atol=1e-8
)

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
plt.yscale('log') # Log scale is often better for coupling flows
plt.legend(fontsize=12)

# Add annotation for strong coupling divergence
# Find where g explodes
if g_sol[-1] > 10:
    plt.text(l_sol[-1]*0.7, max(g_sol)*0.1, r'$\to \infty$ (Strong Coupling)', fontsize=10)

# Plot 2: Flow of Scaling Dimension x
plt.subplot(1, 2, 2)
plt.plot(l_sol, x_sol, label=r'$x(\ell)$', color='red', linewidth=2)
plt.axhline(y=2, color='black', linestyle='--', alpha=0.6, label=r'Marginality ($x=2$)')
plt.xlabel(r'RG Scale $\ell = \ln(\mu_0/\mu)$', fontsize=12)
plt.ylabel('Scaling Dimension $x$', fontsize=12)
plt.title(r'RG Flow of Scaling Dimension', fontsize=14)
plt.grid(True, alpha=0.3)
plt.ylim(0.5, 2.1) # Zoom in to see the cross over near 2
plt.legend(fontsize=12)

plt.tight_layout()
plt.show()

# ==========================================
# Interpretation of Results
# ==========================================

print("\n--- Analysis of Results ---")
if g_sol[-1] > 5 * g_0:
    print("Behavior: The coupling g is growing significantly in the IR.")
else:
    print("Behavior: The coupling g remains small or decreases.")

if x_sol[-1] < x_0:
    print("Effect on x: The scaling dimension x is decreasing.")
    print("Reason: The bosonic stiffness K is being renormalized (screened) by fermion loop corrections.")
    
    # Check if it crosses the relevance threshold (x=2)
    # Though we started at x=1.8, let's verify the trend
    print("Trend: A decreasing x (below 2) increases the factor (2-x) in beta(g), accelerating the flow.")
else:
    print("Effect on x: The scaling dimension x is increasing.")
```
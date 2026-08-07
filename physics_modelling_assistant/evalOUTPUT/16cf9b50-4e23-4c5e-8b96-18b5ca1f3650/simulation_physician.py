```python
import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp

# 1. Model Constants
# Based on the dimension and perturbation analysis, we select parameters 
# that ensure a relevant perturbation in a perturbative regime.
m = 1.0              # Compactification parameter (Integer/Z2 symmetry)
K = 0.25             # Luttinger parameter (Strong interactions, K < 0.5 for relevance with m=1)
mu = 1.0             # Reference scale (set to 1.0 for dimensionless units relative to cutoff)

# 2. Tree-Level Scaling Dimension (x)
# Derived from the Lagrangian: [Delta] = x = 1 - 2mK
x_initial = 1 - 2 * m * K

# 3. Initial Conditions
# We start with a small dimensionless coupling in the perturbative regime.
Delta_tilde_0 = 0.1  # Initial dimensionless coupling
Delta_0 = Delta_tilde_0 * (mu ** x_initial)

print(f"Model Parameters:")
print(f"  m (compactification): {m}")
print(f"  K (Luttinger param):  {K}")
print(f"  mu (reference scale): {mu}")
print(f"Initial State:")
print(f"  x (scaling dimension): {x_initial:.4f}")
print(f"  Delta (dimensionful):  {Delta_0:.4f}")

# 4. Beta Functions
# System of ODEs derived from the model:
# beta_Delta = x * Delta - 0.5 * Delta^2
# beta_x     = -Delta * mu^(-x) 
def rg_equations(t, y, mu):
    """
    Computes the derivatives for the RG flow.
    t: log(mu) (integration parameter)
    y: array [Delta, x]
    mu: reference mass scale
    """
    Delta, x = y
    
    # Calculate Dimensionless coupling
    Delta_tilde = Delta * (mu ** (-x))
    
    # Beta functions
    dDelta_dt = x * Delta - 0.5 * Delta**2
    dx_dt     = -Delta * (mu ** (-x))
    
    return [dDelta_dt, dx_dt]

# 5. Integration
# We integrate from t=0 (UV, mu=1) down to t=-10 (IR).
# Note: d/dt = - d/d(ln mu) is a common convention, but here we defined
# d/dt = mu d/dmu (increasing t -> increasing mu). 
# To flow to the IR (mu -> 0), we integrate backwards in t (from 0 to negative).

t_span = (0, -10)  # Flow from UV (t=0) to IR (t=-10)
t_eval = np.linspace(0, -10, 500)

sol = solve_ivp(
    fun=lambda t, y: rg_equations(t, y, mu),
    t_span=t_span,
    y0=[Delta_0, x_initial],
    t_eval=t_eval,
    method='RK45'
)

# 6. Visualization
# Plot the RG flow trajectories for Delta(t) and x(t)
plt.figure(figsize=(12, 5))

# Plot for Delta
plt.subplot(1, 2, 1)
plt.plot(sol.t, sol.y[0], label=r'$\Delta(t)$', color='blue', linewidth=2)
plt.xlabel(r'$t = \ln(\mu)$', fontsize=12)
plt.ylabel(r'Coupling $\Delta$', fontsize=12)
plt.title(r'Flow of Coupling $\Delta$', fontsize=14)
plt.grid(True, linestyle='--', alpha=0.6)
plt.legend(fontsize=12)
# Annotate direction
plt.annotate('Flow to IR', xy=(-8, sol.y[0][-1]), xytext=(-5, sol.y[0][0]),
             arrowprops=dict(facecolor='black', arrowstyle='->'), fontsize=12)

# Plot for x
plt.subplot(1, 2, 2)
plt.plot(sol.t, sol.y[1], label=r'$x(t)$', color='red', linewidth=2)
plt.xlabel(r'$t = \ln(\mu)$', fontsize=12)
plt.ylabel(r'Scaling Dimension $x$', fontsize=12)
plt.title(r'Flow of Scaling Dimension $x$', fontsize=14)
plt.grid(True, linestyle='--', alpha=0.6)
plt.legend(fontsize=12)
# Annotate direction
plt.annotate('Flow to IR', xy=(-8, sol.y[1][-1]), xytext=(-5, sol.y[1][0]),
             arrowprops=dict(facecolor='black', arrowstyle='->'), fontsize=12)

plt.tight_layout()
plt.show()

# 7. Code Template Output (as requested)
print("\n--- Code Template Output ---")
# Extract final state values for the template
Delta_final_code = sol.y[0][-1]
x_final_code = sol.y[1][-1]

# Note: The template usually implies the functional form.
beta_Delta_template = "x * Delta - 0.5 * Delta**2"
beta_x_template = "-Delta * mu**(-x)"

print(f"beta_Delta = {beta_Delta_template}")
print(f"beta_x     = {beta_x_template}")

# Final numerical check
print("\nFinal Numerical Check (IR limit):")
print(f"Final Delta: {Delta_final_code:.4e}")
print(f"Final x:     {x_final_code:.4e}")
```
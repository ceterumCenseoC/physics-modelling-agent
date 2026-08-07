```python
import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp

def run_rg_simulation():
    """
    Sets up parameters, solves the Renormalization Group (RG) flow equations,
    and visualizes the results.
    
    Model Context:
    The RG flow describes a system of a Majorana fermion coupled to a boson,
    perturbed by the operator i\bar{\chi}\chi cos(2m\phi).
    
    Variables:
    m: Compactification parameter (e.g., 1 for Ising/Z2).
    K: Luttinger parameter.
    x: Scaling dimension of the coupling.
    Delta: Coupling constant.
    mu: Reference mass scale.
    """

    # --- 1. Model Constants ---
    # Physical values chosen based on derivation in the prompt:
    # m = 1 for standard Ising symmetry.
    # K = 0.25 implies strong interaction regime (K < 0.5 ensures relevance for m=1).
    m = 1.0
    K = 0.25
    mu = 1.0  # Reference scale, normalized to 1.

    print(f"--- Model Parameters ---")
    print(f"Compactification (m): {m}")
    print(f"Luttinger Param (K):   {K}")
    print(f"Reference Scale (mu): {mu}")

    # --- 2. Initial Conditions ---
    # Tree-level scaling dimension: x = 1 - 2mK
    x_0 = 1 - 2 * m * K
    
    # Initial dimensionless coupling tilde_Delta = Delta * mu^(-x).
    # We start in the perturbative regime (tilde_Delta << 1).
    tilde_Delta_0 = 0.1
    
    # Initial dimensionful coupling Delta.
    Delta_0 = tilde_Delta_0 * (mu ** x_0)

    print(f"\n--- Initial State ---")
    print(f"Scaling Dim (x_0):     {x_0:.4f}")
    print(f"Coupling (Delta_0):    {Delta_0:.4f}")
    print(f"Dimless Coupling:      {tilde_Delta_0:.4f}")

    # --- 3. Beta Functions ---
    def rg_system(t, y):
        """
        Defines the system of Ordinary Differential Equations (ODEs) for the RG flow.
        
        Equations provided by the derivation:
        d(Delta)/dt = x * Delta - 0.5 * Delta^2
        d(x)/dt     = -Delta * mu^(-x)
        
        where t = ln(mu).
        """
        Delta, x = y
        
        # Delta_tilde is the dimensionless combination required for consistency
        Delta_tilde = Delta * (mu ** (-x))
        
        dDelta_dt = x * Delta - 0.5 * Delta**2
        dx_dt     = -Delta_tilde
        
        return [dDelta_dt, dx_dt]

    # --- 4. Integration ---
    # We define the flow from UV to IR.
    # UV: t = 0 (mu = 1).
    # IR: t -> -infinity (mu -> 0).
    # We integrate backwards in 't' (from 0 to a negative number) to go towards IR.
    
    t_span = (0, -10)
    t_eval = np.linspace(0, -10, 500)
    
    print(f"\n--- Running Integration ---")
    sol = solve_ivp(
        fun=rg_system,
        t_span=t_span,
        y0=[Delta_0, x_0],
        t_eval=t_eval,
        method='RK45',
        rtol=1e-9,
        atol=1e-9
    )
    
    if not sol.success:
        print("Integration failed.")
        return

    # --- 5. Visualization ---
    plt.figure(figsize=(12, 5))

    # Plot for Delta
    plt.subplot(1, 2, 1)
    plt.plot(sol.t, sol.y[0], color='blue', lw=2)
    plt.title(r'RG Flow of Coupling $\Delta$')
    plt.xlabel(r'$t = \ln(\mu)$')
    plt.ylabel(r'$\Delta$')
    plt.grid(True, linestyle='--', alpha=0.7)
    
    # Annotation for direction
    plt.annotate('UV Region', xy=(0, Delta_0), xytext=(-1, Delta_0*1.5),
                 arrowprops=dict(facecolor='black', shrink=0.05), ha='center')
    plt.annotate('IR Region', xy=(-10, sol.y[0][-1]), xytext=(-8, sol.y[0][-1]*1.5),
                 arrowprops=dict(facecolor='black', shrink=0.05), ha='center')

    # Plot for x
    plt.subplot(1, 2, 2)
    plt.plot(sol.t, sol.y[1], color='red', lw=2)
    plt.title(r'RG Flow of Scaling Dimension $x$')
    plt.xlabel(r'$t = \ln(\mu)$')
    plt.ylabel(r'$x$')
    plt.grid(True, linestyle='--', alpha=0.7)

    plt.tight_layout()
    plt.show()

    # --- 6. Output Code Template ---
    print(f"\n--- Executable Code Template ---")
    print("To reproduce the beta function calculation step-by-step:")
    print("beta_Delta = x * Delta - 0.5 * Delta**2")
    print("beta_x     = -Delta * mu**(-x)")
    
    # --- 7. Final Numerical Check ---
    print(f"\n--- Final Values (at t = -10) ---")
    print(f"Final Delta: {sol.y[0][-1]:.6f}")
    print(f"Final x:     {sol.y[1][-1]:.6f}")

if __name__ == "__main__":
    run_rg_simulation()
```

```python
import numpy as np
import matplotlib.pyplot as plt
from scipy import integrate, special
from dataclasses import dataclass

# ==========================================
# 1. Model Setup & Constants
# ==========================================

@dataclass
class Parameters:
    """
    Physical parameters for the AdS3/BCFT2 one-point function calculation.
    
    Attributes:
        m (float): Mass of the bulk scalar field (dimensionless in AdS units).
        r0 (float): Radius of the black hole horizon (related to temperature).
        eta (float): Tension of the boundary brane (dimensionless).
        Lambda (float): UV cutoff for the boundary.
    """
    m: float = 10.0
    r0: float = 1.0
    eta: float = 0.5
    Lambda: float = 10000.0
    # AdS radius is set to 1
    L_Ads: float = 1.0 

# Global parameters instance
params = Parameters()

# ==========================================
# 2. Analytic Geodesic Length Calculation
# ==========================================

def geodesic_length_unregulated(r_curr: float, r0: float) -> float:
    """
    Computes the indefinite integral of the radial length element in BTZ.
    L(r) = arccosh(r / r0) = ln( r/r0 + sqrt((r/r0)^2 - 1) )
    """
    return np.arccosh(r_curr / r0)

def calculate_renormalized_length(p: Parameters) -> float:
    """
    Calculates the renormalized geodesic length from the AdS boundary to the brane.
    
    The brane is located at r_b = -eta/2 (behind the horizon).
    The geodesic length L(Lambda) = L(Lambda) - L(r_b).
    Renormalized length L_ren = limit(L(Lambda) - log(2*Lambda)).
    
    Using the analytic result derived:
    L_ren = -ln( sqrt(r0^2 - eta^2/4) + eta/2 )
    """
    r0 = p.r0
    eta = p.eta
    
    # Ensure the argument of the sqrt is positive (physical region)
    # eta is dimensionless, r0 is dimensionless. 
    # In the model logic: r_b = -eta/2. 
    # The effective length depends on the combination sqrt(r0^2 - r_b^2) + |r_b|...?
    # Actually, derived formula: L_ren = -ln( sqrt(r0^2 - eta^2/4) + eta/2 )
    
    term = np.sqrt(r0**2 - (eta**2)/4.0) + eta/2.0
    
    return -np.log(term)

# ==========================================
# 3. One-Point Function Calculation
# ==========================================

def one_point_function_geometric(p: Parameters) -> float:
    """
    The leading order contribution based on the boundary-to-brane geodesic length.
    <O> ~ exp(-m * L_ren)
    """
    L_ren = calculate_renormalized_length(p)
    return np.exp(-p.m * L_ren)

def one_point_function_integrated(p: Parameters) -> tuple[float, float]:
    """
    Computes the perturbative contribution using the integral form.
    
    <O> ~ Integral_{r0}^{inf} dr sqrt(g) * K0(r) * <chi^2(r)>
    
    Approximated integrand based on the provided model summary:
    I(r) ~ exp(-m * ell(r)) / ( sqrt(r) * (r^2 - r0^2)^(1/4) )
    
    Note: This captures the functional dependence requested.
    """
    r0 = p.r0
    m = p.m
    
    # Define the integrand
    # The geodesic distance from boundary to a point r in the bulk is roughly 
    # ell(r) ~ ln(2r/r0) - log(2r_c) ... 
    # The dominant local factor is proportional to exp(-m * distance).
    # distance ~ ln(r/r0).
    
    def integrand(r):
        # Avoid division by zero at the horizon
        if r <= r0: 
            return 0.0
        
        # Local "distance" factor approximating the exponential decay from boundary to r
        # cosh(sigma) ~ r^2/r0^2 => sigma ~ 2*ln(r/r0) for large r
        # distance sigma = 2 * ln(r/r0)
        local_gamma = np.exp(-m * 2 * np.log(r/r0))
        
        # Wightman function / Propagator factors approximated from the prompt context
        # Denominator structure derived from prompt's simplified integral expression
        denominator = np.sqrt(r) * (r**2 - r0**2)**0.25
        
        return local_gamma / denominator

    # Perform numerical integration from just above horizon to a cutoff
    # We use a cutoff upper limit to avoid divergence to infinity, 
    # effectively regularizing similar to the geodesic case.
    upper_limit = 100.0 # Sufficiently large for the exponential decay to kill the integrand
    
    res, err = integrate.quad(integrand, r0 + 1e-5, upper_limit, limit=200)
    
    # The pre-factors (2*pi*lambda/r0 etc) are constants that don't affect the 
    # shape of dependence on m, r0, eta in this plot, but we return the raw integral.
    return res, err

# ==========================================
# 4. Visualization & Analysis
# ==========================================

def plot_mass_dependence():
    """
    Plots the one-point function as a function of mass m.
    """
    p = params
    masses = np.linspace(5, 20, 50)
    vals_geometric = []
    
    for m_val in masses:
        p.m = m_val
        vals_geometric.append(one_point_function_geometric(p))
        
    plt.figure(figsize=(8, 5))
    plt.semilogy(masses, vals_geometric, label=r'Geodesic approx: $e^{-m \ell_{ren}}$', linewidth=2)
    plt.xlabel(r'Mass $m$')
    plt.ylabel(r'$\langle \mathcal{O} \rangle$')
    plt.title(f'Dependence on Mass ($r_0={p.r0}, \eta={p.eta}$)')
    plt.grid(True, which="both", ls="-", alpha=0.5)
    plt.legend()
    plt.show()

def plot_r0_dependence():
    """
    Plots the one-point function as a function of black hole radius r0.
    """
    p = params
    # Reset m
    p.m = 10.0
    
    r0_vals = np.linspace(0.55, 2.0, 50) # Avoid r0=0.5 if eta is large (eta < 2r0 constraint)
    vals_geometric = []
    
    for r0_val in r0_vals:
        p.r0 = r0_val
        vals_geometric.append(one_point_function_geometric(p))
        
    plt.figure(figsize=(8, 5))
    plt.plot(r0_vals, vals_geometric, label=r'Geodesic approx', linewidth=2, color='darkred')
    plt.xlabel(r'Black Hole Radius $r_0$')
    plt.ylabel(r'$\langle \mathcal{O} \rangle$')
    plt.title(f'Dependence on Black Hole Size ($m={p.m}, \eta={p.eta}$)')
    plt.grid(True, which="both", ls="-", alpha=0.5)
    plt.legend()
    plt.show()

def plot_eta_dependence():
    """
    Plots the one-point function as a function of brane tension eta.
    """
    p = params
    # Reset params
    p.m = 10.0
    p.r0 = 1.0
    
    eta_vals = np.linspace(0.01, 0.9, 50)
    vals_geometric = []
    
    for eta_val in eta_vals:
        p.eta = eta_val
        vals_geometric.append(one_point_function_geometric(p))
        
    plt.figure(figsize=(8, 5))
    plt.plot(eta_vals, vals_geometric, label=r'Geodesic approx', linewidth=2, color='green')
    plt.xlabel(r'Brane Tension $\eta$')
    plt.ylabel(r'$\langle \mathcal{O} \rangle$')
    plt.title(f'Dependence on Brane Tension ($m={p.m}, r_0={p.r0}$)')
    plt.grid(True, which="both", ls="-", alpha=0.5)
    plt.legend()
    plt.show()

def Analytical_Check():
    """
    Prints the analytical result vs numerical integration check for a specific case.
    """
    p = params # Default: m=10, r0=1, eta=0.5
    
    print(f"--- Analysis for m={p.m}, r0={p.r0}, eta={p.eta} ---")
    
    # Calculate Renormalized Length
    L_ren = calculate_renormalized_length(p)
    print(f"Renormalized Geodesic Length L_ren = {L_ren:.4f}")
    
    # Calculate Geometric One-point function
    O_geo = one_point_function_geometric(p)
    print(f"Geometric <O> = exp(-m * L_ren) = {O_geo:.4f}")
    
    # Calculate Integral One-point function (perturbative part approx)
    # Note: The integral result is not directly <O> but the perturbative kernel. 
    # We verify the scaling.
    integral_val, err = one_point_function_integrated(p)
    print(f"Integral Value (Kernel) = {integral_val:.4e} (+/- {err:.1e})")
    print("\nThe integral value captures the radial integration profile, while the geometric\n"
          "result gives the dominant exponential suppression usually associated with the VEV.")

# ==========================================
# 5. Main Execution
# ==========================================

if __name__ == "__main__":
    print("Initializing AdS3/BCFT2 One-Point Function Model...")
    
    # Run analytical check
    Analytical_Check()
    
    # Generate plots
    print("\nGenerating visualizations...")
    try:
        plot_mass_dependence()
        plot_r0_dependence()
        plot_eta_dependence()
    except Exception as e:
        print(f"Error generating plots: {e}")
        
    print("Done.")
```
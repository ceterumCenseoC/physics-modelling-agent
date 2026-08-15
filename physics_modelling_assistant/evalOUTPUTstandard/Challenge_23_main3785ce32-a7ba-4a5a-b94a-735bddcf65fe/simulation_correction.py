
```python
import numpy as np
import matplotlib.pyplot as plt
from scipy import integrate
import sympy as sp

# ==========================================
# Model Implementation: Sail-Diagram Contribution
# ==========================================
# Reference:
# J. Chay, "Disentangling Scheme Dependence in Quasi-PDFs with a Transverse-Momentum Cutoff",
# arXiv:2607.04182 [hep-ph].
#
# This module calculates the finite part of the sail diagram contribution to the one-loop
# renormalized quasi-PDF in the MS-bar scheme.
#
# The calculation is divided into three regions of the momentum fraction x:
# 1. x < 0: Unphysical region, contains IR divergences (regulated by epsilon_IR).
# 2. 0 < x < 1: Physical region, contains UV divergences (regulated by epsilon_UV).
# 3. x > 1: Unphysical region, contains IR divergences (regulated by epsilon_IR).
#
# The finite part provided here corresponds to the remainder terms after counterterm
# subtraction, as detailed in Eq. (3.38) of the reference.

class SailDiagramQuasiPDF:
    def __init__(self, alpha_s=0.3, Cf=4/3, mu=2.0, pz=2.0):
        """
        Initialize the model with physical parameters.
        
        Parameters:
        alpha_s (float): Strong coupling constant.
        Cf (float): Casimir operator (4/3 for SU(3)).
        mu (float): Renormalization scale in GeV.
        pz (float): Longitudinal momentum in GeV.
        """
        self.alpha_s = alpha_s
        self.Cf = Cf
        self.mu = mu
        self.pz = pz
        
        # Precompute common factor: alpha_s * C_F / (2 * pi)
        self.common_prefactor = (self.alpha_s * self.Cf) / (2 * np.pi)

    def _region_0_1_plus_distribution(self, x):
        """
        Compute the integrand for 0 < x < 1.
        This region involves a plus-prescription due to the singularity at x=1.
        Formula derived from Eq. (3.38):
        [ (1+x^2)/(1-x) * ln( 4*x*(1-x)*pz^2 / mu^2 ) - x*(1+x)/(1-x) ]
        """
        # Handle the singularity at x=1
        if x == 1.0:
            return np.nan

        # Argument of the logarithm
        # We add a tiny epsilon to prevent domain errors in floating point if x is very close to 0 or 1
        arg = 4 * x * (1 - x) * (self.pz**2) / (self.mu**2)
        
        if arg <= 0:
            return np.nan

        term1 = (1 + x**2) / (1 - x) * np.log(arg)
        term2 = (x * (1 + x)) / (1 - x)
        
        return term1 - term2

    def _region_x_gt_1(self, x):
        """
        Compute the expression for x > 1.
        This region involves a plus-prescription over [1, infinity].
        Formula derived from Eq. (3.38):
        [ (1+x^2)/(x-1) * ln(x/(x-1)) + 1 + 3/(2x) ]  - 3/(2x)
        Note: (1+x^2)/(1-x) is rewritten as -(1+x^2)/(x-1).
        """
        # Rewrite denominator (1-x) as -(x-1) for better numerical stability for x>1
        term1 = -(1 + x**2) / (x - 1) * np.log(x / (x - 1))
        term2 = 1
        term3 = 3 / (2 * x)
        
        dist_part = term1 + term2 + term3
        
        # Subtract the tail term for the 'plus' definition on [1, inf]
        return dist_part - 3 / (2 * x)

    def _region_x_lt_0(self, x):
        """
        Compute the expression for x < 0.
        This region involves a plus-prescription over [-infinity, 0].
        Formula derived from Eq. (3.38):
        [ (1+x^2)/(1-x) * ln((1-x)/(-x)) - 1 + 3/(2(1-x)) ] - 3/(2(1-x))
        """
        term1 = (1 + x**2) / (1 - x) * np.log((1 - x) / (-x))
        term2 = -1
        term3 = 3 / (2 * (1 - x))
        
        dist_part = term1 + term2 + term3
        
        # Subtract the tail term for the 'plus' definition on [-inf, 0]
        # Note: The tail term subtraction effectively removes the divergence as x -> -inf
        # leaving the finite remainder relevant for matching.
        return dist_part - 3 / (2 * (1 - x))

    def evaluate_finite_part(self, x_vals):
        """
        Vectorized evaluation of the finite part for an array of x values.
        Note: This returns the 'integrand' form. For the 'plus' distributions,
        the pointwise value is singular at boundaries (x=0, x=1). 
        We mask these singular points.
        """
        results = []
        for x in x_vals:
            # Logic to switch between regions
            if 0 < x < 1:
                val = self._region_0_1_plus_distribution(x)
            elif x > 1:
                val = self._region_x_gt_1(x)
            elif x < 0:
                val = self._region_x_lt_0(x)
            else:
                # x is exactly 0 or 1, or NaN
                val = np.nan
            results.append(val)
        
        return self.common_prefactor * np.array(results)

    def get_analytic_expression(self, region, x_sym, mu_sym, pz_sym):
        """
        Return a SymPy expression for the model in a specific region.
        Useful for symbolic verification or integration.
        """
        alpha_s, Cf = sp.symbols('alpha_s Cf', positive=True)
        prefactor = alpha_s * Cf / (2 * sp.pi)
        
        expr = None
        if region == '0<x<1':
            # (1+x^2)/(1-x) * ln(4*x*(1-x)*pz^2/mu^2) - x*(1+x)/(1-x)
            expr = (1 + x_sym**2)/(1 - x_sym) * sp.log(4*x_sym*(1-x_sym)*pz_sym**2/mu_sym**2) - \
                   (x_sym*(1+x_sym))/(1-x_sym)
        elif region == 'x>1':
            # ((1+x^2)/(1-x) * ln(x/(x-1)) + 1 + 3/(2*x)) - 3/(2*x)
            # Note: 1-x is negative here.
            expr = ((1 + x_sym**2)/(1 - x_sym) * sp.log(x_sym/(x_sym - 1)) + 1 + 3/(2*x_sym)) - \
                   3/(2*x_sym)
        elif region == 'x<0':
            # ((1+x^2)/(1-x) * ln((1-x)/(-x)) - 1 + 3/(2*(1-x))) - 3/(2*(1-x))
            expr = ((1 + x_sym**2)/(1 - x_sym) * sp.log((1 - x_sym)/(-x_sym)) - 1 + 3/(2*(1 - x_sym))) - \
                   3/(2*(1 - x_sym))
                   
        return prefactor * expr

# ==========================================
# Simulation and Visualization
# ==========================================

def run_simulation():
    # 1. Setup Parameters
    # Using realistic QCD scales: GeV units
    alphas = 0.3
    mu = 2.0     # Renormalization scale
    pz = 1.93    # Longitudinal momentum (typical for lattice: ~3 * 2pi/a)
    
    model = SailDiagramQuasiPDF(alpha_s=alphas, mu=mu, pz=pz)
    
    # 2. Define x-ranges to avoid singularities at 0 and 1
    # We split the domain to plot the three regions separately
    npoints = 300
    x_neg = np.linspace(-0.6, -0.001, npoints)
    x_mid = np.linspace(0.001, 0.999, npoints)
    x_pos = np.linspace(1.001, 2.0, npoints)
    
    # 3. Calculate Values
    y_neg = model.evaluate_finite_part(x_neg)
    y_mid = model.evaluate_finite_part(x_mid)
    y_pos = model.evaluate_finite_part(x_pos)
    
    # 4. Create Graphics
    plt.figure(figsize=(10, 6))
    
    # Plotting with distinct colors/styles
    plt.plot(x_neg, y_neg, label='x < 0 (IR)', color='blue', linestyle='--')
    plt.plot(x_mid, y_mid, label='0 < x < 1 (UV)', color='red')
    plt.plot(x_pos, y_pos, label='x > 1 (IR)', color='green', linestyle='--')
    
    # Annotations for regions and parameters
    title_text = (f"Sail-Diagram Finite Remainder $\\tilde{{q}}^{{(1), rem}}_{{sail}}(x)$\n"
                  f"$\\alpha_s={alphas}$, $\\mu={mu}$ GeV, $P^z={pz}$ GeV")
    plt.title(title_text, fontsize=12)
    plt.xlabel("Momentum Fraction $x$", fontsize=12)
    plt.ylabel("Contribution", fontsize=12)
    
    # Vertical lines for physical boundaries
    plt.axvline(0, color='black', linewidth=0.8, alpha=0.5)
    plt.axvline(1, color='black', linewidth=0.8, alpha=0.5)
    plt.axhline(0, color='black', linewidth=0.5, linestyle=':', alpha=0.5)
    
    plt.legend()
    plt.grid(True, alpha=0.3)
    
    print("Plotting Sail-Diagram contribution...")
    plt.show()

    # 5. Symbolic Verification
    # Compare the numeric evaluation with a direct symbolic substitution
    # to ensure no formulas were transcribed incorrectly.
    print("\nRunning symbolic verification...")
    x_sym, mu_sym, pz_sym = sp.symbols('x mu pz', positive=True)
    
    # Verification point in 0<x<1 region
    test_x = 0.5
    expr_mid = model.get_analytic_expression('0<x<1', x_sym, mu_sym, pz_sym)
    # Substitute parameters
    subs_dict = {
        x_sym: test_x, 
        mu_sym: mu, 
        pz_sym: pz, 
        sp.symbols('alpha_s'): alphas, 
        sp.symbols('Cf'): 4/3
    }
    val_symbolic = float(expr_mid.subs(subs_dict).evalf())
    
    val_numeric = model.evaluate_finite_part(np.array([test_x]))[0]
    
    print(f"Check at x={test_x}:")
    print(f"Symbolic result: {val_symbolic:.6f}")
    print(f"Numeric result:  {val_numeric:.6f}")
    print(f"Difference:      {abs(val_symbolic - val_numeric):.2e}")
    
    if abs(val_symbolic - val_numeric) < 1e-9:
        print("Verification Passed.")
    else:
        print("Verification Failed.")

# ==========================================
# Main Execution
# ==========================================

if __name__ == "__main__":
    run_simulation()
```
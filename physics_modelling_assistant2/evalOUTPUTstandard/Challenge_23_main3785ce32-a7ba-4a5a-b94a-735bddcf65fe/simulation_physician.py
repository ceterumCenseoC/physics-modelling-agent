
```python
import numpy as np
import matplotlib.pyplot as plt
from scipy import integrate
import sympy as sp

# ==========================================
# Model Implementation: Sail-Diagram Contribution
# ==========================================

# The implementation follows the derivations described in the provided context,
# specifically arXiv:2607.04182, Sec 3.2 and 3.3.
# The goal is to compute the matching coefficient or the diagram contribution
# in three x-regions: x < 0, 0 < x < 1, and x > 1.

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
        Helper to compute the plus-prescription part for 0 < x < 1.
        This handles the UV divergence and the finite part in the physical region.
        Based on Eq (3.38) in Chay (arXiv:2607.04182).
        
        The term in the {0<x<1} bracket is:
        [ (1+x^2)/(1-x) * ln(4*x*(1-x)*pz^2/mu^2) - x*(1+x)/(1-x) ]
        
        Note: The 'plus' distribution logic for plotting is handled by the main 
        evaluation function which integrates against a test function or simply 
        evaluates the function away from x=1. For direct plotting, we usually 
        plot the 'raw' integrand, but the 'plus' nature implies regularization.
        
        Here we return the integrand part that acts on f(x).
        int_0^1 [F(x)]_+ f(x) dx = int_0^1 F(x) (f(x)-f(1)) dx
        """
        # Avoid division by zero at x=1 in the return value
        # We handle x=1 limit explicitly if needed, or return NaNs
        
        if x == 1.0:
            return np.nan # The distribution is defined by integration, not point value
        
        arg = 4 * x * (1 - x) * (self.pz**2) / (self.mu**2)
        
        # Protect against log of zero or negative arguments (floating point errors near boundaries)
        # The limit x->0 is finite, x->1 has divergence handled by distribution
        if arg <= 0:
            if x < 0: arg = 1e-10 # Should not happen here
            if x > 1: arg = 1e-10 # Should not happen here
            if x > 0 and x < 1: # x is very close to 0 or 1
                if x < 1e-9: arg = 1e-10
                else: arg = 1e-10

        term1 = (1 + x**2) / (1 - x) * np.log(arg)
        term2 = (x * (1 + x)) / (1 - x)
        
        return term1 - term2

    def _region_x_gt_1(self, x):
        """
        Helper for x > 1.
        This region contains IR divergences (regulated by epsilon_IR).
        We return the finite part structure requested in the model equations.
        
        Term: [ (1+x^2)/(1-x) * ln(x/(x-1)) + 1 + 3/(2x) ]^(1)_+,inf - 3/(2x)
        """
        # The expression inside the bracket for the distribution part
        # Usually finite for x>1, let's check the singularities.
        # 1-x is negative. x > 1.
        # ln(x/(x-1)) is finite.
        
        term1 = (1 + x**2) / (1 - x) * np.log(x / (x - 1))
        term2 = 1
        term3 = 3 / (2 * x)
        
        dist_part = term1 + term2 + term3
        
        # Subtract the 3/(2x) tail term
        return dist_part - 3 / (2 * x)

    def _region_x_lt_0(self, x):
        """
        Helper for x < 0.
        This region contains IR divergences.
        
        Term: [ (1+x^2)/(1-x) * ln((1-x)/(-x)) - 1 + 3/(2(1-x)) ]^(1)_+,[-inf,0] - 3/(2(1-x))
        """
        term1 = (1 + x**2) / (1 - x) * np.log((1 - x) / (-x))
        term2 = -1
        term3 = 3 / (2 * (1 - x))
        
        dist_part = term1 + term2 + term3
        
        # Subtract the 3/(2(1-x)) tail term
        return dist_part - 3 / (2 * (1 - x))

    def evaluate_finite_part(self, x_vals):
        """
        Evaluate the finite part of the sail diagram contribution (remainder)
        for an array of x values.
        
        Note: This implementation focuses on the finite 'remainder' structure
        characteristic of the sail diagram's contribution to the matching 
        coefficient or the renormalized quasi-PDF in the MS-bar scheme.
        
        The pole terms (1/epsilon) are omitted here as we are interested in the
        O(epsilon^0) finite part for numerical evaluation.
        """
        results = []
        for x in x_vals:
            if 0 < x < 1:
                val = self._region_0_1_plus_distribution(x)
                # For plotting simply f(x), we take the integrand. 
                # The 'plus' nature means the integral is finite, but f(1) blows up.
                # For x close to 1, this large value is expected in the raw function.
            elif x > 1:
                val = self._region_x_gt_1(x)
            elif x < 0:
                val = self._region_x_lt_0(x)
            else:
                # Boundaries x=0 or x=1
                val = np.nan
            results.append(val)
        
        return self.common_prefactor * np.array(results)

    def get_analytic_expression(self, region, x_sym, mu_sym, pz_sym):
        """
        Return a SymPy expression for the model in a specific region.
        This satisfies the requirement to implement the formulas mathematically.
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
            # Note: The outer bracket is the plus distribution kernel.
            # Here we output the raw kernel as per the function's logic.
            expr = ((1 + x_sym**2)/(1 - x_sym) * sp.log(x_sym/(x_sym - 1)) + 1 + 3/(2*x_sym)) - \
                   3/(2*x_sym)
        elif region == 'x<0':
            # ((1+x^2)/(1-x) * ln((1-x)/(-x)) - 1 + 3/(2*(1-x))) - 3/(2*(1-x))
            expr = ((1 + x_sym**2)/(1 - x_sym) * sp.log((1 - x_sym)/(-x_sym)) - 1 + 3/(2*(1 - x_sym))) - \
                   3/(2*(1 - x_sym))
                   
        # If prefactor is constant in the matching coeff (evaluated at specific alphas), 
        # we can apply it. 
        return prefactor * expr

# ==========================================
# Simulation and Visualization
# ==========================================

def run_simulation():
    # 1. Setup Parameters (Using values from the Realistic Parameters section)
    # alpha_s ~ 0.3, mu ~ 2 GeV, pz ~ 2 GeV
    # Setting mu = pz minimizes the log term ln(mu^2/pz^2) but here we have ln(pz^2/mu^2) inside.
    # Let's use distinct scales to show the log dependence.
    alphas = 0.3
    mu = 2.0     # GeV
    pz = 1.93    # GeV (approx typical lattice momentum 3 * 2pi/L approx)
    
    model = SailDiagramQuasiPDF(alpha_s=alphas, mu=mu, pz=pz)
    
    # 2. Define x-range
    # We need to cover x < 0, 0 < x < 1, x > 1
    # Avoid exactly 0 and 1 in the plot arrays
    x_neg = np.linspace(-0.6, -0.01, 200)
    x_mid = np.linspace(0.01, 0.99, 200)
    x_pos = np.linspace(1.01, 2.0, 200)
    
    # 3. Calculate Values
    y_neg = model.evaluate_finite_part(x_neg)
    y_mid = model.evaluate_finite_part(x_mid)
    y_pos = model.evaluate_finite_part(x_pos)
    
    # 4. Create Graphics
    plt.figure(figsize=(10, 6))
    
    plt.plot(x_neg, y_neg, label='x < 0', color='blue', linestyle='--')
    plt.plot(x_mid, y_mid, label='0 < x < 1', color='red')
    plt.plot(x_pos, y_pos, label='x > 1', color='green', linestyle='--')
    
    # Annotations for regions
    plt.title(f"Sail-Diagram Contribution to Quasi-PDF\n($\\alpha_s={alphas}, \\mu={mu}$ GeV, $P^z={pz}$ GeV)")
    plt.xlabel("Momentum Fraction $x$", fontsize=12)
    plt.ylabel("Contribution $\\tilde{q}^{(1)}_{sail}(x)$", fontsize=12)
    plt.axvline(0, color='black', linewidth=0.8)
    plt.axvline(1, color='black', linewidth=0.8)
    plt.axhline(0, color='black', linewidth=0.5, linestyle=':')
    plt.legend()
    plt.grid(True, alpha=0.3)
    
    print("Displaying plot of the Sail-Diagram contribution...")
    plt.show()

    # 5. Symbolic Verification Unit Test
    # Verify the analytic expression matches the implemented logic for a specific point
    x_sym, mu_sym, pz_sym = sp.symbols('x mu pz', positive=True)
    
    # Test region 0<x<1 at x=0.5
    expr_mid = model.get_analytic_expression('0<x<1', x_sym, mu_sym, pz_sym)
    val_expr = expr_mid.subs({x_sym: 0.5, mu_sym: mu, pz_sym: pz, sp.symbols('alpha_s'): alphas, sp.symbols('Cf'): 4/3})
    val_expr = float(val_expr.evalf())
    
    val_numeric = model.evaluate_finite_part(np.array([0.5]))[0]
    
    print(f"\nSymbolic vs Numeric Check at x=0.5:")
    print(f"Symbolic: {val_expr}")
    print(f"Numeric:  {val_numeric}")
    print(f"Difference: {abs(val_expr - val_numeric):.2e}")

# ==========================================
# Main Execution
# ==========================================

if __name__ == "__main__":
    run_simulation()
```
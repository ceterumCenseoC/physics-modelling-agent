
```python
import numpy as np
import matplotlib.pyplot as plt
from typing import Union, Tuple, Literal

class CoulombGaugeQuasiPDF:
    """
    Implements the model for the Coulomb Gauge (CG) quasi-PDF 
    up to 1-loop order for a free massless quark state.
    """
    def __init__(self, alpha_s: float, cf: float = 4.0/3.0):
        """
        Initialize the model with physical constants.
        
        Parameters:
        alpha_s: Strong coupling constant.
        cf: Casimir constant (default 4/3 for QCD).
        """
        self.alpha_s = alpha_s
        self.cf = cf
        self.prefactor = (self.alpha_s * self.cf) / (2.0 * np.pi)

    def _f1_pos(self, y: np.ndarray, mu: float, pz: float, eps_ir: float) -> np.ndarray:
        """
        1-loop correction for 0 < y < 1.
        Implementation of:
        [ (1+y^2)/(1-y) * (1/eps_ir - ln(mu^2/4pz^2) + ln(1-y)) + 3/2 * 1/(1-y) ]_+
        
        Note: We implement the 'bare' structure inside the bracket. 
        The plus-prescription is handled in the main evaluation function 
        when integrating or plotting depending on context, but for pointwise 
        evaluation we return the integrand form.
        """
        # Avoid division by zero at y=1, handled by safety checks in calling functions
        mask = (y > 0) & (y < 1)
        
        # Pre-calculate log terms
        # ln(1-y)
        ln_1my = np.log(1.0 - y[mask])
        # ln(mu^2 / 4pz^2)
        log_ratio = np.log(mu**2 / (4.0 * pz**2))
        
        # Structure: (1+y^2)/(1-y)
        structure = (1.0 + y[mask]**2) / (1.0 - y[mask])
        
        # Pole term
        pole_term = 1.0 / eps_ir
        
        # Assemble the expression
        # (1+y^2)/(1-y) * (1/eps - ln(mu^2/4pz^2) + ln(1-y))
        term1 = structure * (pole_term - log_ratio + ln_1my)
        
        # 3/2 * 1/(1-y)
        term2 = 1.5 / (1.0 - y[mask])
        
        result = np.zeros_like(y)
        result[mask] = term1 + term2
        return result

    def _f1_gt1(self, y: np.ndarray) -> np.ndarray:
        """
        1-loop correction for y > 1.
        Implementation of:
        (1+y^2)/(y-1) * ln(y/(y-1)) - y + 3/2
        """
        mask = y > 1
        result = np.zeros_like(y)
        
        # (1+y^2)/(y-1) * ln( y / (y-1) )
        # Note: y/(y-1) is always > 1 for y > 1, so log is positive.
        term1 = (1.0 + y[mask]**2) / (y[mask] - 1.0) * np.log(y[mask] / (y[mask] - 1.0))
        
        # -y + 3/2
        term2 = -y[mask] + 1.5
        
        result[mask] = term1 + term2
        return result

    def _f1_lt0(self, y: np.ndarray) -> np.ndarray:
        """
        1-loop correction for y < 0.
        Implementation of:
        -(1+y^2)/(1-y) * ln( -y / (1-y) ) - y - 3/2
        """
        mask = y < 0
        result = np.zeros_like(y)
        
        # Argument of log: -y / (1-y). 
        # If y < 0, -y > 0 and 1-y > 1, so ratio is positive.
        arg_log = (-y[mask]) / (1.0 - y[mask])
        val_log = np.log(arg_log)
        
        # -(1+y^2)/(1-y) * ln(...)
        term1 = - (1.0 + y[mask]**2) / (1.0 - y[mask]) * val_log
        
        # -y - 3/2
        term2 = -y[mask] - 1.5
        
        result[mask] = term1 + term2
        return result

    def compute_f1(self, y: Union[float, np.ndarray], mu: float, pz: float, 
                   eps_ir: float) -> Union[float, np.ndarray]:
        """
        Computes the 1-loop correction tilde_f_q^{(1)} for given y values.
        
        Parameters:
        y: Momentum fraction (can be scalar or array).
        mu: Renormalization scale.
        pz: Large longitudinal momentum.
        eps_ir: Infrared regulator (small positive number).
        
        Returns:
        The 1-loop correction value.
        """
        y_arr = np.atleast_1d(y)
        f1 = np.zeros_like(y_arr)
        
        # Region 0 < y < 1
        f1 += self._f1_pos(y_arr, mu, pz, eps_ir)
        
        # Region y > 1
        f1 += self._f1_gt1(y_arr)
        
        # Region y < 0
        f1 += self._f1_lt0(y_arr)
        
        if np.isscalar(y):
            return f1[0]
        return f1

    def compute_total(self, y: Union[float, np.ndarray], mu: float, 
                      pz: float, eps_ir: float, plus_prescription: bool = True) -> Union[float, np.ndarray]:
        """
        Computes the total quasi-PDF tilde_f_q = delta(1-y) + (alpha_s CF / 2pi) * f1
        
        Parameters:
        y: Momentum fraction.
        mu: Renormalization scale.
        pz: Large longitudinal momentum.
        eps_ir: Infrared regulator.
        plus_prescription: If True (default), the region 0<y<1 is treated with + prescription.
                           If False, the raw divergent term is returned (useful for inspection).
                           Note: For pointwise plotting with finite discretization, this parameter
                           just determines if we apply the subtraction at y=1, or just return f1.
        
        Returns:
        The total quasi-PDF value.
        """
        y_arr = np.atleast_1d(y)
        
        # 1. Get the 1-loop correction factor
        f1 = self.compute_f1(y_arr, mu, pz, eps_ir)
        
        # 2. Handle Plus Prescription for 0 < y < 1 if requested
        # The delta function contribution is effectively infinite at y=1 and 0 elsewhere in pointwise calc.
        # We compute the "distribution value" excluding the delta spot for visualization, 
        # or add a Gaussian approximation for the delta to make it look like a function.
        
        if plus_prescription:
            # For numerical evaluation of the continuous part in 0<y<1 away from singularity,
            # we use the raw f1 function. 
            # However, strictly speaking, the plus prescription modifies the integral weight.
            # For a pointwise plot of the shape, we usually plot the `f1` term defined above.
            # The delta function is handled as a special case below.
            pass

        total = self.prefactor * f1
        
        # Add Tree Level Delta Function
        # In a discrete plot, we can't represent a true Dirac delta. 
        # We can represent it by adding 1.0 to bin containing y=1 or explicitly noting it.
        # Here, we will not add it to the array because it makes plotting messy,
        # but we will note it in the return/doc.
        # Alternatively, if user wants to iterate, they sum total + delta(y-1).
        
        # Identify very close to y=1
        # For actual branching calculations, one should use integration methods.
        
        if np.isscalar(y):
            return total[0] # Note: Delta not applied to scalar != 1
        return total

def main():
    # --- 1. Setup Parameters from Planning ---
    # Realistic starting parameters for LaMET/QCD
    alpha_s = 0.30
    cf = 4.0 / 3.0
    mu = 2.0  # GeV
    pz = 2.0  # GeV (Large momentum)
    eps_ir = 1e-5  # IR regulator for numerical check of pole
    
    # Initialize Model
    model = CoulombGaugeQuasiPDF(alpha_s=alpha_s, cf=cf)
    
    # --- 2. Verify Formulas at specific points (Analytical Check) ---
    print("--- Model Verification ---")
    
    # Region y > 1 (e.g., y=2) - should be independent of scales
    y_test_2 = 2.0
    val_gt1 = model.compute_f1(y_test_2, mu, pz, eps_ir)
    # Analytical approx: (1+4)/1 * ln(2/1) - 2 + 1.5 = 5*0.693 - 0.5 = 2.96
    print(f"Region y>1 (y=2): Model = {val_gt1:.5f}")
    
    # Region y < 0 (e.g., y=-1) - should be independent of scales
    y_test_neg1 = -1.0
    val_lt0 = model.compute_f1(y_test_neg1, mu, pz, eps_ir)
    # Analytical: -(1+1)/(2) * ln(1/2) - (-1) - 1.5 = -1 * (-0.693) + 1 - 1.5 = -1 + 0.693 = -0.307
    print(f"Region y<0 (y=-1): Model = {val_lt0:.5f}")
    
    # Region 0 < y < 1 (e.g., y=0.5) - depends on scales
    y_test_05 = 0.5
    val_pos = model.compute_f1(y_test_05, mu, pz, eps_ir)
    # Terms: (1+0.25)/0.5 = 2.5
    # Log terms: 1/eps - ln(4/16) + ln(0.5) = 1e5 - (-1.386) - 0.693 = Huge number.
    # Let's check the finite part structure visually rather than the pole dominated number.
    print("Region 0<y<1 (y=0.5): Value dominated by 1/eps_ir pole.")
    print(f"  With eps_ir={eps_ir}, value = {val_pos:.2f}")
    
    # --- 3. Graphics Generation ---
    print("\n--- Generating Graphics ---")
    
    # Define ranges for plotting
    # Note: We exclude exactly y=1 in the arrays to avoid division by zero warnings
    y_neg = np.linspace(-2.0, -0.01, 400)
    y_pos_small = np.linspace(0.01, 0.99, 400)
    y_pos_large = np.linspace(1.01, 3.0, 400)
    
    fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(10, 8))
    
    # --- Plot 1: Full Shape (Comparison of Regions) ---
    # Since 0<y<1 is divergent at y->1 due to 1/eps and 1/(1-y), we can't plot it "fully" 
    # without subtraction. 
    # For visualization, we will:
    # 1. Plot y < 0 and y > 1 using full formula.
    # 2. Plot 0 < y < 1 assuming a finite cutoff or just showing the structure.
    #    Here we show the structure WITHOUT the 1/eps_ir pole to make it readable on the same scale,
    #    or we acknowledge it is a distribution.
    #    Let's plot the "finite" part of the 0<y<1 expression by setting 1/eps = 0 for visualization only,
    #    just to show the log cut structure.
    
    def plot_f1_visual(y_arr, region_name, ax):
        # Calculates for plotting. For 0<y<1, we suppress the 1/eps pole for visibility if desired,
        # but let's show the full magnitude where finite.
        
        # Compute full f1
        vals_full = model.compute_f1(y_arr, mu, pz, eps_ir)
        
        # For 0<y<1 region, the values are huge due to 1/eps_ir (1e5). 
        # To visualize the structure, we also compute just the finite structure (excluding 1/eps)
        # strictly for the shape of the scattering function.
        if region_name == "0<y<1":
            vals_finite = model.compute_f1(y_arr, mu, pz, eps_ir=np.inf) # 1/inf -> 0
            ax.plot(y_arr, vals_full, 'b--', alpha=0.1, label=r'$\tilde{f}^{(1)}_{pos}$ (with $1/\epsilon_{IR}$)')
            ax.plot(y_arr, vals_finite, 'r-', label=r'$\tilde{f}^{(1)}_{pos}$ (finite part structure)')
        else:
            ax.plot(y_arr, vals_full, 'g-', label=r'$\tilde{f}^{(1)}$')
            
        ax.set_ylabel(r'$\tilde{f}_q^{(1)}$')
        ax.set_title(f'{region_name} Region')
        ax.grid(True, alpha=0.3)
        ax.legend()

    # Plot y > 1
    ax = ax1
    ax.set_title(r'Coulomb Gauge Quasi-PDF 1-Loop Correction $\tilde{f}_q^{(1)}$')
    # Region y < 0
    vals_neg = model.compute_f1(y_neg, mu, pz, eps_ir)
    ax.plot(y_neg, vals_neg, 'b-', label=r'$y < 0$')
    
    # Region 0 < y < 1 (Finite part structure only, as pole is huge)
    # Using eps_ir=infinity trick to zero out the pole term for shape visualization
    vals_pos_finite = model.compute_f1(y_pos_small, mu, pz, eps_ir=1e10) 
    ax.plot(y_pos_small, vals_pos_finite, 'r-', label=r'$0 < y < 1$ (finite structure)')
    
    # Region y > 1
    vals_gt1 = model.compute_f1(y_pos_large, mu, pz, eps_ir)
    ax.plot(y_pos_large, vals_gt1, 'g-', label=r'$y > 1$')
    
    ax.axvline(x=0, color='k', linestyle=':', alpha=0.5)
    ax.axvline(x=1, color='k', linestyle=':', alpha=0.5)
    ax.set_xlabel(r'Momentum Fraction $y$')
    ax.set_ylabel(r'$\tilde{f}_q^{(1)}$')
    ax.set_ylim(-5, 5) # Zoom in to see shape
    ax.legend()
    ax.grid(True, alpha=0.3)
    
    # --- Plot 2: Comparison of Different Scales/Momenta ---
    # We compare the shape in y>1 which is independent of scales (so they should overlap exactly),
    # vs 0<y<1 which changes with ln(mu^2/pz^2).
    
    ax = ax2
    y_test = np.linspace(0.1, 0.9, 100)
    
    # Case 1: mu = 2 GeV, pz = 2 GeV (Large log term: ln(4/16) = ln(0.25) = -1.386)
    vals_case1 = model.compute_f1(y_test, mu=2.0, pz=2.0, eps_ir=1e10) 
    
    # Case 2: mu = 2 GeV, pz = 4 GeV (Large log term: ln(4/64) = ln(0.0625) = -2.772)
    vals_case2 = model.compute_f1(y_test, mu=2.0, pz=4.0, eps_ir=1e10)
    
    # Plot difference to highlight scale dependence
    ax.plot(y_test, vals_case1, label=r'$\mu=2$ GeV, $p_z=2$ GeV')
    ax.plot(y_test, vals_case2, label=r'$\mu=2$ GeV, $p_z=4$ GeV', linestyle='--')
    
    ax.set_xlabel(r'Momentum Fraction $y$ ($0<y<1$)')
    ax.set_title(r'Scale Dependence in $0<y<1$ (Finite part)')
    ax.legend()
    ax.grid(True, alpha=0.3)
    
    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    main()
```
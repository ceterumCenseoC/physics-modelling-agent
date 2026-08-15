```python
import numpy as np
import matplotlib.pyplot as plt
from typing import Union

class CoulombGaugeQuasiPDF:
    """
    Implements the model for the Coulomb Gauge (CG) quasi-PDF 
    up to 1-loop order for a free massless quark state.

    Formulas implemented based on provided context:
    - Region 0 < y < 1: Kernel with IR pole and logarithmic terms.
    - Region y > 1: Finite expression independent of scales.
    - Region y < 0: Finite expression independent of scales.
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
        Formula: [ (1+y^2)/(1-y) * (1/eps_ir - ln(mu^2/4pz^2) + ln(1-y)) + 3/2 * 1/(1-y) ]
        
        Note: Returns the integrand structure. The plus-prescription [ ... ]_+ 
        is implicit in the usage of this distribution when integrated.
        For pointwise evaluation of the structure, we return the term inside the bracket.
        """
        # Mask for the valid region to avoid division by zero or log(negative)
        # Although caller should ensure y in (0,1), we add safety check
        mask = (y > 0.0) & (y < 1.0)
        result = np.zeros_like(y)
        
        if not np.any(mask):
            return result

        y_valid = y[mask]
        
        # Pre-calculate components
        # ln(1-y)
        ln_1my = np.log(1.0 - y_valid)
        # ln(mu^2 / 4pz^2) = 2*ln(mu) - 2*ln(pz) - ln(4)
        # Formula explicitly has 4pz^2
        log_ratio = np.log(mu**2 / (4.0 * pz**2))
        
        # Splitting kernel factor: (1+y^2)/(1-y)
        pqq_splitting = (1.0 + y_valid**2) / (1.0 - y_valid)
        
        # Pole term
        pole_term = 1.0 / eps_ir
        
        # Assemble the expression inside the plus distribution
        term1 = pqq_splitting * (pole_term - log_ratio + ln_1my)
        term2 = 1.5 / (1.0 - y_valid)
        
        result[mask] = term1 + term2
        return result

    def _f1_gt1(self, y: np.ndarray) -> np.ndarray:
        """
        1-loop correction for y > 1.
        Formula: (1+y^2)/(y-1) * ln( y / (y-1) ) - y + 3/2
        """
        mask = y > 1.0
        result = np.zeros_like(y)
        
        if not np.any(mask):
            return result

        y_valid = y[mask]
        
        # (1+y^2)/(y-1) * ln( y / (y-1) )
        # y > 1 implies y/(y-1) > 0, so log is real
        ratio = y_valid / (y_valid - 1.0)
        term1 = (1.0 + y_valid**2) / (y_valid - 1.0) * np.log(ratio)
        
        # -y + 3/2
        term2 = -y_valid + 1.5
        
        result[mask] = term1 + term2
        return result

    def _f1_lt0(self, y: np.ndarray) -> np.ndarray:
        """
        1-loop correction for y < 0.
        Formula: -(1+y^2)/(1-y) * ln( -y / (1-y) ) - y - 3/2
        """
        mask = y < 0.0
        result = np.zeros_like(y)
        
        if not np.any(mask):
            return result
            
        y_valid = y[mask]
        
        # Argument of log: -y / (1-y)
        # If y < 0, -y > 0 and 1-y > 1, so ratio is positive.
        arg_log = (-y_valid) / (1.0 - y_valid)
        val_log = np.log(arg_log)
        
        # -(1+y^2)/(1-y) * ln(...)
        term1 = - (1.0 + y_valid**2) / (1.0 - y_valid) * val_log
        
        # -y - 3/2
        term2 = -y_valid - 1.5
        
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
        
        # Add contributions from all regions
        f1 += self._f1_pos(y_arr, mu, pz, eps_ir)
        f1 += self._f1_gt1(y_arr)
        f1 += self._f1_lt0(y_arr)
        
        if np.isscalar(y):
            return f1[0]
        return f1

    def compute_total(self, y: Union[float, np.ndarray], mu: float, 
                      pz: float, eps_ir: float) -> Union[float, np.ndarray]:
        """
        Computes the total quasi-PDF tilde_f_q = delta(1-y) + (alpha_s CF / 2pi) * f1
        
        Note: The Dirac delta function delta(1-y) is not representable as a finite value
        at y=1 in a continuous array context. This function returns the finite 1-loop
        contribution multiplied by the prefactor. The delta function must be added 
        separately during integration or distribution processing.
        
        Parameters:
        y: Momentum fraction.
        mu: Renormalization scale.
        pz: Large longitudinal momentum.
        eps_ir: Infrared regulator.
        
        Returns:
        The 1-loop contribution to the total quasi-PDF (excluding delta function).
        """
        loop_correction = self.compute_f1(y, mu, pz, eps_ir)
        return self.prefactor * loop_correction

def main():
    # --- 1. Setup Parameters ---
    # Realistic starting parameters for LaMET/QCD
    alpha_s = 0.30
    cf = 4.0 / 3.0
    mu = 2.0  # GeV
    pz = 2.0  # GeV (Large momentum)
    eps_ir = 1e-5  # IR regulator for numerical check of pole
    
    # Initialize Model
    model = CoulombGaugeQuasiPDF(alpha_s=alpha_s, cf=cf)
    
    # --- 2. Verify Formulas at specific points (Analytical Check) ---
    print("--- Model Verification (Analytical Checks) ---")
    
    # Region y > 1 (e.g., y=2) - should be independent of scales
    y_test_2 = 2.0
    val_gt1 = model.compute_f1(y_test_2, mu, pz, eps_ir)
    # Calculation:
    # y=2 => y^2=4
    # (1+4)/(2-1) = 5
    # ln(2/1) = ln(2) ~= 0.6931
    # Term1 = 5 * 0.6931 = 3.4657
    # Term2 = -2 + 1.5 = -0.5
    # Total = 2.9657
    expected_gt1 = 5 * np.log(2) - 0.5
    print(f"Region y>1 (y=2): Model = {val_gt1:.5f}, Expected = {expected_gt1:.5f}, Diff = {val_gt1 - expected_gt1:.2e}")
    
    # Region y < 0 (e.g., y=-1) - should be independent of scales
    y_test_neg1 = -1.0
    val_lt0 = model.compute_f1(y_test_neg1, mu, pz, eps_ir)
    # Calculation:
    # y=-1 => y^2=1
    # Arg log = -(-1)/(1-(-1)) = 1/2 = 0.5
    # ln(0.5) = -0.6931
    # Term1 = -(1+1)/(1-(-1)) * (-0.6931) = -(2/2) * (-0.6931) = 0.6931
    # Term2 = -(-1) - 1.5 = 1 - 1.5 = -0.5
    # Total = 0.1931
    expected_lt0 = - (2.0 / 2.0) * np.log(0.5) - 0.5
    print(f"Region y<0 (y=-1): Model = {val_lt0:.5f}, Expected = {expected_lt0:.5f}, Diff = {val_lt0 - expected_lt0:.2e}")
    
    # Region 0 < y < 1 (e.g., y=0.5) - depends on scales
    y_test_05 = 0.5
    val_pos = model.compute_f1(y_test_05, mu, pz, eps_ir)
    # Terms: (1+0.25)/0.5 = 2.5
    # Log term = -ln(mu^2/4pz^2) + ln(1-y)
    # With mu=pz, -ln(1/4) = 1.386; ln(0.5) = -0.693 => combined ~0.693
    # Pole term dominates if eps_ir is small.
    print("Region 0<y<1 (y=0.5): Value dominated by 1/eps_ir pole.")
    print(f"  With eps_ir={eps_ir}, value = {val_pos:.4f}")
    print(f"  Structure check (finite part with 1/eps=0): {model.compute_f1(y_test_05, mu, pz, eps_ir=np.inf):.4f}")
    
    # --- 3. Graphics Generation ---
    print("\n--- Generating Graphics ---")
    
    # Define ranges for plotting
    # We avoid exactly y=1 to handle division by zero gracefully in array generation
    y_neg = np.linspace(-2.0, -0.01, 400)
    y_pos_small = np.linspace(0.01, 0.99, 400)
    y_pos_large = np.linspace(1.01, 3.0, 400)
    
    fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(10, 10))
    
    # --- Plot 1: Full Shape ---
    # Region y < 0
    vals_neg = model.compute_f1(y_neg, mu, pz, eps_ir)
    ax1.plot(y_neg, vals_neg, 'b-', label=r'$y < 0$')
    
    # Region 0 < y < 1
    # For visualization, we want to see the shape, not the 1/1e-5 pole hitting the ceiling.
    # We calculate the "finite" part by sending eps_ir to infinity (making 1/eps -> 0)
    # or just the raw values if we were interested in the pole behavior.
    vals_pos_finite = model.compute_f1(y_pos_small, mu, pz, eps_ir=np.inf) 
    ax1.plot(y_pos_small, vals_pos_finite, 'r-', label=r'$0 < y < 1$ (finite structure)')
    
    # Region y > 1
    vals_gt1 = model.compute_f1(y_pos_large, mu, pz, eps_ir)
    ax1.plot(y_pos_large, vals_gt1, 'g-', label=r'$y > 1$')
    
    ax1.axvline(x=0, color='k', linestyle=':', alpha=0.5)
    ax1.axvline(x=1, color='k', linestyle=':', alpha=0.5)
    ax1.set_title(r'Coulomb Gauge Quasi-PDF 1-Loop Correction $\tilde{f}_q^{(1)}$')
    ax1.set_xlabel(r'Momentum Fraction $y$')
    ax1.set_ylabel(r'$\tilde{f}_q^{(1)}$')
    ax1.set_ylim(-3, 4)  # Adjust limits to see the shape clearly
    ax1.legend()
    ax1.grid(True, alpha=0.3)
    
    # --- Plot 2: Total Quasi-PDF (Finite part structure) ---
    # Plot delta(1-y) + prefactor * f1
    # Since we plot continuous y, we visualize the loop contribution and indicate the delta peak
    
    total_neg = model.compute_total(y_neg, mu, pz, eps_ir)
    total_pos_finite = model.compute_total(y_pos_small, mu, pz, eps_ir=np.inf)
    total_gt1 = model.compute_total(y_pos_large, mu, pz, eps_ir)
    
    ax2.plot(y_neg, total_neg, 'b-', label=r'$\alpha C_F/2\pi \cdot \tilde{f}^{(1)} (y<0)$')
    ax2.plot(y_pos_small, total_pos_finite, 'r-', label=r'$\alpha C_F/2\pi \cdot \tilde{f}^{(1)} (0<y<1)$')
    ax2.plot(y_pos_large, total_gt1, 'g-', label=r'$\alpha C_F/2\pi \cdot \tilde{f}^{(1)} (y>1)$')
    
    # Simulate the delta function at y=1 with a narrow Gaussian for visualization purposes only
    y_delta = np.linspace(0.5, 1.5, 300)
    # Gaussian with small width and height normalized roughly to prefactor
    width = 0.02
    height = 1.0 * 10.0 # arbitrary height to show peak in plot
    delta_approx = height * np.exp(-(y_delta - 1.0)**2 / (2 * width**2))
    ax2.plot(y_delta, delta_approx, 'k--', alpha=0.6, label=r'$\delta(1-y)$ (Visualization)')

    ax2.axvline(x=0, color='k', linestyle=':', alpha=0.5)
    ax2.axvline(x=1, color='k', linestyle=':', alpha=0.5)
    ax2.set_title(r'Total Quasi-PDF $\tilde{f}_q \approx \delta(1-y) + \frac{\alpha_s C_F}{2\pi} \tilde{f}^{(1)}$')
    ax2.set_xlabel(r'Momentum Fraction $y$')
    ax2.set_ylabel(r'Value')
    ax2.set_ylim(-0.5, 1.5)
    ax2.legend()
    ax2.grid(True, alpha=0.3)
    
    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    main()
```
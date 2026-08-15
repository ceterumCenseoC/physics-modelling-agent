
```python
import numpy as np
import matplotlib.pyplot as plt

class SailDiagramModel:
    """
    Implements the sail-diagram contribution to the quasi-PDF in LaMET.
    
    Based on the Large Momentum Effective Theory (LaMET) framework, 
    this model calculates the perturbative matching coefficient contribution
    from the 'sail' diagram using dimensional regularization.
    """
    
    def __init__(self, alpha_s=0.30, Cf=4.0/3.0, pz=3.0, mu=2.0):
        """
        Initialize the physics parameters for the Sail Diagram model.
        
        Parameters:
        -----------
        alpha_s : float
            Strong coupling constant (dimensionless). Default ~0.30 for hadronic scales.
        Cf : float
            Quadratic Casimir for fundamental representation. 4/3 for SU(3) QCD.
        pz : float
            Large longitudinal momentum of the hadron state (GeV).
        mu : float
            Renormalization scale (GeV).
        """
        self.alpha_s = alpha_s
        self.Cf = Cf
        self.pz = pz
        self.mu = mu
        
    def compute_contribution(self, x, epsilon_uv=0.0, epsilon_ir=0.0):
        """
        Compute the sail diagram contribution tilde_q_sail.
        
        The model computes the result in the MS-bar scheme order epsilon^0.
        
        Parameters:
        -----------
        x : float or np.array
            Momentum fraction.
        epsilon_uv : float
            UV regulator (pole 1/eps_UV). In MS-bar, UV poles are subtracted, 
            so this parameter acts as a flag or allows inspection of the bare structure 
            if passed, though the MS-bar formula inherently removes the UV pole 
            structure present in the intermediate steps.
        epsilon_ir : float
            IR regulator (pole 1/eps_IR). 
            
        Returns:
        --------
        tilde_q : float or np.array
            The sail diagram contribution.
        """
        # Ensure x is a numpy array for vectorized operations
        x_arr = np.array(x, dtype=float)
        result = np.zeros_like(x_arr)
        
        # Prefactor alpha_s * Cf / (2 * pi)
        prefactor = (self.alpha_s * self.Cf) / (2.0 * np.pi)
        
        # Mask for the region 0 < x < 1 (Valence region)
        # We treat x <= 0 and x >= 1 as 0.
        mask_valence = (x_arr > 0) & (x_arr < 1)
        
        if np.any(mask_valence):
            x_val = x_arr[mask_valence]
            
            # Splitting kernel P_qq(x) = (1 + x^2) / (1 - x)
            # Note: The math derivation provided gives:
            # t_q ~ - P_qq(x) * ( ln(mu^2 / (4*x*(1-x)*pz^2)) - 1/eps_IR )
            #        - P_qq(x) + 3*(1-x)
            
            # Handle 1-x division carefully
            denominator = 1.0 - x_val
            
            # We clip the denominator to avoid division by zero at x=1.
            # Since the integration is strictly 0<x<1, x approaches 1 but is not 1.
            However, for numerical arrays, we must protect values extremely close to 1.
            # In a strict mathematical implementation, we would use a distribution (Plus-prescription).
            # Here we implement the algebraic function directly.
            
            # Add a small epsilon to denominator if it is zero to prevent runtime warnings,
            # though physically x should not be exactly 1.
            safe_denom = np.where(denominator == 0, 1e-10, denominator)
            
            P_qq = (1.0 + x_val**2) / safe_denom
            
            # The Logarithmic Term: log( mu^2 / (4 * x * (1-x) * pz^2) )
            # Note: As x -> 0 or x -> 1, the argument of the log goes to infinity.
            # This leads to the singularity structure of the PDF.
            log_arg = (self.mu**2) / (4.0 * x_val * (1.0 - x_val) * self.pz**2)
            
            # Safety check for log argument
            # If x or 1-x is extremely small, argument is large. 
            # If the input array contains 0 exactly, handle it.
            log_arg = np.maximum(log_arg, 1e-10) 
            log_term = np.log(log_arg)
            
            # The IR Divergence Term: - 1/epsilon_IR
            # The formula in the solution is: - P_qq * ( Log - 1/eps_IR )
            # So the term is + P_qq * (1/eps_IR) - P_qq * Log
            # Wait, let's re-read the provided solution formula:
            # - P_qq(x) * ( ln(...) - 1/eps_IR ) - P_qq(x) + 3(1-x)
            # = - P_qq * ln(...) + P_qq * (1/eps_IR) - P_qq + 3(1-x)
            
            # To implement the 1/eps_IR pole numerically, we use the input epsilon_ir.
            # If epsilon_ir is 0 passed by user, the pole is infinite.
            # Usually, we visualize the limit or set epsilon_ir to a small number (1e-5) for plots.
            
            ir_pole_term = 0.0
            if abs(epsilon_ir) > 1e-9:
                ir_pole_term = 1.0 / epsilon_ir
            else:
                # If epsilon is 0, the term is singular.
                # In a numerical plot of the finite part, we might ignore it, 
                # but for the full 'bare' or 'divergent' expression we handle it.
                # Here we just set the coefficient assuming standard perturbation theory
                # where the pole cancels elsewhere. For visualization, we might set it to 0 
                # or allow user to pass small epsilon.
                ir_pole_term = 0.0 # Effectively infinite if calculated properly, 0 if ignored for finite part
            
            valence_contribution = -P_qq * (log_term - ir_pole_term) - P_qq + 3.0 * (1.0 - x_val)
            
            result[mask_valence] = prefactor * valence_contribution
            
        return result

    def plot_distribution(self, x_range=np.linspace(0.01, 0.99, 500), epsilon_ir=1e-4):
        """
        Plot the sail diagram contribution over a range of x.
        """
        y_vals = self.compute_contribution(x_range, epsilon_ir=epsilon_ir)
        
        plt.figure(figsize=(10, 6))
        plt.plot(x_range, y_vals, label=r'$\tilde{q}_{\rm sail}$')
        
        # Highlight the singular behavior at x=1
        plt.title(f"Sail Diagram Contribution ($p^z={self.pz}$ GeV, $\mu={self.mu}$ GeV)")
        plt.xlabel(r"Momentum Fraction $x$")
        plt.ylabel(r"$\tilde{q}_{\rm sail}(x)$")
        plt.grid(True, alpha=0.3)
        plt.legend()
        
        # Set reasonable y-limits, taking care of the singularity at x=1
        # We filter out extreme values for the plot limits to keep it readable
        finite_y = y_vals[np.isfinite(y_vals)]
        if len(finite_y) > 0:
            y_min, y_max = np.min(finite_y), np.max(finite_y)
            plt.ylim(y_min - 0.5*abs(y_min), y_max + 0.5*abs(y_max))
            
        print("Plot generated. Showing plot window.")
        plt.show()

# --- Example Usage ---
if __name__ == "__main__":
    # 1. Setup the Model with realistic parameters
    # Parameters derived from the realistic setup context:
    # alpha_s ~ 0.30, Pf ~ 3.0 GeV, mu ~ 2.0 GeV
    model = SailDiagramModel(alpha_s=0.30, Cf=4.0/3.0, pz=3.0, mu=2.0)
    
    # 2. Compute for specific values in the three regimes
    x_points = [-0.5, 0.5, 1.5]
    print(f"Calculating for x={x_points} with epsilon_IR = 1e-5 (approx 0):")
    for x in x_points:
        res = model.compute_contribution(x, epsilon_ir=1e-5) 
        print(f"  x = {x:4.1f}: tilde_q = {res:.4f}")

    # 3. Compute for a grid of x values in 0 < x < 1 to show structure
    # We should observe the negative sign and the divergence as x -> 1
    x_grid = np.linspace(0.1, 0.9, 9)
    print(f"\nCalculating for x in 0<x<1 grid:")
    for x in x_grid:
        res = model.compute_contribution(x, epsilon_ir=1e-5)
        print(f"  x = {x:.2f}: tilde_q = {res:.4f}")

    # 4. Generate a plot
    # Note: The values diverge near x=1 and x=0. The plot will show this trend.
    print("\nGenerating plot...")
    # We pass a small epsilon_ir to visualize the "regulated" divergence shape
    model.plot_distribution(epsilon_ir=1e-3)

```
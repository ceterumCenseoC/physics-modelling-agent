
```python
import numpy as np
import matplotlib.pyplot as plt
import sympy as sp

class CompositeParticleModel:
    """
    Implementation of the composite particle splitting/recombination model on a 1D lattice.
    
    The model derives the generating function Omega(x, g, lambda) analytically and provides
    methods for numerical evaluation and analysis.
    """
    
    def __init__(self):
        pass

    def generate_function_expr(self):
        """
        Returns the symbolic expression for the generating function Omega(x, g, lambda).
        Based on the derived formula:
        Omega = (1 - 2*lambda*x - sqrt((1 - 2*lambda*x)^2 - 2*g*x*(1 - sqrt(1 - 4*x^2)))) 
                / (g*x*(1 - sqrt(1 - 4*x^2)))
        """
        x, g_param, lam = sp.symbols('x g lambda', positive=True)
        
        # Define the inner square root term sqrt(1 - 4x^2)
        # Check domain validity for symbolic simplification later
        inner_sqrt = sp.sqrt(1 - 4*x**2)
        
        # Denominator term: (1 - sqrt(1 - 4x^2))
        denom_factor = 1 - inner_sqrt
        
        # The term K(x) = (1 - sqrt(...)) / 2. 
        # We substitute 2*K(x) into the formula directly where it appears.
        # The discriminant term is: (1 - 2*lambda*x)^2 - 2*g*x*(1 - sqrt(1 - 4*x^2))
        discriminant_term = (1 - 2*lam*x)**2 - 2*g_param*x*denom_factor
        
        # Main square root: sqrt(Discriminant)
        main_sqrt = sp.sqrt(discriminant_term)
        
        numerator = 1 - 2*lam*x - main_sqrt
        denominator = g_param * x * denom_factor
        
        omega_expr = numerator / denominator
        return omega_expr, (x, g_param, lam)

    def get_partition_function_series(self, g_val, lam_val, t_max=10):
        """
        Computes Z(t) for t = 0 to t_max by expanding the generating function analytically.
        Z(t) is the coefficient of x^t in the Taylor series expansion of Omega.
        
        Parameters:
        g_val (int): Number of distinct splitting ways.
        lam_val (float): Diffusion weight parameter.
        t_max (int): Maximum time step to compute.
        
        Returns:
        np.array: Array of Z(t) values.
        """
        expr, symbols = self.generate_function_expr()
        x_sym, g_sym, lam_sym = symbols
        
        # Substitute specific parameter values
        sub_expr = expr.subs({g_sym: g_val, lam_sym: lam_val})
        
        # Expand series up to x^t_max
        series = sp.series(sub_expr, x_sym, 0, t_max+1).removeO()
        
        # Extract coefficients
        z_vals = []
        for t in range(t_max + 1):
            coeff = sp.expand(series).coeff(x_sym, t)
            # Sympy returns exact rationals, convert to float for utility
            z_vals.append(float(coeff))
            
        return np.array(z_vals)

    def numerical_omega(self, x_val, g_val, lam_val):
        """
        Numerically evaluates Omega(x, g, lambda) for a specific scalar or array of x values.
        Uses numpy for efficient array operations if x_val is an array.
        
        Parameters:
        x_val (float or np.array): Fugacity parameter(s).
        g_val (int): Splitting factor.
        lam_val (float): Diffusion weight.
        
        Returns:
        float or np.array: The value of the generating function.
        """
        x = np.array(x_val, dtype=float)
        
        # Precompute terms to handle domain issues (x must be < 0.5 near real line)
        # 1 - 4*x^2
        val_1_minus_4x2 = 1 - 4 * x**2
        # Handle potential numerical errors near boundary or if complex values arise
        # In the physical domain x < 0.5, this is positive.
        
        sqrt_1_minus_4x2 = np.sqrt(val_1_minus_4x2)
        
        # Denominator factor: 1 - sqrt(1 - 4x^2)
        # If x is 0, this factor is 0, but the limit is defined. 
        # We handle the x=0 case or use epsilon.
        denom_factor = 1 - sqrt_1_minus_4x2
        
        # Discriminant term: (1 - 2*lambda*x)^2 - 2*g*x*(1 - sqrt(1 - 4x^2))
        disc_val = (1 - 2 * lam_val * x)**2 - 2 * g_val * x * denom_factor
        
        # Ensure we take the correct branch of the square root for the Omega function.
        # The solution requires the root that results in Omega(0)=1.
        # This corresponds to the negative sign in the numerator: 1 - 2lx - sqrt(disc)
        
        # If disc_val is negative, Omega becomes complex (hyper-critical region).
        # We return complex numbers in that case.
        sqrt_disc = np.sqrt(disc_val)
        
        numerator = 1 - 2 * lam_val * x - sqrt_disc
        denominator = g_val * x * denom_factor
        
        # Handle x=0 singularity analytically: limit should be 1
        # Using np.where to avoid division by zero warnings
        omega = np.divide(numerator, denominator, out=np.ones_like(numerator), where=(denominator != np.zeros_like(denominator)))
        
        return omega

    def find_critical_point(self, g_val, lam_val):
        """
        Finds the critical fugacity x_c where the generating function diverges (radius of convergence).
        This occurs when the discriminant of the quadratic equation for Omega is zero.
        (1 - 2*lambda*x)^2 - 2*g*x*(1 - sqrt(1 - 4*x^2)) = 0
        
        Parameters:
        g_val (int): Splitting factor.
        lam_val (float): Diffusion weight.
        
        Returns:
        float: The critical x value.
        """
        x_sym = sp.symbols('x', real=True, positive=True)
        
        # Equation: (1 - 2*lambda*x)^2 - 2*g*x*(1 - sqrt(1 - 4*x^2)) = 0
        # Note: We multiply by (1 + sqrt(1-4x^2))^2 to remove nested radicals, 
        # but direct solving is often sufficient for numerical approximation.
        
        disc_expr = (1 - 2*lam_val*x_sym)**2 - 2*g_val*x_sym*(1 - sp.sqrt(1 - 4*x_sym**2))
        
        # nsolve requires an initial guess. For random walks, x_c is usually near 0.5
        # We try a guess near 0.4 or 0.45 depending on parameters.
        try:
            xc_solution = sp.nsolve(disc_expr, 0.4, tol=1e-14, maxsteps=100)
            return float(xc_solution)
        except ValueError:
            # If 0.4 doesn't work, try closer to the singularity of simple RW
            try:
                xc_solution = sp.nsolve(disc_expr, 0.1, tol=1e-14, maxsteps=100)
                return float(xc_solution)
            except Exception as e:
                print(f"Could not find critical point for g={g_val}, lam={lam_val}: {e}")
                return None

    def plot_phase_diagram(self):
        """
        Generates a phase diagram showing the critical fugacity x_c as a function
        of the splitting factor g for different diffusion weights lambda.
        """
        g_range = np.arange(1, 6)  # g = 1, 2, 3, 4, 5
        lambdas = [0.1, 0.5, 1.0, 2.0]
        
        plt.figure(figsize=(10, 6))
        
        print("Computing critical points for phase diagram...")
        for lam in lambdas:
            critical_xs = []
            for g in g_range:
                xc = self.find_critical_point(g, lam)
                critical_xs.append(xc)
            plt.plot(g_range, critical_xs, 'o-', label=f'$\lambda = {lam}$')
            
        plt.xlabel('Splitting Factor $g$')
        plt.ylabel('Critical Fugacity $x_c$')
        plt.title('Phase Diagram: Critical Fugacity vs. Splitting Factor')
        plt.legend()
        plt.grid(True, linestyle='--', alpha=0.7)
        
        # Save or show plot
        plt.show(block=False)
        plt.savefig('phase_diagram.png')
        print("Plot saved to 'phase_diagram.png'")

    def plot_omega_series(self, g_val, lam_val, x_max=0.4):
        """
        Plots the generating function Omega(x) for a range of fugacity x.
        """
        x_vals = np.linspace(0.001, x_max, 100)
        
        # Calculate Omega numerically
        omega_vals = self.numerical_omega(x_vals, g_val, lam_val)
        
        plt.figure(figsize=(8, 5))
        plt.plot(x_vals, omega_vals.real, label='Re($\Omega$)', color='blue', linewidth=2)
        
        # Check if there is an imaginary part (in the unstable/disordered phase)
        if np.any(np.abs(omega_vals.imag) > 1e-6):
            plt.plot(x_vals, omega_vals.imag, label='Im($\Omega$)', color='red', linestyle='--')

        # Find critical point
        xc = self.find_critical_point(g_val, lam_val)
        if xc and xc < x_max:
            plt.axvline(x=xc, color='green', linestyle=':', label=f'$x_c \\approx {xc:.3f}$')
            plt.title(f'Generating Function $\Omega(x)$ for $g={g_val}, \lambda={lam_val}$\nDivergence at $x_c$')
        else:
            plt.title(f'Generating Function $\Omega(x)$ for $g={g_val}, \lambda={lam_val}$')

        plt.xlabel('Fugacity $x$')
        plt.ylabel('$\Omega(x, g, \lambda)$')
        plt.legend()
        plt.grid(True, alpha=0.5)
        plt.show(block=False)
        plt.savefig(f'omega_series_g{g_val}_lam{lam_val}.png')
        print(f"Plot saved to 'omega_series_g{g_val}_lam{lam_val}.png'")

    def print_analytical_result(self):
        """
        Prints the derived analytical formula using SymPy's pretty print.
        """
        expr, symbols = self.generate_function_expr()
        print("Analytical Derivation of Generating Function Omega(x, g, lambda):")
        print("Formula:")
        print("Omega = (1 - 2*lambda*x - sqrt((1 - 2*lambda*x)^2 - 2*g*x*(1 - sqrt(1 - 4*x^2)))) / (g*x*(1 - sqrt(1 - 4*x^2)))")
        print("\nSymPy Representation:")
        sp.pprint(expr)
        
        # Verify boundary condition Omega(x=0) = 1 via limit
        x, g, lam = symbols
        limit_zero = sp.limit(expr.subs({g: 2, lam: 0.5}), x, 0)
        print(f"\nVerification of Boundary Condition (Limit x->0): {limit_zero}")


# --- Main Execution Block ---
if __name__ == "__main__":
    model = CompositeParticleModel()
    
    # 1. Display the Analytical Formula
    model.print_analytical_result()
    
    # 2. Compute Partition Function Z(t) for a specific parameter set
    #    Let's use the recommended starting parameters:
    #    x (fugacity) is implicit in the series expansion terms, 
    #    but Z(t) is the coefficient.
    g = 2
    lam = 0.5
    t_max = 10
    
    print(f"\n--- Computing Partition Function Z(t) for g={g}, lambda={lam} ---")
    z_series = model.get_partition_function_series(g, lam, t_max)
    print(f"t :\t Z(t)")
    for t, z in enumerate(z_series):
        print(f"{t} :\t {z:.4f}")

    # 3. Generate Graphics
    print("\n--- Generating Graphics ---")
    
    # Plot Omega(x) for the baseline parameters
    model.plot_omega_series(g_val=g, lam_val=lam, x_max=0.45)
    
    # Generate Phase Diagram (optional, takes a few seconds to solve roots)
    # Uncomment the line below to generate the phase diagram
    # model.plot_phase_diagram()
    
    print("\nProcess complete.")
```
```python
import numpy as np
from scipy.optimize import root_scalar
from scipy.integrate import quad
import matplotlib
import matplotlib.pyplot as plt

# Ensure matplotlib works non-interactively if no display is available
matplotlib.use('Agg')

# ==========================================
# 1. Model Implementation and Setup
# ==========================================

class EfimovModel:
    def __init__(self):
        """
        Initialize the Efimov effect model with physical and mathematical constants.
        Units are dimensionless for this angular problem.
        """
        # Constant term in the transcendental equation: 8/sqrt(3)
        self.C = 8.0 / np.sqrt(3.0)
        self.s1 = None
        self.H_val = None
        self.N_s1 = None
        self.G_s1 = None
        self.P_s1 = None

    def phi_angular(self, s, alpha):
        """
        The unsymmetrized hyperangular component varphi(s, alpha).
        varphi(s, alpha) = sin(s * (pi/2 - alpha))
        """
        return np.sin(s * (np.pi / 2.0 - alpha))

    def F_func(self, s, alpha):
        """
        Function F(s, alpha) = varphi(s, alpha) / sin(2*alpha)
        """
        sin_2a = np.sin(2.0 * alpha)
        # Handle potential division by zero at boundaries if strictly necessary,
        # though sin(2*alpha) -> 0 is handled by the limit of F in physics.
        # For numerical integration, avoiding exact 0 and pi/2 is sufficient.
        # If sin_2a is very small, we might encounter warnings, but the limit is finite.
        # We perform the division directly.
        return self.phi_angular(s, alpha) / sin_2a

    def symmetrized_phi(self, s, alpha):
        """
        Calculate the unnormalized symmetrized wave function (1+Q)F(s, alpha).
        Here alpha corresponds to alpha_3 (angle related to pair r12).
        Symmetrization sums over particle permutations.
        Permutation relations for hyperangles in 3-body systems:
        Given alpha_3, we find alpha_1 such that:
        sin(alpha_1) = sin(alpha_3) / sqrt(sin^2(alpha_3) + 3/2)
        alpha_2 = pi/2 - alpha_1
        """
        # alpha_3 is the input variable
        a3 = alpha
        
        # Calculate alpha_1 based on geometric mapping
        sin_a3 = np.sin(a3)
        # Geometric identity for permuting particles in hyperspherical coordinates
        sin_a1 = sin_a3 / np.sqrt(sin_a3**2 + 1.5)
        
        # Clip value to [-1, 1] to avoid numerical noise arcsin errors
        sin_a1 = np.clip(sin_a1, -1.0, 1.0)
        
        a1_val = np.arcsin(sin_a1)
        
        # alpha_2 relation
        a2_val = np.pi / 2.0 - a1_val
        
        # Sum the contributions (1 + P13 + P23)F
        val = self.F_func(s, a3) + self.F_func(s, a1_val) + self.F_func(s, a2_val)
        return val

    def transcendental_equation(self, s):
        """
        The boundary condition equation:
        d(varphi)/dalpha @ 0 + C * varphi @ pi/3 = 0
        -s * cos(s*pi/2) + C * sin(s*pi/6) = 0
        """
        return -s * np.cos(s * np.pi / 2.0) + self.C * np.sin(s * np.pi / 6.0)

    def calculate_s1(self):
        """
        Solve for the first non-integer value of s (Efimov parameter).
        Scans the range [0, 2] for a root.
        """
        x_vals = np.linspace(0.01, 1.99, 500)
        f_vals = self.transcendental_equation(x_vals)
        
        roots = []
        for i in range(len(x_vals) - 1):
            if np.sign(f_vals[i]) != np.sign(f_vals[i+1]):
                try:
                    res = root_scalar(self.transcendental_equation, 
                                      bracket=[x_vals[i], x_vals[i+1]], 
                                      method='bisect')
                    if res.converged:
                        roots.append(res.root)
                except ValueError:
                    pass
        
        # Filter out integers (or near integers) and select the smallest positive
        real_roots = [r for r in roots if not np.isclose(r, np.round(r), atol=1e-4)]
        real_roots.sort()
        
        if not real_roots:
            # Fallback bisection in known range if scanning failed
            # s1 is known to be approx 1.006
            res = root_scalar(self.transcendental_equation, 
                              bracket=[1.0, 1.02], 
                              method='bisect')
            if res.converged:
                self.s1 = res.root
                return self.s1
            else:
                raise ValueError("Root finding failed.")

        self.s1 = real_roots[0]
        return self.s1

    def calculate_N_integrand(self, s, alpha):
        """
        Integrand for N(s): sin^2(2*alpha) * [(1+Q)F(s, alpha)]^2
        """
        sym_phi = self.symmetrized_phi(s, alpha)
        return (np.sin(2.0 * alpha)**2) * (sym_phi**2)

    def calculate_G_integrand(self, s, alpha):
        """
        Integrand for G(s): sin^2(2*alpha) * (1+Q)F(s, alpha)
        """
        sym_phi = self.symmetrized_phi(s, alpha)
        return (np.sin(2.0 * alpha)**2) * (sym_phi)

    def calculate_H(self):
        """
        Calculate H = integral_0^pi/2 sin^2(2*alpha) dalpha
        """
        res, _ = quad(lambda x: np.sin(2*x)**2, 0, np.pi/2)
        self.H_val = res
        return self.H_val

    def run(self):
        print("Executing Efimov Model Calculations...")
        
        # 1. Calculate s1
        s1 = self.calculate_s1()
        print(f"Calculated s1: {s1:.5f}")
        
        # 2. Calculate H (Numeric verification)
        H_num = self.calculate_H()
        print(f"Calculated H (Numeric): {H_num:.5f}")
        print(f"Calculated H (Analytic pi/4): {np.pi/4:.5f}")
        
        # 3. Calculate N(s1) (Raw normalization constant)
        # Integral of sin^2(alpha) * ((1+Q)F)^2
        # Using full_output=0 to get just result, limit subdiv increases for oscillatory integrand
        N_raw, N_err = quad(lambda x: self.calculate_N_integrand(s1, x), 0, np.pi/2, limit=200)
        self.N_s1 = N_raw
        print(f"Calculated N(s1) [Raw Norm]: {self.N_s1:.5f} (err: {N_err:.2e})")

        # 4. Calculate G(s1) (Raw overlap numerator)
        G_raw, G_err = quad(lambda x: self.calculate_G_integrand(s1, x), 0, np.pi/2, limit=200)
        self.G_s1 = G_raw
        print(f"Calculated G(s1) [Raw Overlap]: {self.G_s1:.5f} (err: {G_err:.2e})")

        # 5. Calculate P(s1)
        # P = G^2 / (N * H)
        # Verified context: G and N refer to raw integrals of unnormalized wavefunction in these formulas
        if self.H_val > 0 and self.N_s1 > 0:
            self.P_s1 = (self.G_s1**2) / (self.N_s1 * self.H_val)
            print(f"Calculated P(s1): {self.P_s1:.5f}")
        else:
            print("Error: Invalid values for H or N resulting in division by zero.")
            self.P_s1 = 0

        return s1, self.H_val, self.N_s1, self.G_s1, self.P_s1

# ==========================================
# 2. Graphics Generation
# ==========================================

def plot_results(model):
    """
    Generate and save sensible graphics for the Efimov model.
    """
    print("Generating plots...")
    
    # Plot 1: The Transcendental Equation and Root Finding
    x = np.linspace(0.01, 2.0, 400)
    y = model.transcendental_equation(x)
    
    plt.figure(figsize=(10, 6))
    plt.plot(x, y, label=r'$-s \cos(s\pi/2) + \frac{8}{\sqrt{3}} \sin(s\pi/6)$')
    plt.axhline(0, color='black', linewidth=0.8)
    plt.axvline(model.s1, color='red', linestyle='--', label=f'Solution $s_1 \\approx {model.s1:.4f}$')
    plt.title('Solving the Efimov Characteristic Equation')
    plt.xlabel('s')
    plt.ylabel('f(s)')
    plt.legend()
    plt.grid(True, alpha=0.3)
    plt.savefig('transcendental_equation.png')
    plt.close()
    print("Saved plot: transcendental_equation.png")
    
    # Plot 2: Normalized Hyperangular Wavefunctions
    # Avoid exact 0 and pi/2 to prevent division by zero artifacts in F_func (though limits are finite)
    alpha = np.linspace(0.001, np.pi/2 - 0.001, 400)
    
    # Non-interacting/Hyperspherical Harmonic density
    # Unnormalized Non-interacting shape: sin^2(2a)
    # Normalized density: sin^2(2a) / H
    
    # Calculate Efimov wavefunction components
    psi_Efimov = np.array([model.symmetrized_phi(model.s1, a) for a in alpha])
    norm_factor = np.sqrt(model.N_s1)
    psi_Efimov_norm = psi_Efimov / norm_factor
    
    prob_density_Efimov = (np.sin(2*alpha)**2) * (psi_Efimov_norm**2)
    prob_density_NonInt = (np.sin(2*alpha)**2) / model.H_val
    
    plt.figure(figsize=(10, 6))
    plt.plot(alpha, prob_density_NonInt, label='Non-interacting Threshold State', linestyle='--')
    plt.plot(alpha, prob_density_Efimov, label=f'Efimov State ($s_1={model.s1:.3f}$)')
    plt.title('Hyperangular Probability Densities')
    plt.xlabel(r'Hyperangle $\alpha$')
    plt.ylabel(r'Probability Density $\propto \sin^2(2\alpha)|\phi|^2$')
    plt.legend()
    plt.grid(True, alpha=0.3)
    plt.savefig('probability_densities.png')
    plt.close()
    print("Saved plot: probability_densities.png")

# ==========================================
# 3. Main Execution
# ==========================================

if __name__ == "__main__":
    # Instantiate and run model
    efimov = EfimovModel()
    
    try:
        efimov.run()
        
        # Print summary of required values
        print("-" * 30)
        print("SUMMARY OF RESULTS")
        print("-" * 30)
        print(f"s_1       : {efimov.s1:.3f}")
        print(f"H         : {efimov.H_val:.3f}")
        print(f"P(s_1)    : {efimov.P_s1:.3f}")
        print("-" * 30)
        
        # Generate Graphics
        plot_results(efimov)
        
    except Exception as e:
        print(f"An error occurred during execution: {e}")
```
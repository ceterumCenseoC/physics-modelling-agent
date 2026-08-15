
```python
import numpy as np
from scipy.optimize import root_scalar
from scipy.integrate import quad
import matplotlib.pyplot as plt

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
        return self.phi_angular(s, alpha) / np.sin(2.0 * alpha)

    def symmetrized_phi(self, s, alpha):
        """
        Calculate the symmetrized wave function component (1+Q)F(s, alpha).
        We map the single variable alpha to the full hyperangular dependency.
        
        alpha = alpha_3 corresponds to r_12 / rho_3.
        alpha_1 = arcsin( sin(alpha_3) / sqrt(sin^2(alpha_3) + 3/2) )
        alpha_2 = pi/2 - alpha_1
        Note: F(s, alpha) has specific symmetry properties. F(s, pi/2 - alpha) = F(s, alpha).
        The operator Q effectively sums over the particle permutations expressed in 
        hyperangular coordinates.
        """
        # alpha_3 is just the input alpha
        a3 = alpha
        
        # Calculate alpha_1 based on geometry
        # This corresponds to the mapping angle in the (alpha_1, alpha_3) plane
        # Given r_31 and rho_2.
        # Using geometric identities for hyperangles in 3-body systems.
        sin_a3 = np.sin(a3)
        sin_a1 = sin_a3 / np.sqrt(sin_a3**2 + 1.5)
        a1 = np.arcsin(sin_a1)
        
        # Due to symmetry of F(s, alpha) around pi/4, and identical bosons:
        # The (1+Q) operator acts on the hyperangular function. 
        # In terms of alpha_3, the other contributions map to regions of the 
        # interval [0, pi/2] or require a Jacobian factor if considered as a simple sum.
        # However, the standard approach for the overlap P involves integrating
        # over the full 5D hyperangular solid angle. 
        
        # Geometric identity: The sum (1+Q) acting on the basis function 
        # effectively sums the function evaluated at the three equivalent angles.
        # A simpler way for identical bosons mapping [0, pi/2] is provided by 
        # Kartavtsev and Malykh (similar to Eq 15 in context of Efimov):
        # Fully symmetric wavefunction Phi_sym ~ F(s, a) + 2*cos(2a)*F(s, pi/2-a) 
        # depends on specific basis. Let's stick to the explicit definition provided 
        # or standard mapping.
        
        # Using mapping:
        # a1 = acos( cos(a) / sqrt(cos^2(a) + 3*sin^2(a)) )
        # Standard geometric relation:
        # sin(a1) = sin(a3) / sqrt(sin^2(alpha_3) + 3/2)
        
        # alpha_2 is related. For alpha_3 in [0, pi/2], alpha_1 covers [0, pi/2].
        # For identical bosons, phi is symmetric.
        
        # Analytic derivation can be complex, so we use the geometric mapping numerically.
        # Permutation P13 -> alpha_1
        a1_val = a1
        
        # Permutation P23 -> alpha_2
        # In the plane of alpha_1, alpha_3, the third angle is determined.
        # However, for identical bosons, the hyperangles are just permutations.
        # The Jacobian for the integral d(omega) = sin^2(2alpha) dalpha * constant.
        # Since we are looking at the wavefunction value at a point:
        # The term (1+Q)F = F(a3) + F(a1) + F(a2)
        
        # We need a2. For resonance, a1 + a2 + pi/2 = pi ?? No.
        # Relation: alpha_1 = arcsin( sin(alpha_3) / sqrt(sin^2(alpha_3) + 1.5) )
        # alpha_2 = pi/2 - alpha_1
        
        a2_val = np.pi/2.0 - a1_val
        
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
        Solve for the first non-integer value of s.
        Range: [0, 2] is a reasonable start, as the next integer is 2.
        """
        # Scan for sign changes
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
            raise ValueError("No non-integer root found.")
            
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
        Note: Usually overlap is defined against the non-interacting state.
        The non-interacting state is proportional to sin^2(2*alpha) in the wavefunction,
        or strictly speaking unit function in the probability density *after* measure.
        
        Problem states:
        P(s) = G(s)^2 / (N(s) H)
        G(s) = integral sin^2(2a) phi(s,a)
        N(s) = integral sin^2(2a) phi(s,a)^2
        H = integral sin^2(2a)
        
        Phi(s,a) in the formula is defined as (1+Q)F / sqrt(N).
        So:
        Numerator G(s) uses normalized phi:
        G = Integral [ sin^2 * (SymPhi / sqrt(N)) ] = (1/sqrt(N)) * Integral [ sin^2 * SymPhi ]
        
        Let G_raw = Integral [ sin^2 * SymPhi ]
        Let N_raw = Integral [ sin^2 * SymPhi^2 ]
        
        Formula P = (Norm_G)^2 / (Norm_Norm * H)
        Formula P = (G_raw / sqrt(N_raw))^2 / (1 * H) = G_raw^2 / (N_raw * H)
        
        Wait, N(s) in the prompt refers to the integral of sin^2 * phi^2.
        Since phi is normalized by definition using N(s), the integral of sin^2 * phi^2 is 1.
        Let's re-read carefully.
        "w.f. ... = (1+Q)F / sqrt(N(s))"
        "N(s) = integral sin^2 ... (wave function)^2"
        This implies the definition of N(s) IS the normalization constant such that the integral is 1.
        
        If so, N(s) in the formula P(s) = G^2 / (N H) refers to the Normalization Constant in denominator of Phi.
        Let's call the constant Z. Phi = SymPhi / sqrt(Z).
        N_formula = integral sin^2 Phi^2 = 1.
        
        Does the prompt mean N(s) is the RAW integral?
        "N(s) is the normalization factor." usually implies the Z.
        Let's assume standard definitions:
        Phi = SymPhi / sqrt(Z)
        Z = Integral sin^2 SymPhi^2
        
        Then the prompt asks to calculate "N(s)". If I compute the integral of the normalized wavefunction, it is 1.
        If I compute the raw integral, it is Z.
        Given the context "calculate N(s)... and use these results to obtain P(s)",
        and P contains N in denominator, it is mathematically consistent that N refers to 
        the squared norm of the *unnormalized* function (Z), or the variable in the denominator of Phi.
        
        Let's calculate Z (Raw Norm).
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
        # 1. Calculate s1
        s1 = self.calculate_s1()
        print(f"Calculated s1: {s1:.4f}")
        
        # 2. Calculate H (Analytic is pi/4, but let's do numeric to verify or as asked)
        H_num = self.calculate_H()
        print(f"Calculated H (Numeric): {H_num:.4f}")
        print(f"Calculated H (Analytic pi/4): {np.pi/4:.4f}")
        
        # 3. Calculate N(s) (Raw normalization constant)
        # Integral of sin^2(alpha) * ((1+Q)F)^2
        N integrand is sin^2 * SymPhi^2
        N_raw, N_err = quad(lambda x: self.calculate_N_integrand(s1, x), 0, np.pi/2)
        self.N_s1 = N_raw
        print(f"Calculated N(s1) [Raw Norm]: {self.N_s1:.4f}")

        # 4. Calculate G(s) (Raw overlap numerator)
        # Integral of sin^2 * SymPhi
        G_raw, G_err = quad(lambda x: self.calculate_G_integrand(s1, x), 0, np.pi/2)
        self.G_s1 = G_raw
        print(f"Calculated G(s1) [Raw Overlap]: {self.G_s1:.4f}")

        # 5. Calculate P(s1)
        # P = G^2 / (N * H)
        # Here G is the numerator of the overlap, G_raw.
        # The normalization factor is 1/sqrt(N_raw).
        # The formula given in prompt P = G(s)^2 / (N(s)H)
        # If G(s) is defined with normalized w.f.: G(s) = 1/sqrt(N) * G_raw.
        # Then G(s)^2 = 1/N * G_raw^2.
        # P = (G_raw^2 / N) / (1 * H) = G_raw^2 / (N * H).
        # This matches the structure.
        
        self.P_s1 = (self.G_s1**2) / (self.N_s1 * self.H_val)
        print(f"Calculated P(s1): {self.P_s1:.4f}")

# ==========================================
# 2. Graphics Generation
# ==========================================

def plot_results(model):
    """
    Generate sensible graphics for the Efimov model.
    """
    
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
    plt.show()
    
    # Plot 2: Normalized Hyperangular Wavefunctions
    alpha = np.linspace(0.01, np.pi/2 - 0.01, 400)
    
    # Non-interacting/Hyperspherical Harmonic (related to H)
    # psi_nonint ~ 1 (normalized), but density is sin^2(2a). 
    # The "shape" of the zero-threshold constant wavefunction in the Faddeev basis is often cited.
    # Let's plot the probability density.
    # Unnormalized Non-interacting density: dP/dalpha ~ sin^2(2a)
    # Normalized: (sin^2(2a)) / H
    
    psi_Efimov = np.array([model.symmetrized_phi(model.s1, a) for a in alpha])
    # Normalization factor
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
    plt.show()

# ==========================================
# 3. Main Execution
# ==========================================

if __name__ == "__main__":
    # Instantiate and run model
    efimov = EfimovModel()
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
```
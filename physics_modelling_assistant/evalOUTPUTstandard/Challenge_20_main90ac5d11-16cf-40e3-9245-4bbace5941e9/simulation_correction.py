```python
import numpy as np
import matplotlib.pyplot as plt
from scipy.constants import c, epsilon_0, pi, hbar

# ==========================================
# 1. Model Implementation
# ==========================================

class CoupledEllipsoidsModel:
    def __init__(self, a, b, rho, eps_r, P0, w0, R):
        """
        Initialize parameters for two coupled dielectric ellipsoids in optical tweezers.
        
        Parameters:
        -----------
        a : float
            Semi-major axis of the ellipsoid (meters).
        b : float
            Semi-minor axis of the ellipsoid (meters).
        rho : float
            Mass density of the ellipsoid material (kg/m^3).
        eps_r : float
            Relative permittivity (dielectric constant) of the material.
        P0 : float
            Laser power (Watts).
        w0 : float
            Beam waist radius (meters).
        R : float
            Separation distance between the two ellipsoids along the x-axis (meters).
        """
        self.a = a
        self.b = b
        self.rho = rho
        self.eps_r = eps_r
        self.P0 = P0
        self.w0 = w0
        self.R = R
        
        # Derived Geometric Properties
        self.V = (4/3) * pi * a * b**2  # Volume
        self.I = (8/15) * pi * rho * a * b**4  # Moment of Inertia about x-axis
        
    def get_depolarization_factors(self):
        """
        Calculate depolarization factors L_parallel and L_perpendicular.
        Using analytical approximations provided in the derivation.
        """
        # L_parallel approx b^4 / (2a^2b^2 + b^4) = 1 / (2(a/b)^2 + 1)
        L_parallel = 1 / (2 * (self.a/self.b)**2 + 1)
        
        # For a prolate spheroid, sum of L's = 1. Due to symmetry in y and z axes:
        L_perp = (1 - L_parallel) / 2
        
        return L_parallel, L_perp

    def get_polarizabilities(self):
        """
        Calculate polarizability components parallel and perpendicular to the major axis.
        alpha = epsilon_0 * V * (eps_r - 1) / (1 + L * (eps_r - 1))
        """
        L_para, L_perp = self.get_depolarization_factors()
        
        term_numerator = epsilon_0 * self.V * (self.eps_r - 1)
        
        alpha_parallel = term_numerator / (1 + L_para * (self.eps_r - 1))
        alpha_perp = term_numerator / (1 + L_perp * (self.eps_r - 1))
        
        return alpha_parallel, alpha_perp

    def calculate_trap_frequency(self):
        """
        Derive the torsional trap frequency omega_t.
        omega_t = sqrt( kappa_theta / I )
        kappa_theta = 4 * P0 * (alpha_parallel - alpha_perp) / (pi * c * w0^2)
        
        Returns:
        --------
        omega_t : float
            Torsional trap frequency in rad/s.
        """
        alpha_par, alpha_perp = self.get_polarizabilities()
        
        # Numerator term inside sqrt: 4 * P0 * (alpha_par - alpha_perp)
        num = 4 * self.P0 * (alpha_par - alpha_perp)
        
        # Denominator term inside sqrt: pi * c * w0^2 * I
        denom = pi * c * self.w0**2 * self.I
        
        kappa_theta = num / denom
        omega_t = np.sqrt(kappa_theta / self.I)
        
        return omega_t

    def calculate_coupling_strength(self, omega_t):
        """
        Derive the coupling strength g.
        Based on the corrected dimensional analysis:
        g = (P0 * V^2 * chi_parallel^2) / (2 * pi^2 * c * w0^2 * R^3 * I * omega_t)
        where chi_parallel = (eps_r - 1) / (1 + L_par * (eps_r - 1))
        
        Note: This formula is derived from kappa_12 = alpha_par^2 * E0^2 / (4*pi*eps_0*R^3)
        but correcting for units where alpha includes epsilon_0 epsilon_r factors effectively.
        Here we use the direct substitution from the 'Corrected Formula' section:
        g = (P0 V^2 (eps_r - 1)^2) / (2 pi^2 c w0^2 R^3 I omega_t) * (1 / (1 + L_par(eps_r - 1))^2)
        
        Returns:
        --------
        g : float
            Coupling strength in rad/s.
        """
        L_par, _ = self.get_depolarization_factors()
        chi_term = (self.eps_r - 1) / (1 + L_par * (self.eps_r - 1))
        
        # Factor 1: P0 * V^2
        num_1 = self.P0 * self.V**2
        
        # Factor 2: chi_term^2
        num_2 = chi_term**2
        
        # Denominator: 2 * pi^2 * c * w0^2 * R^3 * I * omega_t
        denom = 2 * pi**2 * c * self.w0**2 * self.R**3 * self.I * omega_t
        
        g = (num_1 * num_2) / denom
        return g

# ==========================================
# 2. Simulation Setup with Defined Parameters
# ==========================================

# Instantiate the model with parameters derived from the initialization guide
# Parameters: [a, b, rho, eps_r, P0, w0, R]
# Units: [m, m, kg/m^3, -, W, m, m]

a = 1.5e-6        # 1.5 um
b = 0.5e-6        # 0.5 um
rho = 2000.0      # 2000 kg/m^3 (Silica)
eps_r = 2.1       # n^2 approx 2.1
P0 = 0.1          # 100 mW
w0 = 1.0e-6       # 1.0 um waist
R = 3.0e-6        # 3.0 um separation

model = CoupledEllipsoidsModel(a, b, rho, eps_r, P0, w0, R)

# ==========================================
# 3. Calculation of Results
# ==========================================

omega_t = model.calculate_trap_frequency()
g = model.calculate_coupling_strength(omega_t)

# Output the results
print("-" * 60)
print("OPTICAL TWEEZERS COUPLED ELLIPSOIDS MODEL RESULTS")
print("-" * 60)
print(f"Input Parameters:")
print(f"  Semi-major axis (a):    {a*1e6:.2f} um")
print(f"  Semi-minor axis (b):    {b*1e6:.2f} um")
print(f"  Density (rho):          {rho:.0f} kg/m^3")
print(f"  Relative Permittivity:  {eps_r:.2f}")
print(f"  Laser Power (P0):       {P0*1000:.0f} mW")
print(f"  Beam Waist (w0):        {w0*1e6:.2f} um")
print(f"  Separation (R):         {R*1e6:.2f} um")
print("-" * 60)

# Convert Omega to Hz for readability
omega_t_hz = omega_t / (2 * pi)
g_hz = g / (2 * pi)

print(f"Derived Dynamic Properties:")
print(f"  Torsional Freq (omega_t): {omega_t:.2f} rad/s  ({omega_t_hz:.2f} Hz)")
print(f"  Coupling Strength (g):    {g:.4f} rad/s   ({g_hz:.4f} Hz)")

# Check regimes
g_ratio = g / omega_t
print(f"\nRegime Analysis:")
print(f"  Coupling Ratio (g/omega_t): {g_ratio:.4f}")
if g_ratio > 0.1:
    print("  -> Strong coupling regime (Fast energy exchange)")
elif g_ratio > 0.01:
    print("  -> Intermediate coupling")
else:
    print("  -> Weak coupling regime")

# Check Hamiltonian coefficients
H_coeff_local = hbar * omega_t
H_coeff_coup = hbar * g
print(f"\nHamiltonian Energy Scales:")
print(f"  Local term (hbar*omega_t): {H_coeff_local:.2e} J")
print(f"  Coupling term (hbar*g):    {H_coeff_coup:.2e} J")

# ==========================================
# 4. Graphics: Dependence on Separation
# ==========================================

plt.figure(figsize=(10, 6))

# Define a range of separations R
# We vary from slightly touching (approx 2a) to 10um
R_min = 2 * a + 0.1e-6 # slightly touching
R_values = np.linspace(R_min, 10e-6, 200)

g_values = []

# Calculate g for each separation
for r_val in R_values:
    # We update the model's R parameter temporarily
    temp_model = CoupledEllipsoidsModel(a, b, rho, eps_r, P0, w0, r_val)
    # Omega_t is independent of R in this model (decoupled traps approximation)
    current_omega_t = omega_t 
    g_val = temp_model.calculate_coupling_strength(current_omega_t)
    g_values.append(g_val)

g_values = np.array(g_values)

# Plot
plt.plot(R_values * 1e6, g_values / (2 * np.pi), linewidth=2, color='blue')
plt.title(f'Coupling Strength $g$ vs. Separation Distance $R$\n'
          f'($P_0={P0*1000:.0f}$mW, $w_0={w0*1e6:.1f}$$\mu$m, $a={a*1e6:.1f}$$\mu$m)', fontsize=14)
plt.xlabel('Separation Distance $R$ [$\mu$m]', fontsize=12)
plt.ylabel('Coupling Strength $g / 2\pi$ [Hz]', fontsize=12)
plt.grid(True, which='both', linestyle='--', alpha=0.7)

# Highlight the initial R
plt.axvline(R * 1e6, color='red', linestyle='--', label=f'Operating Point $R={R*1e6:.1f}\mu m$')
plt.legend()

plt.tight_layout()
plt.show()
```
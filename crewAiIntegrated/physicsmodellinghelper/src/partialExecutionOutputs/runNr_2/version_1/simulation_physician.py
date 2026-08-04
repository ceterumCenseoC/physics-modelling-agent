

```python
import numpy as np
import matplotlib.pyplot as plt

# =============================================================================
# Physical Constants (SI Units)
# =============================================================================
e = 1.602176634e-19      # Elementary charge (C)
mu_B = 9.2740100783e-24  # Bohr magneton (J/T or A*m^2)
hbar = 1.054571817e-34   # Reduced Planck constant (J*s)

# =============================================================================
# Model Implementation: Direct Edelstein Effect (DEE) in Rashba 2DEG
# =============================================================================
class EdelsteinModel:
    """
    Implements the Direct Edelstein Effect for a Rashba fermion at the Gamma point.
    Strictly follows the provided Hamiltonian, dispersion, and susceptibility formulas.
    """
    def __init__(self, m, alpha, tau, EF):
        """
        Parameters:
            m (float): Effective carrier mass (kg)
            alpha (float): Rashba spin-orbit coupling strength (J*m)
            tau (float): Momentum relaxation time (s)
            EF (float): Fermi energy measured from band crossing (J)
        """
        self.m = m
        self.alpha = alpha
        self.tau = tau
        self.EF = EF
        
        # Crossover energy between LDR and HDR regimes: Ec = m*alpha^2 / hbar^2
        self.Ec = (m * alpha**2) / hbar**2
        
        # Common prefactor from dimensional analysis correction
        self.prefactor = (e * mu_B * tau) / (2 * np.pi * hbar**2)

    def get_susceptibility(self, EF=None):
        """
        Computes the scalar Edelstein susceptibility chi_Ed.
        Handles regime switching automatically based on EF relative to Ec.
        Returns chi_Ed in SI units (A/V).
        """
        if EF is None:
            EF = self.EF
            
        # High-Density Regime (HDR): Both chiral bands occupied
        if EF >= self.Ec:
            chi = self.prefactor * self.m * self.alpha
        # Low-Density Regime (LDR): Only lower band occupied
        else:
            chi = self.prefactor * np.sqrt(self.m**2 * self.alpha**2 + 2 * self.m * EF)
            
        return chi

    def get_magnetization_vector(self, E_mag, phi_E):
        """
        Computes the magnetization vector M for a given electric field magnitude and angle.
        M = chi_Ed * (z x E)
        E = E_mag * [cos(phi_E), sin(phi_E), 0]
        z x E = E_mag * [-sin(phi_E), cos(phi_E), 0]
        """
        chi = self.get_susceptibility()
        M_x = -chi * E_mag * np.sin(phi_E)
        M_y =  chi * E_mag * np.cos(phi_E)
        M_z = 0.0
        return np.array([M_x, M_y, M_z])

    def get_magnetization_magnitude(self, E_mag):
        """Linear response magnitude: |M| = chi_Ed * E"""
        return self.get_susceptibility() * E_mag

# =============================================================================
# Baseline Parameters (SI Units) - Derived from experimental 2DEG systems
# =============================================================================
m0 = 3.92e-32         # Effective mass (kg) ~ 0.043 m_e
alpha0 = 1.60e-20     # Rashba coupling (J*m) ~ 0.1 eV*A
tau0 = 1.0e-12        # Relaxation time (s) ~ 1 ps
EF0 = 1.60e-21        # Fermi energy (J) ~ 10 meV
E0 = 5.0e3            # Electric field (V/m)

# Instantiate model
model = EdelsteinModel(m0, alpha0, tau0, EF0)

# =============================================================================
# Graphics Generation
# =============================================================================
fig, axs = plt.subplots(2, 2, figsize=(14, 11))
fig.suptitle("Direct Edelstein Effect in Isotropic Rashba 2DEG", fontsize=16, fontweight='bold', y=0.995)

# --- Plot 1: Magnetization Magnitude vs Electric Field Strength ---
E_vals = np.linspace(0, 2*E0, 100)
# Compare HDR and LDR responses by fixing EF in different regimes
chi_HDR_reg = model.get_susceptibility(EF=10*model.Ec)
chi_LDR_reg = model.get_susceptibility(EF=model.EF)

axs[0,0].plot(E_vals, chi_HDR_reg * E_vals, 'b-', linewidth=2, label='High-Density Regime (HDR)')
axs[0,0].plot(E_vals, chi_LDR_reg * E_vals, 'r-', linewidth=2, label='Low-Density Regime (LDR)')
axs[0,0].plot(E0, chi_LDR_reg * E0, 'ko', markersize=8, label='Baseline Operating Point')
axs[0,0].set_xlabel('Electric Field $E$ (V/m)', fontsize=12)
axs[0,0].set_ylabel('Magnetization Magnitude $|\\mathbf{M}|$ (A/m)', fontsize=12)
axs[0,0].set_title('1. Linear Response: $|\\mathbf{M}|$ vs $E$', fontsize=13)
axs[0,0].legend(fontsize=10)
axs[0,0].grid(True, alpha=0.3)

# --- Plot 2: Susceptibility vs Fermi Energy (Carrier Density) ---
EF_vals = np.linspace(0, 10*model.Ec, 200)
chi_vs_EF = np.array([model.get_susceptibility(EF=ef) for ef in EF_vals])

axs[0,1].plot(EF_vals/1e-22, chi_vs_EF * 1e10, 'k-', linewidth=2)
axs[0,1].axvline(model.Ec/1e-22, color='green', linestyle='--', linewidth=1.5, label=f'Crossover $E_c = m\\alpha^2/\\hbar^2$')
axs[0,1].axhline(chi_HDR_reg * 1e10, color='blue', linestyle=':', linewidth=1.5, label='HDR Plateau')
axs[0,1].fill_between([0, EF_vals[-1]/1e-22], 0, chi_vs_EF[-1]*1e10, 
                       where=(EF_vals <= model.Ec), alpha=0.2, color='orange', label='LDR Region')
axs[0,1].set_xlabel('Fermi Energy $E_F$ ($\\times 10^{-22}$ J)', fontsize=12)
axs[0,1].set_ylabel('Susceptibility $\\chi_{Ed}$ ($\\times 10^{10}$ A/V)', fontsize=12)
axs[0,1].set_title('2. Density Dependence: $\\chi_{Ed}$ vs $E_F$', fontsize=13)
axs[0,1].legend(fontsize=10)
axs[0,1].grid(True, alpha=0.3)

# --- Plot 3: Magnetization Direction vs Electric Field Angle ---
# Demonstrates M = chi * (z x E) => M is strictly perpendicular to E
phi_vals = np.linspace(0, 2*np.pi, 12, endpoint=False)
x_E = np.cos(phi_vals)
y_E = np.sin(phi_vals)
x_M = -np.sin(phi_vals)
y_M = np.cos(phi_vals)

axs[1,0].quiver(np.zeros_like(phi_vals), np.zeros_like(phi_vals), x_E, y_E, 
                color='blue', angles='xy', scale_units='xy', scale=1, width=0.015, label='$\\mathbf{E}$')
axs[1,0].quiver(np.zeros_like(phi_vals), np.zeros_like(phi_vals), x_M, y_M, 
                color='red', angles='xy', scale_units='xy', scale=1, width=0.015, label='$\\mathbf{M}$')
circle = plt.Circle((0,0), 1.5, color='gray', fill=False, linestyle='--', linewidth=1)
axs[1,0].add_artist(circle)
axs[1,0].set_xlim(-2, 2)
axs[1,0].set_ylim(-2, 2)
axs[1,0].set_aspect('equal')
axs[1,0].set_xlabel('$x$ (arbitrary units)', fontsize=12)
axs[1,0].set_ylabel('$y$ (arbitrary units)', fontsize=12)
axs[1,0].set_title('3. Vector Relationship: $\\mathbf{M} = \\chi_{Ed} (\\hat{z} \\times \\mathbf{E})$', fontsize=13)
axs[1,0].legend(fontsize=10)
axs[1,0].grid(True, alpha=0.3)

# --- Plot 4: Susceptibility vs Rashba Coupling Strength ---
alpha_vals = np.linspace(0.1*alpha0, 5*alpha0, 100)
# Calculate chi for varying alpha, keeping EF fixed (LDR) and High EF (HDR)
chi_alpha_arr = []
for a in alpha_vals:
    # Recalculate regime boundaries for each alpha
    Ec_a = m0 * a**2 / hbar**2
    pf = (e * mu_B * tau0) / (2 * np.pi * hbar**2)
    if EF0 >= Ec_a:
        chi_alpha_arr.append(pf * m0 * a)
    else:
        chi_alpha_arr.append(pf * np.sqrt(m0**2 * a**2 + 2 * m0 * EF0))
chi_alpha_arr = np.array(chi_alpha_arr)

# HDR always scales linearly
chi_HDR_alpha = (e * mu_B * tau0) / (2 * np.pi * hbar**2) * m0 * alpha_vals

axs[1,1].plot(alpha_vals/1e-20, chi_alpha_arr * 1e10, 'r-', linewidth=2, label=f'LDR ($E_F$ fixed)')
axs[1,1].plot(alpha_vals/1e-20, chi_HDR_alpha * 1e10, 'b-', linewidth=2, label='HDR ($E_F \\gg E_c$)')
axs[1,1].axvline(alpha0/1e-20, color='gray', linestyle=':', linewidth=1.5, label='Baseline $\\alpha$')
axs[1,1].set_xlabel('Rashba Coupling $\\alpha$ ($\\times 10^{-20}$ J·m)', fontsize=12)
axs[1,1].set_ylabel('Susceptibility $\\chi_{Ed}$ ($\\times 10^{10}$ A/V)', fontsize=12)
axs[1,1].set_title('4. SOC Dependence: $\\chi_{Ed}$ vs $\\alpha$', fontsize=13)
axs[1,1].legend(fontsize=10)
axs[1,1].grid(True, alpha=0.3)

plt.tight_layout()
plt.show()

# =============================================================================
# Numerical Output for Baseline Configuration
# =============================================================================
print("="*60)
print("BASELINE MODEL OUTPUT")
print("="*60)
print(f"Parameters: m={m0:.2e} kg, alpha={alpha0:.2e} J*m, tau={tau0:.2e} s")
print(f"Fermi Energy: EF={EF0:.2e} J | Crossover: Ec={model.Ec:.2e} J")
print(f"Operating Regime: {'HDR' if EF0 >= model.Ec else 'LDR'}")
print("-"*60)

chi_base = model.get_susceptibility()
print(f"Edelstein Susceptibility: chi_Ed = {chi_base:.4e} A/V")

# Test different E field magnitudes and directions
angles_deg = [0, 45, 90, 135, 180]
print("\nMagnetization Vector M (A/m) for varying E-field directions (|E| = 5000 V/m):")
for deg in angles_deg:
    phi = np.deg2rad(deg)
    M_vec = model.get_magnetization_vector(E0, phi)
    mag = np.linalg.norm(M_vec)
    print(f"  E angle = {deg:3d}° | M = [{M_vec[0]:9.4e}, {M_vec[1]:9.4e}, {M_vec[2]:9.4e}] | |M| = {mag:.4e}")
print("="*60)
```
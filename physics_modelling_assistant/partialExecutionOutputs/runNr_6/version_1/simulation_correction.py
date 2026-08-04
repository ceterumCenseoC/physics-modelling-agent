
```python
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.gridspec import GridSpec

# ==========================================
# 1. Physical Constants and Model Parameters
# ==========================================

# Fundamental Constants
hbar = 1.0545718e-34       # Reduced Planck constant (J*s)
e_charge = 1.60217663e-19  # Elementary charge (C)
m_e = 9.10938356e-31       # Electron mass (kg)
mu_B = 9.27400999e-24      # Bohr magneton (J/T)

# Model Parameters (Based on InAs-like 2DEG)
m_eff = 0.023 * m_e        # Effective mass (kg)
alpha_eV_A = 100.0         # Rashba parameter (eV*Angstrom)
# Note: The Hamiltonian is H_R = alpha * (k x sigma). 
# Therefore alpha must have units of Energy * Length.
alpha = alpha_eV_A * e_charge * 1e-10  # Rashba parameter (J*m)
tau = 1.0e-12              # Relaxation time (s)

# Conversion factors for plotting
eV_to_J = 1.60217663e-19

# ==========================================
# 2. Theoretical Functions
# ==========================================

def susceptibility_hdr(m, alpha, tau, hbar, mu_B, e):
    """
    High-Density Regime (HDR) Edelstein Susceptibility.
    Both bands occupied (E_F > 0 relative to band crossing).
    Formula: chi_xy = (mu_B * e * tau * m * alpha) / (2 * pi * hbar^3)
    Units: A/V (Amperes per Volt, equivalent to Siemens for this 2D geometry context)
    """
    prefactor = (mu_B * e * tau * m * alpha) / (2 * np.pi * hbar**3)
    return prefactor

def susceptibility_ldr(E_F, m, alpha, tau, hbar, mu_B, e):
    """
    Low-Density Regime (LDR) Edelstein Susceptibility.
    Only inner band occupied (E_F < 0 relative to crossing).
    
    The susceptibility transitions from 0 (deep in the band) to the HDR value (at E_F=0).
    We use a physically motivated interpolation based on the Fermi wavevector k_F.
    For E_F < 0, the dispersion is E = (hbar^2 k^2 / 2m) - alpha k.
    At the band minimum (k = m alpha / hbar^2), E = -m alpha^2 / (2 hbar^2) = -E_R.
    
    The susceptibility scales with the density of states and the average spin polarization.
    Approximation used here for smooth transition:
    Chi(E_F) = Chi_HDR * sqrt( (E_F + E_R) / E_R ) for E_F in [-E_R, 0].
    This ensures Chi=0 at the bottom of the band (-E_R) and Chi=Chi_HDR at the crossing (0).
    """
    E_R = (m * alpha**2) / (2 * hbar**2) # Rashba energy splitting
    
    if E_F >= 0:
        # High Density Regime
        return susceptibility_hdr(m, alpha, tau, hbar, mu_B, e)
    else:
        # Low Density Regime
        # Ensure we don't take sqrt of negative numbers if E_F is below band bottom
        if E_F < -E_R:
            return 0.0
        else:
            chi_hdr = susceptibility_hdr(m, alpha, tau, hbar, mu_B, e)
            # Dimensionless factor that goes 0 -> 1
            factor = np.sqrt((E_F + E_R) / E_R)
            return chi_hdr * factor

def calculate_magnetization(E_field_vec, E_F, m, alpha, tau, hbar, mu_B, e):
    """
    Calculate magnetization vector M.
    M = Chi_xy * (z_hat x E)
    If E = (Ex, Ey), M = Chi * (Ey, -Ex)
    """
    Ex, Ey = E_field_vec[0], E_field_vec[1]
    
    chi = susceptibility_ldr(E_F, m, alpha, tau, hbar, mu_B, e)
    
    # M is perpendicular to E in the plane
    Mx = chi * Ey
    My = -chi * Ex
    
    return np.array([Mx, My])

def fermi_energy_from_density(n_2d, m, hbar):
    """
    Calculate Fermi energy for a 2D electron gas (parabolic approximation).
    E_F = (pi * hbar^2 * n_2d) / m
    """
    return (np.pi * hbar**2 * n_2d) / m

# ==========================================
# 3. Visualization Setup
# ==========================================

# Define ranges for plots
E_fields = np.linspace(0, 5000, 100)  # V/m
# Range for E_F: from -2*Rashba Energy to +2*Rashba Energy approx
E_R_val = (m_eff * alpha**2) / (2 * hbar**2)
E_Fs = np.linspace(-2 * E_R_val, 2 * E_R_val, 200) # J
alphas = np.linspace(0.1, 2.0, 50) * 1e-11 # J*m (range 10 to 200 meV*A)

# --- Graphic 1: Magnetization vs Electric Field ---
# Calculate M for a fixed E_F (HDR regime)
n_2d_hdr = 5e15 # m^-2
E_F_hdr = fermi_energy_from_density(n_2d_hdr, m_eff, hbar) 
chi_hdr = susceptibility_hdr(m_eff, alpha, tau, hbar, mu_B, e_charge)
M_vs_E = chi_hdr * E_fields

# --- Graphic 2: Susceptibility vs Chemical Potential ---
Chis_vs_EF = [susceptibility_ldr(ef, m_eff, alpha, tau, hbar, mu_B, e_charge) for ef in E_Fs]
E_Fs_meV = E_Fs / eV_to_J * 1000

# --- Graphic 3: Susceptibility vs Rashba Strength ---
Chis_vs_Alpha = [susceptibility_hdr(m_eff, a, tau, hbar, mu_B, e_charge) for a in alphas]
alphas_meVA = alphas / (e_charge * 1e-10)

# ==========================================
# 4. Plotting
# ==========================================

fig = plt.figure(figsize=(16, 10))
fig.suptitle('Edelstein Effect in Rashba Fermions', fontsize=20, fontweight='bold')

gs = GridSpec(2, 2, figure=fig)

# Plot 1: Magnetization vs Electric Field
ax1 = fig.add_subplot(gs[0, 0])
ax1.plot(E_fields, M_vs_E, 'b-', linewidth=2, label=f'$\\alpha={alpha_eV_A:.0f}$ meV$\\cdot$Å')
ax1.set_xlabel('Electric Field $E_x$ (V/m)', fontsize=12)
ax1.set_ylabel('Induced Magnetization $M_y$ (A/m)', fontsize=12)
ax1.set_title('Linear Response: $M \\propto E$', fontsize=14)
ax1.grid(True, linestyle='--', alpha=0.7)
ax1.legend()

# Plot 2: Susceptibility vs Chemical Potential
ax2 = fig.add_subplot(gs[0, 1])
ax2.plot(E_Fs_meV, Chis_vs_EF, 'r-', linewidth=2)
ax2.axvline(0, color='k', linestyle='--', alpha=0.5)
ax2.text(0.5, 0.9, 'High Density\nRegime', transform=ax2.transAxes, fontsize=10, color='green', ha='center')
ax2.text(0.5, 0.1, 'Low Density\nRegime', transform=ax2.transAxes, fontsize=10, color='orange', ha='center')
ax2.set_xlabel('Chemical Potential $E_F$ (meV)', fontsize=12)
ax2.set_ylabel('Edelstein Susceptibility $\\chi_{xy}$ (A/V)', fontsize=12)
ax2.set_title('Dependence on Carrier Density', fontsize=14)
ax2.grid(True, linestyle='--', alpha=0.7)

# Plot 3: Susceptibility vs Rashba Strength
ax3 = fig.add_subplot(gs[1, 0])
ax3.plot(alphas_meVA, Chis_vs_Alpha, 'g-', linewidth=2)
ax3.set_xlabel('Rashba Parameter $\\alpha$ (meV$\\cdot$Å)', fontsize=12)
ax3.set_ylabel('Edelstein Susceptibility $\\chi_{xy}$ (A/V)', fontsize=12)
ax3.set_title('Spin-Charge Conversion Efficiency', fontsize=14)
ax3.grid(True, linestyle='--', alpha=0.7)

# Plot 4: Vector Relationship (Polar/Quiver)
ax4 = fig.add_subplot(gs[1, 1], projection='polar')
angles = np.linspace(0, 2*np.pi, 8, endpoint=False)
# E field arrows (Blue)
for theta in angles:
    ax4.annotate('', xy=(theta, 1.0), xytext=(theta, 0),
                 arrowprops=dict(facecolor='blue', shrink=0.05, width=2))
    # M field arrows (Red, rotated by 90 deg = pi/2)
    ax4.annotate('', xy=(theta + np.pi/2, 0.8), xytext=(theta + np.pi/2, 0),
                 arrowprops=dict(facecolor='red', shrink=0.05, width=2))

ax4.set_rticks([]) # Hide radial ticks
ax4.set_xticks(angles)
ax4.set_xticklabels([r'$\vec{E}$' for _ in angles], fontsize=12, color='blue')
ax4.set_title(r'Spin-Momentum Locking: $\vec{M} \perp \vec{E}$', fontsize=14, pad=20)
# Add a legend manually
ax4.text(np.pi/2, 1.3, r'$\vec{M}$', color='red', fontsize=14, ha='center', fontweight='bold')
ax4.text(np.pi/2, 1.1, r'$\vec{E}$', color='blue', fontsize=14, ha='center', fontweight='bold')

plt.tight_layout(rect=[0, 0.03, 1, 0.95])
plt.show()

# ==========================================
# 5. Numerical Output Example
# ==========================================

print("-" * 60)
print("Edelstein Effect Calculation Output")
print("-" * 60)
print(f"Parameters:")
print(f"  Effective Mass (m): {m_eff/m_e:.3f} m_e")
print(f"  Rashba Parameter (alpha): {alpha_eV_A:.1f} meV·Å")
print(f"  Relaxation Time (tau): {tau*1e12:.1f} ps")
print(f"  Fermi Energy (HDR): {E_F_hdr/eV_to_J*1000:.1f} meV")
print("-" * 60)

# Test for a specific field
E_test = 1000.0 # V/m
M_test = calculate_magnetization([E_test, 0], E_F_hdr, m_eff, alpha, tau, hbar, mu_B, e_charge)
print(f"Input Electric Field: E = {E_test} V/m (x-direction)")
print(f"Calculated Magnetization: M = ({M_test[0]:.2e}, {M_test[1]:.2e}) A/m")
print(f"  Magnitude: {np.linalg.norm(M_test):.2e} A/m")
print(f"  Direction: Along +y (perpendicular to E)")
print("-" * 60)

# Spin Density Calculation
spin_density = np.linalg.norm(M_test) / mu_B
print(f"Induced Spin Density: {spin_density:.2e} spins/m^2")
print(f"Induced Spin Density: {spin_density*1e-4:.2e} spins/cm^2")
print("-" * 60)
```
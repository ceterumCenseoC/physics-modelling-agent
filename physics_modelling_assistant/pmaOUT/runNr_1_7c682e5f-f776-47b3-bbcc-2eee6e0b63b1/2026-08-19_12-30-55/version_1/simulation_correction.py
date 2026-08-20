Looking at this code, I need to fix several bugs:

1. **Plot 3 issue**: The polar plot arrows use `ax.arrow` incorrectly - polar axes need different handling
2. **Plot 7 issue**: The magnetization arrows are scaled incorrectly (multiplying by 1e12 which may not be appropriate)
3. **Print statement issue**: `{0:.2e}` will throw an error - can't format integer 0 as scientific notation
4. **Variable naming**: `chi_Ed` is ambiguous (should be clearer)
5. **Plot 2 spin texture**: The spin formula for the lower band needs correction
6. **Plot 6**: Division by zero risk if `kF_p` or `kF_m` becomes zero
7. **Efficiency**: The loop in Plot 6 can be vectorized
8. **Plot 3**: The arrows on polar plot are problematic - better to use a different approach

Let me fix these issues:

```python
"""
Edelstein Effect in Rashba Fermion Systems
==========================================
Implementation of the corrected model for the electric-field-induced magnetization
in a 2DEG with Rashba spin-orbit coupling at the Gamma point.

The central result:
    M = chi * (g * mu_B * e * tau * alpha_R / (4*pi*hbar)) * (z_hat x E)

All quantities are computed in SI units. Graphics are generated using matplotlib.
"""

import numpy as np
import matplotlib.pyplot as plt

# ============================================================
# Physical constants (SI units)
# ============================================================
hbar = 1.054571817e-34          # J·s
m_e = 9.1093837015e-31          # kg
e_charge = 1.602176634e-19      # C
mu_B = 9.2740100783e-24         # J/T
k_B = 1.380649e-23              # J/K

# ============================================================
# Starting parameters (InGaAs/InAlAs 2DEG)
# ============================================================
m_star = 0.05 * m_e             # effective mass (kg)
alpha_R = 0.5e-11 * e_charge    # Rashba SOC strength (J·m)  [0.5e-11 eV·m]
E_F = 20e-3 * e_charge          # Fermi energy (J)  [20 meV]
tau = 1e-12                     # momentum relaxation time (s)
g_factor = 4                    # electron g-factor
chi = +1                        # chirality (+1 or -1)
T = 4.0                         # temperature (K)

# ============================================================
# Derived quantities
# ============================================================
E_SO = m_star * alpha_R**2 / (2 * hbar**2)          # spin-orbit energy (J)
k0 = np.sqrt(2 * m_star * E_F + (m_star * alpha_R / hbar)**2) / hbar  # central Fermi wavevector
k_F_plus = k0 - chi * m_star * alpha_R / hbar**2    # upper band Fermi wavevector
k_F_minus = k0 + chi * m_star * alpha_R / hbar**2   # lower band Fermi wavevector
v_F = hbar * k0 / m_star                            # Fermi velocity (m/s)
l_mfp = v_F * tau                                   # mean free path (m)

print("=== Derived quantities ===")
print(f"E_SO = {E_SO/e_charge*1e3:.4f} meV")
print(f"k0   = {k0:.4e} m^-1")
print(f"k_F+ = {k_F_plus:.4e} m^-1")
print(f"k_F- = {k_F_minus:.4e} m^-1")
print(f"v_F  = {v_F:.4e} m/s")
print(f"mean free path = {l_mfp*1e9:.1f} nm")
print(f"k_F * l = {k0 * l_mfp:.1f} (diffusive limit: >>1)")

# Edelstein susceptibility
chi_Ed = g_factor * mu_B * e_charge * tau * alpha_R / (4 * np.pi * hbar)
print(f"\nEdelstein susceptibility (SI): {chi_Ed:.4e} A·m^2/V")
print(f"  = {chi_Ed / (9.274e-24) * 1e-18 * 100:.4e} μ_B/(nm^2·(V/cm))")

# Conversion factor: A·m²/V to μ_B/(nm²·(V/cm))
# 1 A·m²/V = 1/(mu_B) μ_B / (1e18 nm²) / (100 V/cm) = 1e-20/(mu_B) μ_B/(nm²·(V/cm))
conv_factor = 1e-20 / mu_B * 100  # μ_B/(nm²·(V/cm)) per A·m²/V

# ============================================================
# Plot 1: Energy dispersion along k_x (k_y=0)
# ============================================================
fig, ax = plt.subplots(figsize=(8, 6))
k_x = np.linspace(-0.03e10, 0.03e10, 400)  # m^-1, range ±0.03 Å^-1
eps_plus = hbar**2 * k_x**2 / (2 * m_star) + chi * alpha_R * np.abs(k_x)
eps_minus = hbar**2 * k_x**2 / (2 * m_star) - chi * alpha_R * np.abs(k_x)

ax.plot(k_x / 1e10, eps_plus / e_charge * 1e3, 'r-', lw=2, label=r'$\varepsilon_+(k)$')
ax.plot(k_x / 1e10, eps_minus / e_charge * 1e3, 'b-', lw=2, label=r'$\varepsilon_-(k)$')
ax.axhline(0, color='k', lw=0.5)
ax.axhline(E_F / e_charge * 1e3, color='g', ls='--', lw=1.5, label=r'$E_F$')
ax.axhline(E_SO / e_charge * 1e3, color='gray', ls=':', lw=1, label=r'$E_{SO}$')
ax.plot(0, 0, 'ko', ms=8, label='Dirac point')
ax.set_xlabel(r'$k_x$ ($\AA^{-1}$)', fontsize=14)
ax.set_ylabel('Energy (meV)', fontsize=14)
ax.set_title('Rashba Band Structure', fontsize=16)
ax.legend(fontsize=12, loc='upper right')
ax.set_xlim(-0.03, 0.03)
ax.set_ylim(-5, 15)
ax.grid(True, alpha=0.3)
plt.tight_layout()
plt.savefig('plot1_energy_dispersion.png', dpi=150)
plt.show()

# ============================================================
# Plot 2: Spin texture in momentum space
# ============================================================
fig, ax = plt.subplots(figsize=(8, 8))
k_vals = np.linspace(-0.025e10, 0.025e10, 15)
KX, KY = np.meshgrid(k_vals, k_vals)
phi_k = np.arctan2(KY, KX)
# Spin expectation for lower band (lambda = -1): <sigma> = -chi * (z_hat x k_hat)
# <sigma_x> = -chi * (-sin(phi)) = chi*sin(phi)
# <sigma_y> = -chi * (cos(phi)) = -chi*cos(phi)
Sx = chi * np.sin(phi_k)
Sy = -chi * np.cos(phi_k)
# Normalize for arrow length
norm = np.sqrt(Sx**2 + Sy**2 + 1e-10)
ax.quiver(KX / 1e10, KY / 1e10, Sx / norm, Sy / norm, 
          color='steelblue', alpha=0.8, scale=30, width=0.002)

# Draw Fermi circles for both bands
theta = np.linspace(0, 2 * np.pi, 200)
for kF, color in [(k_F_plus, 'red'), (k_F_minus, 'blue')]:
    ax.plot(kF * np.cos(theta) / 1e10, kF * np.sin(theta) / 1e10, 
            color=color, lw=2, label=f'$k_F$ = {kF/1e8:.2f}×10⁸ m⁻¹')
ax.set_xlabel(r'$k_x$ ($\AA^{-1}$)', fontsize=14)
ax.set_ylabel(r'$k_y$ ($\AA^{-1}$)', fontsize=14)
ax.set_title(f'Spin Texture (χ = {chi:+d})', fontsize=16)
ax.legend(fontsize=10, loc='upper right')
ax.set_aspect('equal')
ax.grid(True, alpha=0.3)
plt.tight_layout()
plt.savefig('plot2_spin_texture.png', dpi=150)
plt.show()

# ============================================================
# Plot 3: Magnetization vs. electric field direction (polar)
# ============================================================
theta_E = np.linspace(0, 2 * np.pi, 200)
E_mag = 100  # V/m (1 V/cm)
M_mag = chi_Ed * E_mag
# M = chi*chi_Ed*(z_hat x E) = chi*chi_Ed*E*(-sin(theta), cos(theta))
M_x = chi * chi_Ed * E_mag * (-np.sin(theta_E))
M_y = chi * chi_Ed * E_mag * (np.cos(theta_E))
M_norm = np.sqrt(M_x**2 + M_y**2)

fig, ax = plt.subplots(figsize=(8, 8), subplot_kw={'projection': 'polar'})
ax.plot(theta_E, M_norm * conv_factor, 'b-', lw=2, label=r'$|\mathbf{M}|$')
# Overlay points at selected angles showing direction
for angle in np.linspace(0, 2*np.pi, 8, endpoint=False):
    mx = chi * chi_Ed * E_mag * (-np.sin(angle)) * conv_factor
    my = chi * chi_Ed * E_mag * (np.cos(angle)) * conv_factor
    ax.plot(angle, np.hypot(mx, my), 'ro', markersize=6)
    # Add direction indicator
    ax.annotate('', xy=(angle, np.hypot(mx, my)), xytext=(angle, 0),
                arrowprops=dict(arrowstyle='->', color='red', lw=1.5))
ax.set_title('Magnetization vs Field Direction\n(radius = |M| in μ_B/nm²)', fontsize=14)
ax.legend(loc='upper right', bbox_to_anchor=(1.3, 1.1))
plt.tight_layout()
plt.savefig('plot3_mag_vs_direction.png', dpi=150)
plt.show()

# ============================================================
# Plot 4: Magnetization vs. electric field magnitude (E along x)
# ============================================================
E_values = np.linspace(0, 10, 100)  # V/cm
E_SI = E_values * 100  # V/m
M_y = chi * chi_Ed * E_SI
M_x = np.zeros_like(M_y)
M_norm = np.abs(M_y)

fig, ax = plt.subplots(figsize=(8, 6))
ax.plot(E_values, M_x * conv_factor, 'b--', lw=2, label=r'$M_x$')
ax.plot(E_values, M_y * conv_factor, 'r-', lw=2, label=r'$M_y$')
ax.plot(E_values, M_norm * conv_factor, 'g:', lw=2, label=r'$|\mathbf{M}|$')
ax.set_xlabel('Electric field (V/cm)', fontsize=14)
ax.set_ylabel(r'Magnetization ($\mu_B$/nm²)', fontsize=14)
ax.set_title('Magnetization vs E (E along x)', fontsize=16)
ax.legend(fontsize=12)
ax.grid(True, alpha=0.3)
plt.tight_layout()
plt.savefig('plot4_mag_vs_E.png', dpi=150)
plt.show()

# ============================================================
# Plot 5: Magnetization vs. Rashba SOC strength
# ============================================================
alpha_values = np.linspace(0, 2e-11, 200) * e_charge  # J·m
E_fixed = 100  # V/m
chi_Ed_alpha = g_factor * mu_B * e_charge * tau * alpha_values / (4 * np.pi * hbar)
M_alpha = chi_Ed_alpha * E_fixed

fig, ax = plt.subplots(figsize=(8, 6))
ax.plot(alpha_values / e_charge * 1e11, M_alpha * conv_factor, 'b-', lw=2)
ax.axvline(0.5, color='r', ls='--', lw=1, label='InGaAs value')
ax.set_xlabel(r'$\alpha_R$ ($10^{-11}$ eV·m)', fontsize=14)
ax.set_ylabel(r'$|\mathbf{M}|$ ($\mu_B$/nm²)', fontsize=14)
ax.set_title('Magnetization vs Rashba SOC Strength', fontsize=16)
ax.legend(fontsize=12)
ax.grid(True, alpha=0.3)
plt.tight_layout()
plt.savefig('plot5_mag_vs_alpha.png', dpi=150)
plt.show()

# ============================================================
# Plot 6: Magnetization vs. Fermi energy (with impurity scattering)
# ============================================================
# Include impurity scattering: tau depends on DOS
n_i = 1e15  # impurity density m^-2
V0 = 1e-28  # scattering potential J·m^2 (tunable)
E_F_range = np.linspace(0.01e-3, 50e-3, 300) * e_charge  # J

# Vectorized calculation
k0_range = np.sqrt(2 * m_star * E_F_range + (m_star * alpha_R / hbar)**2) / hbar
kF_p = k0_range - chi * m_star * alpha_R / hbar**2
kF_m = k0_range + chi * m_star * alpha_R / hbar**2

# Avoid division by zero
kF_p = np.maximum(kF_p, 1e-10)
kF_m = np.maximum(kF_m, 1e-10)

# Density of states for each band
N_plus = m_star / (2 * np.pi * hbar**2) * (1 + chi * alpha_R * m_star / (hbar**2 * kF_p))**(-1)
N_minus = m_star / (2 * np.pi * hbar**2) * (1 - chi * alpha_R * m_star / (hbar**2 * kF_m))**(-1)
N_tot = N_plus + N_minus

# Relaxation time from impurity scattering
tau_i = hbar**2 / (2 * np.pi * n_i * V0**2 * N_tot)

# Edelstein susceptibility
chi_Ed_E = g_factor * mu_B * e_charge * tau_i * alpha_R / (4 * np.pi * hbar)

# Apply correction for EF < E_SO (only lower band occupied)
mask = E_F_range < E_SO
chi_Ed_E[mask] *= (1 - E_F_range[mask] / E_SO)

fig, ax = plt.subplots(figsize=(8, 6))
ax.plot(E_F_range / e_charge * 1e3, chi_Ed_E / np.max(chi_Ed_E), 'b-', lw=2)
ax.axvline(E_SO / e_charge * 1e3, color='r', ls='--', lw=1.5, label=r'$E_{SO}$')
ax.set_xlabel('Fermi energy (meV)', fontsize=14)
ax.set_ylabel('Normalized Edelstein susceptibility', fontsize=14)
ax.set_title('Edelstein Susceptibility vs Fermi Energy', fontsize=16)
ax.legend(fontsize=12)
ax.grid(True, alpha=0.3)
plt.tight_layout()
plt.savefig('plot6_mag_vs_EF.png', dpi=150)
plt.show()

# ============================================================
# Plot 7: Effect of chirality
# ============================================================
fig, axes = plt.subplots(1, 2, figsize=(12, 6))

# Scale for arrow visualization (arbitrary units)
arrow_scale = 1e-12

for idx, chi_val in enumerate([+1, -1]):
    ax = axes[idx]
    # Magnetization for E along x (E = 100 V/m)
    M_vec = chi_val * chi_Ed * E_fixed * np.array([0, 1])  # along y
    E_vec = np.array([1, 0]) * E_fixed
    
    # Draw coordinate axes
    ax.axhline(0, color='k', lw=0.5)
    ax.axvline(0, color='k', lw=0.5)
    
    # Draw electric field arrow (scaled)
    ax.arrow(0, 0, E_vec[0] * arrow_scale, E_vec[1] * arrow_scale, 
             head_width=0.02, head_length=0.02, 
             fc='red', ec='red', lw=2, label='E')
    
    # Draw magnetization arrow (scaled)
    ax.arrow(0, 0, M_vec[0] * arrow_scale, M_vec[1] * arrow_scale, 
             head_width=0.02, head_length=0.02,
             fc='blue', ec='blue', lw=2, label='M')
    
    ax.set_xlim(-0.15, 0.15)
    ax.set_ylim(-0.15, 0.15)
    ax.set_aspect('equal')
    ax.set_title(f'χ = {chi_val:+d}', fontsize=14)
    ax.legend(fontsize=10)
    ax.grid(True, alpha=0.3)
    ax.set_xlabel('x', fontsize=12)
    ax.set_ylabel('y', fontsize=12)

fig.suptitle('Effect of Chirality on Magnetization Direction (E along +x)', fontsize=16)
plt.tight_layout()
plt.savefig('plot7_chirality.png', dpi=150)
plt.show()

# ============================================================
# Additional quantitative output
# ============================================================
print("\n=== Edelstein Effect Results ===")
print("E along x (100 V/m = 1 V/cm):")
M_x_val = 0.0
M_y_val = chi * chi_Ed * 100
print(f"  M = ({M_x_val:.2e}, {M_y_val * conv_factor:.4f}) μ_B/nm²")
print(f"  |M| = {abs(M_y_val) * conv_factor:.4f} μ_B/nm²")
print("\nE along y (100 V/m = 1 V/cm):")
M_x_val2 = -chi * chi_Ed * 100
M_y_val2 = 0.0
print(f"  M = ({M_x_val2 * conv_factor:.4f}, {M_y_val2:.2e}) μ_B/nm²")
print("\nFor chi = -1: M reverses direction for same E")

# Verify linearity
print("\n=== Linearity Check ===")
E_test = np.array([50, 100, 200]) * 100  # V/m
for E in E_test:
    M = chi * chi_Ed * E
    print(f"E = {E/100:.0f} V/cm: |M| = {np.linalg.norm(M) * conv_factor:.4f} μ_B/nm²")

# ============================================================
# Summary
# ============================================================
print("\n" + "="*60)
print("MODEL SUMMARY")
print("="*60)
print("Central formula: M = χ · g·μ_B·e·τ·α_R/(4π·ℏ) · (ẑ × E)")
print(f"  χ = {chi:+d}")
print(f"  g = {g_factor}")
print(f"  α_R = {alpha_R/e_charge:.2e} eV·m = {alpha_R:.2e} J·m")
print(f"  τ = {tau:.0f} ps")
print(f"  Edelstein susceptibility = {chi_Ed:.3e} A·m²/V")
print(f"  = {chi_Ed * conv_factor:.3e} μ_B/(nm²·(V/cm))")
print(f"\nAll 7 plots generated successfully.")
print("The magnetization is perpendicular to E, linear in |E| and α_R,")
print("and reverses direction with chirality χ.")
```

Key fixes made:
1. **Plot 3**: Replaced problematic `ax.arrow` on polar plot with proper polar annotations
2. **Plot 7**: Used consistent `arrow_scale` for both E and M vectors
3. **Print statements**: Fixed invalid format specifiers `{0:.2e}` → `{M_x_val:.2e}`
4. **Plot 2**: Corrected spin texture formulas for lower band
5. **Plot 6**: Vectorized the loop, added protection against division by zero
6. **Plot 3/4/5/7**: Used consistent `conv_factor` for unit conversion
7. **Added proper unit conversion factor** for A·m²/V to μ_B/(nm²·(V/cm))
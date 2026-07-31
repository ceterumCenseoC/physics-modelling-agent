```python
import numpy as np
import matplotlib.pyplot as plt

# ============================================================
# 1. PHYSICAL CONSTANTS AND MODEL PARAMETERS
# ============================================================
# SI Units
e = 1.602e-19           # Elementary charge (C)
mu_B = 9.274e-24        # Bohr magneton (J/T)
hbar = 1.054e-34        # Reduced Planck constant (J*s)
m_e = 9.109e-31         # Electron rest mass (kg)

# Material/System Parameters (based on realistic context for InGaAs 2DEG)
m_star = 0.05 * m_e     # Effective mass (kg)
alpha = 50e-3 * e * 1e-10  # Rashba parameter = 50 meV Angstrom (J*m)
tau = 1.0e-12           # Relaxation time (s)
E_F = 50e-3 * e         # Fermi energy = 50 meV (J)

# Magnetic permeability of free space (for potential conversion to H-fields)
mu_0 = 4 * np.pi * 1.0e-7 # T*m/A

# ============================================================
# 2. MATHEMATICAL MODEL IMPLEMENTATION
# ============================================================

def calculate_edelstein_magnetization(E_field_mag, alpha_val, m_val, EF_val, tau_val):
    """
    Calculates the magnitude of the Edelstein magnetization for a given 
    electric field and system parameters.
    
    The code strictly implements the dimensionally corrected formulas 
    derived in the theoretical model context.
    
    Formulas:
    1. Crossover Energy: E_0 = m * alpha^2 / 2 * hbar^2
    2. HDR (EF > E_0): M = (e * tau * mu_B * m * alpha) / (2 * pi * hbar^2) * |E|
    3. LDR (EF < E_0): M = (e * tau * mu_B) / (2 * pi * hbar^2) * sqrt(m^2 * alpha^2 + 2*m*EF*hbar^2) * |E|
    """
    
    # Calculate the Rashba energy crossing point
    # Note: E_0 in prompt text is m*alpha^2/2hbar^2, but dispersion min is at k = m*alpha/hbar^2
    # The energy at k_0 is -m*alpha^2/2hbar^2. The separation between bands is 2*alpha*k.
    # We follow the explicit HDR/LDR criteria derived in the text and dimensional analysis.
    
    # The text defines the HDR condition as EF >> m*alpha^2/2m (simplified) which implies 
    # the scale is set by m*alpha^2/hbar^2.
    
    # Using the dimensionally corrected formulas provided in the context:
    # Corresponds to the magnitude of the shift needed to populate the second band
    E_cross_scale = (m_val * alpha_val**2) / (2 * hbar**2)
    
    # Constants factor common to both regimes (dimensionally corrected)
    # Prefactor = (e * tau * mu_B) / (2 * pi * hbar^2)
    prefactor = (e * tau_val * mu_B) / (2 * np.pi * hbar**2)
    
    if EF_val > E_cross_scale:
        # High-Density Regime (HDR)
        M = prefactor * (m_val * alpha_val) * E_field_mag
        regime = "HDR"
    else:
        # Low-Density Regime (LDR)
        term_sqrt = np.sqrt((m_val**2 * alpha_val**2) + (2 * m_val * EF_val * hbar**2))
        M = prefactor * term_sqrt * E_field_mag
        regime = "LDR"
        
    return M, regime

def get_magnetization_direction_vec(E_field_vec):
    """
    Returns the magnetization vector M = lambda * (z x E).
    Direction is strictly perpendicular to E in the plane.
    """
    Ex, Ey = E_field_vec
    # Cross product z_hat x E_vec
    # z_hat = (0,0,1), E = (Ex, Ey, 0) -> Result = (-Ey, Ex, 0)
    Mx = -Ey
    My = Ex
    # Normalize direction
    norm = np.sqrt(Mx**2 + My**2)
    if norm == 0:
        return np.array([0.0, 0.0])
    return np.array([Mx/norm, My/norm])

# ============================================================
# 3. VISUALIZATION AND ANALYSIS
# ============================================================

# --- Setup Data Ranges ---
# 1. Magnetization vs Electric Field
E_range = np.linspace(0, 2e5, 100)  # 0 to 20,000 V/m
M_vs_E = []
for E_val in E_range:
    M_mag, _ = calculate_edelstein_magnetization(E_val, alpha, m_star, E_F, tau)
    M_vs_E.append(M_mag)

# 2. Magnetization vs Rashba Parameter (Alpha)
alpha_range = np.linspace(10, 200, 100) * e * 1e-10  # 10 to 200 meV Angstrom
M_vs_alpha = []
for alpha_val in alpha_range:
    M_mag, _ = calculate_edelstein_magnetization(1e4, alpha_val, m_star, E_F, tau)
    M_vs_alpha.append(M_mag)

# 3. Magnetization vs Fermi Energy (showing transition LDR -> HDR)
# Up to 60 meV
EF_range = np.linspace(-5e-3 * e, 60e-3 * e, 200) 
M_vs_EF regimes = []
for ef_val in EF_range:
    # Ensure EF is physical for simple calculation, though model handles positive/negative logic implicitly
    calc_ef = max(0, ef_val) # The model assumes occupancy, restrict to >= 0 for this visual
    M_mag, reg = calculate_edelstein_magnetization(1e4, alpha, m_star, calc_ef, tau)
    M_vs_EF.append(M_mag)
    regimes.append(reg)

# 4. Spin Texture Visualization
# Grid for k-space
k_lim = 2.0  # Normalized units
kx = np.linspace(-k_lim, k_lim, 15)
ky = np.linspace(-k_lim, k_lim, 15)
KX, KY = np.meshgrid(kx, ky)
# Avoid division by zero at origin
K_norm = np.sqrt(KX**2 + KY**2)
K_norm[K_norm == 0] = 1e-9

# Spin expectation values for outer band (nu = -) -> <sig> = (-ky, kx, 0)/k
# (as per section 2 of the model)
SX = -KY / K_norm
SY = KX / K_norm

# ============================================================
# 4. PLOTTING
# ============================================================

fig = plt.figure(figsize=(15, 10))
plt.style.use('seaborn-v0_8-darkgrid')

# --- Subplot 1: Magnetization vs Electric Field (HDR) ---
ax1 = fig.add_subplot(2, 2, 1)
ax1.plot(E_range / 1e4, np.array(M_vs_E) / 1e-30, color='royalblue', linewidth=2.5)
ax1.set_xlabel('Electric Field Magnitude $|\vec{E}|$ ($10^4$ V/m)', fontsize=12)
ax1.set_ylabel('Magnetization Magnitude $M$ ($10^{-30}$ J/T)', fontsize=12)
ax1.set_title(f'(a) Edelstein Response vs Electric Field\n(HDR, $E_F$ = {E_F/e*1000:.1f} meV)', fontsize=14)
ax1.tick_params(axis='both', which='major', labelsize=10)

# --- Subplot 2: Magnetization vs Rashba Parameter ---
ax2 = fig.add_subplot(2, 2, 2)
# Convert alpha back to meV Angstrom for x-axis display
alpha_display = alpha_range / (e * 1e-10)
ax2.plot(alpha_display, np.array(M_vs_alpha) / 1e-30, color='crimson', linewidth=2.5)
ax2.set_xlabel('Rashba Parameter $\\alpha$ (meV·Å)', fontsize=12)
ax2.set_ylabel('Magnetization Magnitude $M$ ($10^{-30}$ J/T)', fontsize=12)
ax2.set_title(f'(b) Dependence on Spin-Orbit Strength\n($|\vec{E}| = 10^4$ V/m)', fontsize=14)
ax2.tick_params(axis='both', which='major', labelsize=10)

# --- Subplot 3: Magnetization vs Fermi Energy (Transition) ---
ax3 = fig.add_subplot(2, 2, 3)
EF_display = EF_range / e * 1000 # meV
# Filter for plotting positive energy mainly for visual clarity of transition
plot_indices = EF_display >= 0
ax3.plot(EF_display[plot_indices], np.array(M_vs_EF)[plot_indices] / 1e-30, color='forestgreen', linewidth=2.5)

# Highlight the transition point (approximate)
E_cross_val = (m_star * alpha**2) / (2 * hbar**2) / e * 1000
ax3.axvline(x=E_cross_val, color='black', linestyle='--', alpha=0.7, label=f'Transition $\sim$ {E_cross_val:.1f} meV')
ax3.text(E_cross_val + 1, ax3.get_ylim()[1]*0.8, 'HDR', color='black', fontsize=11, fontweight='bold')
ax3.text(E_cross_val - 8, ax3.get_ylim()[1]*0.8, 'LDR', color='black', fontsize=11, fontweight='bold')

ax3.set_xlabel('Fermi Energy $E_F$ (meV)', fontsize=12)
ax3.set_ylabel('Magnetization Magnitude $M$ ($10^{-30}$ J/T)', fontsize=12)
ax3.set_title(f'(c) Crossover from Low to High Density\nRegime ($|\vec{E}| = 10^4$ V/m)', fontsize=14)
ax3.legend()
ax3.tick_params(axis='both', which='major', labelsize=10)

# --- Subplot 4: Spin Texture at Gamma (Visualization) ---
ax4 = fig.add_subplot(2, 2, 4)
# Quiver plot
# Color vectors by magnitude (which is 1 everywhere except origin) or by angle
Q = ax4.quiver(KX, KY, SX, SY, pivot='mid', color='purple', scale=20, width=0.005)
# Draw circle to represent Fermi surface (arbitrary radius for visual)
theta_circle = np.linspace(0, 2*np.pi, 100)
ax4.plot(np.cos(theta_circle), np.sin(theta_circle), 'k--', alpha=0.3, label='Constant Energy Contour')
ax4.set_xlabel('$k_x$ (normalized)', fontsize=12)
ax4.set_ylabel('$k_y$ (normalized)', fontsize=12)
ax4.set_title(f'(d) Spin-Momentum Locking\n(Tangential to Fermi Surface)', fontsize=14)
ax4.set_aspect('equal')
ax4.legend(loc='upper right')

# Annotate direction of M for a specific E-field
# Example: E pointing along +x -> M points along +y
arrow_E = dict(facecolor='blue', edgecolor='blue', width=0.1)
arrow_M = dict(facecolor='red', edgecolor='red', width=0.1)
ax4.annotate('$\\vec{E}$', xy=(-1.2, -1.2), xytext=(-1.8, -1.2),
             arrowprops=dict(arrowstyle="->", color='blue', lw=2))
ax4.annotate('$\\vec{M}$', xy=(-1.2, -1.2), xytext=(-1.2, -0.5),
             arrowprops=dict(arrowstyle="->", color='red', lw=2))
ax4.text(-1.8, -1.3, "Applied E", color='blue', fontsize=10)
ax4.text(-1.25, -0.4, "Induced M", color='red', fontsize=10)

plt.tight_layout()
plt.show()

# ============================================================
# 5. NUMERICAL OUTPUT VERIFICATION
# ============================================================
print("--- Model Verification ---")
print(f"System Parameters:")
print(f"  Effective Mass (m): {m_star:.2e} kg")
print(f"  Rashba Param (alpha): {alpha:.2e} J m  ({alpha/(e*1e-10):.1f} meV Angstrom)")
print(f"  Fermi Energy (E_F): {E_F:.2e} J  ({E_F/e*1000:.1f} meV)")
print(f"  Relaxation Time (tau): {tau:.2e} s")

# Calculate crossover energy precisely as defined in code logic
E_cross_calc = (m_star * alpha**2) / (2 * hbar**2)
print(f"\nCalculated Crossover Energy (LDR -> HDR): {E_cross_calc:.2e} J ({E_cross_calc/e*1000:.2f} meV)")

# Test a specific E-field value
E_test = 1.0e4 # V/m
M_test, regime_test = calculate_edelstein_magnetization(E_test, alpha, m_star, E_F, tau)
print(f"\nCalculation for |E| = {E_test:.1e} V/m:")
print(f"  Regime: {regime_test}")
print(f"  Magnetization Magnitude: {M_test:.4e} J/T")
print(f"  Magnetization Magnitude: {M_test/mu_B:.4e} Bohr magnetons")

# Calculate direction for a vector E
E_vec = np.array([1e4, 0]) # E along x
M_dir = get_magnetization_direction_vec(E_vec)
print(f"  Input E direction: ({E_vec[0]:.1e}, {E_vec[1]:.1e}) [V/m]")
print(f"  Output M direction: ({M_dir[0]:.2f}, {M_dir[1]:.2f}) (Normalized)")
print(f"  Relation: M is perpendicular to E (Cross Product z x E)")
```
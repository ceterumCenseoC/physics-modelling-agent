```python
import numpy as np
import matplotlib.pyplot as plt

# ============================================================
# 1. PHYSICAL CONSTANTS AND MODEL PARAMETERS
# ============================================================
# Fundamental Constants in SI Units
e = 1.602176634e-19      # Elementary charge (C)
mu_B = 9.2740100783e-24  # Bohr magneton (J/T)
hbar = 1.054571817e-34   # Reduced Planck constant (J*s)
m_e = 9.1093837015e-31   # Electron rest mass (kg)

# Material/System Parameters (based on realistic context for InGaAs 2DEG)
m_star = 0.05 * m_e      # Effective mass (kg)
alpha = 50e-3 * e * 1e-10  # Rashba parameter = 50 meV Angstrom (J*m)
tau = 1.0e-12            # Relaxation time (s)
E_F_input = 50e-3 * e    # Fermi energy = 50 meV (J)

# Constants for Model
# The HDR/LDR distinction depends on the energy scale E_cross.
# E_cross represents the energy scale of the band touching/separation relative to the parabolic term.
E_cross = (m_star * alpha**2) / (2 * hbar**2)

# ============================================================
# 2. MATHEMATICAL MODEL IMPLEMENTATION
# ============================================================

def calculate_edelstein_magnetization(E_field_mag, alpha_val, m_val, EF_val, tau_val, hbar_val):
    """
    Calculates the magnitude of the Edelstein magnetization based on the 
    dimensionally corrected analytical formulas.
    
    Parameters:
    -----------
    E_field_mag : float
        Magnitude of the electric field (V/m).
    alpha_val : float
        Rashba spin-orbit coupling strength (J*m).
    m_val : float
        Effective carrier mass (kg).
    EF_val : float
        Fermi energy (J).
    tau_val : float
        Transport relaxation time (s).
    hbar_val : float
        Reduced Planck constant (J*s).
        
    Returns:
    --------
    M : float
        Magnetization magnitude (J/T).
    regime : str
        'HDR' (High-Density Regime) or 'LDR' (Low-Density Regime).
    """
    
    # Common dimensionally consistent prefactor
    # Corresponds to (e * tau * mu_B) / (2 * pi * hbar^2) * E_field
    # We calculate the base factor and multiply by E_field later
    constants = (e * tau_val * mu_B) / (2 * np.pi * hbar_val**2)
    
    # Theoretical crossover energy
    # This scale determines which occupied band physics dominates the response
    energy_scale = (m_val * alpha_val**2) / (2 * hbar_val**2)
    
    if EF_val > energy_scale:
        # High-Density Regime (HDR)
        # M = [e * tau * mu_B / (2 * pi * hbar^2)] * (m * alpha) * E
        M = constants * (m_val * alpha_val) * E_field_mag
        regime = "HDR"
    else:
        # Low-Density Regime (LDR)
        # M = [e * tau * mu_B / (2 * pi * hbar^2)] * sqrt(m^2 * alpha^2 + 2 * m * EF * hbar^2) * E
        sqrt_term = np.sqrt((m_val**2 * alpha_val**2) + (2 * m_val * EF_val * hbar_val**2))
        M = constants * sqrt_term * E_field_mag
        regime = "LDR"
        
    return M, regime

# ============================================================
# 3. DATA GENERATION FOR PLOTTING
# ============================================================

# 1. Magnetization vs Electric Field (HDR)
# Linear regime check: fixed E_F (50 meV) > E_cross (~8 meV) ensures HDR
E_vals = np.linspace(0, 2e5, 100)  # 0 to 20,000 V/m
M_vs_E = []
for E_val in E_vals:
    M_calc, _ = calculate_edelstein_magnetization(E_val, alpha, m_star, E_F_input, tau, hbar)
    M_vs_E.append(M_calc)
M_vs_E = np.array(M_vs_E)

# 2. Magnetization vs Rashba Parameter (Alpha)
# Linear dependence expected in HDR
alpha_vals = np.linspace(10, 200, 100) * e * 1e-10  # 10 to 200 meV Angstrom
M_vs_alpha = []
for a_val in alpha_vals:
    # Use a fixed E_F sufficiently high to maintain HDR for most alpha values
    # Conservative E_F = 100 meV for this scan
    M_calc, _ = calculate_edelstein_magnetization(1e4, a_val, m_star, 100e-3*e, tau, hbar)
    M_vs_alpha.append(M_calc)
M_vs_alpha = np.array(M_vs_alpha)

# 3. Magnetization vs Fermi Energy (LDR -> HDR Transition)
# Scanning from below E_cross to above E_cross
EF_vals = np.linspace(-10e-3*e, 100e-3*e, 300) # -10 meV to 100 meV
M_vs_EF = []
regimes_list = []
for ef_val in EF_vals:
    # We clamp EF to 0 for the simple occupancy model logic (no unoccupied states below 0 in this simple picture)
    # though the formula handles the math.
    calc_ef = ef_val
    M_calc, reg = calculate_edelstein_magnetization(1e4, alpha, m_star, calc_ef, tau, hbar)
    M_vs_EF.append(M_calc)
    regimes_list.append(reg)
M_vs_EF = np.array(M_vs_EF)

# 4. Spin Texture Visualization
k_grid = 2.0
kx = np.linspace(-k_grid, k_grid, 20)
ky = np.linspace(-k_grid, k_grid, 20)
KX, KY = np.meshgrid(kx, ky)
K_mag = np.sqrt(KX**2 + KY**2)
# Avoid division by zero
K_mag[K_mag == 0] = 1e-12

# Spin expectation <sigma>_k^- for outer branch (curling counter-clockwise)
# Formula: (-ky, kx) / k
SX = -KY / K_mag
SY = KX / K_mag

# ============================================================
# 4. PLOTTING AND VISUALIZATION
# ============================================================

fig = plt.figure(figsize=(14, 10))
plt.suptitle(f"Edelstein Effect in Rashba Fermions\n($m^* = 0.05m_e, \\alpha_{{ref}} = 50$ meV$\\cdot$Å)", fontsize=16)

# --- Plot 1: Magnetization vs Electric Field ---
ax1 = fig.add_subplot(2, 2, 1)
ax1.plot(E_vals/1e4, M_vs_E/1e-30, color='tab:blue', linewidth=2.5, label='HDR Model')
ax1.set_xlabel('Electric Field $|\vec{E}|$ ($10^4$ V/m)', fontsize=12)
ax1.set_ylabel('Magnetization $M$ ($10^{-30}$ J/T)', fontsize=12)
ax1.set_title('(a) Magnetization vs Electric Field', fontsize=13)
ax1.grid(True, linestyle='--', alpha=0.7)
ax1.legend()

# --- Plot 2: Magnetization vs Rashba Parameter ---
ax2 = fig.add_subplot(2, 2, 2)
# Convert alpha for plotting labels
alpha_plot = alpha_vals / (e * 1e-10) # in meV Angstrom
ax2.plot(alpha_plot, M_vs_alpha/1e-30, color='tab:orange', linewidth=2.5)
ax2.set_xlabel('Rashba Parameter $\\alpha$ (meV$\\cdot$Å)', fontsize=12)
ax2.set_ylabel('Magnetization $M$ ($10^{-30}$ J/T)', fontsize=12)
ax2.set_title('(b) Magnetization vs Spin-Orbit Strength', fontsize=13)
ax2.grid(True, linestyle='--', alpha=0.7)

# --- Plot 3: Magnetization vs Fermi Energy (Regime Crossover) ---
ax3 = fig.add_subplot(2, 2, 3)
EF_plot = EF_vals / (e * 1000) # in meV
ax3.plot(EF_plot, M_vs_EF/1e-30, color='tab:green', linewidth=2.5, label='Edelstein Response')

# Calculate crossover point for visualization
# Crossover math: E_cross should be ~8 meV based on parameters
E_cross_mev = E_cross / (e * 1000)
ax3.axvline(x=E_cross_mev, color='black', linestyle=':', alpha=0.8, label=f'Crossover $\\approx$ {E_cross_mev:.1f} meV')

# Annotate regimes
ax3.text(E_cross_mev + 5, max(M_vs_EF/1e-30)*0.9, 'HDR', fontsize=12, fontweight='bold', color='black')
ax3.text(E_cross_mev - 15, max(M_vs_EF/1e-30)*0.9, 'LDR', fontsize=12, fontweight='bold', color='black')

ax3.set_xlabel('Fermi Energy $E_F$ (meV)', fontsize=12)
ax3.set_ylabel('Magnetization $M$ ($10^{-30}$ J/T)', fontsize=12)
ax3.set_title('(c) Dependence on Fermi Energy (LDR $\\to$ HDR)', fontsize=13)
ax3.set_xlim(0, 100)
ax3.grid(True, linestyle='--', alpha=0.7)
ax3.legend()

# --- Plot 4: Spin Texture (Quiver Plot) ---
ax4 = fig.add_subplot(2, 2, 4)
q = ax4.quiver(KX, KY, SX, SY, K_mag, cmap='viridis', pivot='mid', scale=25, width=0.015)

# Add a circle to suggest a Fermi surface
circle_theta = np.linspace(0, 2*np.pi, 100)
ax4.plot(np.cos(circle_theta), np.sin(circle_theta), 'k--', alpha=0.5, label='Fermi Contour')

# Add vector indications
ax4.annotate('$\\vec{E}$', xy=(0, 0), xytext=(-1.5, -1.5),
             arrowprops=dict(arrowstyle="->", color='blue', lw=2), fontsize=14, color='blue')
ax4.annotate('$\\vec{M}$', xy=(0,0), xytext=(-1.5, -1.5),
             arrowprops=dict(arrowstyle="->", color='red', lw=2), fontsize=14, color='red')

# Text offset for arrows
ax4.text(-1.7, -1.4, "Field Direction", color='blue', fontsize=10)
ax4.text(-1.4, -0.2, "Induced M", color='red', fontsize=10)

ax4.set_xlabel('$k_x$ (normalized)', fontsize=12)
ax4.set_ylabel('$k_y$ (normalized)', fontsize=12)
ax4.set_title('(d) Spin Texture ($\\nu=-$)', fontsize=13)
ax4.set_aspect('equal')
ax4.legend(loc='upper right', fontsize=9)

plt.tight_layout(rect=[0, 0.03, 1, 0.95]) # Adjust layout to make room for suptitle
plt.show()

# ============================================================
# 5. CONSOLE OUTPUT FOR VERIFICATION
# ============================================================
print("--------------------------------------------------")
print("  EDELSTEIN EFFECT MODEL - PARAMETER CHECK")
print("--------------------------------------------------")
print(f"Effective Mass (m)      : {m_star:.3e} kg")
print(f"Rashba Parameter (alpha): {alpha:.3e} Jm ({alpha/(e*1e-10):.1f} meV Angstrom)")
print(f"Relaxation Time (tau)   : {tau:.3e} s")
print(f"Fermi Energy (E_F)      : {E_F_input:.3e} J ({E_F_input/e*1000:.1f} meV)")
print("")
print(f"Crossover Energy Scale  : {E_cross:.3e} J ({E_cross/e*1000:.1f} meV)")
print(f"System Regime at E_F    : {'HDR (High Density)' if E_F_input > E_cross else 'LDR (Low Density)'}")
print("--------------------------------------------------")
print("  SAMPLE CALCULATION (|E| = 10^4 V/m)")
print("--------------------------------------------------")
E_test = 1e4
M_val, M_reg = calculate_edelstein_magnetization(E_test, alpha, m_star, E_F_input, tau, hbar)
print(f"Magnetization Magnitude : {M_val:.3e} J/T")
print(f"Magnetization Magnitude : {M_val/mu_B:.3e} mu_B")
print("--------------------------------------------------")
```
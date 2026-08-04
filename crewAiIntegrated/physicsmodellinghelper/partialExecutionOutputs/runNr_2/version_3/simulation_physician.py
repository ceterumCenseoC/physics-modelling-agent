
```python
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as patches
from mpl_toolkits.mplot3d import Axes3D
from matplotlib.quiver import Quiver3D

# ==========================================
# 1. Physical Constants & Units
# ==========================================
# Using SI units throughout
hbar = 1.0545718e-34   # Reduced Planck constant [J s]
e = 1.60217663e-19     # Elementary charge [C]
mu_B = 9.27401007e-24  # Bohr magneton [J/T]
m_e = 9.10938356e-31   # Free electron mass [kg]

# Unit conversion helpers
eV_to_J = e
Angstrom_to_m = 1e-10
fs_to_s = 1e-15

# ==========================================
# 2. Model Implementation (Corrected Formulas)
# ==========================================

def calculate_edelstein_magnetization(E_vec, alpha_R, m_eff, tau, E_F, hbar=hbar, e=e, mu_B=mu_B):
    """
    Calculates the magnetization vector M for a Rashba system.
    Assumes the corrected dimensionally consistent formulas derived in the context.
    
    Parameters:
    -----------
    E_vec : array_like
        Applied electric field vector [Ex, Ey, Ez] in V/m.
    alpha_R : float
        Rashba spin-orbit coupling strength in J*m.
    m_eff : float
        Effective carrier mass in kg.
    tau : float
        Transport relaxation time in s.
    E_F : float
        Fermi energy (chemical potential) in J.
        
    Returns:
    --------
    M_vec : numpy.ndarray
        Magnetization vector [Mx, My, Mz] in A/m.
    prefactor : float
        The scalar coefficient M / |E|.
    regime : str
        'HDR' (High Density) or 'LDR' (Low Density).
    """
    # Calculate the energy threshold for the HDR
    # Condition: E_F > alpha_R^2 * m / (2 * hbar^2)
    threshold_E = (alpha_R**2 * m_eff) / (2 * hbar**2)
    
    # Direction of M is strictly perpendicular to E in the plane (z cross E)
    # We assume 2D plane is xy, normal is z.
    # cross([0,0,1], [Ex, Ey, 0]) = [-Ey, Ex, 0]
    M_dir = np.cross(np.array([0, 0, 1]), E_vec)
    norm_E = np.linalg.norm(E_vec)
    
    if norm_E == 0:
        return np.zeros(3), 0.0, "Undefined"
        
    M_dir_normalized = M_dir / norm_E
    
    # Determine Regime and Prefactor
    # Using the CORRECTED formulas from the unit_checking_task
    
    if E_F > threshold_E:
        regime = "HDR"
        # Corrected HDR Formula: M = (e * mu_B * alpha * tau) / (2 * pi * hbar^2) * |E|
        # Note: original had mass 'm' in numerator, corrected version removed it for consistency.
        prefactor = (e * mu_B * alpha_R * tau) / (2 * np.pi * hbar**2)
    else:
        regime = "LDR"
        # Corrected LDR Formula: M = (e * mu_B * tau) / (2 * pi * hbar^2) * sqrt(alpha_R^2 + (2*hbar^2*E_F)/m_eff) * |E|
        sqrt_term = np.sqrt(alpha_R**2 + (2 * hbar**2 * E_F) / m_eff)
        prefactor = (e * mu_B * tau * sqrt_term) / (2 * np.pi * hbar**2)

    M_vec = prefactor * norm_E * M_dir_normalized
    
    return M_vec, prefactor, regime

# ==========================================
# 3. Simulation Configuration (Au(111)-like)
# ==========================================

# Baseline Parameters
params = {
    'm_eff': 0.25 * m_e,           # Effective mass in kg
    'alpha_R_evA': 0.33,           # Rashba strength in eV*Angstrom (common literature unit)
    'tau_fs': 30.0,                # Relaxation time in fs
    'E_F_eV': 0.1,                 # Fermi energy in eV
    'E_mag': 1e4,                  # Electric field magnitude in V/m
}

# Convert to SI
params['alpha_R'] = params['alpha_R_evA'] * eV_to_J * Angstrom_to_m
params['tau'] = params['tau_fs'] * fs_to_s
params['E_F'] = params['E_F_eV'] * eV_to_J

print(f"--- Model Configuration (Au(111) Baseline) ---")
print(f"Effective Mass: {params['m_eff']/m_e:.2f} m_e")
print(f"Rashba Constant: {params['alpha_R_evA']} eV·Å")
print(f"Relaxation Time: {params['tau_fs']} fs")
print(f"Fermi Energy: {params['E_F_eV']} eV")
print(f"Applied Field: {params['E_mag']} V/m")

# ==========================================
# 4. Calculations and Graphics
# ==========================================

# --- 4.1 Field Direction Dependence (Vector Diagram) ---
fig = plt.figure(figsize=(15, 10))

# Subplot 1: Vector Diagram
ax1 = fig.add_subplot(2, 3, 1)
ax1.set_title("Edelstein Geometry\n(Right-Hand Rule)", fontsize=12)
ax1.set_xlim(-1.5, 1.5)
ax1.set_ylim(-1.5, 1.5)
ax1.set_aspect('equal')
ax1.grid(True, linestyle='--', alpha=0.6)

# Draw Fermi Surfaces (Schematic k-space)
# Inner band (+) and Outer band (-)
theta = np.linspace(0, 2*np.pi, 100)
# Arbitrary radius for visualization
k_inner = 0.5 
k_outer = 0.9
ax1.plot(k_inner*np.cos(theta), k_inner*np.sin(theta), 'b-', alpha=0.5, label='Inner Band (+)')
ax1.plot(k_outer*np.cos(theta), k_outer*np.sin(theta), 'r-', alpha=0.5, label='Outer Band (-)')

# Draw Spin Textures (Arrows on circles)
for th in np.linspace(0, 2*np.pi, 8, endpoint=False):
    # Inner band spin direction: tangential, counter-clockwise texture
    # <sigma> = (sin(th), -cos(th))
    u_in, v_in = np.sin(th), -np.cos(th)
    ax1.arrow(k_inner*np.cos(th), k_inner*np.sin(th), u_in*0.2, v_in*0.2, 
              head_width=0.05, head_length=0.1, fc='blue', ec='blue')
    
    # Outer band spin direction: tangential, clockwise texture
    # <sigma> = (-sin(th), cos(th))
    u_out, v_out = -np.sin(th), np.cos(th)
    ax1.arrow(k_outer*np.cos(th), k_outer*np.sin(th), u_out*0.2, v_out*0.2, 
              head_width=0.05, head_length=0.1, fc='red', ec='red')

# Physical Vectors (Real space)
# E along x
ex, ey = 1.2, 0
# M along y
mx, my = 0, 1.2

ax1.arrow(0, 0, ex, ey, head_width=0.1, head_length=0.15, fc='k', ec='k', linewidth=2, label='E Field')
ax1.arrow(0, 0, mx, my, head_width=0.1, head_length=0.15, fc='g', ec='g', linewidth=2, label='M Induced')

ax1.text(ex/2, ey+0.1, r'$\vec{E}$', ha='center', fontsize=14, fontweight='bold')
ax1.text(mx+0.1, my/2, r'$\vec{M}$', va='center', fontsize=14, fontweight='bold')
ax1.set_xlabel(r'$k_x$ ($\parallel$)')
ax1.set_ylabel(r'$k_y$ ($\perp$)')
ax1.legend(loc='upper left', fontsize=8)


# --- 4.2 Susceptibility vs. Chemical Potential ---
# Compute M_y for E_x. Susceptibility chi = M_y / E_x.
# Loop over E_F
ax2 = fig.add_subplot(2, 3, 2)
E_Fs_eV = np.linspace(0, 0.5, 200)
susceptibility = []

E_test_vec = np.array([params['E_mag'], 0, 0])

for Ef_eV in E_Fs_eV:
    Ef_J = Ef_eV * eV_to_J
    M_vec, pref, reg = calculate_edelstein_magnetization(
        E_test_vec, params['alpha_R'], params['m_eff'], params['tau'], Ef_J
    )
    # M_vec is along y for E along x. Susceptibility is M_y / E_x
    # pref is technically M/E because direction is handled by vector math.
    # Here we use the magnitude prefactor returned by helper for clarity.
    susceptibility.append(pref)

susceptibility = np.array(susceptibility)

# Plot
ax2.plot(E_Fs_eV, susceptibility, 'b-', linewidth=2)
# Mark regime transition
threshold_J = (params['alpha_R']**2 * params['m_eff']) / (2 * hbar**2)
threshold_eV = threshold_J / eV_to_J
ax2.axvline(x=threshold_eV, color='k', linestyle='--', label='Regime Transition')
ax2.text(threshold_eV, 0.5 * np.max(susceptibility), 'HDR', rotation=90, verticalalignment='center')
ax2.text(threshold_eV * 0.5, 0.5 * np.max(susceptibility), 'LDR', rotation=90, verticalalignment='center')

ax2.set_xlabel(r'Chemical Potential $\mu$ (eV)')
ax2.set_ylabel(r'Magnitude of Coefficient $M/E$ (A s / m^2)')
ax2.set_title(r'Edelstein Response vs. $\mu$')
ax2.grid(True, alpha=0.5)


# --- 4.3 Susceptibility vs. Rashba Parameter ---
# Fix E_F in HDR (e.g., 0.2 eV)
ax3 = fig.add_subplot(2, 3, 3)
alphas_evA = np.linspace(0.1, 2.0, 100) # Vary from weak to strong SOC (Bi/Ag range)
susceptibility_alpha = []

fixed_EF_J = 0.2 * eV_to_J # Ensure HDR for most alphas, let function decide though

for alpha_evA in alphas_evA:
    alpha_Jm = alpha_evA * eV_to_J * Angstrom_to_m
    M_vec, pref, reg = calculate_edelstein_magnetization(
        E_test_vec, alpha_Jm, params['m_eff'], params['tau'], fixed_EF_J
    )
    susceptibility_alpha.append(pref)

ax3.plot(alphas_evA, susceptibility_alpha, 'r-', linewidth=2)
ax3.set_xlabel(r'Rashba Strength $\alpha_R$ (eV·Å)')
ax3.set_ylabel(r'Magnitude of Coefficient $M/E$ (A s / m^2)')
ax3.set_title(r'Edelstein Response vs. $\alpha_R$ (HDR approx)')
ax3.grid(True, alpha=0.5)


# --- 4.4 Anisotropy Boost (Schematic) ---
# The model describes anisotropic boost via ratios.
# Chi_xy ~ 1 / (1 + sqrt(r_m)) for mass anisotropy.
# We plot the analytical scaling factor given in the text relative to isotropic case.
ax4 = fig.add_subplot(2, 3, 4)
r_vals = np.linspace(1, 10, 100)
boost_factor_m = 1.0 / (1 + np.sqrt(r_vals)) # Approximation scaling from text
boost_factor_alpha = 1.0 / (1 + r_vals)      # Approximation scaling from text

ax4.plot(r_vals, boost_factor_m, label=r'Mass Anisotropy ($r_m$)')
ax4.plot(r_vals, boost_factor_alpha, label=r'SOC Anisotropy ($r_\alpha$)', linestyle='--')
ax4.set_xlabel(r'Anisotropy Ratio ($r$)')
ax4.set_ylabel(r'Susceptibility Scaling ($\chi/\chi_0$)')
ax4.set_title('Anisotropy Effects (Analytical Trend)')
ax4.legend()
ax4.grid(True, alpha=0.5)

# Note: The prompt asked for explicit graphics on Anisotropy. The theoretical context
# provides specific forms: chi ~ (4pi m_x alpha r_m)/(1+sqrt(r_m)).
# The above plot visualizes the denominator suppression when r < 1 (isotropic baseline).
# If r>1, it enhances. Let's plot 0.1 to 10 to show the full effect.
ax4.clear()
r_vals_log = np.logspace(-1, 1, 200)
# Normalized to r=1.
# Text implies: chi_xy/chi_0(r_m) proportional to r_m / (1 + sqrt(r_m)) (assuming definition of chi_0 specific)
# Here we just plot the functional dependence f(r) = r / (1 + sqrt(r))
f_r_m = r_vals_log / (1 + np.sqrt(r_vals_log))
f_r_alpha = r_vals_log / (1 + r_vals_log)

ax4.semilogx(r_vals_log, f_r_m, label=r'Mass Anisotropy $\propto r_m/(1+\sqrt{r_m})$')
ax4.semilogx(r_vals_log, f_r_alpha, label=r'SOC Anisotropy $\propto r_\alpha/(1+r_\alpha)$', linestyle='--')
ax4.axvline(x=1, color='k', linestyle=':')
ax4.set_xlabel(r'Anisotropy Ratio ($r$)')
ax4.set_ylabel(r'Relative Response Factor')
ax4.set_title('Anisotropy Boost Factor')
ax4.legend()
ax4.grid(True, which='both', alpha=0.5)

# --- 4.5 Anisotropy Map (Heatmap) ---
# Visualize dependence on both r_m and r_alpha simultaneously
# Using a simplified combined factor model f(rm, ra) = (rm / (1+sqrt(rm))) * (ra / (1+ra))
# This combines the independent boosting effects mentioned in text context.
ax5 = fig.add_subplot(2, 3, 5)
Rm, Ra = np.meshgrid(np.linspace(0.1, 5, 50), np.linspace(0.1, 5, 50))
Z = (Rm / (1 + np.sqrt(Rm))) * (Ra / (1 + Ra))

c = ax5.pcolormesh(Rm, Ra, Z, shading='auto', cmap='viridis')
ax5.set_xlabel(r'Mass Ratio $r_m$')
ax5.set_ylabel(r'SOC Ratio $r_\alpha$')
ax5.set_title('Combined Anisotropy Susceptibility Map')
plt.colorbar(c, ax=ax5, label='Relative Response')


# ==========================================
# 5. Numerical Output
# ==========================================
print(f"\n--- Numerical Results for Au(111) Baseline ---")
E_vec = np.array([params['E_mag'], 0, 0])
M_vec, pref, regime = calculate_edelstein_magnetization(
    E_vec, params['alpha_R'], params['m_eff'],
    params['tau'], params['E_F']
)

M_mag = np.linalg.norm(M_vec)
print(f"Regime: {regime}")
print(f"Magnetization Magnitude: {M_mag:.2e} A/m")
print(f"Magnetization Direction: {M_vec / M_mag}")
print(f"Susceptibility Coefficient (|M|/|E|): {pref:.4e} A s / m^2")

# Verify cross product relationship
cross_check = np.cross(np.array([0,0,1]), E_vec/params['E_mag'])
print(f"Check Direction M || z x E: {np.allclose(M_vec/M_mag, cross_check)}")

plt.tight_layout()
print("\nGenerating Graphics...")
plt.show()
```
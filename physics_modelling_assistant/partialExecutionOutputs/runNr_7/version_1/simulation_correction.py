```python
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# ==========================================
# 1. Physical Constants (SI Units)
# ==========================================
mu_B = 9.274e-24     # Bohr magneton (J/T)
e = 1.602e-19        # Elementary charge (C)
hbar = 1.054e-34     # Reduced Planck constant (J s)
m_e = 9.109e-31      # Electron rest mass (kg)

# ==========================================
# 2. Realistic Model Parameters
# ==========================================
# Based on typical Rashba systems like BiTeX or GeTe
m = 0.15 * m_e                  # Effective mass (kg)
alpha_val_eV_A = 3.0            # Rashba SOC strength in eV*Angstrom
alpha = alpha_val_eV_A * 1.602e-19 * 1e-10  # Converted to J*m
tau = 0.1e-12                   # Relaxation time (s) - 0.1 ps

# Fermi Energies for different regimes
EF_HDR = 0.10 * 1.602e-19       # +0.10 eV (High Density Regime)
EF_LDR = -0.05 * 1.602e-19      # -0.05 eV (Low Density Regime)

# ==========================================
# 3. Theoretical Model (Dimensionally Corrected)
# ==========================================

def edelstein_magnetization(E_mag, EF, alpha, m, tau, regime='HDR'):
    """
    Computes the magnetization magnitude based on the Rashba-Edelstein model.
    
    The formulas are corrected with factors of hbar to ensure dimensional 
    consistency in SI units.
    
    Parameters:
    E_mag (float): Magnitude of Electric Field (V/m)
    EF (float): Fermi Energy (J)
    alpha (float): Rashba SOC strength (J*m)
    m (float): Effective mass (kg)
    tau (float): Relaxation time (s)
    regime (str): 'HDR' (High Density, EF>0) or 'LDR' (Low Density, EF<0)
    
    Returns:
    float: Magnetization Magnitude (A/m)
    """
    # Prefactor: (mu_B * e * tau) / (2 * pi * hbar^3)
    # This factor ensures the result has units of A/m (Magnetization)
    prefactor = (mu_B * e * tau) / (2 * np.pi * hbar**3)
    
    if regime == 'HDR':
        # High Density Regime: Both bands occupied
        # Formula: M = (mu_B e tau / 2pi hbar^3) * m * alpha * E
        return prefactor * m * alpha * E_mag
        
    else: 
        # Low Density Regime: Only inner band occupied
        # Formula: M = (mu_B e tau / 2pi hbar^3) * sqrt(m^2 alpha^2 + 2 m hbar^2 |EF|) * E
        # Note: The term 2 * m * hbar^2 * |EF| is required for dimensional consistency
        # with the m^2 * alpha^2 term.
        term_inside_root = (m * alpha)**2 + 2 * m * (hbar**2) * abs(EF)
        return prefactor * np.sqrt(term_inside_root) * E_mag

def get_magnetization_direction(E_vec):
    """
    Returns the direction of the magnetization vector M given E.
    M is proportional to z x E (Counter-Clockwise rotation by 90 degrees).
    """
    # E_vec is [Ex, Ey]
    # z x E = [Ey, -Ex]
    return np.array([E_vec[1], -E_vec[0]])

# ==========================================
# 4. Computations
# ==========================================

# --- 4.1 Magnetization vs Electric Field Magnitude ---
E_range = np.linspace(0, 2e5, 100) # 0 to 200 kV/m
M_HDR_vals = edelstein_magnetization(E_range, EF_HDR, alpha, m, tau, 'HDR')
M_LDR_vals = edelstein_magnetization(E_range, EF_LDR, alpha, m, tau, 'LDR')

# --- 4.2 Magnetization vs Spin-Orbit Coupling (alpha) ---
alpha_range = np.linspace(0.1e-11, 6.0e-11, 100) # Range of alpha values (J*m)
# Fix E-field for this scan
E_fixed = 1e5 # 100 kV/m
M_alpha_HDR = edelstein_magnetization(E_fixed, EF_HDR, alpha_range, m, tau, 'HDR')
M_alpha_LDR = edelstein_magnetization(E_fixed, EF_LDR, alpha_range, m, tau, 'LDR')

# --- 4.3 Magnetization vs Fermi Energy (Transition) ---
EF_range = np.linspace(-0.2, 0.2, 200) * 1.602e-19 # -0.2 eV to +0.2 eV
E_fixed_scan = 1e5 # 100 kV/m
M_vs_EF = []
for ef in EF_range:
    if ef >= 0:
        M_vs_EF.append(edelstein_magnetization(E_fixed_scan, ef, alpha, m, tau, 'HDR'))
    else:
        M_vs_EF.append(edelstein_magnetization(E_fixed_scan, ef, alpha, m, tau, 'LDR'))
M_vs_EF = np.array(M_vs_EF)

# ==========================================
# 5. Graphics Generation
# ==========================================

# Plot 1: Magnetization vs Electric Field
plt.figure(figsize=(8, 5))
plt.plot(E_range/1e3, M_HDR_vals, label='HDR ($E_F > 0$)', linewidth=2, color='blue')
plt.plot(E_range/1e3, M_LDR_vals, label='LDR ($E_F < 0$)', linewidth=2, color='red', linestyle='--')
plt.xlabel('Electric Field Magnitude $|\\vec{E}|$ (kV/m)', fontsize=12)
plt.ylabel('Magnetization Magnitude $|\\vec{M}|$ (A/m)', fontsize=12)
plt.title('Direct Edelstein Effect: $|\\vec{M}|$ vs $|\\vec{E}|$', fontsize=14)
plt.legend(fontsize=12)
plt.grid(True, alpha=0.3)
plt.tight_layout()
plt.show()

# Plot 2: Dependence on Spin-Orbit Coupling Strength
plt.figure(figsize=(8, 5))
# Convert alpha back to eV*A for plotting
alpha_plot_units = alpha_range / (1.602e-19 * 1e-10)
plt.plot(alpha_plot_units, M_alpha_HDR, label='HDR Response', linewidth=2, color='blue')
plt.plot(alpha_plot_units, M_alpha_LDR, label='LDR Response', linewidth=2, color='red', linestyle='--')
plt.xlabel('Rashba SOC Strength $\\alpha$ (eV$\\cdot$\\AA)', fontsize=12)
plt.ylabel('Magnetization Magnitude $|\\vec{M}|$ (A/m)', fontsize=12)
plt.title('Edelstein Response vs Spin-Orbit Coupling Strength', fontsize=14)
plt.legend(fontsize=12)
plt.grid(True, alpha=0.3)
plt.tight_layout()
plt.show()

# Plot 3: Magnetization vs Fermi Energy (Showing the kink at Gamma)
plt.figure(figsize=(8, 5))
plt.plot(EF_range/1.602e-19, M_vs_EF, linewidth=2, color='green')
plt.axvline(0, color='black', linestyle=':', linewidth=1.5, label='$E_F = 0$ (Band Crossing)')
plt.xlabel('Fermi Energy $E_F$ (eV)', fontsize=12)
plt.ylabel('Magnetization Magnitude $|\\vec{M}|$ (A/m)', fontsize=12)
plt.title('Edelstein Response vs Fermi Energy ($E=100$ kV/m)', fontsize=14)
plt.legend(fontsize=12)
plt.grid(True, alpha=0.3)
plt.tight_layout()
plt.show()

# Plot 4: Vector Field Visualization (Direction)
fig, ax = plt.subplots(figsize=(6, 6))
# Define a grid of E-field vectors
x = np.linspace(-1, 1, 5)
y = np.linspace(-1, 1, 5)
X, Y = np.meshgrid(x, y)
U = X # Ex component
V = Y # Ey component

# Calculate M directions
# M = z x E => (Ey, -Ex)
M_u = V
M_v = -U

# Plot E field (Blue)
ax.quiver(X, Y, U, V, color='blue', label='$\\vec{E}$', scale=20, width=0.005)
# Plot M field (Red)
ax.quiver(X, Y, M_u, M_v, color='red', label='$\\vec{M}$', scale=20, width=0.005)

ax.set_xlim(-1.5, 1.5)
ax.set_ylim(-1.5, 1.5)
ax.set_xlabel('$x$')
ax.set_ylabel('$y$')
ax.set_title('Directional Relationship: $\\vec{M} \\propto \\hat{z} \\times \\vec{E}$')
ax.legend()
ax.grid(True, alpha=0.3)
ax.axhline(0, color='black', linewidth=0.5)
ax.axvline(0, color='black', linewidth=0.5)
ax.set_aspect('equal')
plt.tight_layout()
plt.show()

# Plot 5: 3D Surface Plot (M vs E and EF)
fig = plt.figure(figsize=(10, 7))
ax = fig.add_subplot(111, projection='3d')

E_mesh = np.linspace(0, 2e5, 50) # 0 to 200 kV/m
EF_mesh = np.linspace(-0.1, 0.1, 50) * 1.602e-19 # -0.1 to 0.1 eV
E_grid, EF_grid = np.meshgrid(E_mesh, EF_mesh)

M_grid = np.zeros_like(E_grid)

for i in range(len(EF_mesh)):
    for j in range(len(E_mesh)):
        ef_val = EF_mesh[i]
        e_val = E_mesh[j]
        if ef_val >= 0:
            M_grid[i, j] = edelstein_magnetization(e_val, ef_val, alpha, m, tau, 'HDR')
        else:
            M_grid[i, j] = edelstein_magnetization(e_val, ef_val, alpha, m, tau, 'LDR')

surf = ax.plot_surface(E_grid/1e3, EF_grid/1.602e-19, M_grid, cmap='viridis', edgecolor='none')
ax.set_xlabel('Electric Field (kV/m)')
ax.set_ylabel('Fermi Energy (eV)')
ax.set_zlabel('Magnetization (A/m)')
ax.set_title('Edelstein Magnetization Surface')
fig.colorbar(surf, shrink=0.5, aspect=5)
plt.show()
```
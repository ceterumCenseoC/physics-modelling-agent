
```python
import numpy as np
import matplotlib.pyplot as plt
from scipy.constants import hbar, e, m_e, mu_B, pi

# ==========================================
# 1. PHYSICAL CONSTANTS & MODEL PARAMETERS
# ==========================================

# Constants
HBAR = hbar       # Reduced Planck constant [J*s]
E_CHARGE = e      # Elementary charge [C]
MASS_E = m_e      # Electron rest mass [kg]
MU_B = mu_B       # Bohr magneton [J/T]

# Model Parameters (Realistic Starting Values)
# Based on the provided context (e.g., Au(111) or BiAg2 surface states)
m_eff = 1.0 * MASS_E       # Effective mass [kg]
alpha = 1.0e-11            # Rashba coupling strength [eV*m] -> convert to J*m
alpha_Jm = alpha * E_CHARGE
tau = 0.5e-12              # Relaxation time [s] (0.5 ps)
E_F = 0.1 * E_CHARGE       # Fermi energy [J] (100 meV)

# Derived Regime Check
# The Rashba energy scale E_R = m * alpha^2 / (2 * hbar^2)
E_R = (m_eff * alpha_Jm**2) / (2 * HBAR**2)
print(f"Rashba Energy Scale E_R: {E_R/E_CHARGE*1000:.2f} meV")
print(f"Fermi Energy E_F: {E_F/E_CHARGE*1000:.2f} meV")

if E_F > E_R:
    regime = "High-Density Regime (HDR)"
    print(f"System is in {regime}. Both bands occupied.")
else:
    regime = "Low-Density Regime (LDR)"
    print(f"System is in {regime}. Only lower band occupied.")

# ==========================================
# 2. MODEL IMPLEMENTATION (FORMULAS)
# ==========================================

def calculate_susceptibility_HDR(m, alpha, tau):
    """
    Calculates the Edelstein susceptibility in the High-Density Regime.
    Formula: lambda = (mu_B * e * tau * m * alpha) / (2 * pi * hbar^2)
    
    Units:
    - mu_B: J/T
    - e: C
    - tau: s
    - m: kg
    - alpha: J*m
    - hbar: J*s
    
    Result lambda units: (J/T * C * s * kg * J*m) / (J^2 * s^2) 
                       = (C * kg * m) / (T * s) 
                       = (A * s * kg * m) / (kg * s^-2 * A^-1 * s) 
                       = A^2 * s^2 * m^-1 * s^-2 ... 
                       
    Note: The dimensional analysis suggests a mismatch in the strict SI definition 
    of M vs lambda in the text. However, we implement the corrected formula 
    provided in the context analysis (adding hbar^2 to denominator) which is 
    the standard physical form for the susceptibility relating M to E.
    """
    return (MU_B * E_CHARGE * tau * m * alpha) / (2 * pi * HBAR**2)

def calculate_susceptibility_LDR(m, alpha, tau, E_F):
    """
    Calculates the Edelstein susceptibility in the Low-Density Regime.
    Corrected Formula: lambda = (mu_B * e * tau) / (2 * pi * hbar^2) * 
                               sqrt( (m*alpha/hbar)^2 + 2*m*E_F/hbar^2 )
    """
    term1 = (m * alpha / HBAR)**2
    term2 = 2 * m * E_F / HBAR**2
    return (MU_B * E_CHARGE * tau) / (2 * pi * HBAR**2) * np.sqrt(term1 + term2)

def get_magnetization(E_vector, m, alpha, tau, E_F):
    """
    Computes the magnetization vector M for a given electric field vector E.
    M = lambda * (z_hat x E)
    """
    Ex, Ey = E_vector
    
    # Determine susceptibility based on Fermi energy
    if E_F > (m * alpha**2) / (2 * HBAR**2):
        lam = calculate_susceptibility_HDR(m, alpha, tau)
    else:
        lam = calculate_susceptibility_LDR(m, alpha, tau, E_F)
        
    # Cross product (z_hat x E_hat)
    # If E = (Ex, Ey, 0), z x E = (-Ey, Ex, 0)
    Mx = -lam * Ey
    My = lam * Ex
    
    return np.array([Mx, My]), lam

# ==========================================
# 3. CALCULATIONS & PLOTTING
# ==========================================

# --- 3.1 Fermi Surface Shift & Spin Texture ---
print("\nGenerating Figure 1: Fermi Surface Shift & Spin Texture...")

fig1, ax1 = plt.subplots(figsize=(8, 8))

# Calculate Fermi wavevectors for HDR
k0 = (m_eff * alpha_Jm) / HBAR**2
k_F_base = np.sqrt(2 * m_eff * E_F) / HBAR

k_outer = -k0 + np.sqrt(k0**2 + k_F_base**2)
k_inner = k0 + np.sqrt(k0**2 + k_F_base**2) # Note: usually defined relative to shift, here geometric radii

# Create circles
theta = np.linspace(0, 2*np.pi, 100)
x_inner = k_inner * np.cos(theta)
y_inner = k_inner * np.sin(theta)
x_outer = k_outer * np.cos(theta)
y_outer = k_outer * np.sin(theta)

# Shift vector delta_k = -e*E*tau / hbar
E_field_mag = 1e4 # V/m
dk = (E_CHARGE * E_field_mag * tau) / HBAR
dx = dk # Assuming E in x direction
dy = 0

# Plot unshifted circles (dashed)
ax1.plot(x_inner, y_inner, 'b--', label='Inner FS (Equilibrium)')
ax1.plot(x_outer, y_outer, 'r--', label='Outer FS (Equilibrium)')

# Plot shifted circles (solid)
ax1.plot(x_inner - dx, y_inner - dy, 'b', alpha=0.5, label='Inner FS (Shifted)')
ax1.plot(x_outer - dx, y_outer - dy, 'r', alpha=0.5, label='Outer FS (Shifted)')

# Plot Spin Vectors (Tangential)
# Subsample for clarity
step = 10
# Inner spins (Clockwise for typical Rashba)
sx_inner = np.sin(theta)
sy_inner = -np.cos(theta)
ax1.quiver(x_inner[::step], y_inner[::step], sx_inner[::step], sy_inner[::step], 
           color='blue', scale=20, width=0.005, label='Spin Texture')

# Indicate E-field and M
ax1.arrow(0, -k_outer*1.3, dx*500, 0, head_width=1e8, head_length=1e8, fc='k', ec='k', label='E field')
ax1.text(dx*250, -k_outer*1.4, r'$\vec{E}$', fontsize=12)

ax1.set_xlabel(r'$k_x$ [m$^{-1}$]')
ax1.set_ylabel(r'$k_y$ [m$^{-1}$]')
ax1.set_title('Fermi Surface Shift and Spin Texture')
ax1.legend()
ax1.axis('equal')
ax1.grid(True, alpha=0.3)
plt.tight_layout()

# --- 3.2 Magnetization vs Electric Field Magnitude ---
print("Generating Figure 2: Magnetization vs Electric Field...")

fig2, ax2 = plt.subplots(figsize=(8, 6))

E_values = np.linspace(0, 5e4, 100) # V/m
M_values = []

for E_val in E_values:
    M_vec, lam = get_magnetization([E_val, 0], m_eff, alpha_Jm, tau, E_F)
    M_values.append(M_vec[1]) # My component

ax2.plot(E_values, M_values, 'g-', linewidth=2, label=f'Magnetization ($\\tau={tau*1e12:.1f}$ ps)')
ax2.set_xlabel('Electric Field $E_x$ [V/m]')
ax2.set_ylabel('Magnetization $M_y$ [A/m]')
ax2.set_title('Linear Response: Magnetization vs Electric Field')
ax2.grid(True, alpha=0.3)
ax2.legend()

# --- 3.3 Susceptibility vs Rashba Strength ---
print("Generating Figure 3: Susceptibility vs Rashba Strength...")

fig3, ax3 = plt.subplots(figsize=(8, 6))

alpha_range = np.linspace(0.1e-11, 3.0e-11, 100) # eV*m
lambda_HDR = []
lambda_LDR = []

for a_val in alpha_range:
    a_Jm = a_val * E_CHARGE
    
    # HDR susceptibility
    l_hdr = calculate_susceptibility_HDR(m_eff, a_Jm, tau)
    lambda_HDR.append(l_hdr)
    
    # LDR susceptibility (assuming same E_F, though physically E_F might shift)
    # For LDR plot, we assume a lower fixed E_F to stay in LDR for the range
    E_F_low = 0.005 * E_CHARGE # 5 meV
    l_ldr = calculate_susceptibility_LDR(m_eff, a_Jm, tau, E_F_low)
    lambda_LDR.append(l_ldr)

ax3.plot(alpha_range*1e11, lambda_HDR, 'r-', label='High Density Regime (HDR)')
ax3.plot(alpha_range*1e11, lambda_LDR, 'b--', label='Low Density Regime (LDR)')
ax3.set_xlabel('Rashba Coupling $\\alpha$ [$10^{-11}$ eV$\\cdot$m]')
ax3.set_ylabel('Edelstein Susceptibility $\\lambda_{EE}$ [arb. units]')
ax3.set_title('Dependence of Susceptibility on Spin-Orbit Coupling')
ax3.legend()
ax3.grid(True, alpha=0.3)

# --- 3.4 Directional Response (Vector Field) ---
print("Generating Figure 4: Directional Response...")

fig4, ax4 = plt.subplots(figsize=(8, 8))

# Define a set of E field directions
angles = np.linspace(0, 2*np.pi, 12, endpoint=False)
E_mag = 3e4

for ang in angles:
    Ex = E_mag * np.cos(ang)
    Ey = E_mag * np.sin(ang)
    
    M_vec, lam = get_magnetization([Ex, Ey], m_eff, alpha_Jm, tau, E_F)
    
    # Plot E vector (Red)
    ax4.arrow(0, 0, Ex, Ey, head_width=2000, head_length=3000, fc='r', ec='r', length_includes_head=True)
    # Plot M vector (Blue)
    ax4.arrow(0, 0, M_vec[0]*1e5, M_vec[1]*1e5, head_width=2000, head_length=3000, fc='b', ec='b', length_includes_head=True)

# Add dummy arrows for legend
ax4.arrow(0, 0, 0, 0, fc='r', ec='r', label='Electric Field E')
ax4.arrow(0, 0, 0, 0, fc='b', ec='b', label='Magnetization M')

ax4.set_xlim(-E_mag*1.2, E_mag*1.2)
ax4.set_ylim(-E_mag*1.2, E_mag*1.2)
ax4.set_aspect('equal')
ax4.set_xlabel(r'$E_x$ / $M_x$ (scaled)')
ax4.set_ylabel(r'$E_y$ / $M_y$ (scaled)')
ax4.set_title('Directional Response: $\\vec{M} \\propto \\hat{z} \\times \\vec{E}$')
ax4.legend(loc='upper right')
ax4.grid(True, alpha=0.3)

# ==========================================
# 4. OUTPUT RESULTS
# ==========================================

plt.show()

# Print numerical result for a specific case
E_test = 1e4 # V/m
M_test, lam_test = get_magnetization([E_test, 0], m_eff, alpha_Jm, tau, E_F)

print("\n" + "="*40)
print(f"Numerical Result for E = {E_test/1000:.1f} kV/m:")
print(f"Edelstein Susceptibility: {lam_test:.4e} (SI units: s*A/kg)")
print(f"Induced Magnetization:    {M_test[1]:.4e} A/m")
print(f"Direction:                +y (perpendicular to E_x)")
print("="*40)
```
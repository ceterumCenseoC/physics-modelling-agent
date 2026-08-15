
```python
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import FancyArrowPatch
from mpl_toolkits.mplot3d import proj3d

# ==========================================
# 1. Physical Constants (SI Units)
# ==========================================
hbar = 1.0545718e-34       # Reduced Planck constant [J*s]
e_charge = 1.6021766e-19   # Elementary charge [C]
mu_B = 9.2740099e-24       # Bohr magneton [J/T]
m_e = 9.10938356e-31       # Free electron mass [kg]

# ==========================================
# 2. Model Parameters (InGaAs Quantum Well)
# ==========================================
# Effective mass (0.05 * m_e)
m_star = 0.05 * m_e        

# Rashba coupling strength (eV*m -> J*m)
# Value: 1.0e-11 eV*m
alpha_R_eVm = 1.0e-11      
alpha_R = alpha_R_eVm * e_charge 

# Fermi energy (meV -> J)
# Value: 50 meV
E_F_meV = 50.0             
E_F = E_F_meV * 1e-3 * e_charge

# Momentum relaxation time (s)
tau = 1.0e-12              # 1 picosecond

# Lande g-factor
g_factor = -15.0           

# ==========================================
# 3. Model Functions
# ==========================================

def calculate_fermi_wavevectors(m_s, alpha, E_Fermi):
    """
    Calculates Fermi wavevectors k_F+ and k_F- for the two bands.
    
    Formula: k_F^lambda = (m*/hbar^2) * (sqrt(alpha^2 + 2*hbar^2*E_F/m*) - lambda*alpha)
    """
    term_under_root = alpha**2 + (2 * hbar**2 * E_Fermi) / m_s
    
    if term_under_root < 0:
        raise ValueError("Fermi energy is too low (inside the gap).")
        
    k_scale = (m_s / hbar**2) * np.sqrt(term_under_root)
    k_offset = (m_s / hbar**2) * alpha
    
    k_F_plus = k_scale - k_offset    # Band lambda = +1
    k_F_minus = k_scale + k_offset   # Band lambda = -1
    
    # Physical constraint: k must be positive
    if k_F_plus < 0: k_F_plus = 0
    
    return k_F_plus, k_F_minus

def calculate_edelstein_magnetization(m_s, alpha, E_Fermi, tau, g, E_vec):
    """
    Calculates the non-equilibrium magnetization M (Edelstein effect).
    
    M = (g * mu_B * e * tau * m* / (4 * pi * hbar^3)) * 
        sqrt(alpha^2 + 2*hbar^2*E_F/m*) * (E_vec x z_hat)
        
    Returns:
        M_vec (numpy array): Magnetization vector [Mx, My, Mz] in units of A/m
    """
    E_mag = np.linalg.norm(E_vec)
    if E_mag == 0:
        return np.array([0.0, 0.0, 0.0])
    
    # Pre-factor coefficient
    term_under_root = alpha**2 + (2 * hbar**2 * E_Fermi) / m_s
    scale_factor = np.sqrt(term_under_root)
    
    prefactor = (g * mu_B * e_charge * tau * m_s) / (4 * np.pi * hbar**3)
    
    M_magnitude = prefactor * scale_factor * E_mag
    
    # Direction: z_hat cross E_hat
    # If E = (Ex, Ey, 0), then M = (Ey, -Ex, 0) * (M_magnitude / E_mag)
    # Because z x E = (0,0,1) x (Ex, Ey, 0) = (-Ey, Ex, 0) ? 
    # Check: (0,0,1) x (1,0,0) = (0,1,0) -> y-direction. Correct.
    # Formula: (0,0,1) x (Ex, Ey, 0) = (-Ey, Ex, 0)
    
    M_x = -E_vec[1] * (M_magnitude / E_mag)
    M_y =  E_vec[0] * (M_magnitude / E_mag)
    M_z = 0.0
    
    return np.array([M_x, M_y, M_z])

def dispersion_relation(k, m_s, alpha, lambda_band):
    """
    Returns energy epsilon for a given k and band index lambda (+1, -1).
    epsilon = (hbar^2 * k^2) / (2m*) + lambda * alpha * k
    """
    return (hbar**2 * k**2) / (2 * m_s) + lambda_band * alpha * k

# ==========================================
# 4. Simulation and Visualization
# ==========================================

def run_simulation():
    print("--- Edelstein Effect Simulation ---")
    print(f"System: InGaAs Quantum Well")
    print(f"Parameters: m*={m_star/m_e:.2f}me, alpha_R={alpha_R_eVm:.2e}eVm, Ef={E_F_meV:.0f}meV")
    
    # --- 1. Basic Calculation Check ---
    k_plus, k_minus = calculate_fermi_wavevectors(m_star, alpha_R, E_F)
    print(f"\nFermi Wavevectors: k+={k_plus:.2e}, k-={k_minus:.2e} [1/m]")
    
    # Calculate M for a specific E field (e.g., 500 V/m in x direction)
    E_test = np.array([500.0, 0.0, 0.0]) # V/m
    M_test = calculate_edelstein_magnetization(m_star, alpha_R, E_F, tau, g_factor, E_test)
    print(f"\nTest Case: E = {E_test[0]} V/m")
    print(f"Magnetization M = [{M_test[0]:.2e}, {M_test[1]:.2e}, {M_test[2]:.2e}] A/m")
    print(f"Magnitude |M| = {np.linalg.norm(M_test):.2e} A/m")
    
    # --- 2. Graphics: Magnitude vs Electric Field ---
    E_values = np.linspace(0, 2000, 100) # V/m
    M_y_values = []
    
    for E_val in E_values:
        E_vec = np.array([E_val, 0.0, 0.0])
        M_vec = calculate_edelstein_magnetization(m_star, alpha_R, E_F, tau, g_factor, E_vec)
        M_y_values.append(M_vec[1])
        
    plt.figure(figsize=(8, 5))
    plt.plot(E_values, M_y_values, 'b-', linewidth=2)
    plt.title(f'Edelstein Magnetization vs Electric Field ($E_\\parallel \\hat{{x}}$)')
    plt.xlabel('Electric Field $E_x$ [V/m]')
    plt.ylabel('Magnetization $M_y$ [A/m]')
    plt.grid(True, alpha=0.3)
    plt.axhline(0, color='k', linewidth=1)
    plt.text(1000, np.max(M_y_values)*0.8, f'Linear Response\n(Slope $\chi_{{EE}}$)', ha='center')
    plt.tight_layout()
    plt.show()
    
    # --- 3. Graphics: Parameter Dependence (Alpha_R) ---
    alpha_range = np.linspace(0.1e-11, 3.0e-11, 50) # eV*m
    M_vs_alpha = []
    
    # Fixed Field for comparison
    E_fixed = np.array([500.0, 0.0, 0.0]) 
    
    for a_val in alpha_range:
        a_SI = a_val * e_charge
        M_temp = calculate_edelstein_magnetization(m_star, a_SI, E_F, tau, g_factor, E_fixed)
        M_vs_alpha.append(np.linalg.norm(M_temp))
        
    plt.figure(figsize=(8, 5))
    plt.plot(alpha_range, M_vs_alpha, 'r-', linewidth=2)
    plt.title('Magnetization Dependence on Rashba Coupling $\\alpha_R$')
    plt.xlabel('Rashba Coupling $\\alpha_R$ [eV$\\cdot$m]')
    plt.ylabel('$|M|$ [A/m]')
    plt.grid(True, alpha=0.3)
    plt.tight_layout()
    plt.show()
    
    # --- 4. Graphics: Fermi Contours ---
    # Plot the two circles in k-space corresponding to E_F
    plt.figure(figsize=(6, 6))
    theta = np.linspace(0, 2*np.pi, 100)
    
    # Band +1
    x_plus = k_plus * np.cos(theta)
    y_plus = k_plus * np.sin(theta)
    plt.plot(x_plus, y_plus, label='Band $\\lambda = +1$ (Outer)')
    
    # Band -1 (only if it exists)
    if k_minus > 0:
        x_minus = k_minus * np.cos(theta)
        y_minus = k_minus * np.sin(theta)
        plt.plot(x_minus, y_minus, label='Band $\\lambda = -1$ (Inner)')
        
    plt.title(f'Fermi Contours ($E_F = {E_F_meV}$ meV)')
    plt.xlabel('$k_x$ [1/m]')
    plt.ylabel('$k_y$ [1/m]')
    plt.axis('equal')
    plt.legend()
    plt.grid(True, alpha=0.3)
    
    # Add text for spin texture
    plt.text(0, 0, 'Spin locked\n$\\perp \\mathbf{k}$', ha='center', va='center', fontsize=10, color='white', bbox=dict(facecolor='black', alpha=0.5))
    
    plt.tight_layout()
    plt.show()
    
    # --- 5. Graphics: Vector Orientation (3D representation simplified to 2D) ---
    # Showing that M is perpendicular to E
    fig, ax = plt.subplots(figsize=(6, 6))
    
    # Draw E-field arrow (Red)
    # Arbitrary angle
    angle_E = np.pi / 4
    E_len = 1.0
    ax.arrow(0, 0, E_len*np.cos(angle_E), E_len*np.sin(angle_E), 
             head_width=0.05, head_length=0.1, fc='r', ec='r', label='Electric Field E')
    
    # Draw Magnetization arrow (Blue)
    # M is rotated +90 degrees from E (z cross E)
    # In 2D plane: (cos, sin) -> (-sin, cos)
    M_len = 0.8 # Just for visualization scale
    ax.arrow(0, 0, M_len*(-np.sin(angle_E)), M_len*(np.cos(angle_E)), 
             head_width=0.05, head_length=0.1, fc='b', ec='b', label='Magnetization M')
             
    ax.set_xlim(-1.2, 1.2)
    ax.set_ylim(-1.2, 1.2)
    ax.set_aspect('equal')
    ax.grid(True, alpha=0.3)
    ax.set_title('Vector Relationship: $\\mathbf{M} \\perp \\mathbf{E}$')
    ax.legend(loc='upper right')
    
    # Remove ticks for cleaner vector plot
    ax.set_xticks([])
    ax.set_yticks([])
    
    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    run_simulation()
```
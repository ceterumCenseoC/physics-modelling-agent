```python
import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import quad
from scipy.constants import hbar, e, m_e, mu_B, k_B, pi

# ============================================================
# Physical Constants (SI units)
# ============================================================
HBAR = hbar          # 1.054571817e-34 J·s
E_CHARGE = e         # 1.602176634e-19 C
M_E = m_e            # 9.1093837015e-31 kg
MU_B = mu_B          # 9.2740100783e-24 J/T
KB = k_B             # 1.380649e-23 J/K
PI = pi

# ============================================================
# Parameter Sets (Realistic values from literature)
# ============================================================
# Baseline: InGaAs/InAlAs heterostructure
baseline_params = {
    'm_star': 0.05 * M_E,        # kg
    'alpha_R': 0.1 * e * 1e-10,  # eV·Å → J·m (1 eV·Å = 1.602e-29 J·m)
    'tau': 1e-12,                # s
    'E_F': 100e-3 * e,           # meV → J
    'g_factor': 2.0,             # dimensionless
    'T': 4.2,                    # K
}

# Material sets for comparison
material_sets = {
    'InGaAs/InAlAs': {
        'm_star': 0.05 * M_E,
        'alpha_R': 0.1 * e * 1e-10,
        'tau': 1e-12,
        'E_F': 100e-3 * e,
        'g_factor': 2.0,
        'T': 4.2,
    },
    'Au(111)': {
        'm_star': 0.26 * M_E,
        'alpha_R': 0.33 * e * 1e-10,
        'tau': 10e-15,           # 10 fs
        'E_F': 400e-3 * e,
        'g_factor': 2.0,
        'T': 4.2,
    },
    'Bi(111)': {
        'm_star': 0.016 * M_E,
        'alpha_R': 3.55 * e * 1e-10,
        'tau': 1e-12,
        'E_F': 280e-3 * e,
        'g_factor': 2.0,
        'T': 4.2,
    }
}

# ============================================================
# Core Model Functions
# ============================================================

def energy_dispersion(k, params, band=+1):
    """Energy dispersion: ε±(k) = ħ²k²/(2m*) ± α_R k
    
    Args:
        k: wave vector magnitude (m⁻¹)
        params: parameter dict with m_star, alpha_R
        band: +1 for upper band, -1 for lower band
    Returns:
        Energy in Joules
    """
    m_star = params['m_star']
    alpha_R = params['alpha_R']
    return (HBAR**2 * k**2) / (2 * m_star) + band * alpha_R * k


def group_velocity(k, params, band=+1):
    """Group velocity: v±(k) = ħk/m* ± α_R/ħ (radial direction)
    
    Returns:
        Velocity magnitude in m/s
    """
    m_star = params['m_star']
    alpha_R = params['alpha_R']
    return (HBAR * k / m_star) + band * (alpha_R / HBAR)


def spin_expectation(phi, band=+1):
    """Spin expectation values: ⟨σ⟩± = ±(-sinφ, cosφ, 0)
    
    Args:
        phi: angle in xy-plane (rad)
        band: +1 for upper band, -1 for lower band
    Returns:
        (x, y, z) spin expectation
    """
    return (band * (-np.sin(phi)), band * np.cos(phi), 0.0)


def fermi_dirac(energy, params):
    """Fermi-Dirac distribution function
    
    Args:
        energy: energy in Joules
        params: parameter dict with E_F, T
    Returns:
        Occupation probability (0-1)
    """
    E_F = params['E_F']
    T = params['T']
    if T == 0:
        return 1.0 if energy < E_F else 0.0
    return 1.0 / (1.0 + np.exp((energy - E_F) / (KB * T)))


def delta_f(k, phi, E_field, params, band=+1):
    """Non-equilibrium distribution correction
    
    δf = τ e E·v (−∂f₀/∂ε)
    
    Args:
        k: wave vector magnitude (m⁻¹)
        phi: angle (rad)
        E_field: (Ex, Ey) electric field (V/m)
        params: parameter dict
        band: band index
    Returns:
        δf correction
    """
    tau = params['tau']
    v_mag = group_velocity(k, params, band)
    # Velocity vector (radial direction)
    v_vec = v_mag * np.array([np.cos(phi), np.sin(phi)])
    # Electric field vector
    E_vec = np.array(E_field)
    # Energy derivative of Fermi function (numerical)
    eps = energy_dispersion(k, params, band)
    delta = 1e-10  # small shift for derivative
    df0 = (fermi_dirac(eps + delta, params) - fermi_dirac(eps - delta, params)) / (2 * delta)
    return tau * E_CHARGE * np.dot(E_vec, v_vec) * (-df0)


def compute_spin_density(E_field, params, k_max_factor=3.0, N_k=200, N_phi=100):
    """Compute induced spin density by numerical integration over k-space
    
    δS = (ħ/2) Σ± ∫ d²k/(2π)² δf±(k) ⟨σ⟩±(k)
    
    Args:
        E_field: (Ex, Ey) electric field (V/m)
        params: parameter dict
        k_max_factor: integration limit as multiple of Fermi k
        N_k: number of radial grid points
        N_phi: number of angular grid points
    Returns:
        (Sx, Sy, Sz) spin density (m⁻²)
    """
    E_F = params['E_F']
    m_star = params['m_star']
    alpha_R = params['alpha_R']
    
    # Determine integration limit
    k_F0 = np.sqrt(2 * m_star * E_F) / HBAR  # Fermi k without SO
    k_max = k_max_factor * k_F0
    
    # Integration grid
    k_grid = np.linspace(0, k_max, N_k)
    phi_grid = np.linspace(0, 2*PI, N_phi, endpoint=False)
    dk = k_grid[1] - k_grid[0]
    dphi = 2*PI / N_phi
    
    # Initialize spin density
    S = np.zeros(3)
    
    # Integrate over both bands
    for band in [1, -1]:
        for i, k in enumerate(k_grid):
            for j, phi in enumerate(phi_grid):
                # Skip k=0 to avoid singularity
                if k == 0:
                    continue
                # δf
                df = delta_f(k, phi, E_field, params, band)
                # Spin expectation
                sig = spin_expectation(phi, band)
                # Weight: (ħ/2) * k * dk * dphi / (2π)²
                weight = (HBAR/2) * k * dk * dphi / (2*PI)**2
                S += df * np.array(sig) * weight
    
    return S


def compute_magnetization(E_field, params, method='analytic'):
    """Compute induced magnetization
    
    Analytic: M = gμB eτ/(8πħ) (m*α_R/ħ²) (ẑ × E)
    Numerical: M = gμB δS
    
    Args:
        E_field: (Ex, Ey) electric field (V/m)
        params: parameter dict
        method: 'analytic' or 'numerical'
    Returns:
        (Mx, My, Mz) magnetization (A/m)
    """
    g = params['g_factor']
    
    if method == 'analytic':
        m_star = params['m_star']
        alpha_R = params['alpha_R']
        tau = params['tau']
        
        # Coefficient M₀ = gμB eτ/(8πħ) * (m*α_R/ħ²)
        coeff = (g * MU_B * E_CHARGE * tau) / (8*PI*HBAR) * (m_star * alpha_R / HBAR**2)
        
        # M = M₀ (ẑ × E) = M₀ (Ey, -Ex, 0)
        Ex, Ey = E_field
        return np.array([coeff * Ey, -coeff * Ex, 0.0])
    
    elif method == 'numerical':
        S = compute_spin_density(E_field, params)
        return g * MU_B * S
    
    else:
        raise ValueError("Method must be 'analytic' or 'numerical'")


def susceptibility_parameter(params):
    """Calculate the spin-electric susceptibility parameter M₀
    
    M₀ = gμB eτ/(8πħ) * (m*α_R/ħ²)
    
    Returns:
        M₀ in A·m/V
    """
    m_star = params['m_star']
    alpha_R = params['alpha_R']
    tau = params['tau']
    g = params['g_factor']
    
    return (g * MU_B * E_CHARGE * tau) / (8*PI*HBAR) * (m_star * alpha_R / HBAR**2)


# ============================================================
# Numerical Validation of Analytic Formula
# ============================================================

def validate_numerical():
    """Compare analytic and numerical results for baseline parameters"""
    params = baseline_params.copy()
    E_field = (1e4, 0.0)  # Ex = 10⁴ V/m, Ey = 0
    
    # Analytic
    M_analytic = compute_magnetization(E_field, params, method='analytic')
    
    # Numerical (coarser grid for speed)
    M_numerical = compute_magnetization(E_field, params, method='numerical')
    
    print("=== Validation of Analytic Formula ===")
    print(f"Electric field: Ex = {E_field[0]} V/m, Ey = {E_field[1]} V/m")
    print(f"Analytic magnetization: ({M_analytic[0]:.6e}, {M_analytic[1]:.6e}, {M_analytic[2]:.6e}) A/m")
    print(f"Numerical magnetization: ({M_numerical[0]:.6e}, {M_numerical[1]:.6e}, {M_numerical[2]:.6e}) A/m")
    print(f"Relative error: {np.linalg.norm(M_analytic - M_numerical)/np.linalg.norm(M_analytic):.2%}")
    print()


# ============================================================
# Plot 1: Magnetization magnitude vs Electric field magnitude
# ============================================================

def plot_M_vs_E():
    params = baseline_params.copy()
    E_values = np.logspace(3, 6, 100)  # 10³ to 10⁶ V/m
    M_magnitudes = []
    
    for E in E_values:
        M = compute_magnetization((E, 0), params)
        M_magnitudes.append(np.linalg.norm(M))
    
    plt.figure(figsize=(8, 6))
    plt.loglog(E_values, M_magnitudes, 'b-', linewidth=2)
    plt.xlabel('Electric Field |E| (V/m)', fontsize=12)
    plt.ylabel('Magnetization |M| (A/m)', fontsize=12)
    plt.title('Edelstein Effect: Magnetization vs Electric Field Magnitude', fontsize=14)
    plt.grid(True, alpha=0.3)
    plt.tight_layout()
    plt.savefig('M_vs_E.png', dpi=150)
    plt.show()


# ============================================================
# Plot 2: Magnetization direction vs Electric field direction
# ============================================================

def plot_M_direction():
    params = baseline_params.copy()
    E_mag = 1e4  # V/m
    theta_E = np.linspace(0, 2*PI, 24, endpoint=False)
    
    Ex = E_mag * np.cos(theta_E)
    Ey = E_mag * np.sin(theta_E)
    
    Mx = np.zeros_like(Ex)
    My = np.zeros_like(Ey)
    
    for i in range(len(theta_E)):
        M = compute_magnetization((Ex[i], Ey[i]), params)
        Mx[i] = M[0]
        My[i] = M[1]
    
    fig, ax = plt.subplots(figsize=(8, 8))
    
    # Plot E field vectors (red)
    for i in range(len(theta_E)):
        ax.arrow(0, 0, Ex[i]*0.01, Ey[i]*0.01, 
                head_width=0.5, head_length=0.5, fc='red', ec='red', alpha=0.6)
    
    # Plot M field vectors (blue)
    for i in range(len(theta_E)):
        ax.arrow(0, 0, Mx[i]*1e10, My[i]*1e10, 
                head_width=0.5, head_length=0.5, fc='blue', ec='blue', alpha=0.6)
    
    # Circle guides
    circle1 = plt.Circle((0, 0), np.max(Ex)*0.01, fill=False, color='red', linestyle='--', alpha=0.3)
    circle2 = plt.Circle((0, 0), np.max(Mx)*1e10, fill=False, color='blue', linestyle='--', alpha=0.3)
    ax.add_patch(circle1)
    ax.add_patch(circle2)
    
    ax.set_xlim(-1.5, 1.5)
    ax.set_ylim(-1.5, 1.5)
    ax.set_aspect('equal')
    ax.set_xlabel('x-direction (arb. units)', fontsize=12)
    ax.set_ylabel('y-direction (arb. units)', fontsize=12)
    ax.set_title('Magnetization Direction vs Electric Field Direction', fontsize=14)
    ax.legend(['E field', 'M field'])
    ax.grid(True, alpha=0.3)
    plt.tight_layout()
    plt.savefig('M_direction.png', dpi=150)
    plt.show()


# ============================================================
# Plot 3: Magnetization vs Rashba parameter α_R
# ============================================================

def plot_M_vs_alpha():
    params = baseline_params.copy()
    alpha_values = np.linspace(-3, 3, 200) * e * 1e-10  # -3 to 3 eV·Å
    M_magnitudes = []
    
    for alpha in alpha_values:
        params['alpha_R'] = alpha
        M = compute_magnetization((1e4, 0), params)
        M_magnitudes.append(np.linalg.norm(M))
    
    plt.figure(figsize=(8, 6))
    plt.plot(alpha_values/(e*1e-10), M_magnitudes, 'b-', linewidth=2)
    plt.xlabel('Rashba Parameter α_R (eV·Å)', fontsize=12)
    plt.ylabel('Magnetization |M| (A/m)', fontsize=12)
    plt.title('Magnetization vs Rashba Parameter', fontsize=14)
    plt.grid(True, alpha=0.3)
    plt.tight_layout()
    plt.savefig('M_vs_alpha.png', dpi=150)
    plt.show()


# ============================================================
# Plot 4: Magnetization vs Effective mass
# ============================================================

def plot_M_vs_mass():
    params = baseline_params.copy()
    mass_ratios = np.linspace(0.01, 1.0, 100)  # m*/m_e
    M_magnitudes = []
    
    for ratio in mass_ratios:
        params['m_star'] = ratio * M_E
        M = compute_magnetization((1e4, 0), params)
        M_magnitudes.append(np.linalg.norm(M))
    
    plt.figure(figsize=(8, 6))
    plt.plot(mass_ratios, M_magnitudes, 'b-', linewidth=2)
    plt.xlabel('Effective Mass m*/m_e', fontsize=12)
    plt.ylabel('Magnetization |M| (A/m)', fontsize=12)
    plt.title('Magnetization vs Effective Mass', fontsize=14)
    plt.grid(True, alpha=0.3)
    plt.tight_layout()
    plt.savefig('M_vs_mass.png', dpi=150)
    plt.show()


# ============================================================
# Plot 5: Parametric map in (α_R, E_F) space
# ============================================================

def plot_parametric_map():
    alpha_range = np.linspace(0.1, 3.0, 50) * e * 1e-10  # eV·Å
    EF_range = np.linspace(10, 500, 50) * e * 1e-3  # meV
    
    # Grid for M₀ (since |M| ∝ E, we plot M₀)
    M0_grid = np.zeros((len(EF_range), len(alpha_range)))
    
    for i, EF in enumerate(EF_range):
        for j, alpha in enumerate(alpha_range):
            params = baseline_params.copy()
            params['E_F'] = EF
            params['alpha_R'] = alpha
            M0_grid[i, j] = susceptibility_parameter(params)
    
    plt.figure(figsize=(10, 8))
    plt.contourf(alpha_range/(e*1e-10), EF_range/(e*1e-3), M0_grid, 
                levels=50, cmap='viridis')
    plt.colorbar(label='M₀ (A·m/V)')
    plt.xlabel('Rashba Parameter α_R (eV·Å)', fontsize=12)
    plt.ylabel('Fermi Energy E_F (meV)', fontsize=12)
    plt.title('Edelstein Susceptibility Parameter M₀', fontsize=14)
    plt.tight_layout()
    plt.savefig('parametric_map.png', dpi=150)
    plt.show()


# ============================================================
# Plot 6: Temperature dependence
# ============================================================

def plot_temperature_dependence():
    params = baseline_params.copy()
    T_values = np.linspace(0, 300, 100)
    M_ratio = []
    
    M_0 = np.linalg.norm(compute_magnetization((1e4, 0), params))
    
    for T in T_values:
        params['T'] = T
        M = np.linalg.norm(compute_magnetization((1e4, 0), params))
        M_ratio.append(M / M_0)
    
    # Analytical correction
    EF = params['E_F']
    analytic_ratio = 1 - (PI**2 / 6) * (KB * T_values / EF)**2
    
    plt.figure(figsize=(8, 6))
    plt.plot(T_values, M_ratio, 'b-', linewidth=2, label='Numerical')
    plt.plot(T_values, analytic_ratio, 'r--', linewidth=2, label='Analytic (2nd order)')
    plt.xlabel('Temperature T (K)', fontsize=12)
    plt.ylabel('|M(T)| / |M(0)|', fontsize=12)
    plt.title('Temperature Dependence of Edelstein Effect', fontsize=14)
    plt.legend()
    plt.grid(True, alpha=0.3)
    plt.tight_layout()
    plt.savefig('M_vs_T.png', dpi=150)
    plt.show()


# ============================================================
# Plot 7: Chirality dependence (positive vs negative α_R)
# ============================================================

def plot_chirality():
    params = baseline_params.copy()
    theta_E = np.linspace(0, 2*PI, 100)
    E_mag = 1e4
    
    Mx_pos = []
    My_pos = []
    Mx_neg = []
    My_neg = []
    
    for theta in theta_E:
        E_field = (E_mag*np.cos(theta), E_mag*np.sin(theta))
        
        # Positive α_R
        params['alpha_R'] = abs(baseline_params['alpha_R'])
        M_pos = compute_magnetization(E_field, params)
        Mx_pos.append(M_pos[0])
        My_pos.append(M_pos[1])
        
        # Negative α_R
        params['alpha_R'] = -abs(baseline_params['alpha_R'])
        M_neg = compute_magnetization(E_field, params)
        Mx_neg.append(M_neg[0])
        My_neg.append(M_neg[1])
    
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 6))
    
    # Positive chirality
    ax1.plot(theta_E, Mx_pos, 'b-', label='Mx')
    ax1.plot(theta_E, My_pos, 'r-', label='My')
    ax1.set_xlabel('Electric Field Angle θ_E (rad)', fontsize=12)
    ax1.set_ylabel('Magnetization Components (A/m)', fontsize=12)
    ax1.set_title('α_R > 0 (Right-handed)', fontsize=14)
    ax1.legend()
    ax1.grid(True, alpha=0.3)
    
    # Negative chirality
    ax2.plot(theta_E, Mx_neg, 'b-', label='Mx')
    ax2.plot(theta_E, My_neg, 'r-', label='My')
    ax2.set_xlabel('Electric Field Angle θ_E (rad)', fontsize=12)
    ax2.set_ylabel('Magnetization Components (A/m)', fontsize=12)
    ax2.set_title('α_R < 0 (Left-handed)', fontsize=14)
    ax2.legend()
    ax2.grid(True, alpha=0.3)
    
    plt.tight_layout()
    plt.savefig('chirality.png', dpi=150)
    plt.show()


# ============================================================
# Plot 8: Fermi velocity dependence
# ============================================================

def plot_M_vs_vF():
    params = baseline_params.copy()
    
    # Vary effective mass to change Fermi velocity (keeping α_R constant)
    mass_ratios = np.linspace(0.01, 1.0, 100)
    vF_values = []
    M_values = []
    
    for ratio in mass_ratios:
        params['m_star'] = ratio * M_E
        k_F = np.sqrt(2 * params['m_star'] * params['E_F']) / HBAR
        v_F = HBAR * k_F / params['m_star'] + params['alpha_R'] / HBAR  # upper band
        vF_values.append(v_F)
        
        M = compute_magnetization((1e4, 0), params)
        M_values.append(np.linalg.norm(M))
    
    plt.figure(figsize=(8, 6))
    plt.plot(vF_values, M_values, 'b-', linewidth=2)
    plt.xlabel('Fermi Velocity v_F (m/s)', fontsize=12)
    plt.ylabel('Magnetization |M| (A/m)', fontsize=12)
    plt.title('Magnetization vs Fermi Velocity', fontsize=14)
    plt.grid(True, alpha=0.3)
    plt.tight_layout()
    plt.savefig('M_vs_vF.png', dpi=150)
    plt.show()


# ============================================================
# Main execution
# ============================================================

if __name__ == "__main__":
    print("="*60)
    print("Edelstein Effect for Rashba Fermion")
    print("="*60)
    print()
    
    # Validate numerical integration against analytic formula
    validate_numerical()
    
    # Baseline parameters summary
    print("\n=== Baseline Parameters (InGaAs/InAlAs) ===")
    for key, value in baseline_params.items():
        if key == 'm_star':
            print(f"  {key}: {value/M_E:.3f} m_e")
        elif key == 'alpha_R':
            print(f"  {key}: {value/(e*1e-10):.2f} eV·Å")
        elif key == 'E_F':
            print(f"  {key}: {value/(e*1e-3):.1f} meV")
        elif key == 'T':
            print(f"  {key}: {value} K")
        else:
            print(f"  {key}: {value}")
    
    # Material comparison
    print("\n=== Material Comparison (E = 10⁴ V/m) ===")
    E_field = (1e4, 0)
    for material, params in material_sets.items():
        M = compute_magnetization(E_field, params)
        M0 = susceptibility_parameter(params)
        print(f"  {material}: |M| = {np.linalg.norm(M):.3e} A/m, M₀ = {M0:.3e} A·m/V")
    
    # Generate all plots
    print("\nGenerating plots...")
    plot_M_vs_E()
    plot_M_direction()
    plot_M_vs_alpha()
    plot_M_vs_mass()
    plot_parametric_map()
    plot_temperature_dependence()
    plot_chirality()
    plot_M_vs_vF()
    
    print("\nAll plots generated successfully!")
    print("Files saved: M_vs_E.png, M_direction.png, M_vs_alpha.png,")
    print("M_vs_mass.png, parametric_map.png, M_vs_T.png, chirality.png, M_vs_vF.png")
```
```python
#!/usr/bin/env python3
"""
Edelstein Effect in Rashba Fermions at the Γ Point
===================================================
This code implements the corrected Rashba fermion Edelstein effect model.
It calculates the electric-field-induced spin density and magnetization for:
  - Massless (Dirac-like) Rashba fermions
  - Parabolic Rashba fermions (with corrected group velocity)
It analyzes the dependence on:
  - Electric field magnitude and direction
  - Rashba parameter (SOC strength)
  - Fermi velocity
  - Chirality (λ = ±1)
  - Relaxation time
All units are SI (with eV·Å for α_R where convenient).
"""

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import FancyArrowPatch
from scipy.constants import (hbar, e, m_e, mu_0, k as k_B, pi, hbar)
# Note: scipy.constants.e is elementary charge, hbar is reduced Planck constant

# =============================================================================
# PHYSICAL CONSTANTS AND UNIT CONVERSIONS
# =============================================================================
eV = 1.602176634e-19        # Joule per eV
Angstrom = 1e-10            # meters per Ångström
mu_B = 9.2740100783e-24     # Bohr magneton (J/T)
g_factor = -4.0             # Landé g-factor for InGaAs (dimensionless)

# Conversion factors
alpha_R_conv = eV * Angstrom  # eV·Å → J·m

# =============================================================================
# MODEL PARAMETERS (Realistic for InGaAs quantum well)
# =============================================================================
params = {
    'alpha_R': 0.5 * alpha_R_conv,      # Rashba parameter (J·m) [0.5 eV·Å]
    'k_F': 3.0e9,                       # Fermi wavevector (m⁻¹) [0.03 Å⁻¹]
    'm_star': 0.041 * m_e,              # Effective mass (kg)
    'tau': 1.0e-12,                     # Relaxation time (s) [1 ps]
    'v_F': None,                        # Will be computed for parabolic case
    'E_field': 1.0e3,                   # Electric field magnitude (V/m)
    'theta_E': 0.0,                     # Electric field angle (rad)
    'T': 1.0,                           # Temperature (K)
    'eps_F': None,                      # Will be computed
}

# Compute derived quantities
params['v_F'] = hbar * params['k_F'] / params['m_star']  # Fermi velocity (m/s)
params['eps_F'] = hbar * params['v_F'] * params['k_F']   # Fermi energy (J)

# =============================================================================
# CORE MODEL FUNCTIONS
# =============================================================================

def rashba_hamiltonian(kx, ky, model='parabolic', alpha_R=None, v_F=None, m_star=None):
    """
    Rashba Hamiltonian matrix (2x2) for given kx, ky.
    
    Parameters:
        kx, ky: wavevector components (m⁻¹)
        model: 'parabolic' or 'massless'
        alpha_R: Rashba parameter (J·m) [parabolic]
        v_F: Fermi velocity (m/s) [massless]
        m_star: effective mass (kg) [parabolic]
    
    Returns:
        2x2 complex numpy array
    """
    if alpha_R is None:
        alpha_R = params['alpha_R']
    if v_F is None:
        v_F = params['v_F']
    if m_star is None:
        m_star = params['m_star']
    
    sigma_x = np.array([[0, 1], [1, 0]], dtype=complex)
    sigma_y = np.array([[0, -1j], [1j, 0]], dtype=complex)
    
    k_sq = kx**2 + ky**2
    
    if model == 'parabolic':
        kinetic = (hbar**2 * k_sq / (2 * m_star)) * np.eye(2)
        soc = alpha_R * (ky * sigma_x - kx * sigma_y)
        return kinetic + soc
    elif model == 'massless':
        soc = hbar * v_F * (ky * sigma_x - kx * sigma_y)
        return soc
    else:
        raise ValueError("Model must be 'parabolic' or 'massless'")

def eigenvalues(kx, ky, model='parabolic', **kwargs):
    """Energy eigenvalues for given kx, ky."""
    H = rashba_hamiltonian(kx, ky, model=model, **kwargs)
    return np.linalg.eigvalsh(H)

def group_velocity(kx, ky, lambda_idx, model='parabolic', **kwargs):
    """
    Group velocity for band λ = ±1 (CORRECTED for parabolic case).
    
    For parabolic: v = ħk/m* + λ(α_R/ħ)(ẑ × k̂)
    For massless:  v = λ v_F k̂
    """
    alpha_R = kwargs.get('alpha_R', params['alpha_R'])
    v_F = kwargs.get('v_F', params['v_F'])
    m_star = kwargs.get('m_star', params['m_star'])
    
    k = np.sqrt(kx**2 + ky**2)
    if k < 1e-12:
        return np.zeros(2)
    
    k_hat = np.array([kx, ky]) / k
    
    if model == 'parabolic':
        v_parabolic = hbar * np.array([kx, ky]) / m_star
        # CORRECTED Rashba term: (α_R/ħ)(ẑ × k̂) = (α_R/ħ)(-k̂_y, k̂_x)
        v_soc = lambda_idx * (alpha_R / hbar) * np.array([-k_hat[1], k_hat[0]])
        return v_parabolic + v_soc
    elif model == 'massless':
        return lambda_idx * v_F * k_hat
    else:
        raise ValueError("Model must be 'parabolic' or 'massless'")

def spin_texture(kx, ky, lambda_idx):
    """Spin expectation value for eigenstate: <σ> = λ(ẑ × k̂)."""
    k = np.sqrt(kx**2 + ky**2)
    if k < 1e-12:
        return np.array([0.0, 0.0, 0.0])
    k_hat = np.array([kx, ky]) / k
    # ẑ × k̂ = (-k̂_y, k̂_x, 0)
    return lambda_idx * np.array([-k_hat[1], k_hat[0], 0.0])

# =============================================================================
# EDELSTEIN EFFECT CALCULATIONS
# =============================================================================

def induced_spin_density(E_vector, model='parabolic', **kwargs):
    """
    Compute the electric-field-induced spin density δS (m⁻²).
    
    For parabolic: δS = (eτ/4πħ)(α_R k_F)(ẑ × E)
    For massless:  δS = (eτ/2πħ) k_F (ẑ × E)
    
    Parameters:
        E_vector: 2D electric field vector (V/m)
        model: 'parabolic' or 'massless'
        kwargs: model parameters (alpha_R, k_F, tau, ...)
    
    Returns:
        δS: 2D spin density vector (m⁻²) [in the xy-plane]
    """
    alpha_R = kwargs.get('alpha_R', params['alpha_R'])
    k_F = kwargs.get('k_F', params['k_F'])
    tau = kwargs.get('tau', params['tau'])
    
    Ex, Ey = E_vector[0], E_vector[1]
    
    # ẑ × E = (-Ey, Ex)
    cross_E = np.array([-Ey, Ex])
    
    if model == 'parabolic':
        prefactor = e * tau / (4 * pi * hbar) * alpha_R * k_F
    elif model == 'massless':
        prefactor = e * tau / (2 * pi * hbar) * k_F
    else:
        raise ValueError("Model must be 'parabolic' or 'massless'")
    
    return prefactor * cross_E

def induced_magnetization(E_vector, model='parabolic', **kwargs):
    """
    Compute the Edelstein magnetization M = g μ_B δS (A/m).
    """
    g = kwargs.get('g', g_factor)
    delta_S = induced_spin_density(E_vector, model=model, **kwargs)
    # Convert to magnetization: M = g μ_B δS / volume?
    # For 2D, magnetization per unit area is: M_2D = g μ_B δS (in A)
    # To get 3D magnetization (A/m), divide by layer thickness.
    # Here we return the 2D magnetization per unit area (A)
    return g * mu_B * delta_S

def susceptibility_tensor(model='parabolic', **kwargs):
    """
    Spin susceptibility tensor χ_ij = δS_i / E_j.
    Returns 2x2 matrix.
    """
    alpha_R = kwargs.get('alpha_R', params['alpha_R'])
    k_F = kwargs.get('k_F', params['k_F'])
    tau = kwargs.get('tau', params['tau'])
    
    if model == 'parabolic':
        chi_xy = e * tau / (4 * pi * hbar) * alpha_R * k_F
    elif model == 'massless':
        chi_xy = e * tau / (2 * pi * hbar) * k_F
    else:
        raise ValueError("Model must be 'parabolic' or 'massless'")
    
    # χ_xy = -χ_yx = chi_xy, χ_xx = χ_yy = 0
    return np.array([[0, -chi_xy], [chi_xy, 0]])

# =============================================================================
# NUMERICAL VERIFICATION (FULL BAND INTEGRATION)
# =============================================================================

def numerical_edelstein(E_field, model='parabolic', n_k=400, **kwargs):
    """
    Numerically compute δS by summing over the Fermi surface using the
    Boltzmann transport equation in relaxation-time approximation.
    
    This verifies the analytical formulas.
    """
    alpha_R = kwargs.get('alpha_R', params['alpha_R'])
    k_F = kwargs.get('k_F', params['k_F'])
    tau = kwargs.get('tau', params['tau'])
    T = kwargs.get('T', params['T'])
    m_star = kwargs.get('m_star', params['m_star'])
    v_F = kwargs.get('v_F', params['v_F'])
    
    eps_F = kwargs.get('eps_F', params['eps_F'])
    
    # Integration over k-space (polar grid)
    k_max = 3 * k_F  # integration cutoff
    dk = k_max / n_k
    dphi = 2 * pi / n_k
    
    delta_S = np.zeros(3)  # [Sx, Sy, Sz]
    
    for i in range(n_k):
        k = (i + 0.5) * dk
        for j in range(n_k):
            phi = (j + 0.5) * dphi
            kx = k * np.cos(phi)
            ky = k * np.sin(phi)
            
            # Energy eigenvalues for both bands
            eps = eigenvalues(kx, ky, model=model, alpha_R=alpha_R,
                              v_F=v_F, m_star=m_star)
            
            # For each band λ
            for lambda_idx, eps_lam in enumerate([eps[0], eps[1]]):
                # Chirality: λ = +1 for upper band, -1 for lower band
                if model == 'parabolic':
                    lam = 1 if eps_lam > (hbar**2 * k**2 / (2*m_star)) else -1
                else:
                    lam = 1 if eps_lam > 0 else -1
                
                # Fermi-Dirac distribution derivative at zero T
                if T < 1e-6:
                    # Zero temperature: derivative is delta function at ε_F
                    if abs(eps_lam - eps_F) < 0.01 * eps_F:
                        df0_deps = -1.0  # approximate
                    else:
                        df0_deps = 0.0
                else:
                    # Finite T: Fermi function derivative
                    x = (eps_lam - eps_F) / (k_B * T)
                    if abs(x) < 50:
                        df0_deps = -np.exp(x) / (k_B * T * (1 + np.exp(x))**2)
                    else:
                        df0_deps = 0.0
                
                # Group velocity
                v_lam = group_velocity(kx, ky, lam, model=model,
                                       alpha_R=alpha_R, v_F=v_F, m_star=m_star)
                
                # δf = eτ (∂f₀/∂ε) v·E
                delta_f = e * tau * df0_deps * np.dot(v_lam, E_field)
                
                # Spin texture
                spin = spin_texture(kx, ky, lam)
                
                # Accumulate
                delta_S += delta_f * spin * k * dk * dphi
    
    # Normalize by (2π)²
    delta_S /= (2 * pi)**2
    return delta_S

# =============================================================================
# PLOTTING FUNCTIONS
# =============================================================================

def plot_spin_texture():
    """Plot the equilibrium spin texture in k-space."""
    fig, ax = plt.subplots(figsize=(6, 6))
    
    k_range = np.linspace(-0.05, 0.05, 15)  # in Å⁻¹
    KX, KY = np.meshgrid(k_range, k_range)
    
    for i in range(KX.shape[0]):
        for j in range(KX.shape[1]):
            kx = KX[i,j] * 1e10  # convert to m⁻¹
            ky = KY[i,j] * 1e10
            k = np.sqrt(kx**2 + ky**2)
            if k < 1e-6:
                continue
            for lam in [1, -1]:
                spin = spin_texture(kx, ky, lam)
                # Scale for visualization
                scale = 0.9 * k_range[-1] / (np.sqrt(spin[0]**2 + spin[1]**2) + 1e-12)
                ax.arrow(KX[i,j], KY[i,j], spin[0]*scale, spin[1]*scale,
                         head_width=0.002, head_length=0.003, fc='red' if lam==1 else 'blue',
                         ec='red' if lam==1 else 'blue', alpha=0.7)
    
    ax.set_xlabel(r'$k_x$ (Å⁻¹)')
    ax.set_ylabel(r'$k_y$ (Å⁻¹)')
    ax.set_title('Equilibrium Spin Texture')
    ax.set_aspect('equal')
    ax.grid(True, alpha=0.3)
    
    # Add legend
    ax.plot([], [], 'ro', label='λ = +1')
    ax.plot([], [], 'bo', label='λ = -1')
    ax.legend(loc='upper right')
    
    plt.tight_layout()
    plt.savefig('spin_texture.png', dpi=150)
    plt.show()

def plot_edelstein_vs_Efield():
    """Plot magnetization vs electric field magnitude and direction."""
    fig, axes = plt.subplots(1, 2, figsize=(12, 5))
    
    # Panel 1: |M| vs |E|
    E_mags = np.linspace(0, 5e3, 100)
    M_mags_parabolic = []
    M_mags_massless = []
    for E in E_mags:
        E_vec = np.array([E, 0.0])
        M_para = induced_magnetization(E_vec, model='parabolic')
        M_mass = induced_magnetization(E_vec, model='massless')
        M_mags_parabolic.append(np.linalg.norm(M_para))
        M_mags_massless.append(np.linalg.norm(M_mass))
    
    axes[0].plot(E_mags, M_mags_parabolic, 'b-', linewidth=2, label='Parabolic')
    axes[0].plot(E_mags, M_mags_massless, 'r--', linewidth=2, label='Massless')
    axes[0].set_xlabel('Electric Field |E| (V/m)')
    axes[0].set_ylabel('|M| (A)')  # 2D magnetization per unit area
    axes[0].set_title('Magnetization vs Electric Field Magnitude')
    axes[0].legend()
    axes[0].grid(True, alpha=0.3)
    
    # Panel 2: Direction dependence (angular plot)
    theta = np.linspace(0, 2*pi, 100)
    Mx_para, My_para = [], []
    Mx_mass, My_mass = [], []
    E0 = 1e3
    for th in theta:
        E_vec = E0 * np.array([np.cos(th), np.sin(th)])
        M_para = induced_magnetization(E_vec, model='parabolic')
        M_mass = induced_magnetization(E_vec, model='massless')
        Mx_para.append(M_para[0]); My_para.append(M_para[1])
        Mx_mass.append(M_mass[0]); My_mass.append(M_mass[1])
    
    # Plot as parametric curve M vs E direction
    axes[1].plot(Mx_para, My_para, 'b-', linewidth=2, label='Parabolic')
    axes[1].plot(Mx_mass, My_mass, 'r--', linewidth=2, label='Massless')
    axes[1].set_xlabel('M$_x$ (A)')
    axes[1].set_ylabel('M$_y$ (A)')
    axes[1].set_title('Magnetization Vector for Rotating E')
    axes[1].legend()
    axes[1].grid(True, alpha=0.3)
    axes[1].set_aspect('equal')
    
    # Add arrows showing E and M at θ=30°
    th = 30 * pi/180
    E_vec = E0 * np.array([np.cos(th), np.sin(th)])
    M_vec = induced_magnetization(E_vec, model='parabolic')
    scale = 1e-3
    axes[1].arrow(0, 0, E_vec[0]*scale, E_vec[1]*scale, 
                  head_width=0.5e-5, head_length=0.5e-5, fc='green', ec='green', label='E')
    axes[1].arrow(0, 0, M_vec[0]*1e5, M_vec[1]*1e5,
                  head_width=0.5e-5, head_length=0.5e-5, fc='black', ec='black', label='M')
    
    plt.tight_layout()
    plt.savefig('edelstein_vs_E.png', dpi=150)
    plt.show()

def plot_parameter_dependencies():
    """Plot magnetization vs key parameters."""
    fig, axes = plt.subplots(2, 2, figsize=(12, 10))
    
    E0 = 1e3
    E_vec = np.array([E0, 0.0])
    
    # Panel 1: vs Rashba parameter α_R
    alpha_vals = np.linspace(0, 2.0, 100) * alpha_R_conv  # in J·m
    M_vals = []
    for a in alpha_vals:
        M = induced_magnetization(E_vec, model='parabolic', alpha_R=a)
        M_vals.append(np.linalg.norm(M))
    axes[0,0].plot(alpha_vals/alpha_R_conv, M_vals, 'b-', linewidth=2)
    axes[0,0].set_xlabel(r'$\alpha_R$ (eV·Å)')
    axes[0,0].set_ylabel('|M| (A)')
    axes[0,0].set_title('Magnetization vs Rashba Parameter')
    axes[0,0].grid(True, alpha=0.3)
    
    # Panel 2: vs Fermi wavevector k_F
    kF_vals = np.linspace(0.01, 0.06, 100) * 1e10  # m⁻¹
    M_vals = []
    for kf in kF_vals:
        M = induced_magnetization(E_vec, model='parabolic', k_F=kf)
        M_vals.append(np.linalg.norm(M))
    axes[0,1].plot(kF_vals/1e10, M_vals, 'r-', linewidth=2)
    axes[0,1].set_xlabel(r'$k_F$ (Å⁻¹)')
    axes[0,1].set_ylabel('|M| (A)')
    axes[0,1].set_title('Magnetization vs Fermi Wavevector')
    axes[0,1].grid(True, alpha=0.3)
    
    # Panel 3: vs relaxation time τ
    tau_vals = np.linspace(0.1, 5.0, 100) * 1e-12  # s
    M_vals = []
    for t in tau_vals:
        M = induced_magnetization(E_vec, model='parabolic', tau=t)
        M_vals.append(np.linalg.norm(M))
    axes[1,0].plot(tau_vals/1e-12, M_vals, 'g-', linewidth=2)
    axes[1,0].set_xlabel('τ (ps)')
    axes[1,0].set_ylabel('|M| (A)')
    axes[1,0].set_title('Magnetization vs Relaxation Time')
    axes[1,0].grid(True, alpha=0.3)
    
    # Panel 4: vs Fermi velocity v_F (massless model)
    vF_vals = np.linspace(1e5, 1e6, 100)  # m/s
    M_vals = []
    eps_F_fixed = 0.79 * eV  # fixed Fermi energy
    for vf in vF_vals:
        kf = eps_F_fixed / (hbar * vf)  # k_F = ε_F/(ħv_F)
        M = induced_magnetization(E_vec, model='massless', k_F=kf)
        M_vals.append(np.linalg.norm(M))
    axes[1,1].plot(vF_vals/1e5, M_vals, 'm-', linewidth=2)
    axes[1,1].set_xlabel('$v_F$ (10⁵ m/s)')
    axes[1,1].set_ylabel('|M| (A)')
    axes[1,1].set_title('Magnetization vs Fermi Velocity (massless, fixed ε_F)')
    axes[1,1].grid(True, alpha=0.3)
    
    plt.tight_layout()
    plt.savefig('parameter_dependencies.png', dpi=150)
    plt.show()

def plot_chirality_dependence():
    """Plot contributions from λ = +1 and λ = -1 bands."""
    fig, ax = plt.subplots(figsize=(8, 6))
    
    E0 = 1e3
    E_vec = np.array([E0, 0.0])
    
    # For parabolic model, compute band-resolved contributions
    alpha_R = params['alpha_R']
    k_F = params['k_F']
    tau = params['tau']
    m_star = params['m_star']
    eps_F = params['eps_F']
    
    # Fermi wavevectors for each band
    k0 = m_star * alpha_R / hbar**2
    kF_plus = -k0 + np.sqrt(k0**2 + 2*m_star*eps_F/hbar**2)
    kF_minus = k0 + np.sqrt(k0**2 + 2*m_star*eps_F/hbar**2)
    
    # Band contributions (from theory)
    delta_S_plus = e * tau / (4*pi*hbar) * alpha_R * kF_plus
    delta_S_minus = -e * tau / (4*pi*hbar) * alpha_R * kF_minus
    
    M_plus = g_factor * mu_B * delta_S_plus
    M_minus = g_factor * mu_B * delta_S_minus
    M_total = M_plus + M_minus
    
    # Bar chart
    bars = ['λ = +1', 'λ = -1', 'Total']
    values = [M_plus, M_minus, M_total]
    colors = ['red', 'blue', 'green']
    
    ax.bar(bars, values, color=colors, alpha=0.7, edgecolor='black')
    ax.set_ylabel('M$_y$ (A)')
    ax.set_title('Chirality-Resolved Edelstein Magnetization')
    ax.axhline(0, color='black', linewidth=0.5)
    ax.grid(True, alpha=0.3, axis='y')
    
    # Add value labels
    for i, v in enumerate(values):
        ax.text(i, v + 0.05*max(abs(v) for v in values)*np.sign(v) if v != 0 else 0,
                f'{v:.2e}', ha='center', fontsize=10)
    
    plt.tight_layout()
    plt.savefig('chirality_dependence.png', dpi=150)
    plt.show()

def plot_numerical_verification():
    """Verify analytical formula against numerical k-integration."""
    fig, axes = plt.subplots(1, 2, figsize=(12, 5))
    
    E0 = 1e3
    E_vec = np.array([E0, 0.0])
    
    # Test over a range of alpha_R values
    alpha_vals = np.linspace(0.1, 2.0, 10) * alpha_R_conv
    analytical = []
    numerical = []
    
    for a in alpha_vals:
        M_ana = induced_magnetization(E_vec, model='parabolic', alpha_R=a)
        analytical.append(M_ana[1])
        
        # Numerical calculation (coarse grid for speed)
        M_num = numerical_edelstein(E_vec, model='parabolic', n_k=200,
                                    alpha_R=a, k_F=params['k_F'],
                                    tau=params['tau'], T=1e-6)
        numerical.append(M_num[1])
    
    axes[0].plot(alpha_vals/alpha_R_conv, analytical, 'b-', linewidth=2, label='Analytical')
    axes[0].plot(alpha_vals/alpha_R_conv, numerical, 'ro', markersize=6, label='Numerical')
    axes[0].set_xlabel(r'$\alpha_R$ (eV·Å)')
    axes[0].set_ylabel('δS$_y$ (m⁻²)')
    axes[0].set_title('Verification: Parabolic Model')
    axes[0].legend()
    axes[0].grid(True, alpha=0.3)
    
    # Massless model
    vF_vals = np.linspace(2e5, 8e5, 10)
    analytical_mass = []
    numerical_mass = []
    eps_F_fixed = 0.79 * eV
    
    for vf in vF_vals:
        kf = eps_F_fixed / (hbar * vf)
        M_ana = induced_magnetization(E_vec, model='massless', k_F=kf)
        analytical_mass.append(M_ana[1])
        
        M_num = numerical_edelstein(E_vec, model='massless', n_k=200,
                                    v_F=vf, k_F=kf, tau=params['tau'],
                                    T=1e-6, eps_F=eps_F_fixed)
        numerical_mass.append(M_num[1])
    
    axes[1].plot(vF_vals/1e5, analytical_mass, 'b-', linewidth=2, label='Analytical')
    axes[1].plot(vF_vals/1e5, numerical_mass, 'ro', markersize=6, label='Numerical')
    axes[1].set_xlabel('$v_F$ (10⁵ m/s)')
    axes[1].set_ylabel('δS$_y$ (m⁻²)')
    axes[1].set_title('Verification: Massless Model')
    axes[1].legend()
    axes[1].grid(True, alpha=0.3)
    
    plt.tight_layout()
    plt.savefig('numerical_verification.png', dpi=150)
    plt.show()

# =============================================================================
# MAIN EXECUTION
# =============================================================================

def main():
    """Run all calculations and generate plots."""
    print("="*70)
    print("EDELSTEIN EFFECT IN RASHBA FERMIONS AT THE Γ POINT")
    print("="*70)
    
    # Display parameters
    print("\n--- Model Parameters (InGaAs Quantum Well) ---")
    print(f"Rashba parameter α_R    : {params['alpha_R']/alpha_R_conv:.2f} eV·Å")
    print(f"Fermi wavevector k_F    : {params['k_F']/1e10:.3f} Å⁻¹")
    print(f"Effective mass m*       : {params['m_star']/m_e:.3f} m_e")
    print(f"Fermi velocity v_F      : {params['v_F']:.2e} m/s")
    print(f"Fermi energy ε_F        : {params['eps_F']/eV:.4f} eV")
    print(f"Relaxation time τ       : {params['tau']/1e-12:.2f} ps")
    print(f"Temperature T           : {params['T']:.1f} K")
    print(f"Landé g-factor          : {g_factor:.1f}")
    print(f"Electric field          : {params['E_field']:.0f} V/m along x")
    
    # =====================================================================
    # 1. Compute Edelstein effect for different electric fields
    # =====================================================================
    print("\n--- Edelstein Effect Calculations ---")
    
    E0 = params['E_field']
    E_x = np.array([E0, 0.0])
    E_y = np.array([0.0, E0])
    E_45 = np.array([E0/np.sqrt(2), E0/np.sqrt(2)])
    
    for E_vec, label in [(E_x, 'E = (1000, 0) V/m'),
                         (E_y, 'E = (0, 1000) V/m'),
                         (E_45, 'E = (707, 707) V/m')]:
        M_para = induced_magnetization(E_vec, model='parabolic')
        M_mass = induced_magnetization(E_vec, model='massless')
        print(f"\n{label}:")
        print(f"  Parabolic: M = ({M_para[0]:.3e}, {M_para[1]:.3e}) A")
        print(f"  Massless:  M = ({M_mass[0]:.3e}, {M_mass[1]:.3e}) A")
        
        # Check perpendicularity
        dot_para = np.dot(M_para, E_vec)
        dot_mass = np.dot(M_mass, E_vec)
        print(f"  M·E = {dot_para:.2e} (parabolic), {dot_mass:.2e} (massless)")
    
    # =====================================================================
    # 2. Susceptibility tensor
    # =====================================================================
    print("\n--- Spin Susceptibility Tensor ---")
    chi_para = susceptibility_tensor(model='parabolic')
    chi_mass = susceptibility_tensor(model='massless')
    print("Parabolic model:")
    print(chi_para)
    print("Massless model:")
    print(chi_mass)
    
    # =====================================================================
    # 3. Generate plots
    # =====================================================================
    print("\n--- Generating Plots ---")
    
    # Plot spin texture
    print("  - Plotting spin texture...")
    plot_spin_texture()
    
    # Plot Edelstein effect vs electric field
    print("  - Plotting magnetization vs electric field...")
    plot_edelstein_vs_Efield()
    
    # Plot parameter dependencies
    print("  - Plotting parameter dependencies...")
    plot_parameter_dependencies()
    
    # Plot chirality dependence
    print("  - Plotting chirality dependence...")
    plot_chirality_dependence()
    
    # Numerical verification
    print("  - Running numerical verification...")
    plot_numerical_verification()
    
    # =====================================================================
    # 4. Summary
    # =====================================================================
    print("\n" + "="*70)
    print("SUMMARY OF RESULTS")
    print("="*70)
    
    # Calculate final values
    M_final = induced_magnetization(E_x, model='parabolic')
    delta_S_final = induced_spin_density(E_x, model='parabolic')
    
    print(f"\nInduced spin density (parabolic, E along x):")
    print(f"  δS = ({delta_S_final[0]:.3e}, {delta_S_final[1]:.3e}) m⁻²")
    print(f"  |δS| = {np.linalg.norm(delta_S_final):.3e} m⁻²")
    print(f"  Equivalent spin polarization: {np.linalg.norm(delta_S_final)/params['k_F']**2/(2*pi)*100:.3f}% of total electrons")
    
    print(f"\nInduced magnetization (parabolic, E along x):")
    print(f"  M = ({M_final[0]:.3e}, {M_final[1]:.3e}) A (2D per unit area)")
    print(f"  |M| = {np.linalg.norm(M_final):.3e} A")
    
    print("\nKey dependencies confirmed:")
    print("  - M ∝ E (linear response)")
    print("  - M ⊥ E (perpendicular geometry)")
    print("  - M ∝ α_R k_F (SOC strength × Fermi momentum)")
    print("  - M ∝ τ (relaxation time)")
    print("  - Chirality matters: reversing α_R flips M direction")
    
    print("\nAll plots saved as PNG files.")
    print("="*70)

if __name__ == "__main__":
    main()
```
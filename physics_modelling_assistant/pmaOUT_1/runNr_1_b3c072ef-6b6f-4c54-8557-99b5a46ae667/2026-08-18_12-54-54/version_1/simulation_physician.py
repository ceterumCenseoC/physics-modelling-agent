```python
#!/usr/bin/env python3
"""
Corrected Edelstein Effect for a Rashba Fermion at the Gamma Point
====================================================================
Implements the corrected model (with proper units and factors of hbar)
for the linear and nonlinear Edelstein effect in an isotropic Rashba
2DEG, plus the anisotropic Rashba model.

Formulas implemented (CORRECTED):
  HDR:  M = (mu_B |e| tau / (2 pi hbar)) * m * alpha * (z_hat x E)
  LDR:  M = (mu_B |e| tau / (2 pi hbar)) * sqrt(m^2 alpha^2 + 2m E_F)
            * (z_hat x E)
  Anisotropic (mass ratio r_m = m_y/m_x):
        chi_xy / chi_0 = 4 pi m_x alpha r_m / (1 + sqrt(r_m))
  Anisotropic (SOC ratio r_alpha = alpha_y/alpha_x):
        chi_xy / chi_0 = 4 pi m alpha_x r_alpha / (1 + r_alpha)

Nonlinear clean-limit model (Vignale-Tokatly):
  gamma = e E L_s / E_F,  L_s = hbar / (2 m alpha)
  S_y(t)/S_max = (1/(2*pi)) * integral over theta of
       [cos(theta) - sqrt(gamma)*tau_dim] / sqrt(1 + gamma*tau_dim^2
        - 2 sqrt(gamma) tau_dim cos(theta))
       * (1 - exp(-pi sin^2(theta)/gamma))
  with tau_dim = alpha * p_F * sqrt(gamma) * t / hbar

All units are SI (magnetization in A, i.e., 2D spin density).
"""

import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import quad

# ----------------------------------------------------------------------
# Physical constants (exact SI values)
# ----------------------------------------------------------------------
hbar = 1.054571817e-34      # J·s
e_charge = 1.602176634e-19  # C
mu_B = 9.2740100783e-24     # J/T
m_e = 9.1093837015e-31      # kg
pi = np.pi

# ----------------------------------------------------------------------
# Helper: convert eV·Å to m/s for alpha
# ----------------------------------------------------------------------
def alpha_eV_A_to_m_per_s(alpha_eV_A):
    """Convert Rashba parameter from eV·Å to m/s (velocity units)."""
    # 1 eV = e_charge J, 1 Å = 1e-10 m
    # [alpha] = eV·Å = (e_charge J) * (1e-10 m) = e_charge*1e-10 J·m
    # For H_R = alpha * p * sigma, [alpha] = m/s
    # So alpha_m/s = alpha_eV_A * (e_charge * 1e-10) / hbar
    return alpha_eV_A * e_charge * 1e-10 / hbar

# ----------------------------------------------------------------------
# Linear Edelstein effect: isotropic Rashba model
# ----------------------------------------------------------------------
def edelstein_magnetization_linear(alpha_m_s, m_star, E_F, tau, E_field, hbar=hbar):
    """
    Compute 2D magnetization (spin density in A) for linear Edelstein effect.
    
    Parameters:
    -----------
    alpha_m_s : float - Rashba coupling in m/s
    m_star    : float - effective mass in kg
    E_F       : float - Fermi energy in J
    tau       : float - transport relaxation time in s
    E_field   : float - electric field magnitude in V/m (along x)
    hbar      : float - reduced Planck constant
    
    Returns:
    --------
    M_y : float - magnetization along y in A (2D areal magnetization)
    """
    # High-Density Regime check
    E_cross = -m_star * alpha_m_s**2 / (2 * hbar**2)  # J
    
    if E_F > E_cross:
        # HDR: magnetization independent of E_F
        M_y = (mu_B * e_charge * tau / (2 * pi * hbar)) * m_star * alpha_m_s * E_field
    else:
        # LDR: only lower band occupied
        M_y = (mu_B * e_charge * tau / (2 * pi * hbar)) * np.sqrt(
            m_star**2 * alpha_m_s**2 + 2 * m_star * E_F
        ) * E_field
    
    return M_y

def edelstein_susceptibility_linear(alpha_m_s, m_star, E_F, tau):
    """
    Linear Edelstein susceptibility chi_xy in A·m/V.
    """
    E_cross = -m_star * alpha_m_s**2 / (2 * hbar**2)
    if E_F > E_cross:
        return (mu_B * e_charge * tau / (2 * pi * hbar)) * m_star * alpha_m_s
    else:
        return (mu_B * e_charge * tau / (2 * pi * hbar)) * np.sqrt(
            m_star**2 * alpha_m_s**2 + 2 * m_star * E_F
        )

def magnetization_for_arbitrary_E(alpha_m_s, m_star, E_F, tau, E_vector):
    """
    Return magnetization vector M = (Mx, My) for arbitrary in-plane E.
    M = chi * (0 -1; 1 0) * E  =>  M = chi * (-Ey, Ex)
    """
    chi = edelstein_susceptibility_linear(alpha_m_s, m_star, E_F, tau)
    Ex, Ey = E_vector[0], E_vector[1]
    Mx = -chi * Ey
    My = chi * Ex
    return np.array([Mx, My])

# ----------------------------------------------------------------------
# Nonlinear clean-limit Edelstein effect (Vignale-Tokatly)
# ----------------------------------------------------------------------
def nonlinear_spin_polarization(gamma, tau_dim):
    """
    Compute normalized spin polarization S_y(t)/S_max for given gamma
    and dimensionless time tau_dim = alpha p_F sqrt(gamma) t / hbar.
    
    S_max = alpha * n / v_F  (max saturation in adiabatic limit)
    
    Formula:
    S_y(t)/S_max = (1/(2*pi)) * ∫₀^{2π} dθ 
        [cosθ - sqrt(γ)τ] / sqrt(1 + γτ² - 2√γ τ cosθ)
        * (1 - exp(-π sin²θ / γ))
    """
    integrand = lambda theta: (
        (np.cos(theta) - np.sqrt(gamma)*tau_dim)
        / np.sqrt(1 + gamma*tau_dim**2 - 2*np.sqrt(gamma)*tau_dim*np.cos(theta))
        * (1 - np.exp(-pi * np.sin(theta)**2 / gamma))
    )
    result, _ = quad(integrand, 0, 2*pi, limit=500)
    return result / (2*pi)

def nonlinear_long_time_limit(gamma):
    """
    Long-time limit of normalized spin polarization S_y(∞)/S_max.
    For gamma -> 0, this approaches -1/2 (full saturation).
    For gamma -> ∞, approaches cos(theta_p) averaged (which is 0 for isotropic).
    We compute the asymptotic limit by taking tau_dim very large.
    """
    # At large tau, the integrand approaches:
    # (cosθ - √γτ)/|√γ τ| * (1 - e^{-π sin²θ/γ})
    # ≈ (cosθ/√γτ - 1) * (1 - e^{-π sin²θ/γ}) → -(1 - e^{-π sin²θ/γ})
    integrand_inf = lambda theta: -(1 - np.exp(-pi * np.sin(theta)**2 / gamma))
    result, _ = quad(integrand_inf, 0, 2*pi, limit=500)
    return result / (2*pi)

# ----------------------------------------------------------------------
# Anisotropic Rashba model (C2v symmetry)
# ----------------------------------------------------------------------
def anisotropic_susceptibility_mass(r_m, m_x, alpha, chi0_norm=1.0):
    """
    Susceptibility for mass anisotropy: chi_xy/chi_0 = 4π m_x α r_m/(1+√r_m)
    Returns normalized by chi_0.
    """
    return 4 * pi * m_x * alpha * r_m / (1 + np.sqrt(r_m))

def anisotropic_susceptibility_soc(r_alpha, m, alpha_x, chi0_norm=1.0):
    """
    Susceptibility for SOC anisotropy: chi_xy/chi_0 = 4π m α_x r_α/(1+r_α)
    Returns normalized by chi_0.
    """
    return 4 * pi * m * alpha_x * r_alpha / (1 + r_alpha)

# ----------------------------------------------------------------------
# Numerical validation: direct integration of Boltzmann formula
# ----------------------------------------------------------------------
def edelstein_numerical(alpha_m_s, m_star, E_F, tau, E_field, kmax_factor=4.0,
                        Nk=2000, Ntheta=2000, broadening=0.5e-3*e_charge):
    """
    Numerically integrate the Boltzmann Edelstein formula with Lorentzian
    delta function. Returns M_y in A.
    
    chi_xy = -(tau e mu_B / (4π² hbar)) Σ_ν ∫ d²k ⟨σ_y⟩_ν δ(E_ν-μ) v_x^ν
    """
    # Momentum offset
    k0 = m_star * alpha_m_s / hbar  # m⁻¹
    
    # Fermi momenta
    kmax = kmax_factor * (k0 + np.sqrt(k0**2 + 2*m_star*E_F/hbar**2))
    
    # Grids
    k = np.linspace(0.001*kmax, kmax, Nk)
    theta = np.linspace(0, 2*pi, Ntheta)
    K, TH = np.meshgrid(k, theta, indexing='ij')
    
    # Band energies
    E_plus = hbar**2 * K**2 / (2*m_star) + alpha_m_s * hbar * K
    E_minus = hbar**2 * K**2 / (2*m_star) - alpha_m_s * hbar * K
    
    # Group velocities along x
    vx_plus = hbar**2 * K * np.cos(TH) / m_star + alpha_m_s * np.cos(TH)
    vx_minus = hbar**2 * K * np.cos(TH) / m_star - alpha_m_s * np.cos(TH)
    
    # Spin expectation values ⟨σ_y⟩
    sy_plus = -np.cos(TH)
    sy_minus = np.cos(TH)
    
    # Lorentzian delta functions
    delta_plus = (broadening/pi) / ((E_plus - E_F)**2 + broadening**2)
    delta_minus = (broadening/pi) / ((E_minus - E_F)**2 + broadening**2)
    
    # Integrand: k * ⟨σ_y⟩ * v_x * delta(E - E_F)
    integrand_plus = K * sy_plus * vx_plus * delta_plus
    integrand_minus = K * sy_minus * vx_minus * delta_minus
    
    # Sum over bands and integrate
    dk = k[1] - k[0]
    dtheta = theta[1] - theta[0]
    
    integral = np.sum(integrand_plus + integrand_minus) * dk * dtheta
    
    # Edelstein susceptibility
    chi_xy = -(tau * e_charge * mu_B / (4*pi**2 * hbar)) * integral
    
    # Magnetization
    M_y = chi_xy * E_field
    return M_y

# ======================================================================
# MAIN SCRIPT: Generate all required graphics
# ======================================================================
def main():
    print("="*70)
    print("CORRECTED EDELSTEIN EFFECT IN RASHBA FERMION")
    print("="*70)
    
    # ------------------------------------------------------------------
    # Default parameters (InGaAs quantum well)
    # ------------------------------------------------------------------
    alpha_eV_A = 0.25                      # eV·Å
    alpha_m_s = alpha_eV_A_to_m_per_s(alpha_eV_A)
    m_star = 0.05 * m_e                    # kg
    E_F = 0.075 * e_charge                 # J (75 meV)
    tau = 5e-12                            # s
    E_field = 1e4                          # V/m (linear regime)
    
    print(f"\nDefault parameters (InGaAs 2DEG):")
    print(f"  alpha = {alpha_eV_A} eV·Å = {alpha_m_s:.3e} m/s")
    print(f"  m* = {m_star/m_e:.3f} m_e = {m_star:.3e} kg")
    print(f"  E_F = {E_F/e_charge*1000:.1f} meV")
    print(f"  tau = {tau*1e12:.2f} ps")
    print(f"  E = {E_field/100:.1f} V/cm")
    
    # Derived quantities
    k0 = m_star * alpha_m_s / hbar
    L_s = hbar / (2 * m_star * alpha_m_s)
    gamma_lin = e_charge * E_field * L_s / E_F
    print(f"\nDerived:")
    print(f"  k0 = {k0:.3e} m⁻¹ = {k0*1e-10:.3f} Å⁻¹")
    print(f"  L_s = {L_s*1e9:.2f} nm")
    print(f"  gamma (linear regime) = {gamma_lin:.3e}")
    
    # ------------------------------------------------------------------
    # 1. Magnetization vs Electric Field (Linear regime)
    # ------------------------------------------------------------------
    E_values = np.linspace(0, 5e4, 100)  # V/m
    M_y_lin = [edelstein_magnetization_linear(alpha_m_s, m_star, E_F, tau, E) 
               for E in E_values]
    
    fig1, ax1 = plt.subplots(figsize=(8, 6))
    ax1.plot(E_values/100, np.array(M_y_lin)*1e9, 'b-', linewidth=2)
    ax1.set_xlabel('Electric Field $E_x$ (V/cm)', fontsize=14)
    ax1.set_ylabel('$M_y$ (nA)', fontsize=14)
    ax1.set_title('Linear Edelstein Effect: $M_y$ vs $E_x$', fontsize=16)
    ax1.grid(True, alpha=0.3)
    ax1.tick_params(labelsize=12)
    plt.tight_layout()
    plt.savefig('edelstein_linear_My_vs_E.png', dpi=150)
    plt.show()
    
    # ------------------------------------------------------------------
    # 2. Magnetization vs Electric Field direction (vector plot)
    # ------------------------------------------------------------------
    phi_values = np.linspace(0, 2*pi, 20)
    E_mag = 1e4  # V/m
    Mx_list = []
    My_list = []
    for phi in phi_values:
        E_vec = E_mag * np.array([np.cos(phi), np.sin(phi)])
        M_vec = magnetization_for_arbitrary_E(alpha_m_s, m_star, E_F, tau, E_vec)
        Mx_list.append(M_vec[0])
        My_list.append(M_vec[1])
    
    fig2, ax2 = plt.subplots(figsize=(8, 8))
    # Plot E vectors (blue) and M vectors (red)
    for phi, Mx, My in zip(phi_values, Mx_list, My_list):
        Ex = E_mag * np.cos(phi)
        Ey = E_mag * np.sin(phi)
        ax2.quiver(0, 0, Ex, Ey, color='blue', angles='xy', scale_units='xy', 
                   scale=1, alpha=0.6, label='E' if phi==0 else "")
        ax2.quiver(0, 0, Mx*1e12, My*1e12, color='red', angles='xy', 
                   scale_units='xy', scale=1, alpha=0.6, label='M' if phi==0 else "")
    
    ax2.set_xlabel('$E_x$ (V/m) / $M_x$ (arb. units)', fontsize=14)
    ax2.set_ylabel('$E_y$ (V/m) / $M_y$ (arb. units)', fontsize=14)
    ax2.set_title('Edelstein Effect: $\\mathbf{M} \\perp \\mathbf{E}$', fontsize=16)
    ax2.legend(['$\\mathbf{E}$', '$\\mathbf{M}$'], fontsize=12)
    ax2.grid(True, alpha=0.3)
    ax2.axhline(0, color='black', linewidth=0.5)
    ax2.axvline(0, color='black', linewidth=0.5)
    ax2.set_aspect('equal')
    plt.tight_layout()
    plt.savefig('edelstein_vector_field.png', dpi=150)
    plt.show()
    
    # ------------------------------------------------------------------
    # 3. Magnetization vs Rashba coupling alpha
    # ------------------------------------------------------------------
    alpha_values_eV_A = np.linspace(0.01, 0.5, 50)
    M_y_alpha = []
    for alpha_ev in alpha_values_eV_A:
        alpha_ms = alpha_eV_A_to_m_per_s(alpha_ev)
        M_y_alpha.append(edelstein_magnetization_linear(alpha_ms, m_star, E_F, tau, E_field))
    
    fig3, ax3 = plt.subplots(figsize=(8, 6))
    ax3.plot(alpha_values_eV_A, np.array(M_y_alpha)*1e9, 'r-', linewidth=2)
    ax3.set_xlabel('Rashba coupling $\\alpha$ (eV·Å)', fontsize=14)
    ax3.set_ylabel('$M_y$ (nA)', fontsize=14)
    ax3.set_title('Edelstein Effect: $M_y$ vs $\\alpha$ (HDR)', fontsize=16)
    ax3.grid(True, alpha=0.3)
    ax3.tick_params(labelsize=12)
    plt.tight_layout()
    plt.savefig('edelstein_My_vs_alpha.png', dpi=150)
    plt.show()
    
    # ------------------------------------------------------------------
    # 4. Susceptibility vs Fermi energy (HDR plateau / LDR rise)
    # ------------------------------------------------------------------
    E_F_values = np.linspace(0.001, 0.15, 200) * e_charge  # J
    chi_values = [edelstein_susceptibility_linear(alpha_m_s, m_star, E_Fv, tau) 
                  for E_Fv in E_F_values]
    
    # Normalize by chi at large E_F
    chi_max = chi_values[-1]
    
    fig4, ax4 = plt.subplots(figsize=(8, 6))
    ax4.plot(E_F_values/e_charge*1000, np.array(chi_values)/chi_max, 'g-', linewidth=2)
    ax4.set_xlabel('Fermi Energy $E_F$ (meV)', fontsize=14)
    ax4.set_ylabel('$\\chi_{xy} / \\chi_{xy}^{max}$', fontsize=14)
    ax4.set_title('Edelstein Susceptibility vs $E_F$', fontsize=16)
    ax4.grid(True, alpha=0.3)
    ax4.tick_params(labelsize=12)
    # Mark the band crossing
    E_cross = -m_star * alpha_m_s**2 / (2*hbar**2) / e_charge * 1000  # meV
    ax4.axvline(E_cross, color='black', linestyle='--', linewidth=1.5, 
                label=f'$E_{{cross}}$ = {E_cross:.4f} meV')
    ax4.legend(fontsize=12)
    plt.tight_layout()
    plt.savefig('edelstein_chi_vs_EF.png', dpi=150)
    plt.show()
    
    # ------------------------------------------------------------------
    # 5. Anisotropic susceptibility: mass ratio and SOC ratio
    # ------------------------------------------------------------------
    r_m_values = np.linspace(0.1, 5, 100)
    r_alpha_values = np.linspace(0.1, 5, 100)
    
    # Normalize to isotropic (r=1)
    chi_m_iso = anisotropic_susceptibility_mass(1.0, m_star, alpha_m_s)
    chi_a_iso = anisotropic_susceptibility_soc(1.0, m_star, alpha_m_s)
    
    chi_m = [anisotropic_susceptibility_mass(rm, m_star, alpha_m_s)/chi_m_iso 
             for rm in r_m_values]
    chi_a = [anisotropic_susceptibility_soc(ra, m_star, alpha_m_s)/chi_a_iso 
             for ra in r_alpha_values]
    
    fig5, (ax5a, ax5b) = plt.subplots(1, 2, figsize=(14, 6))
    
    ax5a.plot(r_m_values, chi_m, 'b-', linewidth=2)
    ax5a.set_xlabel('Mass anisotropy ratio $r_m = m_y/m_x$', fontsize=14)
    ax5a.set_ylabel('$\\chi_{xy}/\\chi_{xy}(r_m=1)$', fontsize=14)
    ax5a.set_title('Effect of Mass Anisotropy', fontsize=14)
    ax5a.grid(True, alpha=0.3)
    ax5a.tick_params(labelsize=12)
    ax5a.axhline(1, color='gray', linestyle='--')
    
    ax5b.plot(r_alpha_values, chi_a, 'r-', linewidth=2)
    ax5b.set_xlabel('SOC anisotropy ratio $r_\\alpha = \\alpha_y/\\alpha_x$', fontsize=14)
    ax5b.set_ylabel('$\\chi_{xy}/\\chi_{xy}(r_\\alpha=1)$', fontsize=14)
    ax5b.set_title('Effect of SOC Anisotropy', fontsize=14)
    ax5b.grid(True, alpha=0.3)
    ax5b.tick_params(labelsize=12)
    ax5b.axhline(1, color='gray', linestyle='--')
    
    plt.tight_layout()
    plt.savefig('edelstein_anisotropy.png', dpi=150)
    plt.show()
    
    # ------------------------------------------------------------------
    # 6. Nonlinear regime: S_y(t) vs dimensionless time for various gamma
    # ------------------------------------------------------------------
    gamma_values = [0.1, 1.0, 10.0]
    tau_dim_values = np.linspace(0, 10, 300)
    
    fig6, ax6 = plt.subplots(figsize=(10, 7))
    for gamma in gamma_values:
        Sy_t = [nonlinear_spin_polarization(gamma, tau_d) for tau_d in tau_dim_values]
        ax6.plot(tau_dim_values, Sy_t, linewidth=2, label=f'$\\gamma$ = {gamma}')
    
    # Add long-time limits
    for gamma in gamma_values:
        limit = nonlinear_long_time_limit(gamma)
        ax6.axhline(limit, color='gray', linestyle='--', linewidth=1)
        ax6.text(0.5, limit-0.03, f'$\\gamma$={gamma}: {limit:.3f}', fontsize=10)
    
    ax6.set_xlabel('Dimensionless time $\\tau = \\alpha p_F \\sqrt{\\gamma}\\, t / \\hbar$', fontsize=14)
    ax6.set_ylabel('$S_y(t)/S_{max}$', fontsize=14)
    ax6.set_title('Nonlinear Edelstein Effect: Time Evolution', fontsize=16)
    ax6.legend(fontsize=12)
    ax6.grid(True, alpha=0.3)
    ax6.tick_params(labelsize=12)
    plt.tight_layout()
    plt.savefig('edelstein_nonlinear_time.png', dpi=150)
    plt.show()
    
    # ------------------------------------------------------------------
    # 7. Nonlinear regime: Long-time limit vs gamma
    # ------------------------------------------------------------------
    gamma_sweep = np.logspace(-2, 2, 100)
    limits = [nonlinear_long_time_limit(g) for g in gamma_sweep]
    
    fig7, ax7 = plt.subplots(figsize=(8, 6))
    ax7.semilogx(gamma_sweep, limits, 'b-', linewidth=2)
    ax7.set_xlabel('Nonlinearity parameter $\\gamma$', fontsize=14)
    ax7.set_ylabel('$S_y(\\infty)/S_{max}$', fontsize=14)
    ax7.set_title('Long-Time Saturation vs $\\gamma$', fontsize=16)
    ax7.grid(True, alpha=0.3, which='both')
    ax7.tick_params(labelsize=12)
    # Reference values from theory
    ref_gamma = [0.1, 1, 10]
    ref_limits = [-0.449, -0.287, -0.098]
    ax7.plot(ref_gamma, ref_limits, 'ro', markersize=8, label='Theory (Vignale-Tokatly)')
    ax7.legend(fontsize=12)
    plt.tight_layout()
    plt.savefig('edelstein_nonlinear_saturation.png', dpi=150)
    plt.show()
    
    # ------------------------------------------------------------------
    # 8. Numerical validation vs analytical formula
    # ------------------------------------------------------------------
    print("\n" + "="*70)
    print("NUMERICAL VALIDATION (Boltzmann integration vs analytical)")
    print("="*70)
    
    # Test with coarser grid for speed
    Nk_test = 500
    Ntheta_test = 500
    broadening_test = 1e-3 * e_charge  # 1 meV
    
    E_test_values = [1e3, 5e3, 1e4]
    for E_test in E_test_values:
        M_analytical = edelstein_magnetization_linear(alpha_m_s, m_star, E_F, tau, E_test)
        M_numerical = edelstein_numerical(alpha_m_s, m_star, E_F, tau, E_test,
                                          Nk=Nk_test, Ntheta=Ntheta_test,
                                          broadening=broadening_test)
        print(f"  E = {E_test:.1e} V/m:")
        print(f"    Analytical: {M_analytical*1e9:.4f} nA")
        print(f"    Numerical:  {M_numerical*1e9:.4f} nA")
        print(f"    Relative error: {abs(M_numerical-M_analytical)/abs(M_analytical)*100:.2f}%")
    
    # ------------------------------------------------------------------
    # Summary printout
    # ------------------------------------------------------------------
    print("\n" + "="*70)
    print("SUMMARY OF RESULTS")
    print("="*70)
    M_y_default = edelstein_magnetization_linear(alpha_m_s, m_star, E_F, tau, E_field)
    print(f"Default linear Edelstein magnetization:")
    print(f"  M_y = {M_y_default*1e9:.4f} nA for E_x = {E_field/100:.0f} V/cm")
    print(f"  Spin density S_y = M_y/mu_B = {M_y_default/mu_B:.3e} m⁻²")
    print(f"  Susceptibility chi_xy = {edelstein_susceptibility_linear(alpha_m_s, m_star, E_F, tau):.3e} A·m/V")
    
    # Nonlinear saturation values
    print(f"\nNonlinear long-time limits (normalized):")
    for gamma in [0.1, 1, 10]:
        lim = nonlinear_long_time_limit(gamma)
        print(f"  gamma = {gamma}: S_y(inf)/S_max = {lim:.4f}")
    
    print("\nAll graphics saved as PNG files.")
    print("="*70)

if __name__ == "__main__":
    main()
```
```python
"""
Edelstein Effect for Rashba Fermions
====================================
This module implements the Edelstein effect (current-induced spin polarization)
for a 2D Rashba spin-orbit coupled electron gas at the Gamma point.

The model Hamiltonian is:
    H(k) = (hbar^2 k^2)/(2m*) + alpha_R * (sigma_x * k_y - sigma_y * k_x)

The induced magnetization due to an electric field E is:
    delta_M = (g * mu_B * e * tau * m* * alpha_R) / (2*pi*hbar^3) * (z_hat x E)

All calculations are done in natural units where hbar = e = mu_B = tau = 1.
"""

import numpy as np
import matplotlib.pyplot as plt
from scipy import constants as const

# ============================================================
# Natural units: hbar = 1, e = 1, mu_B = 1, tau = 1
# ============================================================
HBAR = 1.0
E_CHARGE = 1.0
MU_B = 1.0
TAU = 1.0
G_FACTOR = 2.0

# Pauli matrices
SIGMA_X = np.array([[0, 1], [1, 0]], dtype=complex)
SIGMA_Y = np.array([[0, -1j], [1j, 0]], dtype=complex)
SIGMA_Z = np.array([[1, 0], [0, -1]], dtype=complex)


def rashba_hamiltonian(kx, ky, alpha, m_star=1.0, chi=1.0):
    """
    Rashba Hamiltonian matrix for given wavevector components.
    
    Parameters:
    -----------
    kx, ky : float
        Wavevector components (in units of inverse length)
    alpha : float
        Rashba spin-orbit coupling strength (eV·Å in natural units)
    m_star : float
        Effective mass (in units of electron mass)
    chi : int (+1 or -1)
        Chirality of the Rashba coupling
    
    Returns:
    --------
    2x2 complex numpy array
    """
    k2 = kx**2 + ky**2
    kinetic = (HBAR**2 * k2) / (2 * m_star) * np.eye(2)
    spin_orbit = chi * alpha * (SIGMA_X * ky - SIGMA_Y * kx)
    return kinetic + spin_orbit


def band_energies_and_states(kx, ky, alpha, m_star=1.0, chi=1.0):
    """
    Compute eigenvalues and eigenvectors of the Rashba Hamiltonian.
    
    Returns:
    --------
    energies : array of shape (2,)
    states : array of shape (2, 2) - columns are eigenvectors
    """
    H = rashba_hamiltonian(kx, ky, alpha, m_star, chi)
    energies, states = np.linalg.eigh(H)
    return energies, states


def band_velocities(kx, ky, alpha, m_star=1.0, chi=1.0):
    """
    Compute band velocities v_n = (1/hbar) * dE_n/dk.
    
    Returns:
    --------
    velocities : array of shape (2, 2) - [band, component]
    """
    # Numerical derivative for simplicity
    dk = 1e-6
    energies, _ = band_energies_and_states(kx, ky, alpha, m_star, chi)
    
    # dE/dkx
    energies_x, _ = band_energies_and_states(kx + dk, ky, alpha, m_star, chi)
    vx = (energies_x - energies) / dk / HBAR
    
    # dE/dky
    energies_y, _ = band_energies_and_states(kx, ky + dk, alpha, m_star, chi)
    vy = (energies_y - energies) / dk / HBAR
    
    return np.column_stack([vx, vy])


def fermi_distribution_derivative(energy, mu, temperature=0.0):
    """
    Derivative of Fermi-Dirac distribution with respect to energy.
    At zero temperature, this is -delta(E - mu).
    
    Parameters:
    -----------
    energy : float
        Energy in eV
    mu : float
        Chemical potential in eV
    temperature : float
        Temperature in K (0 for zero temperature)
    
    Returns:
    --------
    float : d(f0)/dE
    """
    if temperature == 0.0:
        # Delta function approximation using a Gaussian
        width = 1e-4  # eV - small broadening for numerical stability
        return -np.exp(-((energy - mu)**2) / (2 * width**2)) / (width * np.sqrt(2 * np.pi))
    else:
        kBT = const.k_B * temperature / const.e  # Convert to eV
        x = (energy - mu) / kBT
        return -np.exp(x) / (kBT * (1 + np.exp(x))**2)


def equilibrium_density_matrix(kx, ky, alpha, mu, m_star=1.0, chi=1.0):
    """
    Compute equilibrium density matrix rho_0 = sum_n f(E_n) |u_n><u_n|.
    
    Returns:
    --------
    2x2 complex numpy array
    """
    energies, states = band_energies_and_states(kx, ky, alpha, m_star, chi)
    rho = np.zeros((2, 2), dtype=complex)
    
    for n in range(2):
        f = 1.0 if energies[n] <= mu else 0.0  # Zero temperature occupation
        psi = states[:, n]
        rho += f * np.outer(psi, np.conj(psi))
    
    return rho


def density_matrix_correction(kx, ky, alpha, mu, E_field, m_star=1.0, chi=1.0):
    """
    Compute non-equilibrium density matrix correction due to electric field.
    
    delta_rho = sum_n delta_f_n |u_n><u_n|
    where delta_f_n = e*tau*E·v_n * (-df/dE_n)
    
    Parameters:
    -----------
    E_field : array of shape (2,)
        Electric field vector [Ex, Ey]
    
    Returns:
    --------
    2x2 complex numpy array
    """
    energies, states = band_energies_and_states(kx, ky, alpha, m_star, chi)
    velocities = band_velocities(kx, ky, alpha, m_star, chi)
    
    delta_rho = np.zeros((2, 2), dtype=complex)
    
    for n in range(2):
        # delta_f = e*tau*E·v * (-df/dE)
        E_dot_v = E_field[0] * velocities[n, 0] + E_field[1] * velocities[n, 1]
        delta_f = E_CHARGE * TAU * E_dot_v * fermi_distribution_derivative(energies[n], mu)
        
        psi = states[:, n]
        delta_rho += delta_f * np.outer(psi, np.conj(psi))
    
    return delta_rho


def full_density_matrix(kx, ky, alpha, mu, E_field, m_star=1.0, chi=1.0):
    """
    Compute full density matrix rho = rho_0 + delta_rho.
    """
    rho_0 = equilibrium_density_matrix(kx, ky, alpha, mu, m_star, chi)
    delta_rho = density_matrix_correction(kx, ky, alpha, mu, E_field, m_star, chi)
    return rho_0 + delta_rho


def spin_operator():
    """
    Spin operator S = hbar * sigma / 2.
    Returns 3-component list of 2x2 matrices.
    """
    return [HBAR / 2 * SIGMA_X, HBAR / 2 * SIGMA_Y, HBAR / 2 * SIGMA_Z]


def spin_expectation(rho):
    """
    Compute spin expectation value <S> = Tr(rho * S).
    
    Returns:
    --------
    array of shape (3,) - [Sx, Sy, Sz]
    """
    S_ops = spin_operator()
    result = np.zeros(3)
    for i, S in enumerate(S_ops):
        result[i] = np.real(np.trace(rho @ S))
    return result


def compute_magnetization(alpha, mu, E_field, m_star=1.0, chi=1.0, 
                          k_max=0.5, n_grid=200):
    """
    Compute the total magnetization by integrating over k-space.
    
    M = (g*mu_B/hbar) * integral(d^2k/(2*pi)^2 * Tr(delta_rho * S))
    
    Parameters:
    -----------
    alpha : float
        Rashba coupling strength
    mu : float
        Chemical potential
    E_field : array of shape (2,)
        Electric field vector
    m_star : float
        Effective mass
    chi : int
        Chirality (+1 or -1)
    k_max : float
        Maximum k for integration grid
    n_grid : int
        Number of grid points in each direction
    
    Returns:
    --------
    array of shape (3,) - magnetization [Mx, My, Mz]
    """
    # Create 2D grid
    kx = np.linspace(-k_max, k_max, n_grid)
    ky = np.linspace(-k_max, k_max, n_grid)
    dk = kx[1] - kx[0]
    
    # Integration weight: dk^2 / (2*pi)^2
    weight = dk**2 / (2 * np.pi)**2
    
    M = np.zeros(3)
    
    for i in range(n_grid):
        for j in range(n_grid):
            kx_val = kx[i]
            ky_val = ky[j]
            
            # Only integrate within circle of radius k_max for better accuracy
            if kx_val**2 + ky_val**2 > k_max**2:
                continue
            
            # Get density matrix correction
            delta_rho = density_matrix_correction(
                kx_val, ky_val, alpha, mu, E_field, m_star, chi
            )
            
            # Compute spin expectation
            S = spin_expectation(delta_rho)
            
            # Accumulate
            M += weight * S
    
    # Multiply by g*mu_B/hbar factor
    M *= G_FACTOR * MU_B / HBAR
    
    return M


def print_magnetization(label, M):
    """Print magnetization vector with label."""
    print(f"{label}:")
    print(f"  Mx = {M[0]:.6e} A/m")
    print(f"  My = {M[1]:.6e} A/m")
    print(f"  Mz = {M[2]:.6e} A/m")
    print(f"  |M| = {np.linalg.norm(M):.6e} A/m")
    if np.linalg.norm(M) > 0:
        print(f"  Direction angle = {np.arctan2(M[1], M[0]) * 180/np.pi:.2f} degrees")


def step7_verify_direction():
    """Step 7: Verify magnetization direction relative to field."""
    print("=" * 60)
    print("Step 7: Magnetization direction verification")
    print("=" * 60)
    
    alpha = 0.1
    mu = 0.1
    m_star = 0.05
    k_max = 0.5
    n_grid = 200
    
    # Field in x-direction
    E_x = np.array([0.1, 0.0])
    M_x = compute_magnetization(alpha, mu, E_x, m_star, k_max=k_max, n_grid=n_grid)
    print_magnetization("E = (0.1, 0)", M_x)
    
    # Field in y-direction
    E_y = np.array([0.0, 0.1])
    M_y = compute_magnetization(alpha, mu, E_y, m_star, k_max=k_max, n_grid=n_grid)
    print_magnetization("E = (0, 0.1)", M_y)
    
    # Check perpendicularity
    dot_product = M_x[0] * 0.1 + M_x[1] * 0  # M·E for first case
    print(f"\nDot product M·E (x-field): {dot_product:.6e}")
    print(f"  Should be ~0 for perpendicular")
    
    # Check linearity
    E_double = np.array([0.2, 0.0])
    M_double = compute_magnetization(alpha, mu, E_double, m_star, k_max=k_max, n_grid=n_grid)
    ratio = np.linalg.norm(M_double) / np.linalg.norm(M_x)
    print(f"\nRatio |M(2E)|/|M(E)| = {ratio:.4f} (should be ~2 for linear)")
    
    return M_x, M_y


def step8_chirality():
    """Step 8: Test chirality dependence."""
    print("\n" + "=" * 60)
    print("Step 8: Chirality dependence")
    print("=" * 60)
    
    alpha = 0.1
    mu = 0.1
    m_star = 0.05
    E_field = np.array([0.1, 0.0])
    k_max = 0.5
    n_grid = 200
    
    M_plus = compute_magnetization(alpha, mu, E_field, m_star, chi=+1, 
                                   k_max=k_max, n_grid=n_grid)
    M_minus = compute_magnetization(alpha, mu, E_field, m_star, chi=-1,
                                    k_max=k_max, n_grid=n_grid)
    
    print_magnetization("chi = +1", M_plus)
    print_magnetization("chi = -1", M_minus)
    
    print(f"\nRatio M(chi=-1)/M(chi=+1): {M_minus[1]/M_plus[1]:.4f}")
    print("  Should be ~-1 for chirality reversal")
    
    return M_plus, M_minus


def step9_alpha_dependence():
    """Step 9: Dependence on spin-orbit coupling strength."""
    print("\n" + "=" * 60)
    print("Step 9: Spin-orbit coupling dependence")
    print("=" * 60)
    
    mu = 0.1
    m_star = 0.05
    E_field = np.array([0.1, 0.0])
    k_max = 0.5
    n_grid = 200
    
    alpha_values = [0.05, 0.1, 0.2, 0.5]
    M_values = []
    
    print(f"{'alpha':>10} {'|M|':>12} {'alpha*|M|':>12}")
    print("-" * 40)
    
    for alpha in alpha_values:
        M = compute_magnetization(alpha, mu, E_field, m_star, k_max=k_max, n_grid=n_grid)
        M_mag = np.linalg.norm(M)
        M_values.append(M_mag)
        print(f"{alpha:10.3f} {M_mag:12.6e} {alpha*M_mag:12.6e}")
    
    # Check if alpha*M is roughly constant
    print("\nNote: If alpha*|M| is roughly constant, then |M| ~ 1/alpha")
    
    return alpha_values, M_values


def step10_E_field_dependence():
    """Step 10: Dependence on electric field magnitude."""
    print("\n" + "=" * 60)
    print("Step 10: Electric field magnitude dependence")
    print("=" * 60)
    
    alpha = 0.1
    mu = 0.1
    m_star = 0.05
    k_max = 0.5
    n_grid = 200
    
    E_values = np.logspace(-3, -1, 10)  # From 0.001 to 0.1
    M_values = []
    
    print(f"{'E':>12} {'My':>12} {'M/E':>12}")
    print("-" * 40)
    
    for E in E_values:
        E_field = np.array([E, 0.0])
        M = compute_magnetization(alpha, mu, E_field, m_star, k_max=k_max, n_grid=n_grid)
        M_values.append(M[1])  # My component
        print(f"{E:12.6e} {M[1]:12.6e} {M[1]/E:12.6e}")
    
    # Check linearity: M/E should be constant
    print("\nNote: If M/E is constant, then M is linear in E")
    
    return E_values, M_values


def step11_E_direction_dependence():
    """Step 11: Dependence on electric field direction."""
    print("\n" + "=" * 60)
    print("Step 11: Electric field direction dependence")
    print("=" * 60)
    
    alpha = 0.1
    mu = 0.1
    m_star = 0.05
    E_mag = 0.1
    k_max = 0.5
    n_grid = 200
    
    angles = np.arange(0, 360, 30)  # 0 to 330 degrees in 30-degree steps
    M_results = []
    
    print(f"{'theta_E':>8} {'theta_M':>8} {'|M|':>12} {'theta_M - theta_E':>16}")
    print("-" * 50)
    
    for theta in angles:
        theta_rad = np.deg2rad(theta)
        E_field = E_mag * np.array([np.cos(theta_rad), np.sin(theta_rad)])
        M = compute_magnetization(alpha, mu, E_field, m_star, k_max=k_max, n_grid=n_grid)
        
        M_mag = np.linalg.norm(M)
        M_angle = np.arctan2(M[1], M[0]) * 180 / np.pi
        M_results.append((theta, M_mag, M_angle))
        
        print(f"{theta:8.0f} {M_angle:8.1f} {M_mag:12.6e} {M_angle - theta:16.1f}")
    
    # Check: |M| constant, angle offset ~90 degrees
    M_mags = [r[1] for r in M_results]
    print(f"\n|M| range: {min(M_mags):.6e} to {max(M_mags):.6e}")
    print(f"  Should be constant (within numerical error)")
    print(f"Angle offset should be ~90 degrees")
    
    return M_results


def step12_mu_dependence():
    """Step 12: Dependence on chemical potential."""
    print("\n" + "=" * 60)
    print("Step 12: Chemical potential dependence")
    print("=" * 60)
    
    alpha = 0.1
    m_star = 0.05
    E_field = np.array([0.1, 0.0])
    k_max = 0.5
    n_grid = 200
    
    mu_values = np.linspace(0.01, 0.5, 10)
    M_values = []
    
    print(f"{'mu':>10} {'|M|':>12}")
    print("-" * 25)
    
    for mu in mu_values:
        M = compute_magnetization(alpha, mu, E_field, m_star, k_max=k_max, n_grid=n_grid)
        M_mag = np.linalg.norm(M)
        M_values.append(M_mag)
        print(f"{mu:10.3f} {M_mag:12.6e}")
    
    # Check: M should be independent of mu for 2D Rashba
    print("\nNote: For 2D Rashba, M should be independent of mu")
    
    return mu_values, M_values


def create_plot_M_vs_E(E_values, M_values):
    """Step 13: Plot magnetization vs electric field magnitude."""
    fig, ax = plt.subplots(figsize=(8, 6))
    
    ax.loglog(E_values, np.abs(M_values), 'bo-', label='Numerical')
    
    # Reference line with slope 1
    E_ref = np.array([1e-3, 1e-1])
    M_ref = np.abs(M_values[-1]) / E_values[-1] * E_ref
    ax.loglog(E_ref, M_ref, 'r--', label='Linear (slope 1)')
    
    ax.set_xlabel('Electric Field |E| (V/Å)')
    ax.set_ylabel('|Magnetization| (A/m)')
    ax.set_title('Edelstein Effect: Magnetization vs Electric Field')
    ax.legend()
    ax.grid(True, which='both', alpha=0.3)
    
    plt.tight_layout()
    plt.savefig('fig_M_vs_E.png', dpi=150)
    plt.close()
    print("\nSaved figure: fig_M_vs_E.png")


def create_plot_M_vs_alpha(alpha_values, M_values):
    """Step 14: Plot magnetization vs spin-orbit coupling."""
    fig, ax = plt.subplots(figsize=(8, 6))
    
    ax.loglog(alpha_values, M_values, 'bo-', label='Numerical')
    
    # Reference 1/alpha line (fit to last point)
    alpha_ref = np.array([0.05, 0.5])
    M_ref = M_values[-1] * alpha_values[-1] / alpha_ref
    ax.loglog(alpha_ref, M_ref, 'r--', label='1/alpha reference')
    
    ax.set_xlabel('Spin-orbit coupling $\\alpha_R$ (eV·Å)')
    ax.set_ylabel('|Magnetization| (A/m)')
    ax.set_title('Edelstein Effect: Magnetization vs Spin-Orbit Coupling')
    ax.legend()
    ax.grid(True, which='both', alpha=0.3)
    
    plt.tight_layout()
    plt.savefig('fig_M_vs_alpha.png', dpi=150)
    plt.close()
    print("Saved figure: fig_M_vs_alpha.png")


def create_plot_M_direction(M_results):
    """Step 15: Polar plot of magnetization direction."""
    fig = plt.figure(figsize=(8, 8))
    ax = fig.add_subplot(111, projection='polar')
    
    # Extract angles
    theta_E = np.deg2rad([r[0] for r in M_results])
    theta_M = np.deg2rad([r[2] for r in M_results])
    
    # Plot numerical results
    ax.scatter(theta_M, np.ones_like(theta_M), c='b', s=50, label='Numerical', alpha=0.7)
    
    # Plot theoretical line: theta_M = theta_E + 90 degrees
    theta_theory = theta_E + np.pi/2
    ax.plot(theta_theory, np.ones_like(theta_theory), 'r-', label='Theory: $\\theta_M = \\theta_E + 90°$')
    
    ax.set_ylim(0, 1.2)
    ax.set_title('Magnetization Direction vs Field Direction')
    ax.legend(loc='upper right')
    
    plt.tight_layout()
    plt.savefig('fig_M_direction.png', dpi=150)
    plt.close()
    print("Saved figure: fig_M_direction.png")


def create_plot_chirality(M_plus, M_minus):
    """Step 16: Bar chart of chirality dependence."""
    fig, ax = plt.subplots(figsize=(8, 6))
    
    labels = ['$\\chi = +1$', '$\\chi = -1$']
    values = [M_plus[1], M_minus[1]]  # My component
    
    bars = ax.bar(labels, values, color=['blue', 'red'], alpha=0.7)
    
    ax.axhline(0, color='black', linewidth=0.5)
    ax.set_ylabel('$M_y$ (A/m)')
    ax.set_title('Edelstein Effect: Chirality Dependence')
    
    # Add value labels
    for bar, val in zip(bars, values):
        ax.text(bar.get_x() + bar.get_width()/2, bar.get_height(),
                f'{val:.3e}', ha='center', va='bottom' if val > 0 else 'top')
    
    plt.tight_layout()
    plt.savefig('fig_chirality.png', dpi=150)
    plt.close()
    print("Saved figure: fig_chirality.png")


def create_plot_M_vs_mu(mu_values, M_values):
    """Step 17: Plot magnetization vs chemical potential."""
    fig, ax = plt.subplots(figsize=(8, 6))
    
    ax.plot(mu_values, M_values, 'bo-', label='Numerical')
    
    # Add horizontal line at mean value
    mean_M = np.mean(M_values)
    ax.axhline(mean_M, color='r', linestyle='--', 
               label=f'Mean: {mean_M:.3e}')
    
    ax.set_xlabel('Chemical potential $\\mu$ (eV)')
    ax.set_ylabel('|Magnetization| (A/m)')
    ax.set_title('Edelstein Effect: Magnetization vs Chemical Potential')
    ax.legend()
    ax.grid(True, alpha=0.3)
    
    plt.tight_layout()
    plt.savefig('fig_M_vs_mu.png', dpi=150)
    plt.close()
    print("Saved figure: fig_M_vs_mu.png")


def step19_convergence_check():
    """Step 19: Check numerical convergence."""
    print("\n" + "=" * 60)
    print("Step 19: Numerical convergence check")
    print("=" * 60)
    
    alpha = 0.1
    mu = 0.1
    m_star = 0.05
    E_field = np.array([0.1, 0.0])
    
    # Coarse grid
    M_coarse = compute_magnetization(alpha, mu, E_field, m_star, 
                                     k_max=0.5, n_grid=100)
    
    # Fine grid
    M_fine = compute_magnetization(alpha, mu, E_field, m_star,
                                   k_max=0.5, n_grid=400)
    
    M_coarse_mag = np.linalg.norm(M_coarse)
    M_fine_mag = np.linalg.norm(M_fine)
    
    print(f"Coarse grid (100x100): |M| = {M_coarse_mag:.6e}")
    print(f"Fine grid (400x400):   |M| = {M_fine_mag:.6e}")
    
    diff_percent = abs(M_fine_mag - M_coarse_mag) / M_fine_mag * 100
    print(f"Difference: {diff_percent:.4f}%")
    
    if diff_percent < 1.0:
        print("Convergence: GOOD (< 1% difference)")
    else:
        print("Convergence: WARNING - difference > 1%")
    
    return diff_percent


def main():
    """Main execution function."""
    print("=" * 70)
    print("EDELSTEIN EFFECT FOR RASHBA FERMIONS")
    print("=" * 70)
    print("\nUnits: Natural units with hbar = e = mu_B = tau = 1")
    print("Model: 2D Rashba gas at Gamma point")
    print("H(k) = (hbar^2*k^2)/(2m*) + alpha_R*(sigma_x*k_y - sigma_y*k_x)")
    print("=" * 70)
    
    # Run all steps
    M_x, M_y = step7_verify_direction()
    M_plus, M_minus = step8_chirality()
    alpha_values, M_alpha = step9_alpha_dependence()
    E_values, M_E = step10_E_field_dependence()
    M_results = step11_E_direction_dependence()
    mu_values, M_mu = step12_mu_dependence()
    
    # Convergence check
    diff = step19_convergence_check()
    
    # Generate all figures
    print("\n" + "=" * 60)
    print("Generating figures...")
    print("=" * 60)
    
    create_plot_M_vs_E(E_values, M_E)
    create_plot_M_vs_alpha(alpha_values, M_alpha)
    create_plot_M_direction(M_results)
    create_plot_chirality(M_plus, M_minus)
    create_plot_M_vs_mu(mu_values, M_mu)
    
    print("\n" + "=" * 60)
    print("ALL CALCULATIONS COMPLETED")
    print("=" * 60)
    print("Figures saved:")
    print("  - fig_M_vs_E.png")
    print("  - fig_M_vs_alpha.png")
    print("  - fig_M_direction.png")
    print("  - fig_chirality.png")
    print("  - fig_M_vs_mu.png")
    
    return 0


if __name__ == "__main__":
    main()
```
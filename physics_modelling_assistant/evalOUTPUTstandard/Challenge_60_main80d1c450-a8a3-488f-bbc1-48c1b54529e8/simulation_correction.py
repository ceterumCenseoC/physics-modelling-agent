```python
import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import simpson

# ==========================================
# Model Implementation
# ==========================================

def gaussian_psf(x, sigma=1.0):
    """
    Defines the Point Spread Function (PSF) as a normalized Gaussian amplitude profile.
    
    Args:
        x (float or np.ndarray): Image plane coordinate(s).
        sigma (float): Width of the PSF (standard deviation of intensity).
        
    Returns:
        float or np.ndarray: Amplitude of the PSF at x.
    """
    # Normalization factor: (pi * sigma^2)^(-1/4) ensures integral(psi^2) = 1
    norm = (np.pi * sigma**2)**(-0.25)
    return norm * np.exp(-x**2 / (2 * sigma**2))

def gaussian_psf_derivative(x, sigma=1.0):
    """
    Calculates the derivative of the Gaussian PSF with respect to x.
    
    Args:
        x (float or np.ndarray): Image plane coordinate(s).
        sigma (float): Width of the PSF.
        
    Returns:
        float or np.ndarray: Derivative d(psi)/dx at x.
    """
    psi = gaussian_psf(x, sigma)
    # d/dx [ exp(-x^2/2s^2) ] = (-x/s^2) * exp(-x^2/2s^2)
    return - (x / sigma**2) * psi

def compute_Delta_k_squared(sigma=1.0, integration_limit=10.0, num_points=10000):
    """
    Calculates delta_k_squared equivalent (J_11 or J_22).
    Defined as Integral [ (d(psi)/dx)^2 ] dx.
    
    Args:
        sigma (float): Width of the PSF.
        integration_limit (float): +/- limit for numerical integration (in units of sigma).
        num_points (int): Number of points for the integration grid.
        
    Returns:
        float: The calculated Delta k squared value.
    """
    # Create a grid centered around 0
    x = np.linspace(-integration_limit * sigma, integration_limit * sigma, num_points)
    
    d_psi = gaussian_psf_derivative(x, sigma)
    integrand = d_psi**2
    
    # Use Simpson's rule for numerical integration
    val = simpson(integrand, x)
    
    return val

def compute_gamma(u1, u2, sigma=1.0, integration_limit=10.0, num_points=10000):
    """
    Calculates the cross-term gamma (J_12).
    Based on the dimensionally corrected model:
    gamma = Integral [ (d(psi(x-u1))/dx) * (d(psi(x-u2))/dx) ] dx
    
    Note: Using the corrected definition where both terms are derivatives 
    to maintain dimensional consistency (units of 1/L^2).
    
    Args:
        u1 (float): Position of source 1.
        u2 (float): Position of source 2.
        sigma (float): Width of the PSF.
        integration_limit (float): +/- limit for numerical integration.
        num_points (int): Number of points for the integration grid.
        
    Returns:
        float: The calculated gamma value.
    """
    # Shifted variables to cover the effective support of both PSFs
    # Center around the midpoint
    center = (u1 + u2) / 2
    separation = abs(u2 - u1)
    
    # Adjust integration window to ensure we capture the shifted modes
    width_scale = max(integration_limit * sigma, separation + 5 * sigma)
    x = np.linspace(center - width_scale, center + width_scale, num_points)
    
    # Derivative with respect to x of shifted PSF psi(x - u) is simply d_psi(x-u)
    d_psi_1 = gaussian_psf_derivative(x - u1, sigma)
    d_psi_2 = gaussian_psf_derivative(x - u2, sigma)
    
    integrand = d_psi_1 * d_psi_2
    
    val = simpson(integrand, x)
    
    return val

def calculate_qfi_theta(u1, u2, sigma=1.0):
    """
    Calculates the Quantum Fisher Information for the parameter theta.
    theta = (1/3)u1 + (2/3)u2
    
    Formula: J_theta = (5/9) * Delta_k^2 + (4/9) * gamma
    
    Args:
        u1 (float): Position of source 1.
        u2 (float): Position of source 2.
        sigma (float): Width of the PSF.
        
    Returns:
        float: The QFI per photon for estimating theta.
        float: Delta_k^2 value used.
        float: Gamma value used.
    """
    dk2 = compute_Delta_k_squared(sigma)
    gam = compute_gamma(u1, u2, sigma)
    
    j_theta = (5.0/9.0) * dk2 + (4.0/9.0) * gam
    
    return j_theta, dk2, gam

def analytic_solution_comparison(u1, u2, sigma=1.0):
    """
    Provides the analytic values for the Gaussian PSF case for comparison.
    """
    dk2 = 1.0 / (2.0 * sigma**2)
    sep = u2 - u1
    gam = dk2 * np.exp(-sep**2 / (4.0 * sigma**2))
    j_theta = (5.0/9.0) * dk2 + (4.0/9.0) * gam
    return j_theta, dk2, gam

# ==========================================
# Simulation and Visualization
# ==========================================

def run_simulation():
    # 1. Setup Parameters based on "Suggested Starting Parameters"
    sigma = 1.0
    d = 0.5  # Separation
    
    # Symmetric positions around 0
    u1 = -d / 2.0
    u2 = d / 2.0
    
    print(f"--- Model Calculation ---")
    print(f"Parameters: Sigma={sigma}, u1={u1}, u2={u2}, Separation={d}")
    
    # 2. Calculate QFI
    j_num, dk2_num, gam_num = calculate_qfi_theta(u1, u2, sigma)
    
    # 3. Compare with Analytic Solution (for Gaussian)
    j_ana, dk2_ana, gam_ana = analytic_solution_comparison(u1, u2, sigma)
    
    print(f"\nResults:")
    print(f"Delta k^2 (Numerical): {dk2_num:.6f} | (Analytic): {dk2_ana:.6f}")
    print(f"Gamma      (Numerical): {gam_num:.6f} | (Analytic): {gam_ana:.6f}")
    print(f"QFI_theta  (Numerical): {j_num:.6f} | (Analytic): {j_ana:.6f}")
    
    # 4. Visualization: QFI vs Source Separation
    # We vary the separation d to see how the resolution limit changes
    separations = np.linspace(0.01, 5.0, 100)
    qfi_vs_d = []
    dk2_const = 1.0/(2.0*sigma**2)
    
    # We can use the analytic formula for the curve for speed and smoothness
    # J = 5/9 * dk2 + 4/9 * dk2 * exp(-d^2/4s^2)
    qfi_vs_d = (5.0/9.0) * dk2_const + (4.0/9.0) * dk2_const * np.exp(-separations**2 / (4.0 * sigma**2))
    
    plt.figure(figsize=(10, 6))
    plt.plot(separations, qfi_vs_d, linewidth=2, label=r'$\mathcal{J}_\theta(d)$')
    
    # Highlight the specific calculated point
    plt.plot(d, j_num, 'ro', label=f'Simulation Point @ $d={d}$')
    
    # Add reference lines
    # Limit for d -> infinity (gamma -> 0)
    lim_inf = (5.0/9.0) * dk2_const
    plt.axhline(y=lim_inf, color='gray', linestyle='--', alpha=0.7, label=r'$\lim_{d\to\infty} \mathcal{J}_\theta = \frac{5}{9}\Delta k^2$')
    
    # Limit for d -> 0 (gamma -> dk2)
    lim_zero = (5.0/9.0 + 4.0/9.0) * dk2_const
    plt.axhline(y=lim_zero, color='gray', linestyle=':', alpha=0.7, label=r'$\lim_{d\to 0} \mathcal{J}_\theta = \Delta k^2$')

    plt.title('Quantum Fisher Information for Weighted Centroid Estimation $\\theta$')
    plt.xlabel(r'Source Separation $d = u_2 - u_1$ ($\sigma$ units)')
    plt.ylabel(r'QFI $\mathcal{J}_\theta$ (Inverse Variance)')
    plt.grid(True, alpha=0.3)
    plt.legend()
    plt.tight_layout()
    
    # Save plot (optional)
    # plt.savefig('qfi_centroid_estimation.png')
    plt.show()

    # 5. Visualization of the PSFs and Derivatives for the calculated case
    x_plot = np.linspace(-5*sigma, 5*sigma, 500)
    psi1 = gaussian_psf(x_plot - u1, sigma)
    psi2 = gaussian_psf(x_plot - u2, sigma)
    dpsi1 = gaussian_psf_derivative(x_plot - u1, sigma)
    dpsi2 = gaussian_psf_derivative(x_plot - u2, sigma)
    
    fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(10, 8), sharex=True)
    
    # Plot Amplitudes
    ax1.plot(x_plot, psi1, label=r'$\psi(x-u_1)$', alpha=0.8)
    ax1.plot(x_plot, psi2, label=r'$\psi(x-u_2)$', alpha=0.8)
    ax1.plot(x_plot, np.sqrt(psi1**2 + psi2**2), 'k--', label='Total Amplitude Envelope')
    ax1.set_title(r'PSF Amplitudes ($\sigma=1.0, d=0.5$)')
    ax1.set_ylabel('Amplitude')
    ax1.legend()
    ax1.grid(True, alpha=0.3)
    
    # Plot Derivatives (used in QFI calculation)
    ax2.plot(x_plot, dpsi1, label=r'$\partial_x \psi(x-u_1)$', alpha=0.8)
    ax2.plot(x_plot, dpsi2, label=r'$\partial_x \psi(x-u_2)$', alpha=0.8)
    # The overlap of these determines Gamma
    overlap_area = dpsi1 * dpsi2
    # Fill overlap to visualize gamma integration
    ax2.fill_between(x_plot, overlap_area, color='green', alpha=0.3, label=r'$\partial_x \psi_1 \cdot \partial_x \psi_2$ ($\propto \gamma$)')
    
    ax2.set_title(r'PSF Derivatives and Overlap ($\gamma$ Integral)')
    ax2.set_xlabel('Position x')
    ax2.set_ylabel('Derivative Amplitude')
    ax2.legend()
    ax2.grid(True, alpha=0.3)
    
    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    run_simulation()
```
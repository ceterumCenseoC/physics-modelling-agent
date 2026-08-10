
```python
import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import quad

# ==========================================
# 1. Physical Parameters and Constants
# ==========================================

# Wavelength and Optical Parameters
wavelength = 532e-9      # 532 nm in meters
NA = 0.85                # Numerical Aperture

# PSF Width (Gaussian approximation)
# Using the proxy for Airy disk width sigma ~ 0.61 * lambda / NA
sigma_psf = (0.61 * wavelength) / NA

# Source Positions
# We place sources symmetrically around 0 for the sweep, 
# but the specific calculation uses u1=-150nm, u2=150nm (Sep=300nm)
# as per the derived parameters in the context.
u1 = -150e-9
u2 = 150e-9
delta_u = u2 - u1

# ==========================================
# 2. Model Functions
# ==========================================

def psf(x, u, sigma):
    """
    Gaussian Point Spread Function.
    psi(x) = (1/(2*pi*sigma^2))^(1/4) * exp(-x^2 / (4*sigma^2))
    """
    norm_factor = 1.0 / np.power(2 * np.pi * sigma**2, 0.25)
    return norm_factor * np.exp(-(x - u)**2 / (4 * sigma**2))

def d_psf_dx(x, u, sigma):
    """
    Derivative of the PSF with respect to x.
    psi'(x) = d/dx [ psi(x-u) ]
    """
    psi = psf(x, u, sigma)
    # Analytic derivative for Gaussian: - (x-u)/(2*sigma^2) * psi
    return - (x - u) / (2 * sigma**2) * psi

def calculate_delta_k_sq(sigma):
    """
    Calculates Delta k^2 = integral [ (d_psi/dx)^2 ] dx
    """
    # Using analytic result for Gaussian: 1 / (4 * sigma^2)
    return 1.0 / (4 * sigma**2)

def calculate_gamma_prime(u1, u2, sigma):
    """
    Calculates Gamma' = integral [ psi'(x-u1) * psi'(x-u2) ] dx
    Note: Using gamma' (derivative overlap) for dimensional consistency.
    """
    d = u2 - u1
    # Analytic result for the overlap of two Gaussian derivatives
    # Derived from integration of product of two Gaussians.
    # exp(-d^2 / (8*sigma^2)) * (1 - d^2/(8*sigma^2)) / (4*sigma^2)
    # However, let's use numerical integration to be general and 
    # strictly follow the "numerical implementation" instruction.
    
    def integrand(x):
        return d_psf_dx(x, u1, sigma) * d_psf_dx(x, u2, sigma)
    
    # Integrate over a sufficiently large range (e.g., +/- 5 sigma of the combined width)
    limit = 10 * sigma 
    integral_val, _ = quad(integrand, -limit, limit)
    return integral_val

def calculate_qfi(w1, w2, delta_k_sq, gamma_prime):
    """
    Calculates QFI = (w1^2 + w2^2)*Delta_k^2 + 2*w1*w2*Gamma'
    """
    return (w1**2 + w2**2) * delta_k_sq + 2 * w1 * w2 * gamma_prime

# ==========================================
# 3. Calculation and Visualization
# ==========================================

# -- 3.1. Calculate Parameters for the Specific Configuration (300nm separation) --
dk2_val = calculate_delta_k_sq(sigma_psf)
gp_val = calculate_gamma_prime(u1, u2, sigma_psf)

# Weights
w1 = 1.0/3.0
w2 = 2.0/3.0

qfi_val = calculate_qfi(w1, w2, dk2_val, gp_val)

print("--- Results for Separation = 300 nm ---")
print(f"Wavelength (lambda): {wavelength*1e9:.1f} nm")
print(f"PSF Sigma: {sigma_psf*1e9:.1f} nm")
print(f"Delta k^2: {dk2_val:.4e} m^-2")
print(f"Gamma' (Overlap): {gp_val:.4e} m^-2")
print(f"Quantum Fisher Information (per photon): {qfi_val:.4e} m^-2")

# -- 3.2. Sweep Separation and Plot --
separations_nm = np.linspace(0, 1000, 200)
separations = separations_nm * 1e-9
qfi_sweep = []

for sep in separations:
    # Symmetric positions
    u_t1 = -sep / 2
    u_t2 = sep / 2
    gp_t = calculate_gamma_prime(u_t1, u_t2, sigma_psf)
    qfi_t = calculate_qfi(w1, w2, dk2_val, gp_t) # Delta k^2 is constant
    qfi_sweep.append(qfi_t)

# Convert to convenient units for plotting (nm^-2)
qfi_sweep_plot = np.array(qfi_sweep) * (1e-9)**2 # Convert m^-2 to nm^-2
dk2_plot = dk2_val * (1e-9)**2

plt.figure(figsize=(10, 6))
plt.plot(separations_nm, qfi_sweep_plot, label=r'$F_Q(\theta)$', linewidth=2, color='blue')
# Plot the asymptotic limit (sources far apart, Gamma' -> 0)
plt.axhline(y=(5.0/9.0)*dk2_plot, color='red', linestyle='--', 
            label=r'Asymptotic Limit ($\frac{5}{9}\Delta k^2$)')
# Highlight the Rayleigh-like regime
plt.axvline(x=300, color='green', linestyle=':', alpha=0.7, label='Specified Separation (300nm)')
plt.title('Quantum Fisher Information vs Source Separation')
plt.xlabel('Source Separation $\Delta u$ (nm)')
plt.ylabel('QFI ($nm^{-2}$)')
plt.legend()
plt.grid(True, alpha=0.3)
plt.show()
```
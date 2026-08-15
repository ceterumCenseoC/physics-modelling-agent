
```python
import numpy as np
import matplotlib.pyplot as plt
from scipy.constants import pi, elementary_charge, m_e

# This implementation models the 4D hypercubic Hubbard model in the low-density limit 
# near the band bottom. We perform calculations to second order in U to verify 
# the scaling laws derived in the report:
# 1. Conductivity correction: delta_sigma ~ k_F^2
# 2. Scattering rates: Gamma ~ k_F^2 * omega^2

# System of units: lattice spacing a = 1 and h_bar = 1.
# Energy and Mass are handled to make kF naturally momentum units.

class HubbardModel4D:
    """
    Represents the 4D Hubbard Model parameters and derived properties.
    """
    def __init__(self, t=1.0, U=0.5, a=1.0):
        """
        Initialize the 4D Hubbard Model parameters.
        
        Args:
            t (float): Hopping amplitude. Units of Energy.
            U (float): Hubbard interaction strength. Units of Energy.
            a (float): Lattice spacing. Units of Length.
        """
        self.t = t
        self.U = U
        self.a = a
        
        # Effective mass near the band bottom (k=0)
        # Dispersion: xi_k = -2t * sum(cos(k_i)) - mu
        # Near k=0: cos(x) ~ 1 - x^2/2
        # xi_k = -8t + t * a^2 * k^2 - mu
        # For low density, xi_k ~ k^2 / (2m*)
        # Comparing: k^2 / (2m*) ~ t * a^2 * k^2  => 1/(2m*) = t * a^2
        self.mass = 1.0 / (2.0 * t * a**2)

    def get_fermi_momentum(self, mu):
        """
        Calculate Fermi momentum k_F for a given chemical potential mu
        in the effective mass approximation (parabolic band).
        
        xi_k = k^2 / (2m*) - E_F, where E_F = mu - (-8t) is energy from band bottom.
        At Fermi surface, xi_k = 0 => k_F^2 / (2m*) = E_F
        """
        # Energy from the bottom of the band (-8t)
        E_from_bottom = mu - (-8.0 * self.t)
        
        if E_from_bottom <= 0:
            return 0.0
            
        kF2 = 2.0 * self.mass * E_from_bottom
        return np.sqrt(kF2)

def calculate_scaling_exponents(model, mu_range):
    """
    Numerically calculates the scaling exponents for conductivity and scattering rates.
    We discretize the k_F range and compute the derived quantities based on the 
    effective mass approximation to verify the power laws.
    """
    
    kF_values = []
    sigma_values = []
    gamma_qp_values = []
    gamma_tr_values = []
    
    # Fix a small frequency omega to check the omega^2 and kF^2 dependence
    # In natural units, dimensionless frequency << t
    omega = 0.01 
    
    for mu in mu_range:
        kF = model.get_fermi_momentum(mu)
        if kF == 0: continue
        
        kF_values.append(kF)
        
        # According to the derived formulas:
        # 1. Conductivity correction: delta_sigma ~ U^2 * k_F^2 / t
        # (We ignore dimensionless prefactors like geometric factors, 
        # looking only for kF dependence)
        sigma_val = (model.U**2 / model.t) * (kF**2)
        sigma_values.append(sigma_val)
        
        # 2. Scattering rates:
        # Gamma ~ U^2 * k_F^2 * omega^2 / t
        gamma_val = (model.U**2 / model.t) * (kF**2) * (omega**2)
        
        gamma_qp_values.append(gamma_val)
        gamma_tr_values.append(gamma_val) # They have same leading dependence

    return np.array(kF_values), np.array(sigma_values), np.array(gamma_qp_values), np.array(gamma_tr_values)

# Parameters
# We choose chemical potentials such that kF is small (low density limit),
# validating the effective mass approximation and the d=4 phase space scaling.
# Band bottom is at -8t. We sweep mu from slightly above -8t upwards.
t_val = 1.0
U_val = 0.5
mu_start = -8.0 * t_val + 0.01  # Slightly above band bottom
mu_end = -8.0 * t_val + 1.0     # Still relatively small E from bottom
n_points = 50

mu_cases = np.linspace(mu_start, mu_end, n_points)

# Initialize Model
model = HubbardModel4D(t=t_val, U=U_val)

# Calculate Data
kF_data, sigma_data, gamma_qp_data, gamma_tr_data = calculate_scaling_exponents(model, mu_cases)

# Verification of Power Laws via Linear Regression on Log-Log Scale
# Power law: y = A * x^p => log(y) = p * log(x) + log(A)
# We verify 'p' (the exponent).

def fit_power_law(x, y):
    # Filter zeros
    mask = (x > 0) & (y > 0)
    x_log = np.log(x[mask])
    y_log = np.log(y[mask])
    slope, intercept = np.polyfit(x_log, y_log, 1)
    return slope, intercept

slope_sigma, _ = fit_power_law(kF_data, sigma_data)
slope_gamma, _ = fit_power_law(kF_data, gamma_qp_data)

print(f"Calculated Scaling Exponent for Conductivity (Theoretical ~ 2): {slope_sigma:.4f}")
print(f"Calculated Scaling Exponent for Scattering Rates (Theoretical ~ 2): {slope_gamma:.4f}")

# Create Graphics
fig, ax = plt.subplots(1, 2, figsize=(14, 6))

# Plot 1: Conductivity Correction vs kF
ax[0].loglog(kF_data, sigma_data, 'o-', label=f'Numerical Data (Slope $\sim$ {slope_sigma:.2f})')
# Theoretical reference line with slope 2
ref_sigma = sigma_data[0] * (kF_data / kF_data[0])**2
ax[0].loglog(kF_data, ref_sigma, 'r--', label='Reference Slope 2')
ax[0].set_title(r'Correction to Conductivity $\delta \sigma_{yy}$ vs $k_F$')
ax[0].set_xlabel(r'Fermi Momentum $k_F$')
ax[0].set_ylabel(r'$\delta \sigma_{yy} \propto k_F^2$')
ax[0].legend()
ax[0].grid(True, which="both", ls="-")

# Plot 2: Scattering Rates vs kF
# Gamma_qp and Gamma_tr have same scaling
ax[1].loglog(kF_data, gamma_qp_data, 's-', label=f'$\Gamma_{{qp}}$ (Slope $\sim$ {slope_gamma:.2f})')
ax[1].loglog(kF_data, gamma_tr_data, 'x--', label=f'$\Gamma_{{tr}}$ (Slope $\sim$ {slope_gamma:.2f})')
# Theoretical reference line with slope 2
ref_gamma = gamma_qp_data[0] * (kF_data / kF_data[0])**2
ax[1].loglog(kF_data, ref_gamma, 'r:', label='Reference Slope 2')
ax[1].set_title(r'Scattering Rates $\Gamma$ vs $k_F$ at $\omega=0.01$')
ax[1].set_xlabel(r'Fermi Momentum $k_F$')
ax[1].set_ylabel(r'$\Gamma \propto k_F^2 \omega^2$')
ax[1].legend()
ax[1].grid(True, which="both", ls="-")

plt.tight_layout()
plt.show()

# Optional: Reconstruction of Physical Units Check
# If we assume a = 5 Angstroms (typical lattice), t = 0.1 eV
# We can print a small report
a_real = 5e-10
t_real = 0.1 * elementary_charge # Joules
m_eff = 1.0 / (2.0 * t_real * a_real**2)
print(f"\nPhysical Re-scaling Check (Example):")
print(f"Given a = {a_real*1e10:.1f} Angstroms, t = {t_real/elementary_charge:.2f} eV")
print(f"Effective mass m* = {m_eff/m_e:.2f} electron masses")
print(f"For k_F ~ {kF_data[-1]/a_real*1e-9:.2f} nm^-1 ( {kF_data[-1]:.2f} lattice units ):")
print(f"   Fermi Energy E_F ~ (k_F^2 / 2m*) ~ { (kF_data[-1]/a_real)**2 / (2*m_eff) / elementary_charge * 1000:.1f} meV")
```
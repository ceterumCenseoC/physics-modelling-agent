```python
import numpy as np
import matplotlib.pyplot as plt

def compute_spectrum(k_vec, chi, kappa, sigma):
    """
    Computes the complex spectrum omega(k) for the dissipative 
    quadrupole effective field theory model.
    
    The characteristic equation derived from the linearized hydrodynamics 
    (Damped Euler-Bernoulli Beam equation) is:
    chi * w^2 + i * sigma * k^4 * w - kappa * k^4 = 0
    
    Parameters:
    k_vec (array): Wavenumbers.
    chi (float): Charge susceptibility (inertia).
    kappa (float): Quadrupole superfluid stiffness.
    sigma (float): Dissipative coefficient.
    
    Returns:
    omegas (complex array): The computed frequencies for the positive branch.
    """
    omegas = []
    
    # We solve the quadratic equation a*w^2 + b*w + c = 0 for each k
    # a = chi
    # b = i * sigma * k^4
    # c = -kappa * k^4
    
    for k in k_vec:
        a = chi
        b = 1j * sigma * (k**4)
        c = -kappa * (k**4)
        
        # Calculate discriminant
        delta = np.sqrt(b**2 - 4*a*c)
        
        # Calculate roots
        # w = (-b +/- sqrt(b^2 - 4ac)) / 2a
        # Note: We use the form (-b + delta) / (2a) and (-b - delta) depending on phase
        # to ensure we get the +c_s k^2 mode and the -c_s k^2 mode.
        w1 = (-b + delta) / (2*a)
        w2 = (-b - delta) / (2*a)
        
        # Select the propagating mode with positive real part (Re(w) > 0)
        # In the non-dissipative limit (sigma=0), w ~ +/- sqrt(kappa/chi)*k^2.
        # We pick the positive frequency branch.
        if np.real(w1) >= 0:
            omegas.append(w1)
        else:
            omegas.append(w2)
            
    return np.array(omegas)

# --- Main Simulation Parameters ---
# The model uses normalized units for general illustration.
chi_val = 1.0      # Susceptibility (Inertia)
kappa_val = 1.0    # Stiffness (Restoring force)
sigma_val = 0.1    # Dissipation (Damping coefficient)

# --- Wavevector Setup ---
k_max = 2.0        # Maximum wavenumber
k_points = 200     # Resolution
# Avoid k=0 to prevent division by zero in some scaling forms, 
# though the solver handles k=0 fine (returns 0).
k_vals = np.linspace(0.01, k_max, k_points)

# --- Calculation ---
omega_vals = compute_spectrum(k_vals, chi_val, kappa_val, sigma_val)

# --- Visualization ---
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 6))

# Plot 1: Real Part (Dispersion)
ax1.plot(k_vals, np.real(omega_vals), 'b-', linewidth=2, label=r'Re($\omega$)')
# Theoretical approximation for small k (Propagating Quadrupole Mode)
# w_theory = sqrt(kappa/chi) * k^2
w_theory_real = np.sqrt(kappa_val/chi_val) * k_vals**2
ax1.plot(k_vals, w_theory_real, 'r--', linewidth=2, label=r'Theory $\sqrt{\kappa/\chi} k^2$')

ax1.set_xlabel(r'Wavenumber $k$', fontsize=14)
ax1.set_ylabel(r'Frequency $\omega$ (Real)', fontsize=14)
ax1.set_title(r'Dispersion Relation Re($\omega(k)$)', fontsize=16)
ax1.grid(True, linestyle='--')
ax1.legend(fontsize=12)

# Plot 2: Imaginary Part (Damping)
ax2.plot(k_vals, np.imag(omega_vals), 'g-', linewidth=2, label=r'Im($\omega$)')
# Theoretical approximation for damping
# gamma_theory = -(sigma / (2*chi)) * k^4
w_theory_imag = -(sigma_val / (2*chi_val)) * k_vals**4
ax2.plot(k_vals, w_theory_imag, 'm--', linewidth=2, label=r'Theory $-\frac{\sigma}{2\chi} k^4$')

ax2.set_xlabel(r'Wavenumber $k$', fontsize=14)
ax2.set_ylabel(r'Damping Rate $\gamma = -$Im($\omega$)', fontsize=14)
ax2.set_title(r'Dissipation Profile Im($\omega(k)$)', fontsize=16)
ax2.grid(True, linestyle='--')
ax2.legend(fontsize=12)

plt.tight_layout()
plt.show()

# --- Numerical Output for Verification ---
k_test = 1.0
w_test = compute_spectrum(np.array([k_test]), chi_val, kappa_val, sigma_val)[0]
print("-" * 50)
print(f"Model Parameters:")
print(f"  Susceptibility (\u03C7): {chi_val}")
print(f"  Stiffness (\u03BA):     {kappa_val}")
print(f"  Dissipation (\u03C3):   {sigma_val}")
print("-" * 50)
print(f"Spectrum at k = {k_test}:")
print(f"  \u03C9 = {w_test:.5f}")
print(f"  Re(\u03C9) [Dispersion]: {np.real(w_test):.5f}")
print(f"  Im(\u03C9) [Damping]:    {np.imag(w_test):.5f}")
print("-" * 50)

# Compare with theoretical small-k approximations at k=1.0
# Note: k=1.0 is not necessarily "small", so deviations are expected for sigma > 0
real_approx = np.sqrt(kappa_val/chi_val) * k_test**2
imag_approx = -(sigma_val / (2*chi_val)) * k_test**4
print(f"Theoretical approximations (small k):")
print(f"  Re(\u03C9) \u2248 {real_approx:.5f}")
print(f"  Im(\u03C9) \u2248 {imag_approx:.5f}")
```
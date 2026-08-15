
```python
import numpy as np
import matplotlib.pyplot as plt

def cascaded_opa_model(r1, r2, mu, eta, phi1, phi2, theta):
    """
    Calculates the mean squared power of the photocurrent's sideband < |I_theta(nu)|^2 >.

    Parameters:
    -----------
    r1, r2 : float
        Gain parameters of the two OPAs.
    mu : float
        Transmission coefficients of on-chip loss (signal and idler).
    eta : float
        Detection efficiencies (signal and idler).
    phi1, phi2 : float
        Pump phases of the two OPAs.
    theta : float
        The phase theta in the definition of I_theta.

    Returns:
    --------
    float
        The normalized photocurrent power spectral density < |I_theta|^2 >.
    """
    
    # Precompute hyperbolic functions
    c1, s1 = np.cosh(r1), np.sinh(r1)
    c2, s2 = np.cosh(r2), np.sinh(r2)
    sh2r1 = np.sinh(2*r1)
    sh2r2 = np.sinh(2*r2)
    ch2r1 = np.cosh(2*r1)
    ch2r2 = np.cosh(2*r2)
    
    # The interaction term derived from the general Bogoliubov transformation.
    # V = 1 + (eta*mu)^2 [ ch(2r1)ch(2r2) + sh(2r1)sh(2r2)cos(dphi) + sh(2r1)sh(2r2)cos(2theta - phi1 - phi2) ]
    #   + eta^2(1-mu^2)ch(2r2) + (1-eta^2)
    # Note: The constant 1 comes from the commutator <0|a a^dag|0> = 1.
    
    term_interaction = ch2r1 * ch2r2 + \
                      sh2r1 * sh2r2 * np.cos(phi2 - phi1) + \
                      sh2r1 * sh2r2 * np.cos(2 * theta - phi1 - phi2)
                      
    # Total Variance
    V = (2 - eta**2) + \
        eta**2 * (1 - mu**2) * ch2r2 + \
        (eta * mu)**2 * term_interaction
        
    return V

def get_min_max_noise(r1, r2, mu, eta):
    """
    Calculates maximum squeezed and anti-squeezed values for phi2 - phi1 = pi.
    """
    # Using the simplified formulas derived for the pi phase difference
    base = 2 - eta**2 + eta**2 * (1 - mu**2) * np.cosh(2 * r2)
    
    # Squeezed (min) and Anti-squeezed (max) terms
    min_noise = base + (eta * mu)**2 * np.exp(-2 * (r1 + r2))
    max_noise = base + (eta * mu)**2 * np.exp(2 * (r1 + r2))
    
    return min_noise, max_noise

# --- Setup Parameters ---
# Using the suggested starting parameters from the context
r1 = 0.5
r2 = 0.5
mu = 0.90
eta = 0.85
phi1 = 0.0
phi2 = np.pi  # Phase difference of pi

# --- 1. Plotting Noise vs Phase Theta ---
theta_vals = np.linspace(0, 2*np.pi, 500)
noise_vals = []

for th in theta_vals:
    noise_vals.append(cascaded_opa_model(r1, r2, mu, eta, phi1, phi2, th))

min_noise_theory, max_noise_theory = get_min_max_noise(r1, r2, mu, eta)

plt.figure(figsize=(10, 6))
plt.plot(theta_vals, noise_vals, label=r'$\langle |I_{\\theta}|^2 \\rangle$')
plt.axhline(y=1, color='k', linestyle='--', alpha=0.5, label='Shot Noise Limit (1)')
plt.axhline(y=min_noise_theory, color='g', linestyle=':', label='Calculated Minimum (Squeezed)')
plt.axhline(y=max_noise_theory, color='r', linestyle=':', label='Calculated Maximum (Anti-Squeezed)')

# Mark min/max
min_idx = np.argmin(noise_vals)
max_idx = np.argmax(noise_vals)
plt.plot(theta_vals[min_idx], noise_vals[min_idx], 'go', label=f'Min ({theta_vals[min_idx]:.2f} rad)')
plt.plot(theta_vals[max_idx], noise_vals[max_idx], 'ro', label=f'Max ({theta_vals[max_idx]:.2f} rad)')

plt.title(r'Photocurrent Noise Power vs Phase $\theta$ ($\phi_2-\phi_1=\pi$)')
plt.xlabel(r'Phase $\theta$ (radians)')
plt.ylabel(r'Noise Power $\langle |I_{\\theta}|^2 \\rangle$ (Normalized)')
plt.grid(True, alpha=0.3)
plt.legend()
plt.tight_layout()
plt.show()

# --- 2. Sweeping Gains (r1 = r2 = r) ---
r_sweep = np.linspace(0.1, 1.2, 50)
min_sweep = []
max_sweep = []

for r in r_sweep:
    mn, mx = get_min_max_noise(r, r, mu, eta)
    min_sweep.append(mn)
    max_sweep.append(mx)

plt.figure(figsize=(10, 6))
plt.plot(r_sweep, np.array(min_sweep), 'g-', linewidth=2, label='Maximum Squeezing (Min Noise)')
plt.plot(r_sweep, np.array(max_sweep), 'r-', linewidth=2, label='Maximum Anti-Squeezing (Max Noise)')
plt.axhline(y=1, color='k', linestyle='--', alpha=0.5, label='Shot Noise Limit (1)')

plt.title(r'Squeezing vs Gain Parameter ($\eta=0.85, \mu=0.90$)')
plt.xlabel(r'Gain $r_1 = r_2$')
plt.ylabel(r'Noise Power $\langle |I|^2 \\rangle$')
plt.yscale('log') 
plt.grid(True, alpha=0.3, which="both")
plt.legend()
plt.tight_layout()
plt.show()

# Print numerical results for the starting parameters
print(f"--- Results for r1={r1}, r2={r2}, mu={mu}, eta={eta}, dPhi={phi2-phi1:.2f} ---")
print(f"Minimum Noise (Squeezing): {min_noise_theory:.4f}")
print(f"Maximum Noise (Anti-squeezing): {max_noise_theory:.4f}")
print(f"Squeezing in dB: {10*np.log10(min_noise_theory):.2f} dB")
print(f"Anti-squeezing in dB: {10*np.log10(max_noise_theory):.2f} dB")

# Verify against the analytic predictions for Min/Max phases
# Min should be at theta = phi1 = 0
# Max should be at theta = phi1 + pi/2 = pi/2
val_at_0 = cascaded_opa_model(r1, r2, mu, eta, phi1, phi2, 0)
val_at_pi2 = cascaded_opa_model(r1, r2, mu, eta, phi1, phi2, np.pi/2)

print(f"\n--- Verification of Phase Dependence ---")
print(f"Noise at theta=0 (Expected Min): {val_at_0:.4f}")
print(f"Noise at theta=pi/2 (Expected Max): {val_at_pi2:.4f}")

assert np.isclose(val_at_0, min_noise_theory, atol=1e-6), "Min phase check failed"
assert np.isclose(val_at_pi2, max_noise_theory, atol=1e-6), "Max phase check failed"
print("Phase checks passed.")
```
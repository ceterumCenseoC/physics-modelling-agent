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

    # Derived coefficients for the detected modes
    # A = eta * mu * [ cosh(r1)*cosh(r2) + exp(i*(phi2-phi1))*sinh(r1)*sinh(r2) ]
    # B = eta * mu * [ exp(i*phi1)*sinh(r1)*cosh(r2) + exp(i*phi2)*cosh(r1)*sinh(r2) ]
    
    # Precompute hyperbolic functions
    c1, s1 = np.cosh(r1), np.sinh(r1)
    c2, s2 = np.cosh(r2), np.sinh(r2)
    
    # Calculate A and B coefficients complex values
    # Note: The phase difference is crucial
    exp_dphi = np.exp(1j * (phi2 - phi1))
    
    A_coeff_real = eta * mu * (c1 * c2 + np.cos(phi2 - phi1) * s1 * s2)
    A_coeff_imag = eta * mu * (np.sin(phi2 - phi1) * s1 * s2)
    A = A_coeff_real + 1j * A_coeff_imag
    
    # B term
    B = eta * mu * (np.exp(1j * phi1) * s1 * c2 + np.exp(1j * phi2) * c1 * s2)
    
    # Calculate the terms required for < |I_theta|^2 >
    # Term 1: Constant term 1 from commutator relation
    constant_term = 1.0
    
    # Term 2: |A|^2 + |B|^2
    # Or more efficiently combined with the specific general formula derived
    
    # Let's use the explicit compact formula derived in the analysis context for robustness
    # < |I|^2 > = 2 - eta^2 + eta^2(1-mu^2)cosh(2r2) + eta^2*mu^2[ ... ]
    
    term_base = 2 - eta**2 + eta**2 * (1 - mu**2) * np.cosh(2 * r2)
    
    # The theta-dependent part inside the mu^2 term
    # cosh(2r1)cosh(2r2) + sinh(2r1)sinh(2r2)cos(phi2-phi1) 
    # + sinh(2r1)sinh(2r2)cos(2*theta - phi1 - phi2)
    # We use the specific derivation form:
    # K = cosh(2r1)cosh(2r2) - sinh(2r1)sinh(2r2) if cos(dphi) = -1
    
    # Implement the most general form first based on A and B
    # <I> = 1 + 2|B|^2 + 2*Re(A*B*exp(2i*theta)) + V_vac
    # V_vac = (1-eta) + eta(1-mu)(cosh^2 r2 + sinh^2 r2)
    
    # Let's calculate using the A, B coefficients directly to ensure correctness for any phi
    # a_det = A a_in + B a_id_dag + vacuum
    # a_i_det_dag = B* a_in_dag + A* a_i_dag + vacuum_dag
    
    # < a_s^dag a_s > = |B|^2 (assuming vacuum input <a_in^dag a_in>=0) NO. 
    # If a_s = A a_s_in + B a_i_in_dag, then <a_s^dag a_s> = |B|^2 <a_i_in a_i_in^dag> = |B|^2 * 1
    # And <a_i a_i^dag> = <(B* a_s_in^dag + A* a_i_in)(A a_s_in + B a_i_in^dag)> = 1 + |B|^2
    
    # Total Signal Contribution: |B|^2 + 1 + |B|^2 = 1 + 2|B|^2
    
    # Correlation Term: <a_s a_i> = <(A a_s + B a_i^dag)(B* a_s^dag + A* a_i)> = A A* <a_s a_s^dag> + B B* <a_i^dag a_i>
    # Wait, let's stick to derived formula.
    
    # Formula: 
    # V = 2 - eta^2 + eta^2(1-mu^2)cosh(2r2) + 
    #     eta^2*mu^2 [ cosh(2r1)cosh(2r2) + sinh(2r1)sinh(2r2)cos(phi2-phi1) + sinh(2r1)sinh(2r2)cos(2theta - phi1 - phi2) ]
    # Note: The term inside [] in the previous 'Summary of Key Results' table is slightly different due to grouping.
    # Using the 'More compact form' from the text:
    # V = 1 + eta^2*mu^2 * (...) + eta^2(1-mu^2)cosh(2r2) + (1-eta^2)
    # V = 2 - eta^2 + eta^2(1-mu^2)cosh(2r2) + eta^2*mu^2 * Interaction
    
    # Let's implement this "More compact form" explicitly
    sh2r1 = np.sinh(2*r1)
    sh2r2 = np.sinh(2*r2)
    ch2r1 = np.cosh(2*r1)
    ch2r2 = np.cosh(2*r2)
    
    # The 'Interaction' term from the 'More compact form' expansion needs to be verified.
    # Let's calculate V using the A and B algebra, it is safer.
    # V = 1 + 2|B|^2 + 2*Re(AB* exp(2itheta)) + Noise
    # Noise = (1-eta) + eta(1-mu)(ch^2 r2 + sh^2 r2)
    
    # Calculate A, B, and their norms/products
    # Recalculating A and B carefully with pre-computes
    # A = eta * mu * ( c1*c2 + exp(i*dphi)*s1*s2 )
    A_real = eta * mu * (c1*c2 + np.cos(phi2-phi1)*s1*s2)
    A_imag = eta * mu * (np.sin(phi2-phi1)*s1*s2)
    
    # B = eta * mu * ( exp(i*phi1)*s1*c2 + exp(i*phi2)*c1*s2 )
    B_real = eta * mu * (np.cos(phi1)*s1*c2 + np.cos(phi2)*c1*s2)
    B_imag = eta * mu * (np.sin(phi1)*s1*c2 + np.sin(phi2)*c1*s2)
    
    A = A_real + 1j*A_imag
    B = B_real + 1j*B_imag
    
    # Terms of the photocurrent variance
    # <I I_dag> = <a_s^dag a_s> + <a_i a_i^dag> + e^(-2i theta)<a_s a_i> + e^(2i theta)<a_s^dag a_i^dag> + Noise
    
    # Assuming vacuum input
    # <a_s^dag a_s> = |B|^2
    # <a_i a_i^dag> = 1 + |B|^2 (due to the structure of the conjugate transformation)
    # Proof: If a_s = A u + B v^dag, then (a_i)^dag = B* u^dag + A* v. 
    # a_i = B u^dag^* + A* v^*. In vacuum <0|0>=0. <a_i a_i^dag> needs careful handling of the conjugate pair.
    # Actually, simpler: The commutation relation must hold: [a_s, a_s^dag] = 1.
    # [A u + B v^dag, A* u^dag + B* v] = |A|^2 + |B|^2 = 1.
    # This is satisfied for ideal lossless OPA.
    # With loss (eta, mu), the commutator is eta^2 mu^2 (cosh^2 + sinh^2) ...
    # The vacuum noise term added in the formula accounts for this.
    
    # Let's stick to the derived Result for General Case in step 5 of the text:
    # < |I|^2 > = 1 + |A|^2 + |B|^2 + 2*Re(AB* e^(-2i theta)) + Vac
    
    # Wait, the text says: "The vacuum terms contribute |A_v|^2 + ..."
    # The summarized formula in the 'Summary of Key Results' table is:
    # V = 2 - eta^2 + eta^2(1-mu^2)cosh(2r2) + eta^2*mu^2[ ch(2r1-2r2) - sh(2r1)sh(2r2)cos(dphi) + ... ]
    # This "Summary" formula was for phi2-phi1=pi. Let's look for the General one before that.
    
    # The text provides: 
    # V = 1 + eta^2 mu^2 [ ch(2r1)ch(2r2) + sh(2r1)sh(2r2)cos(dphi) + 2ch(r1)sh(r1)ch(r2)sh(r2)(e^2i(...)+...) ]
    # + eta^2(1-mu^2)ch(2r2) + (1-eta^2)
    
    # Let's implement the simplified logic:
    # 1. Calculate the 'Signal' part treated as a beam splitter of efficiency eta*mu.
    # 2. Calculate noise added by vacuum.
    
    # Using the cleaner form identified in the 'Special Case' derivation logic applied to general terms:
    # V_signal(chi) = ch(2r1)ch(2r2) + sh(2r1)sh(2r2)cos(dphi) + sh(2r1)sh(2r2)cos(2theta - phi1 - phi2)
    # Note: The last term 2*c1*s1*c2*s2*2cos(...) = sh(2r1)sh(2r2)*cos(...)
    
    term_interaction = ch2r1 * ch2r2 + \
                      sh2r1 * sh2r2 * np.cos(phi2 - phi1) + \
                      sh2r1 * sh2r2 * np.cos(2 * theta - phi1 - phi2)
                      
    # Total Variance
    V = (2 - eta**2) + \
        eta**2 * (1 - mu**2) * ch2r2 + \
        (eta * mu)**2 * term_interaction
        
    # The (2 - eta^2) comes from 1 (signal) + 1 (idler) + (1-eta^2) (detector vacuum)?
    # Wait, if input is vacuum, <a_in a_in_dag> = 1.
    # Vacuum added by detector: (1-eta^2).
    # Vacuum added by inter-stage loss: eta^2 * (1-mu^2) * ch2r2. (Amplified by OPA2)
    # The (eta*mu)^2 term is the main signal processing chain.
    
    return V

def get_min_max_noise(r1, r2, mu, eta):
    """
    Calculates maximum squeezed and anti-squeezed values for phi2 - phi1 = pi.
    """
    # Using the simplified formulas derived for the pi phase difference
    # Squeezed (min)
    # V_min = 2 - eta^2 + eta^2(1-mu^2)cosh(2r2) + (eta*mu)^2 * exp(-2(r1+r2))
    
    # Noting: exp(-2*r) is e^{-2r}. 
    # If r1=r2=r, then exp(-4r). The text says e^{-2(r1+r2)}.
    
    base = 2 - eta**2 + eta**2 * (1 - mu**2) * np.cosh(2 * r2)
    
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
plt.yscale('log') # Log scale is often useful for squeezing (dB)
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
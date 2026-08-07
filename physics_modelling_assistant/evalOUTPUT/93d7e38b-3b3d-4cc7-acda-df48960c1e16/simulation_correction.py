```python
import numpy as np
import matplotlib.pyplot as plt

def photocurrent_power(theta, r1, r2, mu, eta, phi1, phi2):
    """
    Calculate the mean squared power of the photocurrent sideband.
    
    Parameters:
    -----------
    theta : float or array_like
        Homodyne detection phase in radians.
    r1, r2 : float
        Gains of the first and second OPAs (squeezing parameters).
    mu : float
        Transmission coefficient for on-chip loss.
    eta : float
        Detection efficiency.
    phi1, phi2 : float
        Pump phases of the first and second OPAs in radians.
        
    Returns:
    --------
    power : float or array_like
        The normalized mean squared photocurrent power < |I_theta(v)|^2 >.
    """
    # Calculate Trigonometric/Hyperbolic components
    sin_r1, cosh_r1 = np.sinh(r1), np.cosh(r1)
    sin_r2, cosh_r2 = np.sinh(r2), np.cosh(r2)
    
    # Expression for <a2_dag a2>
    # Term 1: mu * sinh^2(r1) * cosh(2*r2)
    term1 = mu * (sin_r1**2) * np.cosh(2 * r2)
    
    # Term 2: sinh^2(r2)
    term2 = sin_r2**2
    
    # Term 3: 0.5 * mu * sinh(2*r1) * sinh(2*r2) * cos(phi1 + phi2)
    term3 = 0.5 * mu * np.sinh(2 * r1) * np.sinh(2 * r2) * np.cos(phi1 + phi2)
    
    n_a2 = term1 + term2 + term3
    
    # Expression for <a2^2>
    # Calculate complex components
    # C1 = mu * sinh(r1) * cosh(r1) * (cosh^2(r2) * e^(i*phi1) + sinh^2(r2) * e^(i*(phi2-phi1)))
    part_real = mu * sin_r1 * cosh_r1 * ( (cosh_r2**2) * np.exp(1j * phi1) + (sin_r2**2) * np.exp(1j * (phi2 - phi1)) )
    
    # C2 = e^(i*phi2) * sinh(r2) * cosh(r2) * (1 + 2 * mu * sinh^2(r1))
    part_imag_term = np.exp(1j * phi2) * sin_r2 * cosh_r2 * (1 + 2 * mu * (sin_r1**2))
    
    a2_sq = part_real + part_imag_term
    
    # Calculate total power
    # Power = 1 + 2*eta * N_a2 + 2*eta * Re[ e^(2*i*theta) * a2_sq ]
    oscillating_term = 2 * eta * np.real(np.exp(2j * theta) * a2_sq)
    
    power = 1 + 2 * eta * n_a2 + oscillating_term
    
    return power

def calculate_extrema(r1, r2, mu, eta, phi1, phi2):
    """
    Calculate the maximum squeezed and anti-squeezed values 
    assuming the phase condition phi2 - phi1 = pi is met.
    
    Parameters are the same as photocurrent_power.
    """
    # Check phase condition
    if not np.isclose(phi2 - phi1, np.pi):
        print("Warning: phi2 - phi1 is not exactly pi. General extrema calculation not implemented, returning min/max of full sweep.")
        # Fallback to sweep if phase condition is not met
        theta_vals = np.linspace(0, 2*np.pi, 10000)
        p_vals = photocurrent_power(theta_vals, r1, r2, mu, eta, phi1, phi2)
        return np.min(p_vals), np.max(p_vals)

    # Formula derived in the solution for phi2 - phi1 = pi
    # C = 0.5 * mu * sinh(2*r1) - 0.5 * sinh(2*r2) * (1 + 2*mu*sinh^2(r1))
    C = 0.5 * mu * np.sinh(2 * r1) - 0.5 * np.sinh(2 * r2) * (1 + 2 * mu * (np.sinh(r1)**2))
    
    # Base term: 1 + 2*eta * [ mu*sinh^2(r1)*cosh(2*r2) + sinh^2(r2) - 0.5*mu*sinh(2*r1)*sinh(2*r2)*cos(2*phi1) ]
    base_term = 1 + 2 * eta * (
        mu * (np.sinh(r1)**2) * np.cosh(2 * r2) + 
        (np.sinh(r2)**2) - 
        0.5 * mu * np.sinh(2 * r1) * np.sinh(2 * r2) * np.cos(2 * phi1)
    )
    
    # Oscillation magnitude: 2*eta * |C|
    osc_amp = 2 * eta * np.abs(C)
    
    # Max Squeezed (Minimum Power)
    min_power = base_term - osc_amp
    
    # Anti-Squeezed (Maximum Power)
    max_power = base_term + osc_amp
    
    return min_power, max_power

if __name__ == "__main__":
    # 1. Setup Parameters based on the "Suggested Realistic Starting Parameters"
    r1 = 1.0
    r2 = 1.0
    mu = 0.85
    eta = 0.90
    phi1 = 0
    phi2 = np.pi  # Condition: phi2 - phi1 = pi

    # 2. Calculate Extrema
    sq_val, anti_sq_val = calculate_extrema(r1, r2, mu, eta, phi1, phi2)
    
    print(f"Parameters: r1={r1}, r2={r2}, mu={mu}, eta={eta}, phi2-phi1={phi2-phi1}")
    print(f"Maximum Squeezed Power (Min Variance) : {sq_val:.6f}")
    print(f"Anti-Squeezed Power (Max Variance)    : {anti_sq_val:.6f}")
    print(f"Vacuum Level                          : 1.000000")
    
    # 3. Plot the Phase Dependence
    theta_range = np.linspace(0, 2*np.pi, 500)
    power_vals = photocurrent_power(theta_range, r1, r2, mu, eta, phi1, phi2)
    
    plt.figure(figsize=(10, 6))
    plt.plot(theta_range, power_vals, label=r'$\langle |I_{\theta}(\nu)|^2 \rangle$', color='blue', linewidth=2)
    plt.axhline(y=1, color='gray', linestyle='--', label='Vacuum Level')
    plt.axhline(y=sq_val, color='green', linestyle=':', label=f'Min Squeezed: {sq_val:.3f}')
    plt.axhline(y=anti_sq_val, color='red', linestyle=':', label=f'Max Anti-Squeezed: {anti_sq_val:.3f}')
    
    plt.title(r'Photocurrent Sideband Power vs. Homodyne Angle $\theta$')
    plt.xlabel(r'Homodyne Angle $\theta$ (radians)')
    plt.ylabel(r'Normalized Power $\langle |I_{\theta}(\nu)|^2 \rangle$')
    plt.grid(True, alpha=0.3)
    plt.legend()
    
    # Annotation for phases
    plt.annotate('$\phi_2 - \phi_1 = \pi$', xy=(0.5, 0.9), xycoords='axes fraction', 
                 ha='center', fontsize=12, bbox=dict(facecolor='white', alpha=0.8))
    
    plt.show()
```
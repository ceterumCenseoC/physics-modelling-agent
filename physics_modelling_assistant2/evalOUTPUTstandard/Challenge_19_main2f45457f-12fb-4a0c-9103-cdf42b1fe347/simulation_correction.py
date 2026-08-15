
```python
import numpy as np
import matplotlib.pyplot as plt

def calculate_cascaded_opa_variance(r1, r2, mu, eta, theta, phi1, phi2):
    """
    Calculates the mean squared power of the photocurrent's sideband 
    for the cascaded OPA system.

    Parameters:
    r1 (float): Gain parameter of the first OPA (squeezing factor).
    r2 (float): Gain parameter of the second OPA (squeezing factor).
    mu (float): Transmission coefficient of the loss between OPAs.
    eta (float): Detection efficiency.
    theta (float or np.array): Detection phase (local oscillator phase).
    phi1 (float): Pump phase of the first OPA.
    phi2 (float): Pump phase of the second OPA.

    Returns:
    float or np.array: The mean squared power < |I_theta|^2 >.
    """
    delta_phi = phi2 - phi1
    
    # Hyperbolic functions
    c1, s1 = np.cosh(r1), np.sinh(r1)
    c2, s2 = np.cosh(r2), np.sinh(r2)
    
    # Trigonometric functions of phase difference
    cos_dp = np.cos(delta_phi)
    sin_dp = np.sin(delta_phi)
    
    # --- Coefficient Magnitudes and Components ---
    # A = sqrt(mu) * (c1*c2 + e^(i*delta_phi)*s1*s2)
    # B = sqrt(mu) * e^(i*phi1) * (s1*c2 + e^(i*delta_phi)*c1*s2)
    
    # |B|^2 calculation
    # B_component = s1*c2 + e^(i*delta_phi)*c1*s2
    # Re(B_comp) = s1*c2 + cos_dp*c1*s2
    # Im(B_comp) = sin_dp*c1*s2
    # |B|^2 = mu * (|B_comp|^2)
    
    re_b = s1 * c2 + cos_dp * c1 * s2
    im_b = sin_dp * c1 * s2
    abs_b_sq = mu * (re_b**2 + im_b**2)
    
    # --- Noise Channel Contribution ---
    # D = sqrt(1-mu) * e^(i*phi2) * s2
    # |D|^2 = (1-mu) * s2^2
    abs_d_sq = (1 - mu) * (s2**2)
    
    # Photon Number Term <n>
    photon_number_term = abs_b_sq + abs_d_sq
    
    # --- Correlation Term <a^2> ---
    # <a_out^2> = A*B + C*D
    
    # Term 1: A*B
    # We need the complex phase of this term to rotate by e^(-2i theta).
    # A = sqrt(mu) * (X)
    # B = sqrt(mu) * e^(i*phi1) * (Y)
    # AB = mu * e^(i*phi1) * X * Y
    
    # X = c1*c2 + e^(i*delta_phi)*s1*s2
    re_x = c1 * c2 + cos_dp * s1 * s2
    im_x = sin_dp * s1 * s2
    
    # Y = re_b + i*im_b (calculated above)
    
    # Complex multiplication X*Y
    XY_re = re_x * re_b - im_x * im_b
    XY_im = re_x * im_b + im_x * re_b
    
    # Rotate AB by phi1
    # AB_real = mu * (XY_re * cos(phi1) - XY_im * sin(phi1))
    # AB_imag = mu * (XY_re * sin(phi1) + XY_im * cos(phi1))
    
    AB_re = mu * (XY_re * np.cos(phi1) - XY_im * np.sin(phi1))
    AB_im = mu * (XY_re * np.sin(phi1) + XY_im * np.cos(phi1))
    
    # Term 2: C*D
    # C = sqrt(1-mu) * c2
    # D = sqrt(1-mu) * e^(i*phi2) * s2
    # CD = (1-mu) * e^(i*phi2) * c2 * s2
    # Since c2*s2 is real:
    CD_re = (1 - mu) * c2 * s2 * np.cos(phi2)
    CD_im = (1 - mu) * c2 * s2 * np.sin(phi2)
    
    # Total <a^2>
    a2_re = AB_re + CD_re
    a2_im = AB_im + CD_im
    
    # Correlation term in variance: 2 * Re[ <a^2> e^(-2i theta) ]
    # Re[ (a2_re + i a2_im) * (cos(-2t) + i sin(-2t)) ]
    # = a2_re * cos(2t) + a2_im * sin(2t)
    
    correlation_term = 2 * (a2_re * np.cos(2 * theta) + a2_im * np.sin(2 * theta))
    
    # Total Ideal Variance
    # <I^2> = 1 + 2<n> + corr_term
    variance_ideal = 1 + 2 * photon_number_term + correlation_term
    
    # Apply Detection Efficiency
    # V_meas = eta * V_ideal + (1 - eta)
    variance_measured = eta * variance_ideal + (1 - eta)
    
    return variance_measured

def calculate_extrema(r1, r2, mu, eta):
    """
    Calculates the analytical maximum (anti-squeezed) and minimum (squeezed) 
    values based on the derived formulas for phi2 - phi1 = pi.
    """
    # Maximum Anti-squeezed Value (Max Variance)
    # Condition: cos(phi1 - 2*theta) = 1
    # V_max = eta [ mu * exp(2(r1-r2)) + (1-mu) * exp(-2r2) ] + (1-eta)
    v_max_ideal = mu * np.exp(2 * (r1 - r2)) + (1 - mu) * np.exp(-2 * r2)
    v_max = eta * v_max_ideal + (1 - eta)
    
    # Maximum Squeezed Value (Min Variance)
    # Condition: cos(phi1 - 2*theta) = -1
    # V_min = eta [ mu * exp(-2(r1-r2)) + (1-mu) * exp(2r2) ] + (1-eta)
    v_min_ideal = mu * np.exp(-2 * (r1 - r2)) + (1 - mu) * np.exp(2 * r2)
    v_min = eta * v_min_ideal + (1 - eta)
    
    return v_min, v_max

def main():
    # --- Realistic Starting Parameters ---
    r1 = 1.0
    r2 = 0.5
    mu = 0.90
    eta = 0.90
    phi1 = 0.0
    phi2 = np.pi # Condition: phi2 - phi1 = pi
    
    # --- Calculation of Extrema ---
    v_min, v_max = calculate_extrema(r1, r2, mu, eta)
    
    print(f"--- System Parameters ---")
    print(f"r1: {r1}, r2: {r2}")
    print(f"On-chip transmission (mu): {mu}")
    print(f"Detection efficiency (eta): {eta}")
    print(f"Phase difference (phi2-phi1): {phi2-phi1}")
    
    print(f"\n--- Results for phi2 - phi1 = pi ---")
    print(f"Maximum Squeezed Value (Min Variance): {v_min:.4f} ({10*np.log10(v_min):.2f} dB)")
    print(f"Maximum Anti-squeezed Value (Max Variance): {v_max:.4f} ({10*np.log10(v_max):.2f} dB)")

    # --- Visualization ---
    theta_range = np.linspace(0, 2*np.pi, 500)
    variances = calculate_cascaded_opa_variance(r1, r2, mu, eta, theta_range, phi1, phi2)
    
    # Convert to dB for plotting
    variances_db = 10 * np.log10(variances)
    
    plt.figure(figsize=(10, 6))
    plt.plot(theta_range, variances_db, label=r'$\langle |I_{\theta}|^2 \rangle$')
    plt.axhline(10*np.log10(v_min), color='g', linestyle='--', label='Calculated Minimum (Squeezed)')
    plt.axhline(10*np.log10(v_max), color='r', linestyle='--', label='Calculated Maximum (Anti-squeezed)')
    plt.axhline(0, color='k', linestyle=':', label='Shot Noise (Vacuum)')
    
    plt.title('Photocurrent Noise Power vs Detection Phase\nCascaded OPAs ($\phi_2 - \phi_1 = \pi$)')
    plt.xlabel(r'Detection Phase $\theta$ (radians)')
    plt.ylabel('Noise Power (dB)')
    plt.grid(True, alpha=0.3)
    plt.legend()
    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    main()
```

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
    
    # Intermediate coefficients for bogoliubov transformation
    # We use the explicit general form derived in the text before setting phi_diff=pi
    
    # Coefficients A, B for the input vacuum mode a_in
    # A = sqrt(mu) * (cosh(r1)*cosh(r2) + exp(i*delta_phi)*sinh(r1)*sinh(r2))
    # B = sqrt(mu) * exp(i*phi1) * (sinh(r1)*cosh(r2) + exp(i*delta_phi)*cosh(r1)*sinh(r2))
    
    # Coefficients C, D for the intermediate vacuum mode v
    # C = sqrt(1-mu) * cosh(r2)
    # D = sqrt(1-mu) * exp(i*phi2) * sinh(r2)
    
    # Expectation values
    # <n> = |B|^2 + |D|^2
    # <a^2> = AB + CD (since <a_in^2> = <v^2> = 0, but <a a^+> = 1 contributes to AB and CD terms)
    # Note on AB and CD: In the expansion a_out^2, the terms <a_in a_in^+> and <v v^+> give 1.
    # Specifically, <a_out^2> = A*B + C*D. (Conjugates don't matter for the magnitude in the sum AB+CD* correctly)
    # Based on detailed derivation:
    # <n> = |B|^2 + |D|^2
    # <a_out^2> = AB + CD (assuming 2|B|^2 etc factor in variance formula)
    
    # Let's use the exponential form for robustness
    # |B|^2 = mu * |sinh(r1)cosh(r2) + e^(i dPhi) cosh(r1)sinh(r2)|^2
    # Complex number B_mag = sinh(r1)cosh(r2) + cos(dPhi)cosh(r1)sinh(r2) + i sin(dPhi)cosh(r1)sinh(r2)
    
    cos_dp = np.cos(delta_phi)
    sin_dp = np.sin(delta_phi)
    
    # Calculate |B|^2
    # Re = s1 c2 + cdp c1 s2
    # Im = sdp c1 s2
    # |z|^2 = Re^2 + Im^2
    c1, s1 = np.cosh(r1), np.sinh(r1)
    c2, s2 = np.cosh(r2), np.sinh(r2)
    
    term1 = s1 * c2
    term2 = c1 * s2
    
    re_b = term1 + cos_dp * term2
    im_b = sin_dp * term2
    abs_b_sq = mu**2 * (re_b**2 + im_b**2) # wait, B definition had sqrt(mu) outside
    # B = sqrt(mu) * e^(i phi1) * ( ... )
    # So |B|^2 = mu * ( ... )
    abs_b_sq = mu * (re_b**2 + im_b**2)
    
    # Calculate |D|^2
    # D = sqrt(1-mu) e^(i phi2) sinh(r2)
    # |D|^2 = (1-mu) sinh^2(r2)
    abs_d_sq = (1 - mu) * (s2**2)
    
    photon_number_term = abs_b_sq + abs_d_sq
    
    # Calculate Re[ <a_out^2> e^(-2 i theta) ]
    # <a_out^2> = A B + C D
    
    # A = sqrt(mu) (c1 c2 + e^(i dPhi) s1 s2)
    re_a = c1 * c2 + cos_dp * s1 * s2
    im_a = sin_dp * s1 * s2
    
    # AB = mu * e^(i phi1) * ( (c1 c2 + e^(i dPhi) s1 s2) * (s1 c2 + e^(i dPhi) c1 s2)* ) <-- careful with conjugates
    # A = sqrt(mu) * Z_a
    # B = sqrt(mu) * e^(i phi1) * Z_b
    # AB = mu * e^(i phi1) * Z_a * Z_b    <-- Note: B does not have conjugate in <a^2>
    # Wait, derivation <a^2> term in <I^2> = 2 Re[ <a^2> e^(-2i theta) ]
    # <a_out^2> = A^2 <a a> + B^2 <a+ a+> + AB (<a a+> + <a+ a>) ? No.
    # a_out = A a + B a+
    # a_out^2 = A^2 a^2 + B^2 (a+)^2 + AB (a a+ + a+ a)
    # <a a> = 0, <(a+)^2> = 0.
    # <a a+> = 1, <a+ a> = 0.
    # So <a_out^2> = AB * 1.
    # Correct.
    
    # A = sqrt(mu) * X
    # B = sqrt(mu) * e^(i phi1) * Y
    # AB = mu * e^(i phi1) * X * Y
    
    # C = sqrt(1-mu) * c2
    # D = sqrt(1-mu) * e^(i phi2) * s2
    # CD = (1-mu) * e^(i phi2) * c2 * s2
    
    # Total <a_out^2> = mu e^(i phi1) X Y + (1-mu) e^(i phi2) c2 s2
    # We need Re[ <a_out^2> e^(-2 i theta) ]
    
    # Term 1 magnitude and phase
    # X Y is complex.
    X_re = re_a
    X_im = im_a
    Y_re = re_b
    Y_im = im_b
    
    # X * Y = (Xr + i Xi)(Yr + i Yi) = XrYr - XiYi + i(XrYi + XiYr)
    XY_re = X_re * Y_re - X_im * Y_im
    XY_im = X_re * Y_im + X_im * Y_re
    
    # Term 1 phase addition: e^(i phi1)
    T1_mag = mu
    T1_re = T1_mag * (XY_re * np.cos(phi1) - XY_im * np.sin(phi1))
    T1_im = T1_mag * (XY_re * np.sin(phi1) + XY_im * np.cos(phi1))
    
    # Term 2 magnitude and phase
    # e^(i phi2) * c2 * s2. c2*s2 is real.
    T2_mag = (1 - mu) * c2 * s2
    T2_re = T2_mag * np.cos(phi2)
    T2_im = T2_mag * np.sin(phi2)
    
    # Sum <a_out^2>
    a2_re = T1_re + T2_re
    a2_im = T1_im + T2_im
    
    # Rotate by -2 theta
    # Re[ (a2_re + i a2_im) * (cos(-2t) + i sin(-2t)) ]
    # = Re[ Z * (cos(2t) - i sin(2t)) ]
    # = a2_re cos(2t) + a2_im sin(2t)
    
    correlation_term = 2 * (a2_re * np.cos(2 * theta) + a2_im * np.sin(2 * theta))
    
    # Total Variance
    # <I^2> = 1 + 2 <n> + correlation_term
    variance = 1 + 2 * photon_number_term + correlation_term
    
    # Apply detection efficiency
    # V_det = eta * V_ideal + (1 - eta)
    detected_variance = eta * variance + (1 - eta)
    
    return detected_variance

def calculate_extrema(r1, r2, mu, eta):
    """
    Calculates the analytical maximum (anti-squeezed) and minimum (squeezed) 
    values based on the derived formulas for phi2 - phi1 = pi.
    """
    # Anti-squeezed: V_max = eta [ mu * exp(2(r1-r2)) + (1-mu) * exp(-2r2) ] + (1-eta)
    v_max_ideal = mu * np.exp(2 * (r1 - r2)) + (1 - mu) * np.exp(-2 * r2)
    v_max = eta * v_max_ideal + (1 - eta)
    
    # Squeezed: V_min = eta [ mu * exp(-2(r1-r2)) + (1-mu) * exp(2r2) ] + (1-eta)
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
    
    # --- Calculation Extrema ---
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
    plt.axhline(10*np.log10(v_min), color='g', linestyle='--, label='Calculated Minimum (Squeezed)')
    plt.axhline(10*np.log10(v_max), color='r', linestyle='--, label='Calculated Maximum (Anti-squeezed)')
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
```python
import numpy as np
import scipy.optimize
from scipy.special import spherical_jn
import matplotlib.pyplot as plt

def compute_cavity_shift():
    """
    Computes the dimensionless cavity shift for an electron in a spherical 
    conducting cavity using non-relativistic quantum mechanics.
    
    Model based on:
    Brown, L. S., Helmerson, K., & Tan, J. (1986). Cyclotron motion in a spherical microwave cavity. 
    Physical Review A, 34(4), 2638.
    """
    
    print("--- Cavity Shift Calculation ---")
    
    # --- 1. Physical Constants (CODATA 2018) ---
    m_e = 9.1093837015e-31       # kg (electron mass)
    e_charge = 1.602176634e-19   # C (elementary charge)
    c = 2.99792458e8             # m/s (speed of light)
    hbar = 1.054571817e-34       # J*s (reduced Planck constant)
    epsilon_0 = 8.8541878128e-12 # F/m (vacuum permittivity)
    
    # Derived constant: Fine structure constant (alpha)
    # alpha = e^2 / (4 * pi * epsilon_0 * hbar * c)
    alpha = e_charge**2 / (4 * np.pi * epsilon_0 * hbar * c)
    
    # --- 2. System Parameters ---
    R = 0.01                     # m (Cavity radius = 1 cm)
    B = 5.0                      # T (Magnetic field)
    
    # --- 3. Derived Frequencies ---
    # Classical cyclotron frequency: omega_c = eB / m
    omega_c_0 = (e_charge * B) / m_e
    f_c_0 = omega_c_0 / (2 * np.pi)
    
    print(f"System Configuration:")
    print(f"  B-field: {B} T")
    print(f"  Cavity Radius: {R} m")
    print(f"  Cyclotron Frequency (fc): {f_c_0/1e9:.2f} GHz")
    print(f"  Fine structure constant: {alpha:.5f}")
    
    # --- 4. Cavity Mode Calculation ---
    # We need roots u'_1p of d/dr [r * j1(r)] = 0 for TM_{1p} modes.
    
    def d_dx_xj1(x):
        # Analytic derivative of x * j1(x)
        # j1(x) derivative: j1'(x) = j0(x) - (2/x) * j1(x)
        # Let f(x) = x * j1(x). f'(x) = j1(x) + x * j1'(x)
        # f'(x) = j1(x) + x * (j0(x) - 2/x * j1(x)) = j1(x) + x*j0(x) - 2*j1(x) = x*j0(x) - j1(x)
        return x * spherical_jn(0, x) - spherical_jn(1, x)

    # Define search range for roots. 
    # For R=1cm, modes extend into几百GHz. We search up to ~300GHz to capture convergence.
    # omega_max = 2*pi*f_max. u = omega * R / c.
    f_target_max = 300e9 # Hz
    omega_max = 2 * np.pi * f_target_max
    u_max = omega_max * R / c
    
    # Find roots using sign changes on a dense grid
    u_vals = np.linspace(0.1, u_max, 200000)
    y_vals = d_dx_xj1(u_vals)
    
    # Identify indices where sign changes occur
    sign_changes = np.where(np.sign(y_vals[:-1]) != np.sign(y_vals[1:]))[0]
    
    u_roots = []
    for idx in sign_changes:
        u_low = u_vals[idx]
        u_high = u_vals[idx+1]
        # Refine root using Brent's method
        try:
            root = scipy.optimize.brentq(d_dx_xj1, u_low, u_high, xtol=1e-14, rtol=1e-14)
            u_roots.append(root)
        except ValueError:
            # Should not happen with sign change, but catch for safety
            continue

    u_roots = np.array(u_roots)
    
    # --- 5. Calculate Contributions ---
    
    # Prefactor formula derived from Natural Units to SI conversion:
    # Delta_omega / omega = (3 * alpha) / (2 * m_e * R) * Sum(...)
    # In SI, replace 1/(m_e R) with hbar / (m_e R c)
    prefactor = (3 * alpha * hbar) / (2 * m_e * R * c)
    
    print(f"\n--- Calculating Mode Contributions ---")
    print(f"Prefactor: {prefactor:.3e}")
    
    contributions = []
    mode_freqs = []
    
    for p, u_p in enumerate(u_roots):
        # Mode frequency in Hz
        omega_p = c * u_p / R
        f_p = omega_p / (2 * np.pi)
        mode_freqs.append(f_p)
        
        # Dimensionless detuning parameter x_p = omega_c * R / (c * u_p)
        x_p = omega_c_0 * R / (c * u_p)
        x_p_sq = x_p**2
        
        # Calculate Mode Shape Factor F_p
        # F_p = -u_p^5 * j_1(u_p) / D_p
        j1_up = spherical_jn(1, u_p)
        num_F = - (u_p**5) * j1_up
        
        # Denominator D_p from normalization integral
        # D_p = u^4 + (2u - 0.5u^3)sin(2u) - (1+cos(2u))u^2 - 1 + cos(2u)
        sin_2u = np.sin(2 * u_p)
        cos_2u = np.cos(2 * u_p)
        
        term1 = u_p**4
        term2 = (2*u_p - 0.5*u_p**3) * sin_2u
        term3 = (1 + cos_2u) * u_p**2
        term4 = -1 + cos_2u
        
        denom_D = term1 + term2 - term3 + term4
        
        F_p = num_F / denom_D
        
        # Calculate term inside the sum: F_p * x_p^2 / (1 - x_p^2)
        # Note: Since x_p != 1 exactly for these parameters, division is safe.
        sum_term = F_p * x_p_sq / (1 - x_p_sq)
        
        # Contribution to the shift
        contrib = prefactor * sum_term
        contributions.append(contrib)
        
        # Analyze near-resonant modes and first few for sanity check
        detuning = f_p - f_c_0
        if p < 3 or abs(detuning) < 20e9:
             print(f"Mode {p+1:2d}: u={u_p:7.4f}, f={f_p/1e9:7.2f} GHz, "
                   f"detuning={detuning/1e9:6.2f} GHz, x^2={x_p_sq:6.3f}, "
                   f"F_p={F_p:6.3f}, contrib={contrib:.3e}")

    # --- 6. Final Result ---
    total_shift = np.sum(contributions)
    
    print(f"\n--- Final Result ---")
    print(f"Total dimensionless cavity shift: {total_shift:.3e}")
    
    # --- 7. Visualization ---
    
    # Plot 1: Mode Spectrum
    plt.figure(figsize=(10, 5))
    p_indices = np.arange(1, len(mode_freqs) + 1)
    plt.bar(p_indices, np.array(mode_freqs)/1e9, color='skyblue', label='TM Modes', alpha=0.7)
    plt.axhline(f_c_0/1e9, color='red', linestyle='--', linewidth=2, label='Cyclotron Freq')
    plt.xlabel('Mode Index ($p$)')
    plt.ylabel('Frequency (GHz)')
    plt.title('TM$_{1p}$ Mode Spectrum in 1 cm Spherical Cavity')
    plt.legend()
    plt.grid(axis='y', alpha=0.5)
    plt.tight_layout()
    
    # Plot 2: Convergence
    plt.figure(figsize=(10, 5))
    cumulative_shift = np.cumsum(contributions)
    plt.semilogy(p_indices, np.abs(cumulative_shift), marker='o', linestyle='-', markersize=4)
    plt.xlabel('Number of Modes ($N$)')
    plt.ylabel('$|\Delta\omega_c / \omega_c|$')
    plt.title('Convergence of Cavity Shift Summation')
    plt.grid(True, which="both", ls="-", alpha=0.3)
    plt.tight_layout()
    
    plt.show()

    return total_shift

if __name__ == "__main__":
    result = compute_cavity_shift()
```
```python
import numpy as np
import matplotlib.pyplot as plt
from scipy.special import spherical_jn

def compute_cavity_shift():
    """
    Computes the dimensionless cavity shift for an electron in a spherical 
    conducting cavity using non-relativistic quantum mechanics.
    
    Model based on:
    Brown, L. S., Helmerson, K., & Tan, J. (1986). Cyclotron motion in a spherical microwave cavity. 
    Physical Review A, 34(4), 2638.
    """
    
    print("--- Cavity Shift Calculation ---")
    
    # --- 1. Physical Constants ---
    # CODATA 2018 values
    m_e = 9.1093837015e-31    # kg (electron mass)
    e_charge = 1.602176634e-19 # C (elementary charge)
    c = 2.99792458e8          # m/s (speed of light)
    hbar = 1.054571817e-34    # J*s (reduced Planck constant)
    epsilon_0 = 8.8541878128e-12 # F/m (vacuum permittivity)
    alpha = e_charge**2 / (4 * np.pi * epsilon_0 * hbar * c) # Fine-structure constant
    
    # --- 2. System Parameters ---
    R = 0.01                  # m (Cavity radius = 1 cm)
    B = 5.0                   # T (Magnetic field)
    
    # --- 3. Derived Frequencies ---
    omega_c_0 = (e_charge * B) / m_e  # Classical cyclotron frequency (rad/s)
    f_c_0 = omega_c_0 / (2 * np.pi)   # Cyclotron frequency (Hz)
    
    print(f"B-field: {B} T")
    print(f"Cavity Radius: {R} m")
    print(f"Cyclotron Frequency (fc): {f_c_0/1e9:.2f} GHz")
    print(f"Fine structure constant: {alpha:.5f}")
    
    # --- 4. Cavity Mode Calculation ---
    # We need to find roots u_{1p}' of d/dr [r * j1(r)] = 0.
    # These correspond to the TM_{1p} modes in a spherical cavity.
    
    def d_dx_xj1(x):
        # Analytic derivative of x * j1(x)
        # j_n(x) derivative: d/dx j_n(x) = j_{n-1}(x) - (n+1)/x * j_n(x)
        # Let f(x) = x * j1(x). f'(x) = j1(x) + x * j1'(x)
        # j1'(x) = j0(x) - 2/x * j1(x)
        # f'(x) = j1(x) + x * (j0(x) - 2/x * j1(x)) = j1(x) + x*j0(x) - 2*j1(x) = x*j0(x) - j1(x)
        return x * spherical_jn(0, x) - spherical_jn(1, x)

    # Define range to search for roots. We need enough modes to bracket omega_c_0.
    # Max frequency ~ 300 GHz is sufficient to find dominant modes
    f_max = 300e9 # Hz
    omega_max = 2 * np.pi * f_max
    # u = omega * R / c
    u_max = omega_max * R / c
    
    # Create a dense grid to find sign changes
    u_vals = np.linspace(0.1, u_max, 100000)
    y_vals = d_dx_xj1(u_vals)
    
    # Find indices where sign changes
    sign_changes = np.where(np.sign(y_vals[:-1]) != np.sign(y_vals[1:]))[0]
    
    roots = []
    for idx in sign_changes:
        # Refine root using Brent's method (brentq) on the interval
        u_low = u_vals[idx]
        u_high = u_vals[idx+1]
        try:
            root = scipy.optimize.brentq(d_dx_xj1, u_low, u_high, xtol=1e-14)
            roots.append(root)
        except ValueError:
            continue

    u_roots = np.array(roots)
    
    # --- 5. Mode Convergence Studies ---
    
    # Calculate contribution for each mode
    # Formula from text (Eq. derived from Ref [2] and [3]):
    # Contribution = (3 * alpha * hbar) / (2 * m_e * R * c) * (F_p * x_p^2 / (1 - x_p^2))
    
    # Prefactor calculation (SI units)
    # Note: The derivation used Natural Units. 
    # In SI, alpha/(m_e R) becomes alpha * hbar / (m_e * R * c) because of length conversions.
    prefactor = (3 * alpha * hbar) / (2 * m_e * R * c)
    
    print(f"\n--- Calculating Contributions (Prefactor ~ {prefactor:.3e}) ---")
    
    contributions = []
    mode_freqs = []
    coupling_terms = []
    
    for p, u_p in enumerate(u_roots):
        omega_p = c * u_p / R
        f_p = omega_p / (2 * np.pi)
        
        # Dimensionless detuning x_p = omega_c * R / (c * u_p)
        x_p = omega_c_0 * R / (c * u_p)
        x_p_sq = x_p**2
        
        # Calculate F_p (Mode Shape Factor)
        # F_p = -u_p^5 * j_1(u_p) / D_p
        j1_up = spherical_jn(1, u_p)
        num_F = - (u_p**5) * j1_up
        
        # Denominator D_p calculation
        # D_p = u^4 + (2u - 0.5u^3)sin(2u) - (1+cos(2u))u^2 - 1 + cos(2u)
        sin_2u = np.sin(2 * u_p)
        cos_2u = np.cos(2 * u_p)
        
        term1 = u_p**4
        term2 = (2*u_p - 0.5*u_p**3) * sin_2u
        term3 = (1 + cos_2u) * u_p**2
        term4 = -1 + cos_2u
        
        denom_D = term1 + term2 - term3 + term4
        
        F_p = num_F / denom_D
        
        # Calculate the term inside the sum: F_p * x_p^2 / (1 - x_p^2)
        try:
            # Handle potential division by zero if x_p is exactly 1 (resonance)
            sum_term = F_p * x_p_sq / (1 - x_p_sq)
        except ZeroDivisionError:
            print(f"Warning: Division by zero for mode p={p+1} (u={u_p:.2f}) - exact resonance.")
            sum_term = 0 
            
        # Final contribution for this mode
        contrib = prefactor * sum_term
        
        contributions.append(contrib)
        mode_freqs.append(f_p)
        coupling_terms.append(sum_term)
        
        # Print details for modes close to resonance and first few
        if p < 3 or (abs(f_p - f_c_0) < 20e9):
             print(f"Mode p={p+1:2d}: u={u_p:7.4f}, f={f_p/1e9:7.2f} GHz, "
                   f"x^2={x_p_sq:6.3f}, F_p={F_p:6.3f}, contrib={contrib:.3e}")

    # --- 6. Total Shift ---
    total_shift = np.sum(contributions)
    
    print(f"\n--- Final Result ---")
    print(f"Total dimensionless cavity shift: {total_shift:.3e}")
    
    # --- 7. Visualization ---
    
    # Plot 1: Mode Spectrum vs Cyclotron Frequency
    plt.figure(figsize=(10, 6))
    p_indices = np.arange(1, len(mode_freqs) + 1)
    plt.bar(p_indices, np.array(mode_freqs)/1e9, color='skyblue', label='TM Modes')
    plt.axhline(f_c_0/1e9, color='red', linestyle='--', linewidth=2, label='Cyclotron Freq ($\omega_c$)')
    plt.xlabel('Mode Index ($p$)', fontsize=12)
    plt.ylabel('Frequency (GHz)', fontsize=12)
    plt.title('Cavity Mode Spectrum vs. Cyclotron Frequency', fontsize=14)
    plt.legend()
    plt.grid(axis='y', alpha=0.3)
    plt.tight_layout()
    plt.show()
    
    # Plot 2: Convergence of the Sum
    cumulative_shift = np.cumsum(contributions)
    
    plt.figure(figsize=(10, 6))
    plt.semilogy(p_indices, np.abs(cumulative_shift), marker='o', linestyle='-', color='blue')
    plt.xlabel('Number of Modes Included ($N$)', fontsize=12)
    plt.ylabel('Magnitude of Cumulative Shift', fontsize=12)
    plt.title('Convergence of Cavity Shift Summation', fontsize=14)
    plt.grid(True, which="both", ls="-", alpha=0.3)
    plt.tight_layout()
    plt.show()

    return total_shift

# Run the calculation
if __name__ == "__main__":
    import scipy.optimize
    result = compute_cavity_shift()
```
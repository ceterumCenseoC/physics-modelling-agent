```python
import numpy as np
import matplotlib.pyplot as plt

# -----------------------------------------------------------------------------
# Model Implementation: Finite-Size Correction for 2D Electron Gas
# Based on Holzmann et al., Phys. Rev. B 94, 035126 (2016)
# -----------------------------------------------------------------------------

def finite_size_correction_2deg(N, r_s):
    """
    Calculates the leading-order finite-size energy correction per electron
    for the 2D electron gas (2DEG).

    Formula:
    Delta E = hbar * omega_p / (2 * N)
    
    For 2D, the plasma frequency omega_p is wavevector dependent:
    omega_p(k) = sqrt( (2 * pi * n * e^2 * k) / m_e )
    
    In Hartree Atomic Units (hbar = m_e = e = a_B = 1):
    omega_p(k) = sqrt(2 * pi * n * k)
    
    The correction is evaluated at the smallest non-zero wavevector k_min,
    where k_min = 2*pi/L and L = r_s * sqrt(N*pi).
    
    Substituting n and k_min leads to:
    Delta E = pi^(1/4) / (r_s^(3/2) * N^(5/4))

    Parameters:
    N (float or int): Number of electrons
    r_s (float): Wigner-Seitz radius

    Returns:
    float: Energy correction in Hartree per electron
    """
    # calculating PI^(1/4) once, though trivial for numpy
    pi_pow_1_4 = np.pi ** (0.25)
    
    # N to the power of 5/4
    # N^(5/4) = N^(1.25)
    N_pow_5_4 = N ** (1.25)
    
    # r_s to the power of 3/2
    # r_s^(3/2) = r_s * sqrt(r_s)
    r_s_pow_3_2 = r_s ** (1.5)
    
    # Apply formula
    delta_E = pi_pow_1_4 / (r_s_pow_3_2 * N_pow_5_4)
    
    return delta_E

# -----------------------------------------------------------------------------
# Visualization and Analysis
# -----------------------------------------------------------------------------

def main():
    # 1. Problem Setup Parameters
    N_vals = 122
    r_s_vals = 10

    # 2. Calculate the specific required value
    correction = finite_size_correction_2deg(N_vals, r_s_vals)
    
    print("-" * 60)
    print(f"Finite-Size Correction Calculation for 2D Electron Gas")
    print("-" * 60)
    print(f"Number of electrons (N): {N_vals}")
    print(f"Wigner-Seitz radius (r_s): {r_s_vals}")
    print("-" * 60)
    print(f"Calculated Correction: {correction:.6e} Hartree")
    # Rounding to two significant digits as requested
    print(f"Rounded (2 sig figs):   {correction:.1e} Hartree")
    print("-" * 60)

    # 3. Create Graphics to visualize the scaling behavior
    # It is sensible to visualize how the correction scales with N for a fixed density
    
    N_range = np.linspace(50, 500, 50)
    corrections_range = finite_size_correction_2deg(N_range, r_s_vals)
    
    plt.figure(figsize=(10, 6))
    
    # Plot scaling with N
    plt.subplot(1, 2, 1)
    plt.plot(N_range, corrections_range, 'b-', linewidth=2, label=r'$\Delta E \propto N^{-5/4}$')
    plt.scatter([N_vals], [correction], color='red', s=100, zorder=5, label='N=122 Point')
    plt.title('Scaling of Finite-Size Error with N', fontsize=12)
    plt.xlabel('Number of Electrons (N)', fontsize=12)
    plt.ylabel(r'Correction $\Delta E$ (Hartree)', fontsize=12)
    plt.grid(True, which='both', linestyle='--', alpha=0.7)
    plt.legend()
    
    # Log-log plot to verify exponent
    plt.subplot(1, 2, 2)
    plt.loglog(N_range, corrections_range, 'k-', linewidth=2, label='Slope = -5/4')
    
    # Reference line for N^-1 comparison
    ref_slope = corrections_range[0] * (N_range[0] / N_range)
    plt.loglog(N_range, ref_slope, 'g--', alpha=0.5, label=r'$\propto N^{-1}$ (3D ref)')
    
    plt.scatter([N_vals], [correction], color='red', s=100, zorder=5)
    plt.title('Log-Log Scaling Verification', fontsize=12)
    plt.xlabel('Number of Electrons (N)', fontsize=12)
    plt.ylabel(r'Correction $\Delta E$ (Hartree)', fontsize=12)
    plt.grid(True, which='both', linestyle='--', alpha=0.7)
    plt.legend()
    
    plt.tight_layout()
    plt.savefig('2deg_finite_size_correction.png')
    plt.show()
    
    print("Plot saved as '2deg_finite_size_correction.png'")

if __name__ == "__main__":
    main()
```
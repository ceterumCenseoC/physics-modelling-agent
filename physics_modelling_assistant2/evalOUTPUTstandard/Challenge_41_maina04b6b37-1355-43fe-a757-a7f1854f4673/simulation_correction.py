```python
import numpy as np
import matplotlib.pyplot as plt

# -----------------------------------------------------------------------------
# Model Implementation: Finite-Size Correction for 2D Electron Gas
# Based on Holzmann et al., Phys. Rev. B 94, 035126 (2016)
# Reference: Drummond et al., Phys. Rev. B 78, 125106 (2008)
# -----------------------------------------------------------------------------

def finite_size_correction_2deg(N, r_s):
    """
    Calculates the leading-order finite-size energy correction per electron
    for the 2D electron gas (2DEG).

    The correction is derived from the plasmon zero-point energy:
    Delta E = hbar * omega_p / (2 * N)
    
    For 2D, the plasma frequency omega_p is wavevector dependent:
    omega_p(k) = sqrt( (2 * pi * n * e^2 * k) / m_e )
    
    In Hartree Atomic Units (hbar = m_e = e = a_B = 1):
    omega_p(k) = sqrt(2 * pi * n * k)
    
    The correction is evaluated at the smallest non-zero wavevector k_min,
    where k_min = 2*pi/L and L = r_s * sqrt(N*pi).
    
    Substituting n = 1/(pi * r_s^2) and k_min leads to:
    Delta E = pi^(1/4) / (r_s^(3/2) * N^(5/4))

    Parameters:
    N (float or int): Number of electrons
    r_s (float): Wigner-Seitz radius

    Returns:
    float: Energy correction in Hartree per electron
    """
    # Pre-calculate constant pi^(1/4)
    pi_pow_1_4 = np.pi ** 0.25
    
    # N to the power of 5/4 (N^(1.25))
    N_pow_5_4 = N ** 1.25
    
    # r_s to the power of 3/2 (r_s * sqrt(r_s))
    r_s_pow_3_2 = r_s ** 1.5
    
    # Apply derived formula
    delta_E = pi_pow_1_4 / (r_s_pow_3_2 * N_pow_5_4)
    
    return delta_E

# -----------------------------------------------------------------------------
# Main Execution and Visualization
# -----------------------------------------------------------------------------

def main():
    # Define parameters from the problem setup
    N_target = 122
    r_s_target = 10.0

    # Calculate the specific value for N=122, r_s=10
    correction_val = finite_size_correction_2deg(N_target, r_s_target)
    
    # Print results
    print("-" * 60)
    print("Finite-Size Correction Calculation for 2D Electron Gas")
    print("Reference: Holzmann et al. (2016), Drummond et al. (2008)")
    print("-" * 60)
    print(f"System Parameters:")
    print(f"  Number of electrons (N): {N_target}")
    print(f"  Wigner-Seitz radius (r_s): {r_s_target}")
    print("-" * 60)
    print(f"Results:")
    print(f"  Leading-Order Correction: {correction_val:.6e} Hartree")
    print(f"  Rounded (2 significant digits): {correction_val:.1e} Hartree")
    print("-" * 60)

    # Generate range of N values for scaling analysis
    N_range = np.linspace(50, 500, 100)
    corrections_range = finite_size_correction_2deg(N_range, r_s_target)
    
    # Setup plotting
    plt.figure(figsize=(12, 6))

    # Plot 1: Linear scaling
    plt.subplot(1, 2, 1)
    plt.plot(N_range, corrections_range * 1000, 'b-', linewidth=2, label=r'$\Delta E \propto N^{-5/4}$')
    plt.scatter([N_target], [correction_val * 1000], color='red', s=100, zorder=5, label=f'N={N_target}')
    plt.title('Finite-Size Correction vs. System Size', fontsize=14)
    plt.xlabel('Number of Electrons (N)', fontsize=12)
    plt.ylabel(r'Correction $\Delta E$ (mHa)', fontsize=12)
    plt.grid(True, which='both', linestyle='--', alpha=0.7)
    plt.legend(fontsize=11)
    
    # Plot 2: Log-Log scaling to verify power law
    plt.subplot(1, 2, 2)
    plt.loglog(N_range, corrections_range, 'k-', linewidth=2, label=r'Slope $-5/4$')
    
    # Calculate and plot reference N^-1 slope (3D behavior) for comparison
    # We normalize it to intersect at the first point to visualize the slope difference
    ref_N_inv = corrections_range[0] * (N_range[0] / N_range)
    plt.loglog(N_range, ref_N_inv, 'g--', alpha=0.6, label=r'3D Reference ($\propto N^{-1}$)')
    
    plt.scatter([N_target], [correction_val], color='red', s=100, zorder=5)
    plt.title('Scaling Verification (Log-Log)', fontsize=14)
    plt.xlabel('Number of Electrons (N)', fontsize=12)
    plt.ylabel(r'Correction $\Delta E$ (Hartree)', fontsize=12)
    plt.grid(True, which='both', linestyle='--', alpha=0.7)
    plt.legend(fontsize=11)
    
    plt.tight_layout()
    
    # Save the figure
    plt.savefig('2deg_finite_size_correction.png', dpi=300)
    plt.show()
    
    print("Output plot saved as '2deg_finite_size_correction.png'")

if __name__ == "__main__":
    main()
```
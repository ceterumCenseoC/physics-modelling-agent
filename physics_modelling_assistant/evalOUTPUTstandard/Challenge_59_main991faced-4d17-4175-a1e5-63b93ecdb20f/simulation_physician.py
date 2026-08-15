
```python
import numpy as np
import matplotlib.pyplot as plt

# =============================================================================
# 1. PHYSICAL CONSTANTS AND PARAMETERS
# =============================================================================

# Units:
# Length: Angstroms (A)
# Mass: atomic mass units (amu) - implicitly handled via lattice parameters
# Charge: elementary charge (e) - implicitly handled for scattering factors if needed

# Lattice Parameters
a = 4.0                  # Lattice constant [A]

# Crystal Dimensions
N_cells_side = 100       # Number of unit cells per side (N^3 total)
N = N_cells_side ** 3    # Total number of unit cells
L = N_cells_side * a     # Physical size of the crystal cube [A]

# Displacement Field Parameters (Strain Wave)
epsilon = 0.08           # Displacement amplitude [A]
M = 20                   # Period of the displacement wave in units of unit cells
Q_mag = 2 * np.pi / (M * a) # Wave vector magnitude of the displacement field [A^-1]

# Scanning Parameters for Reciprocal Space Scan
# We will scan near the fundamental Bragg peak (100), i.e., n_x around 1.
n_center = 1.0           # Center of the scan in reciprocal lattice units (n_x)
scan_width = 0.15        # Scan width (+/-) around n_center
num_points = 1000        # Resolution of the scan
n_points = np.linspace(n_center - scan_width, n_center + scan_width, num_points)

# =============================================================================
# 2. MODEL IMPLEMENTATION
# =============================================================================

def calculate_structure_factor_analytic(nx, ny, nz, N_total, eps, lat_const, period_M):
    """
    Calculates the structure factor S(q) to first order in epsilon using 
    the derived analytical formulas.

    Parameters:
    nx, ny, nz (float or array): Reciprocal lattice indices components of q.
    N_total (int): Total number of unit cells in the crystal.
    eps (float): Displacement amplitude epsilon.
    lat_const (float): Lattice constant a.
    period_M (int): Superlattice period M.

    Returns:
    complex: The complex structure factor S(q).
    """
    
    # 1. Structure factor of the perfect crystal S0(q)
    # S0 is non-zero only if n_y and n_z are integers (transverse condition)
    # and strictly integer n_x. However, for numerical plotting, we simulate
    # the delta-like behavior using the finite size lineshape (Sinc^2).
    # 
    # To形象展示 (Visualize) the analytical result properly, we treat the sums 
    # as discrete Kronecker deltas + finite size broadening. 
    # But the prompt asks to implement THE MODEL.
    # The derived model formula is:
    # S(q) ~ S0 + Correction
    # S0 peaks at integer n.
    # Correction peaks at n = int +/- 1/M.
    
    # Helper function for Sinc (shape of finite crystal peak)
    # The peak profile for N cells is proportional to sin(N*pi*x) / sin(pi*x) -> N at integer x
    # We approximate main peak contribution:
    
    # Since ny, nz are fixed (usually 0) in this 1D scan problem, we check their integer nature.
    # We assume ny = 0, nz = 0 for the scan direction parallel to [100].
    
    # We will calculate the magnitude of the structure factor squared |S|^2 (Intensity)
    # based on the superposition of the main peak and the satellite peaks.
    
    # Parameters for peak width (finite size broadening)
    # Peak width ~ 1/N. To make them visible in plots, we add a small broadening 
    # or simply calculate the theoretical maxima.
    
    sigma = 1.0 / (2 * N_cells_side) # Approximate width for gaussian visualization
    
    # --- Term 1: Main Bragg Peaks ---
    # Condition: n_x is integer (near 1), n_y integer, n_z integer.
    # We assume ny=0, nz=0.
    
    delta_y = 1.0 if np.isclose(ny, round(ny)) else 0.0
    delta_z = 1.0 if np.isclose(nz, round(nz)) else 0.0
    
    # Main peak located at integer n_x, let's say k = 1.
    k = 1
    # Structure factor magnitude for main peak:
    # |S0| = N * delta(nx - int) * delta(ny) * delta(nz)
    
    # We use a Gaussian to visualize the delta function for plotting, 
    # but analytically it's a Kronecker delta.
    S0_profile = np.exp(-((nx - k)**2) / (2 * sigma**2))
    S0_val = N_total * S0_profile * delta_y * delta_z
    
    # --- Term 2: Satellite Peaks ---
    # Condition: n_x = integer +/- 1/M
    # Positions: n_x = k + 1/M and n_x = k - 1/M
    # S_sat = -/+ N * (pi * eps / a) * (integer part)
    # For the first satellite near k=1: integer part is effectively k=1.
    
    # Coefficient magnitude
    coef = (np.pi * eps / lat_const) * k
    amp_sat = N_total * coef
    
    sat_plus_pos = k + 1.0/period_M
    sat_minus_pos = k - 1.0/period_M
    
    # Profiles for visualization
    S_sat_plus_profile = np.exp(-((nx - sat_plus_pos)**2) / (2 * sigma**2))
    S_sat_minus_profile = np.exp(-((nx - sat_minus_pos)**2) / (2 * sigma**2))
    
    # Signs: For k + 1/M (satellite +), the formula derivation yields -N * ...
    # Check derivation:
    # Term is - (pi eps nx / a) * [sum(e^{i(n-1/M)l}) - sum(e^{i(n+1/M)l})]
    # If n = k + 1/M:
    #   1st sum argument: (k + 1/M - 1/M) = k -> Integer. Coefficient is -1.
    #   2nd sum argument: (k + 1/M + 1/M) -> Not integer.
    #   Result: -1 * (-pi eps k / a) = + (pi eps k / a). Wait.
    # Let's re-verify signs from Context section 4: 
    # "S_sat = -/+ N * (pi eps / a) * (M +/- 1)" 
    # Let's check indices. The context uses n_x = M +/- 1. 
    # My n_x is in units of 2pi/a. 
    # The context "n_x = M +/- 1" implies a different indexing convention likely related 
    # to superlattice cells.
    # 
    # Let's stick to the explicit derivation in Section 2/3 of the context:
    # S(q) = S0 - (pi n_x eps / a) [ sum((n-1/M)) - sum((n+1/M)) ]
    #
    # Case 1: Satellite at n_x = k - 1/M. (e.g. 0.95)
    #   sum((k - 1/M - 1/M)) is not integer.
    #   sum((k - 1/M + 1/M)) = sum(k) is integer.
    #   The sum((n+1/M)) is active. It has a '+' sign in the subtraction: "(A - B)".
    #   So contribution is - (pi n_x eps / a) * ( - Active_Sum ). 
    #   Contribution is + (pi n_x eps / a) * N.
    #   Value is approx N * pi eps k / a. Positive.
    #
    # Case 2: Satellite at n_x = k + 1/M. (e.g. 1.05)
    #   sum((k + 1/M - 1/M)) = sum(k) is integer.
    #   The sum((n-1/M)) is active. It has a '-' sign in the subtraction.
    #   So contribution is - (pi n_x eps / a) * ( + Active_Sum ).
    #   Contribution is - N * pi eps k / a. Negative.
    
    S_plus_val = -1.0 * amp_sat * S_sat_plus_profile * delta_y * delta_z  # n = k + 1/M
    S_minus_val = 1.0 * amp_sat * S_sat_minus_profile * delta_y * delta_z # n = k - 1/M
    
    # Total Structure Factor (Real part for visualization, as we plot Intensity)
    S_total = S0_val + S_plus_val + S_minus_val
    
    return S_total

# =============================================================================
# 3. GENERATION OF DATA
# =============================================================================

# We calculate Intensity I(q) = |S(q)|^2
# Note: For the interference plot, we show the real amplitude to distinguish
# constructive/destructive interference if we were summing waves, 
# but typically diffraction plots show Intensity. 
# However, since the prompt asks for "criteria for nonvanishing structural factor"
# and the signs differ, plotting the Amplitude (Structure Factor) is informative.

# Scan near n_x = 1, n_y = 0, n_z = 0
ny_scan = 0.0
nz_scan = 0.0

S_values = calculate_structure_factor_analytic(n_points, ny_scan, nz_scan, N, epsilon, a, M)
Intensity_values = np.abs(S_values)**2

# Calculate theoretical maxima values for annotation
I_peak_main = N**2
# Factor (pi * eps / a)**2
sat_ratio = (np.pi * epsilon / a)**2
I_peak_sat = (N * np.pi * epsilon / a)**2 # Approx N^2 * sat_ratio

print(f"--- Simulation Parameters ---")
print(f"Lattice Constant (a): {a} A")
print(f"Crystal Size (N): {N} cells ({L} nm)")
print(f"Displacement (eps): {epsilon} A")
print(f"Wave Period (M): {M} cells")
print(f"-----------------------------")
print(f"Main Peak Intensity (scaled): {1.0:.4f}")
print(f"Satellite Ratio (eps<{eps}): {sat_ratio:.6f}")
print(f"Expected Satellite Positions (nx): {1 - 1/M:.4f}, {1 + 1/M:.4f}")

# =============================================================================
# 4. VISUALIZATION
# =============================================================================

plt.figure(figsize=(10, 6))

# Plot Intensity
plt.plot(n_points, Intensity_values / np.max(Intensity_values), 
         label=r'Intensity $I(\vec{q}) \propto |S(\vec{q})|^2$ (1st Order)', color='blue', linewidth=1.5)

# Annotations
plt.title(r'Structure Factor of Strained SC Crystal ($\vec{\varepsilon} \parallel [100], \vec{Q} \parallel [100]$)', fontsize=14)
plt.xlabel(r'Reciprocal Index $n_x$ (units of $2\pi/a$)', fontsize=12)
plt.ylabel('Normalized Intensity', fontsize=12)

# Mark positions
plt.axvline(x=1.0, color='black', linestyle='--', alpha=0.3)
plt.text(1.0, 1.05, 'Main Bragg\nPeak', ha='center', va='bottom', fontsize=10)

plt.axvline(x=1 - 1/M, color='red', linestyle='--', alpha=0.3)
plt.text(1 - 1/M, sat_ratio*10, 'Satellite (-)', ha='center', va='bottom', fontsize=10, color='red')
plt.axvline(x=1 + 1/M, color='red', linestyle='--', alpha=0.3)
plt.text(1 + 1/M, sat_ratio*10, 'Satellite (+)', ha='center', va='bottom', fontsize=10, color='red')

# Zoom in on satellites if they are too small, or adjust scale
# The satellites are at ~0.004 (0.4%) of the main peak. 
# We might want a subplot or log scale to see them better if the linear scale crushes them.
# Given the comparison, linear is fine but we should ensure they are visible.

plt.grid(True, alpha=0.4)
plt.legend()
plt.tight_layout()

# Create a second plot showing the "Structure Factor" Amplitude (Complex Real part)
# This highlights the +/- sign criteria (phase) derived in the model
plt.figure(figsize=(10, 6))
plt.plot(n_points, S_values / N, label=r'Structure Factor Amplitude $S(\vec{q})/N$', color='green', linewidth=1.5)
plt.title(r'Structure Factor Amplitude (Showing Phase Differences)', fontsize=14)
plt.xlabel(r'Reciprocal Index $n_x$ (units of $2\pi/a$)', fontsize=12)
plt.ylabel(r'$S/N$', fontsize=12)
plt.axhline(y=0, color='black', linestyle='-', alpha=0.1)
plt.axvline(x=1.0, color='black', linestyle='--', alpha=0.3)
plt.axvline(x=1 - 1/M, color='red', linestyle='--', alpha=0.3)
plt.axvline(x=1 + 1/M, color='red', linestyle='--', alpha=0.3)
plt.grid(True, alpha=0.4)
plt.legend()
plt.tight_layout()

plt.show()

# =============================================================================
# 5. OUTPUT RESULTS
# =============================================================================

print("\n--- Theoretical Results ---")
print("Criteria for nonvanishing Structure Factor (First Order):")
print(f"1. n_y, n_z must be integers.")
print(f"2. n_x must be an integer (Main) OR n_x must be an integer +/- 1/M (Satellites).")
print("\nCorresponding Structure Factor Magnitude (for n_x = 1 +/- 1/M):")
print(f"S_sat = +/- N * (pi * epsilon / a)")
print(f"     = +/- {N} * ({np.pi} * {epsilon} / {a})")
print(f"     approx +/- {N * np.pi * epsilon / a:.1f}")
```
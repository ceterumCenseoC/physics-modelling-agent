```python
import numpy as np
import matplotlib.pyplot as plt

def calculate_structure_factor_properties(a=4.0, N=1e5, M=10, epsilon=0.04, n_x=1, n_y=0, n_z=0):
    """
    Calculates the structure factor properties for a strained simple cubic crystal.

    Parameters:
    a (float): Lattice constant in Angstroms.
    N (float): Number of unit cells (linear approximation for scattering volume).
    M (float): Modulation period integer (dimensionless).
    epsilon (float): Displacement amplitude in Angstroms.
    n_x, n_y, n_z (int): Miller indices for the Bragg peak.

    Returns:
    dict: A dictionary containing calculated values and conditions.
    """
    
    # --- 1. Physics Constants & Derived Parameters ---
    
    # Reciprocal lattice vector G = (2*pi/a) * n
    # We are interested in the properties of the sidebands at K = G +/- Q
    
    # Magnitude of K_x relevant for the dot product K * epsilon
    # K_x = (2*pi/a) * (n_x +/- 1/M)
    # We calculate the coefficient term (K * epsilon) / (2*pi) which is (epsilon/a)*(n_x +/- 1/M)
    
    coef_plus_1 = (epsilon / a) * (n_x + 1.0/M)
    coef_minus_1 = (epsilon / a) * (n_x - 1.0/M)
    
    # Atomic form factor f.
    # For this model, f is a multiplicative constant for intensity. 
    # We assume f=1 for the calculation of relative intensity ratios, 
    # or structure factor amplitude relative to f*N.
    f = 1.0 
    
    # --- 2. Structure Factor Calculation (S_plus, S_minus) ---
    
    # Formula derived: S_pm = +/- (1/2) * f * N * [ K * epsilon ]
    # Where K * epsilon was expanded to include the specific wave vector shift.
    # S_pm = +/- (1/2) * f * N * [ (2*pi*epsilon/a) * (n_x +/- 1/M) ]
    # S_pm = +/- pi * f * N * (epsilon/a) * (n_x +/- 1/M)
    
    S_plus_val = np.pi * f * N * (epsilon / a) * (n_x + 1.0/M)
    S_minus_val = np.pi * f * N * (epsilon / a) * (n_x - 1.0/M)
    
    # --- 3. Intensity Calculation ---
    
    # Main Bragg Peak Intensity: I_0 = |S_0|^2 = |f * N|^2
    I_0 = (f * N)**2
    
    # Satellite Peak Intensities
    I_plus = abs(S_plus_val)**2
    I_minus = abs(S_minus_val)**2
    
    # Intensity Ratios
    R_plus = I_plus / I_0 if I_0 > 0 else 0
    R_minus = I_minus / I_0 if I_0 > 0 else 0
    
    # --- 4. Criteria Checking ---
    
    # Criterion: Sidebands exist (non-zero structure factor) only if K * epsilon != 0.
    # Here, displacement is along [100], so epsilon_x != 0.
    # Thus, K_x must be non-zero.
    
    exists_plus = True
    exists_minus = True
    
    # Check the component n_x +/- 1/M
    val_nx_plus = n_x + 1.0/M
    val_nx_minus = n_x - 1.0/M
    
    if np.isclose(val_nx_plus, 0):
        exists_plus = False
    if np.isclose(val_nx_minus, 0):
        exists_minus = False

    # --- 5. Visualization Data Generation ---
    
    # Generate a range of n_x indices to plot the intensity profile
    n_range = np.linspace(-2, 2, 401)
    
    # We need to handle the fact that S_pm depends on the specific K we choose.
    # Let's plot the intensity of satellites associated with a reflection at G=(n,0,0).
    # The satellites are located at G +/- Q.
    # So X-axis is the fractional index relative to the Bragg peak.
    # Delta_n = +/- 1/M
    
    p_sat = n_range + 1.0/M
    m_sat = n_range - 1.0/M
    
    # Calculate S magnitudes for visualization (setting f=N=1 for scaling normalization in plot shape)
    # The functional dependence is proportional to (n_x +/- 1/M)^2 for intensity
    
    # Actual relative intensity vs scattering vector position (odd plots)
    # Let's plot Intensity vs K_position
    
    K_positions = []
    Intensities = []
    
    # Bragg Peaks
    # Loop through some integer n values
    # We calculate the adjacent satellites
    
    # To create a nice "diffraction pattern" look:
    # We iterate Miller indices n_x from -2 to 2 and plot the peaks.
    
    plot_x = []
    plot_I = []
    
    # Define a small width for graphical peaks (linewidth)
    width = 0.005 
    
    # Structure factor approximation: S ~ N (main), S ~ N * epsilon/a (satellites)
    # For visualization, we plot the normalized Intensity / N^2
    
    main_I_norm = 1.0 # (f*N)^2 / N^2
    sat_amp_coef = (np.pi * epsilon / a)**2
    
    current_n_range = range(-2, 3)
    
    for nx in current_n_range:
        # 1. Main Bragg Peak
        plot_x.append(nx)
        plot_I.append(main_I_norm)
        
        # 2. Satellite Plus (at n + 1/M)
        pos_plus = nx + 1.0/M
        val_plus = (nx + 1.0/M)
        I_plus_norm = sat_amp_coef * (val_plus**2)
        
        plot_x.append(pos_plus)
        plot_I.append(I_plus_norm)
        
        # 3. Satellite Minus (at n - 1/M)
        pos_minus = nx - 1.0/M
        val_minus = (nx - 1.0/M)
        I_minus_norm = sat_amp_coef * (val_minus**2)
        
        plot_x.append(pos_minus)
        plot_I.append(I_minus_norm)
        
    # Sort for plotting
    sorted_indices = np.argsort(plot_x)
    plot_x_sorted = np.array(plot_x)[sorted_indices]
    plot_I_sorted = np.array(plot_I)[sorted_indices]

    return {
        'S_plus': S_plus_val,
        'S_minus': S_minus_val,
        'I_plus': I_plus,
        'I_minus': I_minus,
        'R_plus': R_plus,
        'R_minus': R_minus,
        'exists_plus': exists_plus,
        'exists_minus': exists_minus,
        'plot_x': plot_x_sorted,
        'plot_I': plot_I_sorted,
        'parameters': {
            'a': a, 'N': N, 'M': M, 'epsilon': epsilon, 
            'n_x': n_x, 'n_y': n_y, 'n_z': n_z
        }
    }

def plot_results(results):
    """
    Generates a plot of the diffraction pattern.
    """
    plt.figure(figsize=(10, 6))
    
    # Main peaks vs Satellites
    # We use a stem plot for distinct diffraction peaks
    
    x = results['plot_x']
    y = results['plot_I']
    
    # Separate main peaks and satellites for styling
    # Main peaks are at integer indices (roughly)
    is_main = [abs(val - round(val)) < 1e-6 for val in x]
    
    x_main = np.array(x)[is_main]
    y_main = np.array(y)[is_main]
    
    x_sat = np.array(x)[[not i for i in is_main]]
    y_sat = np.array(y)[[not i for i in is_main]]
    
    plt.stem(x_main, y_main, linefmt='b-', markerfmt='bo', basefmt='k-', label='Bragg Peaks (Main)')
    plt.stem(x_sat, y_sat, linefmt='r--', markerfmt='rx', basefmt='k-', label='Sideband Satellites')
    
    # Simulation Info Text
    params = results['parameters']
    info_text = (
        f"Parameters:\n"
        f"Lattice Constant a = {params['a']} $\AA$\n"
        f"Modulation Period M = {params['M']}\n"
        f"Displacement $\epsilon$ = {params['epsilon']} $\AA$\n"
        f"Strain $\epsilon/a$ = {params['epsilon']/params['a']:.3f}\n"
        f"Focus: $n_x=1$, $n_y=0$, $n_z=0$"
    )
    
    plt.annotate(info_text, xy=(0.02, 0.95), xycoords='axes fraction', 
                 verticalalignment='top', bbox=dict(boxstyle='round', facecolor='wheat', alpha=0.5))
    
    plt.xlabel("Scattering Vector Index (Reciprocal Lattice Units)")
    plt.ylabel("Normalized Intensity ($I / f^2 N^2$)")
    plt.title("Diffraction Pattern: Strained Simple Cubic Crystal")
    plt.legend(loc='upper right')
    plt.grid(True, alpha=0.3)
    plt.xlim(-2.5, 2.5)
    
    # Use log scale or linear? Linear shows the contrast better for small strains.
    # But satellites are much smaller. Let's do linear but zoom or keep wide view.
    # Since we set strain to 1%, satellites are ~1e-3 of main.
    # A linear scale makes satellites invisible next to main peaks.
    plt.yscale('log')
    
    plt.show()
    
    print("\n--- Calculation Results ---")
    print(f"Input Parameters: {params}")
    print(f"Sideband Structure Factor (Plus):  {results['S_plus']:.4e}")
    print(f"Sideband Structure Factor (Minus): {results['S_minus']:.4e}")
    print(f"Intensity Ratio (Plus):  {results['R_plus']:.4e}")
    print(f"Intensity Ratio (Minus): {results['R_minus']:.4e}")
    print(f"Criteria Check (K * epsilon != 0): Plus={results['exists_plus']}, Minus={results['exists_minus']}")

# --- Execution ---

# 1. Define Parameters
# Based on the "Realistic Starting Parameters" section
params_for_calc = {
    'a': 4.0,           # Angstroms
    'N': 1e5,           # Count
    'M': 10,            # Integer
    'epsilon': 0.04,    # Angstroms
    'n_x': 1,           # Miller index
    'n_y': 0,
    'n_z': 0
}

# 2. Run Model
results = calculate_structure_factor_properties(**params_for_calc)

# 3. Display Output
plot_results(results)

# --- Verification of Criteria ---
# Let's test a case where criteria fail (n_x such that n_x +/- 1/M = 0)
# If M=10, then 1/M = 0.1.
# If n_x = -0.1, n_x + 0.1 = 0. But n_x must be integer for a Bragg peak center.
# The satellites are at fractional positions.
# The sideband intensity is proportional to (n_x +/- 1/M).
# If we calculate S_+ for n_x = -1 (main Bragg at -1) -> satellite at -0.9. 
# The factor is (-1 + 0.1) = -0.9. Non-zero.
# If we consider the physics: Geometric structure factor vanishes if K_perp to epsilon.
# Here K is parallel, so it doesn't vanish unless K itself is zero.

print("\n--- Criteria Edge Case Check ---")
# Case n_x = 0 is interesting. 
# S_+ ~ (0 + 1/M) = 1/M. 
# S_- ~ (0 - 1/M) = -1/M. 
# Both non-zero if n_x=0.
# The derivation prompt mentioned "besides n_x=M", which likely was a typo for n_x != 0 or context specific.
# Based on our derived formula S ~ (n_x +/- 1/M), the only way S=0 is if n_x = -/+ 1/M.
# Since n_x is an integer (Bragg peak index), and 1/M is positive fraction, 
# n_x - 1/M = 0 implies n_x = 1/M (not integer).
# n_x + 1/M = 0 implies n_x = -1/M (not integer).
# So for integer n_x, neither S_+ nor S_- vanish for real strain epsilon > 0 in this specific geometry.

edge_results = calculate_structure_factor_properties(n_x=0, n_y=0, n_z=0, a=4, M=10, epsilon=0.04)
print(f"For n_x=0: S_plus = {edge_results['S_plus']}, S_minus = {edge_results['S_minus']}")
print("Conclusion: For this geometry, sidebands do not vanish for standard integer Bragg reflections.")
```
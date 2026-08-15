
```python
import numpy as np
import matplotlib.pyplot as plt

# --- Constants ---
hbar = 1.0545718e-34       # Reduced Planck constant (J*s)
k_B = 1.380649e-23         # Boltzmann constant (J/K)
e = 1.60217663e-19         # Elementary charge (C)
m_0 = 9.10938356e-31       # Free electron mass (kg)
T_ref = 300.0              # Reference Temperature (K)

def calculate_transport_properties(m_c_x, m_c_y, m_v_x, m_v_y, Delta, T, tau):
    """
    Calculates the transport properties for the two-band 2D intrinsic semiconductor model.
    
    Parameters:
    -----------
    m_c_x, m_c_y : float
        Effective masses for conduction band in x and y directions (kg).
    m_v_x, m_v_y : float
        Effective masses for valence band in x and y directions (kg).
    Delta : float
        Band gap energy (J).
    T : float
        Temperature (K).
    tau : float
        Relaxation time (s).
        
    Returns:
    --------
    dict
        Dictionary containing calculated parameters:
        - n_i: Intrinsic carrier density (m^-2)
        - sigma_c_x, sigma_c_y: Conductivity of conduction band (S)
        - sigma_v_x, sigma_v_y: Conductivity of valence band (S)
        - S_c_x, S_c_y: Seebeck coefficient of conduction band (V/K)
        - S_v_x, S_v_y: Seebeck coefficient of valence band (V/K)
        - S_xx, S_yy: Total Seebeck coefficients (V/K)
        - gonio_polar: Boolean, True if goniopolarity condition is met
        - mass_ratio_x: m_v_x / m_c_x
        - mass_ratio_y: m_v_y / m_c_y
    """
    
    # 1. Calculate Intrinsic Carrier Density (n_i)
    # For a 2D parabolic band, DOS is constant: D = g*m / (2*pi*hbar^2)
    # We assume spin degeneracy g=2 for simplicity (usually g=2 per band)
    # The intrinsic carrier density requires integrating Fermi-Dirac or using Boltzmann approx.
    # Assuming Symmetric bands for density calculation (using geometric mean of masses for isotropic approximation in n_i)
    # or simply calculating the density with the reduced mass mu*: 1/mu* = 1/m_e + 1/m_h.
    # To be consistent with the "same density" assumption for the Seebeck formula derivation,
    # we calculate n_i based on the reduced mass of the system.
    
    # Reduced masses for x and y
    m_red_x = (m_c_x * m_v_x) / (m_c_x + m_v_x)
    m_red_y = (m_c_y * m_v_y) / (m_c_y + m_v_y)
    
    # Geometric mean of the reduced mass for the 2D density (assuming circular isofrequency contours for density calculation)
    # A rigorous calculation involves elliptical contours, but roughly m* = sqrt(mx*my)
    m_eff_ni_sq = m_red_x * m_red_y
    m_eff_ni = np.sqrt(m_eff_ni_sq)
    
    # DOS for 2D parabolic band (including spin degeneracy g=2, valleys v=1)
    # N(E) = g * v * m_eff / (2 * pi * hbar^2) (constant)
    # n_i = integral N(E) f(E) dE
    # For intrinsic semiconductor, n_c = n_v.
    # Using Boltzmann approximation: n = N_c * exp(-(E_c - E_f)/kT)
    # Simplified formula for intrinsic density:
    # n_i * p_i = n_i^2 = N_c N_v exp(-Delta/kT).
    # If bands symmetric, N_c approx N_v.
    
    # DOS mass used for density
    # Note: In the problem context, strict symmetry isn't required for the "intrinsic" condition (n_c=n_v),
    # the Fermi level adjusts to ensure n_c = n_v.
    # However, to calculate a numerical n_i, we need an effective mass.
    # We use the reduced mass.
    
    pi = np.pi
    DOS_mass = m_eff_ni * 2 # multiply by 2 for spin degeneracy
    N_eff = DOS_mass * k_B * T / (2 * pi * hbar**2) # approx effective DOS prefactor
    
    # Intrinsic carrier density n_i
    # n_i = N_eff * exp(-Delta / (2 * k_B * T))
    n_i = N_eff * np.exp(-Delta / (2 * k_B * T))
    
    # 2. Calculate Conductivities (sigma)
    # sigma = n * e * mu. mu = e * tau / m
    # sigma = n * e^2 * tau / m
    
    # Conduction band conductivities
    sigma_c_x = n_i * e**2 * tau / m_c_x
    sigma_c_y = n_i * e**2 * tau / m_c_y
    
    # Valence band conductivities (using same n_i because intrinsic)
    sigma_v_x = n_i * e**2 * tau / m_v_x
    sigma_v_y = n_i * e**2 * tau / m_v_y
    
    # 3. Calculate Seebeck Coefficients (S)
    # Using Mott formula for 2D parabolic band in non-degenerate limit:
    # S = -(pi^2 * kB^2 * T) / (3 * e) * (d ln sigma / d E)
    # sigma(E) ~ N(E) * Tau(E) / m.
    # In 2D, N(E) is constant (step function), so d(ln N)/dE is 0 at bands, delta at edges.
    # The energy dependence comes mostly from Tau(E) or the specific transport energy window.
    # However, for the contrasting signs of c and v bands, we use the formalism:
    # S_n = - (E_n - E_F) / (e * T) roughly (Heikes formula limit).
    # Or more accurately for non-degenerate semiconductor:
    # S = (k_B/e) * ( (E_F - E_n) / (k_B T) + A_n )
    # where A_n is a constant related to scattering (typically 2 for acoustic phonon scattering).
    
    # For this specific problem, we rely on the band structure symmetry argument that |S_c| approx |S_v|
    # is not strictly true unless masses are symmetric, but the sign is determined by the band curvature.
    # S_c is negative, S_v is positive.
    # The Mott formula gives the magnitude.
    # Let's compute the magnitude using the standard formula for non-degenerate semiconductors:
    # S_n = +/- (k_B/e) * ( r + 2 - ln(n/N) ) where r is scattering exponent.
    # Since n is same for both and N differs slightly by mass, the difference in magnitude is small compared to sign flip if masses are comparable.
    # To highlight the effect of mass ratios derived in the problem, we strictly enforce the sign convention
    # and use a magnitude that is physically reasonable.
    
    # Magnitude based on kinetic energy relative to Fermi level
    # For electrons: S ~ - (k_B/e) * (Delta / 2k_BT + const)
    # For holes: S ~ + (k_B/e) * (Delta / 2k_BT + const)
    
    scattering_factor = 2.0 # r + 2, assuming acoustic phonon scattering (transport distribution index)
    
    # Effective Fermi level offset -Delta/2 roughly
    # n_c = N_c exp(-(Ec-Ef)/kT) => (Ec-Ef) = kT ln(Nc/n)
    # Seebeck S_c = -(k_B/e) [ (Ec-Ef)/kT + 2 ] = -(k_B/e) [ ln(Nc/n) + 2 ]
    # Nc = m_c * kT / (pi hbar^2) (spin included)
    
    N_c_x = m_c_x * k_B * T / (np.pi * hbar**2)
    N_c_y = m_c_y * k_B * T / (np.pi * hbar**2)
    
    N_v_x = m_v_x * k_B * T / (np.pi * hbar**2)
    N_v_y = m_v_y * k_B * T / (np.pi * hbar**2)
    
    # Seebeck magnitudes
    # Note: The model derivation states S determined by carrier type sign.
    # We compute S_n using the formula: S = (k_B/e) * (sign_n) * (A - ln(n/N_n))
    # sign_n is -1 for electrons (c), +1 for holes (v)
    
    # Holes are carriers in valence band, so S_v > 0
    S_c_x = -(k_B / e) * (scattering_factor - np.log(n_i / N_c_x))
    S_c_y = -(k_B / e) * (scattering_factor - np.log(n_i / N_c_y))
    
    S_v_x = (k_B / e) * (scattering_factor - np.log(n_i / N_v_x))
    S_v_y = (k_B / e) * (scattering_factor - np.log(n_i / N_v_y))
    
    # 4. Total Seebeck Coefficient (Weighted average)
    S_xx = (sigma_c_x * S_c_x + sigma_v_x * S_v_x) / (sigma_c_x + sigma_v_x)
    S_yy = (sigma_c_y * S_c_y + sigma_v_y * S_v_y) / (sigma_c_y + sigma_v_y)
    
    # 5. Check Goniopolarity Condition
    # Condition: S_xx * S_yy < 0 (Signs are opposite)
    # Derived Mass Condition: (m_v_x / m_c_x > 1) and (m_v_y / m_c_y < 1)
    
    is_goniopolar = (S_xx < 0 and S_yy > 0) or (S_xx > 0 and S_yy < 0)
    
    mass_ratio_x = m_v_x / m_c_x
    mass_ratio_y = m_v_y / m_c_y
    condition_met = (mass_ratio_x > 1) and (mass_ratio_y < 1)
    
    return {
        'n_i': n_i,
        'sigma_c_x': sigma_c_x,
        'sigma_c_y': sigma_c_y,
        'sigma_v_x': sigma_v_x,
        'sigma_v_y': sigma_v_y,
        'S_c_x': S_c_x, 'S_c_y': S_c_y,
        'S_v_x': S_v_x, 'S_v_y': S_v_y,
        'S_xx': S_xx, 'S_yy': S_yy,
        'gonio_polar': is_goniopolar,
        'mass_ratio_x': mass_ratio_x,
        'mass_ratio_y': mass_ratio_y,
        'condition_check': condition_met
    }

# --- Parameter Setup based on Context ---
# Using the "Realistic Starting Parameters" provided in the context

# Masses
m_c_x_val = 0.2 * m_0
m_c_y_val = 1.5 * m_0
m_v_x_val = 1.0 * m_0
m_v_y_val = 0.5 * m_0

# Band Gap (200 meV converted to Joules)
Delta_val = 0.2 * e 

# Temperature
T_val = 300.0

# Relaxation time (100 fs)
tau_val = 100e-15

# --- Execution ---
results = calculate_transport_properties(
    m_c_x_val, m_c_y_val, 
    m_v_x_val, m_v_y_val, 
    Delta_val, T_val, tau_val
)

# --- Output Formatting ---
print("--- Simulation Parameters ---")
print(f"Temperature: {T_val} K")
print(f"Band Gap: {Delta_val/e*1000} meV")
print(f"Relaxation Time: {tau_val*1e15} fs")
print(f"Effective Masses (m_c_x, m_c_y): ({m_c_x_val/m_0:.2f}, {m_c_y_val/m_0:.2f}) m0")
print(f"Effective Masses (m_v_x, m_v_y): ({m_v_x_val/m_0:.2f}, {m_v_y_val/m_0:.2f}) m0")
print("\n--- Calculated Transport Properties ---")
print(f"Intrinsic Carrier Density n_i: {results['n_i']:.4e} m^-2")
print(f"Conductivities (S):")
print(f"  Sigma_c_x: {results['sigma_c_x']:.4e}, Sigma_v_x: {results['sigma_v_x']:.4e} (Ratio v/c: {results['mass_ratio_x']:.2f})")
print(f"  Sigma_c_y: {results['sigma_c_y']:.4e}, Sigma_v_y: {results['sigma_v_y']:.4e} (Ratio v/c: {results['mass_ratio_y']:.2f})")
print(f"Seebeck Coefficients (uV/K):")
print(f"  S_c_x: {results['S_c_x']*1e6:.2f}, S_v_x: {results['S_v_x']*1e6:.2f}")
print(f"  S_c_y: {results['S_c_y']*1e6:.2f}, S_v_y: {results['S_v_y']*1e6:.2f}")
print(f"Total Seebeck Coefficients (uV/K):")
print(f"  S_xx: {results['S_xx']*1e6:.2f} (Type: {'n' if results['S_xx'] < 0 else 'p'})")
print(f"  S_yy: {results['S_yy']*1e6:.2f} (Type: {'n' if results['S_yy'] < 0 else 'p'})")
print("\n--- Goniopolarity Condition Check ---")
print(f"Condition (m_v_x/m_c_x > 1): {results['mass_ratio_x'] > 1} (Ratio = {results['mass_ratio_x']:.2f})")
print(f"Condition (m_v_y/m_c_y < 1): {results['mass_ratio_y'] < 1} (Ratio = {results['mass_ratio_y']:.2f})")
print(f"Is System Goniopolar? {results['gonio_polar']}")

# --- Visualization ---
fig, ax = plt.subplots(1, 1, figsize=(6, 4))

# Data for plotting
directions = ['x-direction', 'y-direction']
S_values = [results['S_xx']*1e6, results['S_yy']*1e6] # in microvolts
colors = ['blue' if s < 0 else 'red' for s in S_values]

bars = ax.bar(directions, S_values, color=colors, alpha=0.7)
ax.set_ylabel('Seebeck Coefficient $S_{\\alpha\\alpha}$ ($\mu V/K$)', fontsize=12)
ax.set_title('Goniopolarity: Opposite Signs of Thermopower', fontsize=14)
ax.axhline(0, color='black', linewidth=0.8)
ax.grid(axis='y', linestyle='--', alpha=0.5)

# Add labels on bars
for bar in bars:
    height = bar.get_height()
    label = f"{height:.1f}"
    ax.text(bar.get_x() + bar.get_width()/2., height if height > 0 else height-20, 
            label, ha='center', va='bottom' if height > 0 else 'top', color='black', fontsize=11, fontweight='bold')
    
# Add legend for n-type/p-type
from matplotlib.patches import Patch
legend_elements = [Patch(facecolor='blue', alpha=0.7, label='n-type (Electrons)'),
                   Patch(facecolor='red', alpha=0.7, label='p-type (Holes)')]
ax.legend(handles=legend_elements, loc='upper right')

plt.tight_layout()
plt.savefig('goniopolarity_result.png', dpi=150)
print("\nGraph saved as 'goniopolarity_result.png'")
```
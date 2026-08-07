```python
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import MaxNLocator

# --- Physical Constants & System Configuration ---
# Using real physical units as specified in the planning phase
H_BAR = 1.0545718e-34      # Reduced Planck constant (J*s)
C_LIGHT = 2.99792458e8     # Speed of light (m/s)
PI = np.pi

# --- 1. Driving Field Parameters ---
LAMBDA_0 = 800e-9          # Fundamental wavelength (m)
OMEGA_0 = 2 * PI * C_LIGHT / LAMBDA_0 # Fundamental frequency (rad/s)

PULSE_DURATION_FWHM = 50e-15 # 50 fs
# Convert FWHM intensity to sigma for the Gaussian electric field envelope
# I(t) ~ exp(-t^2 / (2*tau_I^2)) where tau_I = FWHM / (2*sqrt(2*ln(2)))
# E(t) ~ exp(-t^2 / (4*tau_I^2)) -> sigma_t = FWHM / (2*sqrt(2*ln(2))) * sqrt(2) ??
# Standard relation: FWHM = 2*sqrt(2*ln(2)) * sigma_t (for intensity)
# For E-field: FWHM_E = 2*sqrt(2*ln(2)) * sigma_E
PULSE_SIGMA = PULSE_DURATION_FWHM / (2 * np.sqrt(2 * np.log(2)))

# --- 2. Pulse Train Definition ---
# We define the temporal grid
t_window = 400e-15 # 400 fs window
dt = 0.1e-15       # 0.1 fs resolution
time_grid = np.arange(-t_window/2, t_window/2, dt)

# Pulse Delays
delay_1 = 0e-15
delay_2 = 30e-15
delay_3 = 60e-15

# OAM and Spin Properties for the 3 pulses
# Format: {'ell': int, 'sigma': int} where sigma: +1 (LCP), -1 (RCP)
pulses_params = [
    {'ell': -1, 'sigma': +1, 'delay': delay_1, 'name': 'Pulse 1'},
    {'ell':  2, 'sigma': -1, 'delay': delay_2, 'name': 'Pulse 2'},
    {'ell':  1, 'sigma': +1, 'delay': delay_3, 'name': 'Pulse 3'}
]

# --- 3. Model Implementation: HHG Selection Rules ---
def calculate_harmonic_properties(q, pulse):
    """
    Calculates the properties of the q-th harmonic based on the driving pulse
    using HHG selection rules.
    
    Args:
        q (int): Harmonic order.
        pulse (dict): Dictionary containing 'ell' and 'sigma'.
        
    Returns:
        dict: Properties of the harmonic pulse.
    """
    # OAM Conservation: l_q = q * l
    l_q = q * pulse['ell']
    
    # Helicity Conservation: sigma_q = sigma_fund (for odd q)
    # The problem specifies q=23 (odd), so helicity is conserved strictly
    # modulo 2  -->  +1 stays +1, -1 stays -1.
    # Formalism: sigma_q = q * sigma (mod 2) for symmetric media.
    # 23 * (+1) = +23 -> odd -> +1
    # 23 * (-1) = -23 -> odd -> -1
    sigma_q = pulse['sigma']
    
    return {'l_q': l_q, 'sigma_q': sigma_q, 'source_pulse': pulse['name']}

# Target Harmonic
HARMONIC_ORDER = 23

# Calculate properties for each component
results = []
for p in pulses_params:
    harmonic_props = calculate_harmonic_properties(HARMONIC_ORDER, p)
    results.append(harmonic_props)

# --- 4. Visualization of the Pulse Train and Calculated Properties ---
# Generate the E-field envelope shape for visualization purposes
total_envelope = np.zeros_like(time_grid)
pulse_envelopes = []

for p in pulses_params:
    # Gaussian envelope: A * exp(-(t - t0)^2 / (2*sigma^2))
    # Assuming equal amplitude for visualization
    env = np.exp(-(time_grid - p['delay'])**2 / (2 * PULSE_SIGMA**2))
    pulse_envelopes.append(env)
    total_envelope += env

# Plotting
fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(10, 8), sharex=True)

# Plot 1: Driving Field Temporal Structure
ax1.plot(time_grid * 1e15, total_envelope, 'k--', alpha=0.5, label='Total Envelope')
colors = ['#1f77b4', '#ff7f0e', '#2ca02c']
for i, env in enumerate(pulse_envelopes):
    label = f"{pulses_params[i]['name']}\n$\ell$={pulses_params[i]['ell']}, $\sigma$={pulses_params[i]['sigma']:+}"
    ax1.plot(time_grid * 1e15, env, color=colors[i], linewidth=2, label=label)

ax1.set_title(f'Driving Field: Train of {len(pulses_params)} Pulses')
ax1.set_ylabel('Electric Field Envelope (a.u.)')
ax1.set_xlabel('Time (fs)')
ax1.legend(loc='upper right')
ax1.grid(True, alpha=0.3)
ax1.xaxis.set_major_locator(MaxNLocator(integer=True))

# Plot 2: 23rd Harmonic Properties (Informational Bar Chart)
# Since these are discrete quantum numbers, a bar chart representation is appropriate.
y_pos = np.arange(len(results))
l_values = [r['l_q'] for r in results]
sigma_values = [r['sigma_q'] for r in results]
labels = [r['source_pulse'] for r in results]

# Colors based on helicity
bar_colors = ['#1f77b4' if s > 0 else '#d62728' for s in sigma_values]
hatch_patterns = ['/' if s > 0 else '\\\\' for s in sigma_values]

bars = ax2.barh(y_pos, l_values, align='center', color=bar_colors, edgecolor='black')

# Add text labels for Helicity
for i, (bar, sigma) in enumerate(zip(bars, sigma_values)):
    width = bar.get_width()
    label_text = r'$\sigma = ' + f'{sigma:+d}$' + r' (' + ('LCP' if sigma > 0 else 'RCP') + r')'
    ax2.text(width/2, bar.get_y() + bar.get_height()/2, label_text, 
             ha='center', va='center', color='white', fontweight='bold')

ax2.set_yticks(y_pos)
ax2.set_yticklabels(labels)
ax2.set_xlabel('Orbital Angular Momentum $\ell_{23}$ (in units of $\hbar$)')
ax2.set_title(f'Properties of the {HARMONIC_ORDER}rd Harmonic')
ax2.grid(True, axis='x', alpha=0.3)
# Set x-axis limits to center the bars reasonably
min_l = min(l_values)
max_l = max(l_values)
padding = (max_l - min_l) * 0.2
if padding == 0: padding = 5
ax2.set_xlim(min_l - 5, max_l + 5)

plt.tight_layout()
plt.savefig('hhg_oam_analysis.png', dpi=300)
plt.show()

# --- 5. Output Results to Console ---
print("-------------------------------------------------")
print(f"High-Harmonic Generation Analysis: {HARMONIC_ORDER}rd Harmonic")
print("-------------------------------------------------")
print("According to HHG selection rules:")
print("  1. OAM Conservation: l_q = q * l_drive")
print("  2. Helicity Conservation (odd q): sigma_q = sigma_drive")
print("-------------------------------------------------")

for r in results:
    pol_str = "LCP" if r['sigma_q'] > 0 else "RCP"
    print(f"{r['source_pulse']} Harmonic Output:")
    print(f"  OAM (l_q): {r['l_q']} h_bar")
    print(f"  Helicity (sigma): {r['sigma_q']:+d} ({pol_str})")
    print("-" * 40)

print("\nGraphical output saved to 'hhg_oam_analysis.png'")
```
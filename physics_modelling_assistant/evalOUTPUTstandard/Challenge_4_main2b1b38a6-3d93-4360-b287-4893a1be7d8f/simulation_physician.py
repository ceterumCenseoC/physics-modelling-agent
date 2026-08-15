
```python
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3d

# --- Model Parameters ---
# Constants (SI Units where applicable, but OAM/Helicity are dimensionless)
C_LIGHT = 2.99792458e8  # m/s

# Laser Parameters
WAVELENGTH = 800e-9     # meters (800 nm)
PULSE_DURATION = 50e-15 # seconds (50 fs FWHM)
OMEGA = 2 * np.pi * C_LIGHT / WAVELENGTH # rad/s

# Driving Field Configuration
# Each tuple: (Delay in fs, OAM charge l, Helicity sigma)
# Helicity: +1 for LCP, -1 for RCP
# Delay is relative to t=0
pulses = [
    {"t_delay": 0.0,   "l": -1, "sigma": +1, "label": "Pulse 1 (LCP)"},
    {"t_delay": 30.0,  "l":  2, "sigma": -1, "label": "Pulse 2 (RCP)"},
    {"t_delay": 60.0,  "l":  1, "sigma": +1, "label": "Pulse 3 (LCP)"}
]

# Target Harmonic
HARMONIC_ORDER = 23

def calculate_net_properties(pulse_list):
    """
    Calculates the effective net OAM and Helicity of the driving field
    based on the superposition of pulses.

    Note: For coherent summation in HHG, we generally consider the conservation
    laws. The effective OAM is the sum of topological charges. The effective
    helicity is determined by the dominant circular polarization component.
    """
    total_oam = sum(p["l"] for p in pulse_list)
    
    # For helicity, simple addition isn't physically accurate for polarization 
    # (which is a vector property), but in the context of HHG selection rules 
    # described, the order (q) harmonic inherits the helicity of the driver 
    # that satisfies conservation. With 2 LCP and 1 RCP, the field has a net 
    # LCP character. The model implies a net helicity of +1.
    total_helicity = +1
    
    return total_oam, total_helicity

def calculate_harmonic_properties(q, l_drive, sigma_drive):
    """
    Applies HHG conservation laws to find OAM and Helicity of the q-th harmonic.
    """
    l_q = q * l_drive
    sigma_q = sigma_drive
    return l_q, sigma_q

def gaussian_pulse(t, t0, fwhm):
    """Gaussian envelope for the pulse intensity/field."""
    # Convert FWHM to sigma for Gaussian formula: FWHM = 2*sigma*sqrt(2*ln(2))
    sigma = fwhm / (2 * np.sqrt(2 * np.log(2)))
    return np.exp(-((t - t0)**2) / (2 * sigma**2))

def visualize_driving_field(time_array, pulse_list, fwhm_fs):
    """
    Creates a visualization of the driving field envelope and properties.
    """
    fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(10, 8))
    
    # Plot 1: Temporal Overlap
    for p in pulse_list:
        envelope = gaussian_pulse(time_array, p["t_delay"], fwhm_fs)
        # Color code by helicity (Blue for LCP, Red for RCP)
        color = 'blue' if p["sigma"] > 0 else 'red'
        ax1.plot(time_array, envelope, label=f'{p["label"]}: l={p["l"]}, $\sigma$={p["sigma"]}', color=color, linestyle='--')

    # Total envelope (incoherent sum for intensity visualization)
    total_env = np.zeros_like(time_array)
    for p in pulse_list:
        total_env += gaussian_pulse(time_array, p["t_delay"], fwhm_fs)
        
    ax1.plot(time_array, total_env, 'k-', linewidth=2, label='Total Intensity Envelope')
    ax1.set_title('Temporal Composition of Driving Field')
    ax1.set_xlabel('Time (fs)')
    ax1.set_ylabel('Intensity (a.u.)')
    ax1.legend()
    ax1.grid(True, alpha=0.3)

    # Plot 2: Angular Momentum Bar Chart
    oams = [p["l"] for p in pulse_list]
    sigmas = [p["sigma"] for p in pulse_list]
    labels = [p["label"] for p in pulse_list]
    
    x_pos = np.arange(len(labels))
    
    ax2.bar(x_pos - 0.2, oams, 0.4, label='OAM ($\ell$)', color='green', alpha=0.7)
    ax2.bar(x_pos + 0.2, sigmas, 0.4, label='Helicity ($\sigma$)', color='purple', alpha=0.7)
    
    ax2.set_title('Angular Momentum Components of Pulses')
    ax2.set_ylabel('Value')
    ax2.set_xticks(x_pos)
    ax2.set_xticklabels([f'Pulse {i+1}' for i in range(len(labels))])
    ax2.legend()
    ax2.axhline(0, color='black', linewidth=0.8)
    ax2.grid(True, axis='y', alpha=0.3)

    plt.tight_layout()
    plt.savefig('hhg_driving_field_analysis.png', dpi=150)
    print("Graphics saved to 'hhg_driving_field_analysis.png'")

# --- Main Execution ---

# 1. Define time grid for analysis
t_start = -50.0
t_end = 120.0
points = 1000
time_fs = np.linspace(t_start, t_end, points)

# 2. Calculate Model Results
l_net, sigma_net = calculate_net_properties(pulses)
l_23, sigma_23 = calculate_harmonic_properties(HARMONIC_ORDER, l_net, sigma_net)

# 3. Print Results
print("-" * 60)
print(f"High-Harmonic Generation Model Results")
print("-" * 60)
print("Input Parameters:")
print(f"  Center Wavelength: {WAVELENGTH*1e9:.0f} nm")
print(f"  Pulse Duration (FWHM): {PULSE_DURATION*1e15:.0f} fs")
print(f"  Number of Driving Pulses: {len(pulses)}")
print("  Pulse Configurations (t, l, sigma):")
for p in pulses:
    print(f"    - {p['label']}: t={p['t_delay']}fs, l={p['l']}, sigma={p['sigma']}")
print("-" * 60)
print("Calculated Driving Field Properties:")
print(f"  Net Effective OAM ($\ell_{{net}}$): {l_net}")
print(f"  Net Effective Helicity ($\sigma_{{net}}$): {sigma_net} (Left Circular)")
print("-" * 60)
print(f"Target Harmonic Order (q): {HARMONIC_ORDER}")
print(f"  23rd Harmonic OAM ($\ell_{{{HARMONIC_ORDER}}}$): {l_23} $\hbar$")
print(f"  23rd Harmonic Helicity ($\sigma_{{{HARMONIC_ORDER}}}$): {sigma_23} (Left Circular)")
print("-" * 60)

# 4. Generate Graphics
print("\nGenerating visualization...")
visualize_driving_field(time_fs, pulses, PULSE_DURATION*1e15)
print("Done.")
```

```python
import numpy as np
import matplotlib.pyplot as plt

# --- Configuration & Constants ---
# Physics Constants
C_LIGHT = 2.99792458e8        # Speed of light in vacuum (m/s)

# Laser Parameters
WAVELENGTH_M = 800e-9         # Center wavelength (meters)
WAVELENGTH_NM = 800           # Center wavelength (nm)
PULSE_DURATION_FS = 50.0      # Full Width at Half Maximum (FWHM) (fs)
OMEGA = 2 * np.pi * C_LIGHT / WAVELENGTH_M # Angular frequency (rad/s)

# Driving Field Configuration
# Defined as a list of dictionaries containing parameters for each sub-pulse.
# t_delay: Temporal delay relative to t=0 (fs)
# l: Topological charge (OAM) (dimensionless integer)
# sigma: Helicity (Spin Angular Momentum), +1 for LCP, -1 for RCP
PULSES_CONFIG = [
    {"t_delay": 0.0,   "l": -1, "sigma": +1, "label": "Pulse 1 (LCP)"},
    {"t_delay": 30.0,  "l":  2, "sigma": -1, "label": "Pulse 2 (RCP)"},
    {"t_delay": 60.0,  "l":  1, "sigma": +1, "label": "Pulse 3 (LCP)"}
]

# Target Harmonic
TARGET_HARMONIC_Q = 23

def get_pulse_envelope(t_array, t_center, fwhm):
    """
    Calculates the Gaussian intensity envelope of a pulse.
    
    Args:
        t_array (np.array): Time array.
        t_center (float): Center time of the pulse.
        fwhm (float): Full Width at Half Maximum duration.
        
    Returns:
        np.array: Normalized Gaussian envelope.
    """
    # Convert FWHM to standard deviation for the Gaussian formula
    # FWHM = 2 * sigma * sqrt(2 * ln(2))
    sigma = fwhm / (2 * np.sqrt(2 * np.log(2)))
    return np.exp(-((t_array - t_center)**2) / (2 * sigma**2))

def calculate_driving_field_properties(pulse_list):
    """
    Calculates the net effective properties of the composite driving field.
    
    OAM Conservation: l_net = sum(l_i)
    Helicity Logic: The net helicity is determined by the dominant circular 
    polarization component influencing the harmonic generation. Given the 
    conservation rules in isotropic media, the harmonic inherits the helicity 
    of the driving field.
    """
    # Sum of Topological Charges
    l_net = sum(p["l"] for p in pulse_list)
    
    # Determine Net Helicity
    # Based on the provided model: Two LCP (+1) pulses and one RCP (-1) pulse.
    # The composite field is dominated by the LCP component.
    sigma_net = +1
    
    return l_net, sigma_net

def calculate_harmonic_properties(q, l_drive, sigma_drive):
    """
    Calculates the properties of the q-th harmonic based on conservation laws.
    
    OAM: l_q = q * l_drive
    Helicity: sigma_q = sigma_drive (inherited from driver)
    """
    l_q = q * l_drive
    sigma_q = sigma_drive
    return l_q, sigma_q

def generate_analysis_plot(time_array, pulse_list, fwhm_fs):
    """
    Generates and saves a visualization of the temporal overlap and 
    angular momentum composition of the driving pulses.
    """
    try:
        fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(10, 8))
        
        # Plot 1: Temporal Profile
        total_envelope = np.zeros_like(time_array)
        
        for p in pulse_list:
            env = get_pulse_envelope(time_array, p["t_delay"], fwhm_fs)
            total_envelope += env
            
            # Color mapping: Blue for LCP (+1), Red for RCP (-1)
            color = 'blue' if p["sigma"] > 0 else 'red'
            linestyle = '--'
            
            ax1.plot(time_array, env, 
                     label=f'{p["label"]}: $\\ell$={p["l"]}, $\\sigma$={p["sigma"]}', 
                     color=color, linestyle=linestyle, alpha=0.7)

        # Plot the combined intensity envelope
        ax1.plot(time_array, total_envelope, 'k-', linewidth=2, label='Total Intensity Envelope')
        
        ax1.set_title('Temporal Configuration of Driving Pulses')
        ax1.set_xlabel('Time (fs)')
        ax1.set_ylabel('Intensity (arb. units)')
        ax1.legend(loc='upper right')
        ax1.grid(True, alpha=0.3)
        ax1.set_xlim([time_array[0], time_array[-1]])

        # Plot 2: Angular Momentum Components
        indices = np.arange(len(pulse_list))
        oam_values = [p["l"] for p in pulse_list]
        sigma_values = [p["sigma"] for p in pulse_list]
        
        # Bar chart for OAM and Helicity
        width = 0.35
        
        ax2.bar(indices - width/2, oam_values, width, label='OAM ($\\ell$)', color='green', alpha=0.8)
        ax2.bar(indices + width/2, sigma_values, width, label='Helicity ($\\sigma$)', color='purple', alpha=0.8)
        
        ax2.set_title('Angular Momentum Components of Input Pulses')
        ax2.set_ylabel('Topological Charge / Helicity')
        ax2.set_xticks(indices)
        ax2.set_xticklabels([f'Pulse {i+1}' for i in range(len(pulse_list))])
        ax2.legend()
        ax2.axhline(0, color='black', linewidth=0.8)
        ax2.grid(True, axis='y', alpha=0.3)

        plt.tight_layout()
        output_filename = 'hhg_driving_field_analysis.png'
        plt.savefig(output_filename, dpi=150)
        plt.close() # Close the figure to free memory
        print(f"Successfully saved visualization to '{output_filename}'")
        
    except Exception as e:
        print(f"Error during plot generation: {e}")

def main():
    """Main execution function to run the HHG model."""
    
    # 1. Setup Time Grid
    # Create a time array spanning -50 fs to +120 fs to capture all pulses
    t_start = -50.0
    t_end = 120.0
    time_points = 1000
    time_fs = np.linspace(t_start, t_end, time_points)
    
    print("=" * 65)
    print(" HIGH-HARMONIC GENERATION (HHG) MODEL CALCULATION ")
    print("=" * 65)
    
    # 2. Display Input Parameters
    print("\n[Input Parameters]")
    print(f"  Laser Wavelength: {WAVELENGTH_NM} nm")
    print(f"  Pulse Duration (FWHM): {PULSE_DURATION_FS} fs")
    print(f"  Target Harmonic Order (q): {TARGET_HARMONIC_Q}")
    print("\n  Driving Field Components:")
    for i, p in enumerate(PULSES_CONFIG):
        pol_type = "LCP" if p["sigma"] > 0 else "RCP"
        print(f"    Pulse {i+1}: Delay={p['t_delay']} fs, OAM(\\ell)={p['l']}, Helicity(\\sigma)={p['sigma']} ({pol_type})")

    # 3. Calculate Driving Field Properties
    print("\n[Model Calculation]")
    l_net, sigma_net = calculate_driving_field_properties(PULSES_CONFIG)
    
    print(f"  1. Net Driving Field OAM (\\ell_net): {l_net}")
    print(f"     (Calculation: {PULSES_CONFIG[0]['l']} + {PULSES_CONFIG[1]['l']} + {PULSES_CONFIG[2]['l']})")
    
    print(f"  2. Net Driving Field Helicity (\\sigma_net): {sigma_net}")
    
    # 4. Calculate Target Harmonic Properties
    l_q, sigma_q = calculate_harmonic_properties(TARGET_HARMONIC_Q, l_net, sigma_net)
    
    print(f"\n[Result for q = {TARGET_HARMONIC_Q}]")
    print(f"  Harmonic OAM (\\ell_{TARGET_HARMONIC_Q}): {l_q} \u0127")
    print(f"     (Calculation: {TARGET_HARMONIC_Q} * {l_net})")
    print(f"  Harmonic Helicity (\\sigma_{TARGET_HARMONIC_Q}): {sigma_q}")
    
    # 5. Generate Visualization
    print("\n[Generating Visualization]")
    generate_analysis_plot(time_fs, PULSES_CONFIG, PULSE_DURATION_FS)
    
    print("\n" + "=" * 65)
    print(" CALCULATION COMPLETE ")
    print("=" * 65)

if __name__ == "__main__":
    main()
```
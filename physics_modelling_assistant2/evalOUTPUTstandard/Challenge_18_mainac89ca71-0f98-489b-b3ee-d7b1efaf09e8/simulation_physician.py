
```python
import numpy as np
import matplotlib.pyplot as plt
from scipy.constants import c, epsilon_0, pi

def calculate_coupling_constants(
    alpha1, 
    alpha2, 
    E1, 
    E2, 
    k, 
    d0, 
    phi1, 
    phi2
):
    """
    Calculates the coupling constants k1 and k2 based on the derived model.
    
    Parameters:
    -----------
    alpha1, alpha2 : float or array
        Polarizabilities of particle 1 and 2 (SI units: C^2 m^2 / J).
        Note: In SI, p = epsilon_0 * alpha * E, so alpha here relates directly
        to the dimensionless volume polarizability often used in literature.
    E1, E2 : float or array
        Electric field amplitudes of traps 1 and 2 (SI units: V/m).
    k : float
        Wave vector magnitude (SI units: rad/m).
    d0 : float
        Equilibrium separation distance (SI units: m).
    phi1, phi2 : float
        Phases of the traps at the focal plane (SI units: rad).
        
    Returns:
    --------
    k1 : float or array
        Symmetric coupling constant (SI units: N/m).
    k2 : float or array
        Antisymmetric coupling constant (SI units: N/m). Always 0 in this model.
    """
    
    # Calculate k1 based on the derived formula from the context
    # k1 = (epsilon_0 * alpha1 * alpha2 * E1 * E2 * k^3) / (8 * pi * d0) * sin(k*d0 + phi1 - phi2)
    # Note: The text derivation concluded with sin, but Energy expansion usually leads to cos for stiffness
    # unless the linear expansion point (equilibrium) shifts. 
    # Based on the "Final Expressions" provided in the text context:
    # k1 = (3*pi/2) * (alpha1 * alpha2 * omega / (epsilon_0 * lambda^3 * d0)) * sqrt(I1*I2) * sin(...)
    # We will implement the explicit form verified in the deduction section of the prompt:
    
    prefactor = (epsilon_0 * alpha1 * alpha2 * E1 * E2 * k**3) / (8 * pi * d0)
    phase_term = np.sin(k * d0 + phi1 - phi2)
    
    k1 = prefactor * phase_term
    
    # By strict symmetry of dipole-dipole interaction and matching the matrix equations
    k2 = 0.0
    
    return k1, k2

def example_simulation_and_plot():
    """
    Sets up realistic parameters, calculates k1, and plots its behavior as a function
    of separation distance d0.
    """
    # --- 1. System Parameters (SI Units) ---
    
    # Laser / Optical Properties
    wavelength = 1064e-9  # 1064 nm (Typical trapping laser)
    k_wave = 2 * np.pi / wavelength
    power = 20e-3         # 20 mW
    waist_radius = 0.6e-6 # 0.6 microns
    
    # Calculate Electric Field Amplitude E at focus
    # I = P / (pi * w^2)  (Approximate peak intensity)
    # I = 0.5 * c * epsilon_0 * E^2  => E = sqrt(2*I / (c*epsilon_0))
    intensity = power / (pi * waist_radius**2)
    E_field = np.sqrt(2 * intensity / (c * epsilon_0))
    
    # Particle Properties (Silica in Water)
    radius = 50e-9       # 50 nm radius
    n_particle = 1.45    # Silica
    n_medium = 1.33      # Water
    
    # Clausius-Mossotti for polarizability alpha
    # p = epsilon_0 * alpha * E
    # alpha = 4 * pi * R^3 * (n_p^2 - n_m^2) / (n_p^2 + 2*n_m^2)  (This is dimensionless alpha in this relation)
    # Wait, standard formula: alpha_cm = (e_p - e_m) / (e_p + 2*e_m)
    # V_pol = 4 * pi * epsilon_0 * R^3 * (n_p^2 - n_m^2)/(n_p^2 + 2*n_m^2)
    # Therefore alpha (in the prompt's definition p = eps0 * alpha * E) is:
    # alpha = 4 * pi * R^3 * (n_p^2 - n_m^2)/(n_p^2 + 2*n_m^2)
    cm_factor = (n_particle**2 - n_medium**2) / (n_particle**2 + 2 * n_medium**2)
    alpha_val = 4 * np.pi * radius**3 * cm_factor
    
    # Phases
    phi1 = 0.0
    phi2 = 0.0 # In-phase traps
    
    # --- 2. Calculate k1 vs Distance d0 ---
    
    # Range of distances: from 1.5 wavelengths to 6 wavelengths (Far field condition kd >> 1 implies ~3+ lambda)
    d0_vals = np.linspace(1.5 * wavelength, 6 * wavelength, 500)
    k1_vals = np.zeros_like(d0_vals)
    
    # Vectorized calculation
    # Note: calculate_coupling_constants accepts arrays for d0
    k1_res, _ = calculate_coupling_constants(
        alpha1=alpha_val, 
        alpha2=alpha_val, 
        E1=E_field, 
        E2=E_field, 
        k=k_wave, 
        d0=d0_vals, 
        phi1=phi1, 
        phi2=phi2
    )
    k1_vals = k1_res
    
    # --- 3. Plotting ---
    
    plt.figure(figsize=(10, 6))
    plt.plot(d0_vals * 1e6, k1_vals, linewidth=2, color='blue')
    
    # Formatting
    plt.title(f'Optical Binding Coupling Constant ($k_1$) vs Distance\n(silica, R={radius*1e9:.0f}nm, $\lambda$={wavelength*1e9:.0f}nm)', fontsize=14)
    plt.xlabel('Separation Distance $d_0$ ($\mu m$)', fontsize=12)
    plt.ylabel('Coupling Constant $k_1$ (N/m)', fontsize=12)
    plt.grid(True, linestyle='--', alpha=0.7)
    
    # Add annotation for k2
    plt.annotate('$k_2 = 0$ (Symmetric Interaction)', 
                 xy=(0.02, 0.05), 
                 xycoords='axes fraction', 
                 fontsize=12, 
                 bbox=dict(boxstyle="round,pad=0.3", fc="yellow", alpha=0.5))

    plt.tight_layout()
    
    # Show plot
    plt.show()
    
    # Print a numerical example at specific point
    d_example = 3.0 * wavelength
    k1_example, _ = calculate_coupling_constants(alpha_val, alpha_val, E_field, E_field, k_wave, d_example, phi1, phi2)
    print("-" * 50)
    print(f"Example Calculation at d0 = {d_example*1e6:.2f} um:")
    print(f"k1 = {k1_example:.3e} N/m")
    print(f"k2 = 0.0 N/m")
    print("-" * 50)

if __name__ == "__main__":
    example_simulation_and_plot()
```
**


The tunneling energy $t$ and contact interaction $U$ for the 2D Hubbard model in the tight-binding limit are:

$$
t = \frac{4}{\sqrt{\pi}} E_R \left( \frac{V_0}{E_R} \right)^{3/4} \exp\left( -2 \sqrt{\frac{V_0}{E_R}} \right)
$$

$$
U = \frac{2\hbar^2 a_s}{m l_{\text{osc}}^2 \sqrt{\pi} l_z} = \frac{32\pi^2 \hbar^2 a_s}{m \lambda^2 \sqrt{\pi} l_z} \sqrt{\frac{V_0}{E_R}}
$$

where:
- $E_R = \dfrac{2\pi^2\hbar^2}{m\lambda^2}$ is the recoil energy,
- $V_0 = \alpha E^2$ is the potential depth,
- $l_{\text{osc}} = \dfrac{\lambda}{4\pi}\left(\dfrac{E_R}{V_0}\right)^{1/4}$ is the harmonic oscillator length in the lattice plane,
- $l_z$ is the characteristic confinement length in the $z$-direction.

The following Python code implements these formulas, computes the parameters for realistic physical inputs (using $^6$Li), and generates plots visualizing the dependence of $t$ and $U$ on the lattice depth $V_0$.

```python
import numpy as np
import matplotlib.pyplot as plt

def calculate_hubbard_parameters():
    """
    Calculates Hubbard model parameters (t and U) for fermionic atoms 
    in a 2D optical lattice using the harmonic approximation.
    """
    
    # --- 1. Physical Constants ---
    hbar = 1.054571817e-34  # Reduced Planck constant (J*s)
    kB = 1.380649e-23       # Boltzmann constant (J/K)
    amu = 1.66053906660e-27 # Atomic mass unit (kg)
    a0 = 5.29177210903e-11  # Bohr radius (m)
    
    # --- 2. System Definition: Lithium-6 ---
    # Mass of 6Li in kg
    m = 6.015 * amu
    
    # Laser wavelength (typical lattice wavelength for 6Li)
    wavelength = 767e-9  # meters
    
    # Wavenumber k
    k = 2 * np.pi / wavelength
    
    # Recoil Energy Er = hbar^2 * k^2 / (2m)
    Er = (hbar**2 * k**2) / (2 * m)
    Er_kHz = Er / (hbar * 2 * np.pi) * 1e3 # Convert to kHz for easier reading
    
    # Display basic atomic properties
    print(f"--- System Properties: 6Li ---")
    print(f"Mass: {m:.3e} kg")
    print(f"Wavelength: {wavelength*1e9:.1f} nm")
    print(f"Recoil Energy (Er): {Er_kHz:.2f} kHz")
    print("-" * 30)

    # --- 3. Interaction & Confinement Parameters ---
    # S-wave scattering length (in units of Bohr radius a0)
    # 2000 a0 is typical for strong interactions near Feshbach resonance
    as_radius Bohr = 2000 
    
    # Vertical confinement frequency (z-axis)
    # Typical value to ensure 2D behavior
    wz = 2 * np.pi * 3000 # 3 kHz
    lz = np.sqrt(hbar / (m * wz))
    
    print(f"Scattering Length (as): {as_radius_Ba0:.0f} a0")
    print(f"Vertical Freq (wz): {wz/(2*np.pi*1000):.1f} kHz")
    print(f"Vertical Confinement (lz): {lz*1e6:.2f} um")
    
    # --- 4. Variation of Lattice Depth S = V0 / Er ---
    # We analyze a range of lattice depths from 3 Er to 15 Er
    s_vals = np.linspace(3, 15, 100)
    
    # Arrays to store results
    t_vals = [] # Tunneling in Joules
    U_vals = [] # Interaction in Joules
    
    # Pre-calculate constants for the loop
    const_t = (4 / np.sqrt(np.pi)) * Er
    const_U_num = 2 * hbar**2 * (as_radius_Ba0 * a0)
    const_U_denom = m * np.sqrt(np.pi) * lz
    
    for s in s_vals:
        V0 = s * Er
        
        # Calculate Harmonic Oscillator length l_osc
        # l_osc = (wavelength / (4*pi)) * (Er / V0)^(1/4)
        l_osc = (wavelength / (4 * np.pi)) * (1 / s)**(1/4)
        
        # --- Calculate Tunneling t ---
        # t = (4/sqrt(pi)) * Er * s^(3/4) * exp(-2*sqrt(s))
        t_current = const_t * s**(3/4) * np.exp(-2 * np.sqrt(s))
        t_vals.append(t_current)
        
        # --- Calculate Interaction U ---
        # U = 2 * hbar^2 * as / (m * l_osc^2 * sqrt(pi) * lz)
        U_current = const_U_num / (const_U_denom * l_osc**2)
        U_vals.append(U_current)

    # Convert lists to numpy arrays for plotting
    t_vals = np.array(t_vals)
    U_vals = np.array(U_vals)
    
    # Calculate U/t ratio
    Ut_ratio = U_vals / t_vals

    # --- 5. Select Specific Simulation Parameters ---
    # A standard operating point for many experiments is s = 8
    s_sim = 8.0
    # Calculate specific parameters for s = 8
    l_osc_sim = (wavelength / (4 * np.pi)) * (1 / s_sim)**(1/4)
    t_sim = const_t * s_sim**(3/4) * np.exp(-2 * np.sqrt(s_sim))
    U_sim = const_U_num / (const_U_denom * l_osc_sim**2)
    
    print("-" * 30)
    print(f"--- Calculation Results for s = {s_sim} ---")
    print(f"Lattice Depth: {s_sim} Er ({s_sim*Er_kHz:.1f} kHz)")
    print(f"Harmonic Length (l_osc): {l_osc_sim*1e9:.1f} nm")
    print(f"Tunneling (t): {t_sim/hbar/2/np.pi*1000:.3f} kHz")
    print(f"Interaction (U): {U_sim/hbar/2/np.pi*1000:.3f} kHz")
    print(f"Ratio (U/t): {U_sim/t_sim:.2f}")
    print("-" * 30)

    # --- 6. Graphics ---
    # Create plots for t, U, and U/t as functions of lattice depth
    
    fig, (ax1, ax2, ax3) = plt.subplots(1, 3, figsize=(18, 5))
    
    # Plot t in units of Er
    ax1.plot(s_vals, t_vals/Er, color='blue', linewidth=2)
    ax1.set_xlabel('Lattice Depth $s = V_0/E_R$', fontsize=14)
    ax1.set_ylabel('Tunneling $t / E_R$', fontsize=14, color='blue')
    ax1.set_title('Tunneling $t$', fontsize=16)
    ax1.grid(True, linestyle='--', alpha=0.7)
    ax1.tick_params(axis='y', labelcolor='blue')
    
    # Plot U in units of Er
    ax2.plot(s_vals, U_vals/Er, color='red', linewidth=2)
    ax2.set_xlabel('Lattice Depth $s = V_0/E_R$', fontsize=14)
    ax2.set_ylabel('Interaction $U / E_R$', fontsize=14, color='red')
    ax2.set_title('On-site Interaction $U$', fontsize=16)
    ax2.grid(True, linestyle='--', alpha=0.7)
    ax2.tick_params(axis='y', labelcolor='red')
    
    # Plot U/t ratio
    ax3.plot(s_vals, Ut_ratio, color='green', linewidth=2)
    ax3.set_xlabel('Lattice Depth $s = V_0/E_R$', fontsize=14)
    ax3.set_ylabel('Ratio $U/t$', fontsize=14)
    ax3.set_title('$U/t$ Ratio', fontsize=16)
    ax3.grid(True, linestyle='--', alpha=0.7)
    
    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    calculate_hubbard_parameters()
```
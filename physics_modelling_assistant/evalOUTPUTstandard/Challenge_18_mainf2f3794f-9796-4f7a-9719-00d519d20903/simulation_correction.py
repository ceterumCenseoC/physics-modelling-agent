
```python
import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp
from scipy.constants import epsilon_0, c, pi

# ==========================================
# 1. PHYSICAL CONSTANTS & PARAMETERS
# ==========================================

# Fundamental constants are imported from scipy.constants

# Experimental Setup Parameters
# Laser wavelength (Nd:YAG)
wavelength = 1064e-9 
# Wave vector
k = 2 * np.pi / wavelength 
# Beam waist (radius)
w0 = 1.0e-6 
# Rayleigh range
z_R = np.pi * w0**2 / wavelength
# Laser Power per trap
Power = 0.3 

# Particle Parameters (Silica in Water)
radius = 50e-9
volume = (4/3) * np.pi * radius**3
# Density of silica ~2200 kg/m^3
density_particle = 2200 
mass = density_particle * volume

# Refractive indices
n_p = 1.45 # particle
n_m = 1.33 # medium (water)

# Clausius-Mossotti relation for polarizability
# alpha = 3 * eps_0 * V * (np^2 - nm^2) / (np^2 + 2*nm^2)
delectric_contrast = (n_p**2 - n_m**2) / (n_p**2 + 2*n_m**2)
alpha = 3 * epsilon_0 * volume * delectric_contrast

# Equilibrium separation distance between traps
d0 = 3.0e-6 
# Phase difference ( assumed 0 for max coupling in k1, could vary )
delta_phi = 0.0 
# k * d0
k_d0 = k * d0

# ==========================================
# 2. DERIVATION OF COEFFICIENTS
# ==========================================

# --- Single Trap Omega ---
# Formula derived: Omega^2 = (2 * alpha * Power) / (pi * m * c * eps_0 * w0^2 * z_R^2)
# Note: The c * eps_0 term comes from the normalization of Intensity to E-field squared: I = 0.5 * c * eps_0 * E^2
Omega_sq = (2 * alpha * Power) / (np.pi * mass * c * epsilon_0 * w0**2 * z_R**2)
Omega = np.sqrt(Omega_sq)

print(f"System Parameters:")
print(f"------------------")
print(f"Wavelength: {wavelength*1e9:.1f} nm")
print(f"Particle Mass: {mass:.2e} kg")
print(f"Polarizability: {alpha:.2e} C*m^2/V")
print(f"Trap Separation d0: {d0*1e6:.2f} um")
print(f"Trap Frequency Omega: {Omega/2/np.pi/1000:.2f} kHz")

# --- E-field Amplitude ---
# Intensity I = 2P / (pi * w0^2)
# I = 0.5 * c * eps_0 * E0^2  => E0 = sqrt(2I / (c * eps_0))
Intensity = 2 * Power / (np.pi * w0**2)
E0 = np.sqrt(2 * Intensity / (c * epsilon_0))

# --- Coupling Constants k1 and k2 ---
# Based on dipole-dipole interaction in far field (kd >> 1)
# k1 (Conservative term) ~ alpha1*alpha2 * E1*E2 * k^4 / (4*pi*eps_0*d0) * cos(...)
# k2 (Non-conservative/Asymmetric term) ~ alpha1*alpha2 * E1*E2 * k^3 / (4*pi*eps_0*d0^2) * sin(...)

# Prefactor common to both
# Gamma = alpha^2 * E0^2 / (4 * pi * eps_0 * d0)
Gamma = (alpha**2 * E0**2) / (4 * np.pi * epsilon_0 * d0)

# Calculate k1
# Assuming symmetric traps (E1=E2=E0) and identical particles (alpha1=alpha2=alpha)
# Cosine term
cos_phase = np.cos(k_d0 + delta_phi)
k1 = Gamma * (k**4) * cos_phase

# Calculate k2
# Sine term
sin_phase = np.sin(k_d0 + delta_phi)
k2 = Gamma * (k**3) / d0 * sin_phase

print(f"Coupling Constant k1: {k1:.2e} N/m")
print(f"Coupling Constant k2: {k2:.2e} N/m")

# ==========================================
# 3. EQUATIONS OF MOTION
# ==========================================

def equations_of_motion(t, state):
    """
    Computes derivatives for the system:
    m*z1'' = -m*Omega^2*z1 - (k1+k2)*z1 + (k1+k2)*z2
    m*z2'' = -m*Omega^2*z2 - (k1-k2)*z2 + (k1-k2)*z1
    
    State vector: [z1, v1, z2, v2]
    """
    z1, v1, z2, v2 = state
    
    # Forces
    # Acceleration of particle 1
    acc1 = (-Omega_sq * z1 - (k1 + k2)/mass * z1 + (k1 + k2)/mass * z2)
    
    # Acceleration of particle 2
    acc2 = (-Omega_sq * z2 - (k1 - k2)/mass * z2 + (k1 - k2)/mass * z1)
    
    return [v1, acc1, v2, acc2]

# ==========================================
# 4. SIMULATION
# ==========================================

# Initial conditions: small random displacement
initial_displacement = 10e-9  # 10 nm
# Particle 1 starts at +10nm, Particle 2 at -10nm
y0 = [initial_displacement, 0.0, -initial_displacement, 0.0]

# Time span: simulate for a few oscillation periods
# Period T ~ 2*pi/Omega ~ 20 microseconds
T_period = 2 * np.pi / Omega
t_span = (0, 5 * T_period)
t_eval = np.linspace(t_span[0], t_span[1], 1000)

print(f"\nSimulating for {t_span[1]*1e6:.1f} microseconds...")

solution = solve_ivp(equations_of_motion, t_span, y0, t_eval=t_eval, method='RK45')

# Extract results
t = solution.t
z1 = solution.y[0]
z2 = solution.y[2]

# ==========================================
# 5. VISUALIZATION
# ==========================================

fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(8, 8), sharex=True)

# Plot 1: Position vs Time
ax1.plot(t*1e6, z1*1e9, label=r'$z_1$ (Particle 1)', color='blue')
ax1.plot(t*1e6, z2*1e9, label=r'$z_2$ (Particle 2)', color='red', linestyle='--')
ax1.set_ylabel('Position z (nm)')
ax1.set_title('Axial Motion of Optically Bound Nanoparticles')
ax1.legend()
ax1.grid(True)

# Plot 2: Relative Position (Binding dynamics)
# z_rel = z2 - z1 represents the breathing mode of the coupled system
z_rel = z2 - z1
ax2.plot(t*1e6, z_rel*1e9, label=r'$z_{rel} = z_2 - z_1$', color='green')
ax2.set_xlabel('Time ($\mu$s)')
ax2.set_ylabel('Relative Position (nm)')
ax2.set_title('Relative Motion (Binding Mode)')
ax2.legend()
ax2.grid(True)

plt.tight_layout()

# Save the figure
plt.savefig('optical_binding_simulation.png')
print("Plot saved as 'optical_binding_simulation.png'")

# Display parameter summary on console for verification
print("\nSummary of Coupling Strength:")
print(f"Trap Stiffness k_trap = m*Omega^2 = {mass*Omega_sq:.2e} N/m")
print(f"Ratio k1/k_trap = {k1/(mass*Omega_sq)*100:.2f}%")
print(f"Ratio k2/k_trap = {k2/(mass*Omega_sq)*100:.2f}%")
```
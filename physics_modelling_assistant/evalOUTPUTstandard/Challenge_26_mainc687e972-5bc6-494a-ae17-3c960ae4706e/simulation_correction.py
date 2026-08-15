
```python
import numpy as np
import matplotlib.pyplot as plt

# ==========================================
# 1. Definition of Physical Constants
# ==========================================
# Using CODATA 2018 / SI units
e_charge = 1.602176634e-19      # Elementary charge [C]
m_electron = 9.1093837015e-31   # Electron mass [kg]
c_light = 2.99792458e8          # Speed of light [m/s]
h_bar = 1.054571817e-34         # Reduced Planck constant [J*s]
epsilon_0 = 8.8541878128e-12    # Vacuum permittivity [F/m]
alpha = 7.2973525693e-3         # Fine structure constant [dimensionless]

# ==========================================
# 2. Problem Parameters
# ==========================================
B_field = 5.0                   # Magnetic field strength [T]
R_cavity = 0.01                 # Cavity radius [m]

# ==========================================
# 3. Model Implementation
# ==========================================

def compute_classical_cyclotron_frequency(B, m, e):
    """
    Computes the classical cyclotron frequency omega_c^(0) = eB/m.
    
    Args:
        B (float): Magnetic field in Tesla.
        m (float): Particle mass in kg.
        e (float): Particle charge in Coulombs.
        
    Returns:
        float: Angular frequency in rad/s.
    """
    return (e * B) / m

def compute_cyclotron_wavelength(omega_c, c):
    """
    Computes the cyclotron wavelength lambda_c = 2*pi*c / omega_c.
    
    Args:
        omega_c (float): Cyclotron angular frequency in rad/s.
        c (float): Speed of light in m/s.
        
    Returns:
        float: Wavelength in meters.
    """
    return (2 * np.pi * c) / omega_c

def compute_cavity_shift_ratio(lambda_c, R, alpha):
    """
    Computes the dimensionless cavity shift Delta_omega_c / omega_c^(0).
    
    Formula: shift = - (alpha / (15 * pi)) * (lambda_c / (2 * pi * R))^4
    
    Args:
        lambda_c (float): Cyclotron wavelength in meters.
        R (float): Cavity radius in meters.
        alpha (float): Fine structure constant.
        
    Returns:
        float: Dimensionless frequency shift.
    """
    geometric_factor = (lambda_c / (2 * np.pi * R))**4
    coefficient = - alpha / (15 * np.pi)
    return coefficient * geometric_factor

# ==========================================
# 4. Calculations for the Given Scenario
# ==========================================

# Step 1: Compute Cyclotron Frequency
omega_c = compute_classical_cyclotron_frequency(B_field, m_electron, e_charge)

# Step 2: Compute Cyclotron Wavelength
lambda_c = compute_cyclotron_wavelength(omega_c, c_light)

# Step 3: Compute Dimensionless Cavity Shift
dim_shift = compute_cavity_shift_ratio(lambda_c, R_cavity, alpha)

# ==========================================
# 5. Output Results
# ==========================================

print(f"--- Model Implementation Results ---\n")
print(f"Input Parameters:")
print(f"  Magnetic Field (B): {B_field} T")
print(f"  Cavity Radius (R):  {R_cavity*100} cm\n")

print(f"Computed Intermediate Values:")
print(f"  Cyclotron Frequency (omega_c^(0)): {omega_c:.4e} rad/s")
print(f"  Cyclotron Wavelength (lambda_c):   {lambda_c:.6e} m ({lambda_c*1000:.4f} mm)\n")

print(f"Final Result:")
print(f"  Dimensionless Cavity Shift (Delta_omega_c / omega_c^(0)): {dim_shift:.4e}")
print(f"  Rounded to 3 significant figures: {dim_shift:.2e}")

# ==========================================
# 6. Visualization (Sensible Graphics)
# ==========================================
# Visualizing the dependence of the shift on the Cavity Radius R.
# The shift scales as 1/R^4.

radii = np.linspace(0.5, 5.0, 100) * 0.01 # Radii from 0.5 cm to 5.0 cm
shifts = [compute_cavity_shift_ratio(lambda_c, r, alpha) for r in radii]

plt.figure(figsize=(8, 5))
plt.semilogy(radii * 100, np.abs(shifts), marker='.', linestyle='-')
plt.title(r'Dependence of Cavity Shift $|\Delta \omega_c / \omega_c^{(0)}|$ on Radius $R$')
plt.xlabel(r'Cavity Radius $R$ [cm]')
plt.ylabel(r'Absolute Shift Magnitude $|\Delta \omega_c / \omega_c^{(0)}|$')
plt.grid(True, which="both", ls="-")
plt.axvline(x=R_cavity*100, color='r', linestyle='--', label=f'Operating Point R={R_cavity*100} cm')
plt.legend()
plt.show()

# Visualizing the dependence of the shift on the Magnetic Field B.
# The shift depends on B through lambda_c ~ 1/B.
# Shift ~ (1/B)^4.

fields = np.linspace(1.0, 10.0, 100) # Magnetic fields from 1 T to 10 T
shifts_B = []
for B in fields:
    w_c = compute_classical_cyclotron_frequency(B, m_electron, e_charge)
    l_c = compute_cyclotron_wavelength(w_c, c_light)
    s = compute_cavity_shift_ratio(l_c, R_cavity, alpha)
    shifts_B.append(s)

plt.figure(figsize=(8, 5))
plt.semilogy(fields, np.abs(shifts_B), color='g', marker='.', linestyle='-')
plt.title(r'Dependence of Cavity Shift $|\Delta \omega_c / \omega_c^{(0)}|$ on Magnetic Field $B$')
plt.xlabel(r'Magnetic Field $B$ [Tesla]')
plt.ylabel(r'Absolute Shift Magnitude $|\Delta \omega_c / \omega_c^{(0)}|$')
plt.grid(True, which="both", ls="-")
plt.axvline(x=B_field, color='r', linestyle='--', label=f'Operating Point B={B_field} T')
plt.legend()
plt.show()
```
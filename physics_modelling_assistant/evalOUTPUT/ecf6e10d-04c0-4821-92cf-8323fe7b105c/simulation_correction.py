```python
import math

def calculate_cavity_shift():
    """
    Calculates the dimensionless cavity shift for an electron in a Penning trap
    based on the theoretical framework and parameters provided.
    """
    # --- Define Constants (SI units) ---
    # Elementary charge (C)
    e = 1.602176634e-19
    # Electron mass (kg)
    m_e = 9.1093837e-31
    # Speed of light (m/s)
    c = 2.99792458e8
    # Fine-structure constant (dimensionless)
    alpha = 7.297352569e-3
    # Pi
    pi = math.pi

    # --- Define Trap and Cavity Parameters ---
    # Magnetic field strength (T)
    B = 5.0
    # Cavity radius (m)
    R = 0.01

    # --- 1. Calculate Unperturbed Cyclotron Frequency (rad/s) ---
    # Formula: omega_c_0 = (e * B) / m_e
    omega_c_0 = (e * B) / m_e

    # --- 2. Calculate Wave Number (1/m) ---
    # Formula: k = omega_c_0 / c
    k = omega_c_0 / c

    # --- 3. Calculate Dimensionless Cavity Shift ---
    # Formula: Delta_omega_c / omega_c_0 = - (5 * alpha) / (8 * pi * k * R)
    # The term k * R is evaluated first for clarity
    kR = k * R
    cavity_shift_ratio = - (5 * alpha) / (8 * pi * kR)

    # --- Output Results ---
    # Print physical constants and parameters used
    print(f"--- Physical Parameters ---")
    print(f"Elementary charge (e):      {e:.3e} C")
    print(f"Electron mass (m_e):        {m_e:.3e} kg")
    print(f"Speed of light (c):         {c:.3e} m/s")
    print(f"Fine-structure constant (alpha): {alpha:.3e}")
    print(f"Magnetic field (B):         {B:.1f} T")
    print(f"Cavity radius (R):          {R:.3f} m")
    print("")

    # Print intermediate calculations
    print(f"--- Intermediate Calculations ---")
    print(f"Cyclotron frequency (omega_c_0): {omega_c_0:.5e} rad/s")
    print(f"Wave number (k):                 {k:.5e} m^-1")
    print(f"Dimensionless size (kR):         {kR:.5f}")
    print("")

    # Print final result
    print(f"--- Final Result ---")
    # The theoretical value in the context is approx -4.94 * 10^-5
    # We print with high precision to verify.
    print(f"Dimensionless cavity shift (Delta_omega_c / omega_c_0): {cavity_shift_ratio:.5e}")
    
    # Return the calculated value for potential further use
    return cavity_shift_ratio

if __name__ == "__main__":
    calculate_cavity_shift()
```

```python
import numpy as np
import matplotlib.pyplot as plt

def calculate_edelstein_effect():
    """
    Implements the Rashba-Edelstein effect model based on the provided 
    mathematical description and dimensional analysis.
    
    The model calculates the induced magnetization M in response to an 
    electric field E for a 2D Rashba system.
    """
    
    # --- 1. Physical Constants (SI Units) ---
    mu_B = 9.274e-24      # Bohr magneton [J/T]
    e = 1.602e-19         # Elementary charge [C]
    hbar = 1.054e-34      # Reduced Planck constant [J*s]
    m_e = 9.109e-31       # Electron mass [kg]

    # --- 2. Model Parameters ---
    # Based on the suggested starting parameters for a "Giant" Rashba system
    # (e.g., Bi/Ag interface or similar heavy metal/semiconductor heterostructure)
    
    tau = 1.0e-12         # Relaxation time [s] (1 ps)
    
    # Alpha_R: Rashba SOC strength.
    # Note: In the Hamiltonian H = alpha_R * (p x sigma), alpha_R has units of velocity.
    # However, the formula for susceptibility is often derived with alpha_R having units
    # of Energy*Length (let's call it alpha_R_prime) where alpha_R_prime = alpha_R * hbar.
    # The provided formulas for Chi use the form (m * alpha_R) / hbar^2.
    # To be consistent with the Python code provided in the prompt context which uses
    # alpha_R in eV*m (Energy*Length), we define it here in J*m.
    # The dispersion relation E = hbar^2 k^2 / 2m +/- alpha_R * k implies alpha_R has units of Energy*Length.
    alpha_R_eVm = 3.0e-11 # Rashba parameter [eV*m]
    alpha_R = alpha_R_eVm * e # Convert to [J*m]
    
    m = 0.5 * m_e         # Effective mass [kg]
    
    # Fermi Energies for different regimes
    # High-Density Regime (HDR): E_F > m*alpha_R^2 / (2*hbar^2)
    # Low-Density Regime (LDR): E_F < m*alpha_R^2 / (2*hbar^2)
    
    # Calculate the characteristic energy scale (band crossing point)
    # Note: Using the form consistent with alpha_R [J*m]
    # The minimum of the upper band is at E = -m*alpha_R^2 / (2*hbar^2)
    Delta = (m * alpha_R**2) / (2 * hbar**2)
    
    E_F_HDR = 0.1 * e     # 0.1 eV (Safely in HDR)
    E_F_LDR = 0.002 * e   # 0.002 eV (In LDR, close to band bottom)

    print(f"--- Model Parameters ---")
    print(f"Relaxation time (tau): {tau*1e12:.2f} ps")
    print(f"Rashba Strength (alpha_R): {alpha_R_eVm:.2e} eV*m")
    print(f"Effective Mass (m): {m/m_e:.2f} m_e")
    print(f"Characteristic Energy (Delta): {Delta/e:.4f} eV")
    print(f"Fermi Energy HDR: {E_F_HDR/e:.3f} eV")
    print(f"Fermi Energy LDR: {E_F_LDR/e:.3f} eV")

    # --- 3. Susceptibility Functions ---
    
    def get_susceptibility_HDR(m, alpha_R, tau):
        """
        Calculates susceptibility for High-Density Regime.
        Formula: chi = (mu_B * e * tau * m * alpha_R) / (2 * pi * hbar^2)
        Units check: 
        mu_B [J/T], e [C], tau [s], m [kg], alpha_R [J*m], hbar [J*s]
        Result: (J/T * C * s * kg * J*m) / (J^2 * s^2) = C^2 * m / (J * s)
        M/E units: (A/m) / (V/m) = A/V = C^2 / (J * s).
        Consistent.
        """
        return (mu_B * e * tau * m * alpha_R) / (2 * np.pi * hbar**2)

    def get_susceptibility_LDR(m, alpha_R, tau, E_F):
        """
        Calculates susceptibility for Low-Density Regime.
        Formula: chi = (mu_B * e * tau * sqrt(m^2 * alpha_R^2 + 2 * m * E_F)) / (2 * pi * hbar^2)
        """
        term = np.sqrt((m**2 * alpha_R**2) + (2 * m * E_F))
        return (mu_B * e * tau * term) / (2 * np.pi * hbar**2)

    # Calculate susceptibilities
    chi_HDR = get_susceptibility_HDR(m, alpha_R, tau)
    chi_LDR = get_susceptibility_LDR(m, alpha_R, tau, E_F_LDR)

    print(f"\n--- Calculated Susceptibilities ---")
    print(f"Chi_HDR: {chi_HDR:.2e} A/V (or A*m/V)")
    print(f"Chi_LDR: {chi_LDR:.2e} A/V (or A*m/V)")

    # --- 4. Visualization ---

    # Figure 1: Magnetization vs Electric Field Magnitude
    E_mag_range = np.linspace(0, 1e6, 100) # 0 to 1 MV/m
    
    # M = chi * E
    M_HDR = chi_HDR * E_mag_range
    M_LDR = chi_LDR * E_mag_range

    plt.figure(figsize=(8, 5))
    plt.plot(E_mag_range/1e6, M_HDR, label='HDR ($E_F = 0.1$ eV)', linewidth=2, color='tab:blue')
    plt.plot(E_mag_range/1e6, M_LDR, label='LDR ($E_F = 0.002$ eV)', linewidth=2, color='tab:orange', linestyle='--')
    
    plt.xlabel('Electric Field Magnitude |E| [MV/m]', fontsize=12)
    plt.ylabel('Magnetization |M| [A/m]', fontsize=12)
    plt.title('Edelstein Magnetization vs Electric Field', fontsize=14)
    plt.legend(fontsize=12)
    plt.grid(True, alpha=0.3)
    plt.tight_layout()
    plt.show()

    # Figure 2: Magnetization Direction Vector Field
    # M = chi * (z_hat x E)
    # Mx = -chi * Ey
    # My = chi * Ex
    
    theta_E = np.linspace(0, 2*np.pi, 16)
    E0 = 1e6 # 1 MV/m reference magnitude for direction plot
    
    Ex = E0 * np.cos(theta_E)
    Ey = E0 * np.sin(theta_E)
    
    # Calculate M vectors using HDR susceptibility
    Mx = -chi_HDR * Ey
    My = chi_HDR * Ex
    
    # Normalize vectors for visualization of direction
    # (Magnitude is already handled in Fig 1, here we show the relationship)
    M_mag = np.sqrt(Mx**2 + My**2)
    
    plt.figure(figsize=(6, 6))
    # Plot E field (Black)
    plt.quiver(Ex/1e6, Ey/1e6, Ex/1e6, Ey/1e6, color='black', 
               angles='xy', scale_units='xy', scale=1, width=0.005, label='E Field')
    
    # Plot M field (Blue, scaled to be visible alongside E)
    # Note: Actual magnitude of M is much smaller than E in SI units, 
    # so we scale M vectors for the plot to show direction clearly.
    scale_factor = (E0/1e6) / (chi_HDR * E0) * 0.8 # Scale to fit plot
    plt.quiver(Ex/1e6, Ey/1e6, Mx*scale_factor, My*scale_factor, color='tab:blue', 
               angles='xy', scale_units='xy', scale=1, width=0.005, label='Magnetization')
    
    plt.xlabel('$E_x$ [MV/m]', fontsize=12)
    plt.ylabel('$E_y$ [MV/m]', fontsize=12)
    plt.title('Direction of Induced Magnetization', fontsize=14)
    plt.legend(loc='upper right', fontsize=12)
    plt.axis('equal')
    plt.grid(True, alpha=0.3)
    plt.tight_layout()
    plt.show()

    # Figure 3: Susceptibility vs Rashba SOC Strength
    # Vary alpha_R from 0.5x to 2.0x the base value
    alpha_factors = np.linspace(0.5, 2.0, 50)
    alpha_values = alpha_factors * alpha_R_eVm # in eV*m
    
    chi_vs_alpha = []
    for a_val in alpha_values:
        a_J = a_val * e
        # Assuming HDR for this scan (using fixed E_F_HDR)
        # We must check if we remain in HDR for all alpha values
        # Delta = m * a^2 / 2hbar^2. 
        # If alpha increases, Delta increases. 
        # Max alpha = 2 * base -> Delta increases by 4.
        # Base Delta ~ 0.004 eV. Max Delta ~ 0.016 eV.
        # E_F_HDR = 0.1 eV. So we stay in HDR.
        c = get_susceptibility_HDR(m, a_J, tau)
        chi_vs_alpha.append(c)
        
    plt.figure(figsize=(8, 5))
    plt.plot(alpha_values/1e-11, np.array(chi_vs_alpha), color='tab:green', linewidth=2)
    plt.xlabel('Rashba Parameter $\\alpha_R$ [$10^{-11}$ eV$\cdot$m]', fontsize=12)
    plt.ylabel('Susceptibility $\\chi$ [A/V]', fontsize=12)
    plt.title('Dependence of Susceptibility on SOC Strength', fontsize=14)
    plt.grid(True, alpha=0.3)
    plt.tight_layout()
    plt.show()
    
    # Figure 4: Chirality Dependence
    # The sign of alpha_R determines the chirality.
    # Positive alpha_R -> M rotates +90 deg from E (Counter-Clockwise)
    # Negative alpha_R -> M rotates -90 deg from E (Clockwise)
    
    alpha_R_neg = -alpha_R_eVm * e
    chi_HDR_neg = get_susceptibility_HDR(m, alpha_R_neg, tau)
    
    Mx_neg = -chi_HDR_neg * Ey
    My_neg = chi_HDR_neg * Ex
    
    plt.figure(figsize=(12, 5))
    
    plt.subplot(1, 2, 1)
    plt.title(f'Chirality + ($\\alpha_R > 0$)', fontsize=12)
    plt.quiver(Ex/1e6, Ey/1e6, Mx*scale_factor, My*scale_factor, color='tab:blue', 
               angles='xy', scale_units='xy', scale=1)
    plt.xlabel('$E_x$'); plt.ylabel('$E_y$')
    plt.axis('equal'); plt.grid(True, alpha=0.3)
    plt.text(0, -1.2, "M is rotated $+90^\\circ$ from E", ha='center')

    plt.subplot(1, 2, 2)
    plt.title(f'Chirality - ($\\alpha_R < 0$)', fontsize=12)
    plt.quiver(Ex/1e6, Ey/1e6, Mx_neg*scale_factor, My_neg*scale_factor, color='tab:red', 
               angles='xy', scale_units='xy', scale=1)
    plt.xlabel('$E_x$'); plt.ylabel('$E_y$')
    plt.axis('equal'); plt.grid(True, alpha=0.3)
    plt.text(0, -1.2, "M is rotated $-90^\\circ$ from E", ha='center')
    
    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    calculate_edelstein_effect()
```
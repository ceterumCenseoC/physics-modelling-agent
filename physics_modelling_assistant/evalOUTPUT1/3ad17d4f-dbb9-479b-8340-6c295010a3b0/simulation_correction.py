```python
import numpy as np
import matplotlib.pyplot as plt

def simulate_goniopolar():
    # ==========================================
    # 1. CONSTANTS AND PARAMETERS
    # ==========================================
    
    # Fundamental Constants
    e = 1.602e-19          # Elementary charge [C]
    kB = 1.381e-23         # Boltzmann constant [J/K]
    h = 6.626e-34          # Planck constant [J*s]
    hbar = h / (2 * np.pi) # Reduced Planck constant [J*s]
    m0 = 9.109e-31         # Free electron mass [kg]
    
    # System Environment
    T = 300.0              # Temperature [K]
    
    # Material Properties
    Delta_eV = 0.5         # Bandgap [eV]
    Delta = Delta_eV * e   # Bandgap [J]
    
    # Effective Masses (Anisotropic)
    # Scenario: p-like behavior in x, n-like in y
    # Derived from the context parameters
    mc_x = 0.15 * m0       # Conduction mass x [kg]
    mv_x = 0.50 * m0       # Valence mass x [kg]
    mc_y = 1.00 * m0       # Conduction mass y [kg]
    mv_y = 0.30 * m0       # Valence mass y [kg]
    
    # Transport Parameters
    tau = 1.0e-13          # Relaxation time [s]
    
    # ==========================================
    # 2. DERIVATION/LOGIC IMPLEMENTATION
    # ==========================================
    
    # Intrinsic Condition: n = p
    # We use the characteristic energy for non-degenerate 2D semiconductors
    # The Seebeck term <E - mu> ~ Delta/2 + kBT (approx) - mu.
    # For intrinsic undoped case, chemical potential is roughly at the center of the gap.
    # Here we define the central energy term epsilon_0.
    # Note: For the precise sign determination, we only need the relative conductivities.
    # However, to calculate magnitudes, we define n.
    
    # Calculate intrinsic carrier density n_i
    # n_i = (2*pi*m_dos*kBT / h^2) * exp(-Delta / (2*kBT))
    # We need the reduced DOS mass. m_dos = sqrt(mx * my) usually for 2D ellipsoids
    # From the derivation logic:
    m_dos_c = np.sqrt(mc_x * mc_y)
    m_dos_v = np.sqrt(mv_x * mv_y)
    
    # Exact intrinsic carrier density involves solving for mu such that n = p.
    # For non-degenerate, n = 2 * (2*pi*m_c*kBT/h^2) * exp((mu - Ec)/kBT)
    # p = 2 * (2*pi*m_v*kBT/h^2) * exp((Ev - mu)/kBT)
    # This implies exp(2*mu/kB*T) * (m_c/m_v) = exp((Ec+Ev)/kBT) = exp(0) if mid-gap at 0.
    # With Ec = Delta/2, Ev = -Delta/2.
    # mu = (1/2)*(Ec+Ev) + (1/2)*kB*T * ln(m_v/m_c) = 0 + (1/2)*kB*T * ln(m_v/m_c)
    
    # Chemical Potential [J]
    mu_intrinsic = (kB * T / 2.0) * np.log(m_dos_v / m_dos_c)
    
    # Intrinsic density [m^-2]
    # Prefactor A = 2 * pi * m * kB * T / h^2
    prefactor_c = 2 * np.pi * m_dos_c * kB * T / (h**2)
    n_i = prefactor_c * np.exp((mu_intrinsic - Delta/2) / (kB * T))
    
    # ==========================================
    # 3. TRANSPORT COEFFICIENT CALCULATION
    # ==========================================
    
    print(f"--- Simulation Parameters ---")
    print(f"Temperature: {T} K")
    print(f"Bandgap: {Delta_eV} eV")
    print(f"Chemical Potential: {mu_intrinsic/e:.4f} eV (Relative to mid-gap)")
    print(f"Intrinsic Carrier Density: {n_i:.4e} m^-2")
    
    # Conductivity Tensor Components
    # sigma = n * e^2 * tau / m
    # Since n = p, the condictivity ratio is purely mass-dependent.
    
    sigma_c_x = (n_i * e**2 * tau) / mc_x
    sigma_v_x = (n_i * e**2 * tau) / mv_x
    
    sigma_c_y = (n_i * e**2 * tau) / mc_y
    sigma_v_y = (n_i * e**2 * tau) / mv_y
    
    # Total Conductivity (Intrinsic, n=p, so currents add, signs handled in Seebeck)
    sigma_tot_x = sigma_c_x + sigma_v_x
    sigma_tot_y = sigma_c_y + sigma_v_y
    
    # Calculate Energy Average <E - mu>
    # For non-degenerate 2D parabolic bands, <E> = Ec + kB*T (electrons), <E> = Ev - kB*T (holes)
    # So <E - mu>_c = (Delta/2 + kB*T - mu) = epsilon_c
    #    <E - mu>_v = (-Delta/2 - kB*T - mu) = - (Delta/2 + kB*T + mu)
    # However, the hole flux carries +e.
    # Term in Seebeck numerator: sigma_c*<E-mu>_c - sigma_v*<mu-E>_v
    #                    = sigma_c*(Delta/2 + kBT - mu) - sigma_v*(Delta/2 + kBT + mu)
    
    eps_del = Delta / 2.0
    kT = kB * T
    
    term_c = eps_del + kT - mu_intrinsic
    term_v = eps_del + kT + mu_intrinsic 
    
    # The physical intuition from the simplified model is that if masses are balanced,
    # S goes to zero. The sign depends on (sigma_c/mu_term - sigma_v/mu_term).
    # Using the full expression:
    numerator_x = sigma_c_x * term_c - sigma_v_x * term_v
    numerator_y = sigma_c_y * term_c - sigma_v_y * term_v
    
    # Seebeck Coefficient S = (1/eT) * (L1 / L0) = (1/eT) * (Numerator / Sigma_tot)
    S_x = (1 / (e * T)) * (numerator_x / sigma_tot_x)
    S_y = (1 / (e * T)) * (numerator_y / sigma_tot_y)
    
    print(f"\n--- Transport Results ---")
    print(f"Conductivity x: {sigma_tot_x:.4e} S/m")
    print(f"Conductivity y: {sigma_tot_y:.4e} S/m")
    print(f"Seebeck Coefficient x: {S_x*1e6:.2f} uV/K")
    print(f"Seebeck Coefficient y: {S_y*1e6:.2f} uV/K")
    
    # Verify Condition
    cond_val = (mv_x - mc_x) * (mv_y - mc_y)
    print(f"\n--- Goniopolarity Condition ---")
    print(f"(mv_x - mc_x) = {(mv_x - mc_x)/m0:.2f} m0")
    print(f"(mv_y - mc_y) = {(mv_y - mc_y)/m0:.2f} m0")
    print(f"Product: {cond_val:.2e}")
    
    if cond_val < 0:
        print("Condition (mv_x - mc_x)(mv_y - mc_y) < 0 is MET.")
        if S_x * S_y < 0:
            print("Result: Goniopolarity CONFIRMED (S_x and S_y have opposite signs).")
        else:
            print("Result: Goniopolarity condition met numerically, but signs did not flip.")
            print("This might happen if mu is far from center or T is very high.")
    else:
        print("Condition NOT MET. Material is unipolar.")
        
    return S_x, S_y

if __name__ == "__main__":
    S_x, S_y = simulate_goniopolar()
    
    # Optional: Visualization
    # Let's visualize how S_x and S_y evolve with a scaling of the anisotropy
    # We scale mv_x and mv_y together to keep the "cross" nature
    
    print("\nGenerating anisotropy sweep visual...")
    
    # Base values
    mc_x_base = 0.15 * 9.109e-31
    mv_x_base = 0.50 * 9.109e-31
    mc_y_base = 1.00 * 9.109e-31
    mv_y_base = 0.30 * 9.109e-31
    
    scaling_factors = np.linspace(0.1, 10.0, 100)
    S_x_vals = []
    S_y_vals = []
    
    # Re-constants for loop
    e = 1.602e-19
    kB = 1.381e-23
    h = 6.626e-34
    T = 300.0
    Delta = 0.5 * e
    tau = 1.0e-13
    
    # Ideally we recalculate mu for every step, but for qualitative shape of sign flip
    # assuming mu ~ 0 is often sufficient to show the logic. 
    # However, let's do it right: calc mu for every step.
    
    for s in scaling_factors:
        # Apply scaling to the valence masses for this iteration
        # We vary the 'strength' of the anisotropy
        mvc_x = mv_x_base * s
        mvc_y = mv_y_base * s
        
        # Recalc DOS
        mdos_c = np.sqrt(mc_x_base * mc_y_base)
        mdos_v = np.sqrt(mvc_x * mvc_y)
        
        mu = (kB * T / 2.0) * np.log(mdos_v / mdos_c)
        
        # Density
        n = (2 * np.pi * mdos_c * kB * T / (h**2)) * np.exp((mu - Delta/2) / (kB * T))
        
        # Conductivities
        sig_cx = n * e**2 * tau / mc_x_base
        sig_vx = n * e**2 * tau / mvc_x
        sig_cy = n * e**2 * tau / mc_y_base
        sig_vy = n * e**2 * tau / mvc_y
        
        # Seebecks
        num_x = sig_cx * (Delta/2 + kB*T - mu) - sig_vx * (Delta/2 + kB*T + mu)
        num_y = sig_cy * (Delta/2 + kB*T - mu) - sig_vy * (Delta/2 + kB*T + mu)
        
        Sx = (num_x / (sig_cx + sig_vx)) / (e * T)
        Sy = (num_y / (sig_cy + sig_vy)) / (e * T)
        
        S_x_vals.append(Sx * 1e6) # to uV/K
        S_y_vals.append(Sy * 1e6)
        
    plt.figure(figsize=(8, 5))
    plt.plot(scaling_factors, S_x_vals, label='$S_x$ (along x)', color='r')
    plt.plot(scaling_factors, S_y_vals, label='$S_y$ (along y)', color='b')
    plt.axhline(0, color='black', linestyle='--', linewidth=0.8)
    plt.axvline(np.sqrt((mv_x_base/mc_y_base)/(mv_y_base/mc_x_base)), color='gray', linestyle=':', label='Isotropic Mass Ratio Point')
    plt.xscale('log')
    plt.xlabel('Anisotropy Scaling Factor (Valence Masses)')
    plt.ylabel('Seebeck Coefficient [$\mu V/K$]')
    plt.title('Goniopolarity: Seebeck Coefficient vs. Mass Anisotropy')
    plt.legend()
    plt.grid(True, which="both", ls="-", alpha=0.2)
    plt.tight_layout()
    plt.show()
```
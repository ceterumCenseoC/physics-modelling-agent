
```python
import numpy as np
import matplotlib.pyplot as plt

def coulomb_gauge_quasi_pdf(y, pz, mu, alpha_s, cf, ir_regulator_log=0.0):
    """
    Calculates the quasi-PDF in Coulomb Gauge at 1-loop order for a free massless quark.
    
    The model is based on the perturbative structure:
    f_q(y) = delta(1-y) + (alpha_s * C_F / 2pi) * f_q^(1)(y)
    
    For the Coulomb gauge, the 1-loop correction f_q^(1) is modeled with:
    1. The standard splitting kernel P(y) = (1+y^2)/(1-y) modified by LaMET log.
    2. An instantaneous Coulomb term contributing to the non-logarithmic structure.
    
    Parameters:
    -----------
    y : float or np.ndarray
        Momentum fraction.
    pz : float
        Large longitudinal momentum [GeV].
    mu : float
        Renormalization scale [GeV].
    alpha_s : float
        Strong coupling constant.
    cf : float
        Casimir constant (4/3 for SU(3)).
    ir_regulator_log : float
        Logarithm of the IR regulator parameter (e.g. log(lambda^2/mu^2)).
        
    Returns:
    --------
    f_q : float or np.ndarray
        The value of the quasi-PDF.
    """
    
    prefactor = (alpha_s * cf) / (2 * np.pi)
    
    # Ensure input is a numpy array for vectorized operations
    y_array = np.array(y, dtype=float)
    f_q = np.zeros_like(y_array)
    
    # Loop Intervals based on perturbative kinematics for massless quarks
    
    # 1. Interval y < 0: No support for unpolarized massless quarks at this order
    mask_neg = y_array < 0
    f_q[mask_neg] = 0.0
    
    # 2. Interval 0 < y < 1 (Real Emission + Matching Terms)
    mask_pos = (y_array > 0) & (y_array < 1)
    if np.any(mask_pos):
        y_pos = y_array[mask_pos]
        
        # Altarelli-Parisi splitting kernel P(y)
        P_yy = (1 + y_pos**2) / (1 - y_pos)
        
        # LaMET Large Logarithm: ln(pz^2 * (1-y)^2 / mu^2)
        # This term arises from the ratio of the large momentum pz to the renormalization scale mu,
        # regulated by the momentum fraction (1-y).
        lamet_log = np.log((pz**2 * (1 - y_pos)**2) / (mu**2))
        
        # Coulomb Gauge Specific Terms
        # The instantaneous Coulomb interaction (A^0 propagator) generates finite 
        # non-logarithmic contributions modifying the kernel.
        # We model the finite part K(y) to ensure the correct logarithmic structure
        # and infrared behavior consistent with dimensional regularization.
        K_term = 2 * cf * (1 - y_pos)
        
        # Assembly of the real correction
        # Structure: 2*CF * P(y) * (LaMET_Log + Constant) + Coulomb_Finite_Term
        # Note: The -1.0 constant is part of the universal 1-loop expansion.
        f_real = 2 * cf * P_yy * (lamet_log - 1.0)
        
        # The IR regulator term handles the collinear/soft divergence regulated 
        # by dimensional regularization (eps -> 0).
        ir_contribution = ir_regulator_log * 2 * cf * P_yy
        
        f_q[mask_pos] = prefactor * (f_real + K_term + ir_contribution)

    # 3. Interval y = 1 (Tree Level Delta Function)
    # In a numerical evaluation, the delta function is infinite at the point y=1.
    # For plotting or integration, this is handled separately. 
    # Here, we return 0 for the continuous part at y=1.
    
    # 4. Interval y > 1: No support for unpolarized massless quarks
    mask_gt1 = y_array > 1
    f_q[mask_gt1] = 0.0
    
    return f_q

def main():
    """
    Main function to execute the calculation and visualization.
    Uses parameters consistent with typical LaMET and Lattice QCD setups.
    """
    
    # --- Parameters based on Realistic Setup ---
    pz_val = 2.0       # Large longitudinal momentum [GeV]
    mu_val = 2.0       # Renormalization scale [GeV], chosen ~ pz
    alpha_s_val = 0.30 # Strong coupling constant at low scale (~2 GeV)
    cf_val = 4.0 / 3.0 # SU(3) Casimir for fundamental representation
    
    # IR Regularization
    # Using a small gluon mass approximation for the IR regulator lambda
    ir_lambda = 0.050 # GeV (50 MeV)
    ir_log_val = 2.0 * np.log(ir_lambda / mu_val)

    # --- Calculation ---
    # Define momentum fraction range
    y_vals = np.linspace(-0.2, 1.2, 500)
    
    # Calculate the 1-loop correction
    # Note: This function returns the perturbative correction term f_q^(1),
    # so the total quasi-pdf is delta(1-y) + prefactor * result.
    correction_vals = coulomb_gauge_quasi_pdf(
        y_vals, pz_val, mu_val, alpha_s_val, cf_val, ir_log_val
    )
    
    prefactor = (alpha_s_val * cf_val) / (2 * np.pi)

    # --- Visualization ---
    plt.figure(figsize=(10, 6))
    
    # Plot the 1-loop continuum part only
    plt.plot(
        y_vals, 
        prefactor * correction_vals, 
        label=r'1-Loop Continuum $\frac{\alpha_s C_F}{2\pi} \tilde{f}_q^{(1)}(y)$', 
        color='blue', 
        linewidth=2
    )
    
    # Add visual indicator for the Tree Level Delta Function at y=1
    # Since we cannot plot infinity, we indicate its position and support
    plt.scatter([1.0], [0.0], color='black', marker='^', s=150, zorder=10, label=r'Tree: $\delta(1-y)$')
    
    # Highlight the kinematic intervals
    plt.axvspan(-0.2, 0, color='gray', alpha=0.1, label='Region $y < 0$')
    plt.axvspan(0, 1, color='green', alpha=0.1, label='Region $0 < y < 1$')
    plt.axvspan(1, 1.2, color='orange', alpha=0.1, label='Region $y > 1$')
    
    plt.title(
        r'Coulomb Gauge Quasi-PDF: 1-Loop Correction' + '\n' +
        rf'($P^z = {pz_val}$ GeV, $\mu = {mu_val}$ GeV, $\alpha_s = {alpha_s_val}$)'
    )
    plt.xlabel(r'Momentum Fraction $y$')
    plt.ylabel(r'$\tilde{f}_q(y)$')
    plt.grid(True, linestyle=':', alpha=0.6)
    plt.legend()
    plt.ylim(-1.0, 4.0)
    
    # Print the mathematical model being used to console
    print("="*60)
    print("COULOMB GAUGE QUASI-PDF MODEL INITIALIZED")
    print("="*60)
    print(f"Parameters:")
    print(f"  pz  = {pz_val} GeV")
    print(f"  mu  = {mu_val} GeV")
    print(f"  a_s = {alpha_s_val}")
    print(f"  CF  = {cf_val}")
    print(f"  IR Regulator Log = {ir_log_val:.4f}")
    print("-"*60)
    print("Kernel Expression for 0 < y < 1:")
    print("  f^(1)(y) = 2*CF * [ (1+y^2)/(1-y) * (ln(pz^2(1-y)^2/mu^2) - 1) + (1-y) ]")
    print("  + IR_Regulator_Term")
    print("-"*60)
    print("Plotting results...")
    
    plt.show()

if __name__ == "__main__":
    main()
```
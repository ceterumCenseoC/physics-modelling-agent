
```python
import numpy as np
import matplotlib.pyplot as plt

# System constants for QCD
CF = 4.0 / 3.0  # Casimir constant for SU(3)

def calculate_f_1_loop(y, pz, mu, eps_ir):
    """
    Calculates the 1-loop correction to the Coulomb Gauge quasi-PDF 
    based on the provided formula.

    Parameters:
    -----------
    y : array_like
        Momentum fraction.
    pz : float
        Longitudinal momentum of the hadron/state (in GeV).
    mu : float
        Renormalization scale (in GeV).
    eps_ir : float
        Infrared regularization parameter (1/epsilon). 
        For the renormalized result (MS-bar), this pole part is subtracted.
        To visualize the finite structure, pass 0. For the bare expression, 
        pass the divergence value.

    Returns:
    --------
    f1 : array_like
        The 1-loop correction term tilde{f}_q^{(1)}.
    """
    f1 = np.zeros_like(y, dtype=np.float64)
    
    # Precompute the common logarithmic term dependent on scales
    # ln(4 pz^2 / mu^2)
    log_term = np.log(4.0 * pz**2 / mu**2)
    
    # Region 1: y < 0
    # Contribution is 0 according to the derivation
    mask_neg = (y < 0)
    # f1[mask_neg] = 0.0 (default initialization)

    # Region 2: 0 < y < 1
    # Formula: (1+y^2)/(1-y) * [1/eps + ln(...) - ln(1-y) + 1/2] - 1/(2(1-y))
    mask_pos = (y > 0) & (y < 1)
    
    if np.any(mask_pos):
        y_pos = y[mask_pos]
        
        # Calculate the splitting function part (1+y^2)/(1-y)
        kernel = (1.0 + y_pos**2) / (1.0 - y_pos)
        
        # Calculate the bracket [ ... ]
        bracket = (1.0 / eps_ir) + log_term - np.log(1.0 - y_pos) + 0.5
        
        # Calculate the subtraction term -1/(2(1-y))
        const_term = 1.0 / (2.0 * (1.0 - y_pos))
        
        f1[mask_pos] = kernel * bracket - const_term

    # Region 3: y > 1
    # Formula: (1+y^2)/(y-1) * [1/eps + ln(...) - ln(y-1) + 1/2] - 1/(2(y-1))
    mask_large = (y > 1)
    
    if np.any(mask_large):
        y_large = y[mask_large]
        
        kernel_large = (1.0 + y_large**2) / (y_large - 1.0)
        bracket_large = (1.0 / eps_ir) + log_term - np.log(y_large - 1.0) + 0.5
        const_term_large = 1.0 / (2.0 * (y_large - 1.0))
        
        f1[mask_large] = kernel_large * bracket_large - const_term_large
        
    return f1

def main():
    # --- Realistic Starting Parameters ---
    
    # Hadron Momentum (pz): 2.0 GeV
    # Justification: This is a sufficiently high momentum to satisfy the LaMET condition
    # pz >> Lambda_QCD (~0.2 GeV), minimizing power corrections Lambda^2/pz^2,
    # while remaining accessible to Lattice QCD simulations.
    PZ_VAL = 2.0  
    
    # Renormalization Scale (mu): 2.0 GeV
    # Justification: Setting mu = pz minimizes the large logarithmic term 
    # ln(4pz^2/mu^2), ensuring the perturbative expansion remains well-behaved.
    MU_VAL = 2.0  
    
    # Strong Coupling (alpha_s): 0.30
    # Justification: Typical value for QCD running coupling at GeV scales (e.g., at 2 GeV).
    ALPHA_S = 0.30
    
    # IR Regulator (eps_ir)
    # Justification: In the MS-bar scheme, the 1/epsilon pole is subtracted.
    # Here we set 1/eps -> 0 to visualize the finite renormalized part.
    # If one wished to see the bare divergence, 1/eps would be set to a large number.
    EPS_IR_VAL = np.inf 

    # --- Calculation ---
    
    # Define momentum fraction range
    # We plot from -0.5 to 2.0 to capture all regions (y<0, 0<y<1, y>1)
    y_vals = np.linspace(-0.5, 2.0, 1000)
    
    # Calculate the 1-loop correction
    f1_vals = calculate_f_1_loop(y_vals, PZ_VAL, MU_VAL, EPS_IR_VAL)
    
    # --- Visualization ---
    
    prefactor = (ALPHA_S * CF) / (2.0 * np.pi)
    # The plotted values are the strip f^(1), the physical correction is alpha_s * CF / 2pi * f^(1)
    # We plot f^(1) directly as per the formula definitions, noting the scale in the label.
    
    plt.figure(figsize=(10, 6))
    
    plt.plot(y_vals, f1_vals, label=r'$\tilde{f}_q^{(1)}(y)$', color='blue', linewidth=2)
    
    # Visual guides for regions
    plt.axvline(0, color='k', linestyle='--', alpha=0.3)
    plt.axvline(1, color='k', linestyle='--', alpha=0.3)
    
    plt.text(0.5, 0.0, r'$0 < y < 1$ (DGLAP)', ha='center', fontsize=12, verticalalignment='bottom')
    plt.text(1.5, 0.0, r'$y > 1$ (Anti-quark)', ha='center', fontsize=12, verticalalignment='bottom')
    plt.text(-0.2, 0.0, r'$y < 0$', ha='center', fontsize=12, verticalalignment='bottom')
    
    plt.title(r'1-Loop CG Quasi-PDF Correction $\tilde{f}_q^{(1)}(y)$', fontsize=16)
    plt.title(fr'$p_z = {PZ_VAL}$ GeV, $\mu = {MU_VAL}$ GeV', fontsize=12, loc='right', color='gray')
    
    plt.xlabel(r'Momentum Fraction $y$', fontsize=14)
    plt.ylabel(r'$\tilde{f}_q^{(1)}(y)$', fontsize=14)
    
    plt.grid(True, alpha=0.3)
    plt.legend(fontsize=12)
    
    # Adjust limits to focus on relevant structure
    # The singularity at y=1 goes to +infinity ( ~ 1/(1-y) ln(1-y) -> +inf )
    # The singularity at y=1 from the other side goes to -infinity ( ~ -1/(y-1) ln(y-1) -> -inf )
    plt.ylim(-3, 5) 
    plt.xlim(-0.5, 1.5)
    
    print(f"Calculated CG Quasi-PDF 1-Loop correction.")
    print(f"Parameters: p_z={PZ_VAL} GeV, mu={MU_VAL} GeV, alpha_s={ALPHA_S}")
    print("Displaying plot...")
    
    plt.show()

if __name__ == "__main__":
    main()
```
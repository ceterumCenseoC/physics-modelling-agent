The Python code below implements the derived model. It calculates the 1-loop CG quasi-PDF $\tilde{f}_q(y, p_z, \epsilon_{\rm IR}, \mu)$ according to the formula for the three regions. It visualizes the distribution for a set of realistic parameters ($p_z = 2.0$ GeV, $\mu = 2.0$ GeV).

```python
import numpy as np
import matplotlib.pyplot as plt

# System constants
CF = 4.0 / 3.0  # Casimir constant for SU(3)
ALPHA_S = 0.30  # Strong coupling constant

def calculate_f_1_loop(y, pz, mu, eps_ir):
    """
    Calculates the 1-loop correction to the Coulomb Gauge quasi-PDF.
    
    Parameters:
    -----------
    y : array_like
        Momentum fraction.
    pz : float
        Longitudinal momentum of the hadron/state (in GeV).
    mu : float
        Renormalization scale (in GeV).
    eps_ir : float
        Infrared regularization parameter (epsilon). 
        Note: In pure dim-reg, this is 1/epsilon. 
        For visualization, we treat it as a large parameter if pole cancelation is not simulated.
        Here we input the pole value 1/eps_ir directly.
        
    Returns:
    --------
    f1 : array_like
        The 1-loop correction term tilde{f}_q^{(1)}.
    """
    f1 = np.zeros_like(y)
    
    # Precompute common logarithmic term
    # ln(4 pz^2 / mu^2)
    # We assume units are such that the argument of ln is dimensionless (Natural units)
    log_term = np.log(4.0 * pz**2 / mu**2)
    
    # Region 1: y < 0
    # According to the derivation, contribution is 0 for free massless quark
    mask_neg = (y < 0)
    # f1[mask_neg] is already 0
    
    # Region 2: 0 < y < 1
    # Formula: (1+y^2)/(1-y) * [1/eps + ln(...) - ln(1-y) + 1/2] - 1/(2(1-y))
    mask_pos = (y > 0) & (y < 1)
    
    # Handle singularity at y=1 by calculation is done slightly away or masked
    # We proceed with array operations masking y=1 if present
    
    y_pos = y[mask_pos]
    
    # Splitting kernel part
    kernel = (1.0 + y_pos**2) / (1.0 - y_pos)
    
    # Bracket terms
    # Note: 1/eps_ir comes from the dimensional regularization pole
    # To visualize a finite result, one typically sets 1/eps_ir -> some large number or 
    # assumes cancellation with PDF. Here we implement the formula as given.
    bracket = (1.0 / eps_ir) + log_term - np.log(1.0 - y_pos) + 0.5
    
    #Constant term subtraction
    constant_term = 1.0 / (2.0 * (1.0 - y_pos))
    
    f1[mask_pos] = kernel * bracket - constant_term
    
    # Region 3: y > 1
    # Formula: (1+y^2)/(y-1) * [1/eps + ln(...) - ln(y-1) + 1/2] - 1/(2(y-1))
    mask_large = (y > 1)
    
    y_large = y[mask_large]
    
    kernel_large = (1.0 + y_large**2) / (y_large - 1.0)
    
    bracket_large = (1.0 / eps_ir) + log_term - np.log(y_large - 1.0) + 0.5
    
    constant_term_large = 1.0 / (2.0 * (y_large - 1.0))
    
    f1[mask_large] = kernel_large * bracket_large - constant_term_large
    
    return f1

# --- Main Execution and Plotting ---

def main():
    # 1. Define Realistic Starting Parameters based on Model Logic
    #    pz = 2.0 GeV (High momentum LaMET regime)
    #    mu  = 2.0 GeV (Minimizing large logs)
    #    eps_ir = We treat 1/eps as a proxy for log(lambda).
    #            For visualization, we assume the IR pole is cancelled or regulated.
    #            Here we set 1/eps = 0 to show the structure of the finite part
    #            or a small value representing the log of a gluon mass.
    #            Let's assume a small effective regulator lambda ~ 0.05 GeV -> ln(lambda^2/mu^2) ~ -6.6
    #            In Minimal Subtraction, the pole is removed. We look at the finite remainder.
    
    PZ_VAL = 2.0  # GeV
    MU_VAL = 2.0  # GeV
    # To see the shape without the divergence at 1/eps, we focus on the mu and y dependent parts
    # effectively treating the *renormalized* coefficient where pole is subtracted (1/eps -> 0).
    # Or, to be strictly faithful to the formula provided, we pass a value.
    # We will plot the "Finite + Log(mu)" part (setting 1/eps = 0) to show the physical shape.
    EPS_IR_VAL = 1e9 # effectively 1/eps -> 0

    # Momentum fraction range
    y_vals = np.linspace(-0.5, 2.0, 1000)
    
    # Calculate 1-loop term
    f1_vals = calculate_f_1_loop(y_vals, PZ_VAL, MU_VAL, EPS_IR_VAL)
    
    # Total Distribution
    # Tree level: delta(1-y). We approximate delta with a narrow gaussian or just plot 1-loop
    # The prompt asks for the implementation of the model. 
    # We will plot the full distribution f(y) = delta(1-y) + correction.
    # Since delta is singular, we plot the correction and the structure.
    
    plt.figure(figsize=(10, 6))
    
    # Plot the 1-loop correction
    coeff = (ALPHA_S * CF) / (2.0 * np.pi)
    plt.plot(y_vals, f1_vals, label=r'$\tilde{f}_q^{(1)}(y)$', color='blue', linewidth=2)
    
    # Annotate the regions
    plt.axvline(0, color='k', linestyle='--', alpha=0.3)
    plt.axvline(1, color='k', linestyle='--', alpha=0.3)
    plt.text(0.5, 0.0, r'$0 < y < 1$', ha='center', fontsize=12)
    plt.text(1.5, 0.0, r'$y > 1$', ha='center', fontsize=12)
    plt.text(-0.25, 0.0, r'$y < 0$', ha='center', fontsize=12)
    
    plt.title(r'1-Loop CG Quasi-PDF Correction $\tilde{f}_q^{(1)}(y)$' + '\n' + 
              fr'$p_z = {PZ_VAL}$ GeV, $\mu = {MU_VAL}$ GeV, $\alpha_s = {ALPHA_S}$', fontsize=14)
    plt.xlabel(r'Momentum Fraction $y$', fontsize=14)
    plt.ylabel(r'$\tilde{f}_q^{(1)}(y)$', fontsize=14)
    plt.grid(True, alpha=0.5)
    plt.legend(fontsize=12)
    plt.ylim(-2, 5) # Limit y-axis to see the structure near the peak
    plt.xlim(-0.5, 1.5)
    
    print("Calculation complete.")
    print(f"Parameters: p_z={PZ_VAL} GeV, mu={MU_VAL} GeV")
    print("Region 0<y<1 peak strictly at y->1 (DGLAP singularity softened by ln(1-y))")
    
    plt.show()

if __name__ == "__main__":
    main()
```
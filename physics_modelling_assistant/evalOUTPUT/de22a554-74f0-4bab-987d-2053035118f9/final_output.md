**
```python
import numpy as np

def calculate_f_1_loop(y, pz, mu, eps_ir):
    """
    Calculates the 1-loop correction to the Coulomb Gauge quasi-PDF 
    based on the derived formula.

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

    Returns:
    --------
    f1 : array_like
        The 1-loop correction term tilde{f}_q^{(1)}.
    """
    f1 = np.zeros_like(y, dtype=np.float64)
    
    # Precompute the common logarithmic term
    log_term = np.log(4.0 * pz**2 / mu**2)
    
    # Region 1: y < 0
    # Contribution is 0
    mask_neg = (y < 0)
    
    # Region 2: 0 < y < 1
    mask_pos = (y > 0) & (y < 1)
    
    if np.any(mask_pos):
        y_pos = y[mask_pos]
        kernel = (1.0 + y_pos**2) / (1.0 - y_pos)
        bracket = (1.0 / eps_ir) + log_term - np.log(1.0 - y_pos) + 0.5
        const_term = 1.0 / (2.0 * (1.0 - y_pos))
        f1[mask_pos] = kernel * bracket - const_term

    # Region 3: y > 1
    mask_large = (y > 1)
    
    if np.any(mask_large):
        y_large = y[mask_large]
        kernel_large = (1.0 + y_large**2) / (y_large - 1.0)
        bracket_large = (1.0 / eps_ir) + log_term - np.log(y_large - 1.0) + 0.5
        const_term_large = 1.0 / (2.0 * (y_large - 1.0))
        f1[mask_large] = kernel_large * bracket_large - const_term_large
        
    return f1
```
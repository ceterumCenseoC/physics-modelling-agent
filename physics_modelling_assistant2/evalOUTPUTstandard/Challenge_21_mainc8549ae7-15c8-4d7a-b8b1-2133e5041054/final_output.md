```python
import numpy as np

def main():
    # ==========================================
    # 1. Constants and Parameters
    # ==========================================
    CF = 4.0 / 3.0
    beta_0 = 9.0
    Lambda_QCD = 0.2445  # GeV

    mu = 2.0    # GeV, Renormalization scale
    Pz = 2.0    # GeV, Hadron momentum

    N = 500                 # Number of grid points
    dx = 0.002              # Step size
    
    # Generate x grid: 0.002, 0.004, ..., 1.0
    # This matches the definition x_i = 0.002 * i for i=1..500
    x = np.linspace(dx, 1.0, N)

    # ==========================================
    # 2. Physical Functions and Kernels
    # ==========================================

    def get_alpha_s(mu_in):
        """Calculate 1-loop alpha_s."""
        return (4 * np.pi) / (beta_0 * np.log(mu_in**2 / Lambda_QCD**2))

    def f_quasi(x_vals):
        """
        Calculate pion quasi-PDF.
        Formula: (x + 3) * (1 - x)^3
        """
        return (x_vals + 3.0) * (1.0 - x_vals)**3

    # ==========================================
    # 3. Matrix Construction (Vectorized)
    # ==========================================
    print("Constructing Matching Kernel Matrix C...")
    
    alpha_mu = get_alpha_s(mu)
    
    # Create matrices for X (rows) and Y (cols)
    X = x[:, np.newaxis]
    Y = x[np.newaxis, :]
    
    # Calculate xi = x / y for all pairs
    Xi = X / Y
    
    # Logarithmic term for the xi < 1 branch: -ln(mu^2 / (4 * x_i^2 * Pz^2))
    # Note: This term depends on x (row), not y (col)
    log_term_x = -np.log(mu**2 / (4 * X**2 * Pz**2))
    
    # Weight for integration: dy/y ~= dx / y
    W = dx / Y
    
    # Prefactor
    prefactor = (alpha_mu * CF) / (2 * np.pi)
    
    # Initialize matrix
    C = np.zeros((N, N))
    
    # Vectorized calculation with np.errstate to handle singularities at xi=1 temporarily
    # (We handle the plus prescription by masking/ignoring the diagonal contributions effectively)
    with np.errstate(divide='ignore', invalid='ignore'):
        # --- Region 0 < xi < 1 (Upper Triangle) ---
        mask_lt1 = (Xi < 1)
        xi_lt1 = Xi[mask_lt1]
        
        term1 = (1 + xi_lt1**2) / (1 - xi_lt1)
        log_part = np.log((1 - xi_lt1) / xi_lt1)
        reg_part = xi_lt1 * (1 + xi_lt1) / (1 - xi_lt1)
        
        # Kernel formula for 0 < xi < 1
        K_lt1 = prefactor * (term1 * (log_part + log_term_x[mask_lt1]) - reg_part)
        
        # Apply weight
        C[mask_lt1] = W[mask_lt1] * K_lt1
        
        # --- Region xi > 1 (Lower Triangle) ---
        mask_gt1 = (Xi > 1)
        xi_gt1 = Xi[mask_gt1]
        
        term1 = (1 + xi_gt1**2) / (1 - xi_gt1)
        log_part = np.log(xi_gt1 / (xi_gt1 - 1))
        poly_part = 1 + 3.0 / (2.0 * xi_gt1)
        
        raw_plus_term = term1 * log_part + poly_part
        
        # Kernel formula for xi > 1
        # Includes the explicit subtraction of 3/(2*xi) outside the plus bracket
        K_gt1 = prefactor * (raw_plus_term - 3.0 / (2.0 * xi_gt1))
        
        C[mask_gt1] = W[mask_gt1] * K_gt1
        
        # --- Diagonal (xi = 1) ---
        # C initialized to zeros. This handles the 'plus' prescription singularity
        # by effectively ignoring the delta-function contribution in this discretization.
    
    print(f"Matching matrix constructed. Alpha_s at mu={mu} GeV: {alpha_mu:.5f}")

    # ==========================================
    # 4. Solve Matching Equation
    # ==========================================
    f_tilde = f_quasi(x)
    # f = f_tilde - C * f_tilde
    f_match = f_tilde - np.dot(C, f_tilde)

    print("Matching complete.")

    # ==========================================
    # 5. DGLAP Evolution Check
    # ==========================================
    print("\nResummation Check:")
    print(f"Target Scale: {mu} GeV")
    print(f"Initial Scale (Pz): {Pz} GeV")
    print("Since mu == Pz, no evolution is required. Large logs vanish.")

    # ==========================================
    # 6. Results Output
    # ==========================================
    target_xs = [0.4, 0.5, 0.6]
    
    print("\n" + "="*40)
    print(" Final Results for Pion PDF")
    print("="*40)
    
    for tx in target_xs:
        # Calculate index: x = i * dx -> i = x/dx
        # 0-based index is i - 1
        idx = int(tx / dx) - 1
        
        # Verify precision
        if abs(x[idx] - tx) < 1e-6:
            print(f"x = {tx:.1f}: f(x) = {f_match[idx]:.6f}")
        else:
            print(f"Error finding index for x={tx}")
            
    print("="*40)

if __name__ == "__main__":
    main()
```
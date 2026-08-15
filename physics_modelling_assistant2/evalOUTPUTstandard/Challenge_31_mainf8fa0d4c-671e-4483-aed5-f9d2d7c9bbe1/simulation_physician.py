
```python
import numpy as np
import matplotlib.pyplot as plt
from scipy.linalg import eig
from scipy.sparse import diags
from scipy.sparse.linalg import eigs

# ==========================================
# Model Implementation:
# Linear Stability Analysis for Mixed BC RB Convection
# ==========================================

def run_stability_analysis(N=100, k_min=0.0, k_max=6.0, n_k=100):
    """
    Performs linear stability analysis for Rayleigh-Bénard convection 
    with mixed boundary conditions.
    
    BCs:
    Top (z=1): Free-slip, Fixed T
    Bottom (z=0): No-slip, Constant Heat Flux
    
    Parameters:
    N (int): Number of Chebyshev collocation points.
    k_min (float): Minimum horizontal wavenumber to scan.
    k_max (float): Maximum horizontal wavenumber to scan.
    n_k (int): Number of wavenumbers to scan.
    
    Returns:
    tuple: (critical_wavenumber, critical_rayleigh, neutral_curve_data)
    """
    
    # 1. Domain and Discretization (Chebyshev-Gauss-Lobatto)
    # Mapping z_hat in [-1, 1] to z in [0, 1]
    z_hat = np.cos(np.linspace(np.pi, 0, N))
    z = 0.5 * (z_hat + 1)
    
    # 2. First Derivative Matrix (Chebyshev)
    c = np.ones(N)
    c[0] = 2
    c[-1] = 2
    c = c * ((-1)**np.arange(N))
    X = np.tile(z_hat, (N, 1))
    dX = X - X.T
    D = np.outer(c, 1.0/c) / (dX + np.eye(N))  # Off-diagonal entries
    D[range(N), range(N)] = np.sum(-D, axis=1)   # Diagonal entries
    
    # Adjustment for mapping from [-1, 1] to [0, 1] -> derivative is multiplied by 2
    D = 2 * D
    
    # Higher derivatives
    D2 = D @ D
    D3 = D2 @ D
    D4 = D3 @ D
    D5 = D4 @ D
    D6 = D5 @ D

    # 3. Construct the Operators for the Combined System (Theta and W)
    # We solve the coupled system:
    # (D^2 - k^2)^2 W = -Ra k^2 Theta
    # (D^2 - k^2) Theta = -W
    #
    # This leads to the generalized eigenvalue problem: A x = Ra B x
    
    # Matrix A corresponds to the LHS of: L_op * [W; Theta] = 0
    # Matrix B corresponds to the RHS forcing term containing Ra
    
    # Total size 2N x 2N
    n_vars = 2 * N
    
    # Initial operator matrices (filled later)
    A_op = np.zeros((n_vars, n_vars))
    B_op = np.zeros((n_vars, n_vars))
    
    # Populate LHS operators (without BCs)
    # Rows 0 to N-1: (D^2 - k^2)^2 W
    A_op[:N, :N] = (D2 @ D2) - 2*(np.diag(k**2) @ D2) + np.diag(k**4)
    
    # Rows N to 2N-1: (D^2 - k^2) Theta
    A_op[N:, N:] = D2 - np.diag(k**2)
    
    # Populate RHS operators (forcing terms)
    # Rows 0 to N-1: Ra k^2 Theta
    B_op[:N, N:] = np.diag(k**2)
    
    # Rows N to 2N-1: -W
    # Note: The B matrix here actually puts the terms that don't involve Ra on the LHS implicitly 
    # if we moved them, but here we set up A*v = Ra*B*v. 
    # The equation (D^2 - k^2) Theta + W = 0 => (D^2 - k^2) Theta = -W.
    # To fit A*vec = Ra*B*vec, we keep (D^2-k^2) in A, and move +W to RHS.
    # So B[N:, :N] = 1
    B_op[N:, :N] = np.eye(N)

    # 4. Apply Boundary Conditions
    
    # We need to replace rows in A_op and B_op with constraints.
    # The eigenvalue is Ra. The eigenvector is x = [W; Theta].
    
    # Index helpers
    idx_bottom = 0
    idx_top = -1
    
    # Boundary Condition: Bottom (z=0) - No-slip, Constant Flux
    # BC1: W(0) = 0
    A_op[idx_bottom, :] = 0
    B_op[idx_bottom, :] = 0
    A_op[idx_bottom, idx_bottom] = 1.0  # Enforce W[0] = 0
    
    # BC2: W'(0) = 0
    row_w_prime = np.zeros(N)
    row_w_prime[idx_bottom+1] = 1 # Placeholder index, actually use D row
    # Use the first derivative matrix row
    A_op[1, :] = 0
    B_op[1, :] = 0
    A_op[1, :N] = D[0, :] # Enforce sum(D[0,j]*W[j]) = 0
    
    # BC3: dTheta/dz (0) = 0 (Constant flux perturbation)
    A_op[2, :] = 0
    B_op[2, :] = 0
    A_op[2, N:] = D[0, :] # Enforce sum(D[0,j]*Theta[j]) = 0
    
    # Boundary Condition: Top (z=1) - Free-slip, Fixed Temp
    # BC4: W(1) = 0
    A_op[idx_top, :] = 0
    B_op[idx_top, :] = 0
    A_op[idx_top, idx_top] = 1.0 # Enforce W[-1] = 0
    
    # BC5: W''(1) = 0 (Free-slip for vertical velocity u_z implies d^2 u_z/dz^2 = 0)
    A_op[-2, :] = 0
    B_op[-2, :] = 0
    A_op[-2, :N] = D2[idx_top, :]
    
    # BC6: Theta(1) = 0
    A_op[idx_top+1, :] = 0 # Wait, idx_top is -1.
    # We need unique indices. Let's pick specific rows.
    # We used 0, 1, 2 for bottom. 
    # Let's use N-1, N-2, N-3 for top?
    # Actually, let's explicitly define the rows to replace.
    # Let's replace rows 3, 4, 5 for Top BCs.
    
    # Let's re-index carefully to avoid overwrite
    # Rows 0, 1, 2 are Bottom BCs.
    # Rows N-1, N-2, N-3 are Top BCs? No, let's pick rows 3, 4, 5 for Top.
    
    # Re-doing Top BCs
    # Top is z=1, which corresponds to index 0 in z_hat, or N-1 in z array?
    # My z array: z = 0.5*(z_hat+1). z_hat[-1]=0 -> z=0. z_hat[0]=1 -> z=1.
    # So Top is index 0 in z_hat, which is index 0 in the Python arrays? 
    # Yes, `z_hat = np.cos(np.linspace(pi, 0, N))` -> z_hat[0] = -1.
    # Wait, `cos(pi)` is -1. `cos(0)` is 1.
    # `linspace(pi, 0)` -> [pi, ..., 0].
    # So z_hat[0] = cos(pi) = -1.
    # z_hat[-1] = cos(0) = 1.
    # My mapping: z = 0.5 * (z_hat + 1).
    # z[0] = 0.5 * (-1 + 1) = 0 (Bottom).
    # z[-1] = 0.5 * (1 + 1) = 1 (Top).
    
    # Okay, correct indices:
    # Bottom is index 0.
    # Top is index N-1.
    
    # Re-setting rows 3, 4, 5 for Top BCs
    
    # BC4: W(1) = 0
    top_idx = N-1
    A_op[3, :] = 0
    B_op[3, :] = 0
    A_op[3, top_idx] = 1.0
    
    # BC5: W''(1) = 0
    A_op[4, :] = 0
    B_op[4, :] = 0
    A_op[4, :N] = D2[top_idx, :]
    
    # BC6: Theta(1) = 0
    A_op[5, :] = 0
    B_op[5, :] = 0
    A_op[5, N:][top_idx] = 1.0 # A_op[5, N + top_idx] = 1.0
    
    # 5. Scan Wavenumbers
    k_values = np.linspace(k_min, k_max, n_k)
    Ra_values = []
    
    print(f"Computing neutral curve for {n_k} wavenumbers with N={N} collocation points...")
    
    for i, k in enumerate(k_values):
        # Re-build A and B for this specific k
        # We can optimize this by only updating k-dependent blocks
        # but for clarity, we reconstruct the specific blocks.
        
        # A block 1: (D^2 - k^2)^2
        A_op[:N, :N] = (D2 @ D2) - 2*(k**2)*D2 + (k**4)*np.eye(N)
        
        # A block 2: (D^2 - k^2)
        A_op[N:, N:] = D2 - (k**2)*np.eye(N)
        
        # B block 1: k^2 (RHS for Theta forcing W)
        B_op[:N, N:] = (k**2)*np.eye(N)
        # B block 2 is static Identity
        
        # Apply BCs again (they overwrite the operator rows)
        # Bottom BCs
        A_op[0, :] = 0; B_op[0, :] = 0; A_op[0, 0] = 1.0                # W(0)=0
        A_op[1, :] = 0; B_op[1, :] = 0; A_op[1, :N] = D[0, :]            # W'(0)=0
        A_op[2, :] = 0; B_op[2, :] = 0; A_op[2, N:] = D[0, :]            # T'(0)=0
        
        # Top BCs
        A_op[3, :] = 0; B_op[3, :] = 0; A_op[3, top_idx] = 1.0           # W(1)=0
        A_op[4, :] = 0; B_op[4, :] = 0; A_op[4, :N] = D2[top_idx, :]     # W''(1)=0
        A_op[5, :] = 0; B_op[5, :] = 0; A_op[5, N:][top_idx] = 1.0       # T(1)=0
        
        # Solve Generalized Eigenvalue Problem: A x = Ra B x
        # We are looking for the smallest positive real eigenvalue Ra.
        # Since B is singular due to BCs, we typically use eigs with sigma=0 or similar,
        # but here we have a specific structure.
        # Explicitly solving `eigvals(B^-1 A)` is unstable due to singularity.
        # However, since we fixed rows, the system is determined.
        
        # Convert to dense for direct solve (N is small, e.g., 64 or 100)
        try:
            # Use scipy.linalg.eig for small dense matrices
            evals = eig(A_op, B_op, left=False, right=False)
            
            # Find real positive eigenvalues (critical Ra)
            real_evals = evals[np.isreal(evals)].real
            pos_evals = real_evals[real_evals > 0]
            
            if len(pos_evals) > 0:
                Ra_c_k = np.min(pos_evals)
                Ra_values.append(Ra_c_k)
            else:
                Ra_values.append(np.inf)
        except Exception as e:
            print(f"Convergence issue at k={k:.2f}: {e}")
            Ra_values.append(np.inf)

    # 6. Analyze Results
    Ra_values = np.array(Ra_values)
    
    # Filter out infinities for plotting/min finding
    valid_mask = np.isfinite(Ra_values)
    k_valid = k_values[valid_mask]
    Ra_valid = Ra_values[valid_mask]
    
    if len(Ra_valid) == 0:
        return None, None, None

    min_index = np.argmin(Ra_valid)
    k_c = k_valid[min_index]
    Ra_c = Ra_valid[min_index]
    
    print(f"Critical Rayleigh Number found: {Ra_c:.4f}")
    print(f"Critical Wavenumber found: {k_c:.4f}")
    
    # Generate Plot
    plt.figure(figsize=(8, 5))
    plt.plot(k_values, Ra_values, 'b-', linewidth=2, label='Neutral Curve')
    plt.plot(k_c, Ra_c, 'ro', markersize=8, label=f'Critical Point ($k_c={k_c:.2f}$, $R_a_c={Ra_c:.1f}$)')
    plt.xlabel('Horizontal Wavenumber $k$')
    plt.ylabel('Rayleigh Number $Ra$')
    plt.title('Linear Stability Analysis: Mixed BC Convection')
    plt.grid(True, linestyle='--', alpha=0.7)
    plt.legend()
    plt.xlim(left=0)
    plt.ylim(bottom=0)
    plt.show()
    
    return k_c, Ra_c, (k_values, Ra_values)

if __name__ == "__main__":
    # Run the simulation
    # Grid resolution of 64 is usually sufficient for linear stability of this ODE
    # We scan k from 0 to 6 to cover the expected instability range
    kc, Rac, curve_data = run_stability_analysis(N=64, k_min=0.0, k_max=6.0, n_k=50)
    
    if kc is not None:
        print("\n" + "="*40)
        print("FINAL RESULTS")
        print("="*40)
        print(f"Critical Wavenumber (kc): {kc:.4f}")
        print(f"Critical Rayleigh Number (Rac): {Rac:.2f}")
        
        # Check for k_c approx 0 (within tolerance) or small finite value
        # The provided context suggests "instabilities to the largest scales" and "wavenumber is thus zero".
        # Numerically, for finite domain discretization with BCs, k=0 might be singular or handled.
        # The curve should show the minimum.
        
        if abs(kc) < 0.02:
            print("Analysis confirms critical mode is at largest scale (k -> 0).")
        else:
            print(f"Analysis finds finite critical wavenumber {kc:.2f}.")
```
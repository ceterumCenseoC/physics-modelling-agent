```python
import numpy as np
import matplotlib.pyplot as plt
from scipy.linalg import eig

# ==========================================
# Model Implementation:
# Linear Stability Analysis for Mixed BC RB Convection
# ==========================================

def run_stability_analysis(N=64, k_min=0.0, k_max=6.0, n_k=50):
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
    # z_hat = cos(pi * j / (N-1)) for j=0..N-1
    # We want z=0 at bottom and z=1 at top.
    # Standard Chebyshev points on [-1, 1]: x_i = cos(i*pi/(N-1))
    # x=1 (top) -> i=0. x=-1 (bottom) -> i=N-1.
    x_cheb = np.cos(np.linspace(0, np.pi, N))
    z = 0.5 * (x_cheb + 1.0) 
    # Note: z[0] corresponds to x_cheb[0]=1 (Top, z=1)
    #       z[N-1] corresponds to x_cheb[N-1]=-1 (Bottom, z=0)
    # This is reverse order compared to typical logic, but fine as long as consistent.
    # Let's reorder to be increasing z for clarity: z[0]=0, z[N-1]=1.
    z = z[::-1]
    x_cheb = x_cheb[::-1] # Now x_cheb goes from -1 to 1
    
    # 2. First Derivative Matrix (Chebyshev) on [-1, 1]
    # Based on Trefethen, Spectral Methods in MATLAB
    c = np.ones(N)
    c[0] = 2.0
    c[-1] = 2.0
    c = c * ((-1.0)**np.arange(N))
    
    X = np.tile(x_cheb, (N, 1))
    dX = X - X.T
    
    # Handle singularity on diagonal where dividing by (xi - xj)
    # The formula c_i * (-1)^{i+j} / (c_j * (x_i - x_j)) for i!=j
    D = np.outer(c, 1.0/c) / (dX + np.eye(N)) 
    
    D[range(N), range(N)] = 0.0 # Clear diagonal temporarily
    # Diagonal entries: sum of off-diagonal rows with sign change
    D[range(N), range(N)] = -np.sum(D, axis=1)
    
    # Mapping derivative from [-1, 1] to [0, 1]
    # dz/dx = 1/2  => d/dz = (dx/dz) * d/dx = 2 * d/dx
    D = 2.0 * D
    
    # Higher derivatives
    D2 = D @ D
    D3 = D2 @ D
    D4 = D3 @ D

    # 3. Construct Operators
    # System size 2N (N for w, N for theta)
    n_vars = 2 * N
    
    # Index mapping
    idx_w = slice(0, N)
    idx_t = slice(N, 2*N)
    
    # Allocate matrices
    # Equation 1: (D^2 - k^2)^2 w + Ra k^2 theta = 0
    # Equation 2: (D^2 - k^2) theta + w = 0
    # Rearranged for eigenvalue solver A v = Ra B v:
    # Rows 0..N-1: ((D^2 - k^2)^2) w = -Ra k^2 theta  => A contains (D^2 - k^2)^2, B contains +k^2*I
    # Rows N..2N-1: (D^2 - k^2) theta = -w => A contains (D^2 - k^2), B contains -I
    
    # However, to practice standard form A v = s B v, put RHS terms in B.
    # Eq 1: L1 w = Ra (-k^2 theta). Here s=Ra.
    # Eq 2: L2 theta = (-w). Here RHS has no Ra.
    
    # Better form for generalized EVP A x = Ra B x:
    # (D^2 - k^2)^2 w + Ra k^2 theta = 0
    # (D^2 - k^2) theta + w = 0
    
    # A = [[ (D^2-k^2)^2 , 0      ],
    #      [ 0          , (D^2-k^2)]]
    # B = [[ 0, -k^2 I ],
    #      [ -I, 0     ]]
    # We solve A x = -Ra B x => (-A^{-1} B) x = (1/Ra) x
    # Or easier: Just use `eig(A_op, B_op)` where A_op, B_op are constructed carefully.
    # Let's rearrange eq 2 to isolate Ra? No, Ra only in eq 1.
    # This is a quadratic eigenvalue problem or coupled problem.
    # Standard trick: 
    # From eq 2: theta = -(D^2 - k^2)^{-1} w.
    # Substitute into eq 1: (D^2 - k^2)^2 w - Ra k^2 (D^2 - k^2)^{-1} w = 0
    # => (D^2 - k^2)^3 w = Ra k^2 w
    # This is a standard EVP! 
    # LHS operator: (D^2 - k^2)^3
    # RHS operator: k^2 I
    
    # We will solve this reduced system: L w = Ra k^2 w
    # This is numerically more efficient than the 2N system, 
    # provided BCs are handled correctly for the 6th order equation.
    
    # Initialize LHS (A) and RHS (B)
    A_op = np.zeros((N, N))
    B_op = np.zeros((N, N))
    
    # 4. Apply Boundary Conditions to the 6th Order System
    # Domain indices: 0 (z=0, Bottom), N-1 (z=1, Top)
    
    # Bottom BCs (z=0, index 0)
    # 1. w(0) = 0
    # 2. w'(0) = 0
    # 3. theta'(0) = 0. Note: theta = - (D^2 - k^2)^{-1} w. 
    #    This is hard to enforce directly in the 6th order formulation 
    #    without keeping theta.
    #    Let's stick to the Coupled System formulation (2N size) to easily apply all BCs.
    
    # REVERTING TO COUPLED SYSTEM Formulation for clarity of BCs
    A_op = np.zeros((n_vars, n_vars))
    B_op = np.zeros((n_vars, n_vars))
    
    # Operators
    # L_w = D2 - k^2 * I
    # L_theta = D2 - k^2 * I
    
    # Rows 0 to N-1 (Momentum Equation):
    # (L_w)^2 w + Ra k^2 theta = 0
    # A[0:N, 0:N] = L_w @ L_w
    # B[0:N, N:2N] = -k^2 * I  (Move Ra term to B for A*x = Ra*B*x form)
    # Actually, let's use form A*x = lambda*B*x.
    # (L_w)^2 w + Ra k^2 theta = 0  ->  A=[(L_w)^2, 0]; B=[0, -k^2 I]; lambda = Ra
    # L_theta theta + w = 0          ->  A=[0, L_theta]; B=[-I, 0]; lambda = Ra (not present)
    # To make this a standard generalized eigenvalue problem for Ra, we can rearrange Eq 2:
    # w = -L_theta theta -> substitute...
    # Let's simply use `scipy.linalg.eig(A, B)` and build the matrices such that:
    # A x = Ra B x
    # Eq 1: (L_w)^2 w = -Ra k^2 theta  => Row i of A: row_i((L_w)^2) | 0 ; Row i of B: 0 | -k^2 * row_i(I)
    # Eq 2: L_theta theta = -w          => Row i of A: 0 | row_i(L_theta) ; Row i of B: -row_i(I) | 0
    
    # This form is valid. The eigenvalues will be Ra.
    # Note: B will be singular if we have pure Neumann/Dirichlet mixtures without constraints, 
    # but `eig` can handle singular B (returns some infinities).
    
    # Initialize lists to store BC rows indices to replace
    bc_rows = []
    
    # Bottom BCs (index 0)
    bc_rows.extend([0, 1, 2])
    # w(0) = 0
    # w'(0) = 0
    # theta'(0) = 0
    
    # Top BCs (index N-1)
    bc_rows.extend([3, 4, 5])
    # w(1) = 0
    # w''(1) = 0
    # theta(1) = 0
    
    # Calculate neutral curve
    k_values = np.linspace(k_min, k_max, n_k)
    Ra_values = []
    
    print(f"Computing neutral curve for {n_k} wavenumbers with N={N} collocation points...")
    
    for k in k_values:
        k2 = k**2
        
        # Identity for this block
        I = np.eye(N)
        
        # L = D2 - k^2 I
        L = D2 - k2 * I
        L2 = L @ L
        
        # Fill Aop
        # Momentum rows (except BC rows)
        # We use masks to fill internal rows, then overwrite BC rows
        A_op[:N, :N] = L2
        A_op[N:, N:] = L
        
        # Fill Bop
        B_op[:N, N:] = -k2 * I
        B_op[N:, :N] = -I
        
        # Enforce Boundary Conditions
        # Bottom (z=0, index 0)
        
        # 1. w(0) = 0
        A_op[0, :] = 0
        B_op[0, :] = 0
        A_op[0, 0] = 1.0
        
        # 2. w'(0) = 0
        A_op[1, :] = 0
        B_op[1, :] = 0
        A_op[1, :N] = D[0, :] # First derivative at z=0
        
        # 3. theta'(0) = 0
        A_op[2, :] = 0
        B_op[2, :] = 0
        A_op[2, N:] = D[0, :]
        
        # Top (z=1, index N-1)
        
        # 4. w(1) = 0
        A_op[3, :] = 0
        B_op[3, :] = 0
        A_op[3, N-1] = 1.0
        
        # 5. w''(1) = 0 (Free slip)
        A_op[4, :] = 0
        B_op[4, :] = 0
        A_op[4, :N] = D2[N-1, :]
        
        # 6. theta(1) = 0
        A_op[5, :] = 0
        B_op[5, :] = 0
        A_op[5, N + N - 1] = 1.0
        
        # Generalized Eigenvalue Problem: A x = Ra B x
        # Since we have mixed BCs, B is likely singular (has zero rows corresponding to Dirichlet BCs where Ra term vanishes).
        # We solve for the eigenvalues.
        evals = eig(A_op, B_op)
        eigenvalues = evals[0]
        
        # Filter for Ra (real, positive, and finite)
        # Eigenvalues might be complex due to numerical precision, but we look for the real critical Ra.
        real_evals = eigenvalues[np.isreal(eigenvalues)].real
        pos_evals = real_evals[(real_evals > 1.0) & (real_evals < 1e6)] # Filter reasonable range
        
        if len(pos_evals) > 0:
            Ra_c_k = np.min(pos_evals)
            Ra_values.append(Ra_c_k)
        else:
            Ra_values.append(np.inf)

    # 5. Analyze Results
    Ra_values = np.array(Ra_values)
    
    valid_mask = np.isfinite(Ra_values)
    k_valid = k_values[valid_mask]
    Ra_valid = Ra_values[valid_mask]
    
    if len(Ra_valid) == 0:
        print("No valid Rayleigh numbers found in the specified range.")
        return None, None, None

    min_index = np.argmin(Ra_valid)
    k_c = k_valid[min_index]
    Ra_c = Ra_valid[min_index]
    
    print(f"Critical Rayleigh Number found: {Ra_c:.4f}")
    print(f"Critical Wavenumber found: {k_c:.4f}")
    
    # Plotting
    plt.figure(figsize=(8, 5))
    plt.plot(k_values, Ra_values, 'b-', linewidth=2, label='Neutral Curve')
    plt.plot(k_c, Ra_c, 'ro', markersize=8, label=f'Critical Point ($k_c={k_c:.2f}$, $R_a_c={Ra_c:.1f}$)')
    plt.xlabel('Horizontal Wavenumber $k$')
    plt.ylabel('Rayleigh Number $Ra$')
    plt.title('Linear Stability Analysis: Mixed BC Convection')
    plt.grid(True, linestyle='--', alpha=0.7)
    plt.legend()
    plt.ylim(bottom=0)
    if np.min(k_values) >= 0:
        plt.xlim(left=0)
    plt.show()
    
    return k_c, Ra_c, (k_values, Ra_values)

if __name__ == "__main__":
    # Execute the stability analysis
    # N=64 provides good resolution for the 6th order differential equation eigenmodes.
    # k_min is set to a small positive number (0.1) to avoid the trivial k=0 singularity 
    # in the discrete matrix formulation, though the physical limit is k->0.
    # k_max covers the range where the critical mode is expected (or beyond 1.0/p approx 3).
    kc, Rac, curve_data = run_stability_analysis(N=64, k_min=0.1, k_max=6.0, n_k=60)
    
    if kc is not None:
        print("\n" + "="*40)
        print("FINAL RESULTS")
        print("="*40)
        print(f"Critical Wavenumber (kc): {kc:.4f}")
        print(f"Critical Rayleigh Number (Rac): {Rac:.2f}")
        print("-" * 40)
        print(f"Boundary Conditions: Bottom (No-slip, Const. Flux), Top (Free-slip, Fixed T)")
```
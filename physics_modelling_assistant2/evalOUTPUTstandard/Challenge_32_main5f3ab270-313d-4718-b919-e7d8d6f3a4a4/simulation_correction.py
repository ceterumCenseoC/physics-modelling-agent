```python
import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import minimize_scalar, root_scalar
from scipy.linalg import eig
import warnings

# suppress runtime warnings for cleaner output (e.g. division by zero in matrix setups handled by logic)
warnings.filterwarnings('ignore')

class RayleighDarcyStability:
    """
    A class to solve the linear stability analysis for Rayleigh-Darcy convection
    with mixed boundary conditions (constant flux at bottom, constant temperature at top).
    """
    def __init__(self, nz=50, z_target=0.67365):
        """
        Initialize the model parameters and numerical grid.
        Uses Chebyshev-Gauss-Lobatto collocation points mapped to [0, 1].
        
        Parameters:
        nz (int): Number of collocation intervals (total points = nz + 1).
        z_target (float): The specific z-coordinate to evaluate the eigenfunction ratio.
        """
        self.nz = nz
        self.z_target = z_target
        
        # Generate Chebyshev-Gauss-Lobatto nodes in [-1, 1]
        k_vals = np.arange(nz + 1)
        x_nodes = np.cos(np.pi * k_vals / nz)
        
        # Map nodes to physical domain [0, 1]
        self.z = (x_nodes + 1) / 2
        
        # Precompute differentiation matrices up to 4th order
        self.D1, self.D2, self.D3, self.D4 = self._compute_differentiation_matrices(self.z)
        
        # Storage for results
        self.Ra_c = None
        self.k_c = None
        self.w_func = None
        self.t_func = None
        self.ratio_at_target = None

    def _compute_differentiation_matrices(self, z):
        """
        Computes differentiation matrices using Chebyshev polynomials.
        Reference: Trefethen, Spectral Methods in MATLAB.
        Matrices are computed for x in [-1, 1] and transformed to z in [0, 1].
        """
        n = len(z)
        # Canonical interval [-1, 1]
        x = 2 * z - 1
        
        # Construct first derivative matrix D on [-1, 1]
        D = np.zeros((n, n))
        c = np.ones(n)
        c[0] = 2
        c[-1] = 2
        c = c * ((-1) ** np.arange(n))
        
        X = x[:, None] - x[None, :] # Matrix of x_i - x_j
        
        # Off-diagonal entries
        with np.errstate(divide='ignore', invalid='ignore'):
            D = (c[:, None] / c[None, :]) / (X + np.eye(n))
            D = D - np.diag(np.sum(D, axis=1))
            
        # Diagonal correction
        D[0, 0] = (2 * (n - 1)**2 + 1) / 6
        D[-1, -1] = - (2 * (n - 1)**2 + 1) / 6
        
        # Transform D to [0, 1]: d/dz = 2 * d/dx
        D1 = 2 * D
        
        # Compute higher order derivatives
        D2 = D1 @ D1
        D3 = D1 @ D2
        D4 = D1 @ D3
        
        return D1, D2, D3, D4

    def _build_eigenvalue_system(self, k):
        """
        Constructs the matrices A and B for the generalized eigenvalue problem A*v = Ra*B*v.
        System derived from:
        1) (D^2 - k^2)w + Ra*k^2*theta = 0
        2) (D^2 - k^2)theta + w = 0
        BCs: w(0)=0, theta'(0)=0, w(1)=0, theta(1)=0
        """
        n = len(self.z)
        
        # Setup System Matrices A and B
        # Vector v = [w_0...w_n, theta_0...theta_n]
        # Rows 0 to n-1 correspond to w equation
        # Rows n to 2n-1 correspond to theta equation
        
        A_mat = np.zeros((2 * n, 2 * n))
        B_mat = np.zeros((2 * n, 2 * n))
        
        # Operator L = D^2 - k^2 * I
        L = self.D2 - (k**2) * np.eye(n)
        
        # --- Fill Interior Equations ---
        
        # w equation: L*w + Ra*k^2*theta = 0  => A*[w;th] = -Ra*B*[w;th]
        # Here we use formulation A*v = Ra * B*v.
        # Rearranged: L*w = -Ra*k^2*theta => L*w + Ra*k^2*theta = Ra*0 (standard form needed)
        # Actually, usually homogeneous BCs lead to L2 w = Ra k^2 w.
        # Let's stick to the coupled system:
        # L * w + 0 * th  = -Ra * (k^2 * th) -> This puts Ra on RHS.
        # L * th + w      =  0
        
        # Row 0 to n-1: L*w = -Ra * k^2 * theta
        A_mat[:n, :n] = L
        A_mat[:n, n:] = np.zeros((n, n))
        B_mat[:n, n:] = (k**2) * np.eye(n)
        
        # Row n to 2n-1: L*theta + w = 0
        # Since there is no Ra in this equation, we can't easily put it in standard A*v = Ra*B*v form
        # unless we treat one variable as eigenvalue parameter for the other.
        # Better: Eliminate theta.
        # theta = -inv(L) * w.
        # Sub into eq 1: L*w = -Ra * k^2 * (-inv(L)*w)
        # L^2 * w = Ra * k^2 * w
        # Let's solve this 4th order ODE eigenvalue problem directly.
        
        # Re-implementation using 4th order single variable ODE:
        # (D^2 - k^2)^2 w - Ra * k^2 * w = 0
        # BCs:
        # z=0: w=0, theta'=0. 
        #   theta = - (D^2-k^2)^-1 w => theta' = -((D^2-k^2)^-1 w)' = 0
        #   Note: (D^2-k^2) theta = -w. Apply D': (D^2-k^2) theta' = -w'.
        #   So BC is: theta' = 0.
        #   From L theta = -w, we can write (D^2 - k^2) w' = -Ra k^2 theta' (from differentiating Eq 1).
        #   Wait, Eq 1: (D^2 - k^2) w = -Ra k^2 theta.
        #   Diff: (D^2 - k^2) w' = -Ra k^2 theta'.
        #   Bottom BC theta' = 0 => (D^2 - k^2) w' = 0 at z=0.
        #
        # z=1: w=0, theta=0.
        #   Theta BC: (D^2 - k^2) w = -Ra k^2 * 0 => (D^2 - k^2) w = 0 at z=1.
        
        # Construct 4th order operator
        L2 = L @ L
        
        A_mat = np.zeros((n, n))
        # A_mat * w = Ra * k^2 * w
        # L2 * w = Ra * k^2 * w  =>  (L2 - Ra*k^2*I)w = 0 => A w = Ra B w
        # A = L2, B = k^2 * I
        
        A_mat[:, :] = L2
        B_mat = (k**2) * np.eye(n)
        
        # Impose Boundary Conditions
        # z=0 (index 0): w=0  AND  (D^2 - k^2)w' = 0
        
        # 1. w(0) = 0
        # Replace row 0
        A_mat[0, :] = 0
        A_mat[0, 0] = 1
        B_mat[0, :] = 0
        
        # 2. (D^2 - k^2)w' = 0 at z=0
        # w' = D1 * w
        # (D^2 - k^2) w' = (D2 - k^2*I) @ D1 @ w = S @ w
        S = (self.D2 - (k**2) * np.eye(n)) @ self.D1
        # Replace row 1 (arbitrary choice for second BC)
        A_mat[1, :] = S[0, :]
        B_mat[1, :] = 0
        
        # z=1 (index -1): w=0 AND (D^2 - k^2)w = 0
        
        # 3. w(1) = 0
        # Replace row -1
        A_mat[-1, :] = 0
        A_mat[-1, -1] = 1
        B_mat[-1, :] = 0
        
        # 4. (D^2 - k^2)w = 0 at z=1
        # Row -2
        A_mat[-2, :] = L[-1, :]
        B_mat[-2, :] = 0
        
        return A_mat, B_mat

    def solve_for_Ra(self, k):
        """
        Solves the generalized eigenvalue problem for a given wavenumber k
        and returns the minimum positive real eigenvalue (Rayleigh number).
        """
        A, B = self._build_eigenvalue_system(k)
        
        # Solve A*x = lambda*B*x
        # eig returns lambdas. We want lambdas = Ra.
        vals, vecs = eig(A, B)
        
        # Filter eigenvalues
        # We are looking for Ra_k = min(lambda_real) such that lambda > 0.
        real_vals = vals.real
        
        # Filter out extremely large or small eigenvalues (numerical noise)
        valid_vals = real_vals[(real_vals > 0) & (real_vals < 1e6)]
        
        if len(valid_vals) == 0:
            return np.nan
            
        # The critical Ra for this k is the minimum positive eigenvalue
        return np.min(valid_vals)

    def find_critical_parameters(self):
        """
        Finds the critical Rayleigh number (Ra_c) and critical wavenumber (k_c)
        by minimizing Ra(k) over wavenumber space.
        """
        print("Scanning wavenumbers to find critical stability parameters...")
        
        # 1. Coarse scan
        k_scan = np.linspace(2.5, 3.5, 21)
        ra_scan = []
        
        for k in k_scan:
            r = self.solve_for_Ra(k)
            ra_scan.append(r)
            
        # Filter valid results
        k_scan = np.array(k_scan)
        ra_scan = np.array(ra_scan)
        mask = ~np.isnan(ra_scan)
        k_coarse = k_scan[mask]
        ra_coarse = ra_scan[mask]
        
        if len(k_coarse) == 0:
            raise ValueError("No valid Ra found in scan range. Try widening k range.")
            
        idx_min = np.argmin(ra_coarse)
        k_star = k_coarse[idx_min]
        
        print(f"Coarse minimum found at k={k_star:.4f}, Ra={ra_coarse[idx_min]:.4f}")
        
        # 2. Fine minimization
        # Search in smaller interval around k_star
        k_min = max(0.1, k_star - 0.5)
        k_max = k_star + 0.5
        
        def ra_function(k):
            return self.solve_for_Ra(k)
            
        res = minimize_scalar(ra_function, bounds=(k_min, k_max), method='bounded', options={'xatol': 1e-6})
        
        self.k_c = res.x
        self.Ra_c = res.fun
        
        print(f"Optimization converged.")
        print(f"Critical Wavenumber (k_c): {self.k_c}")
        print(f"Critical Rayleigh Number (Ra_c): {self.Ra_c}")
        
        return self.Ra_c, self.k_c

    def compute_eigenfunctions(self):
        """
        Computes the vertical velocity (w) and temperature perturbation (theta)
        eigenfunctions for the critical state.
        """
        if self.k_c is None:
            self.find_critical_parameters()
            
        # Re-build system to get eigenvectors
        A, B = self._build_eigenvalue_system(self.k_c)
        
        # Get all eigenvectors/values
        vals, vecs = eig(A, B)
        
        # Find the eigenvector corresponding to Ra_c
        idx = np.argmin(np.abs(vals.real - self.Ra_c))
        w_vec = vecs[:, idx].real
        
        # Normalize w (arbitrary scaling, typically max(w)=1)
        self.w_func = w_vec / np.max(np.abs(w_vec))
        
        # Compute theta from w using: (D^2 - k^2) theta = -w
        # We solve this linear system for theta.
        # L * theta = -w
        L = self.D2 - (self.k_c**2) * np.eye(len(self.z))
        
        # Modify L to account for temperature BC: theta(1)=0
        # We add this as a row replacement to ensure linear system is solvable
        # Or just solve and subtract boundary value if L is invertible (doesn't satisfy BC by default).
        # It is better to enforce the BC theta(1)=0 directly.
        # We use least squares or modify the linear system.
        # Let's modify L matrix to enforce theta(1)=0.
        
        L_sys = L.copy()
        b_vec = -self.w_func.copy()
        
        # Enforce theta(1) = 0 at last node
        L_sys[-1, :] = 0
        L_sys[-1, -1] = 1
        b_vec[-1] = 0
        
        # Solve for theta
        self.t_func = np.linalg.solve(L_sys, b_vec)
        
        return self.w_func, self.t_func

    def calculate_target_ratio(self):
        """
        Calculates the ratio w(z_target)/theta(z_target).
        """
        if self.w_func is None:
            self.compute_eigenfunctions()
            
        # Interpolate values at target z
        w_target = np.interp(self.z_target, self.z, self.w_func)
        t_target = np.interp(self.z_target, self.z, self.t_func)
        
        # Avoid division by zero
        if abs(t_target) < 1e-9:
            ratio = np.inf if w_target != 0 else np.nan
        else:
            ratio = w_target / t_target
            
        self.ratio_at_target = ratio
        
        print(f"\nEigenfunction Evaluation at z = {self.z_target}:")
        print(f"w(z) = {w_target:.5f}")
        print(f"T(z) = {t_target:.5f}")
        print(f"Ratio w/T = {ratio:.5f}")
        
        return ratio

    def plot_results(self):
        """Plots the eigenfunctions w(z) and theta(z)."""
        if self.w_func is None:
            self.compute_eigenfunctions()
            
        plt.figure(figsize=(10, 6))
        plt.plot(self.z, self.w_func, 'b-', linewidth=2, label=r'$w(z)$')
        plt.plot(self.z, self.t_func, 'r--', linewidth=2, label=r'$\theta(z)$')
        plt.axhline(0, color='k', linestyle=':', alpha=0.5)
        plt.axvline(self.z_target, color='g', linestyle=':', label=f'Target z={self.z_target}')
        
        plt.xlabel('Vertical Coordinate z')
        plt.ylabel('Perturbation Amplitude')
        plt.title(f'Eigenfunctions at Critical State ($Ra_c={self.Ra_c:.2f}, k_c={self.k_c:.2f}$)')
        plt.legend()
        plt.grid(True, alpha=0.3)
        plt.show()

if __name__ == "__main__":
    # Initialize model with enough points for spectral accuracy
    # z_target is specified in the prompt
    model = RayleighDarcyStability(nz=60, z_target=0.67365)
    
    # Run analysis
    Ra_c, k_c = model.find_critical_parameters()
    ratio = model.calculate_target_ratio()
    
    # Display results
    plot = model.plot_results()
    
    print("\n" + "="*60)
    print("COMPUTATIONAL RESULTS SUMMARY")
    print("="*60)
    print(f"Critical Rayleigh Number (Ra_c):  {Ra_c:.5f}")
    print(f"Expected:                        ~42.79")
    print("-" * 60)
    print(f"Critical Wavenumber (k_c):       {k_c:.5f}")
    print(f"Expected:                        ~3.14")
    print("-" * 60)
    print(f"Ratio w(z)/T(z) at z=0.67365:    {ratio:.5f}")
    print(f"Expected:                        ~-21.39")
    print("="*60)
```
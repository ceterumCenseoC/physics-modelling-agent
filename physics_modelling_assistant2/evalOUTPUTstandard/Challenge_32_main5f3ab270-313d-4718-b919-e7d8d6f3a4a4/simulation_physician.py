```python

import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import root_scalar
from scipy.linalg import eig
import warnings

# Suppress warnings for cleaner output unless critical
warnings.filterwarnings('ignore')

class RayleighDarcyStability:
    def __init__(self, nz=100, z_target=0.67365):
        """
        Initialize the model parameters and numerical grid.
        
        Parameters:
        nz (int): Number of collocation points (internal nodes).
        z_target (float): The z-coordinate to evaluate the specific ratio.
        """
        self.nz = nz
        self.z_target = z_target
        
        # Chebyshev-Gauss-Lobatto nodes mapped to [0, 1]
        k = np.arange(nz + 1)
        # Raw Chebyshev nodes in [-1, 1]
        x = np.cos(np.pi * k / nz)
        # Map to [0, 1]
        self.z = (x + 1) / 2
        
        # Ensure target point is handled or interpolated
        self.dz = self.z[1] - self.z[0] if nz > 1 else 1.0

        # Precompute differentiation matrices
        self.D1, self.D2, self.D3, self.D4 = self._compute_differentiation_matrices(self.z)
        
        # Store the critical values once found
        self.Ra_c = None
        self.k_c = None
        self.w_func = None
        self.t_func = None
        self.ratio_at_target = None

    def _compute_differentiation_matrices(self, z):
        """
        Computes 1st to 4th order differentiation matrices using Chebyshev spectral collocation.
        Using the recursive formula.
        """
        n = len(z)
        # We construct the matrix on the canonical interval x in [-1, 1] then transform
        # Mapping z = (x+1)/2 => x = 2z - 1
        
        x = 2 * z - 1
        
        x_col = x.reshape(-1, 1)
        X = x_col - x_col.T
        
        # Handle diagonal for connectivity matrix C
        with np.errstate(divide='ignore', invalid='ignore'):
            C = np.eye(n) * np.diag_indices(n)[1] # Not standard, doing manual diagonals
            c = np.ones(n)
            c[0] = 2
            c[-1] = 2
            c = c * ((-1)**np.arange(n))
            # Off-diagonal
            C = c.reshape(1, -1) / (c.reshape(-1, 1) * X + np.eye(n))
            # Diagonal
            # sum of rows? No. Standard Fornberg or Trefethen.
            # Using Trefethen's cheb function logic.
            
        # Re-implementation of Trefethen's Cheb matrix
        # c = np.ones(n+1)
        # c[0] = 2
        # c[-1] = 2
        # X = x[:, None] - x[None, :]
        # D = np.outer(c, 1/c) / (X + np.eye(n+1))
        # D = D - np.diag(np.sum(D, axis=1))
        
        # Let's use Fornberg's algorithm for robustness on arbitrary z points?
        # Chebyshev points have simple closed form.
        
        N = n - 1 # Index of last point
        D = np.zeros((n, n))
        
        # Construct D1 on [-1, 1]
        for i in range(n):
            for j in range(n):
                if i != j:
                    ci = 2 if (i == 0 or i == N) else 1
                    cj = 2 if (j == 0 or j == N) else 1
                    D[i, j] = (ci / cj) * ((-1)**(i + j)) / (x[i] - x[j])
        
        for i in range(n):
            D[i, i] = 0
            if i == 0: D[i, i] = (2 * N**2 + 1) / 6
            elif i == N: D[i, i] = -(2 * N**2 + 1) / 6
            else: D[i, i] = -x[i] / (2 * (1 - x[i]**2))

        # Transform D to [0, 1] domain: d/dz = 2 * d/dx
        # Higher orders scale by powers of 2
        self.D1_raw = D * 2
        self.D2_raw = self.D1_raw @ self.D1_raw
        self.D3_raw = self.D1_raw @ self.D2_raw
        self.D4_raw = self.D1_raw @ self.D3_raw
        
        return self.D1_raw, self.D2_raw, self.D3_raw, self.D4_raw

    def _build_matrices(self, k, Ra):
        """
        Constructs the operators for the coupled system.
        System:
        (D^2 - k^2) w = -Ra * k^2 * theta
        (D^2 - k^2) theta = -w
        
        We write this as A * v = 0 where v = [w; theta]
        
        Actually, we can eliminate one variable to get a 4th order ODE in one.
        L^2 w - Ra * k^2 * w = 0
        L = D^2 - k^2
        
        We have to incorporate BCs carefully.
        BCs:
        z=0: w=0, theta'=0 => w=0, (D^2-k^2)w' = -w' => ?
        Let's keep the coupled system. It's 2nd order order, easier to impose BCs.
        
        w'' - k^2 w + Ra k^2 theta = 0
        theta'' - k^2 theta + w = 0
        
        Variables vector: y = [w, w', theta, theta']
        y' = [w', w'', theta', theta'']
        y' = [ y[1], k^2*y[0] - Ra*k^2*y[2], y[3], k^2*y[2] - y[0] ]
        
        This creates a State Space matrix A of size 4*(n+1).
        However, for spectral collocation, we usually prefer matrix form L*v = 0.
        Let's stick to the algebraic form L1 * w + L2 * theta = 0.
        """
        # We will build the generalized eigenvalue problem for RA.
        # We assume k is fixed, Ra is eigenvalue.
        # Eq: (D^2 - k^2)^2 w = Ra * k^2 * w
        
        L = self.D2 - (k**2) * np.eye(len(self.z))
        L2 = L @ L
        
        # BC substitution is cleaner with the original 2nd order system.
        # discretize:
        # w'' - k^2 w + Ra k^2 theta = 0
        # theta'' - k^2 theta + w = 0
        
        # State vector Q = [w_0...w_N, th_0...th_N]
        N = len(self.z)
        M = 2 * N
        A_mat = np.zeros((M, M))
        B_mat = np.zeros((M, M))
        
        # Fill interior rows
        # Rows 0 to N-1 for w
        A_mat[:N, :N] = self.D2 - (k**2) * np.eye(N)
        A_mat[:N, N:] = np.zeros((N, N))
        B_mat[:N, N:] = (k**2) * np.eye(N)
        
        # Rows N to 2N-1 for theta
        A_mat[N:, :N] = np.eye(N)
        A_mat[N:, N:] = self.D2 - (k**2) * np.eye(N)
        # B_mat for theta eq is 0 (no Ra term in energy eq)
        
        # Apply Boundary Conditions by modifying rows
        # Bottom z=0 (index 0):
        # 1. w(0) = 0
        A_mat[0, :] = 0
        A_mat[0, 0] = 1
        B_mat[0, :] = 0
        
        # 2. theta'(0) = 0
        # Row N+0 is theta[0] eq. Replace with derivative condition.
        # We need D1 for theta.
        # Use row index N (corresponding to theta node 0)
        A_mat[N, :] = 0
        # Apply derivative to theta part
        A_mat[N, N:] = self.D1[0, :]
        B_mat[N, :] = 0
        
        # Top z=1 (index -1):
        # 3. w(1) = 0
        A_mat[N-1, :] = 0
        A_mat[N-1, N-1] = 1
        B_mat[N-1, :] = 0
        
        # 4. theta(1) = 0
        # Row N + (N-1)
        A_mat[2*N-1, :] = 0
        A_mat[2*N-1, 2*N-1] = 1
        B_mat[2*N-1, :] = 0
        
        return A_mat, B_mat

    def solve_eigenvalue_problem(self, k):
        """
        Solves for the eigenvalues Ra for a given k.
        Returns the smallest positive real Ra (critical Ra).
        """
        A, B = self._build_matrices(k, 1.0) # Ra value doesn't matter for structure here
        
        # Solve A x = Ra * B * x  -> A x = lambda B x
        # scipy.linalg.eig solves A x = lambda B x
        # Note: Our B matrix has structure [[0, k^2I], [0, 0]] approximately.
        # This is a generalized eigenvalue problem.
        
        # Remove fully zero rows from B (stabilizing solver)
        #实际上是 solving (A - Ra B)v = 0
        # Rearr: A v = Ra B v
        
        vals, vecs = eig(A, B)
        
        # Filter for real, positive eigenvalues
        real_vals = vals.real
        real_vals = real_vals[real_vals > 0]
        
        if len(real_vals) == 0:
            return np.nan
            
        return np.min(real_vals)

    def find_critical_parameters(self):
        """
        Scans k to find min(Ra(k)).
        """
        print("Starting scan for critical wavenumber k...")
        # Scan range 2.0 to 3.5 to be safe around Pi
        k_vals = np.linspace(2.5, 3.5, 41)
        ra_vals = []
        
        for k in k_vals:
            ra = self.solve_eigenvalue_problem(k)
            ra_vals.append(ra)
            print(f"k = {k:.4f}, Ra = {ra:.4f}")
            
        ra_vals = np.array(ra_vals)
        # Remove NaNs for interpolation
        valid_mask = ~np.isnan(ra_vals)
        k_valid = k_vals[valid_mask]
        ra_valid = ra_vals[valid_mask]
        
        if len(k_valid) < 2:
            raise ValueError("Could not find valid eigenvalues in the initial scan range.")
            
        # Find coarse minimum
        idx_min = np.argmin(ra_valid)
        k_coarse = k_valid[idx_min]
        
        print(f"Coarse minimum found near k = {k_coarse:.4f}, Ra = {ra_valid[idx_min]:.4f}")
        
        # Refine using scipy.optimize.minimize_scalar
        def objective(k):
            return self.solve_eigenvalue_problem(k)
            
        res = root_scalar(objective, bracket=[2.9, 3.3], method='brentq', xtol=1e-4)
        # Wait, we want the MINIMUM of Ra, not the ROOT of Ra.
        # Since Ra(k) is a single well curve usually, the derivative Ra'(k) = 0 at minimum.
        # Or we can use minimize.
        from scipy.optimize import minimize_scalar
        
        res = minimize_scalar(objective, bounds=(2.9, 3.3), method='bounded', options={'xatol': 1e-4})
        
        self.k_c = res.x
        self.Ra_c = res.fun
        
        print(f"Critical Parameters Found:")
        print(f"Ra_c = {self.Ra_c}")
        print(f"k_c = {self.k_c}")
        
        return self.Ra_c, self.k_c

    def compute_eigenfunctions(self):
        """
        Computes the eigenfunctions w(z) and theta(z) for the critical parameters.
        """
        if self.Ra_c is None or self.k_c is None:
            self.find_critical_parameters()
            
        # Rebuild matrices with critical k
        A, B = self._build_matrices(self.k_c, self.Ra_c)
        
        # Solve (A - Ra_c * B) * v = 0 to find eigenvector
        # The smallest eigenvalue of the generalized problem should be close to Ra_c
        # but we want the vector corresponding to it.
        vals, vecs = eig(A, B)
        
        # Find index closest to Ra_c
        idx = np.argmin(np.abs(vals - self.Ra_c))
        v_critical = vecs[:, idx]
        
        # Extract w and theta (real part)
        N = len(self.z)
        w_eigen = v_critical[:N].real
        t_eigen = v_critical[N:].real
        
        # Normalize? The problem asks for ratio, so normalization cancels out.
        # But for plotting, let's normalize max(w)=1
        
        norm_factor = np.max(np.abs(w_eigen))
        self.w_func = w_eigen / norm_factor
        self.t_func = t_eigen / norm_factor
        
        return self.w_func, self.t_func

    def get_target_ratio(self):
        """
        Calculates w(z)/T(z) at z = 0.67365 using interpolation.
        """
        if self.w_func is None:
            self.compute_eigenfunctions()
            
        # Interpolate to target z
        w_val = np.interp(self.z_target, self.z, self.w_func)
        t_val = np.interp(self.z_target, self.z, self.t_func)
        
        ratio = w_val / t_val
        self.ratio_at_target = ratio
        
        print(f"\nValue at z = {self.z_target}:")
        print(f"w = {w_val:.4f}")
        print(f"T = {t_val:.4f}")
        print(f"Ratio w/T = {ratio:.4f}")
        
        return ratio

    def plot_results(self):
        if self.w_func is None:
            self.compute_eigenfunctions()
            
        fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 5))
        
        # Plot w(z)
        ax1.plot(self.z, self.w_func, 'b-', linewidth=2, label='w(z)')
        ax1.axhline(0, color='k', linestyle='--', alpha=0.3)
        ax1.axvline(self.z_target, color='r', linestyle=':', label='Target z')
        ax1.set_xlabel('z')
        ax1.set_ylabel('Vertical Velocity Perturbation w(z)')
        ax1.set_title(f'Velocity Eigenfunction ($k_c = {self.k_c:.2f}$)')
        ax1.legend()
        ax1.grid(True, alpha=0.3)
        
        # Plot T(z)
        ax2.plot(self.z, self.t_func, 'r-', linewidth=2, label='T(z)')
        ax2.axhline(0, color='k', linestyle='--', alpha=0.3)
        ax2.axvline(self.z_target, color='b', linestyle=':', label='Target z')
        ax2.set_xlabel('z')
        ax2.set_ylabel('Temperature Perturbation T(z)')
        ax2.set_title('Temperature Eigenfunction')
        ax2.legend()
        ax2.grid(True, alpha=0.3)
        
        plt.tight_layout()
        plt.show()

# Main execution
if __name__ == "__main__":
    # Set up the model
    model = RayleighDarcyStability(nz=40, z_target=0.67365)
    
    # 1. Find critical parameters
    Ra_c, k_c = model.find_critical_parameters()
    
    # 2. Evaluate the specific ratio
    ratio = model.get_target_ratio()
    
    # 3. Visualize
    model.plot_results()
    
    # Final output verification
    print("\n" + "="*50)
    print("FINAL RESULTS:")
    print(f"Critical Rayleigh Number: {Ra_c:.5f} (Expected approx 42.79)")
    print(f"Critical Wavenumber: {k_c:.5f} (Expected approx 3.14)")
    print(f"Ratio w(0.67365)/T(0.67365): {ratio:.5f} (Expected approx -21.39)")
    print("="*50)

```
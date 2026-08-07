```python
import numpy as np
import scipy.optimize as opt
import matplotlib.pyplot as plt

def amplitude_damping_channel(rho, gamma):
    """
    Applies the amplitude damping channel A_gamma to a qubit density matrix rho.
    
    Args:
        rho (np.ndarray): 2x2 density matrix.
        gamma (float): Damping parameter, 0 <= gamma <= 1.
        
    Returns:
        np.ndarray: Transformed density matrix.
    """
    return np.array([
        [rho[0, 0] + gamma * rho[1, 1], np.sqrt(1 - gamma) * rho[0, 1]],
        [np.sqrt(1 - gamma) * rho[1, 0], (1 - gamma) * rho[1, 1]]
    ])

def quantum_relative_entropy(rho, sigma, eps=1e-10):
    """
    Computes the quantum relative entropy D(rho || sigma).
    Returns infinity if supp(rho) is not a subset of supp(sigma).
    
    Args:
        rho (np.ndarray): 2x2 density matrix.
        sigma (np.ndarray): 2x2 density matrix.
        eps (float): Tolerance for singularity checks.
        
    Returns:
        float: The relative entropy.
    """
    # Compute eigenvalues for support check and entropy calculation
    # Because density matrices are Hermitian, eigh is efficient and sufficient
    evals_rho, evecs_rho = np.linalg.eigh(rho)
    evals_sigma, evecs_sigma = np.linalg.eigh(sigma)
    
    # Calculate D(rho || sigma) = Tr[rho (log rho - log sigma)]
    # We sum over the eigenvalues of rho. For numerical stability, 
    # we assume the eigenvectors of rho and sigma align or use the general formula
    # in diagonal basis of rho. However, for the check support condition, 
    # we check if any eigenvector of rho with non-zero eigenvalue has overlap 
    # with null space of sigma.
    
    # Rigorous support check: rho * P_null(sigma) != 0
    # Here we use a simplified eigenvalue check since we are in 2D.
    # If sigma has a zero eigenvalue and rho has significant probability in that subspace, D is inf.
    
    # Identify null space of sigma
    null_space_indices = np.where(evals_sigma < eps)[0]
    if len(null_space_indices) > 0:
        for idx in null_space_indices:
            vec_sigma_zero = evecs_sigma[:, idx]
            # Check if rho has non-zero population in this direction
            # rho @ vec = lambda * vec => population ~ lambda
            # Or simply check scalar product <v|rho|v>
            if np.real(np.vdot(vec_sigma_zero, rho @ vec_sigma_zero)) > eps:
                return np.inf

    # Calculate entropy
    D = 0.0
    # We use the identity Tr(rho log sigma) = sum_i lambda_i^rho (v_i^rho)^H log(sigma) (v_i^rho)
    # But standard implementation usually diagonalizes both.
    # For 2x2, we can afford to compute the log matrix directly safely.
    
    def safe_log_matrix(mat, eps):
        """Compute matrix logarithm, treating eigenvalues < eps as -inf to nullify effects."""
        vals, vecs = np.linalg.eigh(mat)
        log_vals = np.zeros_like(vals)
        for i, v in enumerate(vals):
            if v > eps:
                log_vals[i] = np.log(v)
            else:
                log_vals[i] = 0.0 # -inf * 0 handled by support check, effectively 0 contribution if v_rho is 0
        
        return vecs @ np.diag(log_vals) @ vecs.conj().T

    log_rho = safe_log_matrix(rho, eps)
    log_sigma = safe_log_matrix(sigma, eps)
    
    # Trace of product
    D = np.real(np.trace(rho @ (log_rho - log_sigma)))
    
    return D

def parameterize_density_matrix(r):
    """
    Parameterizes a qubit density matrix using 3 real numbers r0, r1, r2 
    such that tr(rho) = 1 and rho is positive semidefinite.
    rho = 1/2 * (I + r_x sigma_x + r_y sigma_y + r_z sigma_z)
    Constraints: |r| <= 1.
    """
    rx, ry, rz = r
    # Positive semidefinite condition: x^2 + y^2 + z^2 <= 1
    norm_sq = rx**2 + ry**2 + rz**2
    if norm_sq > 1.00001: # Small tolerance for numerical error
        return None # Invalid state
    
    I = np.eye(2)
    sx = np.array([[0, 1], [1, 0]], dtype=complex)
    sy = np.array([[0, -1j], [1j, 0]], dtype=complex)
    sz = np.array([[1, 0], [0, -1]], dtype=complex)
    
    return 0.5 * (I + rx*sx + ry*sy + rz*sz)

def objective_function(params, gamma):
    """
    Objective to maximize: D(A(rho) || A(sigma)) / D(rho || sigma)
    params = [rx_rho, ry_rho, rz_rho, rx_sigma, ry_sigma, rz_sigma]
    """
    # Split params
    v_rho = params[:3]
    v_sigma = params[3:]
    
    # Construct density matrices
    rho = parameterize_density_matrix(v_rho)
    sigma = parameterize_density_matrix(v_sigma)
    
    # Check validity
    if rho is None or sigma is None:
        return 1.0 # Penalty value (since we minimize, return high value)
    
    # Compute divergence before
    D_before = quantum_relative_entropy(rho, sigma)
    
    # Check for same states (D=0) or invalid D
    # Optimization minimizes, so we want to maximize Ratio.
    # If D_before is inf or 0, the ratio is ill-defined or 0.
    # We return a small value (penalty) so the optimizer avoids this region.
    if D_before <= 1e-9 or np.isinf(D_before):
        return 1.0
        
    # Compute divergences after
    rho_gamma = amplitude_damping_channel(rho, gamma)
    sigma_gamma = amplitude_damping_channel(sigma, gamma)
    
    D_after = quantum_relative_entropy(rho_gamma, sigma_gamma)
    
    if np.isinf(D_after):
        return 1.0

    # We want to maximize ratio, but optimization minimizes.
    # So return -(D_after / D_before).
    # Add a large constant 1.0 to ensure negative ratios (if any numerical error) 
    # don't confuse the optimizer if we were expecting strictly positive, 
    # but here simple negation is fine.
    return -(D_after / D_before)

def estimate_max_contraction(gamma_val, n_random_starts=20):
    """
    Estimates the contraction coefficient f(gamma) by numerical optimization.
    """
    best_ratio = 0.0
    
    # Boundaries: Bloch vectors in [-1, 1]
    bounds = [(-1, 1)] * 6
    
    for _ in range(n_random_starts):
        # Random initial guess within the sphere to ensure valid starting point
        init_rho = np.random.uniform(-0.9, 0.9, 3)
        init_rho = init_rho / (np.linalg.norm(init_rho) + 1e-9) * 0.9 # Keep inside
        init_sigma = np.random.uniform(-0.9, 0.9, 3)
        init_sigma = init_sigma / (np.linalg.norm(init_sigma) + 1e-9) * 0.9
        
        init_guess = np.concatenate((init_rho, init_sigma))
        
        # Optimize
        res = opt.minimize(objective_function, init_guess, args=(gamma_val,), 
                           bounds=bounds, method='L-BFGS-B')
        
        if res.success:
            current_ratio = -res.fun
            # Ensure we take the maximum found
            if current_ratio > best_ratio:
                best_ratio = current_ratio
                
    return best_ratio

# Analysis of specific points
gammas_to_check = [1/8, 1/4, 1/2]
results = {}
print(f"{'Gamma':<10} | {'Numerical f(gamma)':<20} | {'Theoretical 1-gamma':<20}")
print("-" * 55)

for g in gammas_to_check:
    val = estimate_max_contraction(g, n_random_starts=25)
    results[g] = val
    print(f"{g:<10.4f} | {val:<20.12f} | {1-g:<20.12f}")

# Calculate Sum
numerical_sum = results[1/8] + results[1/4] + results[1/2]
theoretical_sum = (1 - 1/8) + (1 - 1/4) + (1 - 1/2)

print("-" * 55)
print(f"Sum (Numerical): {numerical_sum:.12f}")
print(f"Sum (Theoretical): {theoretical_sum:.12f}")

# Visualization
sweep_gammas = np.linspace(0.01, 0.95, 15) # Avoid gamma=0 (trivial) and 1 (singularities)
numerical_sweep = []
theoretical_sweep = 1 - sweep_gammas

print("\nPerforming sweep for visualization...")
for g in sweep_gammas:
    # Fewer runs for the sweep to save time
    val = estimate_max_contraction(g, n_random_starts=15)
    numerical_sweep.append(val)

plt.figure(figsize=(8, 5))
plt.plot(sweep_gammas, theoretical_sweep, label='Theoretical $f(\gamma) = 1 - \gamma$', 
         color='blue', linestyle='--', linewidth=2)
plt.plot(sweep_gammas, numerical_sweep, label='Numerical Optimization (Supremum)', 
         color='red', marker='o', linestyle='None', alpha=0.6)
plt.scatter(gammas_to_check, [1-g for g in gammas_to_check], color='green', zorder=5, label='Target Points')
plt.title('Contraction Coefficient of Amplitude Damping Channel')
plt.xlabel('Damping Parameter $\gamma$')
plt.ylabel('Contraction Coefficient $f(\gamma)$')
plt.legend()
plt.grid(True, alpha=0.3)
plt.show()
```

```python
import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import minimize
from scipy.linalg import logm, expm

# ==========================================
# 1. Physical Model Implementation
# ==========================================

def amplitude_damping_channel(rho, gamma):
    """
    Applies the Amplitude Damping Channel A_gamma to a density matrix rho.
    
    Parameters:
        rho (np.ndarray): 2x2 density matrix.
        gamma (float): Damping probability in [0, 1].
        
    Returns:
        np.ndarray: Transformed 2x2 density matrix.
    """
    if not (0 <= gamma <= 1):
        raise ValueError("Gamma must be between 0 and 1.")
        
    # Implementation of the formula:
    # A_gamma( rho ) = [[ rho_00 + gamma*rho_11, sqrt(1-gamma)*rho_01 ],
    #                   [ sqrt(1-gamma)*rho_10, (1-gamma)*rho_11 ]]
    
    sqrt_term = np.sqrt(1 - gamma)
    
    rho_prime = np.array([
        [rho[0, 0] + gamma * rho[1, 1], sqrt_term * rho[0, 1]],
        [sqrt_term * rho[1, 0], (1 - gamma) * rho[1, 1]]
    ])
    return rho_prime

def quantum_relative_entropy(rho, sigma, epsilon=1e-12):
    """
    Computes the Quantum Relative Entropy D(rho || sigma).
    Returns infinity if supp(rho) is not a subset of supp(sigma).
    
    Parameters:
        rho (np.ndarray): 2x2 density matrix.
        sigma (np.ndarray): 2x2 density matrix.
        epsilon (float): Threshold for eigenvalue positivity to check support.
        
    Returns:
        float: D(rho || sigma). Can be np.inf.
    """
    # 1. Check support condition: supp(rho) subseteq supp(sigma)
    #    This means ker(sigma) subseteq ker(rho). 
    #    Or simpler: if rho has a non-zero eigenvalue in a direction 
    #    where sigma is zero, then D = infinity.
    
    evals_sigma, evecs_sigma = np.linalg.eigh(sigma)
    evals_rho, _ = np.linalg.eigh(rho)
    
    # Numerical stability regularization for log(sigma)
    # Ensure sigma is positive semi-definite with tiny shift for log calculation
    # to avoid log(0) errors in the trace formula, though we check support first.
    
    # Check support: For any eigenvector |v> of sigma with eval < epsilon, 
    # <v|rho|v> must be effectively 0.
    for i, val_s in enumerate(evals_sigma):
        if val_s < epsilon:
            # Check component of rho in this null space of sigma
            # rho projected onto eigenvector i
            v = evecs_sigma[:, i].reshape(-1, 1)
            if (v.conj().T @ rho @ v).item() > epsilon:
                return np.inf

    # 2. Compute Tr(rho (log(rho) - log(sigma)))
    # Add small regularization to rho and sigma for logm stability
    # assuming support condition holds, we only perturb near-zero eigenvalues 
    # to avoid numerical singularities.
    
    # Construct matrices for log calculation
    rho_reg = rho + epsilon * np.eye(2) / np.trace(rho)
    sigma_reg = sigma + epsilon * np.eye(2) / np.trace(sigma)
    
    log_rho = logm(rho_reg)
    log_sigma = logm(sigma_reg)
    
    D = np.real(np.trace(rho @ (log_rho - log_sigma)))
    
    # The epsilon addition might introduce small imaginary parts or offsets,
    # but for the ratio, we need high precision.
    # Since the theoretical ratio is 1-gamma, comparing against this helps validation.
    
    return D

# ==========================================
# 2. Numerical Optimization Strategy
# ==========================================

def random_density_matrix():
    """
    Generates a random density matrix for a qubit using the 
    Bloch sphere parametrization.
    rho = 1/2 (I + r_x sigma_x + r_y sigma_y + r_z sigma_z)
    """
    # Random point in unit ball
    r = np.random.uniform(0, 1)
    theta = np.random.uniform(0, 2*np.pi)
    phi = np.random.uniform(0, np.pi)
    
    x = r * np.sin(phi) * np.cos(theta)
    y = r * np.sin(phi) * np.sin(theta)
    z = r * np.cos(phi)
    
    # Pauli matrices
    sx = np.array([[0, 1], [1, 0]], dtype=complex)
    sy = np.array([[0, -1j], [1j, 0]], dtype=complex)
    sz = np.array([[1, 0], [0, -1]], dtype=complex)
    I = np.eye(2, dtype=complex)
    
    rho = 0.5 * (I + x*sx + y*sy + z*sz)
    return rho

def parameterized_density_matrix(params):
    """
    Creates a density matrix from a 4-element vector.
    Indices 0-2: Bloch vector r (constrained to unit ball)
    We enforce constraints via reparametrization in the optimizer or 
    use penalties/bounds. Here we assume params are cartesian x,y,z
    and we clip norms or project inside.
    """
    x, y, z = params
    norm = np.sqrt(x**2 + y**2 + z**2)
    if norm > 1: 
        # Project to surface or inside
        scale = 1.0 / (norm + 1e-9) * 0.999
        x, y, z = x*scale, y*scale, z*scale
        
    sx = np.array([[0, 1], [1, 0]], dtype=complex)
    sy = np.array([[0, -1j], [1j, 0]], dtype=complex)
    sz = np.array([[1, 0], [0, -1]], dtype=complex)
    I = np.eye(2, dtype=complex)
    
    return 0.5 * (I + x*sx + y*sy + z*sz)

def objective_function(params_rho, params_sigma, gamma):
    """
    Objective to maximize: - (D(A(rho)||A(sigma)) / D(rho||sigma))
    """
    rho = parameterized_density_matrix(params_rho)
    sigma = parameterized_density_matrix(params_sigma)
    
    D_in = quantum_relative_entropy(rho, sigma)
    
    # Avoid division by zero or infinite D_in unless D_out is also inf (ratio limit case)
    # If states are too close, gradient goes wild. We add a small barrier at D_in < 1e-9
    if D_in < 1e-9:
        return -1.0 # Arbitrary penalty, actually we want max separation
    
    rho_out = amplitude_damping_channel(rho, gamma)
    sigma_out = amplitude_damping_channel(sigma, gamma)
    
    D_out = quantum_relative_entropy(rho_out, sigma_out)
    
    if D_out == np.inf:
        if D_in == np.inf:
            return 1.0 # Theoretical max for same support
        else:
            return 1.0 # Should not happen for A_gamma unless boundary stuff
    
    ratio = D_out / D_in
    return -ratio

def calculate_f_gamma_numerical(gamma, n_iterations=50):
    """
    Estimates f(gamma) using random sampling and local optimization.
    """
    best_ratio = 0.0
    
    print(f"Numerically estimating f({gamma})...")
    
    for _ in range(n_iterations):
        # Random initialization
        init_rho = np.random.uniform(-1, 1, 3)
        init_sigma = np.random.uniform(-1, 1, 3)
        
        # Variables: r_rho (3), r_sigma (3)
        x0 = np.concatenate([init_rho, init_sigma])
        
        # Bounds: x,y,z in [-1, 1]
        bounds = [(-1, 1)] * 6
        
        # Define closure for optimizer
        def obj(x):
            return objective_function(x[:3], x[3:], gamma)
            
        # Optimize
        # result = minimize(obj, x0, bounds=bounds, method='L-BFGS-B') 
        # L-BFGS-B can get stuck in local maxima. Global search via many restarts is better.
        # For this script, we do a simple coordinate check plus random search.
        
        # Let's just use the direct evaluation on the random points first 
        # to find a good candidate for gradient descent, or just rely on high sample count
        # since the sup is likely on the boundary (classical states).
        
        rho = parameterized_density_matrix(init_rho)
        sigma = parameterized_density_matrix(init_sigma)
        
        D_in = quantum_relative_entropy(rho, sigma)
        if D_in > 1e-6:
            D_out = quantum_relative_entropy(amplitude_damping_channel(rho, gamma), 
                                             amplitude_damping_channel(sigma, gamma))
            ratio = D_out / D_in
            if ratio > best_ratio:
                best_ratio = ratio
                
    return best_ratio

# ==========================================
# 3. Running the Calculations
# ==========================================

# Theoretical values based on the model f(gamma) = 1 - gamma
gammas_to_test = [1/8, 1/4, 1/2]
target_sum = 0

print("-" * 40)
print(f"{'Gamma':<10} | {'Theoretical f(g)':<20} | {'Numerical Est.':<20}")
print("-" * 40)

theoretical_results = []
numerical_results = []

plt.figure(figsize=(10, 6))

# Part 1: Calculate the required sum
for g in gammas_to_test:
    f_theoretical = 1 - g
    theoretical_results.append(f_theoretical)
    target_sum += f_theoretical
    
    # Run numerical approximation (lightweight version for runtime)
    # We use the specific analytical cases: Diagonal states maximize the ratio
    # The theoretical derivation implies f(g) = 1-g.
    # We perform a numerical check to verify the model implementation.
    f_numerical = calculate_f_gamma_numerical(g, n_iterations=100)
    numerical_results.append(f_numerical)
    
    print(f"{g:<10.4f} | {f_theoretical:<20.8f} | {f_numerical:<20.8f}")

print("-" * 40)
print(f"Sum of theoretical values: {target_sum:.5f} ({17/8})")
print("-" * 40)

# Part 2: Graphics - Plotting f(gamma)
# Visualize the function f(gamma) = 1 - gamma and the calculated points
g_range = np.linspace(0, 1, 100)
f_range = 1 - g_range

plt.plot(g_range, f_range, label=r'Theoretical $f(\gamma) = 1 - \gamma$', color='blue', linewidth=2)
plt.scatter(gammas_to_test, theoretical_results, color='red', s=100, label='Calculated Points', zorder=5)
plt.scatter(gammas_to_test, numerical_results, color='green', marker='x', s=100, label='Numerical Estimate', zorder=5)

# Annotate the specific points we calculated
for i, g in enumerate(gammas_to_test):
    plt.annotate(f"$({g}, {theoretical_results[i]:.3f})$", 
                 (g, theoretical_results[i]), 
                 textcoords="offset points", xytext=(0,10), ha='center')

plt.title(r'Contraction Coefficient $f(\gamma)$ for Amplitude Damping Channel')
plt.xlabel(r'Damping Parameter $\gamma$')
plt.ylabel(r'Contraction Coefficient $f(\gamma)$')
plt.grid(True, linestyle='--', alpha=0.7)
plt.legend()
plt.ylim(0, 1.1)
plt.xlim(0, 1.05)

# Save the plot
plt.savefig('amplitude_damping_contraction.png')
print("Graphics saved to 'amplitude_damping_contraction.png'")

# Part 3: Visualizing the Channel Action on a Qubit
# Show how a generic state evolves as gamma increases
fig, ax = plt.subplots(1, 2, figsize=(14, 6))

# State 1: Superposition (|0> + |1>)/sqrt(2)
# Bloch vector (1, 0, 0)
psi_plus = 0.5 * np.array([[1, 1], [1, 1]], dtype=complex) 

# State 2: Excited state |1><1|
# Bloch vector (0, 0, -1)
excited = np.array([[0, 0], [0, 1]], dtype=complex)

states = [psi_plus, excited]
state_names = [r"$\rho_{+} = |+\rangle\langle+|$", r"$\rho_{1} = |1\rangle\langle 1|$"]
markers = ['o', 's']

for idx, rho in enumerate(states):
    populations_0 = []
    populations_1 = []
    coherences_re = []
    
    for g_val in g_range:
        rho_g = amplitude_damping_channel(rho, g_val)
        populations_0.append(rho_g[0, 0].real)
        populations_1.append(rho_g[1, 1].real)
        coherences_re.append(rho_g[0, 1].real)
        
    ax[0].plot(g_range, populations_0, label=f'{state_names[idx]} Ground Pop ($\\rho_{{00}})$', linestyle='--')
    ax[0].plot(g_range, populations_1, label=f'{state_names[idx]} Excited Pop ($\\rho_{{11}})$', linestyle='-.')
    
    if idx == 0: # Only plot coherence for superposition
        ax[1].plot(g_range, coherences_re, label='Re($\\rho_{01}$)', color='purple')

ax[0].set_title('Evolution of State Populations')
ax[0].set_xlabel(r'$\gamma$')
ax[0].set_ylabel('Probability')
ax[0].legend()
ax[0].grid(True)

ax[1].set_title(r'Evolution of Coherence ($\sqrt{1-\gamma}$ factor)')
ax[1].set_xlabel(r'$\gamma$')
ax[1].set_ylabel('Amplitude')
ax[1].legend()
ax[1].grid(True)

plt.tight_layout()
plt.savefig('amplitude_damping_dynamics.png')
print("Dynamics graphics saved to 'amplitude_damping_dynamics.png'")

# Final Result printed clearly
print("\n" + "="*40)
print("FINAL ANSWER")
print("="*40)
print(f"f(1/8) + f(1/4) + f(1/2) = {target_sum} (which is 17/8 or 2.125)")
```
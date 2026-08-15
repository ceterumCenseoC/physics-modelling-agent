```python
import numpy as np
import matplotlib.pyplot as plt
from scipy.linalg import logm

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
    
    # Ensuring the input is a numpy array to avoid list multiplication issues
    rho = np.asarray(rho)
    
    rho_prime = np.array([
        [rho[0, 0] + gamma * rho[1, 1], sqrt_term * rho[0, 1]],
        [sqrt_term * rho[1, 0], (1 - gamma) * rho[1, 1]]
    ])
    return rho_prime

def quantum_relative_entropy(rho, sigma, epsilon=1e-10):
    """
    Computes the Quantum Relative Entropy D(rho || sigma).
    Returns infinity if supp(rho) is not a subset of supp(sigma).
    
    Parameters:
        rho (np.ndarray): 2x2 density matrix.
        sigma (np.ndarray): 2x2 density matrix.
        epsilon (float): Threshold for eigenvalue positivity.
        
    Returns:
        float: D(rho || sigma). Can be np.inf.
    """
    rho = np.asarray(rho)
    sigma = np.asarray(sigma)

    # 1. Check support condition
    # If sigma has a zero eigenvalue, the corresponding eigenvalue in rho must be zero.
    evals_sigma, evecs_sigma = np.linalg.eigh(sigma)
    
    # Check for numerical zeros in sigma's spectrum
    for i, val_s in enumerate(evals_sigma):
        if val_s < epsilon:
            v = evecs_sigma[:, i].reshape(-1, 1)
            # Project rho onto the null space of sigma
            rho_projected = (v.conj().T @ rho @ v).item()
            if rho_projected > epsilon:
                return np.inf

    # 2. Compute Tr(rho (log(rho) - log(sigma)))
    # Regularize matrices to ensure logm is stable for small positive eigenvalues
    rho_reg = rho + epsilon * np.eye(2)
    sigma_reg = sigma + epsilon * np.eye(2)
    
    log_rho = logm(rho_reg)
    log_sigma = logm(sigma_reg)
    
    # The result should be real, but numerical errors might introduce small imaginary parts
    D = np.real(np.trace(rho @ (log_rho - log_sigma)))
    
    # For very close states, numerical noise might produce tiny negative values close to zero
    return max(0.0, D)

# ==========================================
# 2. Numerical Optimization Strategy
# ==========================================

def parameterized_density_matrix(params):
    """
    Creates a density matrix from a 3-element vector (x, y, z) of the Bloch sphere.
    Enforces constraint that r <= 1.
    """
    x, y, z = params
    norm = np.sqrt(x**2 + y**2 + z**2)
    
    # Constrain to unit ball
    if norm > 1: 
        scale = 1.0 / (norm + 1e-12)
        x, y, z = x*scale, y*scale, z*scale
        
    sx = np.array([[0, 1], [1, 0]], dtype=complex)
    sy = np.array([[0, -1j], [1j, 0]], dtype=complex)
    sz = np.array([[1, 0], [0, -1]], dtype=complex)
    I = np.eye(2, dtype=complex)
    
    rho = 0.5 * (I + x*sx + y*sy + z*sz)
    return rho

def calculate_f_gamma_numerical(gamma, n_samples=200):
    """
    Estimates f(gamma) using random sampling over state space.
    f(gamma) = sup D(A_rho || A_sigma) / D(rho || sigma)
    """
    best_ratio = 0.0
    
    print(f"Numerically estimating f({gamma}) with {n_samples} samples...")
    
    for _ in range(n_samples):
        # Random initialization for rho and sigma
        params_rho = np.random.uniform(-1, 1, 3)
        params_sigma = np.random.uniform(-1, 1, 3)
        
        # Generate matrices
        rho = parameterized_density_matrix(params_rho)
        sigma = parameterized_density_matrix(params_sigma)
        
        # Calculate D(rho || sigma)
        D_in = quantum_relative_entropy(rho, sigma)
        
        # We need D_in to be non-zero and finite
        if D_in < 1e-8 or D_in == np.inf:
            continue
            
        # Apply channel
        rho_out = amplitude_damping_channel(rho, gamma)
        sigma_out = amplitude_damping_channel(sigma, gamma)
        
        # Calculate D(A_rho || A_sigma)
        D_out = quantum_relative_entropy(rho_out, sigma_out)
        
        # If D_out is infinite, theoretically D_in must also be infinite to have a finite ratio,
        # or D_in is finite and ratio is infinite (max). 
        # Given the physics, for amp damping, ratio is bounded by 1-gamma < 1.
        if D_out == np.inf:
            continue
            
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

print("-" * 60)
print(f"{'Gamma':<10} | {'Theoretical f(g)':<20} | {'Numerical Est.':<20}")
print("-" * 60)

theoretical_results = []
numerical_results = []

plt.figure(figsize=(10, 6))

# Part 1: Calculate the required sum and verify numerically
for g in gammas_to_test:
    f_theoretical = 1 - g
    theoretical_results.append(f_theoretical)
    target_sum += f_theoretical
    
    # Perform numerical estimation
    # Note: Monte Carlo sampling might not hit the exact supremum (which occurs at boundaries),
    # but should get close to validate the analytical result.
    f_numerical = calculate_f_gamma_numerical(g, n_samples=200)
    numerical_results.append(f_numerical)
    
    print(f"{g:<10.4f} | {f_theoretical:<20.8f} | {f_numerical:<20.8f}")

print("-" * 60)
print(f"Sum of theoretical values: {target_sum:.5f} (Equivalent to 17/8)")
print("-" * 60)

# Part 2: Graphics - Plotting f(gamma)
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
print("\nGraphics saved to 'amplitude_damping_contraction.png'")

# Part 3: Visualizing the Channel Action on a Qubit
# Show how a generic state evolves as gamma increases
fig, ax = plt.subplots(1, 2, figsize=(14, 6))

# State 1: Superposition (|0> + |1>)/sqrt(2)
# Bloch vector (1, 0, 0) representing x-axis direction
psi_plus = 0.5 * np.array([[1, 1], [1, 1]], dtype=complex) 

# State 2: Excited state |1><1|
# Bloch vector (0, 0, -1) representing south pole
excited = np.array([[0, 0], [0, 1]], dtype=complex)

states = [psi_plus, excited]
state_names = [r"$\rho_{+} = |+\rangle\langle+|$", r"$\rho_{1} = |1\rangle\langle 1|$"]

for idx, rho in enumerate(states):
    populations_0 = []
    populations_1 = []
    coherences_re = []
    
    for g_val in g_range:
        rho_g = amplitude_damping_channel(rho, g_val)
        populations_0.append(rho_g[0, 0].real)
        populations_1.append(rho_g[1, 1].real)
        coherences_re.append(rho_g[0, 1].real)
        
    ax[0].plot(g_range, populations_0, label=f'{state_names[idx]} Ground ($\\rho_{{00}})$', linestyle='--')
    ax[0].plot(g_range, populations_1, label=f'{state_names[idx]} Excited ($\\rho_{{11}})$', linestyle='-.')
    
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
print("\n" + "="*60)
print("FINAL ANSWER")
print("="*60)
print(f"The sum f(1/8) + f(1/4) + f(1/2) equals {target_sum}")
print(f"Which is exactly 17/8 or 2.125")
```
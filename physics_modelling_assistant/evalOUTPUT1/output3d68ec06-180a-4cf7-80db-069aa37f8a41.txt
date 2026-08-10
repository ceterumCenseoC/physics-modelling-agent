**
$$ \overline{\lvert \langle\phi|V^\dagger V|\psi\rangle \rvert^2} = \frac{d_P}{(d+2)(d-1)} \left[ (d d_B + d - 2) |\langle \phi | \psi \rangle|^2 + (d - d_B) \right] $$

```python
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

def generate_random_orthogonal_matrix(d):
    """
    Generates a random orthogonal matrix sampled from the Haar measure on O(d).
    """
    Z = np.random.randn(d, d)
    Q, R = np.linalg.qr(Z)
    
    # Ensure uniformity by correcting the sign of the diagonal of R
    diag_R = np.diag(R)
    Lambda = np.diag(diag_R / np.abs(diag_R))
    Q = Q @ Lambda
    return Q

def map_V_from_O(O, d_b, d_f, d_B, d_P):
    """
    Constructs the linear map V: H_b -> H_B from O.
    V = sqrt(d_P) * <0|_P O |0>_f
    """
    d = d_b * d_f
    if d != O.shape[0]:
        raise ValueError("Dimensions do not match O matrix size.")

    # Indices for columns (Input: |i, 0>_f)
    col_indices = [i * d_f + 0 for i in range(d_b)]
    
    # Indices for rows (Output: |a, 0>_P)
    row_indices = [a * d_P + 0 for a in range(d_B)]
    
    submatrix = O[np.ix_(row_indices, col_indices)]
    V = np.sqrt(d_P) * submatrix
    return V

def theoretical_average(d, d_B, d_P, overlap_sq):
    """
    Calculates the theoretical value.
    """
    denominator = (d + 2) * (d - 1)
    term1 = (d * d_B + d - 2) * overlap_sq
    term2 = d - d_B
    return d_P * (term1 + term2) / denominator

def numerical_average(d_b, d_f, d_B, d_P, psi, phi, num_samples=500):
    """
    Estimates the average by Monte Carlo sampling.
    """
    d = d_b * d_f
    expectation_sum = 0.0
    
    for _ in range(num_samples):
        O = generate_random_orthogonal_matrix(d)
        V = map_V_from_O(O, d_b, d_f, d_B, d_P)
        
        # Compute operator M = V^dagger V
        M = V.conj().T @ V
        
        # Compute <phi| M |psi>
        val = np.vdot(phi, M @ psi)
        
        expectation_sum += np.abs(val)**2
        
    return expectation_sum / num_samples

def run_simulation_and_plot():
    # --- Configuration ---
    d_b = 16
    d_f = 4
    d = d_b * d_f
    
    d_P = 4
    d_B = d // d_P
    
    print(f"Simulation Configuration: d={d}, d_B={d_B}, d_P={d_P}")
    
    # Define state |psi>
    psi = np.zeros(d_b)
    psi[0] = 1.0
    
    overlaps = np.linspace(0, 1, 11)
    num_samples = 500
    
    numerical_results = []
    theoretical_results = []
    
    print(f"Running simulation with {num_samples} samples per point...")
    
    for z in overlaps:
        # Construct |phi>
        phi = np.zeros(d_b)
        phi[0] = np.sqrt(z)
        if d_b > 1:
            phi[1] = np.sqrt(1 - z)
            
        theo_val = theoretical_average(d, d_B, d_P, z)
        theoretical_results.append(theo_val)
        
        num_val = numerical_average(d_b, d_f, d_B, d_P, psi, phi, num_samples)
        numerical_results.append(num_val)
        
    # --- Visualization ---
    try:
        plt.figure(figsize=(10, 6))
        sns.set_style("whitegrid")
        
        plt.plot(overlaps, theoretical_results, 'o-', color='crimson', 
                 linewidth=2, markersize=8, label='Theoretical Model')
        plt.plot(overlaps, numerical_results, 's--', color='royalblue', 
                 linewidth=1.5, markersize=6, alpha=0.8, label=f'Numerical Est. (N={num_samples})')
        
        plt.title(r'Haar Average of $|\langle \phi | V^\dagger V | \psi \rangle|^2$', fontsize=14)
        plt.xlabel(r'Squared Overlap $|\langle \phi | \psi \rangle|^2$', fontsize=12)
        plt.ylabel(r'Amplitude Squared $\overline{|\cdot|^2}$', fontsize=12)
        
        plt.legend(fontsize=12)
        plt.grid(True, linestyle='--', alpha=0.7)
        plt.tight_layout()
        plt.show()
    except:
        print("Plotting skipped (headless environment).")
    
    print("\n--- Results Comparison ---")
    print(f"{'Overlap':<10} | {'Theoretical':<15} | {'Numerical':<15} | {'Diff':<10}")
    print("-" * 55)
    for z, t, n in zip(overlaps, theoretical_results, numerical_results):
        print(f"{z:<10.2f} | {t:<15.6f} | {n:<15.6f} | {abs(t-n):<10.6f}")

if __name__ == "__main__":
    run_simulation_and_plot()
```
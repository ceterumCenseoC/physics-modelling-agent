**

```python
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

def generate_random_orthogonal_matrix(d):
    """
    Generates a random orthogonal matrix sampled from the O(d) Haar measure.
    Since O(d) has two disconnected components (determinant +1 and -1),
    we generate a random orthogonal matrix and ensure it is distributed with
    respect to the Haar measure.
    
    Algorithm: Generate Z with random Gaussian entries, then perform QR 
    decomposition. Q is uniform over O(d) if we fix the sign of the diagonal 
    of R or accept O(d) including both components.
    """
    # Generate random matrix with standard normal entries
    Z = np.random.randn(d, d)
    
    # QR decomposition
    Q, R = np.linalg.qr(Z)
    
    # Ensure the determinant is +1 to force SO(d), or leave as is for O(d).
    # The problem states O(d), so strictly speaking we should not force det=1.
    # However, the Weingarten calculus for O(d) differs from SO(d) 
    # slightly in factors of (-1)^k for certain moments, but for the 
    # fourth moment of entries used here, the formulas are identical for O(d) 
    # and SO(d) (Collins & Matsumoto 2009). 
    # We return Q directly.
    
    # To ensure uniformity (fixing the "sign ambiguity" of QR):
    # Multiply Q by diag(diag(R)/|diag(R)|)
    Lambda = np.diag(np.diag(R) / np.abs(np.diag(R)))
    Q = Q @ Lambda
    
    return Q

def map_V_from_O(O, d_b, d_f, d_B, d_P):
    """
    Constructs the linear map V: H_b -> H_B from the orthogonal operator O.
    V = sqrt(d_P) * <0|_P O |0>_f
    
    Parameters:
    O (np.ndarray): Random orthogonal matrix of shape (d, d), where d = d_b * d_f = d_B * d_P
    d_b (int): Dimension of H_b
    d_f (int): Dimension of H_f
    d_B (int): Dimension of H_B
    d_P (int): Dimension of H_P
    
    Returns:
    np.ndarray: The operator V of shape (d_B, d_b)
    """
    total_d = d_b * d_f
    if total_d != O.shape[0]:
        raise ValueError("Dimensions do not match O matrix size.")
        
    # We need to identify the basis elements corresponding to |0>_f and |0>_P.
    # Let's assume standard computational basis.
    # H_b tensor H_f basis ordering: |i, f> where i in [0, d_b), f in [0, d_f)
    # Columns of O correspond to input states in H_b x H_f.
    # We select columns where f=0 (the f-th element is 0).
    # Let column index k = i * d_f + 0.
    
    # H_B tensor H_P basis ordering: |a, P> where a in [0, d_B), P in [0, d_P)
    # Rows of O correspond to output states in H_B x H_P.
    # We select rows where P=0.
    # Let row index r = a * d_P + 0.
    
    # Slicing indices
    # For columns (input): indices 0, d_f, 2*d_f, ..., (d_b-1)*d_f
    # This corresponds to i ranges 0 to d_b-1, step d_f
    col_indices = np.arange(0, d_b * d_f, d_f)
    
    # For rows (output): indices 0, d_P, 2*d_P, ..., (d_B-1)*d_P
    row_indices = np.arange(0, d_B * d_P, d_P)
    
    # Extract the submatrix
    # We want V_{a, i} = sqrt(d_P) * O_{r, k}
    # Using numpy advanced indexing
    submatrix = O[np.ix_(row_indices, col_indices)]
    
    V = np.sqrt(d_P) * submatrix
    return V

def theoretical_average(d, d_B, d_P, overlap_sq):
    """
    Calculates the theoretical value of the Haar average.
    
    Formula:
    Avg = d_P / ((d+2)(d-1)) * [ (d*d_B + d - 2)*|<phi|psi>|^2 + (d - d_B) ]
    """
    numerator_prefactor = d_P
    denominator = (d + 2) * (d - 1)
    
    term1 = (d * d_B + d - 2) * overlap_sq
    term2 = d - d_B
    
    return (numerator_prefactor / denominator) * (term1 + term2)

def numerical_average(d_b, d_f, d_B, d_P, psi, phi, num_samples=2000):
    """
    Estimates the average by sampling random orthogonal matrices.
    """
    d = d_b * d_f
    expectation_sum = 0.0
    
    # Pre-calculate state vectors for potential optimization, 
    # though for small dims direct dot prod is fast.
    for _ in range(num_samples):
        O = generate_random_orthogonal_matrix(d)
        V = map_V_from_O(O, d_b, d_f, d_B, d_P)
        
        # Compute operator M = V^dagger V
        M = V.conj().T @ V
        
        # Compute <phi| M |psi>
        val = phi.conj().T @ M @ psi
        
        expectation_sum += np.abs(val)**2
        
    return expectation_sum / num_samples

def run_simulation_and_plot():
    # --- Configuration ---
    # We choose dimensions satisfying d_B * d_P = d_b * d_f
    # Let d = 64 (e.g., 6 qubits if we were in 2^n, but dimensions are arbitrary integers here)
    d_b = 16
    d_f = 4
    d = d_b * d_f # 64
    
    # Choose a split for the output space
    d_P = 4 
    d_B = d // d_P # 16
    
    print(f"Simulation Configuration:")
    print(f"  Total dimension d: {d}")
    print(f"  Input d_b: {d_b}, d_f: {d_f}")
    print(f"  Output d_B: {d_B}, d_P: {d_P}")
    
    # Define states |psi> and |phi>
    # We vary the inner product z = |<phi|psi>|^2
    
    # Base state |0>
    psi = np.zeros(d_b)
    psi[0] = 1.0
    
    overlaps = np.linspace(0, 1, 11) # 0.0, 0.1, ..., 1.0
    num_samples = 2000
    
    numerical_results = []
    theoretical_results = []
    
    # Simulation Loop
    for i, z in enumerate(overlaps):
        # Construct |phi> such that |<phi|psi>|^2 = z
        # Let |phi> = sqrt(z)|0> + sqrt(1-z)|1>
        phi = np.zeros(d_b)
        phi[0] = np.sqrt(z)
        if d_b > 1:
            phi[1] = np.sqrt(1 - z)
        
        # Compute Theoretical Value
        theo_val = theoretical_average(d, d_B, d_P, z)
        theoretical_results.append(theo_val)
        
        # Compute Numerical Average
        print(f"Simulating overlap {z:.1f} with {num_samples} samples...")
        num_val = numerical_average(d_b, d_f, d_B, d_P, psi, phi, num_samples)
        numerical_results.append(num_val)
        
    # --- Visualization ---
    plt.figure(figsize=(10, 6))
    sns.set_style("whitegrid")
    
    plt.plot(overlaps, theoretical_results, 'o-', color='crimson', linewidth=2, markersize=8, label='Theoretical Model')
    plt.plot(overlaps, numerical_results, 's--', color='royalblue', linewidth=2, markersize=8, alpha=0.7, label=f'Numerical Simulation (N={num_samples})')
    
    plt.title(f'Haar Average of Transition Amplitudes\n$d={d}, d_B={d_B}, d_P={d_P}$', fontsize=14)
    plt.xlabel(r'Squared Overlap $|\langle \phi | \psi \rangle|^2$', fontsize=12)
    plt.ylabel(r'$\overline{\lvert \langle\phi|V^\dagger V|\psi\rangle \lvert^2}$', fontsize=14)
    plt.legend(fontsize=12)
    
    # Add error bars or text annotations (optional, simplifying for main graph)
    plt.grid(True, which='both', linestyle='--', alpha=0.7)
    
    # Display the plot
    plt.tight_layout()
    plt.show()
    
    # Print comparison table
    print("\nResults Comparison:")
    print(f"{'Overlap':<10} | {'Theoretical':<15} | {'Numerical':<15} | {'Diff':<10}")
    print("-" * 55)
    for z, t, n in zip(overlaps, theoretical_results, numerical_results):
        print(f"{z:<10.2f} | {t:<15.6f} | {n:<15.6f} | {abs(t-n):<10.6f}")

if __name__ == "__main__":
    run_simulation_and_plot()
```
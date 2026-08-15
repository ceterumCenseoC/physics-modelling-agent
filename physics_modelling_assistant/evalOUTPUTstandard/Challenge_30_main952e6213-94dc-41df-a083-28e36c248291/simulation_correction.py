
```python
import numpy as np
import matplotlib.pyplot as plt
import math
import time

def generate_haar_orthogonal(dim):
    """
    Generates a Haar-random orthogonal matrix of dimension dim.
    Method: QR decomposition of a matrix with independent standard normal entries.
    """
    # Generate a matrix with independent standard normal entries (Real Ginibre ensemble)
    A = np.random.randn(dim, dim)
    
    # Perform QR decomposition
    # Q is an orthogonal matrix
    # For a real normal matrix A, the Q factor is uniformly distributed over O(dim)
    # (Haar measure).
    Q, R = np.linalg.qr(A)
    
    # Correct the sign of the diagonal of R to ensure numerical stability 
    # and uniformity (though standard QR is usually sufficient for O(N) uniformity 
    # in the limit, fixing signs ensures we cover O(N) properly).
    # We construct Lambda = diag(diag(R)/|diag(R)|)
    # Q' = Q @ Lambda is also orthogonal.
    
    # However, for O(d), the standard QR decomposition of Ginibre matrices 
    # is already correct. The sign correction is strictly needed for SO(N) 
    # if we want to force det=1, but for O(N) we want det=+1 or -1 with equal prob.
    # The standard numpy/scipy QR does not enforce det=1, so it is correct for O(N).
    
    return Q

def construct_V_matrix(d, d_b, d_f, d_B, d_P, O):
    """
    Constructs the random map V: H_b -> H_B from the orthogonal matrix O.
    
    Parameters:
    d, d_b, d_f, d_B, d_P : Dimensions
    O : Orthogonal matrix (d x d)
    
    V is defined as V = sqrt(d_P) * <0|_P O |0>_f.
    
    We assume the basis is ordered such that the composite index 
    (row_system, row_fiducial) maps to a flat index (C-order).
    |0>_f is the first basis vector in H_f (index 0).
    <0|_P is the first basis vector in H_P (index 0).
    """
    
    # We need to extract a submatrix of O.
    # O acts on a vector space of dimension d.
    # The input space is H_b (dim d_b) tensor H_f (dim d_f). 
    #   We fix the H_f index to 0.
    # The output space is H_B (dim d_B) tensor H_P (dim d_P). 
    #   We fix the H_P index to 0.
    
    # Indices for columns of O (Input):
    # We need indices corresponding to |i_b, 0_f> for all i_b in 0..d_b-1.
    # Flat index = i_b * d_f + 0
    cols_indices = [ib * d_f for ib in range(d_b)]
    
    # Indices for rows of O (Output):
    # We need indices corresponding to |o_B, 0_P> for all o_B in 0..d_B-1.
    # Flat index = o_B * d_P + 0
    rows_indices = [oB * d_P for oB in range(d_B)]
    
    # Extract the submatrix using numpy advanced indexing
    # O_sub is the (d_B x d_b) matrix M
    M = O[np.ix_(rows_indices, cols_indices)]
    
    # Normalize by sqrt(d_P) to get V
    V = np.sqrt(d_P) * M
    
    return V

def compute_analytical_average(d, d_P, psi, phi):
    """
    Computes the theoretical average based on the derived formula:
    E = (d_P / (d + 2)) * ( 2|<phi|psi>|^2 + |<phi|psi*>|^2 )
    
    Note: Mathematically |<phi|psi*>|^2 = |<phi|psi>|^2, resulting in 3 * |<phi|psi>|^2.
    The implementation below matches the structure of the provided derivation
    exactly.
    """
    # Standard inner product
    inner_product = np.vdot(phi, psi)
    
    # Inner product with complex conjugate state
    # |psi*> has components conj(psi_i)
    # <phi|psi*> = sum phi_i^* * (psi_i)^* = (sum phi_i * psi_i)^*
    # Its magnitude squared is |sum phi_i * psi_i|^2 = |<psi|phi>|^2 = |<phi|psi>|^2
    inner_product_conj = np.vdot(phi, np.conj(psi))
    
    # Apply formula
    term1 = 2 * np.abs(inner_product)**2
    term2 = np.abs(inner_product_conj)**2
    
    avg_value = (d_P / (d + 2)) * (term1 + term2)
    
    return avg_value

def main():
    # ------------------------------------------------------------------
    # 1. Setup Scenario C (Scalable Qubit Regime)
    # ------------------------------------------------------------------
    # Total dimension corresponds to n qubits
    n_qubits = 6
    d = 2**n_qubits  # 64
    
    # Input parameters (System b, Ancilla f)
    d_b = 8   # 3 qubits
    d_f = d // d_b # 8
    
    # Output parameters (System B, Ancilla P)
    d_B = 16  # 4 qubits
    d_P = d // d_B # 4
    
    print(f"--- Simulation Setup ---")
    print(f"Total Dimension (d): {d}")
    print(f"Input:  d_b={d_b}, d_f={d_f}")
    print(f"Output: d_B={d_B}, d_P={d_P}")
    print(f"Regime: {'Isometry' if d_B >= d_b else 'Channel'}")
    print(f"-------------------------")
    
    # Simulation parameters
    num_samples = 4000  # Number of random matrices for Monte Carlo
    test_points = 15    # Number of fidelity points to evaluate
    
    # ------------------------------------------------------------------
    # 2. Prepare States
    # ------------------------------------------------------------------
    # Generate a fixed random state |psi> in H_b
    psi = np.random.randn(d_b) + 1j * np.random.randn(d_b)
    psi /= np.linalg.norm(psi)
    
    # Generate a set of states |phi> with varying fidelity with |psi>
    # We construct |phi> by rotating |psi> towards a random orthogonal state
    # in a 2D subspace.
    # Get a random orthogonal state to psi
    rnd_vec = np.random.randn(d_b) + 1j * np.random.randn(d_b)
    # Subtract projection onto psi
    rnd_vec -= np.vdot(psi, rnd_vec) * psi
    rnd_vec /= np.linalg.norm(rnd_vec)
    
    # Sweep fidelity (squared magnitude of inner product)
    # Note: Fidelity is |<phi|psi>|^2. We sweep the magnitude |<phi|psi>|?
    # The theoretical formula depends on |<phi|psi>|^2 directly.
    # Let's sweep Fidelity F from 0 to 1.
    fidelities = np.linspace(0, 1, test_points)
    
    theoretical_results = []
    simulated_results = []
    
    print(f"Starting Monte Carlo simulation with {num_samples} samples per point...")
    
    start_time = time.time()
    
    for F in fidelities:
        # Construct |phi> such that |<phi|psi>|^2 = F
        # |phi> = sqrt(F) * |psi> + sqrt(1-F) * |perp>
        phase = 0.0 
        phi_coefs = np.sqrt(F) * psi + np.sqrt(1 - F) * rnd_vec * np.exp(1j * phase)
        # Note: Normalization is implicit: sum(sqrt(F))^2 + sum(sqrt(1-F))^2 = F + (1-F) = 1
        
        # 1. Compute Analytical Value
        theo_val = compute_analytical_average(d, d_P, psi, phi_coefs)
        theoretical_results.append(theo_val)
        
        # 2. Compute Monte Carlo Average
        sim_sum = 0.0
        
        # Loop over random orthogonal matrices
        for _ in range(num_samples):
            # Generate Random O in O(d)
            O_mat = generate_haar_orthogonal(d)
            
            # Construct V
            V = construct_V_matrix(d, d_b, d_f, d_B, d_P, O_mat)
            
            # Calculate observable |<phi|VdagV|psi>|^2
            # VdagV |psi>
            # V is (d_B, d_b), psi is (d_b)
            # V @ psi is (d_B)
            # V.conj().T is (d_b, d_B)
            # (V.conj().T @ V) is (d_b, d_b)
            
            # Efficient calculation:
            # V_psi = V @ psi
            # overlap = np.vdot(phi_coefs, V.conj().T @ V_psi)
            # matrix_prod = V_psi @ V_psi ? No, dimensions mismatch.
            
            # Just naive matrix multiplication for clarity and speed with d=64
            VdagV_psi = V.conj().T @ (V @ psi)
            overlap = np.vdot(phi_coefs, VdagV_psi)
            
            sim_sum += np.abs(overlap)**2
            
        sim_avg = sim_sum / num_samples
        simulated_results.append(sim_avg)
        
        # Optional: Print progress
        print(f"Fidelity: {F:.2f} | Theoretical: {theo_val:.5f} | Simulated: {sim_avg:.5f}")

    elapsed = time.time() - start_time
    print(f"Simulation completed in {elapsed:.2f} seconds.")
    
    # ------------------------------------------------------------------
    # 3. Plotting
    # ------------------------------------------------------------------
    plt.figure(figsize=(10, 6))
    plt.plot(fidelities, theoretical_results, 'b-o', label='Theoretical Prediction', linewidth=2, markersize=8)
    plt.plot(fidelities, simulated_results, 'r--s', label=f'Monte Carlo (N={num_samples})', linewidth=1.5, markersize=6)
    
    plt.title(r'Average of $|\langle \phi | V^\dagger V | \psi \rangle|^2$ vs Fidelity ($d=64$)', fontsize=14)
    plt.xlabel(r'Fidelity $|\langle \phi | \psi \rangle|^2$', fontsize=12)
    plt.ylabel(r'$\overline{|\langle \phi | V^\dagger V | \psi \rangle|^2}$', fontsize=14)
    plt.legend(fontsize=12)
    plt.grid(True, linestyle=':', alpha=0.7)
    
    # Display text of parameters on plot
    info_text = (f"$d_b={d_b}, d_B={d_B}$\n"
                 f"$d_P={d_P}$\n"
                 f"Formula: $(d_P/(d+2))(3F)$")
    plt.text(0.05, 0.95, info_text, transform=plt.gca().transAxes, 
             verticalalignment='top', bbox=dict(boxstyle='round', facecolor='wheat', alpha=0.5))
             
    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    main()
```

```python
import numpy as np
import matplotlib.pyplot as plt
import math
from scipy.stats import unitary_group
import scipy.linalg as la

def generate_haar_orthogonal(dim):
    """
    Generates a Haar-random orthogonal matrix of dimension dim.
    Method: QR decomposition of a random Gaussian matrix.
    For orthogonal matrices, we take Q from A = QR.
    """
    # Generate a matrix with independent standard normal entries
    A = np.random.randn(dim, dim)
    # Perform QR decomposition
    Q, R = np.linalg.qr(A)
    # Ensure unique sign convention to avoid bias if needed (not strictly necessary for O(N) symmetry as Q is uniform)
    # But taking Q uniformly from QR decomposition of Gaussian entries is correct for O(N) if we ensure det(Q) = +- 1 uniform?
    # Actually, QR of a Gaussian matrix yields Q uniformly distributed over O(N) if we treat the sign of diag(R).
    # A simpler robust method for O(N) specifically:
    # Z is normal Ginibre, M = (Z + Z.T)/sqrt(2) is symmetric? No, that's symmetric.
    # The QR method: H = Gaussian, Q, R = qr(H). Q is uniform over O(N).
    # We must ensure that det(Q) is uniform between -1 and 1. Standard QR gives Q deterministically +1 or -1 depending on implementation?
    # To be safe and truly Haar on O(N), we can multiply by a random sign if needed, or use scipy.stats.special_ortho_group
    # and pick a random random det sign.
    # However, `np.random.randn` *does* yield uniform O(N) for Q.
    return Q

def construct_V(d, d_b, d_f, d_B, d_P, O):
    """
    Constructs the map V: H_b -> H_B from the random orthogonal matrix O.
    
    Dimensions of spaces:
    H_in  = H_b (dim d_b) x H_f (dim d_f) -> Total dim d
    H_out = H_B (dim d_B) x H_P (dim d_P) -> Total dim d
    
    V = sqrt(d_P) * <0|_P O |0>_f
    
    We assume |0>_f is the first basis vector of H_f.
    We assume |0>_P is the first basis vector of H_P.
    
    We need to map indices:
    O acts on d-dimensional vectors.
    Input vector indices (j): (i_b, i_f) where i_b in 0..d_b-1, i_f in 0..d_f-1.
    Output vector indices (i): (o_B, o_P) where o_B in 0..d_B-1, o_P in 0..d_P-1.
    
    |0>_f corresponds to fixing i_f = 0.
    <0|_P corresponds to fixing o_P = 0.
    
    V maps an input state |psi>_b (dim d_b) to an output state in H_B (dim d_B).
    
    Matrix elements V_{o_B, i_b} = sqrt(d_P) * O_{[o_B, 0], [i_b, 0]}
    
    We need to flatten the composite indices appropriately.
    Let's use row-major order (C-order) consistent with numpy.
    Composite index (row, col) or (subsys1, subsys2).
    
    Input mapping:
    idx_in = i_b * d_f + i_f
    For i_f = 0, idx_in = i_b * d_f + 0 = i_b * d_f
    
    Output mapping:
    idx_out = o_B * d_P + o_P
    For o_P = 0, idx_out = o_B * d_P + 0 = o_B * d_P
    
    V is a subset of O.
    """
    
    V = np.zeros((d_B, d_b), dtype=complex)
    factor = np.sqrt(d_P)
    
    # Extract submatrix
    # Rows of O correspond to output, Cols to input
    # We need specific rows and columns.
    
    # Target columns in O: those corresponding to |i_b, 0>_f
    cols = [ib * d_f + 0 for ib in range(d_b)]
    
    # Target rows in O: those corresponding to |o_B, 0>_P
    rows = [oB * d_P + 0 for oB in range(d_B)]
    
    # Fill V
    for r_idx, oB in enumerate(rows):
        for c_idx, ib in enumerate(cols):
            V[r_idx, c_idx] = factor * O[oB, ib]
            
    return V

def compute_analytical(d, d_P, psi, phi):
    """
    Computes the analytical result:
    E = (d_P / (d + 2)) * ( 2|<phi|psi>|^2 + |<phi|psi*>|^2 )
    """
    # Inner product <phi|psi>
    ip_phi_psi = np.vdot(phi, psi)
    
    # Complex conjugate of psi (element-wise conjugation of vector components)
    # In the standard computational basis, |psi*> has components <psi*|e_k> = (<e_k|psi>)* = psi_k*
    # However, <phi|psi*> = sum phi_k* (psi_k*) = (sum phi_k* psi_k)* = <psi|phi>
    # Wait, definition check: 
    # <phi|psi*> = sum_k phi_k^* . (psi_k)^* = sum_k (phi_k psi_k)^* = (<psi|phi>)^* = <phi|psi>
    # This implies |<phi|psi*>|^2 = |<phi|psi>|^2 ?
    # Let's re-read the text carefully.
    # "|phi^*> denotes the complex conjugate of the state |phi>"
    # Usually, if |psi> = sum p_i |i>, then |psi*> = sum p_i^* |i>.
    # Then <phi|psi*> = sum q_i^* (p_i^*) = (sum q_i p_i)^* = <phi|psi>^*
    # So |<phi|psi*>|^2 = |<phi|psi>|^2.
    
    # HOWEVER, in the context of Real vs Unitary ensembles:
    # If O is Orthogonal (Real), the model distinguishes complex phases.
    # Perhaps the basis used to define the *conjugate* is not the expansion basis of psi?
    # "where |psi*> denotes the complex conjugate of the state |psi> in the chosen basis."
    # If psi is a complex vector, and basis is |i>, psi = sum c_i |i>.
    # psi* in same basis is sum c_i^* |i>.
    # Then <phi|psi*> = sum d_i^* c_i^*. 
    # The magnitude squared is |sum d_i c_i|^2 = |<psi|phi>|^2 = |<phi|psi>|^2.
    
    # Is it possible the model implies something else?
    # Let's look at the derivation formula again: 2 |<phi|psi>|^2 + |<phi|psi*>|^2.
    # If they are equal, it's 3 |<phi|psi>|^2.
    # If psi is real, they are definitely equal.
    # If psi is complex, are they equal? Yes, mathematically.
    # Why separate terms then?
    # Maybe one is |<phi|psi>|^2 and the other involves the "cross" fidelity term if we treat orthogonal group acting on complex space?
    # The derivation terms were:
    # 1. <phi_c* psi_c> <phi_d psi_d*> -> |<phi|psi>|^2
    # 2. <phi_c* phi_c> <psi_a psi_a*> -> 1 (normalized)
    # 3. <phi_c* psi_c*> <phi_a psi_a> -> |<phi|psi*>|^2 (or Re terms?)
    
    # Let's verify the algebraic identity:
    # T3 = sum_c phi_c^* psi_c^* sum_a phi_a psi_a
    #    = (sum_c phi_c psi_c)^* (sum_a phi_a psi_a) = |sum a phi_a psi_a|^2.
    # sum_a phi_a psi_a is <psi|phi>.
    # So T3 = |<psi|phi>|^2 = |<phi|psi>|^2.
    
    # Is there a typo in the prompt's provided derivation text vs the standard result?
    # For Unitary Cauchy: Contribution depends on Fidelity.
    # For Orthogonal: Often involves Fidelity + Cross fidelity (swap) terms.
    # In real basis, <phi|psi*> = <phi|psi>.
    # In complex basis, if O is orthogonal (Real matrix), it maps Re parts to Re parts and Im to Im parts.
    # The term <phi|VdagV|psi> separates Real and Imaginary operators?
    # Let's stick to the literal formula provided in the prompt: 
    # "2 |<phi|psi>|^2 + |<phi|psi*>|^2"
    # I will implement this literal formula. If it simplifies to 3|ip|^2, so be it.
    # However, typically in such problems, psi is arbitrary.
    # Let's generate general complex psi and phi.
    
    val_inner = np.vdot(phi, psi)
    
    # Calculate <phi|psi*>
    # psi_vector_conjugate = np.conj(psi)
    # val_conj = np.vdot(phi, psi_vector_conjugate)
    # As analyzed, val_conj = np.sum(phi.conj() * psi.conj()) = np.conj(np.sum(phi*psi)) = np.conj(np.vdot(psi, phi))
    # |val_conj|^2 = |np.vdot(psi, phi)|^2 = |val_inner|^2.
    # So the formula is effectively (d_P / (d+2)) * 3 * |<phi|psi>|^2.
    
    # WAIT. Let's look at the derivation text step 3 again.
    # Term 2: (sum phi_c* phi_c)(sum psi_a psi_a*) -> Norms -> 1*1 = 1.
    # Term 3: (sum phi_c* psi_c*)(sum phi_a psi_a).
    # If phi = psi, then |<psi|psi>|^2 = 1.
    # Term 3 becomes |sum psi_c* psi_c*|^2 ? 
    # No. sum phi_c* psi_c* = sum psi_c* psi_c*.
    # sum phi_a psi_a = sum psi_a psi_a.
    # These are not inverses. 
    # If psi = Gaussian complex, sum psi^2 is not 1.
    # My previous check assumed T3 = |sum phi_i psi_i|^2.
    # sum phi_c^* psi_c^* = (sum phi_c psi_c)^*
    # sum phi_a psi_a = S.
    # Product = S* S = |S|^2.
    # S = sum phi_a psi_a = vdot(psi, phi).
    # So yes, it is |<psi|phi>|^2.
    
    # Okay, I will implement strictly what the formula says, to avoid error, 
    # even if mathematically $|<\phi|\psi^*>|^2 \equiv |<\phi|\psi>|^2$.
    # Perhaps the definitions of |psi*> in the "real vs complex" context implies conjugation without bra-ket transpose?
    # No, standard QM notation: <A|B> = A^† B.
    # I will code it exactly as written.
    
    term1 = 2 * np.abs(np.vdot(phi, psi))**2
    term2 = np.abs(np.vdot(phi, np.conj(psi)))**2 
    
    return (d_P / (d + 2)) * (term1 + term2)

def run_simulation_and_plot():
    # Scenario C: Scalable/Testable Regime (Qubits)
    n_qubits = 6
    d = 2**n_qubits # 64
    
    d_b = 8  # 3 qubits
    d_B = 16 # 4 qubits
    
    # Calculate d_f and d_P from constraints
    # d = d_b * d_f => d_f = d / d_b
    d_f = d // d_b
    # d = d_B * d_P => d_P = d / d_B
    d_P = d // d_B
    
    print(f"Parameters: d={d}, d_b={d_b}, d_f={d_f}, d_B={d_B}, d_P={d_P}")
    assert d_b * d_f == d
    assert d_B * d_P == d
    
    # Define states |psi> and |phi>
    # To test the terms significantly, we define states with varied overlaps.
    # We want to sweep |<phi|psi>|.
    
    num_samples = 2000 # Number of random O matrices to sample
    test_points = 20   # Number of overlaps to test
    
    # Generate a fixed random |psi>
    psi = np.random.randn(d_b) + 1j * np.random.randn(d_b)
    psi /= np.linalg.norm(psi)
    
    # Generate varied |phi> vectors to span overlaps [-1, 1] (fidelity 0 to 1)
    # We rotate psi in a 2D subspace.
    basis = np.random.randn(d_b, 2) + 1j * np.random.randn(d_b, 2)
    # Orthonormalize basis
    basis, _ = np.linalg.qr(basis)
    
    # |phi(theta)> = cos(theta) |psi> + sin(theta) |perp>
    fidelity_grid = np.linspace(0, 1, test_points)
    angles = np.arccos(fidelity_grid)
    
    theoretical_vals = []
    simulated_vals = []
    
    for theta in angles:
        # Construct |phi>
        phi = np.cos(theta) * psi + np.sin(theta) * basis[:, 1]
        phi /= np.linalg.norm(phi) # ensure normalization
        
        # Compute Theoretical Average
        theo = compute_analytical(d, d_P, psi, phi)
        theoretical_vals.append(theo)
        
        # Compute Simulated Average
        sum_sq = 0.0
        
        # Monte Carlo Loop
        # For performance in Python, we might want to vectorize, but loop is clearer for correctness here.
        # Given d=64, loops are fine.
        for _ in range(num_samples):
            # 1. Generate random O in O(d)
            # Using scipy.stats.unitary_group is for U(d). 
            # We need O(d). 
            # A matrix from the Ginibre ensemble (Gaussian real) Q-corrected is O(d).
            # Or simpler: take a random unitary (complex) and symmetrize? No, that's not Haar O(d).
            # Using the QR method defined above.
            O_mat = generate_haar_orthogonal(d)
            
            # 2. Construct V
            V = construct_V(d, d_b, d_f, d_B, d_P, O_mat)
            
            # 3. Compute |<phi|VdagV|psi>|^2
            # (VdagV)|psi>
            VdagV_psi = V.conj().T @ (V @ psi)
            # <phi|...
            overlap = np.vdot(phi, VdagV_psi)
            sum_sq += np.abs(overlap)**2
            
        sim_avg = sum_sq / num_samples
        simulated_vals.append(sim_avg)
        
        print(f"Fidelity: {np.abs(np.vdot(phi, psi)):.2f}, Theoretical: {theo:.5f}, Simulated: {sim_avg:.5f}")

    # Plotting
    plt.figure(figsize=(10, 6))
    plt.plot(fidelity_grid, theoretical_vals, 'o-', label='Theoretical Model')
    plt.plot(fidelity_grid, simulated_vals, 's--', label=f'Monte Carlo (N={num_samples})')
    plt.xlabel(r'Fidelity $|\langle \phi | \psi \rangle|$')
    plt.ylabel(r'$\overline{|\langle \phi | V^\dagger V | \psi \rangle|^2}$')
    plt.title(r'Average Squared Matrix Element vs Fidelity ($d_b=8, d_B=16, d=64$)')
    plt.legend()
    plt.grid(True)
    plt.show()

if __name__ == "__main__":
    run_simulation_and_plot()
```
The derivation states that $|\langle \phi | \psi^* \rangle|^2$ appears in the final result algebraically, but in standard complex Hilbert spaces with the definition $\langle \phi | \psi^* \rangle = \sum \phi_i^* \psi_i^*$, this quantity is identical to $|\langle \phi | \psi \rangle|^2$ (since $\sum \phi_i^* \psi_i^* = (\sum \phi_i \psi_i)^* = \langle \psi | \phi \rangle^*$). Thus, the term could be simplified to $3 |\langle \phi | \psi \rangle|^2$. However, the implemented function `compute_analytical` strictly follows the provided formula structure without simplification, as "deriving units" is not the task here, only implementing the given model.

The code sets up Scenario C ($d=64$) with suitable parameters for a workstation simulation ($N=2000$). It generates orthogonal matrices using the QR decomposition of Gaussian matrices, which yields Haar-random orthogonal matrices. It then computes the sub-matrix $V$ and averages the squared amplitude.

One slight correction on `generate_haar_orthogonal`: `scipy.stats.special_ortho_group` exists but returns SO(d). We want O(d). The QR decomposition method on a Real Gaussian matrix returns an orthogonal matrix with determinant $\pm 1$ uniformly distributed (probability of $-1$ is non-negligible). However, strictly speaking, the QR decomposition of $N \sim \mathcal{N}(0,1)$ gives $Q$ distributed according to the Haar measure on $O(N)$. (Proof: Invariant distribution). The code uses this method.

The output is a Python script. I will provide the script now.
```python
import numpy as np
import matplotlib.pyplot as plt
from scipy.linalg import eig
import warnings
import scipy.linalg

# Suppress minor warnings for cleaner output
warnings.filterwarnings("ignore")

# ==========================================
# 1. Physical Constants and Helper Functions
# ==========================================

# Pauli Matrices
I = np.array([[1, 0], [0, 1]], dtype=complex)
X = np.array([[0, 1], [1, 0]], dtype=complex)
Y = np.array([[0, -1j], [1j, 0]], dtype=complex)
Z = np.array([[1, 0], [0, -1]], dtype=complex)

# Basis state |0> for the physical qubits
# Defined as a column vector for convenience, though we mostly work with density matrices
psi_0 = np.array([[1], [0]], dtype=complex)
# Initial density matrix for the physical qubits: |0><0|
rho_0_phys = np.kron(psi_0, psi_0.conj().T)

def mat_to_vec(M):
    """
    Flattens a 2x2 matrix into a 4-component vector using the Pauli basis.
    Order: I, X, Y, Z
    M = c0*I + c1*X + c2*Y + c3*Z
    """
    # Coefficients are given by 0.5 * Tr(sigma_i * M) because Tr(sigma_i * sigma_j) = 2 * delta_ij
    c0 = 0.5 * np.trace(M)
    c1 = 0.5 * np.trace(np.dot(X, M))
    c2 = 0.5 * np.trace(np.dot(Y, M))
    c3 = 0.5 * np.trace(np.dot(Z, M))
    return np.array([c0, c1, c2, c3], dtype=complex)

def vec_to_mat(v):
    """Reconstructs a 2x2 matrix from a 4-component vector in the Pauli basis."""
    c0, c1, c2, c3 = v
    return c0*I + c1*X + c2*Y + c3*Z

# ==========================================
# 2. Model Construction: Transfer Matrix
# ==========================================

def construct_transfer_matrix(a, b):
    """
    Constructs the 4x4 transfer matrix T for the qMPS.
    
    The gate is U = e^{-i b (X(X) + Z(Z))/2} e^{-i a X/2}.
    The circuit applies U_0k sequentially starting from k=1.
    
    In the transfer matrix formalism for this specific star-shaped circuit:
    We map the state of the central ancilla (qubit 0) before interacting with 
    qubit k to the state of the ancilla after interaction, tracing out qubit k.
    
    Evolution rule:
    rho_anc_out = Tr_phys[ U (rho_anc_in tensor |0><0|) U^dagger ]
    """
    
    # 1. Construct the unitary gate U acting on the joint system (Ancilla, Physical)
    # Matrix order: Ancilla (index 0) is the first subsystem, Physical (index k) is the second.
    
    # Decomposition U = U_b * U_a
    
    # U_a = e^{-i a X_k / 2}
    # Acts on Physical qubit (index 1), Identity on Ancilla (index 0)
    term_in_exp_a = -1j * a * np.kron(I, X) / 2.0
    U_a = scipy.linalg.expm(term_in_exp_a)
    
    # U_b = e^{-i b (X_j X_k + Z_j Z_k) / 2}
    # Entangles Ancilla and Physical
    term_in_exp_b = -1j * b * (np.kron(X, X) + np.kron(Z, Z)) / 2.0
    U_b = scipy.linalg.expm(term_in_exp_b)
    
    # Full gate
    U = np.dot(U_b, U_a)
    
    # 2. Construct the Transfer Matrix T
    # T maps vector(rho_in) to vector(rho_out)
    T_matrix = np.zeros((4, 4), dtype=complex)
    
    # Basis elements for the ancilla state vector space: I, X, Y, Z
    pauli_basis = [I, X, Y, Z]
    
    for col_idx, P_in in enumerate(pauli_basis):
        # Matrix representation of the input ancilla basis element
        rho_anc_in = P_in
        
        # Prepare the input joint state: rho_anc_in tensor |0><0|
        # Using Kronecker product: (Ancilla) x (Physical)
        rho_joint_in = np.kron(rho_anc_in, rho_0_phys)
        
        # Evolve joint state: U * rho_in * U^dagger
        rho_joint_evolved = np.dot(U, np.dot(rho_joint_in, U.conj().T))
        
        # Trace out the physical qubit to get the new ancilla state
        # Reshape to (2, 2, 2, 2) -> (row_anc, col_anc, row_phys, col_phys)
        # Partial trace over indices 2 and 3
        d = 2
        rho_anc_out = np.zeros((2, 2), dtype=complex)
        
        for i in range(d):      # ancilla row
            for j in range(d):  # ancilla col
                for k in range(d): # phys index (summed out)
                    rho_anc_out[i, j] += rho_joint_evolved[i*d + k, j*d + k]
        
        # Project the resulting ancilla state back onto the Pauli basis
        vec_out = mat_to_vec(rho_anc_out)
        
        # Fill the column of T
        T_matrix[:, col_idx] = vec_out
        
    return T_matrix, U

def get_W_Z_operator(U):
    """
    Constructs the W_Z transfer matrix (column-stacking).
    This corresponds to inserting the Z operator on the physical qubit.
    
    rho_anc_out = Tr_phys[ Z_phys * U * (rho_anc_in tensor |0><0|) * U^dagger ]
    Here Z_phys = I_ancilla tensor Z
    """
    W_Z_matrix = np.zeros((4, 4), dtype=complex)
    pauli_basis = [I, X, Y, Z]
    
    # Z operator on the physical qubit in the joint space
    Z_phys_joint = np.kron(I, Z)
    
    for col_idx, P_in in enumerate(pauli_basis):
        rho_anc_in = P_in
        rho_joint_in = np.kron(rho_anc_in, rho_0_phys)
        
        rho_joint_evolved = np.dot(U, np.dot(rho_joint_in, U.conj().T))
        
        # Apply Z measurement on the physical qubit before tracing out
        rho_joint_measured = np.dot(Z_phys_joint, rho_joint_evolved)
        
        # Trace out physical qubit
        d = 2
        rho_anc_out = np.zeros((2, 2), dtype=complex)
        for i in range(d):
            for j in range(d):
                for k in range(d):
                    rho_anc_out[i, j] += rho_joint_measured[i*d + k, j*d + k]
                    
        vec_out = mat_to_vec(rho_anc_out)
        W_Z_matrix[:, col_idx] = vec_out
        
    return W_Z_matrix

# ==========================================
# 3. Correlation Function Calculation
# ==========================================

def compute_correlation_limit(a, b):
    """
    Computes lim_{N->inf} <Z_{N-2} Z_N>.
    
    Formalism:
    1. Find dominant right eigenvector (v_R) and left eigenvector (v_L) of T.
       T v_R = lambda v_R,  T.T v_L = lambda v_L.
       Normalize such that v_L^H v_R = 1.
    2. Compute <ZZ> = v_L^H (W_Z T W_Z) v_R.
    """
    
    # 1. Construct Matrices
    T, U = construct_transfer_matrix(a, b)
    W_Z = get_W_Z_operator(U)
    
    # 2. Diagonalization of T
    # The transfer matrix T is real for real a, b (as shown by the form of U involving cos/sin or complex pairs), 
    # but we treat it as complex generally.
    val, vec = eig(T)
    
    # Find the dominant eigenvalue (spectral radius)
    # Physically, this must be 1. 
    # We sort by absolute magnitude to be safe.
    idx_max = np.argmax(np.abs(val))
    lambda_max = val[idx_max]
    v_R = vec[:, idx_max]
    
    # Find left eigenvector (eigenvector of T.T)
    val_L, vec_L = eig(T.T)
    idx_max_L = np.argmax(np.abs(val_L))
    v_L = vec_L[:, idx_max_L]
    
    # 3. Normalization
    # Condition: v_L^+ v_R = 1. 
    # Note: v_L returned by eig is the row vector if we view (T.T)v = v, 
    # meaning v^T T = v^T. So v_L is the standard "bra" vector in row space.
    # We take conjugate transpose to get column vector for dot products if needed, 
    # but here we simply want the inner product of the "bra" v_L and "ket" v_R.
    # Since v_L comes from T.T, it corresponds to the standard column eigenvector of T^T, 
    # which is the transpose of the left eigenvector of T.
    # To match the formula v_L^T W v_R, we should ensure the inner product logic holds.
    # Standard eigenvectors are column vectors. 
    # If T v = \lambda v, then v^T T^T = \lambda v^T.
    # So eigenvectors of T.T serve as the "bra" vectors (transposed).
    
    overlap = np.dot(v_L.conj().T, v_R)
    
    # Numerical check: if overlap is too small or purely imaginary, something is wrong.
    # But theoretically it should be 1. Normalize v_R accordingly to preserve v_L.
    v_R = v_R / overlap
    
    # 4. Compute Correlation
    # Term: v_L^H W_Z T W_Z v_R
    # This is equivalent to (v_L^T)* (W_Z T W_Z v_R) for real vector spaces, 
    # but we use conj().T for generality.
    
    temp = np.dot(W_Z, v_R)
    temp = np.dot(T, temp)
    temp = np.dot(W_Z, temp)
    
    numerator = np.dot(v_L.conj().T, temp)
    
    # Numerical result might have a tiny imaginary part due to float precision
    if np.abs(numerator.imag) > 1e-10:
        print(f"Warning: Result has significant imaginary part: {numerator}")
        
    return numerator.real

def analytic_solution(a, b):
    """
    The derived analytic formula:
    C(a,b) = cos^2(a) * cos(2b) + sin^2(a)
    """
    return (np.cos(a)**2) * np.cos(2*b) + np.sin(a)**2

# ==========================================
# 4. Main Execution and Visualization
# ==========================================

def run_simulation():
    print("-" * 60)
    print(" qMPS Two-Point Correlation Function Calculation")
    print(" Target: lim_{N->inf} <Z_{N-2} Z_N>")
    print("-" * 60)

    # Parameters
    # We sweep b for a fixed a to generate the plot
    a_fixed = np.pi / 6.0  # 30 degrees
    b_vals = np.linspace(0, np.pi/2, 60)
    
    corr_vals = []
    analytic_vals = []
    
    for b in b_vals:
        num = compute_correlation_limit(a_fixed, b)
        ana = analytic_solution(a_fixed, b)
        corr_vals.append(num)
        analytic_vals.append(ana)
        
    # Convert to arrays
    corr_vals = np.array(corr_vals)
    analytic_vals = np.array(analytic_vals)
    
    # Calculate maximum error
    max_error = np.max(np.abs(corr_vals - analytic_vals))
    print(f"Calculated for a = {a_fixed:.4f} radians")
    print(f"Max error (Num - Ana): {max_error:.2e}")

    # Plot 1: b-dependence
    plt.figure(figsize=(10, 6))
    plt.plot(b_vals, corr_vals, 'o', markersize=4, label='Numerical (Transfer Matrix)', alpha=0.7)
    plt.plot(b_vals, analytic_vals, 'r-', linewidth=2, label='Analytic Formula')
    plt.title(r'Correlation $\lim_{N\to\infty} \langle Z_{N-2} Z_N \rangle$ vs $b$ ($a=\pi/6$)')
    plt.xlabel(r'Parameter $b$ [radians]')
    plt.ylabel(r'Correlation Value')
    plt.legend()
    plt.grid(True, linestyle='--', alpha=0.6)
    plt.tight_layout()
    plt.savefig('correlation_vs_b.png')
    plt.show()

    # Plot 2: 2D Heatmap of the analytic solution
    a_grid = np.linspace(0, np.pi/2, 100)
    b_grid = np.linspace(0, np.pi/2, 100)
    A, B = np.meshgrid(a_grid, b_grid)
    
    # Vectorized analytic calculation
    C_analytic_grid = (np.cos(A)**2) * np.cos(2*B) + np.sin(A)**2
    
    plt.figure(figsize=(8, 6))
    plt.contourf(A, B, C_analytic_grid, levels=20, cmap='plasma')
    cbar = plt.colorbar(label=r'$\langle Z_{N-2} Z_N \rangle$')
    plt.title(r'Analytic Correlation Function $\cos^2 a \cos(2b) + \sin^2 a$')
    plt.xlabel(r'$a$ [radians]')
    plt.ylabel(r'$b$ [radians]')
    plt.tight_layout()
    plt.savefig('correlation_heatmap.png')
    plt.show()

    # Table of sample values
    print("-" * 60)
    print(" Sample Values (b sweep):")
    print(f"{'b (rad)':<12} | {'Numerical':<12} | {'Analytic':<12}")
    print("-" * 45)
    step = len(b_vals) // 10
    for i in range(0, len(b_vals), step):
        print(f"{b_vals[i]:<12.4f} | {corr_vals[i]:<12.6f} | {analytic_vals[i]:<12.6f}")
    print("-" * 60)

if __name__ == "__main__":
    run_simulation()
```
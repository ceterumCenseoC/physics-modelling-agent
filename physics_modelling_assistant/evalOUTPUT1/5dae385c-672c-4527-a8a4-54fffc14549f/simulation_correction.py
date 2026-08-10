```python
import numpy as np
import matplotlib.pyplot as plt

# ==========================================
# 1. Model Definition and Parameters
# ==========================================

# System Configuration
NUM_ROWS = 3         # n in the problem statement
NUM_COLS = 4         # Fixed at 4
DIM_N = 2            # Dimension of single qubit space
TOTAL_DIM = 2**(NUM_ROWS * NUM_COLS)

# Precision
PRINT_PRECISION = 6

print(f"Quantum Trace Simulation")
print(f"System: {NUM_ROWS} rows x {NUM_COLS} columns")
print(f"Total Hilbert Space Dimension: {TOTAL_DIM}")

# ==========================================
# 2. Operator Construction
# ==========================================

def get_psi_ghz(n):
    """
    Constructs the density operator psi for the n-qubit GHZ state.
    |psi> = 1/sqrt(2) (|0>^n + |1>^n)
    psi = |psi><psi|
    """
    psi_0 = np.array([1, 0], dtype=complex)
    psi_1 = np.array([0, 1], dtype=complex)
    
    # Create product states |0...0> and |1...1>
    state_0 = np.array([1.0 + 0j])
    state_1 = np.array([1.0 + 0j])
    for _ in range(n):
        state_0 = np.kron(state_0, psi_0)
        state_1 = np.kron(state_1, psi_1)
        
    # GHZ State Vector
    state_ghz = (state_0 + state_1) / np.sqrt(2)
    
    # Density Matrix
    rho = np.outer(state_ghz, state_ghz)
    return rho

def compute_N_analytical():
    """
    Computes the 4-qubit operator N using the derived analytical values.
    N = Integral( U^4 (S+S) U^4 )
    """
    dim = 2**4
    N = np.zeros((dim, dim), dtype=complex)
    
    # Map index to basis string (e.g., 0 -> 0000, 15 -> 1111)
    for i in range(dim):
        binary_str = format(i, '04b')
        
        # Logic derived from the "Summation over Computational Basis" section
        # We check weights of (first 2) and (last 2) qubits
        
        # Weight of first 2 qubits
        w1 = int(binary_str[0]) + int(binary_str[1])
        # Weight of last 2 qubits
        w2 = int(binary_str[2]) + int(binary_str[3])
        
        val = 0.0
        if w1 == 0 and w2 == 0: # 0000
            val = 7.0/15.0
        elif w1 == 2 and w2 == 2: # 1111
            val = 7.0/15.0
        elif w1 == 1 and w2 == 1:
            # Check parity for mixed weights
            # 0101 or 1010 -> 2/15
            # 0110 or 1001 -> 13/15
            if binary_str in ['0101', '1010']:
                val = 2.0/15.0
            else:
                val = 13.0/15.0
        else:
            # All other mixed parity pairings
            val = 13.0/15.0
            
        N[i, i] = val
        
    return N

# ==========================================
# 3. Main Computation
# ==========================================

# Step 1: Construct Operators
print("\nConstructing Operators...")

# A. Operator N (acts on 1 row of 4 qubits)
N_row = compute_N_analytical()

# B. Operator N^{otimes n} (acts on n rows of 4 qubits)
# Since N is diagonal in the computational basis, we can compute the tensor product
# efficiently by only tracking the diagonal elements.
# N_tensor_ii = prod_k N_row_i_k_i_k
diag_N_row = np.diag(N_row).reshape(1, -1)
# Kronecker product of vectors corresponds to the tensor product of diagonal matrices
diag_N_tensor = np.ones(1)
for _ in range(NUM_ROWS):
    diag_N_tensor = np.kron(diag_N_tensor, diag_N_row)
    
# To reconstruct the full matrix (if needed for trace) we could use np.diag,
# but since we just need the trace tr(N * psi), and psi is a projector,
# we essentially compute sum_i N_tensor_ii * psi_tensor_ii.

# C. Operator psi (acts on n qubits of a column)
psi_col = get_psi_ghz(NUM_ROWS)
diag_psi_col = np.diag(psi_col).reshape(1, -1)

# D. Operator psi^{otimes 4} (acts on 4 columns of n qubits each)
diag_psi_tensor = np.ones(1)
for _ in range(NUM_COLS):
    diag_psi_tensor = np.kron(diag_psi_tensor, diag_psi_col)

# Compute Trace using the diagonal property of both matrices
# Trace(A * B) = sum_i A_ii * B_ii if both are diagonal.
# N is diagonal. Psi is a pure GHZ state, which is NOT diagonal in the computational basis
# of the whole system. 
# However, N acts on the Row structure (4 qubits per row), while Psi acts on the Column structure
# (n qubits per column).
# The term N_tensor acts on indices corresponding to rows, Psi_tensor acts on indices 
# corresponding to columns.
#
# Trace definition:
# Tr(N \otimes psi) is actually Tr( (N_1 \otimes ... \otimes N_n) (psi^{(1)} \otimes ... \otimes psi^{(4)}) )
#
# Let's verify the dimensions and calculations.
# N_tensor: Shape (16^n, 16^n). Diagonal entries are products of 4-qubit N diagonal entries.
# psi_tensor: Shape (2^n, 2^n). Diagonal entries are products of 1-qubit GHZ diagonal entries?
# Wait. get_psi_ghz(n) returns a density matrix of size 2^n x 2^n.
# Its diagonal elements are:
# |psi> = (1/sqrt(2)) (|0..0> + |1..1>)
# |psi><psi| has non-zero elements only at corners (|0..0><0..0|, |0..0><1..1|, etc).
# Diagonal elements: <0..0|psi><psi|0..0> = 1/2. <1..1|...> = 1/2. All others 0.
# So psi_col is NOT diagonal.
#
# However, trace of product of two matrices is not generally sum of products of diagonals.
# But we have the identity:
# Tr(A B) = sum_{i,j} A_{ij} B_{ji}.
#
# Let's re-read the theoretical derivation.
# "The trace can be expanded in the computational basis... \sum <...| N |...>"
# This calculates Tr(N * psi^{otimes 4}).
#
# Operationally:
# N_tensor is diagonal in the basis |a1 b1 c1 d1 ... an bn cn dn>.
# psi_tensor is diagonal in the basis |\vec{a}\vec{b}\vec{c}\vec{d}> = |a1...an>|b1...bn>|c1...cn>|d1...dn>.
# These are the SAME basis if we order subsystems correctly.
# The code orders subsystems as:
# Row 1 (q1..q4), Row 2 (q1..q4), ...
# N_row acts on (q1, q2, q3, q4) of a specific row.
# N_tensor = N_row_1 kron N_row_2 ...
#
# psi_tensor construction:
# psi_col acts on (Row1_q1, Row2_q1, ..., RowN_q1). Let's call this "Column 1".
# psi_tensor = psi_col_1 kron psi_col_2 ... psi_col_4.
#
# Trace calculation in code:
# N_tensor is diagonal in the basis [r0_q0, r0_q1, r0_q2, r0_q3, r1_q0, ...]
# psi_tensor is diagonal in the basis [r0_q0, r1_q0, ..., r0_q1, r1_q1, ...]
#
# These basis orderings are DIFFERENT.
# Trace(A @ B) is basis independent.
# However, the "sum of diagonal products" optimization only works if A and B are BOTH 
# diagonal in the SAME basis.
# N is diagonal in the Row-basis. Psi is diagonal in the Column-basis.
# THUS, we cannot simply do sum(diag_N * diag_psi).
#
# We must use matrix multiplication or explicit sum over basis.
# Given the size (2^12 = 4096), standard dot product is fast enough and safer than 
# handling basis permutations manually for a "check the code" task.

# Re-constructing full matrices for safety and correctness of trace calculation
print(f"Constructing N^{{\otimes {NUM_ROWS}}} (Full Matrix)...")
N_tensor_full = np.array([[1.0 + 0j]])
for _ in range(NUM_ROWS):
    N_tensor_full = np.kron(N_tensor_full, N_row)

print(f"Constructing psi^{{\otimes 4}} (Full Matrix)...")
psi_tensor_full = np.array([[1.0 + 0j]])
for _ in range(NUM_COLS):
    psi_tensor_full = np.kron(psi_tensor_full, psi_col)

print("Computing Trace tr(N * psi)...")
# Operator Product M = N * psi
M_prod = np.dot(N_tensor_full, psi_tensor_full)

# Calculation of Trace
trace_val = np.trace(M_prod)

# ==========================================
# 4. Results and Visualization
# ==========================================

# Expected analytical value
# Formula: (1/16) * [ 2*(7/15)^n + 2*(2/15)^n + 12*(13/15)^n ]
term1 = 2 * (7.0/15.0)**NUM_ROWS
term2 = 2 * (2.0/15.0)**NUM_ROWS
term3 = 12 * (13.0/15.0)**NUM_ROWS
analytical_val = (term1 + term2 + term3) / 16.0

print("\n" + "="*40)
print(f"Computation Results for n={NUM_ROWS}")
print("="*40)
print(f"Numerical Trace: {trace_val:.{PRINT_PRECISION}f}")
print(f"Analytical Trace: {analytical_val:.{PRINT_PRECISION}f}")
print(f"Difference: {abs(trace_val - analytical_val):.2e}")
print(f"Exact Fraction: 4511/9000 (approx 0.501222...)")
print("="*40)

# ==========================================
# 5. Graphics
# ==========================================

# We want to verify the convergence or behavior of the trace with respect to n.
# However, since the problem asks specifically for n=3 in the code,
# we will visualize the Diagonal elements of N to show the structure
# derived in the "Dimensional Analysis".

fig, ax = plt.subplots(figsize=(10, 4))

# Diagonal elements of N (16 values for the 4-qubit row space)
diag_N = np.real(np.diag(N_row))
x_axis = np.arange(16)

ax.bar(x_axis, diag_N, color='skyblue', alpha=0.8)
ax.set_xlabel('Basis State Index (0-15)', fontsize=12)
ax.set_ylabel(r'Diagonal Element Value $\langle \sigma | N | \sigma \rangle$', fontsize=12)
ax.set_title(r'Diagonal Elements of Operator $N$ (4-qubit row space)', fontsize=14)
ax.set_xticks(x_axis)

# Annotate the specific values derived
# 7/15 approx 0.466, 2/15 approx 0.133, 13/15 approx 0.866
for i, v in enumerate(diag_N):
    if abs(v - 7/15) < 1e-9:
        color = 'red'
        label = "7/15"
    elif abs(v - 2/15) < 1e-9:
        color = 'green'
        label = "2/15"
    else:
        color = 'blue'
        label = "13/15"
    
    ax.text(i, v + 0.02, label, ha='center', fontsize=9, color=color, fontweight='bold')

plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.tight_layout()

# Save the figure
plt.savefig('trace_results_graphic.png')
print("\nGraphics generated: trace_results_graphic.png")

# Show the plot (if in an interactive environment, otherwise just saved)
plt.show()
```
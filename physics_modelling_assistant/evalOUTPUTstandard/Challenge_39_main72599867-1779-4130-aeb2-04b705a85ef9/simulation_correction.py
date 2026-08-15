
```python
import numpy as np
import matplotlib.pyplot as plt
from scipy.sparse import csr_matrix, eye, kron, diags
from scipy.linalg import expm

# ==========================================
# 1. System Configuration and Parameters
# ==========================================

# Physical parameters
# g: Coupling strength (kHz)
# gamma: Decay rate to dark state (kHz)
# alpha_val: Coherent state amplitude (complex)
g = 2 * np.pi * 10.0
gamma = 2 * np.pi * 10.0
alpha_val = 2.0 + 0j 

# Simulation constraints
# max_n: Truncation limit for Fock space. 
# We choose a cutoff large enough to capture the coherent state tail.
max_n = 50

# ==========================================
# 2. Operator Construction
# ==========================================

def create_operators(max_n):
    """
    Constructs the creation (a_dag), annihilation (a), and 
    identity operators for the cavity field.
    """
    # Annihilation operator a: |n-1><n| * sqrt(n)
    a_data = np.sqrt(np.arange(1, max_n))
    a_rows = np.arange(max_n - 1)
    a_cols = np.arange(1, max_n)
    
    a = csr_matrix((a_data, (a_rows, a_cols)), shape=(max_n, max_n))
    
    # Creation operator a_dag (Hermitian conjugate of a)
    a_dag = a.conj().T
    
    # Identity operator
    I_cav = eye(max_n, format='csr', dtype=complex)
    
    return a, a_dag, I_cav

# Create cavity operators
a, a_dag, I_cav = create_operators(max_n)

# Define Atomic Basis
# |b> = [1, 0, 0], |d> = [0, 1, 0], |e> = [0, 0, 1]
proj_b = np.array([[1, 0, 0], [0, 0, 0], [0, 0, 0]])
proj_e = np.array([[0, 0, 0], [0, 0, 0], [0, 0, 1]])
proj_d = np.array([[0, 0, 0], [0, 1, 0], [0, 0, 0]])

# Atomic projectors and raising/lowering operators
# sigma_be = |b><e|
sigma_be = np.zeros((3, 3), dtype=complex)
sigma_be[0, 2] = 1.0
# sigma_eb = |e><b|
sigma_eb = sigma_be.conj().T
# Jump operator |d><e|
sigma_de = np.zeros((3, 3), dtype=complex)
sigma_de[1, 2] = 1.0

# Identity for atomic space
I_atom = np.eye(3, dtype=complex)

# ==========================================
# 3. Liouvillian Superoperator Construction
# ==========================================

# Hamiltonian: H = (g/2) * (|b><e| a_dag + |e><b| a)
H_atom_cavity = (g / 2.0) * (
    csr_matrix(np.kron(sigma_be, a_dag)) + 
    csr_matrix(np.kron(sigma_eb, a))
)

# Jump Operator: J = sqrt(gamma) |d><e| (x) Identity_cavity
# Note: J acts on atom, leaves cavity state unchanged
J = csr_matrix(np.sqrt(gamma) * np.kron(sigma_de, I_cav))

# Superoperator Formalism
# We vectorize the density matrix: rho_vec = vec(rho)
# The Lindblad equation d_rho/dt = L * rho_vec is implemented as:
# L = -1j * (I_kron_H - H_T_kron_I) + D_jump

dim_total = 3 * max_n
I_total = eye(dim_total, format='csr', dtype=complex)

# Hamiltonian Superoperator: -i [H, .]
# vec(H * rho * I) -> I_kron_H
# vec(I * rho * H) -> H_T_kron_I
L_H = -1j * (kron(I_total, H_atom_cavity) - kron(H_atom_cavity.transpose(), I_total))

# Dissipator Superoperator: D(rho) = J rho J_dag - 0.5 {J_dag J, rho}
# J_dag_J calculation
J_dag_J = J.conj().T @ J

# J rho J_dag term
L_pre = kron(J.transpose(), J)
# -0.5 * J_dag J rho term
L_decay = -0.5 * kron(J_dag_J.transpose(), I_total)
# -0.5 * rho J_dag J term
L_decay_back = -0.5 * kron(I_total, J_dag_J)

L_D = L_pre + L_decay + L_decay_back

# Total Liouvillian
L = L_H + L_D

# ==========================================
# 4. Initial State Preparation
# ==========================================

# Construct coherent state |alpha>
# |alpha> = exp(-|alpha|^2/2) * sum_{n=0} (alpha^n / sqrt(n!)) |n>
n_range = np.arange(max_n)
coeffs = np.exp(-0.5 * np.abs(alpha_val)**2) * \
         (alpha_val**n_range) / np.sqrt(np.vectorize(np.math.factorial)(n_range))
# Ensure column vector
psi_alpha = coeffs.reshape(-1, 1)

# Cavity density matrix: rho_c = |alpha><alpha|
rho_c = psi_alpha @ psi_alpha.conj().T

# Atomic density matrix: rho_a = |b><b|
rho_a = proj_b

# Total density matrix: rho_0 = rho_a (x) rho_c
rho_0_flat = np.kron(rho_a, rho_c)
# Convert to sparse matrix for efficient operations
rho_0_csr = csr_matrix(rho_0_flat, dtype=complex)

# ==========================================
# 5. Time Evolution to Steady State
# ==========================================

print("Initializing evolution to steady state...")

# To find the steady state, we can either find the kernel of L 
# (eigenvalue 0) or evolve forward in time.
# Evolution is generally robust for open quantum systems that are ergodic.
# We use the matrix exponential method for time evolution.

# Time scaling: The system should reach steady state within a few lifetimes 1/gamma.
t_final = 10.0 / gamma 
# We perform one large step or several smaller steps. One large step with expm is precise enough 
# if the matrix L is well-behaved (no Eigenvalues with positive real parts).
# Since we are interested in the final state, we can map rho(t) -> exp(L*t) rho(0).
# Note: scipy.sparse.linalg.expm is efficient.

evolution_operator_matrix = expm(L * t_final)

# Vectorize initial state
rho_vec_0 = rho_0_csr.reshape(-1, 1)

# Evolve
rho_vec_final = evolution_operator_matrix @ rho_vec_0

# Reshape back to density matrix (3, max_n, 3, max_n)
# reshape order is 'C' (row-major) by default, matching numpy flatten
rho_ss = np.array(rho_vec_final.todense()).reshape(3, max_n, 3, max_n)

# ==========================================
# 6. Extracting Cavity Coherences
# ==========================================

# Reduced density matrix of the cavity: rho_c = Tr_atom(rho_ss)
# rho_c_{mn} = sum_{k=0}^{2} <k, m| rho_ss |k, n>
rho_c_ss = np.zeros((max_n, max_n), dtype=complex)

for k in range(3): # Trace over atomic basis |b>, |d>, |e>
    rho_c_ss += rho_ss[k, :, k, :]

# The coherences in the Fock basis are simply the elements of this matrix
# C_nn' = <n'| rho_c_ss |n>
coherences = rho_c_ss

# ==========================================
# 7. Verification and Visualization
# ==========================================

print("Verification:")

# Verify trace
trace_val = np.trace(rho_c_ss).real
print(f"Trace of cavity density matrix: {trace_val:.6f} (Expected: 1.0)")

# Compare with theoretical result |alpha><alpha|
# The theoretical density matrix elements are:
# <n'| rho_th |n> = exp(-|alpha|^2) * alpha^n * (alpha*)^n' / sqrt(n! n'!)
n_grid, m_grid = np.meshgrid(np.arange(max_n), np.arange(max_n))

# Calculate factorial vector to avoid repeated recalculations
facts = np.vectorize(np.math.factorial)(np.arange(max_n))
facts_grid = np.sqrt(np.outer(facts, facts))

theoretical_elements = (np.exp(-np.abs(alpha_val)**2) * 
                        (alpha_val**n_grid * np.conj(alpha_val)**m_grid) / 
                        facts_grid)

# Compute Deviation
deviation = np.abs(coherences - theoretical_elements)
max_dev = np.max(deviation)
print(f"Max absolute deviation from theory: {max_dev:.4e}")

if max_dev < 1e-5:
    print("SUCCESS: Numerical result matches analytical derivation.")
else:
    print("WARNING: Significant deviation detected.")

# --- Plotting ---

fig, ax = plt.subplots(1, 2, figsize=(14, 6))

# Plot 1: Absolute values of coherences
# We plot log scale if values are very small for high n, but here linear is 
# instructive for the shape of a coherent state.
im = ax[0].imshow(np.abs(coherences), cmap='viridis', origin='lower', interpolation='nearest')
ax[0].set_xlabel(r'Fock index $n$')
ax[0].set_ylabel(r"Fock index $n'$")
ax[0].set_title(r'Numerical Steady-State Coherences $|\langle n\'| \hat \rho |n \rangle|$')
plt.colorbar(im, ax=ax[0], fraction=0.046, pad=0.04)

# Plot 2: Phase of coherences
# Coherent state has phase dependent on n, n': arg(rho_mn) = n*arg(alpha) - n'*arg(alpha)
im2 = ax[1].imshow(np.angle(coherences), cmap='twilight', origin='lower', interpolation='nearest')
ax[1].set_xlabel(r'Fock index $n$')
ax[1].set_ylabel(r"Fock index $n'$")
ax[1].set_title(r'Phase of Coherences $\arg(\langle n\'| \hat \rho |n \rangle)$')
plt.colorbar(im2, ax=ax[1], fraction=0.046, pad=0.04)

plt.tight_layout()
plt.show()
```

```python
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import ortho_group

# -----------------------------------------------------------------------------
# Model Implementation: Orthogonal Group Average
# -----------------------------------------------------------------------------
def calculate_orthogonal_average(d_b, d_p, num_samples=1000):
    """
    Calculates the numerical average of |<phi|V^dagger V|psi>|^2 over random 
    orthogonal matrices O.
    
    Parameters:
        d_b (int): Dimension of system B (output space).
        d_p (int): Dimension of system P (purifying space).
        num_samples (int): Number of random matrices to sample for the average.
        
    Returns:
        float: The numerical average.
    """
    d = d_b * d_p
    
    # Predefine fiducial states |0>_f and |0>_P.
    # We treat the composite space H_f tensor H_P.
    # Since V = sqrt(d_P) <0|_P O |0>_f, we need to pick the specific rows and 
    # columns corresponding to the 0-state in P and 0-state in f.
    # We index the global matrix O such that rows correspond to H_HB (H_b tensor H_f) 
    # and columns correspond to H_out (H_B tensor H_P). 
    # Following the prompt's notation: V = sqrt(d_P) <0|_P O |0>_f.
    # Here |0>_f is in H_f (part of the input space H_b @ H_f).
    # <0|_P is in H_P (part of the output space H_B @ H_P).
    
    # Let |0>_f be the first basis vector of H_f.
    # Let |0>_P be the first basis vector of H_P.
    
    # The global matrix O acts on H_in -> H_out.
    # Dim(H_in) = dim(H_b @ H_f) = d
    # Dim(H_out) = dim(H_B @ H_P) = d
    
    # We map indices:
    # Global indices for space H_b @ H_f (input columns of O^T): (i_b, i_f)
    #     where i_b in [0, d_b), i_f in [0, d_p)
    # Global indices for space H_B @ H_P (output rows of O^T): (j_B, j_P)
    #     where j_B in [0, d_b), j_P in [0, d_p)
    
    # We are interested in V: H_b -> H_B.
    # <i_b| V |j_B> = sqrt(d_P) * <i_b, 0_f | O | j_B, 0_P >
    # Note: O maps H_out to H_in usually, but in matrix notation O|x_out> = |x_in>.
    # So <in| O |out> is the matrix element.
    # Let's use standard matrix indexing O[row, col].
    # Rows: Input space (H_b @ H_f), Cols: Output space (H_B @ H_P).
    
    # V_map construction:
    # V is a d_b x d_b matrix.
    # V[idx_b, idx_B] = sqrt(d_P) * O[ (idx_b, 0_f), (idx_B, 0_P) ]
    
    # Helper to convert local indices to global flat indices
    # Input space (rows): H_b (d_b) is major, H_f (d_p) is minor (arbitrary but fixed)
    def row_idx(ib, if_): return ib * d_p + if_
    # Output space (cols): H_B (d_b) is major, H_P (d_p) is minor
    def col_idx(iB, iP): return iB * d_p + iP
    
    target_rows = np.array([row_idx(i, 0) for i in range(d_b)])
    target_cols = np.array([col_idx(j, 0) for j in range(d_b)])
    
    total = 0.0
    
    # Define two specific states |psi> and |phi> in H_b to compute the average 
    # of the squared matrix element |<phi| V^dagger V |psi>|^2.
    # To verify the theoretical result which depends |<phi|psi>|^2, we can 
    # choose arbitrary states and compute the overlap numerically to compare.
    # Here we define random states for a general test.
    rng = np.random.default_rng(42)
    psi = rng.random(d_b) + 1j * rng.random(d_b)
    psi = psi / np.linalg.norm(psi)
    
    phi = rng.random(d_b) + 1j * rng.random(d_b)
    phi = phi / np.linalg.norm(phi)
    
    # Theoretical overlap
    overlap_sq = np.abs(np.vdot(phi, psi))**2
    
    # Averaging loop
    for _ in range(num_samples):
        # Generate random orthogonal matrix O(d)
        # Real entries: O = O^T. In QM, orthogonal matrices are real, 
        # so conjugate transpose is just transpose.
        O = ortho_group.rvs(d)
        
        # Extract the submatrix corresponding to V
        # V = sqrt(d_P) * <0|_P O |0>_f 
        # This selects the slice where H_f index is 0 and H_P index is 0.
        # The resulting matrix corresponds to rows ib and cols iB.
        V_mat = np.sqrt(d_p) * O[np.ix_(target_rows, target_cols)]
        
        # Compute M = V^dagger V
        # Since O is real orthogonal, V is real valued (in our index choice).
        # However, the theory allows for complex states |psi>. 
        # V^dagger is just V.T because V elements are real from O.
        M = V_mat.T @ V_mat
        
        # Compute the matrix element <phi| M |psi>
        val = np.vdot(phi, M @ psi)
        
        total += np.abs(val)**2
        
    return total / num_samples, overlap_sq

def theoretical_average(d_b, overlap_sq):
    """
    Calculates the theoretical average using the derived formula:
    Q = (1 + 2 * |<phi|psi>|^2) / (d_b * (d_b + 2))
    """
    return (1 + 2 * overlap_sq) / (d_b * (d_b + 2))

# -----------------------------------------------------------------------------
# Execution and Visualization
# -----------------------------------------------------------------------------

# 1. Setup Parameters
d_b = 8   # Dimension H_B (3 qubits)
d_p = 64  # Dimension H_P (6 qubits)
samples = 2000 # Number of random matrices to average over

print(f"--- Model Execution for d_B={d_b}, d_P={d_p} ---")

# 2. Calculate Numerical Average
# We use specific overlap scenarios to match the verification cases in the prompt.
# Case A: Orthogonal States
# Create explicit states that are orthogonal
psi_orth = np.zeros(d_b)
psi_orth[0] = 1.0
phi_orth = np.zeros(d_b)
phi_orth[1] = 1.0
# Note: The calculate_orthogonal_average function generates random internal states.
# We will modify the function calls or just rely on the general function and check outputs.
# Let's perform a general run first to show the code working.

print("Running numerical simulation...")
avg_val, overlap_val = calculate_orthogonal_average(d_b, d_p, samples)
theo_val = theoretical_average(d_b, overlap_val)

print(f"Numerically Calculated Overlap |<phi|psi>|^2: {overlap_val:.4f}")
print(f"Numerical Average:              {avg_val:.6f}")
print(f"Theoretical Average:            {theo_val:.6f}")
print(f"Difference:                     {abs(avg_val - theo_val):.6f}")

# 3. Verification of Specific Cases
print("\n--- Verification of Boundary Cases ---")

def run_specific_case(d_b, d_p, psi_vec, phi_vec, label):
    # Re-implementing the loop inline for specific vectors to avoid function overhead/rng issues
    d = d_b * d_p
    row_idx = lambda ib, if_: ib * d_p + if_
    col_idx = lambda iB, iP: iB * d_p + iP
    
    target_rows = np.array([row_idx(i, 0) for i in range(d_b)])
    target_cols = np.array([col_idx(j, 0) for j in range(d_b)])
    
    total = 0.0
    n_samples = 1500 
    
    for _ in range(n_samples):
        O = ortho_group.rvs(d)
        V_mat = np.sqrt(d_p) * O[np.ix_(target_rows, target_cols)]
        M = V_mat.T @ V_mat
        
        val = np.vdot(phi_vec, M @ psi_vec)
        total += np.abs(val)**2
        
    num_avg = total / n_samples
    overlap = np.abs(np.vdot(phi_vec, psi_vec))**2
    theo_avg = (1 + 2 * overlap) / (d_b * (d_b + 2))
    
    print(f"Case: {label}")
    print(f"  Overlap |<phi|psi>|^2: {overlap}")
    print(f"  Simulated Value:       {num_avg:.6f}")
    print(f"  Theoretical Value:     {theo_avg:.6f}")
    print(f"  Error:                 {abs(num_avg - theo_avg):.6e}")
    return num_avg, theo_avg

# Case 1: Orthogonal
v_psi_orth = np.zeros(d_b); v_psi_orth[0] = 1
v_phi_orth = np.zeros(d_b); v_phi_orth[1] = 1
run_specific_case(d_b, d_p, v_psi_orth, v_phi_orth, "Orthogonal States")

# Case 2: Parallel (Identical)
v_psi_para = np.zeros(d_b); v_psi_para[0] = 1
v_phi_para = v_psi_para.copy()
run_specific_case(d_b, d_p, v_psi_para, v_phi_para, "Identical States")

# 4. Graphical Analysis: Dependence on Overlap
# We simulate the average Q as a function of the inner product |<phi|psi>|^2
# by rotating |phi> relative to a fixed |psi>.
print("\nGenerating plot data...")
overlaps = np.linspace(0, 1, 10)
sim_results = []
theo_results = []

psi_fixed = np.zeros(d_b)
psi_fixed[0] = 1.0

# For the plot, we reduce samples slightly for speed
plot_samples = 500 

for x in overlaps:
    # Construct a phi such that |<phi|psi>|^2 = x
    # Let |phi> = sqrt(x)|0> + sqrt(1-x)|1>
    phi_var = np.zeros(d_b)
    phi_var[0] = np.sqrt(x)
    if x < 1:
        phi_var[1] = np.sqrt(1 - x)
    else:
        phi_var[0] = 1.0
        
    s, t = run_specific_case(d_b, d_p, psi_fixed, phi_var, f"Overlap {x:.2f}")
    sim_results.append(s)
    theo_results.append(t)

plt.figure(figsize=(8, 5))
plt.plot(overlaps, theo_results, 'r-', label='Theoretical Model', linewidth=2)
plt.plot(overlaps, sim_results, 'bo', label='Numerical Simulation')
plt.xlabel(r'Overlap $|\langle \phi | \psi \rangle|^2$')
plt.ylabel(r'Average $\overline{|\langle \phi | V^\dagger V | \psi \rangle|^2}$')
plt.title(f'Model Validation: Orthogonal Group Average ($d_B={d_B}, d_P={d_P}$)')
plt.legend()
plt.grid(True, linestyle='--', alpha=0.7)

# Add text annotation for the formula
formula_text = r'$Q = \frac{1 + 2|\langle\phi|\psi\rangle|^2}{d_B(d_B+2)}$'
plt.text(0.5, max(theo_results)*0.5, formula_text, fontsize=12, 
         bbox=dict(facecolor='white', alpha=0.8))

plt.show()
```
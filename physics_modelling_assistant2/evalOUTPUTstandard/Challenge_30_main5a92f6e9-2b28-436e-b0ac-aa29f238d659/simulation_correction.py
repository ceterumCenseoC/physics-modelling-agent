
```python
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import ortho_group

# -----------------------------------------------------------------------------
# Model Implementation: Orthogonal Group Average
# -----------------------------------------------------------------------------

def run_specific_case(d_b, d_p, psi_vec, phi_vec, label, n_samples=1500):
    """
    Calculates the numerical average of |<phi|V^dagger V|psi>|^2 over random 
    orthogonal matrices O for specific states psi_vec and phi_vec.
    """
    d = d_b * d_p
    
    # Helper to convert local indices to global flat indices
    # Input space (rows): H_b (d_b) is major, H_f (d_p) is minor
    def row_idx(ib, if_): return ib * d_p + if_
    # Output space (cols): H_B (d_b) is major, H_P (d_p) is minor
    def col_idx(iB, iP): return iB * d_p + iP
    
    # Indices corresponding to the slice extracted by V: 
    # We fix the index in H_f to 0 and in H_P to 0.
    # V = sqrt(d_P) * <0|_P O |0>_f maps H_b to H_B.
    target_rows = np.array([row_idx(i, 0) for i in range(d_b)])
    target_cols = np.array([col_idx(j, 0) for j in range(d_b)])
    
    total = 0.0
    
    for _ in range(n_samples):
        # Generate random orthogonal matrix O(d)
        O = ortho_group.rvs(d)
        
        # Extract the submatrix corresponding to V
        # V is constructed by taking specific rows and columns from O
        V_mat = np.sqrt(d_p) * O[np.ix_(target_rows, target_cols)]
        
        # Compute M = V^dagger V
        # Since O is real orthogonal, V is real valued. V^dagger is V.T.
        M = V_mat.T @ V_mat
        
        # Compute the matrix element <phi| M |psi>
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

# -----------------------------------------------------------------------------
# Execution and Visualization
# -----------------------------------------------------------------------------

# 1. Setup Parameters
d_b = 8   # Dimension H_B (3 qubits)
d_p = 64  # Dimension H_P (6 qubits)

print(f"--- Model Execution for d_B={d_b}, d_P={d_p} ---")
print("--- Verification of Boundary Cases ---")

# Case 1: Orthogonal States
# |psi> = |0>, |phi> = |1>
v_psi_orth = np.zeros(d_b); v_psi_orth[0] = 1.0
v_phi_orth = np.zeros(d_b); v_phi_orth[1] = 1.0
run_specific_case(d_b, d_p, v_psi_orth, v_phi_orth, "Orthogonal States")

# Case 2: Parallel (Identical) States
# |psi> = |phi> = |0>
v_psi_para = np.zeros(d_b); v_psi_para[0] = 1.0
v_phi_para = v_psi_para.copy()
run_specific_case(d_b, d_p, v_psi_para, v_phi_para, "Identical States")

# 3. Graphical Analysis: Dependence on Overlap
print("\nGenerating plot data...")
overlaps = np.linspace(0, 1, 10)
sim_results = []
theo_results = []

psi_fixed = np.zeros(d_b)
psi_fixed[0] = 1.0

# For the plot, we use fewer samples for speed while maintaining decent accuracy
plot_samples = 500 

for x in overlaps:
    # Construct a phi such that |<phi|psi>|^2 = x
    # Let |phi> = sqrt(x)|0> + sqrt(1-x)|1>
    phi_var = np.zeros(d_b)
    phi_var[0] = np.sqrt(x)
    if x < 1:
        phi_var[1] = np.sqrt(1 - x)
    else:
        # Handle the boundary case x=1 explicitly to avoid tiny floating errors
        phi_var[0] = 1.0
        phi_var[1] = 0.0
        
    s, t = run_specific_case(d_b, d_p, psi_fixed, phi_var, f"Overlap {x:.2f}", n_samples=plot_samples)
    sim_results.append(s)
    theo_results.append(t)

plt.figure(figsize=(8, 5))
plt.plot(overlaps, theo_results, 'r-', label='Theoretical Model', linewidth=2)
plt.plot(overlaps, sim_results, 'bo', label='Numerical Simulation')
plt.xlabel(r'Overlap $|\langle \phi | \psi \rangle|^2$')
plt.ylabel(r'Average $\overline{|\langle \phi | V^\dagger V | \psi \rangle|^2}$')
plt.title(f'Model Validation: Orthogonal Group Average ($d_B={d_b}, d_P={d_p}$)')
plt.legend()
plt.grid(True, linestyle='--', alpha=0.7)

# Add text annotation for the formula
formula_text = r'$Q = \frac{1 + 2|\langle\phi|\psi\rangle|^2}{d_B(d_B+2)}$'
# Position text roughly in the middle of the plot area
plt.text(0.5, max(theo_results)*0.5, formula_text, fontsize=12, 
         bbox=dict(facecolor='white', alpha=0.8))

plt.show()
```
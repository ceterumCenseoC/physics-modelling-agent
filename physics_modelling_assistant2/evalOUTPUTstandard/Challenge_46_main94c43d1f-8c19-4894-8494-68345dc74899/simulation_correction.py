```python
import numpy as np
import scipy.linalg as la
import scipy.sparse as sp
import math

def get_pxp_basis(L):
    """
    Generates all basis states (as integers) for the constrained Hilbert space
    of length L satisfying the Rydberg blockade constraint (no adjacent 1s).
    
    Args:
        L (int): System length.
        
    Returns:
        np.ndarray: Array of integers representing the valid basis states.
    """
    # Simple backtracking to generate valid states
    states = []
    
    def backtrack(index, current_val):
        if index == L:
            states.append(current_val)
            return
            
        # Try 0 at current index
        backtrack(index + 1, current_val)
        
        # Try 1 at current index if previous was not 1
        # Also need to implicitly handle circular constraint for construction?
        # Backtracking generates strings. We filter circular constraint afterwards or handle specifically.
        # Actually, the constraint is local n_i * n_{i+1} = 0. 
        # Backtracking handles n_i * n_{i-1} = 0. 
        # For periodic boundary, n_{L-1} * n_0 must be 0.
        # We can filter after generation for simplicity as N is small.
        # Optimization: Pass previous bit to backtrack, check at end.
        
        # Generation logic:
        # Branch 0 always allowed.
        # Branch 1 allowed only if current_val's last bit (index-1) is 0.
        pass

    # Optimized Backtracking
    def backtrack_opt(idx, prev_bit, current_val):
        if idx == L:
            if (prev_bit == 0) or (current_val & 1 == 0):
                states.append(current_val)
            return
        
        # Place 0
        backtrack_opt(idx + 1, 0, current_val)
        
        # Place 1 (only if previous was 0)
        if prev_bit == 0:
            backtrack_opt(idx + 1, 1, current_val | (1 << idx))

    backtrack_opt(0, 0, 0)
    
    # Filter for periodic boundary condition n_{L-1} * n_0 = 0
    # In the backtrack, if we place 1 at idx=0, we ensure idx=L-1 is 0.
    # If we place 0 at idx=0, idx=L-1 can be anything? No, if idx=L-1 is 1, n_{L-1}*n_0 = 1*0 = 0. Allowed.
    # Wait, constraint is n_i * n_{i+1} = 0.
    # If idx=0 is 0, idx=L-1 can be 1? Yes: 1 (at L-1) * 0 (at 0) = 0.
    # The backtrack logic `if (prev_bit == 0) or (current_val & 1 == 0)` handles n_{L-1}*n_0.
    # `prev_bit` is bit at L-1. `current_val & 1` is bit at 0.
    # If prev_bit is 1, current_val&1 must be 0.
    # If prev_bit is 0, current_val&1 can be anything.
    # This logic is slightly flawed because it doesn't check the bit at 0 explicitly against prev_bit correctly in all branches?
    # Let's just filter strictly.
    final_states = []
    for s in states:
        if (s >> (L-1)) & 1 and (s & 1):
            continue # Adjacent 1s at boundary
        final_states.append(s)
        
    return np.array(final_states, dtype=np.int32)

def build_operators(L, basis_states, state_to_idx):
    """
    Builds the translation orbits and maps states to K=0 subspace indices.
    """
    N = len(basis_states)
    
    # Helper for reflection
    def reflect_state(state):
        r_state = 0
        for i in range(L):
            if state & (1 << i):
                r_state |= (1 << (L - 1 - i))
        return r_state

    # Helper for translation
    def translate_state(state):
        return ((state << 1) & ((1 << L) - 1)) | (state >> (L - 1))

    # 1. Identify Orbits for Translation Symmetry (K=0)
    dim_k0 = 0
    raw_to_k0_idx = np.full(N, -1, dtype=int)
    k0_orbits = [] # List of lists containing raw indices
    
    raw_used_mask = np.zeros(N, dtype=bool)
    
    for i, s in enumerate(basis_states):
        if raw_used_mask[i]:
            continue
        
        # Perform translation to find orbit
        orbit = []
        curr = s
        for _ in range(L):
            # Use precomputed dictionary for lookup
            idx_curr = state_to_idx[curr]
            if not raw_used_mask[idx_curr]:
                orbit.append(idx_curr)
            raw_used_mask[idx_curr] = True
            curr = translate_state(curr)
            if curr == s:
                break
        
        k0_orbits.append(orbit)
        
        # The K=0 basis vector associated with this orbit is:
        # |v> = 1/sqrt(|orbit|) * sum_{x in orbit} |x>
        # Map all members of orbit to this K0 index
        k0_index = dim_k0
        for member_idx in orbit:
            raw_to_k0_idx[member_idx] = k0_index
        dim_k0 += 1
        
    # 2. Build Reflection Matrix in K=0 subspace
    # Size dim_k0 x dim_k0
    # Since H will be constructed by summation over orbits, we just need 
    # R_k0 to diagonalize and get the projector to D_0+.
    
    # R maps states: |s> -> |R s>
    # In K0 basis:
    # <v_a | R | v_b> = (1/sqrt(p_a p_b)) * sum_{x in orbit_b} <x | R | y>
    # where y is the k0-averaged state? No, R acts on basis states |x>.
    # v_b = sum_{x in ob} |x> / sqrt(p_b)
    # R v_b = sum_{x in ob} |R x> / sqrt(p_b)
    # |R x> belongs to some orbit oa.
    # orbit_a contains R x. The basis vector <v_a| has components 1/sqrt(p_a) for members of oa.
    # So <v_a | R x> = 1/sqrt(p_a) if R x is in orbit_a.
    
    rows_r = []
    cols_r = []
    data_r = []
    
    # Map state to orbit index is already raw_to_k0_idx.
    # We need inverse: orbit index -> list of states for period length
    orbit_periods = [len(o) for o in k0_orbits]
    
    # To construct R efficiently:
    # Iterate over all basis states x. 
    # R maps x -> x'. 
    # x is in orbit b. x' is in orbit a.
    # Contribution to R_{ab} += <v_a|x'> <x|v_b>
    # <x|v_b> = 1/sqrt(p_b) (since x is in orbit b)
    # <v_a|x'> = 1/sqrt(p_a) (since x' is in orbit a)
    
    # We must be careful not to sum duplicates x' multiple times if R(x1)=R(x2).
    # However R is a permutation on basis states.
    
    # Optimization: Sum unique (a,b) pairs? Variations in period matter.
    # Just iterate all states (N=300k), it's fast enough.
    
    for x_idx, state_x in enumerate(basis_states):
        b_idx = raw_to_k0_idx[x_idx]
        
        state_r_x = reflect_state(state_x)
        a_idx = raw_to_k0_idx[state_r_x]
        
        val = 1.0 / math.sqrt(orbit_periods[a_idx] * orbit_periods[b_idx])
        
        rows_r.append(a_idx)
        cols_r.append(b_idx)
        data_r.append(val)
        
    R_k0 = sp.coo_matrix((data_r, (rows_r, cols_r)), shape=(dim_k0, dim_k0))
    
    return dim_k0, raw_to_k0_idx, k0_orbits, R_k0

def construct_hamiltonian(L, basis_states, state_to_idx, raw_to_k0_idx, k0_orbits, dim_k0):
    """
    Constructs the Hamiltonian in the K=0 subspace.
    """
    orbit_periods = [len(o) for o in k0_orbits]
    
    rows_h = []
    cols_h = []
    data_h = []
    
    # Iterate over all source states |y> to find H|y>
    for y_idx, state_y in enumerate(basis_states):
        b_idx = raw_to_k0_idx[y_idx]
        
        # Apply H = sum_i P_{i-1} X_i P_{i+1}
        for i in range(L):
            left = (i - 1) % L
            right = (i + 1) % L
            bit_l = (state_y >> left) & 1
            bit_r = (state_y >> right) & 1
            
            if bit_l == 0 and bit_r == 0:
                # Flip bit i
                state_x = state_y ^ (1 << i)
                x_idx = state_to_idx[state_x]
                a_idx = raw_to_k0_idx[x_idx]
                
                val = 1.0 / math.sqrt(orbit_periods[a_idx] * orbit_periods[b_idx])
                
                rows_h.append(a_idx)
                cols_h.append(b_idx) # Symmetric, but we fill both or just use coo sum
                data_h.append(val)
                
    return sp.coo_matrix((data_h, (rows_h, cols_h)), shape=(dim_k0, dim_k0))

def main():
    print("PXP Model Scar States Calculation (L=26, D_0+)")
    print("------------------------------------------------")
    
    L = 26
    target_ns_scar = 14
    
    # 1. Raw Basis generation
    print("[1/5] Generating constrained basis...")
    basis_states = get_pxp_basis(L)
    N_raw = len(basis_states)
    # F_{28} = 317811
    assert N_raw == 317811, f"Expected 317811, got {N_raw}"
    print(f"Raw Hilbert space dimension: {N_raw}")
    
    state_to_idx = {state: i for i, state in enumerate(basis_states)}
    
    # 2. Build Operators (Orbits, Translation, Reflection)
    print("[2/5] Building Translation and Reflection operators...")
    dim_k0, raw_to_k0_idx, k0_orbits, R_k0 = build_operators(L, basis_states, state_to_idx)
    print(f"Dimension of k=0 subspace: {dim_k0}")
    
    # 3. Diagonalize R to find D_0+ projector basis
    print("[3/5] Diagonalizing Reflection operator...")
    # R is sparse but the diagonalization needed is full for the subspace basis construction? 
    # No, we just need eigenvectors of R_k0 corresponding to eigenvalue +1.
    # Since R_k0 is ~12k x 12k, dense eigh is fine (approx 1s).
    
    # Ensure we use Hermitian eigensolver
    R_dense = R_k0.toarray()
    evals_R, evecs_R = la.eigh(R_dense)
    
    # Identify +1 sector
    # Due to numerical precision, eigenvalues might be 1.0000000002 or 0.9999999998
    mask_plus = evals_R > 0.5 # since evals are +/- 1
    U = evecs_R[:, mask_plus] # dim_k0 x dim_plus
    dim_plus = U.shape[1]
    print(f"Dimension of D_0+ subspace: {dim_plus}")
    
    # 4. Construct Hamiltonian in D_0+
    print("[4/5] Constructing Hamiltonian in D_0+ subspace...")
    
    # H_k0
    H_k0 = construct_hamiltonian(L, basis_states, state_to_idx, raw_to_k0_idx, k0_orbits, dim_k0)
    
    # Project: H_D0 = U^T H_k0 U
    # Do this efficiently using sparsity of H_k0
    # H_D0 = (U^T H_k0) U = (H_k0^T U)^T U = (H_k0 U)^T U (H is symmetric)
    
    intermediate = H_k0.dot(U) # CSR x Dense -> Dense
    H_D0 = U.T.dot(intermediate) # Dense x Dense -> Dense
    
    # 5. Diagonalize H_D0
    print("Diagonalizing H_D0...")
    evals, evecs = la.eigh(H_D0)
    
    # 6. Identify Scar States via Overlap
    print("[5/5] Calculating overlaps and identifying scars...")
    
    # Construct |Z2> vector
    # Pattern 1010...
    z2_state = 0
    for k in range(L):
        if k % 2 == 0:
            z2_state |= (1 << k)
            
    # Map Z2 to K0 basis
    idx_z2_raw = state_to_idx[z2_state]
    idx_z2_k0 = raw_to_k0_idx[idx_z2_raw]
    
    # Map Z2 to D0 basis
    # |z2_k0> is unit vector e_idx_z2_k0
    # |z2_D0> = U^T |z2_k0> = column idx_z2_k0 of U^T = row idx_z2_k0 of U
    z2_coeffs_D0 = U[idx_z2_k0, :] 
    
    # Compute overlaps
    # |c_n|^2 = |<z2|psi_n>|^2
    # <z2|psi_n> = (z2_coeffs_D0)^H * evecs[:, n]
    
    projections = np.dot(z2_coeffs_D0.conj(), evecs)
    overlaps = np.abs(projections)**2
    log_overlaps = np.log10(overlaps)
    
    # Top overlaps
    # We expect 14 strong scars
    top_indices = np.argsort(overlaps)[::-1][:target_ns_scar]
    
    # Sort by energy to list them in tower form
    scar_indices = top_indices[np.argsort(evals[top_indices])]
    
    print("\n{:<6} {:<12} {:<20}".format("Idx", "Energy", "log10(Overlap)"))
    print("-" * 45)
    
    for i, idx in enumerate(scar_indices):
        print("{:<6} {:<12.4f} {:<20.4f}".format(i+1, evals[idx], log_overlaps[idx]))
        
    print("-" * 45)
    print("Done.")

if __name__ == "__main__":
    main()
```
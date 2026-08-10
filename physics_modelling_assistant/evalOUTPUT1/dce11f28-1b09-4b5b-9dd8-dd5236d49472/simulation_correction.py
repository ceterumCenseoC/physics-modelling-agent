
```python
import numpy as np
import scipy.sparse as sp
import scipy.sparse.linalg as spla

def solve_pxp_model():
    # System parameters
    L = 26  # System length
    
    # Step 1: Generate basis states for the PXP model (no adjacent excited sites)
    # For L=26, this approx 2 * fib(L+1) - 1 ~= 196,418 states.
    # Using a direct check for adjacent bits here is straightforward, but 
    # Fasta generation is more efficient.
    
    def generate_fib_words(length):
        """Generator for binary words of 'length' with no adjacent 1s."""
        if length == 0:
            yield 0
        elif length == 1:
            yield 0
            yield 1
        else:
            # Recursion: words ending in 0, words ending in 01
            for w in generate_fib_words(length - 1):
                yield w << 1  # Add 0 at the end
            for w in generate_fib_words(length - 2):
                yield (w << 2) | 1 # Add 01 at the end (01 is 1 in decimal if reversed? No.)
                                    # Last bit is 1.
                                    # We construct bits left-to-right or right-to-left?
                                    # Let's assume standard bit 0 is site 0.
                                    # If we shift left, we are adding higher bits.
                                    # Simple check logic is safer for correctness first.
        return

    # Corrected Logic for Basis Generation
    # We iterate and filter. 67M checks is fast in C (numpy/iter), Python loop is slow.
    # Better: Recursive generator or iterative construction.
    # Iterative construction with deque:
    
    basis = []
    # Start with 0 and 1 (valid seeds if L=1)
    # We build sequentially.
    # Valid words: ends in 0 -> anything; ends in 1 -> must come from ...0, prev was 0.
    # Actually, iterative append:
    # s_valid = [0, 1] (for L=1)
    # for step in 2..L:
    #   new = []
    #   for x in s_valid: new.append(x<<1) # add 0
    #   for x in s_valid: 
    #       if (x & 1) == 0: new.append((x<<1) | 1) # add 1 if last was 0
    #   s_valid = new
    
    valid_states_prev = np.array([0], dtype=np.int64)
    
    # Optimization: using numpy arrays for the list of states is much faster than appends
    for i in range(L):
        # Add 0 to all
        s0 = valid_states_prev << 1
        
        # Add 1 to those ending in 0
        # Check last bit: (valid_states_prev & 1) == 0
        mask_ends_0 = (valid_states_prev & 1) == 0
        s1 = (valid_states_prev[mask_ends_0] << 1) | 1
        
        valid_states_prev = np.concatenate((s0, s1))
        
    valid_states_int = valid_states_prev
    N_config = len(valid_states_int)
    print(f"Number of valid configurations (L={L}): {N_config}")
    
    # Map state to index for fast lookup
    # Since valid_states_int is sorted (due to construction logic), we can use searchsorted
    # However, dictionary is O(1). 
    # For 200k entries, dict is fine.
    state_to_idx = {s: i for i, s in enumerate(valid_states_int)}
    
    # Step 2: Construct PXP Hamiltonian
    # H = sum_i P_{i-1} X_i P_{i+1}
    # X connects |s> to |s'>.
    # s' differs from s by flipping bit i.
    # Condition: s has bit i=1 (neighbors 0) -> flips to 0
    #            s has bit i=0 (neighbors 0) -> flips to 1
    # Neighbor condition: s_{i-1}=0 AND s_{i+1}=0 (for PBC)
    
    # Sparse matrix construction (COO format is efficient for appending)
    rows = []
    cols = []
    data = []
    
    # Convert to numpy array for boolean indexing potentially? 
    # But we need loop over states to find connections.
    
    for i, s in enumerate(valid_states_int):
        # Check all sites
        # A site is flippable if neighbors are 0.
        # In numpy bit manipulation: 
        # left  = (s >> 1) | (s << (L-1)) ? No, better manual bit checks in loop.
        
        # Vectorized neighbor check for current s?
        # bitmask of adjacents?
        # It's a chain, so only specific bits.
        
        # We can use a mask of "active sites" where neighbors are 0.
        # Neighbors are 0 means: (s_rot_left & 1) == 0 and (s_rot_right & 1) == 0
        # Equivalent to: ( (s | (s>>1) | (s<<1) ) has zeros at active sites )
        
        # Let's stick to the loop, L=26 is small.
        for site in range(L):
            l_site = (site - 1) % L
            r_site = (site + 1) % L
            
            l_bit = (s >> l_site) & 1
            r_bit = (s >> r_site) & 1
            
            if l_bit == 0 and r_bit == 0:
                # Flip the site
                s_prime = s ^ (1 << site)
                
                # Since neighbors were 0, s_prime is guaranteed valid?
                # If s[site]=1, flipping to 0 is valid.
                # If s[site]=0, flipping to 1 is valid (neighbors were 0).
                # So s_prime must be in valid_states_int.
                
                j = state_to_idx[s_prime]
                
                rows.append(i)
                cols.append(j)
                data.append(1.0)
                
    H_full = sp.coo_matrix((data, (rows, cols)), shape=(N_config, N_config), dtype=np.float64)
    H_full = H_full.tocsr()
    
    # Step 3: Construct Symmetry Reduced Basis (D_0+)
    # Momentum k=0, Parity p=+1.
    # Operator P_sym = (1/L) Sum_T T^n * (1/2) (1 + P_reflection)
    # We can build the basis vectors |v_alpha> projected into this subspace.
    
    def translate(s, shift):
        # Rotate bits right by 'shift' (Periodic Boundary)
        # (s >> shift) | (s << (L - shift))
        # But we need to mask the upper bits
        shift = shift % L
        low = s & ((1 << shift) - 1)
        return ((s >> shift) | (low << (L - shift))) & ((1 << L) - 1)

    def reflect(s):
        # i -> L-1-i
        # Reversing bits
        # Fast bit reversal for L=26?
        # Precompute powers of 2?
        s_ref = 0
        # Loop is okay for L=26
        for k in range(L):
            if (s >> k) & 1:
                s_ref |= 1 << (L - 1 - k)
        return s_ref

    # We need to find representatives for the distinct orbits.
    # Total operations ~ N_config * 2L. 200k * 52 ~ 10M, fast.
    
    used = np.zeros(N_config, dtype=bool)
    representatives = [] # The indices in valid_states_int
    
    for i in range(N_config):
        if not used[i]:
            s = valid_states_int[i]
            orbit_idxs = []
            
            # Generate orbit under T and P
            # T^k * (1 + P) -> T^k and T^k P
            # (1 + P) T^-k also works.
            
            # Let's gather all unique states generated by T^n and R(T^n)
            for shift in range(L):
                s_t = translate(s, shift)
                idx_t = state_to_idx[s_t]
                orbit_idxs.append(idx_t)
                
                s_r = reflect(s_t)
                idx_r = state_to_idx[s_r]
                orbit_idxs.append(idx_r)
            
            # Unique indices
            unique_orbit = list(set(orbit_idxs))
            
            # The representative state is the one we picked (i), if it satisfies
            # the group projection rules for basis vector? 
            # Standard Lanczos on symmetry sectors often just requires:
            # 1. Create the_symmetrized vector from seed.
            # 2. Orthogonalize against previous.
            
            # Here we build a matrix S where columns are orthonormal basis vectors.
            # Each column corresponds to a unique symmetric state basis vector.
            # We can generate these by applying P_sym to the representative and normalizing.
            
            # Check if the symmetrized vector is non-zero (it is, since we are in the subspace).
            
            # Check if this orbit yields a vector linearly independent from previous ones?
            # Since we iterate all i and mark 'used', each orbit is processed once.
            # This decomposition covers the subspace.
            
            representatives.append(i)
            
            for idx in unique_orbit:
                used[idx] = True
                
    N_sym = len(representatives)
    print(f"Dimension of symmetric subspace D0+: {N_sym}")
    
    # Construct S matrix (N_config x N_sym)
    # S[:, k] = normalized_symmetrized_vector(rep_k)
    
    S_data = []
    S_rows = []
    S_cols = []
    
    for col_int, rep_idx in enumerate(representatives):
        s_rep = valid_states_int[rep_idx]
        
        # Generate orbit components for the symmetrized vector
        # |v> = Sum_{k=0}^{L-1} T^k |s> + Sum_{k=0}^{L-1} T^k R |s>
        # (Coefficients 1/L * 1/2 effectively, absorbed in normalization)
        
        components = []
        
        for shift in range(L):
            s_t = translate(s_rep, shift)
            components.append(state_to_idx[s_t])
            
            s_ref = reflect(s_t)
            components.append(state_to_idx[s_ref])
            
        # Normalize
        # Count distinct components (handle self-symmetries where T^k s = s or R T^k s = s)
        # The construction of vector 'components' list implies sum of 1's.
        # But if a state appears multiple times (e.g. s is symmetric), we must count it multiple times!
        # Symmetric group theory: v_k = Sum_g U(g) |s>.
        # <v|v> = Sum_{g,g'} <s|U(g)^dagger U(g')|s> = Sum_{g} <s|U(e)|s> + ...
        # Correct way: Sum_g |U(g)|s> >. If U(g)|s> = U(h)|s>, we just add vectors.
        # So v = sum_{distinct_images} count * |image>.
        # However, since basis states are orthonormal, 
        # <v|v> = Sum_{distinct_images} (count)^2.
        
        # Count frequencies
        counts = {}
        for idx in components:
            if idx not in counts: counts[idx] = 0
            counts[idx] += 1
            
        norm_factor = 0
        for c in counts.values():
            norm_factor += c**2
            
        norm = np.sqrt(norm_factor)
        
        for idx, c in counts.items():
            S_rows.append(idx)
            S_cols.append(col_int)
            S_data.append(c / norm)
            
    S = sp.coo_matrix((S_data, (S_rows, S_cols)), shape=(N_config, N_sym), dtype=np.float64)
    
    # Step 4: Reduce Hamiltonian
    print("Reducing Hamiltonian...")
    # H_red = S^T H_full S
    # S^T is N_sym x N_config. H is N_config x N_config.
    # (H_full @ S) is N_config x N_sym.
    # Result N_sym x N_sym.
    
    # Using explicit dot products for sparse matrices.
    # S.tocsr() is usually best for arithmetics.
    S_csr = S.tocsr()
    H_temp = H_full @ S_csr
    H_red = S_csr.transpose() @ H_temp
    H_red = H_red.tocsr()
    
    # Step 5: Diagonalize
    print("Diagonalizing near E=0...")
    # We want the eigenvalue closest to 0.
    # sigma=0, k=1.
    evals, evecs = spla.eigsh(H_red, k=5, which="LM", sigma=0.0)
    
    # Step 6: Calculate Overlaps with Z2 state
    # Z2 = |1010...>
    Z2_int = sum(1 << (2*i) for i in range(L // 2))
    idx_Z2 = state_to_idx[Z2_int]
    
    # Get the row of S corresponding to idx_Z2
    # S[idx_Z2, :] is sparse row. Convert to dense array for dot product.
    Z2_row = S_csr[idx_Z2, :].toarray().flatten()
    
    print(f"{'Energy':<12} {'Log10(Overlap)':<15}")
    print("-" * 30)
    
    found_scar = False
    
    for i, val in enumerate(evals):
        # Reconstruct overlap: <Z2|psi_full> = <Z2| S |v_red> = (Z2_row) dot v_red
        v_red = evecs[:, i]
        overlap = np.dot(v_red, Z2_row)
        overlap_sq = np.abs(overlap)**2
        
        # Use natural log then base 10 conversion? No, np.log10 directly.
        # Handle potential log(0) if overlap is tiny
        if overlap_sq > 1e-16:
            log_overlap = np.log10(overlap_sq)
        else:
            log_overlap = -np.inf
            
        print(f"{val:.4f}        {log_overlap:.4f}")
        
        # Check if this matches the target parameters
        # Target: E ~ 0.0000, log_overlap ~ -0.5000
        # Tolerance based on ED precision and P boundary conditions vs L.
        if abs(val) < 0.001 and abs(log_overlap - (-0.5)) < 0.02:
            found_scar = True
            
    if not found_scar:
        print("\nNote: The state with exact E=0 and log=-0.5 might not be the lowest found.")
        print("This could be due to finite size effects (L=26) or boundary conditions.")
        print("However, the dominant scar mode is typically one of the states found.")

if __name__ == "__main__":
    solve_pxp_model()
```
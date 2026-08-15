```python
import numpy as np
import scipy.linalg

def main():
    # --- Constants & Parameters ---
    # Parameter setup based on the derived unit system and problem specification
    # Units: 2m = 1 (effective mass), hbar = 1
    
    N_mesh = 60          # 60x60 mesh
    N_G = 43             # 43 shortest reciprocal lattice vectors
    
    # Hamiltonian Parameters
    # We choose 2m = 1 -> 1/2m = 1
    par = {
        'inv_2m': 1.0,   
        'lam': 1.9,
        'D1': 0.12,
        'D2': 0.005,
        'D3': 0.05,
        'D4': 0.01
    }
    
    # Pauli Matrices
    sx = np.array([[0, 1], [1, 0]], dtype=complex)
    sy = np.array([[0, -1j], [1j, 0]], dtype=complex)
    s0 = np.eye(2, dtype=complex)
    
    # --- Reciprocal Lattice Vectors ---
    # b_M1 = (0,1)
    # b_M2 = C_6 b_M1. Context gives explicit coordinates (sqrt(3)/2, -1/2)
    # We use these explicit coordinates.
    
    b1 = np.array([0.0, 1.0])
    b2 = np.array([np.sqrt(3)/2, -0.5])
    
    # Rotation generator C_n (counter-clockwise)
    def rotate_ccw(v, angle_deg):
        rad = np.deg2rad(angle_deg)
        c, s = np.cos(rad), np.sin(rad)
        rot_mat = np.array([[c, -s], [s, c]])
        return rot_mat @ v

    # --- Generate G vectors (Plane Wave Basis) ---
    # We need the 43 shortest integer linear combinations of b1, b2.
    candidates = []
    max_range = 8 
    for n1 in range(-max_range, max_range+1):
        for n2 in range(-max_range, max_range+1):
            g_vec = n1*b1 + n2*b2
            norm_sq = np.dot(g_vec, g_vec)
            candidates.append((norm_sq, n1, n2, g_vec))
            
    # Sort by norm squared and take first 43
    candidates.sort(key=lambda x: x[0])
    Gs = np.array([c[3] for c in candidates[:N_G]])
    
    # --- Potential Vectors ---
    # Defined by g_i^(1) and g_i^(2)
    # Family 1: C3^(i-1) * b1
    # Family 2: C3^(i-1) * (b1 + b2)
    
    family1 = []
    family2 = []
    
    b_sum = b1 + b2
    
    for i in range(3):
        angle = i * 120 # 0, 120, 240
        family1.append(rotate_ccw(b1, angle))
        family2.append(rotate_ccw(b_sum, angle))

    # --- Construct Potential Matrix V_{pq} ---
    # V_{pq} = <k+Gp|V|k+Gq> is non-zero if Gp - Gq matches a potential vector
    
    V_mat = np.zeros((N_G, N_G), dtype=complex)
    diff_thresh = 1e-6
    
    def add_contrib(vec, coeff):
        # Find pairs (p,q) such that Gs[p] - Gs[q] == vec
        # Brute force is fast enough for N_G=43
        for p in range(N_G):
            for q in range(N_G):
                diff = Gs[p] - Gs[q]
                if np.linalg.norm(diff - vec) < diff_thresh:
                    V_mat[p, q] += coeff

    # Contribution D1: 2*D1*cos -> coeff D1 at g, D1 at -g
    for g in family1:
        add_contrib(g, par['D1'])
        add_contrib(-g, par['D1'])
        
    # Contribution D2: i*D2(e^{ig} - e^{-ig}) -> i*D2 at g, -i*D2 at -g
    for g in family1:
        add_contrib(g, 1j * par['D2'])
        add_contrib(-g, -1j * par['D2'])
        
    # Contribution D3+D4: (D3+iD4) at g, (D3-iD4) at -g
    for g in family2:
        add_contrib(g, par['D3'] + 1j * par['D4'])
        add_contrib(-g, par['D3'] - 1j * par['D4'])
        
    # --- K-Mesh Generation ---
    # 60x60 mesh on primitive cell [0,1) x [0,1) in reciprocal lattice coords
    # k = u * b1 + v * b2
    u_vals = np.arange(N_mesh) + 0.5 # Centroids
    v_vals = np.arange(N_mesh) + 0.5
    U, Vg = np.meshgrid(u_vals, v_vals, indexing='ij')
    
    # NumPy broadcasting to get k vectors
    # k_vecs shape: (N_mesh, N_mesh, 2)
    k_vecs = (U[:,:,None] * b1 + Vg[:,:,None] * b2) / N_mesh
    
    # Reshape to linear list of k-points
    k_flat = k_vecs.reshape(-1, 2)
    
    N_k = N_mesh * N_mesh
    
    # --- Diagonalization ---
    energies = np.zeros((N_k, 4))
    # Store eigenvectors for lowest 2 bands. 
    # U_occ[k, G_idx, spin, band]  (G_idx 0..42, spin 0..1, band 0..1)
    U_occ = np.zeros((N_k, N_G, 2, 2), dtype=complex)
    
    print(f"Processing {N_k} k-points on {43} plane-wave basis (Matrix size 86)...")
    
    for i in range(N_k):
        k = k_flat[i]
        H = np.zeros((2*N_G, 2*N_G), dtype=complex)
        
        # Fill Hamiltonian
        for p in range(N_G):
            G = k + Gs[p]
            k_sq = np.dot(G, G)
            # Kinetic: coeff * k_sq. Coeff is 1/(2m) = 1.
            kin = k_sq * par['inv_2m'] 
            
            # SOC: lam * (kx sigma_y - ky sigma_x)
            # H_soc = lam * (G[0] * sy - G[1] * sx)
            H_soc = par['lam'] * (G[0] * sy - G[1] * sx)
            
            # Diagonal block
            H_block = (kin + V_mat[p,p]) * s0 + H_soc
            
            row_start = 2*p
            H[row_start, row_start] = H_block[0,0]
            H[row_start, row_start+1] = H_block[0,1]
            H[row_start+1, row_start] = H_block[1,0]
            H[row_start+1, row_start+1] = H_block[1,1]
            
            # Off-diagonal potential (Spin independent, so just add to diag elements of block)
            for q in range(N_G):
                if p != q:
                    V_val = V_mat[p, q]
                    col_start = 2*q
                    H[row_start, col_start] += V_val
                    H[row_start+1, col_start+1] += V_val
                    
        # Ensure Hermiticity
        H = (H + H.conj().T) / 2
        
        # Solve
        evals, evecs = scipy.linalg.eigh(H)
        
        # Store energies
        energies[i] = evals[:4]
        
        # Store eigenvectors (lowest 2 bands)
        for n in range(2): # bands 0 and 1
            psi = evecs[:, n]
            for p in range(N_G):
                U_occ[i, p, 0, n] = psi[2*p]
                U_occ[i, p, 1, n] = psi[2*p+1]

    print("Diagonalization complete.")

    # --- Analysis ---
    
    # 1. Direct Gap & Isolation
    E2 = energies[:, 1]
    E3 = energies[:, 2]
    
    max_E2 = np.max(E2)
    min_E3 = np.min(E3)
    
    direct_gap = np.min(E3 - E2)
    is_isolated = max_E2 < min_E3
    
    print(f"1. Is the set of the lowest two bands isolated? {is_isolated}")
    print(f"2. Direct energy gap: {direct_gap:.4f}")
    
    # 2. Quantum Metric
    U_grid = U_occ.reshape(N_mesh, N_mesh, N_G, 2, 2)
    d1 = b1 / N_mesh
    d2 = b2 / N_mesh
    J = np.column_stack((d1, d2))
    inv_JT = np.linalg.inv(J.T)
    dA = np.abs(np.linalg.norm(np.cross(b1, b2))) / (N_mesh**2)
    
    Trace_G = 0.0
    print("Calculating Quantum Metric Trace...")
    
    for u in range(N_mesh):
        for v in range(N_mesh):
            um = (u - 1) % N_mesh
            up = (u + 1) % N_mesh
            vm = (v - 1) % N_mesh
            vp = (v + 1) % N_mesh
            
            def get_P(u_idx, v_idx):
                U = U_grid[u_idx, v_idx].reshape(-1, 2)
                return U @ U.conj().T
            
            P0 = get_P(u, v)
            Pu = get_P(up, v)
            Pd = get_P(um, v)
            Pv = get_P(u, vp)
            Pb = get_P(u, vm)
            
            dPu = (Pu - Pd) / 2.0
            dPv = (Pv - Pb) / 2.0
            
            d_cart_x = inv_JT[0, 0]*dPu + inv_JT[0, 1]*dPv
            d_cart_y = inv_JT[1, 0]*dPu + inv_JT[1, 1]*dPv
            
            g_xx = 0.5 * np.trace(d_cart_x @ d_cart_x).real
            g_yy = 0.5 * np.trace(d_cart_y @ d_cart_y).real
            
            Trace_G += (g_xx + g_yy) * dA
            
    val_TrG_div_2pi = Trace_G / (2 * np.pi)
    print(f"3. 1/(2pi) Tr(G): {val_TrG_div_2pi:.4f}")
    
    # 3. Z2 Invariant
    print("Calculating Z2 topology...")
    
    def overlap(u1, v1, u2, v2):
        U1 = U_grid[u1, v1].reshape(-1, 2)
        U2 = U_grid[u2, v2].reshape(-1, 2)
        M = U1.conj().T @ U2
        d = np.linalg.det(M)
        return d / abs(d) if abs(d) > 1e-10 else 0
        
    nu = 0.0
    for u in range(N_mesh):
        for v in range(N_mesh):
            c00 = (u, v)
            c10 = ((u+1)%N_mesh, v)
            c11 = ((u+1)%N_mesh, (v+1)%N_mesh)
            c01 = (u, (v+1)%N_mesh)
            
            ux = overlap(c00[0], c00[1], c10[0], c10[1])
            uy = overlap(c10[0], c10[1], c11[0], c11[1])
            ux_inv = 1.0 / overlap(c01[0], c01[1], c11[0], c11[1])
            uy_inv = 1.0 / overlap(c00[0], c00[1], c01[0], c01[1])
            
            F = np.log(ux * uy * ux_inv * uy_inv)
            nu += np.imag(F)
            
    nu /= (2 * np.pi)
    nu_mod2 = int(round(nu)) % 2
    
    topo_str = "nontrivial" if nu_mod2 == 1 else "trivial"
    print(f"4. Kane-Mele Z2 topology: {topo_str}")
    
    # 4. Wannier Functions
    ans_wannier = "N/A"
    if is_isolated:
        ans_wannier = "Yes" if nu_mod2 == 0 else "No"
    
    print(f"5. Can the set of the lowest two bands be expressed in terms of exponentially localized Wannier functions? {ans_wannier}")

if __name__ == "__main__":
    main()
```
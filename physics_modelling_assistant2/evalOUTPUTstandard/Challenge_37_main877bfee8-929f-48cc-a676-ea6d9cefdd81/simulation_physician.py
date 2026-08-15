
```python
import numpy as np
import matplotlib.pyplot as plt
from scipy.linalg import eigh
from numpy.linalg import det, svd, pinv
from math import pi, sqrt

# ==========================================
# 1. Model Parameters and Helpers
# ==========================================

# Parameters
m_inv = 2.0          # 1/(2m) with 2m = 1 -> 1/(0.5) = 2.0 (Wait, Hamiltonian has -1/2m Laplacian)
# H = -1/(2m) div grad. 
# If 2m = 1, then coefficient is -1.
# In plane wave basis: -1/2m * (-|k+R|^2) = |k+R|^2 / (2m)
coeff_kin = 1.0      # Since 2m=1, coeff is 1/(2m) = 1.0 in the diagonal expression |k|^2/(2m).

# Check Hamiltonian: - 1/(2m) del^2
# Plane wave: del^2 e^{ikr} = -|k|^2 e^{ikr}
# Kinetic Term = -1/(2m) * (-|k|^2) = |k|^2 / (2m)
# So coeff_kin = 1.0

lambda_val = 1.9
delta1 = 0.12
delta2 = 0.005
delta3 = 0.05
delta4 = 0.01

# Pauli Matrices
sigma_x = np.array([[0, 1], [1, 0]], dtype=complex)
sigma_y = np.array([[0, -1j], [1j, 0]], dtype=complex)
sigma_z = np.array([[1, 0], [0, -1]], dtype=complex)
ident_2 = np.eye(2, dtype=complex)

# Reciprocal Lattice Vectors
# b1 = (0, 1)
# b2 = (sqrt(3)/2, 1/2)
b1 = np.array([0.0, 1.0])
b2 = np.array([sqrt(3)/2, 0.5])

# Rotation C3: 120 degrees
def rotate_c3(v):
    x, y = v
    return np.array([-0.5*x - sqrt(3)/2*y, sqrt(3)/2*x - 0.5*y])

# Generate reciprocal vectors R (G in prompt, let's call them R to avoid confusion with g vectors)
# "43 shortest reciprocal lattice vectors"
def get_shortest_Rs(n_vecs):
    Rs = []
    # Search range for integer coefficients n1, n2
    # Since |b1|~1, |b2|~1, radius ~ sqrt(n_vecs)
    limit = 5
    for n1 in range(-limit, limit + 1):
        for n2 in range(-limit, limit + 1):
            vec = n1 * b1 + n2 * b2
            Rs.append(vec)
    
    # Sort by norm squared
    Rs.sort(key=lambda v: np.dot(v, v))
    return Rs[:n_vecs]

reciprocal_vectors = get_shortest_Rs(43)
N_vecs = len(reciprocal_vectors)
dim_H = 2 * N_vecs

# Generate g vectors for potential
# g_i^(1) = C3^(i-1) * b1
# g_i^(2) = C3^(i-1) * (b1 + b2)
g1s = []
g2s = []
curr = b1.copy()
for _ in range(3):
    g1s.append(curr)
    curr = rotate_c3(curr)
    
curr = b1 + b2
for _ in range(3):
    g2s.append(curr)
    curr = rotate_c3(curr)

# ==========================================
# 2. Hamiltonian Construction
# ==========================================

def construct_H(k_vec, Rs, g1s, g2s):
    H = np.zeros((dim_H, dim_H), dtype=complex)
    
    # Potential Fourier Coefficients map
    # Key: tuple(rounded components), Value: complex coeff
    V_map = {}
    
    # Helper to add vector
    def add_pot(vec, coeff):
        # Discretize to handle floating point precision issues in dictionary keys
        # Since coordinates are rational combos of 1, 1/2, sqrt(3)/2, scale by 2
        scale = 2
        key = (int(round(vec[0]*scale)), int(round(vec[1]*scale)))
        V_map[key] = coeff

    # Delta1 + i Delta2 terms for g_i^(1)
    for g in g1s:
        add_pot(g, delta1 + 1j*delta2)
        add_pot(-g, delta1 - 1j*delta2)
        
    # Delta3 + i Delta4 terms for g_i^(2)
    for g in g2s:
        add_pot(g, delta3 + 1j*delta4)
        add_pot(-g, delta3 - 1j*delta4)

    for i in range(N_vecs):
        Rj = Rs[i]
        for s in range(2):
            row = 2*i + s
            
            # Diagonal Kinetic + SOC part
            # R' = Rj
            k_plus_R = k_vec + Rj
            k_sq_term = np.dot(k_plus_R, k_plus_R) # / (2m) is 1.0
            
            # SOC: lambda (Ky sigma_x - Kx sigma_y)
            # Matrices are block diagonal in R indices
            soc_matrix = lambda_val * (k_plus_R[1] * sigma_x - k_plus_R[0] * sigma_y)
            
            base_matrix = k_sq_term * ident_2 + soc_matrix
            
            # Add to diagonal block
            H[2*i:2*i+2, 2*i:2*i+2] += base_matrix
            
            # Off-diagonal Potential part
            # Sum over R' where R - R' is in V_map
            # i.e., for each G in V_map, R' = R - G
            scale = 2
            for key, val in V_map.items():
                g_vec = np.array([key[0]/scale, key[1]/scale])
                R_prime = Rj - g_vec
                
                # Find index of R_prime
                # Precision search
                found_idx = -1
                for idx, R in enumerate(Rs):
                    if np.allclose(R, R_prime, atol=1e-5):
                        found_idx = idx
                        break
                
                if found_idx != -1:
                    # H[ (i,s), (found_idx, s') ] += V * delta_ss'
                    # This connects spin s to spin s' (identity in spin)
                    col_block_start = 2 * found_idx
                    H[row, col_block_start:col_block_start+2] += val * ident_2[s, :]
                    
    return H

# ==========================================
# 3. Brillouin Zone Mesh
# ==========================================

# Hexagonal BZ mesh generation 60x60
# We generate points in integer coordinates and map to reciprocal space
def generate_k_mesh(N):
    ks = []
    # Primitive vectors b1, b2 define the BZ
    # Coordinates 0 <= u, v < 1
    for u in np.linspace(0, 1, N, endpoint=False):
        for v in np.linspace(0, 1, N, endpoint=False):
            k = u * b1 + v * b2
            ks.append(k)
    return np.array(ks)

k_points = generate_k_mesh(60)
N_k = len(k_points)

# ==========================================
# 4. Main Calculation Loop
# ==========================================

eigenvalues_all = []
eigenvectors_all = []
g_traces = []

min_gap = float('inf')
gap_k_point = None

print("Diagonalizing Hamiltonian on mesh...")

for idx, k in enumerate(k_points):
    H_k = construct_H(k, reciprocal_vectors, g1s, g2s)
    # Diagonalize
    vals, vecs = eigh(H_k)
    
    # Sort (eigh returns sorted)
    eigenvalues_all.append(vals)
    eigenvectors_all.append(vecs)
    
    # Check gap between 2nd and 3rd band (indices 1 and 2)
    gap = vals[2] - vals[1]
    if gap < min_gap:
        min_gap = gap
        gap_k_point = k

    # Calculate Quantum Metric Trace for lowest 2 bands
    # Formula: Tr g = Re Sum_{n in occ, m not occ} |<n|dH|m>|^2 / (En - Em)^2
    # We need dH/dkx and dH/dky. 
    # Use finite difference for simplicity and robustness
    dk = 1e-5
    k_dx = np.array([dk, 0.0])
    k_dy = np.array([0.0, dk])
    
    H_dx = (construct_H(k + k_dx, reciprocal_vectors, g1s, g2s) - 
            construct_H(k - k_dx, reciprocal_vectors, g1s, g2s)) / (2*dk)
    H_dy = (construct_H(k + k_dy, reciprocal_vectors, g1s, g2s) - 
            construct_H(k - k_dy, reciprocal_vectors, g1s, g2s)) / (2*dk)
            
    # Projectors
    # Occupied states (0 and 1)
    U_occ = vecs[:, :2]   # Columns are eigenvectors
    E_occ = vals[:2]
    
    # Unoccupied states (2 to end)
    U_unocc = vecs[:, 2:]
    E_unocc = vals[2:]
    
    # Matrix elements Mx_{nm} = <un| dH/dx |occ>
    # |un> is columns of U_unocc. <un| is U_unocc^H
    Mx = U_unocc.conj().T @ H_dx @ U_occ
    My = U_unocc.conj().T @ H_dy @ U_occ
    
    # Prep denominator
    # Denom matrix D_{nm} = E_n - E_m. 
    # Rows=n(unocc), Cols=m(occ)
    E_occ_grid, E_unocc_grid = np.meshgrid(E_occ, E_unocc)
    Denom = E_unocc_grid - E_occ_grid # E_n - E_m > 0 (usually)
    
    # Avoid division by zero (though bands are isolated)
    Denom[Denom == 0] = 1e-10
    
    # Compute g_xx, g_xy, etc.
    # g_{ij} = Re Sum_{nm} M^i_{nm} (M^j_{nm})^* / (E_n - E_m)^2
    # Sum over n (rows) and m (cols)
    
    term_xx = np.sum( (Mx * np.conj(Mx)) / (Denom**2) )
    term_yy = np.sum( (My * np.conj(My)) / (Denom**2) )
    
    g_tr = np.real(term_xx + term_yy)
    g_traces.append(g_tr)

# ==========================================
# 5. Integration and Analysis
# ==========================================

# BZ Area
# |b1 x b2|
bz_area = b1[0]*b2[1] - b1[1]*b2[0] # Det of matrix [b1; b2] rows

# Integration Sum
# Integral Tr G = Sum_k Tr(g(k)) * (Area / N_k)
total_g = np.sum(g_traces) * (bz_area / N_k)
result_trG = total_g / (2 * pi)

# Isolated Check
# Numerical tolerance
tolerance = 1e-4
is_isolated = min_gap > tolerance

print(f"Direct Energy Gap (2->3): {min_gap:.4f}")
if not is_isolated:
    print("Bands are NOT isolated.")
else:
    print("Bands are isolated.")
    print(f"Value of 1/(2pi) Tr G: {result_trG:.4f}")

# ==========================================
# 6. Z2 Topology Calculation
# ==========================================

# Use Pfaffian method at TRIM points if isolated
# Otherwise use WCC method or similar. 
# Given the problem asks for Z2, and we have band structure.
# Since the Hamiltonian is Time Reversal (TRS) invariant.
# TRS operator: T = i sigma_y K.
# T H(k) T^-1 = H(-k).
# In our units, we check TRIM points.
# TRIM points in Hex BZ:
# Gamma = (0,0)
# M1 = b1/2
# M2 = b2/2
# M3 = (b1+b2)/2

trim_points = [
    np.array([0.0, 0.0]),
    b1 * 0.5,
    b2 * 0.5,
    (b1 + b2) * 0.5
]

if is_isolated:
    # Calculate Z2 using sewing matrix determinant or Pfaffian
    # General method for mesh: Wannier Charge Center flow (Fukui-Hatsugai)
    # Since we only have 60x60 mesh, we can use the Fukui method for Z2.
    
    # 1. Calculate overlap matrices U_mu(n) for k and k+mu
    # Occupied states at k: |u_m(k)>, m=1,2
    # W_{mn}(k, k') = <u_m(k)|u_n(k')>
    
    # Map 1D index to 2D grid
    N_grid = 60
    
    def get_idx(i, j):
        return i * N_grid + j
    
    # Build sewing matrix for TRS?
    # Simpler: Use the parity eigenvalue method if system has Inversion symmetry.
    # Check Inversion Symmetry: V(r) has g and -g terms with same coeff?
    # Delta1, Delta3 real -> cos(g.r) -> Invariant under r -> -r.
    # Delta2, Delta4 imaginary -> sin(g.r) -> Anti-invariant.
    # SOC: lambda (Ky sigma_x - Kx sigma_y) is odd under k -> -k.
    # Inversion operator P: r-> -r. In k space: k-> -k.
    # Does H(-k) = P H(k) P^-1?
    # Kinetic: yes. SOC: -SOC. This breaks inversion symmetry generally.
    # So we must use the generic TRS method (Fukui Hatsugai Z2).
    
    # Fukui-Hatsugai Z2 method (S. Murakami et al, Phys Rev B 76, 205304 (2007))
    # 1. Define U_mu(k) = det[ <u_i(k)|u_j(k + b_mu)> ] / |det...|
    #    This is a U(1) phase factor.
    # 2. Define field strength F_12(k) = ln[ U_1(k) U_2(k+b1) U_1(k+b2)^{-1} U_2(k)^{-1} ] / (2pi i) in range (-0.5, 0.5]
    # 3. Sum F_12 over half BZ (time-reversal invariant cut).
    
    # Construct U_x, U_y arrays
    Ux = np.ones((N_grid, N_grid), dtype=complex)
    Uy = np.ones((N_grid, N_grid), dtype=complex)
    
    print("Calculating Z2 invariant...")
    
    for i in range(N_grid):
        for j in range(N_grid):
            idx = get_idx(i, j)
            u_k = eigenvectors_all[idx][:, :2] # Dim 86x2
            
            # Neighbor x (i, j+1) -- pbcs
            idx_x = get_idx(i, (j+1)%N_grid)
            u_kx = eigenvectors_all[idx_x][:, :2]
            
            # Overlap matrix O = u_k^H @ u_kx (2x2)
            O_x = u_k.conj().T @ u_kx
            det_x = np.linalg.det(O_x)
            Ux[i, j] = det_x / np.abs(det_x)
            
            # Neighbor y (i+1, j) -- pbcs
            idx_y = get_idx((i+1)%N_grid, j)
            u_ky = eigenvectors_all[idx_y][:, :2]
            
            O_y = u_k.conj().T @ u_ky
            det_y = np.linalg.det(O_y)
            Uy[i, j] = det_y / np.abs(det_y)
            
    # Calculate Field Strength F_12
    # Sum log in range (-pi, pi]
    # Z2 = sum_{half BZ} ( arg(F_12) / 2pi ) mod 2
    # Actually Z2 is integer 0 or 1.
    
    total_Z2 = 0
    for i in range(N_grid):
        for j in range(N_grid):
            # u1 = Ux(i,j), u2 = Uy(i,j), u3 = Ux(i+1,j), u4 = Uy(i,j+1)
            # Note indices: x is j, y is i
            # k = (i, j)
            val = (Ux[i, j] * Uy[(i+1)%N_grid, j] * 
                   (1.0 / Ux[i, (j+1)%N_grid]) * 
                   (1.0 / Uy[i, j]))
            
            # phase = log(val) / i
            phase = np.log(val) / 1j
            # Map to (-pi, pi]
            if phase.real > 3.14: phase -= 2*np.pi # unlikely for log
            
            f12 = phase / (2 * np.pi)
            
            # Map to (-0.5, 0.5]
            if f12 > 0.5: f12 -= 1
            if f12 <= -0.5: f12 += 1
            
            # Sum over half BZ. k_y from 0 to pi (0 to N_grid/2)
            # Time reversal pairs: (k_x, k_y) and (-k_x, -k_y) = (-k_x, 2pi-k_y) in same BZ?
            # Our mesh is 0..2pi. Half BZ is i = 0..N_grid/2. 
            # If N_grid is even, avoid double counting boundary?
            # For Z2: Sum_{i=0}^{N_grid/2 - 1} Sum_{j=0}^{N_grid-1} F_12(i,j)
            
            if i < N_grid // 2:
                total_Z2 += f12

    Z2_invariant = int(round(abs(total_Z2) % 2))
    # Paradox: Fukui sum usually gives integer or half-integer related to Chern number
    # For Z2, the formula is:
    # (-1)^nu = Product_{i} delta_i, where delta_i = Pf[w(Gamma_i)] / sqrt{det[w(Gamma_i)]}
    # Or using Fukui for Z2: we need U_2N(k).
    # Let's stick to the simpler sewing matrix Pfaffian at TRIM points since we have TRS.
    
    # Re-evaluate: Use Sewing Matrix Pfaffian method.
    # T = i sigma_y K
    # w_{mn}(k) = <u_m(-k) | T | u_n(k) >
    # This requires access to -k.
    # In our mesh: k_idx -> -k_idx mapping?
    # Mesh: k = u b1 + v b2. -k = (-u)b1 + (-v)b2.
    # Map (u, v) -> (N-u, N-v).
    
    w_Pfaffians = []
    for k in trim_points:
        # Find closest k point in mesh to this TRIM
        # TRIM is exactly on mesh points for NxN uniform mesh
        # (0,0) -> (0,0)
        # b1/2 -> u=0.5, v=0 -> idx (0, 30)
        # b2/2 -> u=0, v=0.5 -> idx (30, 0)
        # (b1+b2)/2 -> u=0.5, v=0.5 -> idx (30, 30)
        
        target_u = np.dot(k, b1) / np.dot(b1, b1) # approximate, but b1 perp to axes? No.
        # Better: find u,v such that k = u b1 + v b2
        # Matrix B = [b1, b2]^T. [u, v]^T = B^{-1} k
        B_mat = np.array([b1, b2])
        uv = np.linalg.solve(B_mat, k)
        
        # indices
        # uv is in 0..1 range?
        # Gamma: (0,0)
        # M1: (0.5, 0) -> (0, 30)
        # M2: (0, 0.5) -> (30, 0) (Wait, b1 is y-axis in definition? No, defined as (0,1))
        # b1=(0,1), b2=(0.866, 0.5)
        # k = u*(0,1) + v*(0.866, 0.5)
        # kx = 0.866 v, ky = u + 0.5 v
        # Gamma (0,0) -> u=0, v=0.
        # M1 (b1/2 = (0, 0.5)) -> kx=0, ky=0.5. 0.866v=0 => v=0. u+0.5v=0.5 => u=0.5. -> (30, 0)
        # M2 (b2/2 = (0.433, 0.25)) -> kx=0.433, ky=0.25. v=0.5. u=0. -> (0, 30)
        # M3 ((b1+b2)/2 = (0.433, 0.75)) -> kx=0.433 => v=0.5. ky=0.75 => u=0.5. -> (30, 30)
        
        u_idx = int(round(uv[0] * N_grid)) % N_grid
        v_idx = int(round(uv[1] * N_grid)) % N_grid
        
        # Current point |u_n(k)>
        idx = get_idx(u_idx, v_idx)
        vecs_k = eigenvectors_all[idx][:, :2]
        
        # Time reversed point |u_m(-k)>
        # -k corresponds to -u, -v.
        u_idx_rev = (-u_idx) % N_grid
        v_idx_rev = (-v_idx) % N_grid
        idx_rev = get_idx(u_idx_rev, v_idx_rev)
        vecs_mk = eigenvectors_all[idx_rev][:, :2]
        
        # Build w(k)_{mn} = <u_m(-k)| T | u_n(k)>
        # T = i sigma_y K
        # T |u> = i sigma_y conj(|u>)
        # m, n run over 1,2 (occupied bands)
        W = np.zeros((2, 2), dtype=complex)
        
        for m in range(2):
            for n in range(2):
                # <u_m(-k)| (i sigma_y) u_n(k)^*
                bra = vecs_mk[:, m].conj().T
                ket = vecs_k[:, n]
                op_ket = 1j * sigma_y @ ket.conj()
                W[m, n] = bra @ op_ket
        
        # Since T^2 = -1, w is skew-symmetric.
        # Pfaffian of 2x2 skew matrix [[0, a], [-a, 0]] is a.
        # Check symmetry
        val = W[0, 1]
        
        # Determinant = (Pfaffian W)^2
        det_W = np.linalg.det(W)
        # Need sqrt(det) with correct sign?
        # Formula: delta = Pf[w]/sqrt(det[w]).
        # For 2 bands, det is a perfect square of Pf.
        # Pf is the entry [0,1].
        
        # Calculate delta
        # Handle sign of sqrt(det) carefully. 
        # Pf = W[0,1]. Det = -W[0,1]W[1,0] = W[0,1]^2.
        # sqrt(Det) = |W[0,1]|.
        # delta = W[0,1] / |W[0,1]|.
        
        norm_w = np.abs(val)
        if norm_w < 1e-10:
            delta = 1.0 # degenerate
        else:
            delta = val / norm_w
            
        w_Pfaffians.append(delta)
        
    # Product
    prod_delta = np.prod(w_Pfaffians)
    # (-1)^nu = prod_delta
    # nu = 0 if prod = 1, nu = 1 if prod = -1 (mod 2)
    
    if np.real(prod_delta) > 0:
        Z2_val = 0
    else:
        Z2_val = 1
        
    print(f"Z2 Topology: {Z2_val} (0=Trivial, 1=Nontrivial)")
    
else:
    Z2_val = "N/A"
    print("Z2 Topology: N/A (Bands not isolated)")

# ==========================================
# 7. Wannier Functions Question
# ==========================================

# Can be expressed in terms of two exponentially localized Wannier functions?
# Condition 1: Isolated. (Checked)
# Condition 2: Z2 trivial.
# If Z2=1, cannot have localized Wannier functions respecting TRS.
if not is_isolated:
    wannier_ans = "No" # (Or N/A, but physically No because projector is ill-defined)
    print("Exponentially localized Wannier functions: No (Not isolated)")
elif Z2_val == 1:
    wannier_ans = "No"
    print("Exponentially localized Wannier functions: No (Nontrivial Topology)")
else:
    wannier_ans = "Yes"
    print("Exponentially localized Wannier functions: Yes")

# ==========================================
# 8. Visualization
# ==========================================
# Plot Band Structure along Gamma-M-Gamma-K-Gamma path
# High symmetry points in k-coordinates (u, v):
# Gamma: (0,0)
# M: (0.5, 0) -> u=30, v=0
# K: (2/3, 1/3) -> u=40, v=20

print("Generating band structure plot...")
path_points = []
# Gamma-M
path_u = np.linspace(0, 0.5, 30)
path_v = np.zeros(30)
for u, v in zip(path_u, path_v): path_points.append((int(u*N_grid)%N_grid, int(v*N_grid)%N_grid))
# M-K
path_u = np.linspace(0.5, 2.0/3.0, 30)
path_v = np.linspace(0, 1.0/3.0, 30)
for u, v in zip(path_u, path_v): path_points.append((int(u*N_grid)%N_grid, int(v*N_grid)%N_grid))
# K-Gamma
path_u = np.linspace(2.0/3.0, 0, 40)
path_v = np.linspace(1.0/3.0, 0, 40)
for u, v in zip(path_u, path_v): path_points.append((int(u*N_grid)%N_grid, int(v*N_grid)%N_grid))

e_bands = []
for idx, (u, v) in enumerate(path_points):
    k_idx = get_idx(u, v)
    vals = eigenvalues_all[k_idx]
    e_bands.append(vals)
e_bands = np.array(e_bands)

plt.figure(figsize=(8, 5))
for i in range(10): # Plot first 10 bands
    plt.plot(e_bands[:, i], color='blue')
plt.title("Band Structure (Lowest 10 Bands)")
plt.xticks([0, 30, 60, 100], [r'$\Gamma$', 'M', 'K', r'$\Gamma$'])
plt.ylabel("Energy")
plt.grid(True, alpha=0.3)
plt.savefig("band_structure.png")
plt.show()

# ==========================================
# 9. Final Answer Summary
# ==========================================
print("\n--- Final Results ---")
print(f"Are the lowest two bands isolated? {is_isolated}")
print(f"Direct energy gap between lowest two bands: {min_gap:.4f}")
if is_isolated:
    print(f"1/2pi Tr G: {result_trG:.4f}")
else:
    print(f"1/2pi Tr G: N/A")
print(f"Kane-Mele time-reversal Z2 topology: {Z2_val}")
print(f"Can the set... be expressed...? {wannier_ans}")
```
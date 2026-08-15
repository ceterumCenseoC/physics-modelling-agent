
```python
import numpy as np
import scipy.linalg as la

# ==========================================
# 1. Model Parameters and Physical Constants
# ==========================================

# Physical Parameters
theta_deg = 3.5           # Twist angle in degrees
a0 = 3.52                 # Monolayer lattice constant in A
m_eff_ratio = 0.6         # m* / m_e
V = 16.5                  # Moire potential amplitude in meV
w = -18.8                 # Interlayer tunneling in meV
psi_deg = -105.9          # Potential phase in degrees

# Derived Calculation Constants
# Kinetic energy coefficient: hbar^2 / (2 * m*)
# Given constant 7619.96423 corresponds to hbar^2 / (2 * m_e) 
# The previous analysis identified a factor of 2 error in the text's formula 
# and clarifies that 7619.96 is proportional to hbar^2 / (2m_e).
# We use: kinetic_coeff = (hbar^2 / 2m_e) / (m*/m_e)
kinetic_coeff = 7619.96423 / m_eff_ratio

# Geometric Calculations
theta = np.deg2rad(theta_deg)
psi = np.deg2rad(psi_deg)

# Moire period a_M
aM = a0 / (2 * np.sin(theta / 2))

# Magnitude of reciprocal vector g1
g_mag = (4 * np.pi) / (np.sqrt(3) * aM)

# Vectors
def rotate(vector, angle):
    c, s = np.cos(angle), np.sin(angle)
    R = np.array([[c, -s], [s, c]])
    return np.dot(R, vector)

# g_1, q_1 definitions
g1 = np.array([g_mag, 0.0])
q1 = g_mag * np.array([0.0, 1.0/np.sqrt(3)])

# Generate g_i and q_i families
C3_rot = 2 * np.pi / 3
g_vecs = [rotate(g1, i * C3_rot) for i in range(3)]
q_vecs = [rotate(q1, i * C3_rot) for i in range(3)]

# Basis vectors for Brillouin Zone integration
b1 = g1
b2 = g1 + g_vecs[1]

# ==========================================
# 2. Basis Set Generation
# ==========================================

# Cutoff condition: |Q| < 4.1 * |b1|
cutoff_radius = 4.1 * np.linalg.norm(b1)

def get_Q_vectors(shift_vec):
    """
    Generate Q vectors satisfying:
    1. Q - shift_vec is a reciprocal lattice vector (n1*g1 + n2*g2).
    2. |Q| < cutoff_radius
    """
    Q_list = []
    
    # Search range for integer coefficients n1, n2
    limit = 6 
    for n1 in range(-limit, limit + 1):
        for n2 in range(-limit, limit + 1):
            # G = n1*g1 + n2*g2
            G_recip = n1 * g_vecs[0] + n2 * g_vecs[1]
            Q = shift_vec + G_recip
            
            if np.linalg.norm(Q) < cutoff_radius:
                Q_list.append(Q)
                
    # Filter unique vectors using floating point tolerance
    unique_Q = []
    seen = set()
    for q in Q_list:
        t_q = tuple(np.round(q, 8))
        if t_q not in seen:
            seen.add(t_q)
            unique_Q.append(q)
            
    return unique_Q

# Q sets for top (t) and bottom (b) layers
# Top: Q = q1 + G
Q_top = np.array(get_Q_vectors(q_vecs[0]))
# Bottom: Q = -q1 + G
Q_bottom = np.array(get_Q_vectors(-q_vecs[0]))

# Mapping for efficient lookup of basis indices
Q_top_map = {tuple(np.round(q, 8)): i for i, q in enumerate(Q_top)}
Q_bottom_map = {tuple(np.round(q, 8)): i for i, q in enumerate(Q_bottom)}

N_top = len(Q_top)
N_bottom = len(Q_bottom)
dim_H = N_top + N_bottom

print(f"Basis size: Bottom={N_bottom}, Top={N_top}, Total={dim_H}")

# ==========================================
# 3. Hamiltonian Construction
# ==========================================

L_grid = 60
N_k = L_grid * L_grid

# Momentum grid generation
# k = (l1/L - 1/2)*b1 + (l2/L - 1/2)*b2
l_vals = np.arange(L_grid)
weights = (l_vals / L_grid - 0.5)
ks_l1, ks_l2 = np.meshgrid(weights, weights)

ks_flat = np.zeros((N_k, 2))
ks_flat[:, 0] = ks_l1.flatten() * b1[0] + ks_l2.flatten() * b2[0]
ks_flat[:, 1] = ks_l1.flatten() * b1[1] + ks_l2.flatten() * b2[1]

# Prepare matrix containers
# We'll build the Hamiltonian using coo_matrix style logic then convert to dense for diagonalization
# Since dim_H is small (~300), dense matrices are fine.

# Precompute Tunneling connections (Interlayer)
# H_{bt} connects states b and t if Q_t - Q_b = q_i
tunneling_rows = []
tunneling_cols = []
tunneling_data = []

for qi in q_vecs:
    # For each bottom vector Qb, check if Qb + qi is in Top basis
    for ib, Qb in enumerate(Q_bottom):
        target_Qt = Qb + qi
        key = tuple(np.round(target_Qt, 8))
        
        if key in Q_top_map:
            it = Q_top_map[key]
            # Matrix element w
            # Row: Bottom index (0 to N_b-1)
            # Col: Top index (N_b to N_b+N_t-1)
            tunneling_rows.append(ib)
            tunneling_cols.append(N_bottom + it)
            tunneling_data.append(w)
            
            # Hermitian conjugate
            tunneling_rows.append(N_bottom + it)
            tunneling_cols.append(ib)
            tunneling_data.append(np.conj(w))

# Precompute Intralayer Potential connections (within the same layer)
# H connects Q to Q+g_i or Q-g_i
# We are looking for pairs (i, j) where Q_j = Q_i +/- g_k
# We can build these lists once to speed up the loop over k-points.

# Bottom Layer Potentials
pot_b_rows = []
pot_b_cols = []
pot_b_data = []

for g_vec in g_vecs:
    for i, Q in enumerate(Q_bottom):
        # Target Q + g
        target = Q + g_vec
        key = tuple(np.round(target, 8))
        if key in Q_bottom_map:
            j = Q_bottom_map[key]
            # Hamiltonian: 2V cos(g*r + psi) -> V exp(i psi) exp(i g r) + h.c.
            # Element <Q| exp(i g r) |Q+g> is 1.
            # So H[i, j] += V * exp(1j * psi)
            # Note: potential couples Q and Q+g.
            pot_b_rows.append(i)
            pot_b_cols.append(j)
            pot_b_data.append(V * np.exp(1j * psi))

# Top Layer Potentials
pot_t_rows = []
pot_t_cols = []
pot_t_data = []

for g_vec in g_vecs:
    for i, Q in enumerate(Q_top):
        # Target Q + g
        target = Q + g_vec
        key = tuple(np.round(target, 8))
        if key in Q_top_map:
            j = Q_top_map[key]
            # Hamiltonian: 2V cos(g*r - psi) -> V exp(-i psi) exp(i g r) + h.c.
            # So H[i, j] += V * exp(-1j * psi)
            pot_t_rows.append(i + N_bottom) # Add offset
            pot_t_cols.append(j + N_bottom)
            pot_t_data.append(V * np.exp(-1j * psi))

# ==========================================
# 4. Numerical Diagonalization
# ==========================================

eigenvalues = np.zeros((N_k, dim_H))
eigenvectors = np.zeros((N_k, dim_H, dim_H), dtype=complex)

print(f"Diagonalizing Hamiltonian for {N_k} k-points (dim {dim_H})...")

for i_k in range(N_k):
    k_vec = ks_flat[i_k]
    H = np.zeros((dim_H, dim_H), dtype=complex)
    
    # 1. Kinetic Energy: Diagonal in the basis
    # Bottom layer
    for idx, Q in enumerate(Q_bottom):
        k_minus_Q = k_vec - Q
        H[idx, idx] = kinetic_coeff * np.dot(k_minus_Q, k_minus_Q)
        
    # Top layer
    for idx, Q in enumerate(Q_top):
        k_minus_Q = k_vec - Q
        H[N_bottom + idx, N_bottom + idx] = kinetic_coeff * np.dot(k_minus_Q, k_minus_Q)
        
    # 2. Intralayer Potential
    # Use precomputed lists (these are symmetric, we add both upper/lower or just construct both)
    # The lists above store specific pairs. We can just add them.
    for r, c, d in zip(pot_b_rows, pot_b_cols, pot_b_data):
        H[r, c] += d
        H[c, r] += np.conj(d)
        
    for r, c, d in zip(pot_t_rows, pot_t_cols, pot_t_data):
        H[r, c] += d
        H[c, r] += np.conj(d)
        
    # 3. Interlayer Tunneling
    for r, c, d in zip(tunneling_rows, tunneling_cols, tunneling_data):
        H[r, c] += d
        
    # Diagonalize
    evals, evecs = la.eigh(H)
    
    eigenvalues[i_k] = evals
    eigenvectors[i_k] = evecs

# ==========================================
# 5. Compute Chern Numbers and Quantum Metric
# ==========================================

print("Calculating topological quantities...")

# Bands of interest: Top, 2nd highest, 3rd highest
# Indices are dim_H - 1, dim_H - 2, dim_H - 3
band_indices = [dim_H - 1, dim_H - 2, dim_H - 3]

# Integrals
# dk vectors
dk1 = b1 / L_grid
dk2 = b2 / L_grid

# Area element
# BZ Area = |b1 x b2| in 2D it is det([b1, b2])
area_bz = np.abs(b1[0]*b2[1] - b1[1]*b2[0])
dA = area_bz / (L_grid**2)

chern_numbers = [0, 0, 0]
tr_G_metric = 0.0

# We iterate over bands to compute Chern numbers
# We compute metric only for the top band (index dim_H - 1)

for b_idx, band_n in enumerate(band_indices):
    curr_chern = 0.0
    curr_metric = 0.0
    
    # Pre-fetch eigenvectors for the band to avoid indexing 3D array repeatedly
    # Not strictly necessary but clearer
    vecs = np.zeros((L_grid, L_grid, dim_H), dtype=complex)
    for l1 in range(L_grid):
        for l2 in range(L_grid):
            idx = l1 * L_grid + l2
            vecs[l1, l2] = eigenvectors[idx, :, band_n]
            
    for l1 in range(L_grid):
        for l2 in range(L_grid):
            # Periodic boundary conditions
            l1_p1 = (l1 + 1) % L_grid
            l2_p1 = (l2 + 1) % L_grid
            
            # Eigenvectors at corners of the plaquette
            # U1 = link in direction 1 (b1)
            # U2 = link in direction 2 (b2)
            
            u_k = vecs[l1, l2]
            u_kpb1 = vecs[l1_p1, l2]
            u_kb2 = vecs[l1, l2_p1]
            u_kpb1pb2 = vecs[l1_p1, l2_p1]
            
            # Link variables
            # U_mu = <u(k)|u(k+dmu)> / |<u(k)|u(k+dmu)>|
            ov_1 = np.vdot(u_k, u_kpb1)
            ov_2 = np.vdot(u_k, u_kb2)
            ov_1_adj = np.vdot(u_kb2, u_kpb1pb2) # U_1 at k+b2
            ov_2_adj = np.vdot(u_kpb1, u_kpb1pb2) # U_2 at k+b1
            
            norm_1 = np.abs(ov_1)
            norm_2 = np.abs(ov_2)
            norm_1_adj = np.abs(ov_1_adj)
            norm_2_adj = np.abs(ov_2_adj)
            
            # Avoid division by zero (should not happen with this L and basis)
            if norm_1 == 0 or norm_2 == 0 or norm_1_adj == 0 or norm_2_adj == 0:
                # This implies a degeneracy or numerical issue. Skip or handle.
                continue
                
            U1 = ov_1 / norm_1
            U2 = ov_2 / norm_2
            U1b2 = ov_1_adj / norm_1_adj
            U2b1 = ov_2_adj / norm_2_adj
            
            # Chern number contribution (Field strength)
            # F12 = Im ln ( U1(k) U2(k+b1) U1(k+b2)^-1 U2(k)^-1 )
            # Note: U1^-1 = U1* if normalized
            prod = U1 * U2b1 * np.conj(U1b2) * np.conj(U2)
            F12 = np.imag(np.log(prod))
            curr_chern += F12
            
            # Quantum Metric (Only for top band)
            if b_idx == 0:
                # g_ij approx = (1/2) * (delta_ij - Re(U_i U_j*))
                # Tr g = g_xx + g_yy approx sum_mu (1 - |U_mu|^2) / (dk_mu^2)
                # Here dk vectors are not orthogonal, so |dk|^2 is used
                term1 = (1.0 - norm_1**2) / np.dot(dk1, dk1)
                term2 = (1.0 - norm_2**2) / np.dot(dk2, dk2)
                curr_metric += (term1 + term2) * dA * 0.5

    chern_numbers[b_idx] = int(np.round(curr_chern / (2.0 * np.pi)))
    if b_idx == 0:
        tr_G_metric = curr_metric

print("\n============================================")
print(f"Results for theta = {theta_deg} degrees:")
print("============================================")
print("Chern Numbers of Top Three Bands:")
print(f"Top Band (C1): {chern_numbers[0]}")
print(f"2nd Band (C2): {chern_numbers[1]}")
print(f"3rd Band (C3): {chern_numbers[2]}")

print("\nQuantum Metric Trace (Tr G) for Top Electron Band:")
print(f"{tr_G_metric:.2f}")
```
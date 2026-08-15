```python
import numpy as np
import matplotlib.pyplot as plt
from scipy.linalg import eigh
from math import pi, sqrt

# ==========================================
# 1. Model Parameters and Lattice Setup
# ==========================================

# Physical Parameters
# 2m = 1 => Mass m = 0.5
# Hamiltonian coefficient for kinetic term |k|^2/(2m) is 1.0
m_factor = 1.0
lambda_val = 1.9
delta1 = 0.12
delta2 = 0.005
delta3 = 0.05
delta4 = 0.01

# Pauli Matrices
sigma_x = np.array([[0, 1], [1, 0]], dtype=complex)
sigma_y = np.array([[0, -1j], [1j, 0]], dtype=complex)
iden_2x2 = np.eye(2, dtype=complex)

# Reciprocal Lattice Definition
# Primitive vectors:
# b1 = (0, 1)
# b2 = (sqrt(3)/2, 1/2)
b1 = np.array([0.0, 1.0])
b2 = np.array([sqrt(3)/2, 0.5])

# generate_shortest_Rs logic
# We need the 43 shortest reciprocal lattice vectors.
# Combinations of n1*b1 + n2*b2.
def generate_R_vectors(n_vecs):
    # Range of integer coefficients needed
    limit = 6 
    R_list = []
    # Mapping from vector to index for potential construction
    R_dict = {}
    
    count = 0
    for n1 in range(-limit, limit + 1):
        for n2 in range(-limit, limit + 1):
            vec = n1 * b1 + n2 * b2
            if count < n_vecs:
                R_list.append(vec)
                count += 1
            else:
                # Lazily collect all to find min distance, 
                # but we can sort a generated list.
                pass
                
    # Actually, just generate a sufficiently large list and sort
    full_list = []
    for n1 in range(-limit, limit + 1):
        for n2 in range(-limit, limit + 1):
            vec = n1 * b1 + n2 * b2
            sq_norm = np.dot(vec, vec)
            full_list.append((sq_norm, vec))
            
    # Sort by squared norm
    full_list.sort(key=lambda x: x[0])
    
    # Extract the first n_vecs
    Rs = [x[1] for x in full_list[:n_vecs]]
    return Rs

# Get 43 shortest vectors
reciprocal_vectors = generate_R_vectors(43)
N_vecs = 43
dim_H = 2 * N_vecs  # 2 spin components per plane wave

# Generate g-vectors for the Potential
# Rotation operator C3 (120 degrees)
# v = (x, y) -> (-x/2 - sqrt(3)y/2, sqrt(3)x/2 - y/2)
def rotate_c3(v):
    x, y = v
    return np.array([-0.5*x - sqrt(3)*y/2, sqrt(3)*x/2 - 0.5*y])

# g_i^(1) = C3^(i-1) b1
g1_list = []
curr = b1.copy()
for _ in range(3):
    g1_list.append(curr)
    curr = rotate_c3(curr)
    
# g_i^(2) = C3^(i-1) (b1 + b2)
g2_list = []
curr = b1 + b2
for _ in range(3):
    g2_list.append(curr)
    curr = rotate_c3(curr)

# ==========================================
# 2. Hamiltonian Construction
# ==========================================

def get_hamiltonian(k_vec, Rs):
    """
    Constructs the Bloch Hamiltonian H(k) as a 2N x 2N matrix.
    """
    H = np.zeros((dim_H, dim_H), dtype=complex)
    
    # 1. Pre-compute Potential Map
    # V(r) potential couples R to R' if R - R' = G (reciprocal vector of potential)
    # V_fourier(G) = coefficient.
    # The matrix element is V * Identity_spin.
    # We need a lookup for V_coeff at vector G = R_i - R_j.
    
    # V_map keys: scaled integer coordinates of vector G
    V_map = {}
    
    # Helper to round and key
    # scale factor to avoid float precision issues
    scale = 4.0 
    
    def add_to_map(vec, coeff):
        key = (int(round(vec[0]*scale)), int(round(vec[1]*scale)))
        V_map[key] = coeff

    # Terms from Delta1, Delta2 (on g_i^(1))
    # Potential term has Delta1 + i Delta2 for e^(i g.r)
    # And Delta1 - i Delta2 for e^(-i g.r) -> G = -g
    for g in g1_list:
        add_to_map(g, delta1 + 1j*delta2)
        add_to_map(-g, delta1 - 1j*delta2)
        
    # Terms from Delta3, Delta4 (on g_i^(2))
    for g in g2_list:
        add_to_map(g, delta3 + 1j*delta4)
        add_to_map(-g, delta3 - 1j*delta4)
        
    # Fill Hamiltonian
    for i in range(N_vecs):
        Ri = Rs[i]
        k_plus_Ri = k_vec + Ri
        
        # Diagonal Block (R_j = R_i)
        # Kinetic: |k+R|^2
        # SOC: lambda (Ky sigx - Kx sigy)
        E_kin = np.dot(k_plus_Ri, k_plus_Ri) * m_factor
        H_soc_block = lambda_val * (k_plus_Ri[1]*sigma_x - k_plus_Ri[0]*sigma_y)
        H_diag = E_kin * iden_2x2 + H_soc_block
        
        H[2*i : 2*i+2, 2*i : 2*i+2] += H_diag
        
        # Off-diagonal Blocks (R_j != R_i)
        # Coupling is via potential V(G) where G = R_i - R_j
        # We search for Rj such that R_i - R_j is in V_map
        # While constructing, iterating over all Rj is expensive if done naively.
        # But N=43 is small. 43*43 check is fine.
        for j in range(N_vecs):
            if i == j: continue
            
            Rj = Rs[j]
            G_vec = Ri - Rj
            key = (int(round(G_vec[0]*scale)), int(round(G_vec[1]*scale)))
            
            if key in V_map:
                V_coeff = V_map[key]
                # V_coeff is scalar, acts as Identity in spin space
                # H[ i_block, j_block ] += V * I
                H[2*i : 2*i+2, 2*j : 2*j+2] += V_coeff * iden_2x2
                
    return H

# ==========================================
# 3. Diagonalization and Band Analysis
# ==========================================

# Mesh generation: 60x60 Hexagonal symmetric mesh
# Primitive coordinates (u, v) where 0 <= u,v < 1
N_mesh = 60
k_points = []
uv_indices = []
for i in range(N_mesh):
    for j in range(N_mesh):
        u = i / N_mesh
        v = j / N_mesh
        k = u * b1 + v * b2
        k_points.append(k)
        uv_indices.append((i, j))

# Convert to numpy arrays
k_points = np.array(k_points)

# Storage
eigenvalues = []   # List of arrays
eigenvectors = []  # List of arrays
min_gap = float('inf')
isolated_bands = True

print(f"Starting diagonalization for {len(k_points)} k-points...")

for k_idx, k in enumerate(k_points):
    H_k = get_hamiltonian(k, reciprocal_vectors)
    # scipy.linalg.eigh returns sorted eigenvalues
    vals, vecs = eigh(H_k)
    
    eigenvalues.append(vals)
    eigenvectors.append(vecs)
    
    # Gap between 2nd (idx 1) and 3rd (idx 2) band
    gap_val = vals[2] - vals[1]
    if gap_val < min_gap:
        min_gap = gap_val
        
# Isolated check: if min_gap is positive (significant)
if min_gap <= 1e-9:
    isolated_bands = False
    # Avoid doing metric/Z2 if not isolated
    print("WARNING: Bands are NOT isolated.")
else:
    print(f"Bands are isolated. Min Gap: {min_gap:.6f}")

# ==========================================
# 4. Quantum Metric Trace Calculation
# ==========================================

tr_G_integral = 0.0

if isolated_bands:
    print("Calculating Quantum Metric Trace...")
    # Calculate derivatives of H numerically
    dk = 1e-6
    
    for idx, k in enumerate(k_points):
        # Get eigenvectors for lowest 2 bands (columns 0 and 1)
        # Shape: (dim_H, 2)
        u_occ = eigenvectors[idx][:, :2]
        E_occ = eigenvalues[idx][:2]
        
        # Numerical Derivative H_x
        k_dx = np.array([dk, 0.0])
        H_p = get_hamiltonian(k + k_dx, reciprocal_vectors)
        H_m = get_hamiltonian(k - k_dx, reciprocal_vectors)
        dH_dx = (H_p - H_m) / (2*dk)
        
        # Numerical Derivative H_y
        k_dy = np.array([0.0, dk])
        H_p = get_hamiltonian(k + k_dy, reciprocal_vectors)
        H_m = get_hamiltonian(k - k_dy, reciprocal_vectors)
        dH_dy = (H_p - H_m) / (2*dk)
        
        # Sum over unoccupied bands (n=3 to N)
        # | <u_m| dH |u_n> |^2 / (Em - En)^2
        # Precompute <un|dH|uo> matrices
        # u_occ: Dim x 2
        # u_unocc: Dim x (M-2)
        
        u_all = eigenvectors[idx]
        u_unocc = u_all[:, 2:]
        E_unocc = eigenvalues[idx][2:]
        
        # Projection matrices
        # P_un_occ_dH_occ = u_unocc^H @ dH @ u_occ
        # Size: (Unocc, 2)
        Mx = u_unocc.conj().T @ dH_dx @ u_occ
        My = u_unocc.conj().T @ dH_dy @ u_occ
        
        # Denominator: E_n - E_m
        # Rows: E_unocc (broadcast), Cols: E_occ (broadcast)
        D = E_unocc[:, np.newaxis] - E_occ[np.newaxis, :]
        
        # Mask small denominators just in case
        D[np.abs(D) < 1e-10] = 1e-10
        
        # The formula:
        # Tr(g) = Re Sum_{m occ, n unocc} ( |dx_mn|^2 + |dy_mn|^2 ) / (En - Em)^2
        # This is Sum over 2 components of |M|^2 / D^2
        
        # efficient sum
        term = np.sum((np.abs(Mx)**2 + np.abs(My)**2) / (D**2))
        tr_G_integral += term
        
    # Integration area
    # BZ Area = |det( [b1, b2] )|
    # Matrix cols are b1, b2
    bz_vol = np.abs(b1[0]*b2[1] - b1[1]*b2[0])
    
    # Integral: Sum * (Area / N)
    integral_val = tr_G_integral * (bz_vol / len(k_points))
    
    # Result normalized by 2pi
    res_metric = integral_val / (2 * pi)
else:
    res_metric = None

# ==========================================
# 5. Kane-Mele Z2 Topology
# ==========================================

# Using Fukui-Hatsugai method for Z2 on discretized BZ
Z2_inv = None

if isolated_bands:
    print("Calculating Z2 Topology...")
    
    N = N_mesh
    
    # Define overlap matrices Ux, Uy
    # U_mu(n) = det( <u_m(n)|u_n(n+mu)> ) / |det|
    # Determine phases
    
    def get_vecs_at(i, j):
        # Convert u,v indices to flat list index
        # k_points is ordered i then j (mostly)
        flat_idx = i * N + j
        return eigenvectors[flat_idx][:, :2]
        
    Ux = np.zeros((N, N), dtype=complex)
    Uy = np.zeros((N, N), dtype=complex)
    
    for i in range(N):
        for j in range(N):
            u = get_vecs_at(i, j)
            
            # x neighbor: (i, j+1)
            u_x = get_vecs_at(i, (j+1)%N)
            # y neighbor: (i+1, j)
            u_y = get_vecs_at((i+1)%N, j)
            
            # Overlaps
            O_x = u.conj().T @ u_x
            O_y = u.conj().T @ u_y
            
            det_x = np.linalg.det(O_x)
            det_y = np.linalg.det(O_y)
            
            Ux[i,j] = det_x / (np.abs(det_x) + 1e-16)
            Uy[i,j] = det_y / (np.abs(det_y) + 1e-16)
            
    # Field strength F_12
    # F_12 = (1/2pi i) log( Ux(i,j) Uy(i+1,j) Ux(i,j+1)^-1 Uy(i,j)^-1 )
    # branch cut for log: principal (-pi, pi]
    
    Z2_count = 0
    
    for i in range(N // 2): # Sum over half BZ (i = 0 to N/2 - 1)
        for j in range(N):
            
            val = Ux[i, j] * Uy[(i+1)%N, j] * (1.0/Ux[i, (j+1)%N]) * (1.0/Uy[i, j])
            
            # Phase
            phase = np.log(val) / 1j
            
            # Map phase to (-pi, pi]
            while phase <= -pi: phase += 2*pi
            while phase > pi: phase -= 2*pi
            
            f12 = phase / (2*pi)
            
            # Z2 sum
            Z2_count += f12
            
    # Z2 invariant is Z2_count mod 2 (approximately integer)
    # Result should be 0 or 1.
    Z2_inv = int(round(abs(Z2_count) % 2))
    
else:
    Z2_inv = "N/A"

# ==========================================
# 6. Final Classification
# ==========================================

# Wannier Function Criteria
# Requires Isolated AND Z2=0
wannier_localized = False
if isolated_bands and Z2_inv == 0:
    wannier_localized = True
elif isolated_bands and Z2_inv == 1:
    wannier_localized = False # Obstructed
else:
    wannier_localized = False # Not isolated

# ==========================================
# 7. Visualization (Optional but good for verification)
# ==========================================
# Generate band structure path Gamma-K-M-Gamma
# Gamma (0,0)
# K (2/3, 1/3)
# M (1/2, 0)
# Define path in u,v coordinates
path_segments = [
    (np.linspace(0, 2.0/3, 50), np.linspace(0, 1.0/3, 50)), # Gamma-K
    (np.linspace(2.0/3, 0.5, 50), np.linspace(1.0/3, 0, 50)), # K-M
    (np.linspace(0.5, 0, 50), np.zeros(50))                # M-Gamma
]

band_energies = []
ticks = []
tick_pos = []
count = 0
for u_seg, v_seg in path_segments:
    for u, v in zip(u_seg, v_seg):
        # Find closest k or interpolate? Since 60x60, we can just pick nearest.
        # Or calc exactly. Recalculating is safer for plotting.
        k = u*b1 + v*b2
        H = get_hamiltonian(k, reciprocal_vectors)
        vals, _ = eigh(H)
        band_energies.append(vals)
        count += 1
    tick_pos.append(count-1)

band_energies = np.array(band_energies)

# Plotting is tricky in headless, but we can save it if needed.
# For this task, we focus on text output but include the code to plot.

# ==========================================
# 8. Output Results
# ==========================================

print("\n--- Final Report ---")
print(f"1. Are the lowest two bands isolated?")
print(f"   {isolated_bands}")
print(f"2. Direct energy gap between lowest two bands:")
print(f"   {min_gap:.4f}")
print(f"3. 1/(2pi) Tr G:")
if res_metric is not None:
    print(f"   {res_metric:.4f}")
else:
    print(f"   N/A")
print(f"4. Kane-Mele time-reversal Z2 topology:")
print(f"   {Z2_inv}")
print(f"5. Can the set... be expressed in terms of two exponentially localized Wannier functions?")
print(f"   {wannier_localized}")

# Ensure the code ends cleanly
```
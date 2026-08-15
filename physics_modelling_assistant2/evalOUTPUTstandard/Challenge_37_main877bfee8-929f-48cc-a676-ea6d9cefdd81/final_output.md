```python

import numpy as np
from scipy.linalg import eigh
from math import pi, sqrt

# ==========================================
# 1. Model Parameters and Lattice Setup
# ==========================================

# Physical parameters
# Hamiltonian terms: -1/(2m) del^2 + lambda(...) + Potential deltas
# 2m = 1 => m = 0.5
# The coefficient in front of k^2 in the diagonal is 1/(2m) = 1.0.
m_factor = 1.0
lambda_val = 1.9
delta1 = 0.12
delta2 = 0.005
delta3 = 0.05
delta4 = 0.01

# Pauli matrices
sigma_x = np.array([[0, 1], [1, 0]], dtype=complex)
sigma_y = np.array([[0, -1j], [1j, 0]], dtype=complex)
iden_2x2 = np.eye(2, dtype=complex)

# Reciprocal Lattice Definition
# b1 = (0, 1)
# b2 = C6 * b1 = (sqrt(3)/2, 1/2)
b1 = np.array([0.0, 1.0])
b2 = np.array([sqrt(3)/2, 0.5])

# Generate the 43 shortest reciprocal lattice vectors R
def generate_R_vectors(n_vecs):
    # Search range sufficient to find 43 shortest
    limit = 6 
    full_list = []
    for n1 in range(-limit, limit + 1):
        for n2 in range(-limit, limit + 1):
            vec = n1 * b1 + n2 * b2
            sq_norm = np.dot(vec, vec)
            # Store (norm, vec)
            full_list.append((sq_norm, vec))
            
    # Sort by squared norm
    full_list.sort(key=lambda x: x[0])
    
    # Extract the first n_vecs
    Rs = [x[1] for x in full_list[:n_vecs]]
    return Rs

reciprocal_vectors = generate_R_vectors(43)
N_vecs = 43
dim_H = 2 * N_vecs  # Dimension of Hamiltonian: 2 spins * 43 plane waves

# Generate g-vectors for the Potential V(r)
# Rotations C3 (120 degrees)
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
    H = np.zeros((dim_H, dim_H), dtype=complex)
    
    # 1. Potential Map
    # We lookup V_coeff where G = R_i - R_j
    V_map = {}
    scale = 4.0 # for floating point key precision
    
    def add_to_map(vec_key, coeff):
        key = (int(round(vec_key[0]*scale)), int(round(vec_key[1]*scale)))
        V_map[key] = coeff

    # Delta1 + i Delta2 terms (g_i^(1))
    for g in g1_list:
        add_to_map(g, delta1 + 1j*delta2)
        add_to_map(-g, delta1 - 1j*delta2)
        
    # Delta3 + i Delta4 terms (g_i^(2))
    for g in g2_list:
        add_to_map(g, delta3 + 1j*delta4)
        add_to_map(-g, delta3 - 1j*delta4)
        
    # 2. Fill Hamiltonian
    for i in range(N_vecs):
        Ri = Rs[i]
        k_plus_Ri = k_vec + Ri
        
        # Diagonal Block (Kinetic + SOC)
        E_kin = np.dot(k_plus_Ri, k_plus_Ri) * m_factor
        H_soc_block = lambda_val * (k_plus_Ri[1]*sigma_x - k_plus_Ri[0]*sigma_y)
        H_diag = E_kin * iden_2x2 + H_soc_block
        H[2*i : 2*i+2, 2*i : 2*i+2] += H_diag
        
        # Off-diagonal Blocks (Potential)
        for j in range(N_vecs):
            if i == j: continue
            Rj = Rs[j]
            G_vec = Ri - Rj
            key = (int(round(G_vec[0]*scale)), int(round(G_vec[1]*scale)))
            
            if key in V_map:
                V_coeff = V_map[key]
                H[2*i : 2*i+2, 2*j : 2*j+2] += V_coeff * iden_2x2
                
    return H

# ==========================================
# 3. Diagonalization and Band Analysis
# ==========================================

N_mesh = 60
k_points = []
# Generating uniform mesh in primitive coordinates (u, v)
for i in range(N_mesh):
    for j in range(N_mesh):
        u = i / N_mesh
        v = j / N_mesh
        k = u * b1 + v * b2
        k_points.append(k)

k_points = np.array(k_points)
N_k = len(k_points)

eigenvalues = []   # Stores eigenvalues for each k
eigenvectors = []  # Stores eigenvectors for each k

print("Diagonalizing Hamiltonian...")
min_gap = float('inf')

# Store k-points for later gap location finding
k_min_gap = None

for idx, k in enumerate(k_points):
    H_k = get_hamiltonian(k, reciprocal_vectors)
    vals, vecs = eigh(H_k)
    
    eigenvalues.append(vals)
    eigenvectors.append(vecs)
    
    # Check direct gap between 2nd (idx 1) and 3rd (idx 2) band
    gap_val = vals[2] - vals[1]
    if gap_val < min_gap:
        min_gap = gap_val
        k_min_gap = k

# Check Isolation
tolerance = 1e-5
if min_gap > tolerance:
    is_isolated = "Yes"
else:
    is_isolated = "No"

# ==========================================
# 4. Quantum Metric Trace Calculation
# ==========================================

tr_G_over_2pi_res = "N/A"

if is_isolated == "Yes":
    print("Calculating Quantum Metric...")
    dk = 1e-6
    sum_g_trace = 0.0
    
    for idx, k in enumerate(k_points):
        u_occ = eigenvectors[idx][:, :2] # Occupied states (N x 2)
        E_occ = eigenvalues[idx][:2]
        
        u_unocc = eigenvectors[idx][:, 2:] # Unoccupied states
        E_unocc = eigenvalues[idx][2:]
        
        # Derivatives dH/dkx, dH/dky
        k_dx = np.array([dk, 0.0])
        k_dy = np.array([0.0, dk])
        
        H_k_dx = get_hamiltonian(k + k_dx, reciprocal_vectors)
        H_k_dy = get_hamiltonian(k + k_dy, reciprocal_vectors)
        H_k_mx = get_hamiltonian(k - k_dx, reciprocal_vectors)
        H_k_my = get_hamiltonian(k - k_dy, reciprocal_vectors)
        
        dH_dx = (H_k_dx - H_k_mx) / (2*dk)
        dH_dy = (H_k_dy - H_k_my) / (2*dk)
        
        # Sum over states formula
        # <un| dH |uo>
        Mx = u_unocc.conj().T @ dH_dx @ u_occ
        My = u_unocc.conj().T @ dH_dy @ u_occ
        
        D = E_unocc[:, np.newaxis] - E_occ[np.newaxis, :]
        # Avoid div by zero
        D[np.abs(D) < 1e-10] = 1e-10
        
        term_sum = np.sum((np.abs(Mx)**2 + np.abs(My)**2) / (D**2))
        sum_g_trace += term_sum
        
    # Integrate: Sum * (Area_BZ / N_k) * 1/(2pi)
    bz_area = np.abs(np.linalg.det(np.array([b1, b2]).T))
    integral_val = sum_g_trace * (bz_area / N_k)
    tr_G_over_2pi_res = integral_val / (2 * pi)

# ==========================================
# 5. Kane-Mele Z2 Topology
# ==========================================

Z2_res = "N/A"

if is_isolated == "Yes":
    print("Calculating Z2 Topology (Fukui-Hatsugai)...")
    N = N_mesh
    
    # Helper to get eigenvectors at grid (i, j)
    def get_u(i, j):
        return eigenvectors[i * N + j][:, :2]
        
    # Calculate Ux, Uy fields
    Ux = np.zeros((N, N), dtype=complex)
    Uy = np.zeros((N, N), dtype=complex)
    
    for i in range(N):
        for j in range(N):
            u = get_u(i, j)
            ux = get_u(i, (j+1)%N)
            uy = get_u((i+1)%N, j)
            
            Ox = u.conj().T @ ux
            Oy = u.conj().T @ uy
            
            detx = np.linalg.det(Ox)
            dety = np.linalg.det(Oy)
            
            Ux[i,j] = detx / (np.abs(detx) + 1e-15)
            Uy[i,j] = dety / (np.abs(dety) + 1e-15)
            
    # Sum field strength over half BZ
    z2_accum = 0.0
    for i in range(N // 2):
        for j in range(N):
            # Plaquette
            val = Ux[i, j] * Uy[(i+1)%N, j] * (1.0/Ux[i, (j+1)%N]) * (1.0/Uy[i, j])
            
            phase = np.log(val) / 1j
            # Principal branch [-pi, pi)
            # Note: numpy.log handles phase cut at -pi, but formula often requires careful range.
            # Implementation usually takes log and adjusts.
            while phase <= -pi: phase += 2*pi
            while phase > pi: phase -= 2*pi
            
            f12 = phase / (2*pi)
            z2_accum += f12
            
    # Z2 invariant is sum mod 2
    # Due to numerical errors, round to nearest integer
    z2_idx = int(round(abs(z2_accum) % 2))
    if z2_idx == 0:
        Z2_res = "Trivial"
    else:
        Z2_res = "Nontrivial"

# ==========================================
# 6. Wannier Localization
# ==========================================

wannier_res = "N/A"
if is_isolated == "Yes":
    if Z2_res == "Trivial":
        wannier_res = "Yes"
    else:
        wannier_res = "No"
else:
    wannier_res = "No"

# ==========================================
# 7. Output Formatting
# ==========================================

# Format Gap
gap_str = f"{min_gap:.4f}" if is_isolated == "Yes" else "N/A"
# Format Metric
metric_str = f"{float(tr_G_over_2pi_res):.4f}" if tr_G_over_2pi_res != "N/A" else "N/A"

result_tuple = (is_isolated, gap_str, metric_str, Z2_res, wannier_res)

print(result_tuple)

```
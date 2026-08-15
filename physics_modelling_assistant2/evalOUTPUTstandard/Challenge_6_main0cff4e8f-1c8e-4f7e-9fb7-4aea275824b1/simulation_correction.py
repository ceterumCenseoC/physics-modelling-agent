```python
import numpy as np
import matplotlib.pyplot as plt
from scipy.linalg import eigh

# ---------------------------------------------------------
# 1. Configuration and Constants
# ---------------------------------------------------------

# Grid parameters
L = 60  # mesh size
N_bands_to_compute = -1 # Compute all available bands in basis
N_bands_top = 3         # Number of top bands to analyze for Chern number
Target_band_idx = -1    # Index for top electron band (-1 is the highest energy band)

# Physical Constants
# hbar^2 / (2m*) in units meV * Angstrom^2.
# Given constant 7619.96423 corresponds to Rydbergs (Ha*a0^2) converted to meV*A^2.
# 1 Ha * a0^2 approx 7.6 eV*A^2 = 7600 meV*A^2.
kinetic_const_meV_A2 = 7619.96423 

# Model Parameters
# Values from Wu et al. (2019)
theta_deg = 3.5
m_star_ratio = 0.6          # m* relative to m_e
V = 16.5                   # meV
psi_deg = -105.9           # degrees
w = -18.8                  # meV
a0 = 3.52                  # Angstrom

# Derived parameters
theta = np.deg2rad(theta_deg)
psi = np.deg2rad(psi_deg)

# Moire lattice constant a_M
a_M = a0 / (2 * np.sin(theta / 2.0))

# Reciprocal lattice vectors g_i
# g1 = (4*pi)/(sqrt(3)*a_M) * (1, 0)
g_mag = (4 * np.pi) / (np.sqrt(3) * a_M)
g1 = np.array([g_mag, 0.0])

# Rotation matrices
def C3(v):
    # Rotate by 120 degrees (2pi/3)
    c = np.cos(2*np.pi/3)
    s = np.sin(2*np.pi/3)
    R = np.array([[c, -s], [s, c]])
    return np.dot(R, v)

# Generate g_i and q_i
g_vecs = [g1, C3(g1), C3(C3(g1))]
# q1 = |g1| * (0, 1/sqrt(3))
q1 = np.array([0.0, g_mag / np.sqrt(3)])
q_vecs = [q1, C3(q1), C3(C3(q1))]

# Reciprocal lattice basis vectors for BZ
b1 = g1
b2 = g1 + g_vecs[1] # g2
# Check area
BZ_area = np.abs(np.cross(b1, b2))

# Basis cutoff
# |Q| < 4.1 |b1|
cutoff_radius = 4.1 * np.linalg.norm(b1)

# ---------------------------------------------------------
# 2. Plane Wave Basis Generation
# ---------------------------------------------------------

def get_basis_vectors(layer):
    """Generate basis vectors Q for a given layer."""
    basis = []
    # Limit scan range. Since cutoff ~ 4 unit cells and we are near origin +/- q, 
    # scanning +/- 5 integer steps is sufficient.
    limit = 6 
    for n1 in range(-limit, limit + 1):
        for n2 in range(-limit, limit + 1):
            # Reciprocal lattice vector G
            G = n1 * g1 + n2 * g_vecs[1]
            
            if layer == 't':
                # Condition: Q - q1 = G  => Q = G + q1
                Q = G + q1
            else: # 'b'
                # Condition: Q + q1 = G  => Q = G - q1
                Q = G - q1
            
            if np.linalg.norm(Q) < cutoff_radius:
                basis.append(Q)
                
    # Deduplicate
    unique_basis = []
    seen = set()
    for q in basis:
        t = (round(q[0], 6), round(q[1], 6))
        if t not in seen:
            seen.add(t)
            unique_basis.append(q)
            
    return np.array(unique_basis)

Q_basis_t = get_basis_vectors('t')
Q_basis_b = get_basis_vectors('b')

print(f"Basis size (Top): {len(Q_basis_t)}")
print(f"Basis size (Bottom): {len(Q_basis_b)}")
print(f"Total basis size: {len(Q_basis_t) + len(Q_basis_b)}")

# Combine basis
Nt = len(Q_basis_t)
Nb = len(Q_basis_b)
dim = Nt + Nb

# Pre-compute potential matrix elements to speed up construction
# We map basis vectors to indices for fast lookup
def build_index_map(basis):
    mapping = {}
    for idx, q in enumerate(basis):
        t = (round(q[0], 6), round(q[1], 6))
        mapping[t] = idx
    return mapping

idx_map_t = build_index_map(Q_basis_t)
idx_map_b = build_index_map(Q_basis_b)

# ---------------------------------------------------------
# 3. Hamiltonian Construction
# ---------------------------------------------------------

def construct_hamiltonian(k_vec):
    """Construct Hamiltonian matrix at momentum k."""
    H = np.zeros((dim, dim), dtype=complex)
    
    # 1. Diagonal blocks: Kinetic + Potential
    
    # Precompute kinetic energies
    # Top
    for i, Q in enumerate(Q_basis_t):
        k_minus_Q = k_vec - Q
        H[i, i] += (kinetic_const_meV_A2 / m_star_ratio) * np.dot(k_minus_Q, k_minus_Q)
        
        # Potential V (Top layer phase +psi)
        # Terms: V * exp(-i psi) for Q -> Q+g
        #        V * exp(+i psi) for Q -> Q-g
        for g in g_vecs:
            # Q -> Q + g
            Q_plus = Q + g
            t = (round(Q_plus[0], 6), round(Q_plus[1], 6))
            if t in idx_map_t:
                H[idx_map_t[t], i] += V * np.exp(-1j * psi)
            
            # Q -> Q - g
            Q_minus = Q - g
            t = (round(Q_minus[0], 6), round(Q_minus[1], 6))
            if t in idx_map_t:
                H[idx_map_t[t], i] += V * np.exp(1j * psi)

    offset = Nt
    
    # Bottom
    for idx_b, Q in enumerate(Q_basis_b):
        row = offset + idx_b
        k_minus_Q = k_vec - Q
        H[row, row] += (kinetic_const_meV_A2 / m_star_ratio) * np.dot(k_minus_Q, k_minus_Q)
        
        # Potential V (Bottom layer phase -psi)
        # Terms: V * exp(+i psi) for Q -> Q+g  (from e^{-i(g.r-psi)})
        #        V * exp(-i psi) for Q -> Q-g  (from e^{i(g.r-psi)})
        for g in g_vecs:
            Q_plus = Q + g
            t = (round(Q_plus[0], 6), round(Q_plus[1], 6))
            if t in idx_map_b:
                H[offset + idx_map_b[t], row] += V * np.exp(1j * psi)
            
            Q_minus = Q - g
            t = (round(Q_minus[0], 6), round(Q_minus[1], 6))
            if t in idx_map_b:
                H[offset + idx_map_b[t], row] += V * np.exp(-1j * psi)

    # 2. Off-diagonal blocks: Tunneling
    
    # Top to Bottom (H_tb)
    # Coupling w for Q_t -> Q_b = Q_t + q
    for q in q_vecs:
        for i_t, Q_t in enumerate(Q_basis_t):
            Q_b_target = Q_t + q
            t = (round(Q_b_target[0], 6), round(Q_b_target[1], 6))
            if t in idx_map_b:
                H[i_t, offset + idx_map_b[t]] += w
                
    # Bottom to Top (H_bt)
    # Coupling w for Q_b -> Q_t = Q_b - q
    for q in q_vecs:
        for i_b, Q_b in enumerate(Q_basis_b):
            Q_t_target = Q_b - q
            t = (round(Q_t_target[0], 6), round(Q_t_target[1], 6))
            if t in idx_map_t:
                H[offset + i_b, idx_map_t[t]] += w # w is real in this model
                    
    return H

# ---------------------------------------------------------
# 4. Solver and Analysis Functions
# ---------------------------------------------------------

def get_k_mesh(L):
    """Generate k-mesh grid points."""
    ks = []
    for l1 in range(L):
        for l2 in range(L):
            k = ((l1 / L) - 0.5) * b1 + ((l2 / L) - 0.5) * b2
            ks.append(k)
    return np.array(ks)

def compute_bands_and_eigvecs(ks):
    """Diagonalize Hamiltonian for all k points."""
    N_k = len(ks)
    energies = np.zeros((N_k, dim))
    eigvecs = np.zeros((N_k, dim), dtype=complex)
    
    print("Diagonalizing Hamiltonian...")
    for i, k in enumerate(ks):
        H = construct_hamiltonian(k)
        vals, vecs = eigh(H) # Ascending order
        energies[i, :] = vals
        # eigh returns vecs[:, i] as i-th eigenvector.
        # Storing transposed to ease column-wise access later
        eigvecs[i, :] = vecs.T 
    
    return energies, eigvecs

def calculate_chern_numbers(energies, eigvecs, N_bands):
    """
    Calculate Chern numbers for top N_bands bands using Fukui-Hatsugai method.
    """
    N_k = energies.shape[0]
    L_grid = int(np.sqrt(N_k))
    
    # Reshape to grid
    v_grid = eigvecs.reshape((L_grid, L_grid, dim))
    
    Chern_nums = np.zeros(N_bands)
    
    # Indices of top bands (highest energy)
    band_indices = list(range(dim - N_bands, dim))
    
    for b_idx_rel, b_idx_abs in enumerate(band_indices):
        # Calculate link variables
        U1 = np.zeros((L_grid, L_grid), dtype=complex)
        U2 = np.zeros((L_grid, L_grid), dtype=complex)
        
        for n1 in range(L_grid):
            for n2 in range(L_grid):
                # Vector at k
                v_k = v_grid[n1, n2, b_idx_abs]
                
                # Neighbor k + b1
                n1_next = (n1 + 1) % L_grid
                v_k1 = v_grid[n1_next, n2, b_idx_abs]
                overlap1 = np.vdot(v_k, v_k1)
                U1[n1, n2] = overlap1 / np.abs(overlap1)
                
                # Neighbor k + b2
                n2_next = (n2 + 1) % L_grid
                v_k2 = v_grid[n1, n2_next, b_idx_abs]
                overlap2 = np.vdot(v_k, v_k2)
                U2[n1, n2] = overlap2 / np.abs(overlap2)
        
        # Field strength F12
        F_sum = 0.0
        for n1 in range(L_grid):
            for n2 in range(L_grid):
                n1_next = (n1 + 1) % L_grid
                n2_next = (n2 + 1) % L_grid
                
                # Product of links around the plaquette
                val = (U1[n1, n2] * 
                       U2[n1_next, n2] * 
                       np.conj(U1[n1, n2_next]) * 
                       np.conj(U2[n1, n2]))
                
                # Imaginary part of log
                F_sum += np.imag(np.log(val))
        
        C = F_sum / (2 * np.pi)
        Chern_nums[b_idx_rel] = C
        
    return Chern_nums

# ---------------------------------------------------------
# 5. Main Execution
# ---------------------------------------------------------

# Generate Grid
ks = get_k_mesh(L)

# Diagonalize
energies, eigvecs = compute_bands_and_eigvecs(ks)

# Calculate Chern numbers
C_top_3 = calculate_chern_numbers(energies, eigvecs, 3)

print("\n" + "="*30)
print(f"Twist Angle: {theta_deg} deg")
print("Chern Numbers of the top three bands:")
for i, c in enumerate(C_top_3):
    print(f"  Band {i+1} (from top): {c:.0f}")
print("="*30)

# ---------------------------------------------------------
# 6. Quantum Metric Calculation
# ---------------------------------------------------------

def calculate_quantum_metric_trace(energies, eigvecs, band_idx):
    """
    Calculate trace of quantum metric for a specific band.
    Uses finite difference on the k-grid.
    """
    N_k = energies.shape[0]
    L_grid = int(np.sqrt(N_k))
    
    # Reshape
    v_grid = eigvecs.reshape((L_grid, L_grid, dim))
    
    # Grid spacing magnitude for derivatives
    # Since BZ is hexagonal, we use the magnitude of the elementary step vectors
    # for normalization. The grid is defined by steps b1/L and b2/L.
    # |b1| = |b2| = g_mag * 2/sqrt(3)? No, b2 is g1+g2.
    # |b2| = |b1|. Geometry is hexagonal.
    # We approximate dk by the length of the grid vectors in x, y directions.
    dk_mag = np.linalg.norm(b1) / L_grid
    
    total_TrG = 0.0
    
    for n1 in range(L_grid):
        for n2 in range(L_grid):
            u = v_grid[n1, n2, band_idx]
            
            # Periodic neighbors
            u_xp = v_grid[(n1+1)%L_grid, n2, band_idx]
            u_xm = v_grid[(n1-1)%L_grid, n2, band_idx]
            u_yp = v_grid[n1, (n2+1)%L_grid, band_idx]
            u_ym = v_grid[n1, (n2-1)%L_grid, band_idx]
            
            # Central difference
            du_x = (u_xp - u_xm) / (2 * dk_mag)
            du_y = (u_yp - u_ym) / (2 * dk_mag)
            
            # Tr(g) = |d_x u|^2 + |d_y u|^2
            norm_dux_sq = np.vdot(du_x, du_x).real
            norm_duy_sq = np.vdot(du_y, du_y).real
            
            total_TrG += (norm_dux_sq + norm_duy_sq)
            
    # Integrate over BZ
    dA = BZ_area / (L_grid * L_grid)
    integral_TrG = total_TrG * dA
    
    return integral_TrG

# Calculate for Top Band
Tr_G_val = calculate_quantum_metric_trace(energies, eigvecs, -1)

print(f"Trace of Quantum Metric G for top electron band: {Tr_G_val:.2f}")

# Plotting
plt.figure(figsize=(10, 6))
top_bands_e = energies[:, -10:]
k_norms = np.linalg.norm(ks, axis=1)
plt.scatter(k_norms, top_bands_e, s=1, alpha=0.5)
plt.xlabel("|k| ($\AA^{-1}$)")
plt.ylabel("Energy (meV)")
plt.title("Dispersion of top 10 bands")
plt.grid(True, alpha=0.3)
plt.savefig("moire_bands.png")
```
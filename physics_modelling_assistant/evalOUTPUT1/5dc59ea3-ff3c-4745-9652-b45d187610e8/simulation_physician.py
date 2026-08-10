**
```python
import numpy as np
import scipy.linalg as la

# 1. Constants and Parameters
# ---------------------------
# Fundamental constants and Model Parameters
a0 = 3.52  # Monolayer lattice constant in Angstroms
theta = 3.5 * np.pi / 180.0  # Twist angle in radians
m_star_ratio = 0.6  # m* / m_e
V = 16.5  # Moire potential amplitude in meV
w = -18.8  # Interlayer hopping amplitude in meV
psi = -105.9 * np.pi / 180.0  # Phase in radians

# Kinetic Energy Coefficient
# The prompt states: "Choose hbar/(2 m_e) = 7619.96423 meV * A^2".
# Dimensional analysis and typical values for TMD bandwidths suggest 
# the intended value for the effective kinetic term scales with h^2/m.
# 7619.96423 is approximately 2 * (h^2 / 2m_e) in standard units (~3810).
# We interpret this as the physical constant corresponding to h^2 / m_e.
# Thus, h^2 / (2 m*) = (Provided Value / 2) * (m_e / m*)
kinetic_base = 7619.96423 / 2.0
h2_2m_eff = kinetic_base / m_star_ratio 

# Numerical Simulation Parameters
L = 60  # Grid size
Q_cutoff_factor = 4.1  # Cutoff for plane waves in terms of |b1|

# 2. Geometry Setup
# -----------------
# Moire lattice constant
aM = a0 / (2 * np.sin(theta / 2))

# Reciprocal lattice vectors g_i (Moiré BZ basis)
# g1 = (4pi / (sqrt(3) aM)) * (1, 0)
g_mag = 4 * np.pi / (np.sqrt(3) * aM)
g1 = np.array([g_mag, 0.0])

# Rotation by 120 degrees
C3 = np.array([[np.cos(2*np.pi/3), -np.sin(2*np.pi/3)], 
               [np.sin(2*np.pi/3),  np.cos(2*np.pi/3)]])

g2 = C3 @ g1
g3 = C3 @ g2

# Interlayer coupling vectors q_i
# q1 = |g1| * (0, 1/sqrt(3))
q1 = np.array([0.0, g_mag / np.sqrt(3)])
q2 = C3 @ q1
q3 = C3 @ q2

# Vectors for Brillouin Zone integration
b1 = g1
b2 = g1 + g2

# Area of BZ for integration
# Cross product in 2D is scalar z-component
BZ_area = np.abs(np.cross(b1, b2))

# 3. Basis Generation (Q-vectors)
# -------------------------------
# We need to find all Q vectors such that |Q| < R_cut.
# Top layer t: Q - q1 is in Reciprocal Lattice
# Bottom layer b: Q + q1 is in Reciprocal Lattice
# To generate them, we iterate over integer pairs (n, m) for reciprocal lattice vectors G = n*g1 + m*g2.
# We shift G by q1 or -q1 to get Q.

R_cut = Q_cutoff_factor * np.linalg.norm(b1)

# Augment G-vectors until we cover the cutoff radius
max_n = int(np.ceil(R_cut / np.linalg.norm(g1))) + 2

basis_vectors = [] # List of tuples (Q_vec, layer_str, G_parent)
# layer_str: 't' for top, 'b' for bottom

# Define a helper to generate candidates
def generate_basis_layer(shift, layer_label):
    candidates = []
    for n in range(-max_n, max_n + 1):
        for m in range(-max_n, max_n + 1):
            G = n * g1 + m * g2
            Q = G + shift
            if np.linalg.norm(Q) < R_cut:
                candidates.append((Q, layer_label, n, m))
    return candidates

# Top layer: Q = G + q1
top_candidates = generate_basis_layer(q1, 't')
# Bottom layer: Q = G - q1
bottom_candidates = generate_basis_layer(-q1, 'b')

# Merge lists
all_vectors_data = top_candidates + bottom_candidates

# Remove duplicates and create mapping
basis_mapping = {}
Q_list = []
layer_list = []

# Sort for consistency
all_vectors_data.sort(key=lambda x: (x[0][0], x[0][1]))

for data in all_vectors_data:
    Q, layer, n, m = data
    key = (n, m, layer)
    if key not in basis_mapping:
        idx = len(basis_mapping)
        basis_mapping[key] = idx
        Q_list.append(Q)
        layer_list.append(layer)

num_basis = len(Q_list)
print(f"Number of basis vectors (plane waves): {num_basis}")

Q_list = np.array(Q_list)

# Map for fast lookup
tolerance = 1e-6
map_Q_to_idx = {tuple(np.round(q, 6)): i for i, q in enumerate(Q_list)}

# 4. Hamiltonian Structure Precomputation
# ---------------------------------------
# We precompute constant couplings (V, w) to speed up the loop.
h_structure = [] # (row, col, val_real, val_imag)

g_vecs = [g1, g2, g3]

for i in range(num_basis):
    Qi = Q_list[i]
    li = layer_list[i]
    
    # Intralayer Potential
    for g in g_vecs:
        for sign, shift in enumerate([g, -g]):
            Q_target = Qi + shift
            key = tuple(np.round(Q_target, 6))
            if key in map_Q_to_idx:
                j = map_Q_to_idx[key]
                if layer_list[j] == li:
                    val = 0
                    if li == 't':
                        # Top: H = V e^{+i psi} for +g, V e^{-i psi} for -g
                        if np.allclose(shift, g):
                            val = V * (np.cos(psi) + 1j*np.sin(psi))
                        else:
                            val = V * (np.cos(psi) - 1j*np.sin(psi))
                    else:
                        # Bot: H = V e^{-i psi} for +g, V e^{+i psi} for -g
                        if np.allclose(shift, g):
                            val = V * (np.cos(psi) - 1j*np.sin(psi))
                        else:
                            val = V * (np.cos(psi) + 1j*np.sin(psi))
                    
                    h_structure.append((i, j, np.real(val), np.imag(val)))
                    h_structure.append((j, i, np.real(val), -np.imag(val)))

    # Interlayer Hopping
    if li == 'b':
        for q in [q1, q2, q3]:
            Q_target = Qi + q
            key = tuple(np.round(Q_target, 6))
            if key in map_Q_to_idx:
                j = map_Q_to_idx[key]
                if layer_list[j] == 't':
                    # b -> t coupling is w
                    val = w
                    h_structure.append((i, j, np.real(val), np.imag(val)))
                    
    if li == 't':
        for q in [q1, q2, q3]:
            Q_target = Qi - q
            key = tuple(np.round(Q_target, 6))
            if key in map_Q_to_idx:
                j = map_Q_to_idx[key]
                if layer_list[j] == 'b':
                    # t -> b coupling is w
                    val = w
                    h_structure.append((i, j, np.real(val), np.imag(val)))

# 5. Main Loop over BZ
# --------------------
# Generate k-points
ks = []
for l1 in range(L):
    for l2 in range(L):
        frac1 = l1/L - 0.5
        frac2 = l2/L - 0.5
        ks.append(frac1 * b1 + frac2 * b2)
        
ks = np.array(ks)
num_k = len(ks)

all_energies = np.zeros((num_k, num_basis))
all_states = np.zeros((num_k, num_basis, num_basis), dtype=complex)

print("Diagonalizing Hamiltonian...")
for idx_k, k_vec in enumerate(ks):
    Hk = np.zeros((num_basis, num_basis), dtype=complex)
    
    # Kinetic
    p_vec = k_vec - Q_list
    p_sq = np.sum(p_vec**2, axis=1)
    np.fill_diagonal(Hk, -h2_2m_eff * p_sq)
    
    # Add constant couplings
    for (r, c, vr, vi) in h_structure:
        Hk[r, c] += vr + 1j * vi
        
    w, v = la.eigh(Hk)
    all_energies[idx_k, :] = w
    all_states[idx_k, :, :] = v

# 6. Analysis of Bands
# --------------------
center_idx = (L//2) * L + (L//2)
energies_k0 = all_energies[center_idx]
sorted_indices_center = np.argsort(energies_k0)
top_three_indices = sorted_indices_center[-3:]

# We need the highest energy band for Quantum Metric
top_band_idx = top_three_indices[-1] # Last in sorted (ascending) is highest
# Sort top 3 descending for Chern output
top_three_indices_desc = sorted(top_three_indices, key=lambda i: -energies_k0[i])

# 7. Chern Number Calculation
# ----------------------------
U1 = np.zeros((num_k, num_basis), dtype=complex)
U2 = np.zeros((num_k, num_basis), dtype=complex)

print("Calculating Chern Numbers...")
for k_idx in range(num_k):
    l1 = k_idx // L
    l2 = k_idx % L
    
    n1 = ((l1 + 1) % L) * L + l2
    n2 = l1 * L + ((l2 + 1) % L)
    
    vec_k = all_states[k_idx]
    vec_k1 = all_states[n1]
    vec_k2 = all_states[n2]
    
    overlap1 = np.dot(np.conj(vec_k.T), vec_k1)
    overlap2 = np.dot(np.conj(vec_k.T), vec_k2)
    
    diag_up1 = np.diag(overlap1)
    norm1 = np.abs(diag_up1)
    U1[k_idx, :] = diag_up1 / (norm1 + 1e-15)
    
    diag_up2 = np.diag(overlap2)
    norm2 = np.abs(diag_up2)
    U2[k_idx, :] = diag_up2 / (norm2 + 1e-15)

F12 = np.zeros((num_k, num_basis), dtype=complex)
for k_idx in range(num_k):
    l1 = k_idx // L
    l2 = k_idx % L
    idx_k1 = ((l1 + 1) % L) * L + l2
    idx_k2 = l1 * L + ((l2 + 1) % L)
    idx_k12 = ((l1 + 1) % L) * L + ((l2 + 1) % L)
    
    for n in range(num_basis):
        val = U1[k_idx, n] * U2[idx_k1, n] * np.conj(U1[idx_k2, n]) * np.conj(U2[k_idx, n])
        F12[k_idx, n] = np.log(val)

cherns = np.imag(np.sum(F12, axis=0)) / (2 * np.pi)
top_cherns = [int(np.round(cherns[i])) for i in top_three_indices_desc]
print(f"Chern numbers of top three bands (highest to lowest): {top_cherns}")

# 8. Quantum Metric Calculation
# -----------------------------
g_trace_sum = 0.0

print("Calculating Quantum Metric Trace...")
for idx_k in range(num_k):
    k_vec = ks[idx_k]
    E = all_energies[idx_k]
    U = all_states[idx_k]
    
    diff_x = -2.0 * h2_2m_eff * (k_vec[0] - Q_list[:,0])
    diff_y = -2.0 * h2_2m_eff * (k_vec[1] - Q_list[:,1])
    
    Dx = np.diag(diff_x)
    Dy = np.diag(diff_y)
    
    Mx = U.T.conj() @ Dx @ U
    My = U.T.conj() @ Dy @ U
    
    n = top_band_idx
    val_trace = 0.0
    
    for m in range(num_basis):
        if m == n:
            continue
        denom = (E[n] - E[m])**2
        term_xx = (Mx[n, m] * Mx[m, n]).real
        term_yy = (My[n, m] * My[m, n]).real
        val_trace += (term_xx + term_yy) / denom
        
    g_trace_sum += val_trace

dS = BZ_area / (L**2)
Tr_G = g_trace_sum * dS
print(f"Numerical Result for Tr(G) (Top Electron Band): {Tr_G:.2f}")
```
```python
import numpy as np
import scipy.linalg as la

# 1. Constants and Parameters
# ---------------------------
# Fundamental constants and Model Parameters based on provided documents
a0 = 3.52                      # Monolayer lattice constant in Angstroms
theta = 3.5 * np.pi / 180.0    # Twist angle in radians
m_star_ratio = 0.6             # m* / m_e
V = 16.5                       # Moire potential amplitude in meV
w = -18.8                      # Interlayer hopping amplitude in meV
psi = -105.9 * np.pi / 180.0   # Phase in radians

# Kinetic Energy Coefficient
# Based on "Kinetic coefficient: hbar/(2 m_e) = 7619.96423 meV * A^2"
# Note: h^2/(2m*) = (hbar * hbar / (2m*)) = (hbar/(2m_e) * 2 * hbar) ... 
# dimensional consistency for standard effective mass models usually takes the form h^2 k^2 / 2m.
# The coefficient provided in the prompt (7619.96423) is explicitly labeled as hbar / (2 m_e).
# Standard kinetic term is h_bar^2 k^2 / 2m. 
# h_bar = (hbar / (2 m_e)) * 2 * m_e 
# (hbar^2 / 2m*) = (hbar / (2 m_e) * 2 * m_e)^2 / (2 * m_star_ratio * m_e)
# Let K0 = 7619.96423.
# Then Term = (K0 * 2)^2 / (2 * m_ratio) * k^2 = (4 * K0^2) / (2 * m_ratio) * k^2.
# However, examining the context of continuum models (e.g. Wu et al.), usually the term is
# defined with a factor alpha_Theta = h^2 / (2 m* a_M^2).
# Given the prompt's explicit value for hbar/(2m_e), we derive the prefactor for k^2 (where k is in 1/A).
# Prefactor = (h_bar^2) / (2 m*)
# h_bar = 7619.96423 * 2 * m_e
# h_bar^2 = (7619.96423 * 2)^2 * m_e^2
# denominator = 2 * 0.6 * m_e
# Prefactor = (7619.96423^2 * 4) / 1.2  meV * A^2 ~= 193,722,000.
#
# Wait, typically hbar ~ 658 meV fs. 658^2 ~ 430,000.
# If parameter means literally hbar / (2m) ~ 7620 (meV A^2 / mass?), it's strange.
# Let's look at the standard TMD literature value: h^2 / (2m*) is approx 5000 meV A^2.
# In the "Dimensional Analysis" section provided in the context:
# "Given the numerical convention h^2 / 2m* = 7619.96 * ... approx 4572 meV * A^2"
# Wait, the text says "hbar/(2 m_e) = 7619.96423".
# Then "h^2 / 2m* = 7619.96 * ... approx 4572".
# Relation: h^2 = 2 * hbar. (Wait, hbar = h / 2pi).
# Let's assume the prompt intends the value ~4572 meV*A^2 for the kinetic coefficient h^2/(2m*).
# Calculation in "Dimensional Analysis": (7619.96 * 0.6 * m_e / m_e) ?? No, that's ~4572.
# It seems the provided parameter 7619.96423 might actually be the parameter that needs to be scaled by 0.6 to get ~4572.
# Or it is simply h^2/(2m) roughly.
# Let's stick to the calculated value in the text: ~4572 meV A^2.
# Why? 7619.96423 is given. 7619.96423 * 0.6 = 4571.9785. This matches the text's "approx 4572".
# So: kinetic_prefactor = 7619.96423 * m_star_ratio
kinetic_prefactor = 7619.96423 * m_star_ratio  # approx 4572 meV * A^2

# Grid and Cutoff
L = 60                # Grid size (60 x 60)
Q_cutoff_factor = 4.1 # Cutoff for plane waves

# 2. Geometry Setup
# -----------------
# Moire lattice constant
aM = a0 / (2 * np.sin(theta / 2))

# Reciprocal lattice vectors g_i (Moiré BZ basis)
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

# Brillouin Zone integration basis vectors
b1 = g1
b2 = g1 + g2

# Area of BZ for normalization (Cross product of 2D vectors)
BZ_area = np.abs(np.cross(b1, b2))

# 3. Basis Generation (Q-vectors)
# -------------------------------
# Plane wave expansion:
# c_r,l = 1/sqrt(V) sum_k,Q exp(-i(k-Q).r) c_{k-Q,l}
# Q vectors:
# Top layer (t): Q - q1 is Reciprocal Lattice Vector
# Bottom layer (b): Q + q1 is Reciprocal Lattice Vector
# Constraint: |Q| < 4.1 |b1|

# Generate integer lattice points for G = n*g1 + m*g2
# Max extent needed
R_cut = Q_cutoff_factor * np.linalg.norm(b1)
max_n = int(np.ceil(R_cut / np.linalg.norm(g1))) + 2

Q_list = []      # List of Q vectors
layer_list = []  # 'b' or 't'
idx_map = {}     # Map (n, m, layer) -> index in basis

def get_basis_candidates(shift_q, layer_char):
    candidates = []
    for n in range(-max_n, max_n + 1):
        for m in range(-max_n, max_n + 1):
            G = n * g1 + m * g2
            Q = G + shift_q
            if np.linalg.norm(Q) < R_cut:
                candidates.append((Q, n, m))
    return candidates

# Generate candidates for Top (shift +q1? No, text: Q - q1 is RL. So Q = G + q1)
# Text: Top "Q - q1 must be a reciprocal lattice vector" => Q = G + q1
top_cands = get_basis_candidates(q1, 't')
# Text: Bottom "Q + q1 must be a reciprocal lattice vector" => Q = G - q1
bot_cands = get_basis_candidates(-q1, 'b')

# Unique filtering
# Keys for uniqueness: rounded Q vector coordinates
seen_vectors = {}
all_basis_data = []

for Q, n, m in top_cands:
    # Round to avoid float precision duplicates
    key = (np.round(Q[0], 6), np.round(Q[1], 6))
    if key not in seen_vectors:
        seen_vectors[key] = len(Q_list)
        Q_list.append(Q)
        layer_list.append('t')
        all_basis_data.append((Q, 't'))

for Q, n, m in bot_cands:
    key = (np.round(Q[0], 6), np.round(Q[1], 6))
    if key not in seen_vectors:
        seen_vectors[key] = len(Q_list)
        Q_list.append(Q)
        layer_list.append('b')
        all_basis_data.append((Q, 'b'))

# Ensure order consistency (sort by x then y)
indices = np.lexsort((Q_list[:, 1], Q_list[:, 0]))
Q_list = np.array(Q_list)[indices]
layer_list = np.array(layer_list)[indices]

num_basis = len(Q_list)
print(f"Number of basis vectors (plane waves): {num_basis}")

# Inverse map for matrix construction
q_map = { (np.round(q[0], 6), np.round(q[1], 6)): i for i, q in enumerate(Q_list) }

# 4. Hamiltonian Construction
# ---------------------------
# Real space operators -> k-space matrix elements
# Potential: 2 V sum cos(g_i r +/- psi)
# H_pot = V sum (e^{+i...} + e^{-i...}) 
# Off-diagonal: w sum e^{+/- i q_i . r}
# In k-space: delta(k - k' +/- g) or delta(k - k' +/- q)

# Pre-allocate Hamiltonian structure
# H = H_kin + H_pot + H_hop
# Basis is flattened: all Q for layer b, then all Q for layer t? 
# Or interleaved? The code construction will iterate over indices.
# Let's organize indices into blocks for potentially faster access, 
# but general iteration works fine. 
# Let's rebuild Q_list to be [Bottom Qs, Top Qs] for block structure.
# This is not strictly necessary for correctness but good for style.

indices_b = [i for i, l in enumerate(layer_list) if l == 'b']
indices_t = [i for i, l in enumerate(layer_list) if l == 't']

# We will keep the list sorted but indices_b/t tell us where to look.

# Precompute intralayer potential connections
# Potential V couples Q to Q+/-g_i
h_rows = []
h_cols = []
h_data = []

g_vecs = [g1, g2, g3]
q_vecs = [q1, q2, q3]

# Helper to add Hermitian pair
def add_interaction(i, j, val):
    h_rows.append(i)
    h_cols.append(j)
    h_data.append(val)
    h_rows.append(j)
    h_cols.append(i)
    h_data.append(np.conj(val))

for i in range(num_basis):
    Qi = Q_list[i]
    li = layer_list[i]
    
    # Intralayer Potential
    # H_pot = 2V * sum( cos(g.r +/- psi) ) = V * sum( e^{i(g.r +/- psi)} + e^{-i(g.r +/- psi)} )
    # Matrix element: Q + g
    for g in g_vecs:
        # Target vector
        Q_target_p = Qi + g
        Q_target_m = Qi - g
        
        # Check +g
        key = (np.round(Q_target_p[0], 6), np.round(Q_target_p[1], 6))
        if key in q_map:
            j = q_map[key]
            if layer_list[j] == li:
                # Sign convention
                # Phase is +psi for top (e^+i) in cosine term?
                # Model: H = ... + 2V sum cos(g.r - psi) (bottom)?
                # Text: Top: cos(g.r - psi), Bottom: cos(g.r + psi)
                # Complex expansion: cos(A) = 0.5(e^iA + e^-iA)
                # Coeff of e^i g.r is V * e^{i(+/- psi)}
                
                phase = -psi if li == 't' else psi # Text: t: ... - psi, b: ... + psi
                # Wait, term is cos(g.r +/- psi).
                # Hamiltonian Term for k-space:
                # <k+g| e^{i g.r} |k> = 1.
                # We need to match the term exp( i g.r ) in the Hamiltonian expansion.
                # H ~ V ( e^{i(g.r - psi)} + c.c ) = V e^{-i psi} e^{i g.r} + V e^{i psi} e^{-i g.r}.
                # Connection k -> k+g involves e^{i g.r}, coeff V e^{-i psi}.
                # Connection k+g -> k involves e^{-i g.r}, coeff V e^{i psi}.
                
                val = V * np.exp(1j * phase)
                add_interaction(i, j, val)

        # Check -g
        key = (np.round(Q_target_m[0], 6), np.round(Q_target_m[1], 6))
        if key in q_map:
            j = q_map[key]
            if layer_list[j] == li:
                # For e^{-i g.r}, coeff is V e^{i psi} (conjugate of the e^{i g.r} term coeff)
                # Actually, from H = V e^{i phase} e^{-i g.r} + h.c.
                # Here we add the h.c. partner.
                # If we iterate all pairs, we can just add the specific value and its conj.
                # Connection k -> k-g uses e^{-i g.r}.
                val = V * np.exp(-1j * phase)
                add_interaction(i, j, val)

    # Interlayer Hopping w
    # w sum e^{+/- i q_i . r}
    if li == 'b':
        # Hopping from b to t via e^{i q.r} or e^{-i q.r}?
        # Text: w sum e^{-i q.r} (top-left off-diag)
        #           w sum e^{+i q.r} (bottom-right off-diag)
        # Block formulation: [ H_b , T ; T^\dag, H_t ]
        # T ~ sum e^{-i q.r}
        # Term e^{-i q.r} couples k (bottom) to k+q (top).
        for q in q_vecs:
            Q_target = Qi + q
            key = (np.round(Q_target[0], 6), np.round(Q_target[1], 6))
            if key in q_map:
                j = q_map[key]
                if layer_list[j] == 't':
                    add_interaction(i, j, w)
    elif li == 't':
        # Symmetric check to be sure, though `add_interaction` handles it if we used 只有 one direction.
        # Since we iterate all i, we check neighbors.
        # H_tib ~ w* e^{i q.r} (Hermitian conjugate)
        # Connects k (top) to k-q (bottom).
        for q in q_vecs:
            Q_target = Qi - q
            key = (np.round(Q_target[0], 6), np.round(Q_target[1], 6))
            if key in q_map:
                j = q_map[key]
                if layer_list[j] == 'b':
                    add_interaction(i, j, w)

# Convert to dense preparation
H_static = np.zeros((num_basis, num_basis), dtype=complex)
for r, c, d in zip(h_rows, h_cols, h_data):
    H_static[r, c] += d

# 5. Main Loop and Diagonalization
# --------------------------------
ks = []
for l1 in range(L):
    for l2 in range(L):
        # k-points centered on 0
        f1 = (l1 / L) - 0.5
        f2 = (l2 / L) - 0.5
        ks.append(f1 * b1 + f2 * b2)
ks = np.array(ks)
Nk = L * L

print(f"Diagonalizing {Nk} k-points...")
all_states = np.zeros((Nk, num_basis, num_basis), dtype=complex)
all_energies = np.zeros((Nk, num_basis))

for ik in range(Nk):
    k_vec = ks[ik]
    
    Hk = H_static.copy()
    
    # Add Kinetic Energy
    # Term: h^2/2m* |k - Q|^2
    # We overwrite diagonal or add to it. H_static has 0 diagonal initially (potential/hopping purely off-diag)
    # (Correction: Potential V adds off-diagonal. Diagonal is 0 + Kinetic)
    
    p_vec = k_vec - Q_list
    # |p|^2
    p_sq = np.sum(p_vec**2, axis=1)
    # Diagonal kinetic energy
    np.fill_diagonal(Hk, kinetic_prefactor * p_sq)
    
    # Diagonalize
    w, v = la.eigh(Hk)
    all_energies[ik, :] = w
    all_states[ik, :, :] = v

# 6. Band Selection and Chern Number
# -----------------------------------
# Identify top electron band
# At Gamma point (k=0), energies are higher at the center of the BZ for top valence? 
# Wait, this is likely the conduction band (electron band) or valence band?
# "Quantum Metric ... for the top electron band".
# In MoTe2, valence band is usually at negative energy, conduction at positive.
# With parameters V, w typically negative, V pos, we check center.
# k=0 (ik = (L/2)*L + L/2 ~ 30*60+30)
ik_center = (L // 2) * L + (L // 2)
E_center = all_energies[ik_center]
sorted_idx = np.argsort(E_center) # Lowest to Highest

# Top band is highest energy
top_band_flat_idx = sorted_idx[-1]
# Indices of top 3 bands for Chern check
top_3_flat_indices = sorted_idx[-3:]

# We need global indices for bands to calculate Chern numbers efficiently
# Map flat index to band index in sorted order per k point?
# Actually, bands don't cross much in these limits? We assume no crossing for Chern calculation simplicity 
# or we track connectivity.
# Given isolated bands assumption in continuum models:
# We will calculate Chern for the bands that correspond to top_3_flat_indices at k=0.

# 7. Chern Number Calculation (Fukui-Hatsugai-Suzuki Method)
# -----------------------------------------------------------
# U_mu(k) = det < u_n(k) | u_m(k + d_mu) >
# This requires constructing the link variable for the isolated band n.
# However, we need to isolate the bands of interest.
# Let's compute U matrices for all bands, then trace over subgroups.
# Or project onto bands.
# Given small basis size (num_basis ~ 200-400) and L=60, we can do full matrix U.

U1 = np.zeros((Nk, num_basis, num_basis), dtype=complex)
U2 = np.zeros((Nk, num_basis, num_basis), dtype=complex)

# Calculate link variables
for ik in range(Nk):
    l1 = ik // L
    l2 = ik % L
    
    # Neighbors with periodic boundary
    ik1 = ((l1 + 1) % L) * L + l2
    ik2 = l1 * L + ((l2 + 1) % L)
    
    # < u(k) | u(k+mu) >
    # v[:, n] is the n-th eigenvector (column)
    # sum_n v_k^dagger * v_k+mu
    # This acts as a "change of basis" matrix
    
    mat1 = np.dot(np.conj(all_states[ik].T), all_states[ik1])
    mat2 = np.dot(np.conj(all_states[ik].T), all_states[ik2])
    
    U1[ik] = mat1
    U2[ik] = mat2

# Field strength F12
F12 = np.zeros((Nk,), dtype=complex)

# Normalize link variables (optional in theory if eigenstates normalized, but numerical safety)
# Fuhui method: U_mu(k) = P(k, k+mu)
# F12(k) = ln( U1(k) U2(k+1) U1(k+2)^-1 U2(k)^-1 )
# Note on indices: k+1 is mu=1 step, k+2 is mu=2 step.

# We want Chern numbers for specific bands. 
# It is easier to compute U for the subspace.
U1_sub = np.zeros((Nk, 3, 3), dtype=complex)
U2_sub = np.zeros((Nk, 3, 3), dtype=complex)

# Indices of the 3 bands (in the full basis space)
band_indices = top_3_flat_indices 

for ik in range(Nk):
    # Extract submatrices
    U1_sub[ik] = U1[ik][np.ix_(band_indices, band_indices)]
    U2_sub[ik] = U2[ik][np.ix_(band_indices, band_indices)]

# Construct F12 for the bundle
cherns_sum = 0
for n in range(3):
    field_strength_sum = 0.0
    for ik in range(Nk):
        l1 = ik // L
        l2 = ik % L
        
        ik1 = ((l1 + 1) % L) * L + l2
        ik2 = l1 * L + ((l2 + 1) % L)
        ik12 = ((l1 + 1) % L) * L + ((l2 + 1) % L)
        
        # Product of links
        prod = U1_sub[ik, n, n] * U2_sub[ik1, n, n] * \
               np.conj(U1_sub[ik2, n, n]) * np.conj(U2_sub[ik, n, n])
               
        # Numerical stability clip
        if np.abs(prod) > 0:
            # Ensure phase is in [-pi, pi] via log
            field_strength_sum += np.log(prod)
        else:
            # Should not happen for isolated bands
            pass
            
    chern = (1.0 / (2 * np.pi * 1j)) * field_strength_sum
    cherns_sum += chern # This is sum of Chern numbers of the 3 bands
    # The provided code calculated band-by-band. 
    # Let's believe the bands are isolated and individual Tr(U) is effectively the element.
    # However, Fukui method for a single isolated band (subset size N=1) is just the element.
    # For N= bundle, we need det.
    # But we want individual Chern numbers of the 3 bands (1, 0, -1).
    # This implies bands are separable (isolated from each other).
    # So treating them as N=1 bundles is valid.

# Re-calculating explicitly for N=1 subsets
final_cherns = []
for band_offset, b_idx in enumerate(top_3_flat_indices):
    c_sum = 0.0
    for ik in range(Nk):
        l1 = ik // L
        l2 = ik % L
        ik1 = ((l1 + 1) % L) * L + l2
        ik2 = l1 * L + ((l2 + 1) % L)
        ik12 = ((l1 + 1) % L) * L + ((l2 + 1) % L)
        
        # Link variables for this single band
        u1 = np.dot(np.conj(all_states[ik, :, b_idx]), all_states[ik1, :, b_idx])
        u2 = np.dot(np.conj(all_states[ik, :, b_idx]), all_states[ik2, :, b_idx])
        u1_12 = np.dot(np.conj(all_states[ik2, :, b_idx]), all_states[ik12, :, b_idx]) # U1 at ik+2
        u2_1 = np.dot(np.conj(all_states[ik1, :, b_idx]), all_states[ik12, :, b_idx])  # U2 at ik+1
        
        # Inverse for U(1) is conj
        prod = u1 * u2_1 * np.conj(u1_12) * np.conj(u2)
        
        c_sum += np.log(prod)
        
    chern = np.imag(c_sum) / (2 * np.pi)
    final_cherns.append(int(np.round(chern)))

print(f"Chern numbers of top three bands (highest to lowest): {final_cherns}")

# 8. Quantum Metric Calculation
# -----------------------------
# Trace of Quantum Metric G = Tr[g_ij]
# g_ij = Tr[ P d_i P d_j P ] / 2 (summation over band index implied?)
# For single band n: g_ij = Re[ <dn|di n> <dj n|dn> ] ? No.
# g_ij(n) = Re[ sum_{m!=n} <n|di H|m><m|dj H|n> / (En - Em)^2 ]
# Standard formula from perturbation theory.
# Tr G = sum_n integral d^2k (g_kk(n))

# We compute for the top electron band (highest energy)
n_idx = top_band_flat_idx # The index in the flattened array

g_trace_integral = 0.0

# Precompute derivative operators dH/dk_x, dH/dk_y
# dH/dk_x ~ h_bar^2 / m * (k_x - Q_x)
# dH/dk_y ~ h_bar^2 / m * (k_y - Q_y)
# Factor: d/dk (k^2) = 2k.
# Prefactor was kinetic_prefactor = h^2/2m.
# Derivative of (prefactor * k^2) is prefactor * 2k.
# d_eigenbasis = U^dagger dH U

Dx_factor = 2 * kinetic_prefactor
Dy_factor = 2 * kinetic_prefactor

for ik in range(Nk):
    kx = ks[ik, 0]
    ky = ks[ik, 1]
    
    # Construct derivative matrices (diagonal in plane wave basis)
    dHx = np.diag(Dx_factor * (kx - Q_list[:, 0]))
    dHy = np.diag(Dy_factor * (ky - Q_list[:, 1]))
    
    # Eigenvectors
    vecs = all_states[ik]
    vals = all_energies[ik]
    
    # Project derivatives: A_x = U^dagger dHx U
    Ax = vecs.T.conj() @ dHx @ vecs
    Ay = vecs.T.conj() @ dHy @ vecs
    
    # Sum over m != n
    # Formula: g_xx + g_yy
    current_g = 0.0
    
    for m in range(num_basis):
        if m == n_idx:
            continue
        
        delta_E = vals[n_idx] - vals[m]
        den = delta_E**2
        
        # Terms from summation
        # <n|d_x|m><m|d_x|n>
        term_xx = (Ax[n_idx, m] * Ax[m, n_idx]).real
        term_yy = (Ay[n_idx, m] * Ay[m, n_idx]).real
        
        current_g += (term_xx + term_yy) / den
        
    g_trace_integral += current_g

# Integrate over BZ
# d^2k = BZ_area / L^2
dS = BZ_area / (L * L)
Tr_G = g_trace_integral * dS

print(f"Numerical Result for Tr(G) (Top Electron Band): {Tr_G:.5f} (Angstrom^2)")
```
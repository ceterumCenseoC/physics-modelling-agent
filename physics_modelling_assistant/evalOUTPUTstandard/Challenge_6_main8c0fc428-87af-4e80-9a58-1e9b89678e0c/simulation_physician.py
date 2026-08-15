
# Implementation of the Twisted Bilayer MoTe$_2$ Continuum Model

This Python code implements the continuum model described in the problem statement. It calculates the band structure, computes the Chern numbers for the top three bands using the Fukui-Hatsugai-Suzuki method, and evaluates the trace of the quantum metric $\mathop{\mathrm{Tr}}\mathcal{G}$ for the top electron band.

```python
import numpy as np
import scipy.linalg as la

# ==========================================
# 1. Model Parameters and Physical Constants
# ==========================================

# We use units where energy is in meV and length is in Angstroms (A).
# The default unit system for math operations is adopted from the context:
# Energy: meV
# Length: A
# Mass: scaled such that hbar^2 / (2 * m_e) = 7619.96423 meV * A^2

# Physical Parameters
theta_deg = 3.5           # Twist angle in degrees
a0 = 3.52                 # Monolayer lattice constant in A
m_eff_ratio = 0.6         # m* / m_e
V = 16.5                  # Moire potential amplitude in meV
w = -18.8                 # Interlayer tunneling in meV
psi_deg = -105.9          # Potential phase in degrees

# Derived Calculation Constants
# Kinetic energy coefficient: hbar^2 / (2 * m*)
# Given hbar^2 / (2 * m_e) = 7619.96423 meV * A^2
# So hbar^2 / (2 * m*) = (hbar^2 / (2 * m_e)) / (m*/m_e)
hbar2_2me = 7619.96423        
kinetic_coeff = hbar2_2me / m_eff_ratio

# Geometric Calculations
theta = np.deg2rad(theta_deg)
psi = np.deg2rad(psi_deg)

# Moire period a_M
aM = a0 / (2 * np.sin(theta / 2))

# Magnitude of reciprocal vector g1
# g1 = (4*pi) / (sqrt(3) * aM) * (1, 0)
g_mag = (4 * np.pi) / (np.sqrt(3) * aM)

# Vectors
def rotate(vector, angle):
    c, s = np.cos(angle), np.sin(angle)
    R = np.array([[c, -s], [s, c]])
    return np.dot(R, vector)

# g_1, q_1 definitions
g1 = np.array([g_mag, 0])
q1 = g_mag * np.array([0, 1/np.sqrt(3)])

# Generate g_i and q_i families
C3_rot = 2 * np.pi / 3 # 120 degrees
g_vecs = [rotate(g1, i * C3_rot) for i in range(3)]
q_vecs = [rotate(q1, i * C3_rot) for i in range(3)]

# Basis vectors for Brillouin Zone integration
b1 = g1
b2 = g1 + g_vecs[1] # g1 + g2

# Moire reciprocal lattice vectors (for Q set generation)
# The reciprocal lattice vectors are linear combinations of g1 and g2
# We define the lattice basis as g1 and g2 (60 degrees)
G_basis = np.array([g1, g_vecs[1]]).T 
# Inverse to find integer coordinates (n1, n2) from a vector
# Note: g1 and g2 are not orthogonal. 
# We will iterate over integer shells to find Q vectors.

# ==========================================
# 2. Basis Set Generation
# ==========================================

# Cutoff condition: |Q| < 4.1 * |b1|
cutoff_radius = 4.1 * np.linalg.norm(b1)

def get_Q_vectors(shift_vec):
    """
    Generate Q vectors satisfying:
    1. Q - shift_vec is a reciprocal lattice vector.
       i.e., Q = shift_vec + n1*g1 + n2*g2
    2. |Q| < cutoff_radius
    """
    Q_list = []
    
    # We search a large enough range of n1, n2 integers
    # The cutoff in k-space is approx 4.1*g_mag. 
    # shift_vec is approx 0.5*g_mag. So we need n roughly up to 5.
    limit = 6 
    for n1 in range(-limit, limit + 1):
        for n2 in range(-limit, limit + 1):
            # G = n1*g1 + n2*g2
            # Note: Usually basis is g1, g2. Here g2 is 120 deg from g1.
            G_recip = n1 * g_vecs[0] + n2 * g_vecs[1]
            
            Q = shift_vec + G_recip
            
            if np.linalg.norm(Q) < cutoff_radius:
                Q_list.append(Q)
                
    # Filter unique vectors (floating point check)
    # Convert to list of tuples for uniqueness check
    unique_Q = []
    seen = set()
    for q in Q_list:
        # Round to a tolerance to handle float errors
        t_q = tuple(np.round(q, 6))
        if t_q not in seen:
            seen.add(t_q)
            unique_Q.append(q)
            
    return unique_Q

# Q sets for top (t) and bottom (b) layers
# Top: Q - q1 is RL vector -> Q = q1 + G
Q_top = np.array(get_Q_vectors(q_vecs[0]))
# Bottom: Q + q1 is RL vector -> Q = -q1 + G
Q_bottom = np.array(get_Q_vectors(-q_vecs[0]))

print(f"Top layer basis size: {len(Q_top)}")
print(f"Bottom layer basis size: {len(Q_bottom)}")
print(f"Total Hamiltonian dimension: {len(Q_top) + len(Q_bottom)}")

# ==========================================
# 3. Hamiltonian Construction
# ==========================================

L_grid = 60
# Momentum grid
# k = (l1/L - 1/2)*b1 + (l2/L - 1/2)*b2
l_vals = np.arange(L_grid)
weights = (l_vals / L_grid - 0.5)
ks_l1, ks_l2 = np.meshgrid(weights, weights) # shape (L, L)

# Construct the ks array (L, L, 2)
# flatten for iterating
ks_flat = np.zeros((L_grid * L_grid, 2))
ks_flat[:, 0] = ks_l1.flatten() * b1[0] + ks_l2.flatten() * b2[0]
ks_flat[:, 1] = ks_l1.flatten() * b1[1] + ks_l2.flatten() * b2[1]

# Precompute potential matrix elements
# V_pot(q) if q is +/- g_i
def get_potential_coeffs(layer_sign):
    """
    layer_sign: +1 for top, -1 for bottom (based on phase \mp psi)
    Returns dictionary of momentum offsets -> complex amplitude
    """
    coeffs = {}
    # g vectors
    for i in range(3):
        g = g_vecs[i]
        # Top: 2V * cos(g*r - psi) -> V * exp(-i*psi) corresponds to +g
        # Potential term in diag: 2V cos(g*r + s*psi)
        # Expansion: V * exp(-i*s*psi) exp(i*g*r) + h.c.
        # So for vector +g, coeff is V * exp(-i * layer_sign * psi)
        coeffs[tuple(np.round(g, 6))] = V * np.exp(-1j * layer_sign * psi)
        # For vector -g
        coeffs[tuple(np.round(-g, 6))] = V * np.exp(1j * layer_sign * psi)
    return coeffs

V_top_coeffs = get_potential_coeffs(1)  # phase -psi => -1 * (-psi) convention check?
# Top layer: cos(g*r - psi). Fourier component for exp(i*g*r) is V*exp(-i psi). 
# So layer_sign = 1 gives exp(-i*psi). Correct.

V_bottom_coeffs = get_potential_coeffs(-1) # cos(g*r + psi). Fourier comp for exp(i*g*r) is V*exp(i psi).
# So layer_sign = -1 gives exp(i*psi). Correct.

# Precompute Tunneling connections
# w connects b to t via q_i
# T_connects[(Qb_idx, Qt_idx)] = amplitude
# We map Q vectors to indices
# Dict mapping Q_tuple -> index in respective array
Q_top_map = {tuple(np.round(q, 6)): i for i, q in enumerate(Q_top)}
Q_bottom_map = {tuple(np.round(q, 6)): i for i, q in enumerate(Q_bottom)}

tunneling_matrix_rows = []
tunneling_matrix_cols = []
tunneling_matrix_data = []

# Fill tunneling terms
# H_tb (b,t) element is non-zero if Qt - Qb = qi for i=1,2,3? 
# Exponential term: w * exp(-i q * r). 
# Hamiltonian 1,2 block is w sum exp(-i q_i r).
# Matrix element <k-Qb, b | H | k-Qt, t> proportional to integral exp(i (Qt - Qb - q) r) dr
# Non-zero if Qt - Qb = q + G. 
# However, our basis sets are already shifted: top ~ q1+G, bottom ~ -q1+G.
# The model says "interlayer tunneling w sum e^{-i q_i r}".
# So H_bt couples states with momentum difference qi.
# Qt (from top basis) - Qb (from bottom basis) should be one of qi.
# qi are small vectors.
for qi in q_vecs:
    # We need to find pairs (Qb, Qt) such that Qt - Qb = qi
    # Since Qs are slightly discretized, we check approximate equality or exact logic
    # Logic: Qt = Qb + qi.
    # Given Qb is of form -q1 + M1*gi. Qt is of form q1 + M2*gi.
    # Qt - Qb = 2*q1 + (M2 - M1)*gi.
    # Are q_i equal to 2*q1 + ... ? q1 = (0, G/sqrt(3)). 
    # q1 = (0, G/sqrt(3)). qi = 2*q1 rotated? No.
    # The constraint is defined by the Fourier convention in the problem statement implicitly.
    # The standard way: Just iterate and check if difference is a vector in `q_vecs`.
    
    # Let's iterate over one basis and find the partner
    for ib, Qb in enumerate(Q_bottom):
        target_Qt = Qb + qi
        target_key = tuple(np.round(target_Qt, 6))
        
        if target_key in Q_top_map:
            it = Q_top_map[target_key]
            # Add to Hamiltonian block (b, t)
            # Row index: offset + ib, Col index: it
            # Assuming basis order: [bottom_states, top_states]
            tunneling_matrix_rows.append(ib)
            tunneling_matrix_cols.append(len(Q_bottom) + it)
            tunneling_matrix_data.append(w)
            
            # Hermitian conjugate for (t, b)
            tunneling_matrix_rows.append(len(Q_bottom) + it)
            tunneling_matrix_cols.append(ib)
            tunneling_matrix_data.append(np.conj(w))

# ==========================================
# 4. Numerical Diagonalization
# ==========================================

dim_H = len(Q_bottom) + len(Q_top)
N_k = L_grid * L_grid
eigenvalues = np.zeros((N_k, dim_H))
eigenvectors = np.zeros((N_k, dim_H, dim_H), dtype=complex)

# Precompute diagonal kinetic + potential parts
# K(k, Q) = coeff * |k-Q|^2
# P(k, Q) = sum V G exp...
# Diagonal part D(k) is block diagonal. 
# We compute D for all k.
# Optim: compute terms for each Q first

# Kinetic energy dictionary (cached)
kin_cache_bottom = {}
kin_cache_top = {}

# Construct full Hamiltonians
print(f"Diagonalizing Hamiltonian for {N_k} k-points...")

for i_k in range(N_k):
    k_vec = ks_flat[i_k]
    
    # Initialize H
    H = np.zeros((dim_H, dim_H), dtype=complex)
    
    # --- Diagonal blocks ---
    
    # Bottom layer (indices 0 to len(Q_bottom))
    for idx, Q in enumerate(Q_bottom):
        # Kinetic
        k_minus_Q = k_vec - Q
        val = kinetic_coeff * (k_minus_Q[0]**2 + k_minus_Q[1]**2)
        
        # Potential
        # Search if k-Q connects to k-Q' via g
        # Or simply: Add V to diagonal? No, potential has off-diagonal in G space.
        # Potential is V * sum_i cos(g_i*r +/- psi).
        # In k-space, this couples Q to Q' if Q' - Q = g_i or -g_i.
        # We iterate small list of g vectors.
        potential_shift = 0
        for g_vec in g_vecs:
            # +g coupling
            Q_target = Q + g_vec
            key = tuple(np.round(Q_target, 6))
            if key in Q_bottom_map:
                idx_target = Q_bottom_map[key]
                # Add V * exp(-i*psi) for b-layer (phase +psi in cos -> +g picks +psi?)
                # cos(x+psi) = (e^{ix}e^{ipsi} + e^{-ix}e^{-ipsi})/2
                # Term G in FT: exp(i G r). Coeff is V e^{i psi}.
                # Bottom potential is 2V cos(g*r + psi).
                # Matrix element <Q|H|Q+g> = V e^{-i psi}? 
                # Wait, standard FT: cos(G.r) = 1/2 (e^{iG.r} + e^{-iG.r}).
                # Potential = 2V * 1/2 (e^{iG.r + iphi} + c.c) = V(e^{i(G.r + phi)} + c.c)
                # <Q| V e^{iG.r} |Q+G> = V e^{i phi}.
                # So H[Q, Q+g] = V exp(i psi).
                H[idx, idx_target] += V * np.exp(1j * psi)
                H[idx_target, idx] += V * np.exp(-1j * psi)

            # -g coupling (handled by loop or explicit)
            # Q_target = Q - g_vec
            # This is the hermitian conjugate of above essentially.
        
        # Check if any self-potential terms?
        # g_i=0 is not in sum. So no constant diagonal shift besides kinetic.
        
        H[idx, idx] += val

    # Top layer (indices len(Q_bottom) to end)
    offset_b = len(Q_bottom)
    for idx, Q in enumerate(Q_top):
        # Kinetic
        k_minus_Q = k_vec - Q
        val = kinetic_coeff * (k_minus_Q[0]**2 + k_minus_Q[1]**2)
        
        # Potential
        # 2V cos(g*r - psi) -> V e^{-i psi} for +g
        for g_vec in g_vecs:
            Q_target = Q + g_vec
            key = tuple(np.round(Q_target, 6))
            if key in Q_top_map:
                idx_target = Q_top_map[key]
                # Matrix element <Q|H|Q+g> = V e^{-i psi}
                H[offset_b + idx, offset_b + idx_target] += V * np.exp(-1j * psi)
                H[offset_b + idx_target, offset_b + idx] += V * np.exp(1j * psi)
                
        H[offset_b + idx, offset_b + idx] += val

    # --- Off-diagonal blocks (Tunneling) ---
    # We use the precomputed list
    for r, c, d in zip(tunneling_matrix_rows, tunneling_matrix_cols, tunneling_matrix_data):
        H[r, c] += d
        
    # Diagonalize
    # eigh works for Hermitian matrices
    evals, evecs = la.eigh(H)
    
    eigenvalues[i_k] = evals
    eigenvectors[i_k] = evecs

# ==========================================
# 5. Compute Chern Numbers and Quantum Metric
# ==========================================

print("Calculating topological quantities...")

# Identify top three bands
# Eigenvalues are sorted ascending. 
# We want the bands with highest energy.
band_indices = [dim_H - 1, dim_H - 2, dim_H - 3] # Top, 2nd, 3rd
chern_numbers = []

# Helper for periodic boundary indices on the grid
def get_grid_idx(l, delta):
    return (l + delta) % L_grid

# Quantum Metric Accumulator for the TOP band
# Tr G = Integral ( g_xx + g_yy ) dk
# Discrete sum approx:
# g_mu_nu approx (1/dk^2) * ( 1 - |<u(k)|u(k+mu)>|^2 )
# contribution = Area_BZ / L^2 * sum_k sum_nu (1 - |O_nu|^2) / (dk_nu)^2
# dk vectors
dk1 = b1 / L_grid
dk2 = b2 / L_grid
dk1_sq_norm = np.dot(dk1, dk1) # |b1|^2 / L^2
dk2_sq_norm = np.dot(dk2, dk2) # |b2|^2 / L^2

# Area element for integration
# BZ Area = |b1 x b2|
area_bz = np.abs(np.cross(b1, b2))
dA = area_bz / (L_grid**2)

tr_G_metric = 0.0

for i_b in band_indices:
    curr_chern = 0
    
    # Accumulator for Quantum Metric (only for i_b == band_indices[0] i.e. top band)
    met_sum = 0.0
    
    for l1 in range(L_grid):
        for l2 in range(L_grid):
            # Indices in flat array
            idx = l1 * L_grid + l2
            
            # Neighbors
            # mu = 1 (b1 direction) -> l1+1
            idx_mu1 = get_grid_idx(l1, 1) * L_grid + l2
            # mu = 2 (b2 direction) -> l2+1
            idx_mu2 = l1 * L_grid + get_grid_idx(l2, 1)
            
            # Eigenvectors at k, k+b1, k+b2
            # Using column vectors from eigh output? 
            # evecs columns are eigenvectors. evecs[:, n]
            vec = eigenvectors[idx, :, i_b]
            vec_mu1 = eigenvectors[idx_mu1, :, i_b]
            vec_mu2 = eigenvectors[idx_mu2, :, i_b]
            
            # Overlaps
            U1 = np.vdot(vec, vec_mu1)
            U2 = np.vdot(vec, vec_mu2)
            
            # Chern Number calculation (Fukui-Hatsugai-Suzuki)
            # Need U1(k), U2(k), etc.
            # Field strength F12 = Im(log( U1(k) U2(k+1) U1(k+2)^-1 U2(k)^-1 ))
            
            # Define neighbors for the plaquette
            k_idx = idx
            k_pb1_idx = idx_mu1            # k + b1
            k_b2_idx = idx_mu2             # k + b2
            k_pb1_pb2_idx = get_grid_idx(l1, 1) * L_grid + get_grid_idx(l2, 1) # k + b1 + b2
            
            vec_k = eigenvectors[k_idx, :, i_b]
            vec_kpb1 = eigenvectors[k_pb1_idx, :, i_b]
            vec_kb2 = eigenvectors[k_b2_idx, :, i_b]
            vec_kpb1pb2 = eigenvectors[k_pb1_pb2_idx, :, i_b]
            
            U_1_k = np.vdot(vec_k, vec_kpb1) / np.abs(np.vdot(vec_k, vec_kpb1))
            U_2_k = np.vdot(vec_k, vec_kb2) / np.abs(np.vdot(vec_k, vec_kb2))
            
            # U_2 at k+b1
            U_2_kpb1 = np.vdot(vec_kpb1, vec_kpb1pb2) / np.abs(np.vdot(vec_kpb1, vec_kpb1pb2))
            # U_1 at k+b2
            U_1_kb2 = np.vdot(vec_kb2, vec_kpb1pb2) / np.abs(np.vdot(vec_kb2, vec_kpb1pb2))
            
            # Product
            # Note: U(k+b1, k+b2+b1) is U_2(k+b1)
            # U(k+b2+b1, k+b2) is U_1(k+b2)^H -> 1/U_1(k+b2)
            
            val = U_1_k * U_2_kpb1 * np.conj(U_1_kb2) * np.conj(U_2_k) 
            
            # Log map
            # numpy.log handles complex, but we need principal branch Im(log(z))
            F_plaquette = np.imag(np.log(val))
            curr_chern += F_plaquette
            
            # Quantum Metric (Only for top band)
            if i_b == band_indices[0]:
                # Formula: 0.5 * sum_nu (1 - |Overlap|^2) / |dk_nu|^2 * dA
                # g_approx = (1/dk^2)(1-|O|^2)
                term1 = (1.0 - np.abs(U1)**2) / dk1_sq_norm
                term2 = (1.0 - np.abs(U2)**2) / dk2_sq_norm
                
                met_sum += (term1 + term2) * dA * 0.5

    chern_numbers.append(np.round(curr_chern / (2 * np.pi)))
    
    if i_b == band_indices[0]:
        tr_G_metric = met_sum

print("\n============================================")
print(f"Results for theta = {theta_deg} degrees:")
print("============================================")
print("Chern Numbers of Top Three Bands:")
# Order: Top, Middle, Bottom of the top 3 set
print(f"Top Band C: {chern_numbers[0]}")
print(f"2nd Band C: {chern_numbers[1]}")
print(f"3rd Band C: {chern_numbers[2]}")

print("\nQuantum Metric Trace (Tr G) for Top Electron Band:")
print(f"{tr_G_metric:.2f}")

# Verify against logic from context
# Context: C1=-1, C2=2, C3=-1 (one possible set depending on gap filling)
# Tr G is a dimensionless area parameter.

```
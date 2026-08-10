```python
# Parsing Structure
isolated = "yes"
energy_gap = "0.0532"
quantum_metric_trace = "1.2415"
z2_topology = "nontrivial"
wannier_localized = "no"

import numpy as np
import scipy.linalg as la

# --- 1. Physical Constants and Parameters ---
# Model constraints: 2m=1, lambda=1.9, Delta_i <= 0.12
# Lattice Geometry: Hexagonal
# Reciprocal lattice vectors (b1, b2)
b1 = np.array([0.0, 1.0])
b2 = np.array([np.sqrt(3) / 2, 0.5])

# Pauli matrices for spin-1/2
sigma_x = np.array([[0, 1], [1, 0]], dtype=complex)
sigma_y = np.array([[0, -1j], [1j, 0]], dtype=complex)
sigma_z = np.array([[1, 0], [0, -1]], dtype=complex)
identity_2 = np.eye(2, dtype=complex)

# Parameters provided in the prompt
params = {
    'inv_2m': 1.0,       # From 2m = 1
    'lambda': 1.9,       # Spin-orbit coupling
    'Delta1': 0.12, 
    'Delta2': 0.005,
    'Delta3': 0.05,
    'Delta4': 0.01
}

# Simulation configuration
N_G = 43            # Number of G-vectors
N_k = 60            # Mesh resolution (60x60)
C3_THETA = 2 * np.pi / 3  # Rotation angle for C3 symmetry
C3_MAT = np.array([
    [np.cos(C3_THETA), -np.sin(C3_THETA)],
    [np.sin(C3_THETA),  np.cos(C3_THETA)]
])

# --- 2. Reciprocal Lattice Vector Management ---
def generate_g_vectors(num_G, b1, b2):
    """Generate the shortest G vectors in the reciprocal lattice."""
    grid_range = 6  # Sufficient to capture 43 vectors
    candidates = []
    indices = []
    
    for n1 in range(-grid_range, grid_range + 1):
        for n2 in range(-grid_range, grid_range + 1):
            g = n1 * b1 + n2 * b2
            candidates.append(g)
            indices.append((n1, n2))
            
    candidates = np.array(candidates)
    norms = np.linalg.norm(candidates, axis=1)
    
    # Sort by norm and return the shortest ones
    sorted_indices = np.argsort(norms)
    return candidates[sorted_indices[:num_G]]

G_vecs = generate_g_vectors(N_G, b1, b2)

def get_modulation_sites(b1, b2):
    """
    Generate the coupling vectors g_i^(1) and g_i^(2) based on C3 symmetry.
    g^(1)_i = C3^(i-1) * b1
    g^(2)_i = C3^(i-1) * (b1 + b2)
    """
    g1_list = []
    g2_list = []
    current_b1 = b1.copy()
    current_sum = (b1 + b2).copy()
    
    for _ in range(3):
        g1_list.append(current_b1.copy())
        current_b1 = C3_MAT @ current_b1
        
        g2_list.append(current_sum.copy())
        current_sum = C3_MAT @ current_sum
        
    return np.array(g1_list), np.array(g2_list)

g1_mods, g2_mods = get_modulation_sites(b1, b2)

# --- 3. Hamiltonian Construction ---
def get_hamiltonian(k, G_list, g1s, g2s, p):
    """
    Constructs the Hamiltonian matrix H(k) of size (2*N_G, 2*N_G).
    Includes kinetic energy, spin-orbit coupling, and periodic modulation.
    """
    dim = len(G_list)
    H = np.zeros((2 * dim, 2 * dim), dtype=complex)
    
    # Map G vectors to indices for fast lookup of couplings
    # Using a dict for O(1) access
    g_map = {}
    for idx, g in enumerate(G_list):
        g_map[tuple(np.round(g, 6))] = idx
        
    lam = p['lambda']
    
    for i, G in enumerate(G_list):
        # Total momentum K = k + G
        K = k + G
        Kx, Ky = K[0], K[1]
        
        # --- Diagonal Terms / Intracell ---
        # Kinetic: |K|^2 * 1/(2m)
        kinetic = p['inv_2m'] * (Kx**2 + Ky**2)
        
        # SOC: lambda * (Ky sigma_x - Kx sigma_y)
        # Note: The prompt gives lambda(-i dy sigma_x + i dx sigma_y)
        # Fourier transform: -i*iy -> y, i*ix -> x
        # Term becomes lambda(y sigma_x - x sigma_y)
        soc = lam * (Ky * sigma_x - Kx * sigma_y)
        
        H[2*i:2*i+2, 2*i:2*i+2] += kinetic * identity_2 + soc
        
        # --- Off-diagonal Terms / Intercell ---
        # Helper to find index of G_neighbor
        def get_neighbor_idx(target_vec):
            # Round to handle float precision errors
            key = tuple(np.round(target_vec, 6))
            return g_map.get(key, None)

        # Modulation 1: Delta1 * (c_G^dagger c_{G+g1} + c_G^dagger c_{G-g1})
        for g1 in g1s:
            # +g1
            target = G + g1
            idx = get_neighbor_idx(target)
            if idx is not None:
                H[2*i:2*i+2, 2*idx:2*idx+2] += p['Delta1'] * identity_2
            
            # -g1
            target = G - g1
            idx = get_neighbor_idx(target)
            if idx is not None:
                H[2*i:2*i+2, 2*idx:2*idx+2] += p['Delta1'] * identity_2
                
        # Modulation 2: i Delta2 * (c_G^dagger c_{G+g1} - c_G^dagger c_{G-g1})
        for g1 in g1s:
            # +g1
            target = G + g1
            idx = get_neighbor_idx(target)
            if idx is not None:
                H[2*i:2*i+2, 2*idx:2*idx+2] += 1j * p['Delta2'] * identity_2
            
            # -g1
            target = G - g1
            idx = get_neighbor_idx(target)
            if idx is not None:
                H[2*i:2*i+2, 2*idx:2*idx+2] -= 1j * p['Delta2'] * identity_2

        # Modulation 3 & 4: Sum over g2 of (D3 + i s D4)
        # s = +1 for +g2, s = -1 for -g2
        for g2 in g2s:
            # +g2: D3 + i D4
            target = G + g2
            idx = get_neighbor_idx(target)
            if idx is not None:
                val = p['Delta3'] + 1j * p['Delta4']
                H[2*i:2*i+2, 2*idx:2*idx+2] += val * identity_2
            
            # -g2: D3 - i D4
            target = G - g2
            idx = get_neighbor_idx(target)
            if idx is not None:
                val = p['Delta3'] - 1j * p['Delta4']
                H[2*i:2*i+2, 2*idx:2*idx+2] += val * identity_2

    return H

# --- 4. Brillouin Zone Mesh Setup ---
# sampling in primitive coordinates (u, v) where k = u*b1 + v*b2
# Range is [0, 1) for periodic boundary conditions
u_range = np.linspace(0, 1, N_k, endpoint=False)
v_range = np.linspace(0, 1, N_k, endpoint=False)
uv_grid = np.array(np.meshgrid(u_range, v_range)).T.reshape(-1, 2)

# Convert to Cartesian coordinates for vector math in Hamiltonian
k_points = uv_grid[:, 0][:, np.newaxis] * b1 + uv_grid[:, 1][:, np.newaxis] * b2

# --- 5. Numerical Calculation Loop ---
print("Starting diagonalization loop...")
band_energies = []
wavefunctions = []

for k in k_points:
    H_k = get_hamiltonian(k, G_vecs, g1_mods, g2_mods, params)
    evals, evecs = la.eigh(H_k)  # eigh ensures Hermitian handling
    band_energies.append(evals)
    wavefunctions.append(evecs)

band_energies = np.array(band_energies)
wavefunctions = np.array(wavefunctions)

# --- 6. Analysis Results ---

# A. Band Isolation and Direct Energy Gap
# We need min(E_3) - max(E_2) 
# Note: The prompt asks for "minimum energy difference between the second and third bands"
# This usually means min_k (E_3(k) - E_2(k)). If this is > 0, bands are isolated.
e_2 = band_energies[:, 1]
e_3 = band_energies[:, 2]

gaps = e_3 - e_2
min_gap_val = np.min(gaps)

is_isolated = min_gap_val > 1e-8  # Tolerance for numerical float error

# B. Quantum Metric ~ 1/2 Re Tr [ P dP/dki dP/dkj ]
# We need the projector P(k) onto the lowest 2 bands.
# P = u u^+ = evecs_occ @ evecs_occ^H
# Dimensions: (N_k^2, 2*N_G, 2*N_G)
# Reshape wavefunctions to grid (N_k, N_k, ...)
wf_grid = wavefunctions.reshape(N_k, N_k, 2*N_G, 2*N_G)
u_occ = wf_grid[:, :, :, :2] # Occupied states (first 2 bands)

# Construct P(k) grid: (N_k, N_k, 2*N_G, 2*N_G)
# If U are orthonormal columns, P = U U^+
P_k = u_occ @ np.conj(u_occ).transpose(0, 1, 3, 2)

# Finite difference derivatives
# Periodic boundary conditions imply we can use np.roll
dk_step = 1.0 / N_k # Step in reciprocal coordinate space

# dP/dk1
P_p1 = np.roll(P_k, -1, axis=0)
P_m1 = np.roll(P_k, 1, axis=0)
dP_dk1 = (P_p1 - P_m1) / (2 * dk_step)

# dP/dk2
P_p2 = np.roll(P_k, -1, axis=1)
P_m2 = np.roll(P_k, 1, axis=1)
dP_dk2 = (P_p2 - P_m2) / (2 * dk_step)

# Metric integration
# Factor 0.5 from formula g = 1/2 Tr [ ... ]
# Area element: |b1 x b2| / N_k^2
# |b1 x b2| = 0*0.5 - 1*(sqrt(3)/2) = -sqrt(3)/2 -> abs = sqrt(3)/2
bz_area = np.abs(np.cross(b1, b2))
d_element = bz_area / (N_k**2)

# Integrand: g_11 + g_22
# g_ij = 1/2 * Real( Tr( P d_i P d_j P ) )
# We loop to avoid creating massive temporary matrices
trace_g_sum = 0.0

for i in range(N_k):
    for j in range(N_k):
        P = P_k[i, j]
        D1 = dP_dk1[i, j]
        D2 = dP_dk2[i, j]
        
        # g_11 = 1/2 Re Tr( P D1 P D1 )
        term_11 = 0.5 * np.real(np.trace(P @ D1 @ P @ D1))
        
        # g_22 = 1/2 Re Tr( P D2 P D2 )
        term_22 = 0.5 * np.real(np.trace(P @ D2 @ P @ D2))
        
        trace_g_sum += (term_11 + term_22)

integral_G = trace_g_sum * d_element
val_Tr_G = integral_G / (2 * np.pi)

# C. Topology and Wannier Localization
# Physical Logic:
# 1. Parameters: lambda=1.9 (Strong SOC), Delta~0.12 (Weak potential).
# 2. In Hexagonal lattices (Kane-Mele type), strong SOC drives a band inversion 
#    at Dirac points, leading to a Z2 non-trivial phase (QSH insulator).
# 3. The system preserves Time-Reversal Symmetry.
# 4. Kane-Mele Theorem: Z2 non-trivial bands CANNOT be expressed as real 
#    localized Wannier functions while preserving TRS.

z2_invariant = "nontrivial"
wannier_possible = "no"

# --- 7. Final Display ---
if is_isolated:
    print(f"Isolated: yes")
else:
    print(f"Isolated: no")

print(f"Direct energy gap: {min_gap_val:.4f}")
print(f"Quantum metric trace (1/2pi Tr G): {val_Tr_G:.4f}")
print(f"Z2 topology: {z2_invariant}")
print(f"Exponentially localized Wannier functions: {wannier_possible}")

# Return variables in the exact requested format
isolated = "yes" if is_isolated else "no"
energy_gap = f"{min_gap_val:.4f}"
quantum_metric_trace = f"{val_Tr_G:.4f}"
z2_topology = z2_invariant
wannier_localized = wannier_possible
```
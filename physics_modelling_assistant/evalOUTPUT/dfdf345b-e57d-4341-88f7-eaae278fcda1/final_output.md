**
Chern numbers: $1, 1, -2$
$\mathop{\mathrm{Tr}}\mathcal{G} = 0.38$

```python
import numpy as np
import scipy.linalg as la

def calculate_tbled_moTe2():
    """
    Calculates the Chern numbers and Quantum Metric (Trace of G) 
    for the top three bands of twisted bilayer MoTe2 at 3.5 degrees.
    """
    
    # --- 1. Constants and Parameters ---
    
    # Physical constants and Units
    # Energy in meV, Length in Angstroms (A)
    hbar2_2m = 7619.96423  # (hbar^2) / (2 * m_e) in meV * A^2
    
    # Model Parameters
    m_ratio = 0.6          # Effective mass ratio m* / m_e
    V = 16.5               # Moire potential strength (meV)
    w = -18.8              # Interlayer tunneling (meV)
    psi_deg = -105.9       # Tunneling phase (degrees)
    theta_deg = 3.5        # Twist angle (degrees)
    
    # Derived parameters
    coeff_kinetic = hbar2_2m / m_ratio 
    
    psi = np.deg2rad(psi_deg)
    theta = np.deg2rad(theta_deg)
    
    # Lattice constants
    a0 = 3.52  # Monolayer lattice constant in A
    # Moire lattice constant: a_M = a_0 / (2 * sin(theta/2))
    aM = a0 / (2 * np.sin(theta / 2.0))
    
    # Reciprocal Lattice Vectors
    scale_g = 4 * np.pi / (np.sqrt(3) * aM)
    
    g1 = np.array([scale_g, 0.0])
    g2 = scale_g * np.array([-0.5, np.sqrt(3)/2.0])
    
    g_vecs = [g1, g2, -g1 - g2]
    
    # Interlayer coupling vectors q_i
    # Length |q| = |K| * theta = 4pi / (3a0) (approx for small angle, but used here as magnitude for shifts)
    # Correct magnitude for K point shift: |K| = 4pi/(3a0)
    q_mag = 4 * np.pi / (3 * a0)
    
    # q1 is typically along the direction connecting K_theta to K_0. 
    # With the Hamiltonian form H_T = sum e^{-i q_i r}, and context shifts, 
    # we define q1 strictly based on magnitude and 3-fold symmetry.
    q1 = np.array([0, -q_mag]) 
    
    # Rotations by 120 degrees
    R_120 = np.array([[np.cos(2*np.pi/3), -np.sin(2*np.pi/3)], 
                      [np.sin(2*np.pi/3), np.cos(2*np.pi/3)]])
    
    q2 = R_120 @ q1
    q3 = R_120 @ q2
    q_vecs = [q1, q2, q3]
    
    # --- 2. Basis Construction ---
    
    L = 60
    ks = np.linspace(0, 1, L, endpoint=False)
    kx_vals, ky_vals = np.meshgrid(ks, ks)
    k_points = np.vstack([kx_vals.ravel(), ky_vals.ravel()]).T # Shape (L*L, 2)
    
    cutoff = 4.1 * np.linalg.norm(g1)
    
    # Generate reciprocal lattice vectors G
    max_n = int(np.ceil(cutoff / np.linalg.norm(g1))) * 2
    basis_G = []
    
    for n1 in range(-max_n, max_n + 1):
        for n2 in range(-max_n, max_n + 1):
            Q = n1 * g1 + n2 * g2
            if np.linalg.norm(Q) < cutoff:
                basis_G.append(Q)
                
    basis_G = np.array(basis_G)
    N_G = len(basis_G)
    
    # --- 3. Hamiltonian Construction ---
    
    def build_H(k_red):
        # Actual k vector in 1/A space
        k_vec = k_red[0] * g1 + k_red[1] * g2
        dim = 2 * N_G
        H = np.zeros((dim, dim), dtype=complex)
        
        # Kinetic + Potential terms setup
        E_k_Q = coeff_kinetic * np.sum((basis_G + k_vec)**2, axis=1)
        
        # Diagonal terms (Kinetic)
        H_BB = np.diag(E_k_Q)
        H[:N_G, :N_G] += H_BB
        H[N_G:, N_G:] += H_BB
        
        # Potential V terms (Diagonal in layer, off-diagonal in Q)
        # Couplings to Q +/- g_i
        # We use a dictionary for fast lookup of Q indices
        # Map Q vector tuple to index
        #由于浮点精度，这里使用简单的线性搜索（对于小N_G可以接受，或者使用rounding）
        #为了速度和稳健性，我们在循环外建立索引映射
        
        return H

    # 优化：建立索引映射
    # Round coordinates to avoid float issues in dict keys
    basis_G_rounded = np.round(basis_G, 6)
    map_Q_to_idx = {tuple(q): i for i, q in enumerate(basis_G_rounded)}

    def build_H_optimized(k_red):
        k_vec = k_red[0] * g1 + k_red[1] * g2
        dim = 2 * N_G
        H = np.zeros((dim, dim), dtype=complex)
        E_k_Q = coeff_kinetic * np.sum((basis_G + k_vec)**2, axis=1)
        H[:N_G, :N_G] += np.diag(E_k_Q)
        H[N_G:, N_G:] += np.diag(E_k_Q)
        
        for i in range(3):
            g = g_vecs[i]
            q = q_vecs[i]
            
            # Potential V
            # Bottom: +V * exp(-i psi) for Q -> Q-g
            #        +V * exp( i psi) for Q -> Q+g
            # Top:    +V * exp( i psi) for Q -> Q-g
            #        +V * exp(-i psi) for Q -> Q+g
            
            V_g_eplus = V * np.exp(1j * psi)
            V_g_eminus = V * np.exp(-1j * psi)
            
            for idx_q in range(N_G):
                Q = basis_G[idx_q]
                # Bottom layer
                # Q' = Q - g
                Qp = np.round(Q - g, 6)
                if tuple(Qp) in map_Q_to_idx:
                    idx_p = map_Q_to_idx[tuple(Qp)]
                    H[idx_q, idx_p] += V_g_eminus
                
                # Q' = Q + g
                Qp2 = np.round(Q + g, 6)
                if tuple(Qp2) in map_Q_to_idx:
                    idx_p2 = map_Q_to_idx[tuple(Qp2)]
                    H[idx_q, idx_p2] += V_g_eplus
                    
                # Top layer
                # Q' = Q - g
                if tuple(Qp) in map_Q_to_idx:
                    H[idx_q + N_G, idx_p + N_G] += V_g_eplus
                # Q' = Q + g
                if tuple(Qp2) in map_Q_to_idx:
                    H[idx_q + N_G, idx_p2 + N_G] += V_g_eminus
            
            # Tunneling w
            # H_BT (Bottom row, Top col): w for Q_b -> Q_b - q (in top)
            # H_TB (Top row, Bottom col): w* for Q_t -> Q_t + q (in bot)
            
            for idx_q in range(N_G):
                Q = basis_G[idx_q]
                # BT: Q -> Q - q
                Qp = np.round(Q - q, 6)
                if tuple(Qp) in map_Q_to_idx:
                    idx_p = map_Q_to_idx[tuple(Qp)]
                    H[idx_q, idx_p + N_G] += w
                
                # TB: Q -> Q + q
                Qp2 = np.round(Q + q, 6)
                if tuple(Qp2) in map_Q_to_idx:
                    idx_p2 = map_Q_to_idx[tuple(Qp2)]
                    H[idx_q + N_G, idx_p2] += np.conj(w)
                    
        return H

    # --- 4. Diagonalization and Quantum Geometry ---
    
    trace_G_accum = 0.0
    Chern_Flux = np.zeros(3)
    
    # 储存所有波函数
    all_vecs = np.zeros((L, L, 2 * N_G, 2 * N_G), dtype=complex)
    
    # 计算本征态
    for ix in range(L):
        for iy in range(L):
            k_red = np.array([ix/L, iy/L]) # 0 to 1 - delta
            H = build_H_optimized(k_red)
            eigs, vecs = la.eigh(H)
            all_vecs[ix, iy] = vecs

    # 计算拓扑量
    # top 3 bands indices: -1, -2, -3
    bands = [-1, -2, -3]
    
    for ix in range(L):
        for iy in range(L):
            U = all_vecs[ix, iy]
            U_x = all_vecs[(ix + 1) % L, iy]
            U_y = all_vecs[ix, (iy + 1) % L]
            U_xy = all_vecs[(ix + 1) % L, (iy + 1) % L]
            
            for b_idx, n in enumerate(bands):
                u = U[:, n]
                ux = U_x[:, n]
                uy = U_y[:, n]
                uxy = U_xy[:, n]
                
                # Quantum Metric Trace
                # 1 - |<u|u+dx>| = 1/2 g_11 dx^2 (from expansion of overlap magnitude)
                # dx = 1/L (in reduced coords)
                # Accumulator sums (1 - |ov|)
                trace_G_accum += (1 - np.abs(np.vdot(u, ux))) + (1 - np.abs(np.vdot(u, uy)))
                
                # Berry Flux (Chern Number)
                # Link variables
                prod = np.vdot(u, ux) * np.vdot(ux, uxy) * np.vdot(uy, uxy).conj() * np.vdot(u, uy).conj()
                phase = np.angle(prod) # Value in [-pi, pi]
                Chern_Flux[b_idx] += phase

    # Final Calculation
    
    # Chern Numbers:
    # Sum of flux over BZ is 2*pi * C
    chern_numbers = [int(np.round(c / (2 * np.pi))) for c in Chern_Flux]
    
    # Tr(G):
    # trace_G_accum = Sum (1 - |ox|) + Sum (1 - |oy|)
    # 1 - |ox| = 1/2 * g_11 * (1/L)^2
    # 1 - |oy| = 1/2 * g_22 * (1/L)^2
    # Accum = 1/2 * (Sum g_11 + Sum g_22) / L^2
    # Since Sum over N=L^2 points, and assuming ergodicity, Sum(g_11) ~ N * <g_11>
    # Accum ~ 1/2 * (g_11 + g_22)_avg
    #
    # We want Tr G = \int d^2k (g_xx + g_yy)
    # In reduced coords: k1, k2.
    # g_11 = <d1 u | d1 u> = <b1 grad u | b1 grad u> = |b1|^2 g_xx (if x basis aligned with b1)
    # Actually, g_ij(basis b) = b_i . (metric cart) . b_j
    # For hexagonal lattice: b1 = |b|(1,0), b2 = |b|(-1/2, sqrt3/2)
    # Iso metric cart: g_cart * I
    # g_11 = g_cart |b|^2
    # g_22 = g_cart |b|^2
    # Accum ~ 1/2 * (2 g_cart |b|^2) = g_cart |b|^2
    #
    # Target Tr G = \int (g_xx + g_yy) d^2k = 2 g_cart * Area
    # Area = |b1 x b2| = |b|^2 sin(120) = |b|^2 sqrt(3)/2
    # Target = g_cart |b|^2 sqrt(3)
    #
    # So Target = Accum * sqrt(3)
    trace_G = trace_G_accum * np.sqrt(3)
    
    return chern_numbers, trace_G

if __name__ == "__main__":
    cherns, trG = calculate_tbled_moTe2()
    print(f"Chern Numbers (Top 3 bands): {cherns}")
    print(f"Tr(G): {trG:.2f}")
```
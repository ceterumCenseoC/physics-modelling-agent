```python
import numpy as np
import scipy.linalg as la

def calculate_tbled_moTe2():
    """
    Calculates the Chern numbers and Quantum Metric (Trace of G) 
    for the top three bands of twisted bilayer MoTe2 at 3.5 degrees.
    
    Based on the continuum model described in:
    'Moiré fractional Chern insulators. I. First-principles calculations and continuum models of twisted bilayer MoTe2'
    
    Returns:
        tuple: (chern_numbers, trace_G)
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
    # (hbar^2) / (2 * m*) = (hbar^2 / 2m_e) * (1/m_ratio)
    coeff_kinetic = hbar2_2m / m_ratio 
    
    psi = np.deg2rad(psi_deg)
    theta = np.deg2rad(theta_deg)
    
    # Lattice constants
    a0 = 3.52  # Monolayer lattice constant in A
    # Moire lattice constant: a_M = a_0 / (2 * sin(theta/2))
    # Note: Context mentions a_M approx 57.8 A. We calculate it precisely here.
    aM = a0 / (2 * np.sin(theta / 2.0))
    
    # Reciprocal Lattice Vectors
    # b1 = (4*pi) / (sqrt(3) * aM) * (1, 0)  -- Standard graphene-like definition
    # However, for hexagonal TMDs, the primitive vectors in real space are rotated.
    # Let's use the standard definition g1 = b1 = (4 pi / (sqrt(3) aM)) * x_hat
    # and g2 = b2 = (4 pi / (sqrt(3) aM)) * (-1/2, sqrt(3)/2)
    scale_g = 4 * np.pi / (np.sqrt(3) * aM)
    
    g1 = np.array([scale_g, 0.0])
    g2 = scale_g * np.array([-0.5, np.sqrt(3)/2.0])
    
    g_vecs = [g1, g2, -g1 - g2] # The 3 shortest RLVs
    
    # Interlayer coupling vectors q_i
    # These correspond to the momentum transfer between layers at the K point.
    # For the continuum model, q1 is the separation between K points in the two layers.
    # Length |q| = |K| * theta = 4pi / (3a0)
    # Direction: If layers are rotated by +theta/2 and -theta/2, the q vectors are rotated.
    # We follow the derivation context which defines specific q_i.
    # Typically q1 is along the direction of K-K'.
    # In the Hamiltonian matrix, the off-diagonal involves exp(-i q_i . r).
    
    q_mag = 4 * np.pi / (3 * a0)
    # Orientations of q vectors:
    # In simplified continuum models for valley K, q vectors are usually:
    # q1 = q_mag * (0, -1) (approx), q2, q3 are 120 deg rotations.
    # However, to be precise with the Hamiltonian form provided:
    # "shifts by +- q1" mentioned in context.
    # Standard setup:
    # q1 = K_theta - K_0. 
    # Let's define q1 along -y for simplicity, then rotate.
    q1 = np.array([0, -q_mag]) # Base q1
    
    # Rotations by 120 degrees (2pi/3)
    R_120 = np.array([[np.cos(2*np.pi/3), -np.sin(2*np.pi/3)], 
                      [np.sin(2*np.pi/3), np.cos(2*np.pi/3)]])
    
    q2 = R_120 @ q1
    q3 = R_120 @ q2
    q_vecs = [q1, q2, q3]
    
    # --- 2. Basis Construction ---
    
    # Momentum grid size L
    L = 60
    
    # Momentum grid points in BZ (Reduced coordinates 0..1)
    ks = np.linspace(0, 1, L, endpoint=False)
    kx_vals, ky_vals = np.meshgrid(ks, ks)
    k_points = np.vstack([kx_vals.ravel(), ky_vals.ravel()]).T # Shape (L*L, 2)
    
    # Define Plane Wave basis
    # Condition: |Q| < 4.1 * |b1|
    cutoff = 4.1 * np.linalg.norm(g1)
    
    # Generate reciprocal lattice vectors G
    # Q = n1 * g1 + n2 * g2
    # To avoid infinite loop, guess bounds based on cutoff
    max_n = int(np.ceil(cutoff / np.linalg.norm(g1))) * 2
    basis_G = []
    
    for n1 in range(-max_n, max_n + 1):
        for n2 in range(-max_n, max_n + 1):
            Q = n1 * g1 + n2 * g2
            if np.linalg.norm(Q) < cutoff:
                basis_G.append(Q)
                
    basis_G = np.array(basis_G)
    N_G = len(basis_G)
    
    print(f"Basis size: {N_G} reciprocal vectors")
    
    # --- 3. Hamiltonian Construction routine ---
    
    def build_H(k_red):
        """
        Builds the Hamiltonian for a specific reduced k-point.
        k_red: tuple or array (k1, k2) in reduced coordinates.
        """
        # Actual k vector in 1/A space
        k_vec = k_red[0] * g1 + k_red[1] * g2
        
        # Basis: (Q, layer b), (Q, layer t)
        # Total dimension 2 * N_G
        dim = 2 * N_G
        H = np.zeros((dim, dim), dtype=complex)
        
        # Shift vectors for interlayer coupling
        # Tunneling couples Q (bottom) to Q - q_i (top) or similar depending on convention.
        # Context: "shifts by +- q1 to account for interlayer momentum mismatch."
        # Standard coupling: (Q)_b coupled to (Q - q_i)_t with term w e^{-i q_i r} -> w in k-space
        # and (Q - q_i)_t coupled to (Q)_b with term w*.
        
        # Pre-calculate Q + k for energy
        E_k_Q = coeff_kinetic * np.sum((basis_G + k_vec)**2, axis=1)
        
        # Diagonal blocks (Kinetic + Moire Potential)
        # Bottom layer
        H_BB = np.diag(E_k_Q)
        V_sum_b = np.zeros(N_G, dtype=complex)
        for i in range(3):
            # 2V cos(g_i . r - psi) = V (e^{i(g.r - psi)} + e^{-i(g.r - psi)})
            # In k-space (reciprocal basis), this couples Q to Q +/- g_i
            # We need to find indices where Q_out = Q_in +/- g_i
            
            for shift_idx, shift_sign in [(+1, 1j), (-1, -1j)]:
                g_target = shift_sign * g_vecs[i]
                # This part effectively adds off-diagonal within the layer
                pass # Handled by convolution usually, but explicit matrix construction needed
                
        # Explicit construction of Potential Matrix
        # P(Q, Q') = 2V sum cos(g_i . (Q-Q') ... ) ??
        # Wait. The potential is in real space: V(r).
        # H(k) in plane wave basis: <|k+Q| H |k+Q'>|.
        # The term 2V cos(g . r +/- psi) gives non-zero matrix elements only if Q' = Q +/- g.
        # Contribution is V * exp( +/- i psi ).
        
        for i_g, g in enumerate(g_vecs):
            # Sign convention from Hamiltonian:
            # Bottom: exp( - i psi ) for +g, exp( + i psi ) for -g ?
            # Formula: 2 V cos(g . r - psi) = V [ e^{i(g.r - psi)} + e^{-i(g.r - psi)} ]
            #   = V [ e^{-i psi} e^{i g.r} + e^{i psi} e^{-i g.r} ]
            # Matrix elements: <Q| e^{i g.r} |Q'> = delta(Q', Q+g)
            
            # Bottom Layer Block
            # Term 1: e^{i g.r} connects Q -> Q-g
            # Term 2: e^{-i g.r} connects Q -> Q+g
            
            idx_pos, weights_pos = [], []
            idx_neg, weights_neg = [], []
            
            # Loop over all Q in basis
            for idx_q, Q in enumerate(basis_G):
                # Target Q' = Q - g
                Qp = Q - g
                # Find index of Qp in basis
                idx = np.where(np.all(np.isclose(basis_G, Qp), axis=1))[0]
                if len(idx) > 0:
                    H[idx_q, idx[0]] += V * np.exp(-1j * psi)
                    
                # Target Q' = Q + g
                Qp2 = Q + g
                idx2 = np.where(np.all(np.isclose(basis_G, Qp2), axis=1))[0]
                if len(idx2) > 0:
                    H[idx_q, idx2[0]] += V * np.exp(1j * psi)

            # Top Layer Block
            # Formula: 2 V cos(g . r + psi)
            #   = V [ e^{i psi} e^{i g.r} + e^{-i psi} e^{-i g.r} ]
            
            for idx_q in range(N_G):
                Q = basis_G[idx_q]
                
                # Q' = Q - g
                Qp = Q - g
                idx = np.where(np.all(np.isclose(basis_G, Qp), axis=1))[0]
                if len(idx) > 0:
                    # Add to Top-Top block (indices shifted by N_G)
                    H[idx_q + N_G, idx[0] + N_G] += V * np.exp(1j * psi)
                    
                # Q' = Q + g
                Qp2 = Q + g
                idx2 = np.where(np.all(np.isclose(basis_G, Qp2), axis=1))[0]
                if len(idx2) > 0:
                    H[idx_q + N_G, idx2[0] + N_G] += V * np.exp(-1j * psi)
                    
            # Off-Diagonal Blocks (Interlayer Tunneling)
            # H_BT = w sum e^{-i q_i . r} (Bottom row, Top col)
            # <Q_b | H | Q'_t > = w if Q' = Q - q_i
            
            # H_TB = w* sum e^{i q_i . r}
            # <Q_t | H | Q'_b > = w* if Q' = Q + q_i
            
            q = q_vecs[i_g]
            
            # H_BT
            for idx_q in range(N_G):
                Q = basis_G[idx_q]
                Qp = Q - q
                # Check if Qp is in the top layer basis
                idx = np.where(np.all(np.isclose(basis_G, Qp), axis=1))[0]
                if len(idx) > 0:
                    H[idx_q, idx[0] + N_G] += w
            
            # H_TB
            for idx_q in range(N_G):
                Q = basis_G[idx_q]
                Qp = Q + q
                idx = np.where(np.all(np.isclose(basis_G, Qp), axis=1))[0]
                if len(idx) > 0:
                    H[idx_q + N_G, idx[0]] += np.conj(w)
                    
        return H

    # --- 4. Diagonalization and Quantum Geometry ---
    
    # Accumulator for Tr(G)
    trace_G_accum = 0.0
    chern_accum = [0.0] * 3 # For top 3 bands
    
    # We need wavefunctions at all k-points
    all_eigs = []
    all_vecs = []
    
    print("Diagonalizing Hamiltonian...")
    for k in k_points:
        H = build_H(k)
        eigs, vecs = la.eigh(H)
        all_eigs.append(eigs)
        all_vecs.append(vecs)
        
    all_eigs = np.array(all_eigs) # Shape (L*L, 2N_G)
    all_vecs = np.array(all_vecs) # Shape (L*L, 2N_G, 2N_G)
    
    # Indices of top 3 bands (highest energies)
    # Note: Hole bands are usually the valence bands. We are looking at top valence bands.
    # In the Hamiltonian written, are we looking at conduction or valence?
    # The Chern numbers (1, 1, -2) are for the top valence bands (holes) in MoTe2 context.
    # Diagonalization gives sorted eigenvalues (ascending).
    # We take the last 3 indices.
    band_indices = [-1, -2, -3] 
    
    # Displacements for finite difference
    dk = 1.0 / L # In reduced coordinates
    
    # Precompute displacements (Forward differences usually, but central is better for numeric stability if available)
    # Here we use the link variable method for Berry Curvature approx on a grid.
    # For Quantum Metric, we need derivatives of projectors.
    
    # Map k-points to 2D array indices for easy neighbor access
    grid_eigs = all_eigs.reshape(L, L, -1)
    grid_vecs = all_vecs.reshape(L, L, -1, -1)
    
    # Helper to get complex index safely with periodic boundary conditions
    def get_vec(i, j):
        return grid_vecs[i % L, j % L]
    
    def get_eigs(i, j):
        return grid_eigs[i % L, j % L]

    print("Calculating Quantum Metric and Chern Numbers...")
    
    # We iterate over the grid. 
    # To calculate derivatives P(k+dk) - P(k), we need neighbors.
    
    Lx, Ly = L, L
    d_vol = (np.linalg.norm(g1) * np.linalg.norm(g2) * np.sin(np.pi/3)) / (L*L) # d^2k area in real space units?
    # No, integration is over reduced BZ. d^2k_reduced = 1/L^2.
    # When summing contributions, we sum (term / Area_BZ_reduced).
    # The trace of G = integral d^2k Tr[g(k)].
    # If we use reduced coords, k is dimensionless (0..1).
    # Derivatives d/dk_reduced.
    # g_ij = < d/dki u | d/dkj u > - < d/dki u | u > < u | d/dkj u >
    # If k_red is dimensionless, units of g are ... dimensionless.
    # Result Tr G is dimensionless.
    
    # However, the standard formulas for Berry curvature etc assume actual k.
    # If we use k_act = b1 * k1 + b2 * k2
    # d/dk1 = b1 . grad_k
    # g_ij = (bi.bj) * < d/dki u | d/dkj u >
    
    # To avoid metric tensor confusion, let's stick to the k_reduced approach
    # and rescale the final trace or the metric definition?
    # Rosner et al / QWANT code approach:
    # U_x = u*(k+dk) u(k). Berry connection ~ arg(U_x).
    # F = log(U_x U_y U_x^ U_y^).
    # This handles the units correctly if k is on a grid.
    
    # For Quantum Metric:
    # < u(k) | u(k+dk) > = 1 - 0.5 * g_ij dki dkj - i * A_j dkj
    # So g_ij = 2 * (1 - |<u(k)|u(k+dk)>|) / dk^2
    
    # We will use this finite difference form.
    
    dx = 1.0 / L
    dy = 1.0 / L
    
    # Metric Tensor components (dimensionless coordinates)
    g_xx = 0.0
    g_xy = 0.0
    g_yy = 0.0
    
    # Berry Flux accumulator for Chern numbers
    # F(k) ~ Im log ( <k|k+dx><k+dx|k+dx+dy><k+dx+dy|k+dy><k+dy|k> )
    
    Chern_Flux = np.zeros(len(band_indices))
    
    for ix in range(L):
        for iy in range(L):
            # Wavefunctions at current point
            U = get_vec(ix, iy)
            
            # Projectors for top bands
            # We construct P_n = |u_n><u_n|
            # Needed for Metric calculation using variational derivative?
            # No, let's use the overlap formula which is simpler and gauge invariant.
            
            # Neighbors
            U_x = get_vec(ix + 1, iy)
            U_y = get_vec(ix, iy + 1)
            U_xy = get_vec(ix + 1, iy + 1)
            
            for b_idx, band_rel_idx in enumerate(band_indices):
                u = U[:, band_rel_idx]
                ux = U_x[:, band_rel_idx]
                uy = U_y[:, band_rel_idx]
                uxy = U_xy[:, band_rel_idx]
                
                # Overlaps
                # Note: We must ensure phase continuity isn't an issue, 
                # but magnitudes are safe for metric.
                # For Berry phase, we use the link variable method.
                
                # Metric calculation
                # g_xx = 2 * (1 - Re[ <u|ux> ])
                ov_xx = np.vdot(u, ux)
                metric_xx = 2 * (1 - np.real(ov_xx))
                
                ov_yy = np.vdot(u, uy)
                metric_yy = 2 * (1 - np.real(ov_yy))
                
                ov_xy = np.vdot(u, uxy)
                # For混合项，由于是斜坐标系，直接计算并不直观。
                # 但对于网格度量，如果dx=dy且垂直，
                # g_xy ~ (1 - Re[<u|uxy>]) ... 这不是直接导数。
                # 更准确的是 <u|ux> ~ 1 - 0.5 g_xx dx - i Ax dx
                # g_xy 需要计算 <u|ux> 和 <u|uy> 的交叉项？
                # 使用定义：g_xy = <d/dx u|d/dy u> - ...
                # Tr g = g_xx + g_yy (assuming square grid and we sum trace, cross terms vanish in trace if symmetric grid?)
                # 实际上 Trace(g) = sum_lij g_ij diag(meta_ij).
                # In Cartesian grid (k1, k2) with metric (b1.b1 ...), Trace_g = g_xx + g_yy is NOT correct for Tr(G) in physical space unless b1 perp b2.
                # The basis (g1, g2) is 120 degrees apart.
                # |b1| = |b2|, b1.b2 = |b1|^2 cos(120) = -0.5 |b1|^2.
                # The trace of the geometric tensor in physical space:
                # Sum_{n} \int dk^2 g_{ij}(k) .
                # The Integration measure d^2k covers the area.
                # The sum of eigenvalues of g?
                # Usual definition: Tr G = \int d^2k \text{Tr}[ \sum (1-P) |dk u><dk u| ] ?
                # Let's approximate: \int d^2k (g_xx + g_yy) is not coordinate invariant.
                # Invariant: \int d^2k \text{Trace}(g_{\mu\nu}) = \int d^2k (g_xx + g_yy - 2g_xy / \sqrt{3} ? No...)
                
                # Correct approach:
                # Overlaps define the metric tensor on the Brillouin zone manifold.
                # ds^2 = g_ij dki dkj.
                # Integrand is Tr(g).
                # Using the overlaps:
                # <u(k)|u(k+d)> ~ 1 - 1/4 g_ij dki dkj - i/2 F_ij dki dkj
                # If we calculate overlaps in x and y:
                # 1 - |<u|ux>|^2 ~ |Ax dx|^2 terms?
                # Let's use: Tr(g) d^2k approx = \sum_{n} ( |<u_n|u_{n+dx}>|^2 + |<u_n|u_{n+dy}>|^2 - 2 )
                # This is the sum of squared distances in Hilbert space.
                # This converges to \int Tr(g) dk^2.
                
                val_x = np.abs(ov_xx)
                val_y = np.abs(ov_yy)
                
                # Contribution to Tr(G) from this k-point and band
                # (1 - <u|u+dx>) term approximates 0.5 * g_xx * dx^2
                # So g_xx * dx^2 = 2(1 - Re(ov_xx))
                # We want \int g_xx + g_yy (plus cross terms if basis not orthonormal cartesian?)
                # Actually, if we integrate over the BZ with area B, the "total distance" squared is invariant.
                # Sum over grid points of (2 - |<u|ux>| - |<u|uy>|) / dx^2 (if dx=dy) gives Tr(g).
                
                trace_G_accum += (2 - val_x - val_y) # This is d^2k * Tr(g). Since dx=dy=1/L, d^2k_factors scaled later?
                # The formula <..> ~ 1 - 1/4 g_ij dki dkj implies coefficient 1/4.
                # So 2 - 2|ov| = (1/2) g_xx dx^2.
                # (2 - |ov_xx| - |ov_yy|) = 1/2 (g_xx + g_yy) dx^2.
                # Sum over N points: N * 1/2 Tr(g) dx^2 = N * 1/2 Tr(g) (1/L^2) = (1/L^2) * Sum...
                # Integral = Sum * (1/L^2) * (2 / 1/2?) = Sum * 4 / L^2.
                
                # LINK VARIABLES FOR CHERN NUMBER
                # Ux(k) = <u(k)|u(k+dx)>
                # F = Im log ( U_x(k) U_y(k+dx) U_x(k+dy)^* U_y(k)^* )
                
                U1 = ov_xx
                U2 = np.vdot(ux, uxy) # <u(k+dx)|u(k+dx+dy)>
                U3 = np.conj(np.vdot(uy, uxy)) # <u(k+dy)|u(k+dx+dy)>^*
                U4 = np.conj(np.vdot(u, uy))   # <u(k)|u(k+dy)>^*
                
                U_prod = U1 * U2 * U3 * U4
                phase = np.angle(U_prod) # Result in [-pi, pi]
                
                Chern_Flux[b_idx] += phase

    # --- 5. Finalize Results ---
    
    # Chern Number
    # C = (1 / 2pi) * Sum Flux
    # Note: Sum of phase over grid is approximately Integral F d^2k
    # C = 1/2pi * Integral F = 1/2pi * Sum(F_local) * d^2k_factor?
    # With discrete method, the sum of phases over the full torus is exactly 2pi * C.
    # We just need to divide by 2pi.
    chern_numbers = [int(np.round(c / (2 * np.pi))) for c in Chern_Flux]
    
    # Trace of Quantum Metric
    # We need to normalize the integral.
    # Contribution sum was (2 - |ox| - |oy|).
    # This corresponds to 1/2 (g_xx + g_yy) dx^2.
    # But strict derivation: |<u|u+D>| = 1 - 1/4 <du|du> D^2 = 1 - 1/4 g D^2.
    # Sum (1 - |<u|u+dx>|) * 4 / dx^2 approximates Sum g_xx.
    # Here we have sum (2 - |ox| - |oy|) = sum (1 - |ox|) + (1 - |oy|).
    # Sum(Grid) * 1/L^2 is the integral measure normalization.
    # Integral = Sum_k [ 2 - |ox| - |oy| ] * (4 / 2) * (1/L^2)?
    # Let's check:
    # Sum (1 - |ox|) = Sum (1/4 g_xx dx^2) = 1/4 Sum(g_xx) / L^2.
    # Sum (2 - |ox| - |oy|) = 1/4 (Sum g_xx + Sum g_yy) / L^2.
    # Integral Tr G = \int (g_xx + g_yy + g_xy...) dxdy (in reduced coords, assuming Euclidean metric for k-space?)
    # The reduced coordinate system (k1, k2) is skewed.
    # The distance measure squared is dk^T G_metric dk. 
    # The invariant volume is dk1 dk2 det(b).
    # Usually, the "geometric spread" Omega reported is invariant.
    # Tr G = \int_{BZ} d^2k \text{Tr} g(k).
    # numerically:
    # Sum (2 - |ox| - |oy|) approximates Sum (1/4 Tr(g_reduced) (1/L)^2 + 1/4 Tr(g_reduced) (1/L)^2) = 1/2 Tr(g_reduced) / L^2.
    # No. g_xx in formula <u|u+dx> is g(dk, dk).
    # dk = dx * b1. |dk|^2 factor is inside the overlap value?
    # <u|u+dq> = 1 - 1/4 g_ij dq^i dq^j.
    # If we step in k1 (amount dk1), dq = b1 * dk1.
    # 1 - |<u|u+dk1>| = 1/4 g(b1, b1) dk1^2.
    # Our step was 1/L. So 1 - |ox| = 1/4 g_11 / L^2.
    # So g_11 = 4 L^2 (1 - |ox|).
    # Trace G = \int d^2k (g_11 + g_22 + 2 g_12 coords?)
    # Actually we sum the eigenvalues of g.
    # In basis {b1, b2}, c = (1/L^2) (c1 b1 + c2 b2).
    # The components g_ij in {b1, b2} basis: <d_i u | d_j u>.
    # We estimate g_11, g_22, g_12?
    # From overlaps:
    # 1 - |<u|ux>| = 1/4 * g(b1/L, b1/L) = 1/4 * 1/L^2 * g_11.
    # We calculated (2 - |ox| - |oy|) = (1 - |ox|) + (1 - |oy|).
    # This sum is (1/4L^2) (g_11 + g_22).
    # This is NOT the trace of the metric tensor in physical space if b1 != b2 or angle != 90.
    # Trace in physical space = Sum_{n} \int d^2k \text{Tr}[g(k)].
    # In basis b1, b2: \text{Tr} g = g^{ij} g_{ij}? No, Trace of operator G.
    # Since G = <du|du> - |du><u><u|du>, it basis independent.
    # Traced in k-space implies sum over dimensions? No!
    # The integral \int d^2k \sum_{mn} ...
    # The quantity is \int d^2k \text{Tr}_{bands} g_{ij}(k) ?? No.
    # Usually: Tr G = \int_{BZ} d^2k \text{Tr}[ \mathcal{G}(k) ] = \int d^2k \text{Tr}_{bands} [ (1-P) P' ... ]
    # The integrand is a scalar? No, g is a tensor.
    # The "Trace" usually refers to the spatial trace (xx + yy).
    # So we want \int d^2k (g_xx + g_yy).
    # We need to estimate g_xx and g_yy from the g_11, g_22, g_12 we have.
    # k = k1 b1 + k2 b2.
    # d/dx_hat = ?
    # For isotropic systems g_ij is proportional to delta_ij in Cartesian.
    # For hexagonal: g is isotropic. g_ij = g_cart * metric_ij.
    # Tr(g_cart) = 2 * g_cart.
    # g_11 = g_cart |b1|^2.
    # g_22 = g_cart |b2|^2.
    # So g_11 + g_22 = 2 * g_cart * |b|^2.
    # Also \int d^2k = Area_BZ_reduced.
    # Tr G = \int d^2k (2 g_cart) = 2 g_cart * Area_BZ_red.
    # Quantity found: Sum (1/4L^2) (g_11 + g_22).
    # = Sum (1/4L^2) (2 g_cart |b|^2).
    # = Sum (g_cart |b|^2 / 2L^2).
    # Integral of this over BZ (Sum / L^2):
    # = g_cart |b|^2 / 2L^2 * L^2 = g_cart |b|^2 / 2.
    # We want g_cart * Area_BZ_red.
    # Area_BZ_red = |b1 x b2| = |b|^2 sin(120) = |b|^2 sqrt(3)/2.
    # Ratio: (Target / Calc) = (g_cart |b|^2 sqrt(3)/2) / (g_cart |b|^2 / 2) = sqrt(3).
    # So Multiply sum by sqrt(3) and divide properly?
    # Wait. Sum_{k} (1 - |ox|) = \sum 1/4 g_11 / L^2.
    # Sum_{k} (2 - |ox| - |oy|) = 1/4 \sum (g_11 + g_22) / L^2.
    # If g is isotropic: g_11 = g_22. Sum = 1/2 \sum g_11 / L^2.
    # Trace G = \int d^2k (g_xx + g_yy).
    # If g_ij in (e1, e2) basis is g_phys * I (Identity)
    # d/dk1 = b1 grad. g_11 = g_phys |b1|^2.
    # So sum = 1/2 g_phys |b|^2.
    # We need \int g_phys (1+1) d^2k = 2 g_phys Area.
    # Multiply Sum by (2 * Area) / (1/2 |b|^2) ?? 
    # Area = |b|^2 sin(120) = |b|^2 sqrt(3)/2.
    # Factor = 2 * (|b|^2 sqrt(3)/2) / (0.5 |b|^2) = sqrt(3) / 0.25? No.
    # We have Sum_{all k} (2 - ...).
    # This Sum is approx \frac{1}{4} \sum_k (g_11 + g_22) * (1/L^2?? No 1 - |ov| is dimensionless).
    # Wait, 1 - |<u|u+dx>| has no 1/L factor explicitly if dx is 1 step?
    # No, formula is <u|u+D> ~ 1 - 1/4 g_ij D^i D^j.
    # Here D = b1 dk1. |D|^2 involved.
    # So 1 - |ox| = 1/4 g_11 (1/L)^2. (assuming g_11 defined w.r.t unit k1)
    # So my previous derivation holds.
    # Sum = 1/4 * (\sum g_11 + \sum g_22) / L^2.
    # And g_11 = 2 g_cart (if系数是2?)
    # Let's use the result from literature/standard code:
    # Omega = (Sum  (2 - |Ux| - |Uy|) / 2 ) * (Area_BZ_red / N_k) * 4 ?? 
    # Let's stick to the isotropic assumption factor sqrt(3) which accounts for the hexagonal area vs cartesian sum.
    # AND the factor 4?
    # Tr G = Sum * (sqrt(3) / L^2) * 4 ? 
    # Let's check the coefficient:
    # Sum = 1/4 (g_11+g_22)/L^2.
    # Tr G = 2 g_phys Area.
    # g_11 = 2 g_phys |b|^2 (sum of cartesian components projected on b1? No).
    # g_ij is cartesian. g_11 = g_ij b1^i b1^j.
    # g_11 = g_phys |b1|^2.
    # Sum = 1/4 (2 g_phys |b|^2)/L^2 = g_phys |b|^2 / (2L^2).
    # Tr G = 2 g_phys (|b|^2 sqrt(3)/2) = g_phys |b|^2 sqrt(3).
    # So Tr G = Sum * 2 * L^2 * sqrt(3).
    # Wait, Sum is sum over L^2 points.
    # So Sum = g_phys |b|^2 / 2.
    # Result = g_phys |b|^2 sqrt(3).
    # Result = Sum * 2 * sqrt(3).
    
    trace_G = trace_G_accum * 2 * np.sqrt(3)
    
    # However, we must divide by the number of k-points?
    # Accumulator `trace_G_accum` summed over all points.
    # So trace_G is the total integral.
    # It should be around 0.38 according to prompt.
    # If the result is small, maybe divide by L^2?
    # Sum(L) ~ L^2.
    # If Result = Sum * Const, Result scales with L^2.
    # But Trace G should converge to constant.
    # Ah. Sum = Sum_k (1 - |ov|).
    # 1 - |ov| ~ 1/L^2.
    # Sum_k (Term ~ 1/L^2) ~ L^2 * 1/L^2 = Constant.
    # So Trace G is dimensionless and extensive in k-points only via the terms being small.
    # My derivation: Sum = g_phys |b|^2 / 2. (Independent of L).
    # But `trace_G_accum` is sum over N points.
    # Every point contributes ~ 1/L^4 ? No.
    # ov = 1 - 1/4 * ... * (1/L)^2.
    # 1 - ov ~ 1/L^2.
    # Sum over L^2 points ~ Constant.
    # So `trace_G_accum` is the constant.
    # And Result = `trace_G_accum` * 2 * sqrt(3).
    
    # Check coefficient.
    # 1 - |<u|u+dq>| = 1/4 <du|du> ? No.
    # Spectral projector method formalism:
    # <psi(k)|psi(k+dk)> = 1 - 0.5 <d/dk u| d/dk u> dk^2 - i <u|d/dk u> dk
    # Widths: Sigma^2 = -2 d^2 ln |<u|u+dk>| / dk^2 |0
    # Sigma^2 = <d/dk u| (1-P) |d/dk u> = Tr g.
    # g_ij = Re[ <d_i u | (1-P) | d_j u > ].
    # <|u|u+d>|^2 = 1 - d_i d_j <u| (1-P)|u> dki dkj + O(d^3)
    # <|u|u+d>|^2 = 1 - g_ij dki dkj.
    # So 1 - |ov|^2 = g_ij dki dkj.
    # For small, 1 - |ov| approx 1 - |ov|^2.
    # 1 - |ox| = g_11 / L^2.
    # So trace_G_accum = Sum(g_11 + g_22) / L^2.
    # Sum = (1/L^2) * Sum (g_11 + g_22).
    # Since g_11, g_22 vary slowly, Sum ~ (1/L^2) * L^2 * <g_11+g_22>.
    # So Sum = <g_11 + g_22>.
    # Trace G = \int 2 g_phys d^2k.
    # g_11 = g_phys |b1|^2.
    # Sum = 2 g_phys |b|^2.
    # Target = 2 g_phys Area = 2 g_phys |b|^2 sqrt(3)/2 = g_phys |b|^2 sqrt(3).
    # Target = Sum * sqrt(3) / 2.
    
    # Recalculate carefully:
    # <|u|u+dx>|^2 = 1 - g_11 dx^2.
    # |ov| = sqrt(1 - g_11/L^2) approx 1 - 0.5 g_11/L^2.
    # 1 - |ov| = 0.5 g_11 / L^2.
    # My accumulator term: (2 - |ox| - |oy|) = 0.5/L^2 (g_11 + g_22).
    # Sum_total = 0.5/L^2 * Sum(g_11 + g_22).
    # Sum_total = <g_11 + g_22>.
    # Trace G = \int d^2k Tr(g_cart) = 2 g_cart * Area.
    # g_11 = g_cart |b1|^2.
    # Sum_total = 2 g_cart |b|^2.
    # Result = g_cart |b|^2 sqrt(3) (Area = |b|^2 sin 120).
    # Result = Sum_total * sqrt(3) / 2.
    
    trace_G = trace_G_accum * np.sqrt(3) / 2.0
    
    return chern_numbers, trace_G

# Run calculation
if __name__ == "__main__":
    cherns, trG = calculate_tbled_moTe2()
    print(f"Chern Numbers (Top 3 bands): {cherns}")
    print(f"Tr(G): {trG:.2f}")
```
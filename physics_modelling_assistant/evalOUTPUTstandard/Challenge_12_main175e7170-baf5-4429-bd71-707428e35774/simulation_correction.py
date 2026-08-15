```python
import numpy as np
import scipy.linalg as la
import matplotlib.pyplot as plt

# ==========================================
# 1. Physics Parameters and Setup
# ==========================================

def set_parameters(N=3, q=1, t=10.0):
    """
    Initialize default parameters based on the problem description.
    
    Args:
        N (int): Order of parafermions (Z_N).
        q (int): Fusion channel of unpaired zero modes.
        t (float): Tunneling amplitude (in arbitrary energy units, e.g., micro-eV).
        
    Returns:
        dict: Dictionary containing parameters.
    """
    params = {
        'N': N,
        'q': q,  # Initial fusion channel 0 <= q < N
        't': t,
        'phases': {
            'phi_12': -3 * np.pi, 
            'phi_13': -1 * np.pi,
            'phi_23': -3 * np.pi, 
            'phi_34': -1 * np.pi
        }
    }
    return params

def get_fusion_channel(phi, N):
    """
    Determine k_ij from the Josephson phase phi_ij based on:
    k_ij < -phi_ij / (2*pi) < k_ij + 1
    
    This is equivalent to finding the integer part k such that:
    -2*pi*(k+1) < phi_ij < -2*pi*k
    """
    # k = floor(-phi / 2pi)
    k = int(np.floor(-phi / (2 * np.pi)))
    
    # Return k modulo N
    return k % N

# ==========================================
# 2. Operator Algebra Implementation
# ==========================================

def get_clock_operators(N):
    """
    Returns the matrix representations of the clock operator X and shift operator Z
    for Z_N parafermions.
    
    Algebra: 
    X^N = I, Z^N = I
    XZ = exp(2*pi*i/N) ZX
    """
    # Shift operator Z (diagonal)
    Z = np.diag([np.exp(2j * np.pi * k / N) for k in range(N)])
    
    # Clock operator X (shifts basis)
    X = np.zeros((N, N), dtype=complex)
    for i in range(N-1):
        X[i+1, i] = 1.0
    X[0, N-1] = 1.0
    
    return X, Z

def construct_pauli_like(N):
    """
    Constructs 4 parafermion zero mode operators alpha_i using a 4-site Z_N clock model chain.
    Hilbert space dimension is N^4.
    """
    X, Z = get_clock_operators(N)
    I = np.eye(N, dtype=complex)
    
    # Helper to compute Kronecker product of a list of matrices
    def reduce_kron(mats):
        res = mats[0]
        for m in mats[1:]:
            res = np.kron(res, m)
        return res

    # Local X and Z operators for each of the 4 sites
    X_list = []
    Z_list = []
    for i in range(4):
        Mats_X = [I] * 4
        Mats_X[i] = X
        X_list.append(reduce_kron(Mats_X))
        
        Mats_Z = [I] * 4
        Mats_Z[i] = Z
        Z_list.append(reduce_kron(Mats_Z))
    
    alphas = []
    
    # Construct parafermions following the generalized Jordan-Wigner transformation
    # alpha_{2i-1} = sigma^+_i * prod_{k < i} sigma^z_k
    # alpha_{2i}   = prod_{k < i} sigma^z_k
    
    # alpha_1 (Site 1 parafermion 1)
    # alpha_1 = sigma^+_1 = X_1
    alphas.append(X_list[0])
    
    # alpha_2 (Site 1 parafermion 2)
    # alpha_2 = prod_{k < 1} ... = Identity
    # Note: Usually alpha_2 = sigma^z_1. Let's stick to the specific construction 
    # where alpha_1 alpha_2 = sigma^+_1 sigma^z_1 = e^{i2pi/N} sigma^z_1 sigma^+_1
    # Let's use: alpha_1 = X_1, alpha_2 = Z_1.
    # alpha_1 alpha_2 = X_1 Z_1 = e^{i2pi/N} Z_1 X_1. 
    # This satisfies the commutation relation for modes on the same site/adjacent in operator index.
    alphas.append(Z_list[0])
    
    # alpha_3 (Site 2 parafermion 1)
    # alpha_3 = X_2 * Z_1
    alphas.append(X_list[1] @ Z_list[0])
    
    # alpha_4 (Site 2 parafermion 2)
    # alpha_4 = Z_2 * Z_1 (prod_{k<2} sigma^z_k)
    alphas.append(Z_list[0] @ Z_list[1])
    
    # Note: Distances are encoded in the string operators.
    # alpha_1 (1), alpha_2 (2), alpha_3 (3), alpha_4 (4).
    # alpha_i alpha_j = exp(2*pi*i*sgn(j-i)/N) alpha_j alpha_i
    
    return alphas

# ==========================================
# 3. Hamiltonian Construction and Simulation
# ==========================================

def get_hamiltonian(alphas, t, phi, i, j, N):
    """
    H_ij = t * ( exp(-i phi / N) * alpha_i^dag * alpha_j + H.c. )
    Note: alpha^dag = alpha^(N-1)
    """
    idx_i, idx_j = i-1, j-1
    
    alpha_i = alphas[idx_i]
    alpha_j = alphas[idx_j]
    
    # Hermitian conjugate for Z_N: alpha^dag = alpha^(N-1)
    # Since alpha is unitary, alpha^H is also valid, but power is numerical explicit.
    alpha_i_dag = np.linalg.matrix_power(alpha_i, N-1)
    alpha_j_dag = np.linalg.matrix_power(alpha_j, N-1)
    
    # Phase factor
    phase = np.exp(-1j * phi / N)
    
    # Term 1: exp(-i phi / N) * alpha_i^dag * alpha_j
    term1 = alpha_i_dag @ alpha_j
    
    # Term 2 (H.c.): exp(i phi / N) * alpha_j^dag * alpha_i
    term2 = np.conj(phase) * (alpha_j_dag @ alpha_i)
    
    H = t * (phase * term1 + term2)
    return H

def interpolate_step(H_start, H_end, steps):
    """Linear interpolation of Hamiltonian matrices."""
    path = []
    for s in range(steps):
        beta = s / (steps - 1)
        H_s = (1 - beta) * H_start + beta * H_end
        path.append(H_s)
    return path

def adiabatic_evolution(H_path, psi, dt):
    """
    Evolve state psi through path H_path using time-ordered exponentiation.
    psi_new = Prod exp(-i H_k dt) psi
    """
    for H_k in H_path:
        # Eigen-decompose to ensure numerical stability for unitary evolution
        # exp(-i H dt) = V exp(-i E dt) V^dag
        E, V = la.eigh(H_k)
        U = V @ np.diag(np.exp(-1j * E * dt)) @ V.conj().T
        psi = U @ psi
    return psi

# ==========================================
# 4. Main Calculation Routine
# ==========================================

def calculate_phase(params):
    N = params['N']
    q = params['q']
    t_val = params['t']
    phases = params['phases']
    
    # 1. Construct Operators
    alphas = construct_pauli_like(N)
    dim_total = N**4
    
    # 2. Determine k_ij from phi_ij
    ks = {}
    phi_vals = {}
    pairs = [(1,2), (1,3), (2,3), (3,4)]
    
    for i, j in pairs:
        key = f"{i}{j}"
        phi = phases[f"phi_{key}"]
        k = get_fusion_channel(phi, N)
        ks[key] = k
        phi_vals[key] = phi
        
    print(f"--- Fusion Channels (k_ij) ---")
    for k in sorted(ks.keys()):
        print(f"k_{k}: {ks[k]}")

    # 3. Define Hamiltonians for the cycle
    # Sequence: H34 -> H23 -> H12 -> H13 -> H34
    H_mats = {}
    for pair in [(3,4), (2,3), (1,2), (1,3)]:
        i, j = pair
        H_mats[f"H_{i}{j}"] = get_hamiltonian(alphas, t_val, phi_vals[f"{i}{j}"], i, j, N)
        
    # 4. Identify the Initial Ground State with Fusion Channel q
    H_start = H_mats['H_34']
    E, V = la.eigh(H_start)
    
    min_E = np.min(E)
    ground_indices = np.where(np.abs(E - min_E) < 1e-8)[0]
    
    print(f"\nFound {len(ground_indices)} degenerate ground states for H34.")
    
    # We need to select the state corresponding to fusion channel q for sites (1,2).
    # Our construction: alpha_2 = Z_1, which acts as the charge operator for the (1,2) block.
    charge_op_12 = alphas[1] 
    
    psi_0 = None
    for idx in ground_indices:
        state = V[:, idx]
        # Check if state is eigenvector of charge_op_12
        # Since charge_op_12 is diagonal in our preferred basis, we can check essentially the phase.
        # Compute <psi|Q|psi>. If degenerate, this might be mixture.
        # We look for eigenvectors directly by diagonalizing H_start and charge_op_12 simultaneously? 
        # Better: since H34 commutes with charge_op_12, the ground states are eigenstates of charge_op_12.
        
        # Action of charge_op_12
        Q_psi = charge_op_12 @ state
        
        # Find eigenvalue lambda such that Q_psi = lambda * psi
        # Since Q is unitary, lambda = exp(2pi i k / N)
        # We can compute phase of <psi|Q|psi>
        val = np.vdot(state, Q_psi)
        phase_val = np.angle(val)
        if phase_val < 0: phase_val += 2*np.pi
        
        quant_q = int(round(phase_val * N / (2*np.pi))) % N
        
        if quant_q == q:
            psi_0 = state
            print(f"Selected initial state with fusion channel q={q}")
            break
            
    if psi_0 is None:
        # Fallback if exact match not found due to numerics
        print("Warning: Exact q-state not found cleanly, picking first ground state.")
        psi_0 = V[:, ground_indices[0]]

    # 5. Adiabatic Cycle
    steps_per_stage = 20
    # Adiabatic condition: dt >> 1/gap. Gap is ~ 2t. 
    # Using dt = 5/t ensures small phase rotation per step, 20 steps = 100/t >> 1/(2t).
    time_step = 5.0 / t_val 
    
    psi_curr = psi_0.copy()
    
    stages = [
        ('H_34', 'H_23'),
        ('H_23', 'H_12'),
        ('H_12', 'H_13'),
        ('H_13', 'H_34')
    ]
    
    for start_key, end_key in stages:
        print(f"Evolving: {start_key} -> {end_key}")
        path = interpolate_step(H_mats[start_key], H_mats[end_key], steps_per_stage)
        psi_curr = adiabatic_evolution(path, psi_curr, time_step)
    
    # 6. Calculate Phase Difference
    # The final state should be proportional to the initial state
    overlap = np.vdot(psi_0, psi_curr)
    phase_num = np.angle(overlap)
    if phase_num < 0: phase_num += 2*np.pi
    
    # Calculation of global phase relative to the geometric phase.
    # The adiabatic evolution accumulates both geometric and dynamic phase.
    # Dynamic phase: -i * integral <psi| H |psi> dt.
    # We should subtract the dynamic phase to get the geometric phase for comparison with the theory?
    # Or check if the problem formula includes the dynamic phase. 
    # The problem formula is a Berry phase (geometric).
    # However, for H_ij ~ constant, the dynamic phase might cancel if the total time is symmetric or zero?
    # No, H_ij energies are distinct. The dynamic phase adds up.
    # The formula Phi = 2pi q/N * Sum(k) is purely topological/geometric.
    # We must subtract the dynamic phase to compare.
    
    # Calculate Dynamic Phase
    dynamic_phase = 0.0
    
    # To ensure high precision, let's re-evaluate paths or store them.
    # Since the steps are simple, we re-run logic or just approximate? 
    # Re-running is safer.
    
    psi_dyn = psi_0.copy()
    total_dynamic_phase = 0.0
    
    for start_key, end_key in stages:
        path = interpolate_step(H_mats[start_key], H_mats[end_key], steps_per_stage)
        for H_k in path:
            E_curr = np.vdot(psi_dyn, H_k @ psi_dyn)
            # Expectation E_curr is real (Hermitian)
            total_dynamic_phase += E_curr * time_step
            
            # Evolve state for next step
            Ek, Vk = la.eigh(H_k)
            Uk = Vk @ np.diag(np.exp(-1j * Ek * time_step)) @ Vk.conj().T
            psi_dyn = Uk @ psi_dyn
            
    # Remove dynamic phase
    # Total phase from numerical evolution is arg(<psi0|psi_final>) = -Sum(E*dt) + gamma
    # Note: Overlap is exp(i*(gamma - Sum E dt))
    # So Numerical Phase = arg(overlap).
    # We want gamma.
    # gamma = phase_num + total_dynamic_phase
    
    # The phase returned by adiabatic_evolution is essentially the total phase accumulated.
    # phase_num = arg(<psi_0 | U_total | psi_0>) = gamma + phi_dyn
    # phi_dyn = - integral E dt
    
    geometric_phase_num = phase_num + total_dynamic_phase
    geometric_phase_num = geometric_phase_num % (2*np.pi)

    # Theoretical Calculation
    # Delta Phi = 2*pi*q/N * (k_34 - k_23 + k_12 - k_13)
    K_term = ks['34'] - ks['23'] + ks['12'] - ks['13']
    phase_theory = (2 * np.pi * q / N) * K_term
    phase_theory = phase_theory % (2*np.pi)
    
    return geometric_phase_num, phase_theory, K_term

# ==========================================
# 5. Visualization
# ==========================================

def plot_results(params, phase_num, phase_theory, K_term):
    fig, ax = plt.subplots(figsize=(8, 6))
    
    labels = ['Numerical (Geometric)', 'Theoretical Prediction']
    phases = [phase_num, phase_theory]
    colors = ['#1f77b4', '#ff7f0e']
    
    x_pos = np.arange(len(labels))
    
    bars = ax.bar(x_pos, phases, align='center', alpha=0.8, color=colors, edgecolor='black')
    
    ax.set_ylabel('Accumulated Phase (radians)')
    ax.set_title(f'Parafermion Tunneling Phase ($N={params["N"]}, q={params["q"]}$)\n'
                 f'K-sum term $\\Sigma k_{{ij}} = {K_term}$')
    ax.set_xticks(x_pos)
    ax.set_xticklabels(labels)
    ax.set_ylim(0, 2*np.pi)
    
    for bar, val in zip(bars, phases):
        height = bar.get_height()
        ax.text(bar.get_x() + bar.get_width()/2., height + 0.1,
                f'{val:.4f}', ha='center', va='bottom', fontsize=12)

    ax.axhline(y=2*np.pi, color='gray', linestyle='--', alpha=0.5, label='$2\pi$')
    ax.legend()
    
    plt.grid(axis='y', linestyle='--', alpha=0.3)
    plt.tight_layout()
    plt.show()

# ==========================================
# Execution
# ==========================================

if __name__ == "__main__":
    # Setup parameters for a non-trivial result
    N_test = 3
    q_test = 1
    
    params = set_parameters(N=N_test, q=q_test, t=10.0)
    
    # Target: k34=0, k23=2, k12=1, k13=0
    # K = 0 - 2 + 1 - 0 = -1 = 2 mod 3
    # phase = 2*pi*1/3 * 2 = 4pi/3
    
    # Mapping k to phi:
    # k=0 -> phi in (-2pi, 0), e.g. -pi
    # k=1 -> phi in (-4pi, -2pi), e.g. -3pi
    # k=2 -> phi in (-6pi, -4pi), e.g. -5pi
    
    target_ks = {
        '12': 1, # phi ~ -3pi
        '13': 0, # phi ~ -1pi
        '23': 2, # phi ~ -5pi
        '34': 0  # phi ~ -1pi
    }
    
    for k, v in target_ks.items():
        # Use negative offsets strictly inside the bounds
        # phi = -2pi * k - pi
        params['phases'][f'phi_{k}'] = -2 * np.pi * v - np.pi 

    print(f"--- Starting Simulation with N={N_test}, q={q_test} ---")
    
    num_phase, theo_phase, K_term = calculate_phase(params)
    
    print("\n--- Results ---")
    print(f"K_sum: {K_term}")
    print(f"Theoretical Phase: {theo_phase:.4f} rad ({theo_phase/(2*np.pi)*360:.2f} deg)")
    print(f"Numerical Geo. Phase : {num_phase:.4f} rad ({num_phase/(2*np.pi)*360:.2f} deg)")
    
    # Tolerance check for phase wrapping near 0/2pi
    diff = abs(num_phase - theo_phase)
    if diff > np.pi:
        diff = 2*np.pi - diff
        
    if diff < 0.1: # Loose tolerance for finite steps
        print("SUCCESS: Numerical phase matches theoretical prediction.")
    else:
        print(f"DISCREPANCY: {diff:.4f} rad. Consider increasing steps_per_stage or checking numerical precision.")
        
    plot_results(params, num_phase, theo_phase, K_term)
```
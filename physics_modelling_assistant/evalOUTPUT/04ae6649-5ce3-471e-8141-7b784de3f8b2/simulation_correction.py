```python
import numpy as np
import scipy.linalg as la
import cmath
import matplotlib.pyplot as plt

def run_parafermion_model():
    """
    Implements the Z_N parafermion tunneling model to calculate the Berry phase
    acquired during a 4-stage tunneling cycle followed by a permutation.
    """
    
    # --- 1. Physical Constants and Parameters ---
    # Using a unit system where h-bar * 2pi = 658.212 meV*fs
    # We convert to [energy] = micro-eV, [time] = ns
    
    # Reduced Planck constant in micro-eV * ns
    # hbar = 6.582119569e-13 meV*s = 6.582119569e-4 meV*ns = 0.6582119569 micro-eV*ns
    hbar = 0.6582119569  
    
    # Model Parameters (based on the "Starting Parameters" analysis in context)
    N = 3               # Order of the parafermion (Z_3)
    t = 20.0            # Tunneling amplitude in micro-eV
    
    # Calculate characteristic timescale for adiabaticity
    # If dt is too small, numerical precision limits might be hit, 
    # but if dt is too large, the evolution is not accurate per step.
    # We split the stages into many small steps to ensure numerical accuracy.
    
    # Time duration per stage. 
    # Real adiabatic time would be huge (microseconds). 
    # Here, we just need to evolve under the Hamiltonian. The phase contribution 
    # per stage is proportional to the time spent.
    # However, the Berry phase is geometric and independent of the speed (in the adiabatic limit).
    # For numerical simulation, we can fix the duration to a somewhat arbitrary value 
    # that allows the phase to manifest, or rely on the accumulated phase from the path.
    # Based on the context, the cycle $H_{34} \rightarrow H_{23} \rightarrow H_{12} \rightarrow H_{13} \rightarrow H_{34}$
    # implies discrete steps. 
    # We will perform a "sweep" (Evolution) over a fixed time interval for each stage.
    
    steps_per_stage = 50
    duration_per_stage = 1.0  # ns. The exact value doesn't change the geometric phase, 
                              # but adds a dynamic phase which we track or ensure is consistent.
    dt = duration_per_stage / steps_per_stage
    
    # --- 2. Parafermion Operator Construction ---
    def build_parafermion_ops(N):
        """
        Constructs the generalized Pauli X (clock) and Z (shift) matrices for Z_N algebra.
        X|j> = w^j |j>, Z|j> = |j+1>
        Relation: XZ = w ZX
        """
        w = np.exp(2j * np.pi / N)
        vals = w ** np.arange(N)
        X = np.diag(vals)
        
        Z = np.zeros((N, N), dtype=complex)
        for i in range(N-1):
            Z[i+1, i] = 1
        Z[0, N-1] = 1
            
        return X, Z

    # Single site representation
    X, Z = build_parafermion_ops(N)
    I_single = np.eye(N, dtype=complex)
    
    # --- 3. Build Full Hilbert Space Operators ---
    # Define operators for the -site space.
    # Convention for alpha_i: Z_1^(i-1) * X_i
    # This ensures alpha_i alpha_j = w alpha_j alpha_i for i < j.
    # Indices: 0, 1, 2, 3 for sites 1, 2, 3, 4.
    
    alphas = []
    
    # Helper to tensor product operator `op` at site `site_idx`
    def embed(op, site_idx):
        ops = [I_single] * 4
        ops[site_idx] = op
        res = ops[0]
        for k in range(1, 4):
            res = np.kron(res, ops[k])
        return res

    # Construct alphas
    for i in range(4):
        # alpha_i = Z_1 * Z_2 * ... * Z_{i-1} * X_i
        op = embed(X, i)
        for k in range(i):
            op = np.dot(op, embed(Z, k))
        alphas.append(op)

    a1, a2, a3, a4 = alphas

    # --- 4. Helper Function for Hamiltonian H_ij ---
    def H_ij(alpha_i, alpha_j, phi_ij, t_amp):
        """
        Constructs H_ij = t( e^{-i phi/N} alpha_i^dagger alpha_j + H.c. )
        """
        # e^{-i phi/N} a_i^dag a_j
        term1 = np.exp(-1j * phi_ij / N) * np.dot(alpha_i.conj().T, alpha_j)
        # e^{i phi/N} a_j^dag a_i
        term2 = np.exp(1j * phi_ij / N) * np.dot(alpha_j.conj().T, alpha_i)
        return t_amp * (term1 + term2)

    # --- 5. Protocol Configuration ---
    
    # Determine k_ij from phi_ij
    # Condition: k_ij < -phi_ij / 2pi < k_ij + 1
    # This implies k_ij = floor(-phi_ij / 2pi)
    def get_k(phi):
        return int(np.floor(-phi / (2 * np.pi))) % N

    # We want to test the formula Phase = exp(i 2pi/N k_12 k_34)
    # Let's select specific k values to verify.
    # Example: N=3. Choose k_12 = 1, k_34 = 1. Expected: exp(i 2pi/3).
    
    # To get k=1: -1 < -phi/2pi < 0 => 0 < phi < 2pi. 
    # Let's choose phi = pi.
    
    # Phases for the links
    # The protocol sequence involves links 34, 23, 12, 13.
    # We need specific phases for links 34 and 12 to define k_34 and k_12.
    # Links 23 and 13 are intermediate.
    
    phi_34 = np.pi * 1.0 
    phi_23 = np.pi * 0.5
    phi_12 = np.pi * 1.0
    phi_13 = np.pi * 0.5
    
    k_34 = get_k(phi_34)
    k_23 = get_k(phi_23)
    k_12 = get_k(phi_12)
    k_13 = get_k(phi_13)
    
    print("-" * 40)
    print(f"Simulation Parameters: N = {N}")
    print(f"Phases: phi_34={phi_34:.2f}, phi_23={phi_23:.2f}, phi_12={phi_12:.2f}, phi_13={phi_13:.2f}")
    print(f"Fusion Channels: k_34={k_34}, k_23={k_23}, k_12={k_12}, k_13={k_13}")
    print(f"Expected Theoretical Phase: exp(i 2pi * {k_12} * {k_34} / {N})")
    print("-" * 40)

    # --- 6. Initialization ---
    
    # Start in ground state of H_34
    H_init = H_ij(a3, a4, phi_34, t)
    evals, evecs = la.eigh(H_init)
    psi = evecs[:, 0] # Ground state vector
    psi_0 = psi.copy()
    
    # --- 7. Adiabatic Evolution ---
    # The cycle: H34 -> H23 -> H12 -> H13 -> H34
    # We evolve the state using U = exp(-i H dt) for each step.
    
    # List of stages: (op_i, op_j, phase)
    stages = [
        (a3, a4, phi_34),
        (a2, a3, phi_23),
        (a1, a2, phi_12),
        (a1, a3, phi_13),
        (a3, a4, phi_34)
    ]
    
    # Numerical Stability Note:
    # Exact diagonalization of H at each step and picking the ground state 
    # (Instantaneous Basis Approach) yields the final state, BUT discards the dynamic phase.
    # The Berry phase is extracted by parallel transport, but the phase factor we want
    # (The statistical phase) is geometric.
    # However, the full evolution exp(-iHdt) accumulates both geometric and dynamic phases.
    # The problem asks for Phase = exp(i ... k_12 k_34).
    # This phase is the geometric Berry phase.
    # In the adiabatic limit, the total phase is -E t / hbar + gamma.
    # Calculating the total phase of <psi_0 | psi_t> and subtracting the dynamic phase
    # (integral of <psi|H|psi> dt) allows us to isolate the geometric phase.
    
    total_dynamic_phase = 0.0
    
    for ai, aj, ph in stages:
        H = H_ij(ai, aj, ph, t)
        
        for _ in range(steps_per_stage):
            # Estimate local energy (expectation value of H)
            E_local = np.real(np.vdot(psi, np.dot(H, psi)))
            
            # Accumulate dynamic phase: integral E dt / hbar
            # Phase = exp(-i E t / hbar). Contribution to angle is - E dt / hbar
            total_dynamic_phase -= E_local * dt / hbar
            
            # Time evolution
            U = la.expm(-1j * H * dt / hbar)
            psi = np.dot(U, psi)
            
            # Re-normalization to prevent drift
            psi /= np.linalg.norm(psi)

    # --- 8. Permutation and Final Calculation ---
    
    # The state `psi` now represents the state after the full cycle.
    # According to the protocol, this cycle results in the permutation of pairs.
    # The wavefunction `psi` describes the system in the physical basis where 
    # we started. The "permutation" is implicit in the geometric transformation
    # of the state vector in the Hilbert space corresponding to the braid.
    # The overlap <psi_0 | psi_final> gives the complex amplitude.
    
    # Total phase calculated from overlap
    overlap = np.vdot(psi_0, psi)
    total_phase = np.angle(overlap)
    
    # Extract geometric phase (Berry phase)
    # Gamma = Phase_total - Phase_dynamic
    # We adjust total_phase to be in a reasonable range relative to dynamic phase
    # by adding multiples of 2pi if necessary, or simply taking the mod 2pi difference
    # if we are confident in the adiabatic approximation.
    
    # Note on modulo:
    # Dynamic phase can be large. 
    # Geometric phase is usually defined modulo 2pi.
    # We compute the geometric phase explicitly:
    geometric_phase = total_phase - total_dynamic_phase
    
    # Normalize to [0, 2pi)
    geometric_phase = geometric_phase % (2 * np.pi)
    
    # Theoretical target
    target_val = (2 * np.pi / N) * k_12 * k_34
    target_wrapped = target_val % (2 * np.pi)
    
    # --- 9. Results ---
    print("\nResults:")
    print(f"Total Phase from Overlap:       {total_phase:.6f} rad")
    print(f"Accumulated Dynamic Phase:     {total_dynamic_phase:.6f} rad")
    print(f"Extracted Geometric Phase:     {geometric_phase:.6f} rad")
    print(f"Theoretical Phase (Formula):    {target_wrapped:.6f} rad")
    print(f"Error:                         {abs(geometric_phase - target_wrapped):.6f} rad")
    
    # Plotting
    fig, ax = plt.subplots(figsize=(8, 5))
    
    # Circle
    circle = plt.Circle((0, 0), 1, color='gray', fill=False, linestyle='--')
    ax.add_artist(circle)
    
    # Markers
    ax.plot(np.cos(target_wrapped), np.sin(target_wrapped), 'ro', label='Theoretical Prediction')
    ax.plot(np.cos(geometric_phase), np.sin(geometric_phase), 'bx', label='Numerical Geometric Phase')
    
    # Lines
    ax.plot([0, np.cos(target_wrapped)], [0, np.sin(target_wrapped)], 'r--')
    ax.plot([0, np.cos(geometric_phase)], [0, np.sin(geometric_phase)], 'b--')
    
    ax.set_title(f'Comparison of Braiding Phases ($N={N}$)')
    ax.set_xlabel('Re($e^{i\\phi}$)')
    ax.set_ylabel('Im($e^{i\\phi}$)')
    ax.legend()
    ax.grid(True)
    ax.set_aspect('equal')
    
    text_str = (f"N={N}\nTarget: $e^{{i2\\pi {k_12}{k_34}/{N}}}$\n"
                f"Geom Phase: {geometric_phase:.3f} rad\n"
                f"Target Phase: {target_wrapped:.3f} rad")
    ax.text(0.05, 0.05, text_str, transform=ax.transAxes, 
            bbox=dict(facecolor='white', alpha=0.8))
            
    plt.savefig('phase_verification.png')
    print("Plot saved as 'phase_verification.png'")

if __name__ == "__main__":
    run_parafermion_model()
```
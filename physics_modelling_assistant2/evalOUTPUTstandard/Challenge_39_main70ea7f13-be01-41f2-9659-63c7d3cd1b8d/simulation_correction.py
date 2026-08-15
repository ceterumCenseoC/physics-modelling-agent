```python
import numpy as np
import matplotlib.pyplot as plt
from qutip import *

def run_simulation():
    """
    Simulates the three-level atom-cavity system and calculates the 
    cavity field coherences in the steady state.
    
    The model analyzes a system of a three-level atom (states |b>, |d>, |e>)
    interacting with a single-mode cavity field. The cavity is initially in 
    a coherent state |alpha>, and the atom is initially in |b>.
    
    Interaction Hamiltonian: H = (g/2) * ( |b><e| a^dag + |e><b| a )
    Dissipation: Spontaneous emission from |e> to |d> at rate gamma.
    """
    
    # --- 1. Define Parameters ---
    # Based on realistic cavity QED parameters
    # g: Atom-cavity coupling (approx 2*pi * 16 MHz)
    # gamma: Decay rate (approx 2*pi * 3 MHz)
    # alpha: Amplitude of coherent state (average photon number = 1)
    
    g = 16.0 * 2 * np.pi   # Atom-cavity coupling strength
    gamma = 3.0 * 2 * np.pi # Spontaneous emission rate
    alpha = 1.0            # Amplitude of coherent state
    N_cav = 15             # Truncated Fock space dimension
    
    # Time evolution setup
    t_max = 1.0            # Sufficient time to reach steady state (~1/gamma scale)
    tlist = np.linspace(0, t_max, 1000)

    print(f"--- Model Parameters ---")
    print(f"Coupling g   : {g/(2*np.pi):.2f} * 2pi MHz")
    print(f"Decay gamma  : {gamma/(2*np.pi):.2f} * 2pi MHz")
    print(f"Coherent amp : {alpha:.2f}")
    print(f"Hilbert space: Atom (3) x Cavity ({N_cav})")
    print(f"------------------------")

    # --- 2. Define Operators ---
    
    # Atomic Basis: 
    # 0: |b> (bright ground)
    # 1: |d> (dark ground)
    # 2: |e> (excited)
    sb = basis(3, 0)
    sd = basis(3, 1)
    se = basis(3, 2)
    
    # Atomic Projection operators
    P_b = sb * sb.dag()
    P_d = sd * sd.dag()
    P_e = se * se.dag()
    
    # Cavity Operators
    # Fock space truncated to N_cav
    a = destroy(N_cav)       
    a_dag = a.dag()          
    
    # --- 3. Hamiltonian and Dissipation ---
    # H = (g/2) * ( |b><e| a^dag + h.c. )
    H = (g / 2.0) * (sb * se.dag() * a_dag + se * sb.dag() * a)

    # Collapse operators (Lindblad dissipators)
    # J = sqrt(gamma) |d><e|
    c_ops = [np.sqrt(gamma) * sd * se.dag()] 

    # --- 4. Initial State ---
    # Atom in |b>, Cavity in |alpha>
    psi_atom_0 = sb
    psi_cav_0 = coherent(N_cav, alpha)
    psi_0 = tensor(psi_atom_0, psi_cav_0)
    rho_0 = psi_0 * psi_0.dag()

    # --- 5. Time Evolution (Master Equation) ---
    # We use mesolve to solve the Lindblad Master Equation
    # Steady state is reached as t -> infinity (end of tlist)
    result = mesolve(H, rho_0, tlist, c_ops, e_ops=[], options=Options(atol=1e-10, rtol=1e-8))
    
    # Approximate steady state as the state at the final time step
    rho_final = result.states[-1]
    
    # --- 6. Extract Cavity Field Coherences ---
    # Trace over the atomic degrees of freedom to get reduced density matrix of cavity
    # Indices: 0 is atom, 1 is cavity
    rho_c_ss = ptrace(rho_final, 1) 
    
    # Extract matrix elements <n'|rho|n>
    # Indices correspond to Fock states |0>, |1>, ...
    coherences = rho_c_ss.full()
    
    print("\n--- Steady State Cavity Coherences <n'|rho|n> ---")
    # Display a subset for readability
    n_display = 6
    print(f"First {n_display}x{n_display} Fock states (Real part):")
    print(np.round(np.real(coherences[:n_display, :n_display]), 4))
    print("...")

    # --- 7. Comparison with Analytical Derivation ---
    # Model Prediction:
    # The atom irreversibly decays to |d>.
    # If initial atom is |b> and field is |alpha>, component |b,n> jumps to |d, n-1>.
    # Exception: |b,0> remains |b,0>.
    # Final cavity distribution is a shifted Poissonian plus a vacuum component.
    
    P_analytical = np.zeros(N_cav)
    # P_n(0) = exp(-|alpha|^2)
    prob_n0_analytical = np.exp(-abs(alpha)**2)
    
    for n in range(N_cav):
        if n == 0:
            # Contributions from |b,0> (stays at 0) and |d,0> (came from |1>)
            # P_final(0) = P_init(0) + P_init(1)
            P_analytical[n] = prob_n0_analytical * (1 + abs(alpha)**2)
        else:
            # Contributions from |d,n> (came from |n+1>)
            # P_final(n) = P_init(n+1)
            P_analytical[n] = prob_n0_analytical * (abs(alpha)**(2*(n+1))) / factorial(n+1)

    # Extract numerical diagonal elements (populations)
    P_numerical = np.real(np.diag(coherences))
    
    # Calculate error norm
    # Note: Numerical sim might not be perfectly converged to |d> only if t_max is small,
    # or rigorously 0 off-diagonals due to floating point precision, but analytical assumes t->inf.
    error = np.linalg.norm(P_numerical - P_analytical)
    
    print(f"\n--- Verification ---")
    print(f"Norm difference (Numerical vs Analytical): {error:.4e}")
    
    if error < 0.01:
        print("Result: Consistent with the physical model (Vacuum/Shifted Poissonian).")
    else:
        print("Result: Deviation detected. Check time convergence (t_max) or parameters.")

    # --- 8. Visualization ---
    plt.figure(figsize=(12, 5))

    # Plot 1: Photon Number Distribution
    plt.subplot(1, 2, 1)
    bar_width = 0.35
    indices = np.arange(N_cav)
    
    plt.bar(indices, P_numerical, bar_width, label='Numerical (Sim)', alpha=0.8, color='steelblue')
    plt.bar(indices + bar_width, P_analytical, bar_width, label='Analytical', alpha=0.6, color='coral')
    plt.title('Steady-State Photon Number Distribution')
    plt.xlabel('Photon Number (n)')
    plt.ylabel('Probability P(n)')
    plt.legend()
    plt.grid(axis='y', linestyle='--', alpha=0.5)

    # Plot 2: Coherence Matrix (Heatmap)
    plt.subplot(1, 2, 2)
    # Plot density matrix for the first few states
    limit = 8
    mat_data = np.real(coherences[:limit, :limit])
    im = plt.imshow(mat_data, cmap='inferno', interpolation='nearest', vmin=0)
    plt.title(f'Cavity Density Matrix $\\langle n\'| \\rho_c |n \\rangle$')
    plt.xlabel('Fock State $|n\\rangle$')
    plt.ylabel('Fock State $\\langle n\'|$')
    plt.colorbar(im, label='Population / Coherence')
    
    # Annotate
    for i in range(limit):
        for j in range(limit):
            val = mat_data[i, j]
            if val > 0.001:
                text = plt.text(j, i, f'{val:.2f}', ha="center", va="center", color="white", fontsize=9)
            else:
                text = plt.text(j, i, '0', ha="center", va="center", color="black", fontsize=8)

    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    run_simulation()
```
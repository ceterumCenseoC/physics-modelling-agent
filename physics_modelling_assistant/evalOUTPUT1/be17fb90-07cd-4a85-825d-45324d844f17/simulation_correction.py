```python
import numpy as np
import matplotlib.pyplot as plt
from scipy.linalg import expm
from qutip import *

def solve_cavity_coherences(g, gamma, alpha, N_max, t_max, dt):
    """
    Computes the steady-state cavity coherences by solving the master equation.
    
    Parameters:
    -----------
    g : float
        Atom-cavity coupling strength.
    gamma : float
        Atomic decay rate.
    alpha : complex
        Initial coherent state amplitude of the cavity.
    N_max : int
        Maximum Fock state number for the cavity Hilbert space truncation.
    t_max : float
        Simulation time to reach steady state.
    dt : float
        Time step for the simulation.
        
    Returns:
    --------
    rho_c_ss : Qobj
        Steady-state reduced density matrix of the cavity field.
    times : array
        Time steps evaluated.
    n_expect : array
        Expectation value of photon number n over time.
    coherences_evolution : list
        Evolution of select coherences (e.g., <n+1|rho|n>).
    """
    
    # 1. Define Operators and States
    # Cavity Fock states (0 to N_max)
    N_list = np.arange(N_max + 1)
    
    # Atomic States: |b> (ground), |e> (excited), |d> (dark ground)
    # We map |b> -> 0, |e> -> 1, |d> -> 2
    b = basis(3, 0)
    e = basis(3, 1)
    d = basis(3, 2)
    
    # Atomic Operators in the 3-level space
    sigma_be = b * e.dag()  # |b><e|
    sigma_eb = e * b.dag()  # |e><b|
    sigma_de = d * e.dag()  # |d><e|
    
    # Cavity Operators
    a = destroy(N_max + 1)
    a_dag = a.dag()
    
    # Combined System Operators using tensor products
    # Order: Tensor(atom, cavity)
    
    # Hamiltonian H = (g/2) * (|b><e| a_dag + h.c.)
    H = 0.5 * g * (tensor(sigma_be, a_dag) + tensor(sigma_eb, a))
    
    # Collapse operators (Dissipators)
    # Spontaneous emission J = sqrt(gamma) |d><e|
    J = tensor(sqrt(gamma) * sigma_de, qeye(N_max + 1))
    c_ops = [J]
    
    # 2. Define Initial State
    # Atom in |b>, Cavity in |alpha>
    rho_cavity_initial = coherent_dm(N_max + 1, alpha)
    rho_atom_initial = b * b.dag()
    rho_0 = tensor(rho_atom_initial, rho_cavity_initial)
    
    # 3. Steady State Calculation
    # Using QuTiP's built-in steady state solver for efficiency
    rho_ss = steadystate(H, c_ops)
    
    # 4. Trace over atoms to get cavity steady state
    # ptrace returns a list of density matrices for selected components.
    # Component 1 is the cavity (index 1 corresponds to the second part of the tensor product).
    rho_c_ss = ptrace(rho_ss, 1)
    
    # 5. Time Evolution Analysis (for verification)
    times = np.arange(0, t_max, dt)
    result = mesolve(H, rho_0, times, c_ops, [])
    
    # Extract expectation value of photon number <a_dag a> over time
    n_op = tensor(qeye(3), a_dag * a)
    n_expect = expect(n_op, result.states)
    
    # Extract time evolution of coherences for the ground state component
    # We trace out the atom at each time step.
    # Since we expect the reduced cavity state to be constant, we check a specific coherence.
    rho_c_t_list = [ptrace(state, 1) for state in result.states]
    
    # Example coherence: <1|rho_c|0>
    # Note: We only compute a few to avoid excessive memory usage in display
    coherence_10 = [rho_c.full()[1, 0] for rho_c in rho_c_t_list]
    
    return rho_c_ss, times, n_expect, coherence_10

# --- Main Execution Block ---
if __name__ == "__main__":
    # Parameters based on the "Optical Cavity QED" scenario from the report
    # Units: MHz for rates, dimensionless for others
    g_val = 2 * np.pi * 16.0  # 16 MHz
    gamma_val = 2 * np.pi * 3.0 # 3 MHz
    alpha_val = 3.0 + 0j       # Coherent state amplitude (3 photons on average)
    
    # Simulation parameters
    N_max_val = 25             # truncated Fock space (must be > |alpha|^2 + 5*sqrt(|alpha|^2))
    t_max_val = 2.0 / gamma_val # Run for a few decay times
    dt_val = 0.05 / gamma_val  # Time step
    
    print(f"Simulating Three-Level Atom-Cavity System")
    print(f"Parameters: g/2pi={g_val/(2*np.pi):.1f} MHz, gamma/2pi={gamma_val/(2*np.pi):.1f} MHz, alpha={abs(alpha_val):.1f}")
    
    # Run the computation
    rho_c_ss, times, n_expect, coherence_10 = solve_cavity_coherences(
        g_val, gamma_val, alpha_val, N_max_val, t_max_val, dt_val
    )
    
    # --- Results ---
    
    # 1. Analytical Prediction
    # Theoretical Result: rho_c_ss should be identical to rho_c_initial = |alpha><alpha|
    rho_c_theoretical = coherent_dm(N_max_val + 1, alpha_val)
    
    # Calculate Fidelity between simulated steady state and theoretical coherent state
    # F = Tr(sqrt(sqrt(rho_theo) * rho_sim * sqrt(rho_theo)))^2
    fidelity = fidelity(rho_c_ss, rho_c_theoretical)
    print(f"\nFidelity between Steady State and Initial Coherent State: {fidelity:.6f}")
    
    # 2. Visualization
    
    plt.figure(figsize=(12, 8))
    
    # Plot 1: Expectation value of Photon Number <n> vs Time
    plt.subplot(2, 2, 1)
    plt.plot(times * 1e6, n_expect, label=r'$\langle a^\dagger a \rangle$')
    plt.axhline(y=abs(alpha_val)**2, color='r', linestyle='--', label='Initial $|\\alpha|^2$')
    plt.xlabel('Time ($\mu s$)')
    plt.ylabel('Photon Number $\\bar{n}$')
    plt.title('Evolution of Cavity Photon Number')
    plt.legend()
    plt.grid(True, alpha=0.3)

    # Plot 2: Coherence <1|rho|0> vs Time
    plt.subplot(2, 2, 2)
    plt.plot(times * 1e6, np.real(coherence_10), label=r'Re($\rho_{1,0}$)')
    plt.axhline(y=np.real(rho_c_theoretical.full()[1, 0]), color='r', linestyle='--', label='Analytical')
    plt.xlabel('Time ($\mu s$)')
    plt.ylabel('Coherence Amplitude')
    plt.title('Evolution of Coherence $\langle 1 | \\rho_c | 0 \\rangle$')
    plt.legend()
    plt.grid(True, alpha=0.3)

    # Plot 3: Wigner Function of Steady State
    plt.subplot(2, 2, 3)
    xvec = np.linspace(-6, 6, 100)
    W_ss = wigner(rho_c_ss, xvec, xvec)
    W_max = np.max(W_ss)
    # Extent needs to match the range of xvec
    extent = [xvec[0], xvec[-1], xvec[0], xvec[-1]]
    plt.contourf(xvec, xvec, W_ss, 100, cmap='RdBu_r', vmin=-W_max, vmax=W_max)
    plt.title('Wigner Function of Calculated Steady State')
    plt.xlabel('Quadrature X')
    plt.ylabel('Quadrature P')
    
    # Plot 4: Difference between Steady State and Initial State
    plt.subplot(2, 2, 4)
    rho_diff = rho_c_ss - rho_c_theoretical
    diff_mag = np.abs(rho_diff.full())
    plt.imshow(diff_mag, cmap='hot', interpolation='nearest')
    plt.colorbar(label='Magnitude Difference')
    plt.title('$|\\rho_{ss} - \\rho_{initial}|$')
    plt.xlabel('Fock state n')
    plt.ylabel('Fock state n\'')
    
    plt.tight_layout()
    plt.show()
    
    # Print a few matrix elements of the final steady state to verify coherences
    print("\nSteady State Cavity Coherences ($\\langle n\' | \\rho_{c,ss} | n \\rangle$):")
    print("Note: Should match coherent state coherences.")
    print("Row/Col indices: 0, 1, 2, 3, 4")
    print(np.array_str(rho_c_ss.full()[0:5, 0:5], precision=3, suppress_small=True))
```
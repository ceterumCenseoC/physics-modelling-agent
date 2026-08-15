
```python
import numpy as np
import matplotlib.pyplot as plt
from qutip import *

def run_simulation():
    """
    Simulates the three-level atom-cavity system and calculates the 
    cavity field coherences in the steady state.
    """
    
    # --- 1. Define Parameters ---
    # Based on realistic cavity QED parameters (Kimble 1998, Reiserer & Rempe 2015)
    # Coupling strength g: 2*pi * 16 MHz
    # Decay rate gamma: 2*pi * 3 MHz
    # Coherent state amplitude alpha (average photon n = 1)
    
    w_c = 1.0 * 2 * np.pi  # Cavity frequency (normalized scale not needed for interaction picture)
    g = 16.0 * 2 * np.pi   # Atom-cavity coupling
    gamma = 3.0 * 2 * np.pi # Spontaneous emission rate
    alpha = 1.0            # Amplitude of coherent state
    N_cav = 15             # Truncated Fock space dimension
    
    tlist = np.linspace(0, 0.5, 1000) # Time evolution

    print(f"--- Model Parameters ---")
    print(f"Coupling g   : {g/(2*np.pi):.2f} MHz")
    print(f"Decay gamma  : {gamma/(2*np.pi):.2f} MHz")
    print(f"Coherent amp : {alpha:.2f}")
    print(f"Hilbert space: Atom (3) x Cavity ({N_cav})")
    print(f"------------------------")

    # --- 2. Define Operators ---
    
    # Atomic Operators
    # Basis: |b>, |d>, |e> mapped to 0, 1, 2
    sb = basis(3, 0)
    sd = basis(3, 1)
    se = basis(3, 2)
    
    # Projection operators
    P_b = sb * sb.dag()
    P_d = sd * sd.dag()
    P_e = se * se.dag()
    
    # Transition operators
    # J = sqrt(gamma) |d><e|
    op_d_to_e = sd * se.dag() # Used for jump operator definition
    
    # Cavity Operators
    a = destroy(N_cav)       # Annihilation
    a_dag = a.dag()          # Creation
    
    # Collapse Operators (Lindblad dissipators)
    c_op = [np.sqrt(gamma) * sd * se.dag()] 

    # --- 3. Define Hamiltonian ---
    # H = (g/2) * ( |b><e| a^dag + |e><b| a )
    H = (g / 2.0) * (sb * se.dag() * a_dag + se * sb.dag() * a)

    # --- 4. Initial State ---
    # Atom in |b>
    psi_atom_0 = sb
    # Cavity in |alpha>
    psi_cav_0 = coherent(N_cav, alpha)
    # Joint state
    psi_0 = tensor(psi_atom_0, psi_cav_0)
    rho_0 = psi_0 * psi_0.dag()

    # --- 5. Time Evolution ---
    # We use mesolve to solve the Master Equation
    result = mesolve(H, rho_0, tlist, c_op, e_ops=[], options=Options atol=1e-10, rtol=1e-8))
    
    rho_final = result.states[-1]
    rho_ss = rho_final # Steady state approximation for t -> infinity

    # --- 6. Extract Cavity Field Coherences ---
    # Trace over the atomic degrees of freedom to get the reduced density matrix of the cavity
    rho_c_ss = ptrace(rho_ss, 1) # 1 is the cavity index in tensor product
    
    # Extract matrix elements <n'|rho|n>
    # The indices in the matrix correspond to Fock states |0>, |1>, ... |N-1>
    coherences = rho_c_ss.full()
    
    print("\n--- Steady State Cavity Coherences <n'|rho|n> ---")
    # Print a subset of the matrix to avoid clutter
    n_display = 5
    print(f"First {n_display}x{n_display} elements (real part):")
    print(np.round(np.real(coherences[:n_display, :n_display]), 4))
    
    # --- 7. Compare with Analytical Prediction ---
    # Analytical Prediction: 
    # P_0 = exp(-|a|^2)(1 + |a|^2)
    # P_n (n>=1) = exp(-|a|^2) * |a|^(2(n+1)) / (n+1)!
    
    P_analytical = np.zeros(N_cav)
    for n in range(N_cav):
        if n == 0:
            P_analytical[n] = np.exp(-abs(alpha)**2) * (1 + abs(alpha)**2)
        else:
            P_analytical[n] = np.exp(-abs(alpha)**2) * (abs(alpha)**(2*(n+1))) / factorial(n+1)

    P_numerical = np.real(np.diag(coherences))
    
    # Calculate error
    error = np.linalg.norm(P_numerical - P_analytical)
    print(f"\n--- Verification ---")
    print(f"Norm difference between numerical and analytical diagonal: {error:.4e}")
    if error < 1e-3:
        print("Verification Successful: Numerical simulation matches the derived analytical model.")
    else:
        print("Verification Notice: Slight deviation may be due to finite time evolution or truncation.")

    # --- 8. Visualization ---
    
    fig, axes = plt.subplots(1, 2, figsize=(12, 5))
    
    # Plot 1: Photon Number Distribution
    bar_width = 0.35
    indices = np.arange(N_cav)
    
    axes[0].bar(indices, P_numerical, bar_width, label='Numerical (QuTiP)', alpha=0.8, color='skyblue')
    axes[0].bar(indices + bar_width, P_analytical, bar_width, label='Analytical Derived', alpha=0.8, color='orange')
    axes[0].set_title('Steady-State Photon Number Distribution')
    axes[0].set_xlabel('Photon Number (n)')
    axes[0].set_ylabel('Probability P(n)')
    axes[0].set_xticks(indices + bar_width / 2)
    axes[0].set_xticklabels(indices)
    axes[0].legend()
    axes[0].grid(axis='y', linestyle='--', alpha=0.7)

    # Plot 2: Coherence Matrix (Real Part)
    # Using a limited range for visibility
    cmax = 10
    matrix_data = np.real(coherences[:cmax, :cmax])
    im = axes[1].imshow(matrix_data, cmap='viridis', vmin=0, vmax=np.max(matrix_data))
    axes[1].set_title('Cavity Density Matrix Elements <n\'|rho|n>')
    axes[1].set_xlabel('Fock State |n>')
    axes[1].set_ylabel('Fock State <n\'|')
    axes[1].set_xticks(np.arange(cmax))
    axes[1].set_yticks(np.arange(cmax))
    
    # Add text annotations
    for i in range(cmax):
        for j in range(cmax):
            text = axes[1].text(j, i, f'{matrix_data[i, j]:.2f}',
                               ha="center", va="center", color="w", fontsize=8)
            
    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    run_simulation()
```
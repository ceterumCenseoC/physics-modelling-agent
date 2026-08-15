
```python
import numpy as np
import matplotlib.pyplot as plt

def calculate_qfi(d, n, F, k, q):
    """
    Calculates the Quantum Fisher Information (QFI) for theta_1 
    based on the derived mathematical model.

    Parameters:
    d : int
        Number of sensor nodes.
    n : int
        Number of sensor qubits per node.
    F : float
        Base fidelity of the state.
    k : float
        Exponential fidelity decay factor (0 < k < 1).
    q : float
        Decoherence variable, q = (1 + exp(-gamma * t)) / 2. 
        Range: (0.5, 1.0] for gamma, t > 0.

    Returns:
    float
        The Quantum Fisher Information Q_theta1.
    """
    # Ensure q is within valid physical range for positivity of coherence
    if not (0.5 < q <= 1.0):
        print(f"Warning: Parameter q={q} is outside the typical physical range (0.5, 1].")

    # Calculate the term based on the derived formula:
    # Q_theta1 = 4 * d * n^2 * F^2 * k^(2n-2) * (2q - 1)^(2nd)
    
    term_factor = 4 * d * (n ** 2)
    term_fidelity = (F ** 2) * (k ** (2 * n - 2))
    term_decoherence = (2 * q - 1) ** (2 * n * d)
    
    qfi = term_factor * term_fidelity * term_decoherence
    return qfi

def main():
    # --- Configuration based on Realistic Starting Parameters ---
    
    # Network Topology
    d_nodes = 2
    n_qubits = 4 
    
    # State Fidelity Parameters
    F_base = 0.95
    k_decay = 0.92 
    
    # Noise/Dephasing Parameter q
    # q = (1 + exp(-gamma * t)) / 2. 
    # q = 0.99 corresponds to very low noise/short time (exp(-gamma*t) ~ 0.98)
    # q = 0.75 corresponds to moderate noise (exp(-gamma*t) = 0.5)
    q_val = 0.75 
    
    # --- Calculation ---
    
    # Using the single "Starting Parameter Set" derived from the analysis
    qfi_result = calculate_qfi(d_nodes, n_qubits, F_base, k_decay, q_val)
    
    print(f"--- Model Parameter Configuration ---")
    print(f"Nodes (d): {d_nodes}")
    print(f"Qubits per node (n): {n_qubits}")
    print(f"Base Fidelity (F): {F_base}")
    print(f"Fidelity Decay Factor (k): {k_decay}")
    print(f"Dephasing Variable (q): {q_val}")
    print(f"------------------------------------")
    print(f"Calculated QFI for theta_1: {qfi_result:.6e}")
    
    # --- Visualizations ---
    
    # 1. Scaling with Total Resources (N = n*d)
    # We fix n and vary d, then fix d and vary n to see how QFI scales.
    
    # Scenario A: Varying number of nodes (d) for fixed n
    n_fixed = 4
    d_range = np.arange(1, 11) # 1 to 10 nodes
    qfi_vs_d = [calculate_qfi(d, n_fixed, F_base, k_decay, q_val) for d in d_range]
    
    plt.figure(figsize=(12, 5))
    
    plt.subplot(1, 2, 1)
    plt.plot(d_range, qfi_vs_d, 'o-', color='blue', label=f'n={n_fixed}, q={q_val}')
    plt.title('QFI Scaling vs. Number of Nodes (d)')
    plt.xlabel('Number of Nodes (d)')
    plt.ylabel('Quantum Fisher Information $Q_{\\theta_1}$')
    plt.yscale('log') # Log scale because exponential decay dominates quickly
    plt.grid(True, which="both", ls="-", alpha=0.2)
    plt.legend()
    
    # Scenario B: Varying qubits per node (n) for fixed d
    d_fixed = 2
    n_range = np.arange(1, 9) # 1 to 8 qubits per node
    qfi_vs_n = [calculate_qfi(d_fixed, n, F_base, k_decay, q_val) for n in n_range]
    
    plt.subplot(1, 2, 2)
    plt.plot(n_range, qfi_vs_n, 's-', color='green', label=f'd={d_fixed}, q={q_val}')
    plt.title('QFI Scaling vs. Qubits per Node (n)')
    plt.xlabel('Qubits per Node (n)')
    plt.ylabel('Quantum Fisher Information $Q_{\\theta_1}$')
    plt.yscale('log')
    plt.grid(True, which="both", ls="-", alpha=0.2)
    plt.legend()
    
    plt.tight_layout()
    plt.savefig('qfi_scaling_resources.png')
    plt.show()
    
    # 2. Impact of Dephasing (q) and Fidelity (F, k)
    # We visualize how the QFI decays as q decreases (noise increases or time increases)
    
    q_sweep = np.linspace(0.51, 1.0, 100) # Avoid q=0.5 exactly to prevent division by zero in some contexts, though formula is safe (2*0.5-1=0)
    
    # We compare a small system (n=2) vs a larger system (n=4)
    # to show the trade-off between resource scaling and noise fragility.
    
    qfi_curve_small_n = [calculate_qfi(2, 2, F_base, k_decay, q) for q in q_sweep]
    qfi_curve_large_n = [calculate_qfi(2, 4, F_base, k_decay, q) for q in q_sweep]
    
    plt.figure(figsize=(10, 6))
    plt.plot(q_sweep, qfi_curve_small_n, label='System size N=4 (2 nodes, 2 qubits/node)', color='purple')
    plt.plot(q_sweep, qfi_curve_large_n, label='System size N=8 (2 nodes, 4 qubits/node)', color='orange')
    
    # Mark the specific q=0.75 point
    idx_75 = np.abs(q_sweep - 0.75).argmin()
    plt.scatter([0.75], [qfi_curve_large_n[idx_75]], color='red', zorder=5)
    plt.annotate(f'q=0.75\n(Large system)', xy=(0.75, qfi_curve_large_n[idx_75]), 
                 xytext=(0.65, qfi_curve_large_n[idx_75]*10),
                 arrowprops=dict(facecolor='black', shrink=0.05, width=1, headwidth=5))

    plt.title('Impact of Decoherence (q) on QFI')
    plt.xlabel('Decoherence Variable q ($q = (1+e^{-\\gamma t})/2$)')
    plt.ylabel('Quantum Fisher Information $Q_{\\theta_1}$')
    plt.yscale('log')
    plt.grid(True, which="both", ls="-", alpha=0.2)
    plt.legend()
    
    # Annotate physical meaning of q
    plt.text(0.95, max(qfi_curve_small_n)*0.5, 
             'No Noise\n($t=0, \\gamma=0$)', 
             ha='right', va='center', fontsize=9, 
             bbox=dict(boxstyle="round,pad=0.3", fc="white", ec="gray", alpha=0.8))
    
    plt.tight_layout()
    plt.savefig('qfi_decoherence_impact.png')
    plt.show()

if __name__ == "__main__":
    main()
```
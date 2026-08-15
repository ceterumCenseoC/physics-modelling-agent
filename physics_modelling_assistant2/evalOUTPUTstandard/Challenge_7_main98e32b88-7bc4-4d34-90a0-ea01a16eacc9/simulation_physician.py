

```python
import numpy as np
import matplotlib.pyplot as plt
from typing import Tuple, Dict

def calculate_qfi(
    d: int, 
    n: int, 
    F: float, 
    k: float, 
    gamma: float, 
    t: float
) -> Tuple[float, Dict[str, float]]:
    """
    Calculates the Quantum Fisher Information (QFI) for the distributed 
    quantum sensing scenario described.

    The model involves d sensor nodes, each with n qubits using a noisy GHZ state.
    
    Parameters:
    -----------
    d : int
        Number of sensor nodes.
    n : int
        Number of qubits per node.
    F : float
        Base fidelity of the d-qubit GHZ state.
    k : float
        Local quality factor for entanglement generation (fidelity multiplier).
    gamma : float
        Single-qubit dephasing rate (1/s).
    t : float
        Sensing duration (s).

    Returns:
    --------
    qfi : float
        The calculated Quantum Fisher Information for theta_1.
    params : dict
        Dictionary of intermediate parameters used in calculation.
        
    Model Details:
    --------------
    Target Parameter: theta_1 = (sum(x_i)) / sqrt(d)
    Initial Fidelity: F(n) = F * k^(n-1)
    Dynamics Noise: q = (1 + exp(-gamma * t)) / 2
    QFI Formula: F_Q = n^2 * d * (F(n))^2 * (2q - 1)^(2 * n * d)
    """
    
    # 1. Calculate Initial State Fidelity F(n)
    # Formula: F(n) = F * k^(n-1)
    fn = F * (k ** (n - 1))
    
    # 2. Calculate Dynamics Noise Parameter q
    # Formula: q = (1 + e^(-gamma * t)) / 2
    # Safety check for potential overflow in exp (though unlikely for small gamma*t)
    exp_term = np.exp(-gamma * t)
    q = 0.5 * (1 + exp_term)
    
    # 3. Calculate Dynamic Coherence Factor
    # The factor (2q - 1) represents the decay of off-diagonal elements.
    # With (2q - 1) = e^(-gamma * t), the term becomes (e^(-gamma * t))^(n*d)
    dynamic_factor = (2 * q - 1)
    
    # 4. Calculate Total Effective Coherence
    # The total coherence is the product of initial state fidelity and dynamic decay.
    # Note: The fidelity F(n) acts as the amplitude of the initial coherence term 
    # relative to a pure GHZ state.
    effective_visibility = fn * (dynamic_factor ** (n * d))
    
    # 5. Calculate Quantum Fisher Information (QFI)
    # Formula: F_Q = (n^2 * d) * (Effective Visibility)^2
    # The n^2 * d term comes from the variance of the generator for the scaled average
    # phase theta_1 in a pure GHZ state.
    # The variance of G = (1/sqrt(d)) * sum(x_i) is (n^2 * d) / 4.
    # QFI = 4 * Var(G) * (Visibility)^2 = n^2 * d * (Visibility)^2.
    
    qfi = (n**2 * d) * (effective_visibility ** 2)
    
    params = {
        'Fidelity_F_n': fn,
        'Parameter_q': q,
        'Dynamic_Factor': dynamic_factor,
        'Effect_Visibility': effective_visibility
    }
    
    return qfi, params

def parameter_sweep_plot():
    """
    Generates a plot showing the decay of QFI as a function of sensing time t
    for different network sizes (n).
    """
    # Fixed parameters based on "Suggested Starting Parameters"
    d = 5
    F = 0.90
    k = 0.98
    gamma = 1e5 # s^-1
    
    # Range of sensing time
    t_values = np.linspace(0, 5e-6, 100) # 0 to 5 microseconds
    
    # Different n values to compare local resource scaling
    n_values_list = [1, 2, 3, 4, 5]
    
    plt.figure(figsize=(10, 6))
    
    print(f"Generating QFI plot for d={d}, gamma={gamma:.1e} s^-1...")
    
    for n in n_values_list:
        qfi_values = []
        for t in t_values:
            qfi, _ = calculate_qfi(d, n, F, k, gamma, t)
            qfi_values.append(qfi)
            
        plt.plot(t_values * 1e6, qfi_values, label=f'n={n} qubits/node')
        
    plt.title(f'QFI vs Sensing Time (d={d} nodes)')
    plt.xlabel('Sensing Time t ($\mu$s)')
    plt.ylabel('Quantum Fisher Information $F_Q$')
    plt.yscale('log') # Log scale is crucial due to exponential decay
    plt.grid(True, which="both", ls="-", alpha=0.5)
    plt.legend()
    plt.tight_layout()
    
    # Save plot
    plt.savefig('qfi_distributed_sensing.png')
    print("Plot saved as 'qfi_distributed_sensing.png'")

def main():
    """
    Main execution function to demonstrate the model implementation.
    """
    print("--- Noisy Distributed Quantum Sensing QFI Model ---")
    
    # --- 1. Single Point Calculation (example) ---
    # Using the suggested realistic parameters
    params_example = {
        'd': 5,
        'n': 5,
        'F': 0.90,
        'k': 0.98,
        'gamma': 1e5,   # 100 kHz
        't': 1e-6       # 1 microsecond
    }
    
    print("\nExample Calculation:")
    print(f"Parameters: d={params_example['d']}, n={params_example['n']}, gamma={params_example['gamma']:.1e}, t={params_example['t']:.1e}")
    
    qfi, details = calculate_qfi(**params_example)
    
    print("-" * 40)
    print(f"Initial State Fidelity F(n) : {details['Fidelity_F_n']:.4f}")
    print(f"Noise Parameter q           : {details['Parameter_q']:.4f}")
    print(f"Dynamic Coherence (2q-1)    : {details['Dynamic_Factor']:.4f}")
    print(f"Effective Visibility        : {details['Effect_Visibility']:.6f}")
    print("-" * 40)
    print(f"Final QFI for theta_1       : {qfi:.6f}")
    print("-" * 40)
    
    # --- 2. Visualization ---
    # Create a plot to visualize the sensitivity decay
    try:
        parameter_sweep_plot()
    except Exception as e:
        print(f"Could not generate plot (display environment issue): {e}")

if __name__ == "__main__":
    main()
```
```python
import numpy as np
import matplotlib.pyplot as plt
from typing import Tuple

class ParafermionTunnelingModel:
    """
    Implements the Z_N parafermion zero-mode tunneling model to compute 
    the phase between initial and final ground states.
    """
    
    def __init__(self, n_order: int = 3):
        """
        Initialize the model with the parafermion order N.
        
        Args:
            n_order (int): The order of the parafermion group Z_N.
        """
        self.N = n_order
        # Define omega as the primitive N-th root of unity
        self.omega = np.exp(2j * np.pi / self.N)

    def get_ground_state_fusion_channel(self, phi: float) -> int:
        """
        Determines the ground state fusion channel k_ij from the Josephson phase phi.
        
        The condition is: k_ij < -phi / (2*pi) < k_ij + 1
        
        Args:
            phi (float): The Josephson phase in radians.
            
        Returns:
            int: The integer k_ij corresponding to the ground state fusion channel modulo N.
        """
        # Calculate the value: k < -phi / 2pi < k + 1
        val = -phi / (2 * np.pi)
        
        # We need the integer k such that k < val < k+1.
        # Strictly speaking, floor(val) is the largest integer less than or equal to val.
        # If val is exactly an integer, floor(val) == val, which violates k < val.
        # In physical scenarios, phases are swept smoothly; we treat exact integers 
        # by taking the limit from below (subtract a tiny epsilon).
        
        # Determine floor with epsilon correction for strict inequality
        epsilon = 1e-12
        k = int(np.floor(val - epsilon))
        
        # Return result modulo N to handle large phase accumulations
        return k % self.N

    def compute_accumulated_phase(self, k_34: int, k_23: int, k_12: int, k_13: int, q: int) -> Tuple[complex, float]:
        """
        Computes the accumulated phase factor exp(i*Theta) and phase Theta (radians).
        
        Formula from model derivation:
        |psi_f(q)> = exp( (i*pi/N) * (k_34 + k_23 + k_12 + k_13 + q) ) |psi_i(q)>
        
        Args:
            k_34, k_23, k_12, k_13 (int): Ground state fusion channels for links.
            q (int): Global fusion channel of unpaired zero modes.
            
        Returns:
            (complex, float): The phase factor e^(i*Theta) and the phase angle Theta in radians.
        """
        sum_k = k_34 + k_23 + k_12 + k_13
        # Calculate the total phase angle theta
        theta = (np.pi / self.N) * (sum_k + q)
        
        # Calculate the complex phase factor
        phase_factor = np.exp(1j * theta)
        
        return phase_factor, theta

def run_simulation():
    """
    Runs the simulation for the Z_N parafermion model with described parameters.
    """
    # 1. Setup
    # Parameters based on the "Starting Parameters" section of the context
    N = 3
    model = ParafermionTunnelingModel(N)
    
    print(f"--- Z_{N} Parafermion Tunneling Simulation ---")
    
    # 2. Define Phases and calculate k_ij
    # Selecting Josephson phases phi_ij that result in specific integer k_ij.
    # Constraint: k < -phi / 2pi < k + 1
    #
    # To get k=0: pick phi = -pi => -(-pi)/2pi = 0.5. 0 < 0.5 < 1. Correct.
    # To get k=1: pick phi = -3pi => -(-3pi)/2pi = 1.5. 1 < 1.5 < 2. Correct.
    
    test_phases = {
        'phi_34': -np.pi,       # Target k=0
        'phi_23': -np.pi,       # Target k=0
        'phi_12': -3 * np.pi,   # Target k=1
        'phi_13': -np.pi        # Target k=0
    }
    
    # Calculate K values from phases
    k_values = {}
    print("\nDeriving Fusion Channels k_ij from Phases phi_ij:")
    for key, phi in test_phases.items():
        k = model.get_ground_state_fusion_channel(phi)
        # Rename key for storage (phi_34 -> k_34)
        k_key = key.replace('phi', 'k')
        k_values[k_key] = k
        print(f"  {key} = {phi/np.pi:.2f}pi  ->  {k_key} = {k}")

    # 3. Compute Phase for different fusion channels q
    # q can range from 0 to N-1
    q_values = range(N)
    phases = []
    
    print(f"\n--- Calculating Phases for N={N} ---")
    print(f"Parameters: k_34={k_values['k_34']}, k_23={k_values['k_23']}, k_12={k_values['k_12']}, k_13={k_values['k_13']}")
    print(f"{'q':<5} | {'Phase Factor':<20} | {'Theta (rad)':<15} | {'Theta/pi':<10}")
    print("-" * 60)
    
    for q in q_values:
        factor, theta = model.compute_accumulated_phase(
            k_values['k_34'], k_values['k_23'], k_values['k_12'], k_values['k_13'], q
        )
        phases.append(theta)
        
        # Format complex number for clean output
        sign = "+" if factor.imag >= 0 else "-"
        factor_str = f"{factor.real:.3f}{sign}{abs(factor.imag):.3f}j"
        
        print(f"{q:<5} | {factor_str:<20} | {theta:<15.4f} | {theta/np.pi:.4f}")

    # 4. Visualization
    try:
        fig = plt.figure(figsize=(12, 5))
        
        # Plot 1: Phase vs Fusion Channel
        ax1 = fig.add_subplot(1, 2, 1)
        ax1.plot(q_values, phases, marker='o', linestyle='-', color='b', label='Accumulated Phase')
        ax1.set_xlabel('Fusion Channel q')
        ax1.set_ylabel('Phase $\Theta$ (radians)')
        ax1.set_title(f'Phase vs. $q$ ($Z_{N}$, N={N})\n$k_{{vals}}={k_values["k_34"]}{k_values["k_23"]}{k_values["k_12"]}{k_values["k_13"]}$')
        ax1.grid(True, alpha=0.3)
        ax1.legend()

        # Plot 2: Polar Plot of State Vectors
        ax2 = fig.add_subplot(1, 2, 2, projection='polar')
        for q in q_values:
            factor, theta = model.compute_accumulated_phase(
                k_values['k_34'], k_values['k_23'], k_values['k_12'], k_values['k_13'], q
            )
            # Annotate point on unit circle
            ax2.annotate(f"$q={q}$", xy=(theta, 1.1), ha='center')
            ax2.plot([theta, theta], [0, 1], marker='o', linestyle='-', alpha=0.6)
        
        ax2.set_title("Final State Phase Factors")
        ax2.set_yticks([])
        
        plt.tight_layout()
        plt.show()
    except Exception as e:
        print(f"Could not display plot: {e}")

if __name__ == "__main__":
    run_simulation()
```
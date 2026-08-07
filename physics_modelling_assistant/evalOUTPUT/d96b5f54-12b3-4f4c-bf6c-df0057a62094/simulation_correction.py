
```python
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap

def simulate_ising_model(L=100, J=0.441, steps=5000, visuals=True):
    """
    Simulates the 2D Ising Model on a LxL lattice using Metropolis-Hastings.
    
    Parameters:
    L (int): Linear dimension of the lattice.
    J (float): Coupling constant. Critical J ~ 0.4407 for 2D Ising.
    steps (int): Number of Monte Carlo sweeps to perform.
    visuals (bool): Whether to display the lattice configuration.
    
    Returns:
    float: The average magnetization per spin.
    """
    # Initialize random spins (1 or -1)
    spins = np.random.choice([-1, 1], size=(L, L))
    
    # Pre-compute Boltzmann factors for speed: dE = -sum_neighbors * (s_new - s_old)
    # s_new = -s_old, so s_new - s_old = -2*s_old
    # dE = 2 * s_old * sum_neighbors * J
    # We only care about acceptance probability exp(-dE).
    # For Ising, dE can only take specific values.
    
    # To keep it simple and readable, we compute dE on the fly or use a lookup
    # but for a robust implementation, let's use checkerboard updates or 
    # simple sequential updates with efficient numpy shifting for neighbors.
    
    magnetizations = []
    
    print(f"Simulating {L}x{L} Ising Model at J={J:.3f} for {steps} steps...")
    
    for step in range(steps):
        # Vectorized Metropolis update for performance
        # We update even and odd sites separately to allow vectorization
        # (Checkerboard decomposition)
        
        for parity in [0, 1]:
            # Create a mask for the current parity
            # (i + j) % 2 == parity
            i_indices, j_indices = np.indices((L, L))
            mask = ((i_indices + j_indices) % 2) == parity
            
            # Calculate sum of nearest neighbors with periodic boundary conditions
            # np.roll shifts the array: up, down, left, right
            neighbors = (np.roll(spins, 1, axis=0) + 
                         np.roll(spins, -1, axis=0) + 
                         np.roll(spins, 1, axis=1) + 
                         np.roll(spins, -1, axis=1))
            
            # Compute energy change if spin were flipped: dE = 2 * J * S_i * sum(neighbors)
            delta_E = 2 * J * spins * neighbors
            
            # Determine which sites to flip
            # Flip if dE < 0 (energy decreases) or if rand < exp(-dE)
            # Only consider sites in the current parity mask
            transition_probs = np.exp(-delta_E)
            random_thresholds = np.random.random((L, L))
            
            # Boolean array for sites to flip
            should_flip = (delta_E < 0) | (random_thresholds < transition_probs)
            
            # Apply mask to ensure we only update the correct parity
            final_flip_mask = should_flip & mask
            
            # Flip spins
            spins[final_flip_mask] *= -1
            
        # Equilibration: discard first 10% of steps
        if step > steps // 10:
            magnetizations.append(np.abs(np.sum(spins)) / (L * L))
            
    avg_magnetization = np.mean(magnetizations)
    
    if visuals:
        plt.figure(figsize=(8, 6))
        plt.imshow(spins, cmap='coolwarm', interpolation='nearest')
        plt.title(f'Spin Configuration at J={J:.3f}\nAvg Magnetization: {avg_magnetization:.3f}')
        plt.colorbar(ticks=[-1, 1], label='Spin Value')
        plt.axis('off')
        plt.show()
        
    return avg_magnetization

def scan_critical_point(L=20, j_start=0.3, j_end=0.6, steps=3000):
    """
    Scans J values to find the approximate critical point where Magnetization starts rising.
    Note: This is computationally intensive for L=100, so we use a smaller L for the scan
    demonstration, then verify J=0.441 for L=100.
    """
    J_vals = np.linspace(j_start, j_end, 15)
    mags = []
    
    print("Scanning J values...")
    for J in J_vals:
        m = simulate_ising_model(L=L, J=J, steps=steps, visuals=False)
        mags.append(m)
        print(f"J={J:.3f}, M={m:.3f}")
        
    plt.figure(figsize=(8, 5))
    plt.plot(J_vals, mags, 'o-', label=f'L={L}')
    plt.axvline(x=0.441, color='r', linestyle='--', label='Theoretical J_c (approx)')
    plt.xlabel('Coupling Constant J')
    plt.ylabel('Magnetization per Spin')
    plt.title('Phase Transition Scan')
    plt.legend()
    plt.grid(True)
    plt.show()

if __name__ == "__main__":
    # 1. High precision simulation near the expected critical point J ~ 0.441
    # We perform a single run at the suspected value to show the critical state.
    L_target = 100
    J_target = 0.441
    
    mag_critical = simulate_ising_model(L=L_target, J=J_target, steps=2000, visuals=True)
    print(f"Result at J={J_target}: Magnetization = {mag_critical:.4f}")
    print("At the critical point, magnetization is non-zero but finite-size dependent.")
    
    # 2. Verification scan on a smaller lattice (L=20) to show the phase transition logic
    # Scanning L=100 would take too long for a quick script.
    print("\nPerforming a quick scan on a smaller lattice (L=20) to visualize the transition...")
    scan_critical_point(L=20, j_start=0.3, j_end=0.6, steps=1000)
```
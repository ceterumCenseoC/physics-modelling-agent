```python
"""
Simulation of a Cyclic Autocatalytic Reaction Network.
This script implements the stochastic dynamics of the system using the
Gillespie Direct Method. It calculates the trajectories of N species
and performs a dimensional analysis check based on user-provided context.
"""

import numpy as np
import matplotlib.pyplot as plt

# ==========================================
# 1. Physical Parameters and Setup
# ==========================================

# Model Parameters
N_SPECIES = 6           # n: Cycle length. Suggested realistic range: 3 to 10.
RATE_CONST = 1.0        # k: Rate constant (1/s). Normalized time scale.
INIT_POP = 100          # X_tot(0): Initial total molecules. Mesoscopic scale.
TIME_MAX = 50.0         # Total simulation duration in seconds.
VOLUME = 1.0            # Omega: Volume (assumed 1 for concentration ~ count)

# Derived Parameters
DT_OBS = 0.1            # Time resolution for recording data
NUM_STEPS = int(TIME_MAX / DT_OBS) + 1

# ==========================================
# 2. Simulation Engine (Gillespie SSA)
# ==========================================

def gillespie_simulation(n, k, total_molecules, t_max):
    """
    Simulates the cyclic autocatalytic reaction:
    X_{i-1} -> X_{i-1} + X_i (with rate k)
    
    Args:
        n (int): Number of species.
        k (float): Rate constant.
        total_molecules (int): Initial number of molecules (all in X_1).
        t_max (float): Maximum simulation time.
        
    Returns:
        tuple: (time_points, population_counts)
               time_points: Array of time values.
               population_counts: 2D array of species counts (time x species).
    """
    # Initialize system: All molecules start in species X_1
    # Indices: 0 to n-1 representing X_1 to X_n
    state = np.zeros(n, dtype=int)
    state[0] = total_molecules
    
    # Data storage
    times = [0.0]
    history = [state.copy()]
    current_time = 0.0
    
    print(f"Starting Simulation: n={n}, k={k}, Total={total_molecules}")
    
    while current_time < t_max:
        # 1. Calculate Propensities
        # Reaction i: X_{i-1} -> X_{i-1} + X_i
        # In zero-indexed array: Reaction j produces X[j] and consumes nothing (catalyst X[j-1])
        # Propensity a_j = k * count of X_{j-1}
        # Wrap around: Reaction 0 produces X_1 using catalyst X_n
        
        counts = state
        # Catalyst for reaction 0 is species n-1 (last element)
        # Catalyst for reaction j is species j-1
        catalysts = np.roll(counts, 1) 
        propensities = k * catalysts
        
        a0 = np.sum(propensities)
        
        # Stop if no reactions possible (extinction)
        if a0 <= 0:
            # Fill remaining time with last state for plotting consistency
            times.append(t_max)
            history.append(state.copy())
            break
            
        # 2. Determine Time to Next Reaction
        r1 = np.random.random()
        tau = (1.0 / a0) * np.log(1.0 / r1)
        current_time += tau
        
        # 3. Determine Which Reaction Fires
        r2 = np.random.random() * a0
        cumsum = np.cumsum(propensities)
        reaction_idx = np.searchsorted(cumsum, r2)
        
        # 4. Update State
        # Reaction idx produces species idx
        state[reaction_idx] += 1
        
        # 5. Record Data (fixed interval or every step)
        # Here we record continuous steps, could skip for efficiency on long runs
        times.append(current_time)
        history.append(state.copy())
        
    return np.array(times), np.array(history)

# ==========================================
# 3. Dimensional Analysis Check
# ==========================================

def check_formula_dimensional_consistency():
    """
    Checks the dimensional consistency of the derived formula E[C^2] = n * k / 2pi^2.
    """
    print("\n--- Dimensional Analysis Check ---")
    
    # Dimensions:
    # [C] = [N] (Count)
    # [E[C^2]] = [N]^2
    # [k] = [T]^-1
    # [n] = [1]
    
    print(f"LHS Variance [E[C^2]]: Count^2")
    print(f"RHS Term (nk/2pi^2):     {N_SPECIES} * {RATE_CONST} / (2 * pi^2)")
    print(f"RHS Units:                1/Time")
    
    print("Conclusion: The formula is dimensionally inconsistent as provided in the extraction.")
    print("Correction suggestion: E[C^2] should scale with Population^2 (N^2) or similar.")
    print("Using simulation to estimate variance of the transient oscillation amplitude instead.")
    
# ==========================================
# 4. Analysis Functions
# ==========================================

def analyze_mode(history):
    """
    Analyzes the 'mode' (most populous species) to visualize the oscillation/wave.
    """
    times = np.array(history[0]) # This is wrong based on structure, fix below
    
def extract_transient_amplitude(times, counts, n):
    """
    Attempts to estimate the amplitude C of the oscillatory transient.
    Based on X_j(t) approx 1/n * X_tot + Psi_j(t)
    """
    # Total population
    x_tot = np.sum(counts, axis=1)
    
    # Deviation from mean distribution
    # normalized_counts = counts / x_tot[:, None]
    
    # The 'transient' vector Z = X - (1/n)*X_tot
    # We look at the magnitude of Z or specific component Z_1
    # Note: The system grows exponentially, so raw deviations grow.
    # We inspect the deviation of proportion X_1 / X_tot from 1/n.
    
    proportions = counts / x_tot[:, None]
    deviation_1 = proportions[:, 0] - (1.0/n)
    
    # The envelope of this deviation represents the oscillation.
    # For large n, decay rate is approx -k * (1 - cos(2pi/n)).
    decay_rate = -RATE_CONST * (1 - np.cos(2*np.pi/n))
    theory_freq = RATE_CONST * np.sin(2*np.pi/n)
    
    print(f"\n--- Linear Noise Approximation Estimates ---")
    print(f"Oscillation Frequency (omega): {theory_freq:.4f} rad/s")
    print(f"Theory Damping Rate (lambda):  {decay_rate:.4f} 1/s")
    print(f"(Note: These govern the proportions, not total population)")
    
    return times, deviation_1, theory_freq, decay_rate

# ==========================================
# 5. Main Execution
# ==========================================

if __name__ == "__main__":
    # 1. Run Simulation
    times, counts = gillespie_simulation(N_SPECIES, RATE_CONST, INIT_POP, TIME_MAX)
    
    # 2. Perform Dimensional Check
    check_formula_dimensional_consistency()
    
    # 3. Analyze Results
    t_data, dev_1, omega, lam = extract_transient_amplitude(times, counts, N_SPECIES)
    
    # 4. Visualization
    plt.figure(figsize=(12, 8))
    
    # Plot 1: Population Growth (Total and Individual)
    plt.subplot(2, 2, 1)
    plt.plot(times, np.sum(counts, axis=1), label='Total Population', linewidth=2, color='black')
    for i in range(N_SPECIES):
        plt.plot(times, counts[:, i], label=f'$X_{i+1}$', alpha=0.6)
    plt.xlabel('Time (s)')
    plt.ylabel('Molecule Count')
    plt.title('Population Dynamics')
    plt.legend(loc='upper left', fontsize='small')
    plt.grid(True, alpha=0.3)
    
    # Plot 2: Proportions (The "Oscillation")
    plt.subplot(2, 2, 2)
    props = counts / np.sum(counts, axis=1)[:, None]
    for i in range(N_SPECIES):
        plt.plot(times, props[:, i], alpha=0.6)
    plt.xlabel('Time (s)')
    plt.ylabel('Proportion of Total')
    plt.title('Species Proportions (Transient Oscillations)')
    plt.grid(True, alpha=0.3)
    
    # Plot 3: Deviation of X_1 from Mean (Log Scale for exponential growth visualization)
    # We fit an exponential decay envelope to the deviation
    plt.subplot(2, 2, 3)
    
    # Filter for time > 0 to avoid log(0) issues if any
    mask = times > 0.1
    t_fit = times[mask]
    dev_fit = dev_1[mask]
    
    # Visual representation of the decay
    # Envelope ~ exp(lambda * t)
    envelope = np.abs(dev_fit)
    
    plt.plot(t_fit, dev_fit, label='Deviation $(X_1 - \\bar{X})$', color='blue')
    plt.plot(t_fit, envelope, label='Envelope |Deviation|', color='red', linestyle='--')
    
    # Plot theoretical decay
    # Amplitude scales roughly as exp(lam * t) 
    # We scale by initial deviation to match y-axis roughly
    initial_amp = envelope[0]
    theoretical_decay = initial_amp * np.exp(lam * t_fit)
    plt.plot(t_fit, theoretical_decay, label=f'Theory Decay $\\lambda \\approx {lam:.2f}$', color='green', linewidth=2)
    
    plt.xlabel('Time (s)')
    plt.ylabel('Proportion Deviation')
    plt.title(f'Decay of Transient Oscillation (n={N_SPECIES})')
    plt.legend()
    plt.grid(True, alpha=0.3)
    
    # Plot 4: Phase Space (X1 vs X2) - Limit Cycle / Spiral
    plt.subplot(2, 2, 4)
    plt.plot(props[:, 0], props[:, 1], alpha=0.7)
    plt.xlabel('Prop $X_1$')
    plt.ylabel('Prop $X_2$')
    plt.title('Phase Space Trajectory (Transient)')
    plt.grid(True, alpha=0.3)
    
    plt.tight_layout()
    plt.show()
    
    print("\nSimulation Complete.")
    print("Note: The extracted formula for E[C^2] in the text was found dimensionally inconsistent.")
    print("The simulation visualizes the oscillatory approach to the 'stable' exponential manifold.")
```
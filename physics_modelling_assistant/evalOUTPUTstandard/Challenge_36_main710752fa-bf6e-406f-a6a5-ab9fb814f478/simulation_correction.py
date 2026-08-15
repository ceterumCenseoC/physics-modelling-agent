
```python
import numpy as np
import matplotlib.pyplot as plt
from typing import Tuple

def run_autocatalytic_simulation(n: int, k: float, X0: np.ndarray, total_time: float) -> Tuple[np.ndarray, np.ndarray]:
    """
    Simulates the autocatalytic reaction cycle using the Gillespie Stochastic Simulation Algorithm (SSA).
    
    The system consists of n species X_i. The reaction scheme is cyclic:
    X_{i-1} -> X_{i-1} + X_i (indices modulo n).
    
    Parameters:
        n (int): Number of species in the hypercycle.
        k (float): Reaction rate constant.
        X0 (numpy array): Initial population vector (length n).
        total_time (float): Maximum simulation time.
        
    Returns:
        time_log (numpy array): Time points of reactions.
        X_log (numpy array): Population vectors at each time point.
    """
    current_X = X0.astype(int).copy()
    current_time = 0.0
    
    time_log = [0.0]
    X_log = [current_X.copy()]
    
    # Using a while loop to run for a set duration rather than a set number of steps
    # to ensure comparable time trajectories.
    while current_time < total_time:
        # 1. Calculate propensities a_j = k * X_{j-1}
        # Reaction j produces species j. Catalyst is species j-1.
        # Vectorized calculation: Roll array X to align catalysts with reactions
        # Reaction 0: Catalyst X_{n-1}, Reactant X_{n-1} -> Product X_0
        catalysts = np.roll(current_X, 1)
        propensities = k * catalysts
        
        a0 = np.sum(propensities)
        
        # System stops if no reactants are left
        if a0 == 0:
            break
            
        # 2. Determine time to next reaction: tau = -ln(r1) / a0
        r1 = np.random.random()
        tau = -np.log(r1) / a0
        
        # 3. Determine which reaction fires (Linear search or algorithm such as Gibson-Bruck for n>100)
        # For n <= ~10, simple linear scan is efficient enough.
        r2 = np.random.random() * a0
        cumulative = 0.0
        reaction_index = 0
        
        for i, a_i in enumerate(propensities):
            cumulative += a_i
            if r2 <= cumulative:
                reaction_index = i
                break
        
        # 4. Update system state
        # Reaction 'reaction_index' produces one molecule of species 'reaction_index'
        current_X[reaction_index] += 1
        current_time += tau
        
        # Log data
        time_log.append(current_time)
        X_log.append(current_X.copy())
        
    return np.array(time_log), np.array(X_log)

def analyze_and_plot(n: int, k: float, time_log: np.ndarray, X_log: np.ndarray):
    """
    Analyzes the simulation results and plots the dynamics alongside theoretical predictions.
    """
    # Calculate total population over time
    N_total = X_log.sum(axis=1)
    
    # Calculate relative concentrations (fractions)
    fractions = X_log / N_total[:, np.newaxis]
    
    # --- Theoretical Calculation ---
    
    # Condition for oscillations: n >= 5 (derived from eigenvalue analysis)
    oscillation_condition = n >= 5
    
    # Calculate eigenvalues for the dominant mode m=1
    # lambda_m = (k/n) * (exp(i * 2pi / n) - 1)
    # Real part: (k/n)(cos(2pi/n) - 1)
    # Imaginary part: (k/n)sin(2pi/n)
    
    real_part = (k / n) * (np.cos(2 * np.pi / n) - 1)
    imag_part = (k / n) * np.sin(2 * np.pi / n)
    
    omega = imag_part
    decay_rate = real_part
    
    # Calculate Theoretical Mean Squared Amplitude E[C^2]
    # Derived from fluctuation-dissipation relation for the dominant mode
    # E[C^2] = N_tot / (4 * n * sin^2(pi/n))
    if n > 2:
        sin_term = np.sin(np.pi / n)
        E_C2_theoretical = N_total / (4 * n * (sin_term ** 2))
    else:
        E_C2_theoretical = np.zeros_like(N_total)

    # --- Visualization ---
    
    fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(12, 10))
    
    # Downsampling for cleaner plotting
    plot_step = max(1, len(time_log) // 2000)
    
    # Plot 1: Population Dynamics $X_j(t)$
    colors = plt.cm.viridis(np.linspace(0, 1, n))
    for i in range(n):
        ax1.plot(time_log[::plot_step], X_log[::plot_step, i], label=f'$X_{i+1}$', color=colors[i], alpha=0.8)
        
    ax1.set_title(f'Stochastic Transient Dynamics of Autocatalytic Hypercycle ($n={n}, k={k}$)')
    ax1.set_ylabel('Population Count $X_j(t)$')
    ax1.set_xlabel('Time (s)')
    ax1.grid(True, alpha=0.3)
    ax1.legend(loc='upper left', ncol=n//2 + 1)
    
    textstr = '\n'.join((
        r'$n \geq 5$ Condition: ' + ('Met' if oscillation_condition else 'Not Met'),
        r'Oscillation Freq $\omega \approx %.2f \times 10^{-3}$ rad/s' % (omega * 1000),
        r'Decay Rate $\lambda \approx %.2f \times 10^{-3}$ s$^{-1}$' % (decay_rate * 1000)
    ))
    props = dict(boxstyle='round', facecolor='wheat', alpha=0.5)
    ax1.text(0.65, 0.95, textstr, transform=ax1.transAxes, fontsize=10,
             verticalalignment='top', bbox=props)

    # Plot 2: Amplitude of Stochastic Fluctuations
    # We compare the theoretical E[C^2] with the spatial variance of the system.
    # Spatial variance represents the heterogeneity among species, which is driven by the oscillatory mode.
    
    deviations = X_log - (N_total[:, np.newaxis] / n)
    # Sum of squared deviations (proportional to energy in deviating modes)
    spatial_energy = np.sum(deviations**2, axis=1)
    
    ax2.plot(time_log, E_C2_theoretical, 'r--', label=r'Theoretical $\mathbb{E}[C^2]$', linewidth=2)
    ax2.plot(time_log[::plot_step], spatial_energy[::plot_step], 'b.', label='Simulation Energy (Sum of Squared Deviations)', alpha=0.1, markersize=2)
    
    ax2.set_title(r'Theoretical vs. Simulated Amplitude of Fluctuations $\mathbb{E}[C^2]$')
    ax2.set_ylabel(r'Amplitude Squared $\propto$ Energy')
    ax2.set_xlabel('Time (s)')
    ax2.set_yscale('log')
    ax2.legend()
    ax2.grid(True, alpha=0.3)
    
    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    # --- Proposed Starting Parameters ---
    # n = 8: Ensures oscillatory behavior (n >= 5)
    # k = 0.02: Moderate rate for transient observation
    # X0 = [1, ..., 0]: Start with a single copy of species 0
    n_species = 8
    k_rate = 0.02
    duration = 300.0  # seconds
    
    X_init = np.zeros(n_species)
    X_init[0] = 1.0
    
    print(f"--- Starting Autocatalytic Hypercycle Simulation ---")
    print(f"Parameters: n={n_species}, k={k_rate}, Initial State=Single Molecule")
    print(f"Running up to t={duration}s...")
    
    times, pops = run_autocatalytic_simulation(n_species, k_rate, X_init, duration)
    analyze_and_plot(n_species, k_rate, times, pops)
```
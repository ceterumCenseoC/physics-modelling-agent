```python
import numpy as np
import matplotlib.pyplot as plt

def calculate_asymptotic_growth_rate(lam_plus, lam_minus, k_plus, k_minus):
    """
    Calculates the asymptotic population growth rate Lambda_0.

    The formula is derived from the characteristic equation of the renewal process:
    1 = (k_plus / (k_plus + lam_plus - Lambda)) * (k_minus / (k_minus + lam_minus - Lambda))
    
    This simplifies to a quadratic equation: Lambda^2 - S*Lambda + P = 0
    where S = lam_plus + lam_minus + k_plus + k_minus
    and P = lam_plus * lam_minus + k_plus * lam_minus + k_minus * lam_plus
    
    We select the root: Lambda = 0.5 * (S - sqrt(S^2 - 4P))
    
    Parameters:
    -----------
    lam_plus : float
        Growth rate in the '+' state (1/time).
    lam_minus : float
        Growth rate in the '-' state (1/time).
    k_plus : float
        Rate parameter for the Gamma distribution in the '+' state (1/time).
    k_minus : float
        Rate parameter for the Gamma distribution in the '-' state (1/time).
        
    Returns:
    --------
    float
        The asymptotic population growth rate Lambda_0.
    """
    # Sum of parameters for the quadratic formula
    S = lam_plus + lam_minus + k_plus + k_minus
    
    # Product term for the quadratic formula
    P = lam_plus * lam_minus + k_plus * lam_minus + k_minus * lam_plus
    
    # Calculate the discriminant
    delta = S**2 - 4 * P
    
    # The roots are (S +/- sqrt(delta)) / 2.
    # We select the root that corresponds to the stable growth rate.
    # Based on the derivation: Lambda = 0.5 * (S - sqrt(delta))
    Lambda_0 = 0.5 * (S - np.sqrt(delta))
    
    return Lambda_0

def simulation_single_lineage(lam_plus, lam_minus, k_plus, k_minus, alpha, 
                              beta, v_bar, sigma_noise, v_b_init, T_max):
    """
    Simulates a single lineage of cell growth and division using an event-driven 
    approach. Tracks volume over time and calculates the total population count 
    based on symmetric division (1 -> 2 at each event).

    Parameters:
    -----------
    lam_plus, lam_minus : float
        Growth states.
    k_plus, k_minus, alpha : float
        Gamma parameters for switching (rate and shape).
    beta : float
        Size control parameter.
    v_bar : float
        Average birth volume.
    sigma_noise : float
        Std dev of division noise.
    v_b_init : float
        Initial birth volume.
    T_max : float
        Total simulation time.
        
    Returns:
    --------
    times : array
        Time points at which events occurred.
    logN : array
        Log of cumulative population size N(t) at each event.
    volumes : array
        History of the tracked cell's volume.
    """
    
    # Initialize state
    current_lam = lam_plus if np.random.rand() > 0.5 else lam_minus
    
    # Initial gamma waiting time
    scale = (1/k_plus) if current_lam == lam_plus else (1/k_minus)
    t_remain = np.random.gamma(alpha, scale)
    
    v = v_b_init
    v_birth = v_b_init
    
    # Calculate initial division target
    # Target includes additive noise
    noise = np.random.normal(0, sigma_noise)
    v_target = 2 * (v_birth**(1-beta)) * (v_bar**beta) + noise
    
    # Storage for results
    # We record state at every event (division or switch)
    event_times = [0.0]
    logN_history = [0.0] # log(N) where N starts at 1
    vol_history = [v]
    N_half_steps = 0 # N = 2^num_divisions. logN = num_divisions * log(2). 
                     # Using this exact counting avoids precision loss with large N.
    
    t = 0.0
    
    while t < T_max:
        # 1. Determine time to next division event given current growth rate
        # v(t) = v * exp(current_lam * t_div) = v_target
        # t_div = ln(v_target / v) / current_lam
        # Handle lambda=0 or v_target <= v edge cases
        if v_target > v and current_lam > 1e-9:
            t_div = np.log(v_target / v) / current_lam
        elif v_target <= v:
            # If noise makes target smaller than current size, divide immediately
            t_div = 0.0
        elif current_lam <= 0:
            t_div = np.inf
        else:
            t_div = np.inf

        # 2. Determine next event time
        if t_div < t_remain:
            dt_event = t_div
            event_type = 'division'
        else:
            dt_event = t_remain
            event_type = 'switch'
            
        # 3. Advance time and update volume (continuous growth)
        # Make sure we don't overshoot T_max
        if t + dt_event > T_max:
            dt_event = T_max - t
            event_type = 'finish'

        t += dt_event
        v = v * np.exp(current_lam * dt_event)
        t_remain -= dt_event
        
        # 4. Process event
        if event_type == 'switch':
            # Switch growth rate state
            if current_lam == lam_plus:
                current_lam = lam_minus
                scale = 1/k_minus
            else:
                current_lam = lam_plus
                scale = 1/k_plus
            
            # Sample new waiting time for the new state
            # If we just finished a Gamma phase, we start a fresh one.
            # Implementation Note: For phase-type processes, the time to next switch 
            # is always resampled upon entering a state.
            t_remain = np.random.gamma(alpha, scale)
            
            # Record state (optional, let's record at divisions for speed, 
            # but recording all shows the switching dynamics)
            event_times.append(t)
            vol_history.append(v)
            # logN does not change on switch
            logN_history.append(logN_history[-1])

        elif event_type == 'division':
            N_half_steps += 1
            current_logN = N_half_steps * np.log(2)
            
            event_times.append(t)
            vol_history.append(v)
            logN_history.append(current_logN)
            
            # Define birth size of the tracked daughter (symmetric division)
            v_birth = v / 2.0
            v = v_birth
            
            # New target with fresh noise
            noise = np.random.normal(0, sigma_noise)
            v_target = 2 * (v_birth**(1-beta)) * (v_bar**beta) + noise
            
            # t_remain is already updated (reduced by dt_event above)
            
        elif event_type == 'finish':
            break

    return np.array(event_times), np.array(logN_history), np.array(vol_history)

def plot_results(theoretical_lambda, times, logN):
    """
    Plots the simulation results against the theoretical prediction.
    """
    plt.figure(figsize=(10, 6))
    plt.plot(times, logN, label='Simulated Log Population', alpha=0.5)
    
    # Fit slope to the last portion to verify asymptotic growth
    fit_start = int(len(times) * 0.5)
    if fit_start < 2:
        fit_start = 2
        
    # Polyfit for slope: logN = slope * t + intercept
    coeffs = np.polyfit(times[fit_start:] - times[fit_start], logN[fit_start:], 1)
    fit_slope = coeffs[0]
    fit_intercept = coeffs[1]
    
    plt.plot(times[fit_start:], fit_slope * (times[fit_start:] - times[fit_start]) + fit_intercept, 
             'r--', linewidth=2, label=f'Fit Slope: {fit_slope:.3f}\nTheory: {theoretical_lambda:.3f}')
    
    plt.xlabel('Time (hours)')
    plt.ylabel('Log Population Count')
    plt.title('Asymptotic Population Growth Rate Simulation')
    plt.legend()
    plt.grid(True, alpha=0.3)
    plt.show()

def main():
    # --- Parameters Setup ---
    
    # 1. Growth Process Parameters
    lam_plus = 2.0      # h^-1 (Fast growth rate)
    lam_minus = 1.0     # h^-1 (Slow growth rate)
    k_plus = 0.5        # h^-1 (Switching rate + to -)
    k_minus = 0.5       # h^-1 (Switching rate - to +)
    alpha = 10.0        # Shape of Gamma waiting times (dimensionless)
    
    # 2. Cell Division Parameters
    # Note: According to the decoupling theorem, these do NOT affect Lambda 
    # to first order, but they affect the single lineage dynamics and 
    # size distribution shown in the second plot.
    beta = 0.5          # Size regulation (0=Timer-like, 1=Sizer-like)
    v_bar = 1.0         # Average birth volume (fL)
    sigma_noise = 0.1   # Division noise (standard deviation in fL)
    
    # --- Theoretical Calculation ---
    
    Lambda_theoretical = calculate_asymptotic_growth_rate(
        lam_plus, lam_minus, k_plus, k_minus
    )
    
    print(f"--- Model Configuration ---")
    print(f"Growth Rates: lambda+={lam_plus}, lambda-={lam_minus}")
    print(f"Switching Rates: k+={k_plus}, k-={k_minus}")
    print(f"Gamma Shape: alpha={alpha}")
    print(f"Division Control: beta={beta}, v_bar={v_bar}, sigma={sigma_noise}")
    print("-" * 30)
    print(f"Theoretical Asymptotic Growth Rate (Lambda): {Lambda_theoretical:.4f} h^-1")
    print("-" * 30)
    
    # --- Simulation for Validation ---
    print("Running event-driven lineage simulation...")
    
    T_max = 200.0 # hours
    
    times, logN, volumes = simulation_single_lineage(
        lam_plus, lam_minus, k_plus, k_minus, alpha,
        beta, v_bar, sigma_noise, v_b_init=v_bar, T_max=T_max
    )
    
    # Estimate Lambda from simulation slope (last 50% of data)
    idx_start = int(len(times) * 0.5)
    p = np.polyfit(times[idx_start:] - times[idx_start], logN[idx_start:], 1)
    Lambda_simulated = p[0]
    
    print(f"Simulated Growth Rate (from slope): {Lambda_simulated:.4f} h^-1")
    print(f"Difference: {abs(Lambda_theoretical - Lambda_simulated):.5f} h^-1")
    
    # --- Visualization ---
    
    # Plot 1: Population Growth
    plot_results(Lambda_theoretical, times, logN)
    
    # Plot 2: Single Lineage Volume Dynamics
    plt.figure(figsize=(10, 6))
    plt.step(times, volumes, where='post', linewidth=0.8)
    plt.xlabel('Time (hours)')
    plt.ylabel('Cell Volume (fL)')
    plt.title(f'Single Lineage Volume Dynamics\n(beta={beta}, noise={sigma_noise})')
    plt.grid(True, alpha=0.3)
    plt.show()

if __name__ == "__main__":
    main()
```
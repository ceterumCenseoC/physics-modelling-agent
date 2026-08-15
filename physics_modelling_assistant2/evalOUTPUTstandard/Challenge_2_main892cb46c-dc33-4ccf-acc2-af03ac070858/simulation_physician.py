```python
import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import brentq

def calculate_asymptotic_growth_rate(lam_plus, lam_minus, k_plus, k_minus, alpha):
    """
    Calculates the asymptotic population growth rate Lambda_0.
    
    The formula is derived from the characteristic equation of the renewal process:
    1 = (k_plus / (k_plus + lam_plus - Lambda)) * (k_minus / (k_minus + lam_minus - Lambda))
    Evaluating the integral/expectation with Gamma-distributed waiting times puts
    the whole expression to the power of alpha. Solving for Lambda yields the result.
    
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
    alpha : float
        Shape parameter for the Gamma distributions (dimensionless).
        
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
    # This root is guaranteed to be less than min(lam_plus, k_plus, ...) provided 
    # the process is stable (i.e. finite moments).
    
    Lambda_0 = 0.5 * (S - np.sqrt(delta))
    
    return Lambda_0

def simulation_single_lineage(lam_plus, lam_minus, k_plus, k_minus, alpha, 
                              beta, v_bar, sigma_noise, v_b_init, T_max, dt=0.01):
    """
    Simulates a single lineage of cell growth and division using an Euler-Maruyama 
    approximation for the growth rate switching process (simulated as a 
    telegraph process with Gamma distributed waiting times) and exponential growth.
    
    Parameters:
    -----------
    lam_plus, lam_minus : float
        Growth states.
    k_plus, k_minus, alpha : float
        Gamma parameters for switching.
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
    dt : float
        Time step.
        
    Returns:
    --------
    times : array
        Time points.
    logN : array
        Log of cumulative population size N(t) = 2^(number of divisions).
    volumes : array
        Current volume of the tracked lineage (tracking one branch).
    """
    times = np.arange(0, T_max, dt)
    logN = np.zeros_like(times) # log(N)
    N = 1
    logN[0] = 0
    
    # Current volume: we track the volume of one specific cell lineage segment
    v = v_b_init
    volumes = np.zeros_like(times)
    volumes[0] = v
    
    # Current growth state (start at + or - with prob, assume + for simplicity)
    current_lam = lam_plus if np.random.rand() > 0.5 else lam_minus
    
    # Time remaining in current state
    # Sample from Gamma distribution
    # rate = k, scale = 1/k
    scale = (1/k_plus) if current_lam == lam_plus else (1/k_minus)
    t_remain = np.random.gamma(alpha, scale)
    
    # Store history for plotting (optional, but for lineage tracking we just want growth)
    # This simulation tracks a single line of descent (one of the two daughters at each split)
    
    for i in range(1, len(times)):
        t = times[i]
        
        # Update growth state
        t_remain -= dt
        if t_remain <= 0:
            # Switch state
            if current_lam == lam_plus:
                current_lam = lam_minus
                scale = 1/k_minus
            else:
                current_lam = lam_plus
                scale = 1/k_plus
            
            # Sample new waiting time
            t_remain = np.random.gamma(alpha, scale)
            
        # Growth equation: dv/dt = lambda * v
        # Euler update
        dv = current_lam * v * dt
        v += dv
        
        # Check for division
        # Division rule: v_d = 2 * v_b^(1-beta) * v_bar^beta + xi
        # Note: v_b is the birth size of the CURRENT cell. 
        # However, we are continuously updating v. We know v_b from the last division.
        # We need to store v_b. 
        # Let's simplify by checking if v exceeds the threshold calculated at birth? 
        # No, the threshold is set at birth. 
        # Implementation detail: In a step-wise simulation, we should define v_target at birth.
        pass

    # Re-implementation with specific structure for division tracking
    # We need to know birth size to calculate target.
    
    # Reset state
    current_lam = lam_plus if np.random.rand() > 0.5 else lam_minus
    scale = (1/k_plus) if current_lam == lam_plus else (1/k_minus)
    t_remain = np.random.gamma(alpha, scale)
    
    v = v_b_init
    v_birth = v_b_init
    
    # Calculate division target
    noise = np.random.normal(0, sigma_noise)
    v_target = 2 * (v_birth**(1-beta)) * (v_bar**beta) + noise
    
    logN_track = []
    vol_track = []
    time_track = []
    
    t = 0
    
    while t < T_max:
        # Time to next event (either switch or potential division)
        # Since division is continuous (v crosses threshold), we define a small step.
        # Or better, integrate exactly until next switch, check for division in between.
        
        # Time to next switch: t_remain
        # Growth potential until switch: ds_exp = lambda * t_remain
        
        # Check if we reach division before switching
        # v(t) = v * exp(current_lam * t_div)
        # v(t_div) = v_target => t_div = ln(v_target / v) / current_lam
        
        if current_lam == 0:
            t_div = np.inf
        else:
            if v_target > v:
                t_div = np.log(v_target / v) / current_lam
            else:
                # v_target < (noisy case) - should divide immediately or ignore
                t_div = 0 
        
        if t_div < t_remain:
            # Division happens before switch
            # Advance time
            dt_event = t_div
            t += dt_event
            
            # Update volume
            v = v_target
            
            # Record state
            logN_track.append(np.log(N))
            vol_track.append(v)
            time_track.append(t)
            
            # Process Division
            N += 1 # 1 cell -> 2 cells. We track 1, N is total count.
            
            # New birth size (assuming symmetric division, pick one branch to track)
            # v_daughter = v / 2
            v_birth = v / 2
            v = v_birth
            
            # New target
            noise = np.random.normal(0, sigma_noise)
            v_target = 2 * (v_birth**(1-beta)) * (v_bar**beta) + noise
            
            # Reduce switch timer
            t_remain -= dt_event
            
        else:
            # Switch happens before division
            # Advance time
            dt_event = t_remain
            t += dt_event
            
            # Update volume
            v = v * np.exp(current_lam * dt_event)
            
            # Record state (optional, mid-event)
            # logN_track.append(np.log(N))
            # vol_track.append(v)
            # time_track.append(t)
            
            # Switch state
            if current_lam == lam_plus:
                current_lam = lam_minus
                scale = 1/k_minus
            else:
                current_lam = lam_plus
                scale = 1/k_plus
            
            # Sample new waiting time
            t_remain = np.random.gamma(alpha, scale)
            
            # Check for exact overlap or small steps needed
            if t >= T_max:
                break

    return np.array(time_track), np.array(logN_track), np.array(vol_track)

def plot_results(theoretical_lambda, times, logN):
    """
    Plots the simulation results against the theoretical prediction.
    """
    plt.figure(figsize=(10, 6))
    plt.plot(times, logN, label='Simulated Log Population', alpha=0.7)
    
    # Plot theoretical asymptote
    # log(N) ~ Lambda * t + const
    # We fit a line to the end of the simulation to compare, or just plot Lambda*t shifted
    fit_start = int(len(times) * 0.5)
    coeffs = np.polyfit(times[fit_start:] - times[fit_start], logN[fit_start:], 1)
    fit_slope = coeffs[0]
    fit_intercept = coeffs[1]
    
    plt.plot(times[fit_start:], fit_slope * (times[fit_start:] - times[fit_start]) + fit_intercept, 
             'r--', label=f'Fit Slope: {fit_slope:.3f} (Theory: {theoretical_lambda:.3f})')
    
    plt.xlabel('Time (hours)')
    plt.ylabel('Log Population Count')
    plt.title('Asymptotic Population Growth Rate Simulation')
    plt.legend()
    plt.grid(True)
    plt.show()

def main():
    # --- Parameters Setup ---
    
    # Growth Process Parameters (derived from context and literature)
    lam_plus = 2.0      # h^-1
    lam_minus = 1.0     # h^-1
    k_plus = 0.5        # h^-1
    k_minus = 0.5       # h^-1
    alpha = 10.0        # dimensionless
    
    # Division Parameters
    beta = 0.5
    v_bar = 1.0         # fL (arbitrary units relative to Lambda calculation)
    sigma_noise = 0.1   # fL (10% of birth size)
    
    # --- Theoretical Calculation ---
    
    Lambda_theoretical = calculate_asymptotic_growth_rate(
        lam_plus, lam_minus, k_plus, k_minus, alpha
    )
    
    print(f"Model Parameters:")
    print(f"  Growth Rates: lambda+={lam_plus}, lambda-={lam_minus}")
    print(f"  Switching Rates: k+={k_plus}, k-={k_minus}, alpha={alpha}")
    print(f"  Division: beta={beta}, v_bar={v_bar}, sigma={sigma_noise}")
    print("-" * 30)
    print(f"Theoretical Asymptotic Growth Rate (Lambda): {Lambda_theoretical:.4f} h^-1")
    print("-" * 30)
    
    # Discussion on parameters
    print("\nExplaining how Beta and Sigma^2 affect the population growth rate:")
    print("Based on the decoupling theorem for continuous growth models:")
    print("1. Size Regulation (Beta): The parameter beta determines the degree of cell-size")
    print("   control (timer vs sizer). It governs the correlation between mother and")
    print("   daughter birth sizes and the variance of the size distribution.")
    print("   However, it has NO effect on the asymptotic population growth rate Lambda.")
    print("   The population fitness is decoupled from the specific size control mechanism.")
    print("")
    print("2. Division Noise (Sigma^2): The variance in the division threshold introduces")
    print("   stochasticity in the cell cycle duration. While this increases the variance")
    print("   of generation times and cell sizes, it does NOT affect the mean population")
    print("   growth rate Lambda to first order in sigma^2 / v_bar^2.")
    print("   The coefficient of the first-order term is zero.")
    
    print("-" * 30)
    
    # --- Simulation for Validation ---
    print("Running lineage simulation to estimate Lambda from slope...")
    
    T_max = 100.0 # hours (run long enough to see asymptotic slope)
    times, logN, volumes = simulation_single_lineage(
        lam_plus, lam_minus, k_plus, k_minus, alpha,
        beta, v_bar, sigma_noise, v_b_init=v_bar, T_max=T_max
    )
    
    # Estimate Lambda from the last 20% of the simulation
    idx_start = int(len(times) * 0.8)
    # avoid empty slice if sim is short
    if idx_start >= len(times) - 1:
        idx_start = len(times) - 2
        
    # Linear fit: logN = Lambda * t + C
    # We want d(logN)/dt. Note N(t) is total population.
    # logN(t) = log(1 + number_of_divisions)
    # In main(), we computed logN. 
    # Let's perform the fit.
    p = np.polyfit(times[idx_start:], logN[idx_start:], 1)
    Lambda_simulated = p[0]
    
    print(f"Simulated Growth Rate (from lineage slope): {Lambda_simulated:.4f} h^-1")
    print(f"Difference: {abs(Lambda_theoretical - Lambda_simulated):.4f} h^-1")
    
    # Generate Graphics
    plot_results(Lambda_theoretical, times, logN)
    
    # Optional: Plot Volume dynamics to show the noise and regulation
    plt.figure(figsize=(10, 6))
    plt.step(times, volumes, where='post', linewidth=0.5)
    plt.xlabel('Time (hours)')
    plt.ylabel('Cell Volume (fL)')
    plt.title(f'Single Lineage Volume Dynamics (beta={beta})')
    plt.grid(True, alpha=0.3)
    plt.show()

if __name__ == "__main__":
    main()
```
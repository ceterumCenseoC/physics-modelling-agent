
```python
import numpy as np
import matplotlib.pyplot as plt

def calculate_sail_diagram(x_array, pz, mu, alpha_s, Cf, epsilon_uv, epsilon_ir):
    """
    Calculates the sail diagram contribution to the quasi-PDF based on the 
    derived formula.
    
    The formula is:
    q_sail(x) = alpha_s * C_F / (2 * pi) * [ 1/e_uv - 1/e_ir + ln(4 * mu^2 / ((1-x)*(x*pz)^2)) ]
    Support: 0 < x < 1, else 0.
    
    Parameters:
    -----------
    x_array : array-like
        Momentum fraction values.
    pz : float
        Longitudinal momentum of the nucleon (in GeV).
    mu : float
        Renormalization scale (in GeV).
    alpha_s : float
        Strong coupling constant.
    Cf : float
        Color factor.
    epsilon_uv : float
        UV regulator.
    epsilon_ir : float
        IR regulator.
        
    Returns:
    --------
    q_sail : numpy.ndarray
        The calculated sail diagram contribution.
    """
    # Initialize output array with zeros
    q_sail = np.zeros_like(x_array, dtype=float)
    
    # Calculate the prefactor
    prefactor = (alpha_s * Cf) / (2.0 * np.pi)
    
    # Identify the physical support region: 0 < x < 1
    # We use strict inequalities as per the definition
    mask = (x_array > 0) & (x_array < 1)
    
    # Extract x values within physical support
    x_phys = x_array[mask]
    
    # Calculate the Pole Terms
    # If regulators are exactly 0, numpy will raise a warning or return inf.
    # We handle division by zero allowing inf to represent the pole.
    pole_term = 0.0
    if epsilon_uv != 0:
        pole_term += 1.0 / epsilon_uv
    else:
        # Floating point infinity representation
        pole_term += np.inf
        
    if epsilon_ir != 0:
        pole_term -= 1.0 / epsilon_ir
    else:
        pole_term -= np.inf # -inf 
        
    # Calculate the Logarithmic Term
    # Log argument: 4 * mu^2 / ((1-x) * (x * pz)^2)
    # We assume x_phys are strictly between 0 and 1, so denominator is positive.
    log_arg = (4.0 * mu**2) / ((1.0 - x_phys) * (x_phys * pz)**2)
    
    # Calculate natural logarithm
    # Note: np.log(0) or negative values cause issues, but masked x ensures valid range.
    log_term = np.log(log_arg)
    
    # Assemble the total result
    q_sail[mask] = prefactor * (pole_term + log_term)
    
    return q_sail

def main():
    # --- 1. Define Constants and Parameters ---
    
    # Group Theory
    Nc = 3.0
    Cf = (Nc**2 - 1.0) / (2.0 * Nc) # Results in 4/3
    
    # Physical Parameters
    alpha_s = 0.30
    pz = 2.0     # GeV (Longitudinal momentum)
    mu = 2.0     # GeV (Renormalization scale)
    
    # Regulators
    # Use very small numbers to approximate the poles for numerical demonstration,
    # or set to 0 to see the infinite behavior (values will be inf).
    epsilon_uv = 1e-5 
    epsilon_ir = -1e-5
    
    # --- 2. Generate Data ---
    
    # Create a range of x values including outside physical support [-0.2, 1.2]
    x_vals = np.linspace(-0.2, 1.2, 500)
    
    # Calculate the full expression including the pole contributions
    # Note: With epsilon = 1e-5, the pole term is on the order of 1e5 to 1e6.
    q_sail_calc = calculate_sail_diagram(x_vals, pz, mu, alpha_s, Cf, epsilon_uv, epsilon_ir)
    
    # Calculate only the finite part (setting epsilons to infinity-like or just 0 for the math)
    # By setting epsilons -> 0, 1/0 -> inf. However, to plot the shape, 
    # we explicitly calculate just the log term part by passing epsilons such that pole terms are 0.
    # We can achieve this by calling with 0 and masking infs, or just calculating the log term manually.
    # Here we reuse the function: passing very large epsilon effectively makes 1/eps -> 0 for the "finite" view?
    # No, simpler: Pass 0, and then explicitly calculate the finite part logic or just plot the log.
    # Let's create a clean finite array for plotting the physical shape.
    q_sail_finite = np.zeros_like(x_vals)
    mask = (x_vals > 0) & (x_vals < 1)
    x_phys = x_vals[mask]
    log_arg = (4.0 * mu**2) / ((1.0 - x_phys) * (x_phys * pz)**2)
    prefactor = (alpha_s * Cf) / (2.0 * np.pi)
    q_sail_finite[mask] = prefactor * np.log(log_arg)
    
    # --- 3. Display Text Output ---
    
    print("-" * 80)
    print(f"{'Parameter':<25} | {'Value'}")
    print("-" * 80)
    print(f"{'Colors (N_c)':<25} | {Nc}")
    print(f"{'Color Factor (C_F)':<25} | {Cf:.4f}")
    print(f"{'Alpha_s':<25} | {alpha_s}")
    print(f"{'Momentum (p^z)':<25} | {pz} GeV")
    print(f"{'Renorm Scale (mu)':<25} | {mu} GeV")
    print(f"{'Regulator epsilon_UV':<25} | {epsilon_uv}")
    print(f"{'Regulator epsilon_IR':<25} | {epsilon_ir}")
    print("-" * 80)
    print("\nCalculation Results (Sample):")
    print("-" * 80)
    print(f"{'x':<10} | {'Full Expression (approx)':<25} | {'Finite Part (Log)':<20}")
    print("-" * 80)
    
    # Sample every 50th point for brevity
    step = 50
    for i in range(0, len(x_vals), step):
        x = x_vals[i]
        full_val = q_sail_calc[i]
        finite_val = q_sail_finite[i]
        
        # formatting large numbers from poles
        full_str = f"{full_val:.2e}" if abs(full_val) > 1000 else f"{full_val:.4f}"
        
        print(f"{x:<10.2f} | {full_str:<25} | {finite_val:<20.4f}")

    # --- 4. Plotting ---
    
    plt.figure(figsize=(10, 6))
    
    # Plot Finite Part (the x-dependence shape)
    # We plot this in blue
    plt.plot(x_vals, q_sail_finite, label='Finite Part (Logarithmic term)', color='blue', linewidth=2)
    
    # Plot the Full Expression
    # Depending on epsilon, this will be huge. We might skip plotting this or plot on a second axis
    # if we wanted to be thorough, but usually the divergent constant offset obscures the x-dependence.
    # We will just plot the finite part as it represents the physics of x-splitting.
    
    # Formatting
    plt.title(r'Sail Diagram: $\tilde{q}_{\rm sail}(x)$', fontsize=16)
    plt.xlabel(r'Momentum Fraction $x$', fontsize=14)
    plt.ylabel(r'$\tilde{q}_{\rm sail}(x)$', fontsize=14)
    plt.axvline(0, color='black', linestyle='--', linewidth=1, alpha=0.5)
    plt.axvline(1, color='black', linestyle='--', linewidth=1, alpha=0.5)
    plt.grid(True, which='both', linestyle='--', alpha=0.7)
    
    # Axis limits
    # Focus around the support region
    plt.xlim(-0.2, 1.2)
    # Dynamically set Y limits based on finite part range
    y_min = np.min(q_sail_finite) * 1.1
    y_max = np.max(q_sail_finite) * 1.1
    # Ensure 0 is in view if interval crosses it
    if y_min < 0 and y_max > 0:
        pass # Keep as is
    elif y_min < 0:
        y_max = max(0.5, y_max)
    elif y_max > 0:
        y_min = min(-0.5, y_min)
        
    plt.ylim(y_min, y_max)
    
    # Legend
    plt.legend(loc='best', fontsize=12)
    
    # Add parameter box text
    info_text = (
        r"$\alpha_s = " + f"{alpha_s}$" + "\n" +
        r"$p^z = " + f"{pz}$ GeV" + "\n" +
        r"$\mu = " + f"{mu}$ GeV" + "\n" +
        r"$C_F = " + f"{Cf:.3f}$"
    )
    plt.annotate(info_text, xy=(0.05, 0.05), xycoords='axes fraction',
                 bbox=dict(boxstyle="round", facecolor="white", alpha=0.8))
    
    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    main()
```
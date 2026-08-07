**

```python
import numpy as np
import matplotlib.pyplot as plt

def calculate_sail_diagram(x_array, pz, mu, alpha_s, Cf, epsilon_uv, epsilon_ir):
    """
    Calculates the sail diagram contribution to the quasi-PDF.
    
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
        UV regulator (usually small positive number or treated symbolically).
    epsilon_ir : float
        IR regulator (usually small negative number or treated symbolically).
        
    Returns:
    --------
    q_sail : numpy.ndarray
        The calculated sail diagram contribution.
    """
    q_sail = np.zeros_like(x_array)
    
    # The prefactor
    prefactor = (alpha_s * Cf) / (2 * np.pi)
    
    # Identify the physical support region: 0 < x < 1
    mask = (x_array > 0) & (x_array < 1)
    
    # Calculate the argument of the logarithm
    # Log term: ln( 4 * mu^2 / ((1-x) * (x * pz)^2) )
    # We must handle the case where x is exactly 0 or 1, though mask excludes strict boundaries.
    
    x_phys = x_array[mask]
    
    # Note: If epsilon_uv and epsilon_ir are strictly 0, the pole terms diverge.
    # For visualization of the finite part, we might separate them, 
    # but per prompt "implement the model", we include them.
    # If epsilon values provided are None or zero, we might only plot the finite part 
    # or handle the singularity. Here we assume standard float inputs.
    
    # Pole terms
    pole_term = 0.0
    if abs(epsilon_uv) > 1e-10:
        pole_term += 1.0 / epsilon_uv
    if abs(epsilon_ir) > 1e-10:
        pole_term -= 1.0 / epsilon_ir
        
    # Logarithmic term
    # Ensure no division by zero if x_phys contains boundary floats close to 0 or 1
    # Clip x slightly to be safe for numerical calculation if strictly math boundaries aren't hit
    log_arg = (4 * mu**2) / ((1 - x_phys) * (x_phys * pz)**2)
    
    # Handle potential negative arguments or zeros if parameters are unphysical, 
    # though with 0<x<1 and real masses, it should be positive.
    log_term = np.log(log_arg)
    
    q_sail[mask] = prefactor * (pole_term + log_term)
    
    return q_sail

def main():
    # --- Realistic Starting Parameters ---
    
    # 1. Physical Constants
    Nc = 3.0
    Cf = (Nc**2 - 1) / (2 * Nc) # Should be 4/3
    
    # 2. Coupling and Kinematics
    # Using the values suggested in the problem context
    alpha_s = 0.30
    pz = 2.0  # GeV
    mu = 2.0  # GeV (Set equal to pz for this demonstration as often done)
    
    # 3. Regulators
    # For numerical representation of the "O(epsilon^0)" finite result,
    # we typically consider the poles to be subtracted or cancelled in physical quantities.
    # However, to output the function as requested, we can set epsilons to a very small 
    # number or just calculate the finite part.
    # Let's compute the full expression with tiny epsilons to show the code works,
    # but we note that for a plot of the "shape", the pole terms are constant divergences.
    epsilon_uv = 1e-5 # Small positive
    epsilon_ir = -1e-5 # Small negative
    
    # --- Generate Data ---
    
    # Define x range: include outside support to show it is zero
    x_vals = np.linspace(-0.2, 1.2, 100)
    
    # Calculate
    # We will calculate the full expression. 
    # Note: The pole term 1/eps is a constant offset for all x in (0,1).
    # In a real plot of the X-dependence, this constant shift (infinity) 
    # makes the plot unreadable. 
    # To make the graphic "sensible", we will plot the finite part (log term) separately 
    # or plot the total value assuming some large cutoff, but plotting the finite part 
    # is physically most meaningful for the shape of the matching kernel.
    
    q_sail_total = calculate_sail_diagram(x_vals, pz, mu, alpha_s, Cf, epsilon_uv, epsilon_ir)
    
    # Calculate just the finite part for visualization purposes (poles removed)
    q_sail_finite = calculate_sail_diagram(x_vals, pz, mu, alpha_s, Cf, 0.0, 0.0)
    
    # --- Display Results ---
    
    print(f"Parameters: alpha_s={alpha_s}, C_F={Cf:.3f}, pz={pz} GeV, mu={mu} GeV")
    print(f"Regulators: epsilon_UV={epsilon_uv}, epsilon_IR={epsilon_ir}")
    print("-" * 60)
    print(f"{'x':<10} | {'q_sail_total (approx)':<20} | {'q_sail_finite':<20}")
    print("-" * 60)
    
    # Print a subset of values
    for i in range(len(x_vals)):
        if i % 10 == 0: # Print every 10th point
            print(f"{x_vals[i]:<10.2f} | {q_sail_total[i]:<20.6f} | {q_sail_finite[i]:<20.6f}")
            
    # --- Create Graphics ---
    
    plt.figure(figsize=(10, 6))
    
    # Plot the finite part (the physical x-dependence)
    plt.plot(x_vals[(x_vals>0) & (x_vals<1)], q_sail_finite[(x_vals>0) & (x_vals<1)], 
             label=r'Finite Part: $\frac{\alpha_s C_F}{2\pi} \ln(\frac{4\mu^2}{(1-x)(x p^z)^2})$', 
             color='blue', linewidth=2)
             
    # Plot zero outside
    plt.plot(x_vals[(x_vals<=0) | (x_vals>=1)], q_sail_finite[(x_vals<=0) | (x_vals>=1)], 
             color='black', linestyle='-', linewidth=1) # Zero line
    
    # Styling
    plt.title(r'Sail-Diagram Contribution to Quasi-PDF ($\tilde{q}_{\rm sail}$)', fontsize=16)
    plt.xlabel(r'Momentum Fraction $x$', fontsize=14)
    plt.ylabel(r'$\tilde{q}_{\rm sail}(x)$', fontsize=14)
    plt.grid(True, alpha=0.3)
    plt.axhline(0, color='black', linewidth=0.8)
    plt.axvline(0, color='black', linestyle='--', alpha=0.5)
    plt.axvline(1, color='black', linestyle='--', alpha=0.5)
    plt.legend(fontsize=12)
    
    # Annotation for parameters
    param_text = (f"$\\alpha_s = {alpha_s}$\n"
                  f"$p^z = {pz}$ GeV\n"
                  f"$\\mu = {mu}$ GeV\n"
                  f"$C_F = {Cf:.3f}$")
    plt.annotate(param_text, xy=(0.05, 0.95), xycoords='axes fraction',
                 verticalalignment='top', bbox=dict(boxstyle='round', facecolor='white', alpha=0.8))

    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    main()
```
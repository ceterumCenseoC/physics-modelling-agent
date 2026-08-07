```python
import numpy as np
import matplotlib.pyplot as plt

def compute_thermal_one_point_function(r0, mass_m, eta=None):
    """
    Computes the one-point function scaling for AdS3/BCFT2 based on the geodesic approximation.
    
    The formula derived is <O(x)> ~ r0^m, where r0 is the black hole horizon radius
    and m is the mass of the bulk field (conformal dimension).
    
    Parameters:
    -----------
    r0 : float or array_like
        The black hole horizon radius (proportional to Temperature T).
    mass_m : float
        The mass of the bulk field, acting as the exponent. 
        In the large mass limit, m approximates the conformal dimension Delta.
    eta : float, optional
        The brane tension. Included for interface compatibility. The calculation
        assumes the brane is behind the horizon, and thus does not affect the 
        boundary one-point function at leading order.
        
    Returns:
    --------
    float or ndarray
        The proportional value of the one-point function <O(x)>.
    """
    
    # 1. Validate Inputs
    # Ensure r0 is strictly positive as it represents a physical radius.
    if np.any(r0 <= 0):
        raise ValueError("Black hole radius r0 must be positive.")
        
    # Mass m is typically positive in this context (related to Delta >= 0).
    if mass_m < 0:
        raise ValueError("Mass m must be non-negative (related to conformal dimension).")
        
    # Check eta if provided, though it doesn't affect the calculation.
    if eta is not None:
        # The problem context implies 0 < eta < 1 for brane tension values, 
        # but we allow float inputs with a warning if it seems physically off.
        if eta <= 0 or eta >= 1:
            print(f"Warning: Tension eta={eta} is outside the typical physical range (0, 1), but proceeding.")
            print("Note: The calculation result is independent of eta in this approximation.")

    # 2. Compute the One-Point Function
    # Based on the derivation: <O(x)> ~ exp(-m * l_hor_ren)
    # where l_hor_ren = -log(r0) (in dimensionless units where L_Ads = 1)
    # Resulting in: <O(x)> ~ exp(-m * -log(r0)) = r0^m
    
    # We use NumPy's power function to support both scalar and array inputs for r0.
    one_point_function = np.power(r0, mass_m)
    
    return one_point_function

def visualize_scaling():
    """
    Creates a visualization of how the one-point function scales with temperature (r0)
    for different masses (conformal dimensions).
    """
    # Define range of Horizon Radii (Temperature)
    # r0 is proportional to T. We use a logarithmic space to see power-law scaling clearly.
    r0_values = np.logspace(-1, 1, 100) # r0 from 0.1 to 10
    
    # Define a set of masses (Dimensions) to visualize
    # Corresponding to relevant operators of increasing strength.
    masses = [1, 2, 3]
    
    plt.figure(figsize=(10, 6))
    
    for m in masses:
        # Compute scaling using the vectorized function
        O_vals = compute_thermal_one_point_function(r0_values, m)
        
        plt.plot(r0_values, O_vals, label=rf'Mass $m = {m}$ ($\Delta \approx {m}$)')
    
    plt.title(r'Geodesic Approximation: $\langle \mathcal{O}(x) \rangle \propto r_0^m$')
    plt.xlabel(r'Horizon Radius $r_0$ ($\propto$ Temperature $T$)')
    plt.ylabel(r'One-Point Function Magnitude $\langle \mathcal{O}(x) \rangle$')
    plt.grid(True, which='both', linestyle='--', alpha=0.7)
    
    # Log-Log scale is essential to verify the linear relationship in log-log space
    # which indicates a power law.
    plt.yscale('log') 
    plt.xscale('log')
    plt.legend()
    
    # Add annotation about Brane Tension independence
    plt.annotate(
        'Independent of Brane Tension $\eta$\n(Behind Horizon)', 
        xy=(0.05, 0.95), 
        xycoords='axes fraction',
        fontsize=10,
        bbox=dict(boxstyle="round,pad=0.3", fc="white", ec="gray", alpha=0.8)
    )
    
    plt.show()

# --- Main Execution Block ---

if __name__ == "__main__":
    # 1. Exact Calculation demonstration
    # Using the values from the theoretical derivation section:
    # r0 (horizon radius) = 1.0
    # m (mass/dimension) = 2.0
    
    input_r0 = 1.0
    input_m = 2.0
    input_eta = 0.5 # Arbitrary value, result is independent of eta
    
    result = compute_thermal_one_point_function(input_r0, input_m, input_eta)
    
    print(f"--- Exact Result ---")
    print(f"Parameters: Horizon Radius r0 = {input_r0}, Mass m = {input_m}")
    print(f"One-Point Function <O(x)> proportional to: {result}")
    print(f"Dependency: Scales as r0^{input_m}")
    print(f"Brane Tension Influence: None (brane is behind horizon)")
    
    # 2. Generate Graphics
    # Visualizing the scaling behavior derived in the solution
    print("\nGenerating scaling visualization...")
    visualize_scaling()
```
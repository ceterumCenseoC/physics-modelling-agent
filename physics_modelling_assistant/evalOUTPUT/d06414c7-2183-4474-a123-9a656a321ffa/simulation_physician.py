
```python
import numpy as np

def compute_thermal_one_point_function(r0, mass_m, eta=None):
    """
    Computes the one-point function scaling for AdS3/BCFT2 based on the geodesic approximation.
    
    Parameters:
    -----------
    r0 : float
        The black hole horizon radius (proportional to Temperature T).
    mass_m : float
        The mass of the bulk field, corresponding to the conformal dimension Delta.
    eta : float, optional
        The brane tension. Included for interface compatibility, but does not affect 
        the result in the leading geodesic approximation as the brane is behind the horizon.
        
    Returns:
    --------
    float
        The proportional value of the one-point function <O(x)>.
    """
    
    # 1. Validate Inputs
    if r0 <= 0:
        raise ValueError("Black hole radius r0 must be positive.")
    if mass_m < 0:
        raise ValueError("Mass m must be non-negative (related to conformal dimension).")
    if eta is not None and (eta <= 0 or eta >= 1):
        # While eta doesn't change the result in this approximation, the problem states 0 < eta < 1
        print(f"Warning: Tension eta={eta} is outside the typical physical range (0, 1), but proceeding.")

    # 2. Compute the One-Point Function
    # According to the derivation: <O(x)> ~ exp(-m * l_hor_ren)
    # where l_hor_ren = -log(r0) (in dimensionless units where L_Ads = 1)
    # Therefore: <O(x)> ~ exp(m * log(r0)) = r0^m
    
    # We treat mass_m directly as the exponent corresponding to the conformal dimension.
    # In strict AdS3 units, Delta = 1 + sqrt(1 + m^2). However, in the large mass limit,
    # Delta ~ m. The geodesic approximation <O> ~ r0^Delta holds.
    
    one_point_function = r0**mass_m
    
    return one_point_function

def visualize_scaling():
    """
    Creates a visualization of how the one-point function scales with temperature (r0)
    for different masses (conformal dimensions).
    """
    import matplotlib.pyplot as plt
    
    # Define range of Horizon Radii (Temperature)
    # r0 = T * pi, so r0 is proportional to T.
    r0_values = np.linspace(0.1, 5.0, 100)
    
    # Define set of masses (Dimensions) to visualize
    # Corresponding to relevant operators (e.g., Delta = 2, 3, 4)
    masses = [1, 2, 3]
    
    plt.figure(figsize=(10, 6))
    
    for m in masses:
        # Compute scaling
        # We drop the strict eta dependence as derived (eta independent)
        O_vals = [compute_thermal_one_point_function(r, m) for r in r0_values]
        
        plt.plot(r0_values, O_vals, label=rf'Mass $m = {m}$ ($\Delta \approx {m}$)')
    
    plt.title(r'Geodesic Approximation: $\langle \mathcal{O}(x) \rangle \propto r_0^m$')
    plt.xlabel(r'Horizon Radius $r_0$ ($\propto$ Temperature $T$)')
    plt.ylabel(r'One-Point Function Magnitude $\langle \mathcal{O}(x) \rangle$')
    plt.grid(True, which='both', linestyle='--', alpha=0.7)
    plt.yscale('log') # Log scale to visualize power law clearly
    plt.xscale('log')
    plt.legend()
    
    # Add annotation about Brane Tension
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
    # 1. Exact Calculation as requested
    # We use the values from the detailed derivation section:
    # r0 (horizon radius) = 1.0
    # m (mass) = 2 (corresponding to Delta = 2 for simple scalar examples)
    
    input_r0 = 1.0
    input_m = 2.0
    input_eta = 0.5 # Arbitrary value, as result is independent of eta
    
    result = compute_thermal_one_point_function(input_r0, input_m, input_eta)
    
    print(f"--- Exact Result ---")
    print(f"Parameters: Horizon Radius r0 = {input_r0}, Mass m = {input_m}")
    print(f"One-Point Function <O(x)> proportional to: {result}")
    print(f"Dependency: Scales as r0^{input_m}")
    print(f"Brane Tension Influence: None (brane is behind horizon)")
    
    # 2. Generate Graphics
    # Visualizing the scaling behavior derived in the solution
    print("\nGenerating scaling visualization...")
    try:
        visualize_scaling()
    except ImportError:
        print("Matplotlib not found. Skipping graphic generation.")
```
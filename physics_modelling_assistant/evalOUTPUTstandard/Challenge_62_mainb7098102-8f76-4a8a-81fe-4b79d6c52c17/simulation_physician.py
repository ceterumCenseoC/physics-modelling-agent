
```python
import numpy as np
import matplotlib.pyplot as plt

def calculate_violation(phi, k):
    """
    Calculates the quantum violation delta based on the derived formula.
    
    Parameters:
    phi : float or np.array
        The phase angle in radians.
    k : int
        The integer parameter defining N = 2k + 1 paths.
        
    Returns:
    float or np.array
        The calculated violation delta.
    """
    N = 2 * k + 1
    
    # Derived formula: 
    # delta = (4*k / (2k+1)^2) * [k+1 - k*cos(phi)] - 2k
    
    numerator = 4 * k
    denominator = (2 * k + 1)**2
    term_bracket = k + 1 - k * np.cos(phi)
    
    delta = (numerator / denominator) * term_bracket - 2 * k
    return delta

def find_violation_range(k, num_points=1000):
    """
    Determines the range of phi in [0, pi] where delta > 0.
    
    Parameters:
    k : int
        The integer parameter N = 2k + 1.
    num_points : int
        Resolution for scanning the domain.
        
    Returns:
    tuple
        (range_start, range_end) or (None, None) if no violation.
    """
    phi_values = np.linspace(0, np.pi, num_points)
    deltas = calculate_violation(phi_values, k)
    
    # Find indices where delta > 0
    # We use a small epsilon for floating point comparison, though 0 should be exact mathematically
    violation_indices = np.where(deltas > 1e-10)[0]
    
    if len(violation_indices) == 0:
        return None, None
    
    # Assuming the range T is a single continuous interval (or empty)
    start_idx = violation_indices[0]
    end_idx = violation_indices[-1]
    
    # Map indices back to phi values
    # Refine boundaries using interpolation or simple selection
    phi_start = phi_values[start_idx]
    phi_end = phi_values[end_idx]
    
    # Calculate exact boundary analytically if possible for cleaner output
    # Condition: cos(phi) < (1 - 2k - 2k^2) / (2k)
    bound_rhs = (1 - 2*k - 2*(k**2)) / (2*k)
    
    # The range is (arccos(bound_rhs), pi] if bound_rhs is in [-1, 1]
    if -1 <= bound_rhs <= 1:
        exact_start = np.arccos(bound_rhs)
        return exact_start, np.pi
    else:
        return None, None

def main():
    # --- Setup for k=1 (N=3) ---
    k = 1
    print(f"--- Analysis for k={k} (N={2*k+1}) ---")
    
    # 1. Calculate Delta function
    phi = np.linspace(0, np.pi, 500)
    delta = calculate_violation(phi, k)
    print(f"Formula check: delta(0) = {calculate_violation(0, k):.4f}, delta(pi) = {calculate_violation(np.pi, k):.4f}")
    
    # 2. Determine Violation Range T
    start, end = find_violation_range(k)
    if start is not None:
        print(f"Violation Range T: ({start:.4f}, {end:.4f}] radians")
        print(f"Violation Range T: ({np.degrees(start):.2f}, {np.degrees(end):.2f}] degrees")
    else:
        print("Violation Range T: Empty set. No violation found for this configuration.")
        
    # 3. Find phi_max
    # Theoretical derivation shows phi_max = pi
    phi_max = np.pi
    delta_max = calculate_violation(phi_max, k)
    print(f"Maximal violation occurs at phi_max = {phi_max:.4f} rad ({np.degrees(phi_max):.2f} deg)")
    print(f"Maximal violation value delta_max = {delta_max:.4f}")
    print("-" * 30)
    
    # --- Visualization ---
    plt.figure(figsize=(10, 6))
    plt.plot(phi, delta, label=r'$\delta(\phi)$', color='blue', linewidth=2)
    
    # Mark the classical bound (delta=0)
    plt.axhline(0, color='black', linestyle='--', label='Classical Bound ($\delta=0$)')
    
    # Highlight Violation Range T
    if start is not None:
        # Create a masked array for the violation region
        mask = (phi >= start)
        plt.fill_between(phi[mask], 0, delta[mask], color='red', alpha=0.3, label='Violation Region $T$')
        
        # Mark phi_max only if it is within the violation range?
        # Actually, usually max violation implies largest positive deviation.
        # If delta_max is negative, the "violation" never occurred, but the "maximum" of the function still exists.
        # We will mark the maximum value of the function.
        plt.scatter([phi_max], [delta_max], color='green', s=100, zorder=5, label=rf'$\phi_{{max}} = \pi$')
    else:
        plt.scatter([phi_max], [delta_max], color='green', s=100, zorder=5, label=rf'Maximum at $\pi$ (No Violation)')

    plt.title(r'Quantum Violation $\delta(\phi)$ for $k=1$ ($N=3$)')
    plt.xlabel(r'Phase $\phi$ (radians)')
    plt.ylabel(r'Violation $\delta$')
    plt.legend(loc='best')
    plt.grid(True, alpha=0.5)
    
    # Annotate specific points
    plt.annotate(r'$\phi=0$', xy=(0, calculate_violation(0, k)), xytext=(0.2, calculate_violation(0, k)),
                 arrowprops=dict(facecolor='black', shrink=0.05))
    plt.annotate(r'$\phi=\pi$', xy=(np.pi, calculate_violation(np.pi, k)), xytext=(2.5, calculate_violation(np.pi, k)),
                 arrowprops=dict(facecolor='black', shrink=0.05))

    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    main()
```
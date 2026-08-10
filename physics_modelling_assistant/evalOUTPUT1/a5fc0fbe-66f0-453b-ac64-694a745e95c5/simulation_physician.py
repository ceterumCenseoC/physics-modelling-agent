
```python
import numpy as np
import matplotlib.pyplot as plt

def calculate_delta(phi, k):
    """
    Calculates the violation delta for a given phase phi and index k (N=2k+1).
    The formula derived is: delta = (2k(3 - 4k^2 - 4k*cos(phi))) / (2k+1)^2
    """
    numerator = 2 * k * (3 - 4 * k**2 - 4 * k * np.cos(phi))
    denominator = (2 * k + 1)**2
    return numerator / denominator

def find_violation_range(k):
    """
    Determines the range T of phi for which quantum violation occurs (delta > 0).
    Based on the condition cos(phi) < (3 - 4k^2) / 4k.
    
    Returns:
        tuple: (lower_bound, upper_bound) in radians. 
               Returns (None, None) if no violation is possible (e.g. for k >= 2).
    """
    if k == 0:
        return (None, None) # N=1 is trivial
        
    violation_threshold = (3 - 4 * k**2) / (4 * k)
    
    # Check if the threshold is achievable within [-1, 1] for cos(phi)
    if violation_threshold < -1:
        # Condition cos(phi) < (value < -1) is never satisfied in [0, pi]
        # because cos(phi) >= -1.
        return (None, None)
    elif violation_threshold > 1:
        # Violation occurs for all phi, though physically phi is usually [0, pi]
        return (0, np.pi)
    else:
        # arccos returns value in [0, pi]
        lower_bound = np.arccos(violation_threshold)
        return (lower_bound, np.pi)

# --- Parameters as suggested ---
k_value = 1  # Corresponds to N=3, the only N with violation for this model

# --- 1. Express Violation for k=1 ---
phi_values = np.linspace(0, 2*np.pi, 500)
delta_values = calculate_delta(phi_values, k_value)

print(f"--- Part (1): Violation for k={k_value} (N={2*k_value+1}) ---")
# We display the formula and the max value calculated via code
max_delta_idx = np.argmax(delta_values)
phi_numeric_max = phi_values[max_delta_idx]
max_delta_value = delta_values[max_delta_idx]

print(f"Delta(phi) = -({2 + 8*np.cos(phi_values)})/9") # Display formula dynamically
print(f"Max calculated Delta at phi={phi_numeric_max:.2f} rad: {max_delta_value:.4f}")
print(f"Theoretical Max at phi=pi: {calculate_delta(np.pi, k_value):.4f}")


# --- 2. Determine Range T ---
print(f"\n--- Part (2): Range of Violation T for k={k_value} ---")
lb, ub = find_violation_range(k_value)
if lb is not None:
    print(f"Violation occurs for phi in ({lb:.4f}, {ub:.4f}] radians")
    print(f"Or in degrees: ({np.degrees(lb):.2f}, {np.degrees(ub):.2f}]")
else:
    print("No violation range exists for this k.")

# --- 3. Maximal Violation Angle ---
print(f"\n--- Part (3): Maximal Violation Angle ---")
# The theoretical derivation suggests phi_max = pi.
print(f"phi_max = {np.pi} radians ({180} degrees)")


# --- Graphics ---
plt.figure(figsize=(10, 6))
plt.plot(phi_values, delta_values, label=f'$\delta(\phi)$ for k={k_value} ($N={2*k_value+1}$)', color='blue')
plt.axhline(0, color='black', linestyle='--', linewidth=1, label='Classical Bound (0)')
plt.axvline(np.pi, color='red', linestyle=':', label=r'$\phi_{max} = \pi$')

# Shade the violation region if it exists
if lb is not None:
    # Create an array for the region to fill
    phi_violation = np.linspace(lb, np.pi, 100)
    delta_violation = calculate_delta(phi_violation, k_value)
    plt.fill_between(phi_violation, 0, delta_violation, color='green', alpha=0.3, label='Violation Region')
    plt.text(lb + 0.1, max_delta_value/2, 'Violation', color='green')

plt.title(r'Quantum Violation $\delta(\phi)$ for N-Slit Experiment')
plt.xlabel(r'Phase $\phi$ (radians)')
plt.ylabel(r'Violation $\delta(\phi)$')
plt.legend()
plt.grid(True, alpha=0.5)
plt.xlim(0, 2*np.pi)
plt.ylim(min(delta_values)*1.1, max(delta_values)*1.1 + 0.1)

plt.show()
```
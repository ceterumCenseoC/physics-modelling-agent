```python
import numpy as np

def calculate_critical_J():
    """
    Calculates the critical coupling J for the n=3 Replicated Manifold model
    where the twist free energy y = 0.
    
    The model is solved by analytically summing over the bond variables (eta),
    which maps the system to an effective 4-state Potts model. The condition
    y=0 corresponds to the critical point of this Potts model.
    
    The critical condition is:
    cosh(3*J) / cosh(J) = 1 + sqrt(4)

    We solve this equation numerically using a binary search method to ensure
    the code is executable and calculates the result to the required precision.
    """
    
    # The objective function based on the criticality condition derived from the model.
    # We find the root of f(J) = (cosh(3J)/cosh(J)) - 3.
    def critical_condition(J):
        return (np.cosh(3.0 * J) / np.cosh(J)) - 3.0

    # Search boundaries for J.
    # From analysis, J is known to be in the range [0.6, 0.7].
    low = 0.6
    high = 0.7
    
    # Check if the root is bracketed
    if critical_condition(low) * critical_condition(high) > 0:
        print("Error: Root not bracketed in the initial interval [0.6, 0.7]")
        return None

    # Perform binary search to find the root
    # We aim for high precision to correctly round to 3 decimal places.
    tol = 1e-9
    J_estimate = 0.0
    
    while (high - low) > tol:
        mid = (low + high) / 2.0
        val = critical_condition(mid)
        
        if val > 0:
            # cosh(3J)/cosh(J) > 3, J is too large (monotonic function)
            high = mid
        else:
            # cosh(3J)/cosh(J) < 3, J is too small
            low = mid
            
    J_estimate = (low + high) / 2.0
    return J_estimate

if __name__ == "__main__":
    try:
        J_value = calculate_critical_J()
        if J_value is not None:
            # Print the result formatted to 3 decimal places as requested
            print(f"J = {J_value:.3f}")
        else:
            print("Calculation failed.")
    except Exception as e:
        print(f"An error occurred: {e}")
```
```python
import numpy as np
import matplotlib.pyplot as plt

def analytical_fidelity(p):
    """
    Calculates the logical state fidelity of the final 2-qubit logical state
    based on the derived formula.
    
    Args:
        p (float or np.ndarray): The two-qubit gate error rate (probability).
        
    Returns:
        float or np.ndarray: The logical state fidelity.
    """
    # The derived formula from the error analysis is: F = 1 - (2/15) * p
    # This accounts for the undetected logical errors X1X2 and Y1Y2 
    # occurring with probability p/15 each.
    return 1.0 - (2.0 * p / 15.0)

def main():
    """
    Main function to generate parameters, calculate fidelity, and plot results.
    """
    # Define parameters based on realistic hardware constraints
    # Starting parameter derived from state-of-the-art superconducting qubits
    p_start = 0.01
    
    # Range for parameter sweep: 0.1% (trapped ions) to 2% (noisy hardware)
    p_min = 0.001
    p_max = 0.02
    
    # Generate a range of values for plotting
    p_vals = np.linspace(p_min, p_max, 100)
    
    # Calculate fidelity across the range
    f_vals = analytical_fidelity(p_vals)
    
    # Calculate fidelity at the specific start parameter
    f_start = analytical_fidelity(p_start)

    # --- Plotting ---
    plt.figure(figsize=(10, 6))
    
    # Plot the fidelity function
    plt.plot(p_vals, f_vals, 'b-', linewidth=2, label=r'$F(p) = 1 - \frac{2p}{15}$')
    
    # Highlight the starting parameter point
    plt.plot(p_start, f_start, 'ro', markersize=8, 
             label=f'Start Parameter ($p={p_start:.3f}$)')
    
    # Formatting the plot
    plt.title("Logical State Fidelity vs. Two-Qubit Gate Error Rate")
    plt.xlabel("CNOT Error Rate ($p$)")
    plt.ylabel("Logical State Fidelity ($F$)")
    plt.grid(True, linestyle='--', alpha=0.7)
    
    # Set y-axis limits to focus on the relevant high-fidelity region
    plt.ylim(0.996, 1.0005)
    
    # Add legend
    plt.legend()
    
    # Annotate formula on the plot
    plt.annotate(r'$F = 1 - \frac{2p}{15}$', 
                 xy=(p_min + 0.001, 0.9995), 
                 xytext=(p_min + 0.002, 0.9998),
                 fontsize=14, 
                 bbox=dict(facecolor='white', alpha=0.8))

    # Save the plot to a file
    plt.savefig('logical_fidelity_plot.png')
    
    # Print results to console
    print(f"Plot generated: logical_fidelity_plot.png")
    print(f"Analytical fidelity at p={p_start}: {f_start:.12f}")

if __name__ == "__main__":
    main()
```
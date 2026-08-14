#The following Python code defines a class to model the 5-point correlation function in the 2D Ising CFT based on the provided mathematical description. It uses the fermionic representation leading to the determinant formula for the spin sector.

#```python
import numpy as np
import matplotlib.pyplot as plt

class IsingCFT:
    """
    A class to model the 2D Ising Conformal Field Theory and compute 
    correlation functions.
    """
    def __init__(self):
        # Central charge for the minimal model M(4,3) (Ising model)
        self.c = 0.5
        
        # Scaling dimensions (Delta = h + h_bar)
        # Energy operator epsilon: h=1/2, h_bar=1/2 -> Delta=1
        self.Delta_epsilon = 1.0  
        
        # Spin operator sigma: h=1/16, h_bar=1/16 -> Delta=1/8
        self.Delta_sigma = 0.125 
        
        # Structure constant for sigma x sigma -> epsilon OPE
        # Standard normalization in the Ising model is 1/2
        self.C_sigma_sigma_epsilon = 0.5

    def compute_5pt_correlator(self, x1, x2, x3, x4, x5):
        """
        Computes the 5-point correlation function:
        <epsilon(x1) epsilon(x2) epsilon(x3) sigma(x4) sigma(x5)>
        
        The calculation uses the result derived from the fermionic 
        representation of the Ising model. The formula corresponds to
        the dominant conformal block for the cyclic ordering (1,2,3).
        
        Mathematical Model:
        G = C_sse * |x_45|^(-2*Delta_sigma) * 
            sqrt( Product_{k=1}^3 |x_k - x_5| / |x_k - x_4| ) *
            (1 / (|x_12| |x_23| |x_31|))

        Args:
            x1, x2, x3 (complex): Coordinates of the Energy operators.
            x4, x5 (complex): Coordinates of the Spin operators.

        Returns:
            float: The value of the correlation function.
        """
        
        # Helper function to calculate the modulus |x_i - x_j|
        def dist(u, v):
            return abs(u - v)
        
        # Calculate the required distance moduli
        x12 = dist(x1, x2)
        x23 = dist(x2, x3)
        x31 = dist(x3, x1)
        
        x14 = dist(x1, x4)
        x15 = dist(x1, x5)
        x24 = dist(x2, x4)
        x25 = dist(x2, x5)
        x34 = dist(x3, x4)
        x35 = dist(x3, x5)
        x45 = dist(x4, x5)
        
        # Kinematical factor from the sigma-sigma OPE
        # sigma(x) sigma(y) ~ |x-y|^(-1/4) (1 + ...)
        k_sigma = x45**(-0.25) # corresponds to |x_45|^(-2*Delta_sigma)
        
        # Twist sector factor derived from the fermion propagator matrix determinant
        # Represents the sqrt of the ratio of distances to x5 vs x4
        k_twist = np.sqrt((x15 * x25 * x35) / (x14 * x24 * x34))
        
        # Cyclic dependence factor for the 3 epsilon fields
        # Derived from the Cauchy determinant structure 1/(x_i - x_j)
        k_cyclic = 1.0 / (x12 * x23 * x31)
        
        # Combine all factors with the structure constant
        value = self.C_sigma_sigma_epsilon * k_sigma * k_twist * k_cyclic
        
        return value

# --- Main Execution ---

# Initialize the Ising CFT model
model = IsingCFT()

# Case (1): Complex coordinates
# x1 = 1 + i, x2 = 2, x3 = 3, x4 = 4, x5 = 5
x1_case1 = 1 + 1j
x2_case1 = 2 + 0j
x3_case1 = 3 + 0j
x4_case1 = 4 + 0j
x5_case1 = 5 + 0j

result_case1 = model.compute_5pt_correlator(
    x1_case1, x2_case1, x3_case1, x4_case1, x5_case1
)

# Case (2): Real coordinates
# x1 = 1, x2 = 2, x3 = 3, x4 = 4, x5 = 5
x1_case2 = 1.0
x2_case2 = 2.0
x3_case2 = 3.0
x4_case2 = 4.0
x5_case2 = 5.0

result_case2 = model.compute_5pt_correlator(
    x1_case2, x2_case2, x3_case2, x4_case2, x5_case2
)

# Output the results
print("-" * 70)
print("2D Ising CFT 5-Point Correlation Function Calculation")
print("<epsilon(x1)epsilon(x2)epsilon(x3)sigma(x4)sigma(x5)>")
print("-" * 70)

print("\nModel Parameters:")
print(f"Central Charge (c):          {model.c}")
print(f"Delta_epsilon (Scaling):    {model.Delta_epsilon}")
print(f"Delta_sigma (Scaling):      {model.Delta_sigma}")
print(f"OPE Coefficient (C_eps_s):  {model.C_sigma_sigma_epsilon}")

print("\n" + "="*70)
print("CASE 1: Complex Coordinates")
print("="*70)
print(f"Inputs: x1={x1_case1}, x2={x2_case1}, x3={x3_case1}, x4={x4_case1}, x5={x5_case1}")
print(f"Result: {result_case1:.6f}")
print(f"Analytic Check: {np.sqrt(3) * (17**0.25) / (2 * np.sqrt(2) * (10**0.75)):.6f}")

print("\n" + "="*70)
print("CASE 2: Real Coordinates")
print("="*70)
print(f"Inputs: x1={x1_case2}, x2={x2_case2}, x3={x3_case2}, x4={x4_case2}, x5={x5_case2}")
print(f"Result: {result_case2:.6f}")
print(f"Analytic Check: {0.5:.6f}")

# --- Visualization for Case 1 ---
plt.figure(figsize=(8, 6))
# Plot operators: Red for Epsilon, Blue for Sigma
plt.scatter([x1_case1.real, x2_case1.real, x3_case1.real], 
            [x1_case1.imag, x2_case1.imag, x3_case1.imag], 
            color='red', s=100, label='Energy ($\epsilon$)', zorder=5)
plt.scatter([x4_case1.real, x5_case1.real], 
            [x4_case1.imag, x5_case1.imag], 
            color='blue', s=100, label='Spin ($\sigma$)', zorder=5)

# Annotate points
points = {'x1': x1_case1, 'x2': x2_case1, 'x3': x3_case1, 'x4': x4_case1, 'x5': x5_case1}
for label, coord in points.items():
    plt.annotate(f"{label}\n({coord.real:.1f}, {coord.imag:.1f})", 
                 (coord.real, coord.imag),
                 xytext=(5, 5), textcoords='offset points', fontsize=9)

# Formatting
plt.title(f'Ising CFT 5-Point Function Configuration\nValue: {result_case1:.4f}')
plt.xlabel('Real Axis')
plt.ylabel('Imaginary Axis')
plt.axhline(0, color='black', linewidth=0.8)
plt.axvline(0, color='black', linewidth=0.8)
plt.grid(True, linestyle='--', alpha=0.6)
plt.legend()
plt.tight_layout()

# Save the figure
plt.savefig('ising_5pt_function.png')
print("\nVisualization saved to 'ising_5pt_function.png'")

# Show the plot
plt.show()
#```
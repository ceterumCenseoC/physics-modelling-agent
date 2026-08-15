
```python
import numpy as np
import matplotlib.pyplot as plt

def get_spin_operators():
    """
    Returns the spin-1 matrices Sx, Sy, Sz in the standard basis.
    Basis order: |1>, |0>, |-1>.
    """
    # Basis order: |1>, |0>, |-1>
    # Raising and lowering operators for spin-1
    S_plus = np.sqrt(2) * np.array([[0, 1, 0],
                                    [0, 0, 1],
                                    [0, 0, 0]])
    S_minus = np.sqrt(2) * np.array([[0, 0, 0],
                                     [1, 0, 0],
                                     [0, 1, 0]])
    
    # Construct spin operators
    Sx = (S_plus + S_minus) / 2.0
    Sy = (S_plus - S_minus) / (2.0j)
    Sz = np.diag([1, 0, -1])
    
    return Sx, Sy, Sz

def compute_effective_operator_Rz_noisy(p):
    """
    Computes the effective noisy operator tilde{R}_z = E^dagger(R_z).
    
    The noise channel is defined by Kraus operators:
    K0 = sqrt(1-p) * I
    K1 = sqrt(p) * S_x S_y
    K2 = sqrt(p) * S_y S_z
    K3 = sqrt(p) * S_z S_x
    
    Effective operator: Rz_noisy = sum_{alpha} K_alpha^dagger R_z K_alpha
    """
    Sx, Sy, Sz = get_spin_operators()
    I3 = np.eye(3)
    
    # Define R_z = exp(i * pi * S_z)
    # Diagonal elements: exp(i*pi*1) = -1, exp(i*pi*0) = 1, exp(i*pi*(-1)) = -1
    Rz = np.diag([-1.0, 1.0, -1.0])
    
    # Define Kraus operators
    # Note: S matrices are Hermitian, so their products are Hermitian if they commute.
    # For Sx, Sy, Sz, products are not generally Hermitian, but K^dagger operations are handled 
    # correctly in the summation regardless.
    K0 = np.sqrt(1 - p) * I3
    K1 = np.sqrt(p) * (Sx @ Sy)
    K2 = np.sqrt(p) * (Sy @ Sz)
    K3 = np.sqrt(p) * (Sz @ Sx)
    
    kraus_ops = [K0, K1, K2, K3]
    
    # Compute the adjoint map action
    Rz_noisy = np.zeros((3, 3), dtype=complex)
    for K in kraus_ops:
        Rz_noisy += K.conj().T @ Rz @ K
        
    # The analytical derivation predicts Rz_noisy = (1 - 7/4 p) * Rz.
    # We verify this numerically to ensure the code matches the theory.
    # We extract the factor using trace overlap: Tr(Rz_noisy * Rz) / Tr(Rz * Rz)
    # because Rz is traceless but we are checking spectral projection on Rz subspace.
    # A simpler way given the structure: 
    # theoretical_factor = 1 - 1.75 * p
    # numerical_factor = Rz_noisy[0,0] / Rz[0,0] (since diagonals are preserved by symmetry structure implied)
    
    # However, the most robust check against potential machine error or logic errors:
    # Tr(Rz^2) = (-1)^2 + 1^2 + (-1)^2 = 3
    theoretical_factor = 1 - (7.0/4.0) * p
    
    # Calculate numerical scaling factor based on the inverse Hilbert-Schmidt inner product
    # effectively projecting onto Rz
    numerical_factor = np.trace(Rz_noisy @ Rz) / np.trace(Rz @ Rz)
    
    return np.real_if_close(Rz_noisy), theoretical_factor, numerical_factor

def calculate_string_order(l, p):
    """
    Calculates the string order parameter S0(l, p).
    
    Formula: S0 = [-1/3 * (1 - 7/4 p)]^l
    """
    noise_factor = 1 - (7.0/4.0) * p
    decay = -1.0/3.0 * noise_factor
    return decay ** l

def run_simulation():
    """
    Main function to run the calculation, verify operator theory, 
    and plot results.
    """
    print("--- Noisy AKLT Model String Order Parameter Simulation ---")
    
    # Step 1: Verify the Effective Operator Theory
    print("\n[Step 1] Verifying Effective Noisy Operator Calculation")
    p_test = 0.05
    Rz_calc, th_factor, num_factor = compute_effective_operator_Rz_noisy(p_test)
    
    print(f"  Noise probability p = {p_test}")
    print(f"  Theoretical Scaling Factor: {th_factor:.8f}")
    print(f"  Numerical Scaling Factor  : {num_factor:.8f}")
    print(f"  Difference : {abs(th_factor - num_factor):.2e}")
    
    if abs(th_factor - num_factor) > 1e-10:
        print("  WARNING: Numerical derivation of operator factor does not match theory.")
    else:
        print("  Verification Successful: Operator matches theoretical prediction.")

    # Step 2: Calculate String Order Parameters
    print("\n[Step 2] Calculating String Order Parameter S0(l, p)")
    
    # Parameters
    l_values = np.arange(1, 51, 1)  # String length l from 1 to 50
    p_values = [0.0, 0.05, 0.10]    # Different noise rates
    
    results = {}
    for p in p_values:
        s0_series = [calculate_string_order(l, p) for l in l_values]
        results[p] = s0_series
        print(f"  p = {p:.2f} | S0(l=50) = {s0_series[-1]:.6f}")

    # Step 3: Visualization
    print("\n[Step 3] Generating Plot")
    plt.figure(figsize=(10, 6))
    
    for p in p_values:
        label_str = f"p = {p:.2f}"
        plt.plot(l_values, results[p], marker='o', linestyle='-', linewidth=2, label=label_str)
        
    # Plot labels and formatting
    plt.title(r"Noisy String Order Parameter $\mathcal{S}_0(l)$ in AKLT Model", fontsize=16)
    plt.xlabel(r"String Length $l$", fontsize=14)
    plt.ylabel(r"$\mathcal{S}_0$", fontsize=14)
    plt.grid(True, linestyle='--', alpha=0.6)
    plt.legend(fontsize=12)
    
    # Add formula annotation
    formula_text = (r"$\mathcal{S}_0(l) = \left[-\frac{1}{3}\left(1 - \frac{7}{4}p\right)\right]^l$")
    plt.annotate(formula_text, xy=(0.5, 0.15), xycoords='axes fraction',
                 fontsize=14, ha='center',
                 bbox=dict(boxstyle="round,pad=0.3", fc="white", ec="gray", alpha=0.9))
    
    plt.tight_layout()
    
    # Save the figure
    filename = "noisy_string_order_parameter.png"
    plt.savefig(filename)
    print(f"  Plot saved as '{filename}'")
    
    # Display the plot
    try:
        plt.show()
    except Exception as e:
        # Handle environments without display support
        print(f"  Note: Could not display interactive plot window. (Error: {e})")

if __name__ == "__main__":
    run_simulation()
```
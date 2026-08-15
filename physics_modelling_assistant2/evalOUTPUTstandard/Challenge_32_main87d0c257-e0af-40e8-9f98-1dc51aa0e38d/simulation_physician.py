
# Python Code for Rayleigh-Darcy Convection

This code implements the mathematical model derived for Rayleigh-Darcy convection with mixed boundary conditions. It solves the linear stability eigenvalue problem to determine the critical Rayleigh number ($Ra_c$), the critical horizontal wavenumber ($k_c$), and the eigenfunction ratio $w(z)/T(z)$ at the specified height.

## Implementation Details

1.  **Problem Formulation**: The code solves the coupled ordinary differential equations (ODEs) for the vertical velocity $W(z)$ and temperature perturbation $\Theta(z)$ in the vertical direction, assuming horizontal wave-like perturbations with wavenumber $k$.
2.  **Boundary Conditions**:
    *   **Bottom ($z=0$)**: Impermeable ($W=0$) and Constant Heat Flux ($d\Theta/dz = 0$).
    *   **Top ($z=1$)**: Free/Impermeable ($W=0$) and Constant Temperature ($\Theta=0$).
3.  **Numerical Method**:
    *   The code uses `scipy.integrate.solve_bvp` to solve the boundary value problem (BVP).
    *   To find the critical parameters, a wrapper function calculates the smallest eigenvalue (effective Rayleigh number) for a given wavenumber $k$ by treating $Ra$ as an unknown parameter in the BVP.
    *   A minimization routine (`scipy.optimize.minimize_scalar`) sweeps through wavenumbers $k$ to find the critical wavenumber $k_c$ that minimizes the critical Rayleigh number $Ra_c$.

```python
import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_bvp
from scipy.optimize import minimize_scalar

def solve_rayleigh_darcy_mixed(k):
    """
    Solves the linear stability eigenvalue problem for Rayleigh-Darcy convection
    with mixed boundary conditions (isoflux bottom, isothermal top).
    
    Parameters:
    k (float): Horizontal wavenumber.
    
    Returns:
    float: The critical Rayleigh number for the given wavenumber k.
    tuple: (w_array, theta_array, z_mesh) normalized eigenfunctions and mesh.
    """
    
    def ode_system(z, y, p):
        """
        Defines the system of first-order ODEs.
        State vector y = [W, W', Theta, Theta', Ra]
        Note: Ra is treated as a parameter to be determined (eigenvalue).
        """
        W, Wp, Theta, Thetap, Ra = y
        
        # Equations:
        # Momentum: (D^2 - k^2)W = Ra * k^2 * Theta
        # Heat: (D^2 - k^2)Theta = W (assuming sigma=0 for marginal stability)
        
        # Rearranging for second derivatives:
        # W'' = (W + Ra * k^2 * Theta) -- WAIT, standard form is (D^2 - k^2)W ...
        # Correct: W'' - k^2*W = Ra * k^2 * Theta  => W'' = k^2*W + Ra*k^2*Theta
        
        # Correct: Theta'' - k^2*Theta = W       => Theta'' = k^2*Theta + W
        
        dWdz = Wp
        dWpdz = (k**2 * W) + (Ra * (k**2) * Theta)
        dThetadz = Thetap
        dThetapdz = (k**2 * Theta) + W
        dRadz = 0 # Ra is a parameter
        
        return np.vstack((dWdz, dWpdz, dThetadz, dThetapdz, dRadz))

    def bc(ya, yb, p):
        """
        Defines the boundary conditions.
        ya: values at z=0 (bottom)
        yb: values at z=1 (top)
        """
        W_a, Wp_a, Theta_a, Thetap_a, Ra_a = ya
        W_b, Wp_b, Theta_b, Thetap_b, Ra_b = yb
        
        # Boundary Conditions:
        # z=0 (Bottom): Impermeable (W=0), Constant Heat Flux (Theta'=0)
        # z=1 (Top): Free/Impermeable (W=0), Constant Temperature (Theta=0)
        
        return np.array([
            W_a,          # W(0) = 0
            Thetap_a,     # Theta'(0) = 0 (Isoflux)
            W_b,          # W(1) = 0
            Theta_b,      # Theta(1) = 0 (Isothermal)
            # Normalization condition to ensure non-trivial solution
            # We normalize the peaks. A robust way for the first mode is enforcing sign or max value.
            # Here we use a simple scalar normalization constraint.
            # Note: This constraint effectively determines the sign/magnitude of the eigenvector.
            yb[2] - 1.0  # Arbitrary normalization, adjusted for sign in post-processing
        ])

    # Define the mesh
    z_mesh = np.linspace(0, 1, 100)
    
    # Initial guess
    # sin(pi*z/2) roughly satisfies W(0)=0, W(1)!=0 (but we want W(1)=0) -> sin(pi*z)
    # Let's try shapes that satisfy BCs roughly.
    # Theta: cosh/cos shape. Theta(1)=0, Th'(0)=0. Looks like cos((n-0.5)pi*z).
    # W: sin shape.
    
    y_guess = np.zeros((5, z_mesh.size))
    y_guess[0] = np.sin(np.pi * z_mesh) # W guess
    y_guess[2] = np.cos(0.5 * np.pi * z_mesh) # Theta guess (approx shape)
    y_guess[4] = 30.0 # Ra guess (27.1 is expected)

    # Solve BVP
    # Use solve_bvp. Since Ra is an unknown parameter, we pass it via the `p` argument capability 
    # usually done by augmenting y vector, but scipy's solve_bvp handles parameters via a separate input `p`.
    # Here I augmented the state vector `y` to include Ra as the 5th element for simplicity in the `ode_system`.
    # However, standard solve_bvp usage separates parameters. Let's stick to the augmented vector approach 
    # effectively treating the 5th row as a constant parameter.
    # To make `solve_bvp` aware that the last component is a parameter, we simply don't differentiate it.
    
    sol = solve_bvp(ode_system, bc, z_mesh, y_guess)
    
    if not sol.success:
        print(f"Solver failed for k={k}: {sol.message}")
        return None, None, None

    # Extract Ra (it's the last row, should be constant)
    Ra_critical = sol.y[4, 0]
    
    # Normalize eigenfunctions for consistency
    # Let's normalize Theta such that max(|Theta|) = 1
    max_theta = np.max(np.abs(sol.y[2]))
    sol.y[0] /= max_theta
    sol.y[1] /= max_theta
    sol.y[2] /= max_theta
    sol.y[3] /= max_theta
    
    return Ra_critical, (sol.y[0], sol.y[2]), sol.x

def minimize_critical_Ra(k_bounds):
    """
    Finds the wavenumber k_c that minimizes the critical Rayleigh number.
    """
    
    def objective_Ra(k):
        Ra, _, _ = solve_rayleigh_darcy_mixed(k)
        if Ra is None:
            return 1e6 # Return large number if solve fails
        return Ra

    res = minimize_scalar(objective_Ra, bounds=k_bounds, method='bounded')
    return res

# --- Execution ---

print("Starting Linear Stability Analysis...")

# Perform minimization search
# We expect k_c around 2.3 based on the prompt context/derivation
result = minimize_critical_Ra((1.0, 5.0))

k_c_estimated = result.x
Ra_c_estimated = result.fun

print(f"\n--- Results ---")
print(f"Critical Rayleigh Number (Ra_c): {Ra_c_estimated:.5f}")
print(f"Critical Wavenumber (k_c): {k_c_estimated:.5f}")

# --- Extract Eigenfunctions at Critical Point ---
print(f"\nCalculating eigenfunctions at k_c = {k_c_estimated:.5f}...")
Ra_final, (W_final, Theta_final), z_final = solve_rayleigh_darcy_mixed(k_c_estimated)

# --- Compute Eigenfunction Ratio ---
z_target = 0.67365

# Interpolate W and Theta at z_target using the solution mesh
W_target = np.interp(z_target, z_final, W_final)
Theta_target = np.interp(z_target, z_final, Theta_final)

# Calculate ratio
# Note: Theta usually retains sign of perturbation. W/T ratio is specific.
if abs(Theta_target) < 1e-6:
    print("Warning: Theta is close to zero at target z.")
    ratio = 0
else:
    ratio = W_target / Theta_target

print(f"\n--- Eigenfunction Ratio ---")
print(f"z = {z_target}")
print(f"w(z) = {W_target:.5f}")
print(f"T(z) = {Theta_target:.5f}")
print(f"Ratio w(z)/T(z) = {ratio:.5f}")

# --- Graphics ---
plt.figure(figsize=(10, 6))

plt.subplot(1, 2, 1)
plt.plot(z_final, W_final, label='w(z)', linewidth=2)
plt.plot(z_final, Theta_final, label='T(z)', linewidth=2, linestyle='--')
plt.axhline(0, color='black', linewidth=0.5)
plt.axvline(z_target, color='red', linestyle=':', label=f'z = {z_target}')
plt.xlabel('Height z')
plt.ylabel('Amplitude')
plt.title(f'Critical Eigenfunctions (k_c={k_c_estimated:.2f}, Ra_c={Ra_c_estimated:.2f})')
plt.legend()
plt.grid(True, alpha=0.3)

plt.subplot(1, 2, 2)
# Plot the stability curve (Ra vs k) to visualize the minimum
k_range = np.linspace(1.5, 3.5, 20)
Ra_curve = []
for k_val in k_range:
    r, _, _ = solve_rayleigh_darcy_mixed(k_val)
    Ra_curve.append(r)

plt.plot(k_range, Ra_curve, 'o-', color='blue')
plt.plot(k_c_estimated, Ra_c_estimated, 'r*', markersize=15, label='Critical Point')
plt.xlabel('Horizontal Wavenumber k')
plt.ylabel('Critical Rayleigh Number Ra')
plt.title('Neutral Stability Curve')
plt.legend()
plt.grid(True, alpha=0.3)

plt.tight_layout()
plt.show()
```
```python
import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_bvp
from scipy.optimize import minimize_scalar

def solve_rayleigh_darcy_mixed(k, Ra_guess=30.0):
    """
    Solves the linear stability eigenvalue problem for Rayleigh-Darcy convection
    with mixed boundary conditions (isoflux bottom, isothermal top).
    
    Parameters:
    k (float): Horizontal wavenumber.
    Ra_guess (float): Initial guess for the Rayleigh number.
    
    Returns:
    float: The critical Rayleigh number for the given wavenumber k.
    tuple: (w_array, theta_array, z_mesh) normalized eigenfunctions and mesh.
              Returns (None, None, None) if solver fails.
    """
    
    def ode_system(z, y, p):
        """
        Defines the system of first-order ODEs.
        State vector y = [W, W', Theta, Theta']
        Parameter p = [Ra]
        """
        W, Wp, Theta, Thetap = y
        Ra = p[0]
        
        # Governing Equations (Linearized, Marginal Stability sigma=0):
        # Momentum: (D^2 - k^2)W = Ra * k^2 * Theta
        # Heat: (D^2 - k^2)Theta = W
        
        # Rearranging for derivatives:
        # W'' = k^2 * W + Ra * k^2 * Theta
        # Theta'' = k^2 * Theta + W
        
        dWdz = Wp
        dWpdz = (k**2 * W) + (Ra * (k**2) * Theta)
        dThetadz = Thetap
        dThetapdz = (k**2 * Theta) + W
        
        return np.vstack((dWdz, dWpdz, dThetadz, dThetapdz))

    def bc(ya, yb, p):
        """
        Defines the boundary conditions.
        ya: values at z=0 (bottom)
        yb: values at z=1 (top)
        p: parameters [Ra]
        """
        W_a, Wp_a, Theta_a, Thetap_a = ya
        W_b, Wp_b, Theta_b, Thetap_b = yb
        
        # Boundary Conditions:
        # z=0 (Bottom): Impermeable (W=0), Constant Heat Flux (Theta'=0)
        # z=1 (Top): Free/Impermeable (W=0), Constant Temperature (Theta=0)
        
        # Constraints on eigenfunction continuity are implicit in ODE definition
        # We need a normalization condition for the eigen problem
        # e.g., fix Theta at some point or integral of Theta^2 = 1. 
        # Here we fix Theta(mid) = 1 as a normalization constraint.
        
        return np.array([
            W_a,             # W(0) = 0
            Thetap_a,        # Theta'(0) = 0 (Isoflux)
            W_b,             # W(1) = 0
            Theta_b,         # Theta(1) = 0 (Isothermal)
            p[0]             # No constraint on Ra, it is unknown
        ])

    # Define the mesh
    z_mesh = np.linspace(0, 1, 100)
    
    # Initial guess for the solution y(z) and parameter p
    # Try shapes that satisfy BCs roughly.
    # Theta: 0 at top, 0 slope at bot. cos((n-0.5)pi*z) roughly matches.
    # W: 0 at both ends. sin(n*pi*z).
    
    y_guess = np.zeros((4, z_mesh.size))
    
    # Using n=1 mode approximations
    z_mid = 0.3 # approximate peak for Theta with mixed BCs
    y_guess[0] = np.sin(np.pi * z_mesh)            # W guess
    y_guess[2] = np.cos(1.5 * np.pi * z_mesh) # Theta guess (simulates isoflux/isothermal mix)
    y_guess[2] /= np.max(np.abs(y_guess[2]))       # Normalize guess
    
    # Initial guess for Ra
    p_guess = np.array([Ra_guess])

    # Solve BVP
    # Note: solve_bvp requires the number of boundary conditions to equal the size of y + size of p.
    # We have 4 ODEs (vector y) and 1 parameter (Ra).
    # We provided 4 BCs in bc(). 
    
    sol = solve_bvp(ode_system, bc, z_mesh, y_guess, p=p_guess, max_nodes=5000)
    
    if not sol.success:
        # print(f"Solver failed for k={k}: {sol.message}") # Optional: reduce verbosity
        return None, None, None

    # Extract Ra (it's the parameter p)
    Ra_critical = sol.p[0]
    
    # Normalize eigenfunctions for consistency/output
    # We normalize Theta such that max(|Theta|) = 1
    max_theta = np.max(np.abs(sol.y[2]))
    if max_theta > 0:
        sol.y[0] /= max_theta
        sol.y[1] /= max_theta
        sol.y[2] /= max_theta
        sol.y[3] /= max_theta
    
    return Ra_critical, (sol.y[0], sol.y[2]), sol.x

def find_critical_parameters():
    """
    Finds the wavenumber k_c that minimizes the critical Rayleigh number.
    Returns Ra_c, k_c.
    """
    
    def objective_Ra(k):
        # Use the result of the previous iteration to guess the next Ra for speed/stability
        # However, `minimize_scalar` doesn't easily carry state, so we use a fixed guess.
        Ra_val, _, _ = solve_rayleigh_darcy_mixed(k, Ra_guess=30.0)
        if Ra_val is None or np.isnan(Ra_val):
            return 1000.0 # Return large number if solve fails
        return Ra_val

    # Search bounds for k. Theoretical predictions say ~2.33.
    # We search between 1.0 and 5.0 to be safe.
    res = minimize_scalar(objective_Ra, bounds=(1.0, 5.0), method='bounded', options={'xatol': 0.01})
    
    return res.fun, res.x

# --- Execution ---

print("Starting Linear Stability Analysis for Mixed Boundary Conditions...")
print("Bottom: Impermeable, Isoflux | Top: Free, Isothermal")

# 1. Find Critical Parameters (Ra_c, k_c)
Ra_c_estimated, k_c_estimated = find_critical_parameters()

print(f"\n--- Critical Parameters ---")
print(f"Critical Rayleigh Number (Ra_c): {Ra_c_estimated:.5f}")
print(f"Critical Wavenumber (k_c):      {k_c_estimated:.5f}")

# Check if optimization failed
if Ra_c_estimated is None or Ra_c_estimated > 500:
    print("\nError: Failed to find a valid critical point.")
    exit()

# 2. Extract Eigenfunctions at Critical Point
# We resolve the BVP at the estimated k_c for high precision output
Ra_final, (W_final, Theta_final), z_final = solve_rayleigh_darcy_mixed(k_c_estimated, Ra_guess=Ra_c_estimated)

# 3. Compute Eigenfunction Ratio at specific height
z_target = 0.67365
W_target = np.interp(z_target, z_final, W_final)
Theta_target = np.interp(z_target, z_final, Theta_final)

if abs(Theta_target) < 1e-9:
    ratio_result = 0.0
else:
    ratio_result = W_target / Theta_target

print(f"\n--- Eigenfunction Analysis at z = {z_target} ---")
print(f"w(z) / T(z) = {ratio_result:.5f}")

# --- Graphics (Optional Visualization) ---
try:
    plt.figure(figsize=(10, 6))

    plt.subplot(1, 2, 1)
    plt.plot(z_final, W_final, label='w(z)', linewidth=2)
    plt.plot(z_final, Theta_final, label='T(z)', linewidth=2, linestyle='--')
    plt.axhline(0, color='black', linewidth=0.5)
    plt.axvline(z_target, color='red', linestyle=':', label=f'z = {z_target}')
    plt.xlabel('Height z')
    plt.ylabel('Amplitude')
    plt.title(f'Critical Eigenfunctions\n(k_c={k_c_estimated:.2f}, Ra_c={Ra_c_estimated:.2f})')
    plt.legend()
    plt.grid(True, alpha=0.3)

    plt.subplot(1, 2, 2)
    # Plot the stability curve (Ra vs k) to visualize the minimum
    k_range = np.linspace(1.5, 3.5, 25)
    Ra_curve = []
    for k_val in k_range:
        # Use Ra_c as guess to speed up curve generation
        r, _, _ = solve_rayleigh_darcy_mixed(k_val, Ra_guess=Ra_c_estimated)
        Ra_curve.append(r if r else np.nan)

    plt.plot(k_range, Ra_curve, 'o-', color='blue', label='Neutral Curve')
    plt.plot(k_c_estimated, Ra_c_estimated, 'r*', markersize=15, label=f'Critical Point\nRa={Ra_c_estimated:.1f}')
    plt.xlabel('Horizontal Wavenumber k')
    plt.ylabel('Critical Rayleigh Number Ra')
    plt.title('Neutral Stability Curve')
    plt.legend()
    plt.grid(True, alpha=0.3)

    plt.tight_layout()
    print("\nDisplaying plot...")
    plt.show()
except Exception as e:
    print(f"\nCould not generate plot (environment might not support display): {e}")
```
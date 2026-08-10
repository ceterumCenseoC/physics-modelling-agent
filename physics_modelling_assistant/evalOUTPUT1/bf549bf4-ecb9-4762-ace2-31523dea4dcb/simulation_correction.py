```python
import numpy as np
from scipy.linalg import eig
from scipy.optimize import minimize_scalar
import matplotlib.pyplot as plt

def solve_stability_problem(k, Ra, N=200):
    """
    Solves the discretized eigenvalue problem for the linear stability of 
    Rayleigh-Darcy convection.
    
    The governing equations in the marginal state (sigma = 0) are:
    (D^2 - k^2) * W + Ra * k^2 * T = 0
    (D^2 - k^2) * T - W = 0
    
    Boundary Conditions:
    z=0: W=0, dT/dz=0 (Impermeable, Constant Flux)
    z=1: W=0, T=0 (Free/Impermeable, Constant Temperature)
    
    Note: A free boundary in Darcy flow is often treated as W=0 (no penetration).
    The condition is W(0)=0, W(1)=0.
    
    Args:
        k (float): Horizontal wavenumber.
        Ra (float): Rayleigh number.
        N (int): Number of grid points.
        
    Returns:
        eigenvalues (array): Eigenvalues of the system.
        eigenvectors (array): Eigenvectors of the system.
        z (array): Grid coordinates.
    """
    # Grid generation
    z = np.linspace(0, 1, N)
    dz = z[1] - z[0]
    
    # Initialize matrices for the generalized eigenvalue problem A * x = lambda * B * x
    # However, for marginal stability sigma=0, we have a determinantal condition or 
    # we can look for the null space of the steady operator.
    # Here we solve the coupled linear system directly for W, T to see if non-trivial
    # solutions exist. If the determinant is zero (or close to zero), it's a critical state.
    
    # Let y = [W, T]. Dimension is 2N.
    # Matrix size: 2N x 2N
    dim = 2 * N
    A = np.zeros((dim, dim))
    
    # Second derivative operator (central difference)
    # d2f/dz2 approx (f_{i+1} - 2f_i + f_{i-1}) / dz^2
    # We handle boundaries by replacing rows with BC equations.
    
    # Coefficients for finite difference
    c_main = -2.0 / dz**2
    c_neigh = 1.0 / dz**2
    
    # Interior points (1 to N-2)
    # Eq 1: (D^2 - k^2)W + Ra*k^2*T = 0
    for i in range(1, N-1):
        A[i, i-1] = c_neigh             # d2W/dz2 term
        A[i, i]   = c_main - k**2       # d2W/dz2 term - k^2 W
        A[i, i+1] = c_neigh             # d2W/dz2 term
        A[i, N+i] = Ra * k**2           # Ra*k^2 T
        
    # Eq 2: (D^2 - k^2)T - W = 0
    for i in range(1, N-1):
        A[N+i, i] = -1.0                # -W
        A[N+i, N+i-1] = c_neigh         # d2T/dz2 term
        A[N+i, N+i]   = c_main - k**2   # d2T/dz2 term - k^2 T
        A[N+i, N+i+1] = c_neigh         # d2T/dz2 term

    # Boundary Conditions
    # z=0 (index 0):
    # W(0)=0 -> Row 0: W_0 = 1.0 * W_0
    A[0, 0] = 1.0
    
    # dT/dz = 0 -> (T_1 - T_-1)/(2dz) = 0 => T_-1 = T_1
    # Insert into Eq 2 at i=0:
    # (T_1 - 2T_0 + T_-1)/dz^2 - k^2 T_0 - W_0 = 0
    # (2T_1 - 2T_0)/dz^2 - k^2 T_0 = 0
    A[N, 0] = -1.0 # -W_0 (since W_0=0, this term doesn't affect, but good for form)
    A[N, N] = (2*c_main) - k**2 # c_main is -2/dz^2, so 2*c_main = -4/dz^2
    A[N, N+1] = 2*c_neigh
    
    # z=1 (index N-1):
    # W(1)=0 -> Row N-1: W_{N-1} = 1.0 * W_{N-1}
    A[N-1, N-1] = 1.0
    
    # T(1)=0 -> Row 2N-1: T_{N-1} = 1.0 * T_{N-1}
    A[2*N-1, 2*N-1] = 1.0

    # We are looking for the existence of non-trivial solutions.
    # This happens when det(A) is minimum (zero for critical Ra).
    # Since we are solving for Ra given k (or finding k that minimizes Ra),
    # we check the singularity or invertibility.
    # A robust way: Find the smallest singular value. If it is close to 0, we are at criticality.
    
    s = np.linalg.svd(A, compute_uv=False)
    min_singular_value = s[-1]
    
    return min_singular_value

def find_marginally_stable_Ra(k):
    """
    Finds the Rayleigh number Ra for which the system is marginally stable
    (smallest singular value of the system matrix is minimized) for a given k.
    """
    # Optimization objective: Minimize the smallest singular value
    def objective(Ra):
        return solve_stability_problem(k, Ra)
    
    # Search for Ra. For porous media, Ra is usually positive and ranges from 0 to ~1000+.
    # Literature suggests Ra_c ~ 40.
    res = minimize_scalar(objective, bounds=(0.1, 200.0), method='bounded', options={'xatol': 1e-4})
    return res.x, res.fun

# 1. Find critical Ra and critical k
# We scan k to find the Ra that allows for the "most" instability (minimum Ra over k)
k_values = np.linspace(2.0, 5.0, 50) 
Ra_values = []
sv_values = []

print("Calculating Neutral Stability Curve...")
for k in k_values:
    # For each k, find Ra that makes the system singular (minimize SV)
    Ra_min, sv_min = find_marginally_stable_Ra(k)
    Ra_values.append(Ra_min)
    sv_values.append(sv_min)

# Find the global minimum of Ra on the calculated curve
idx_opt = np.argmin(Ra_values)
k_c_approx = k_values[idx_opt]
Ra_c_approx = Ra_values[idx_opt]

# Refine search around the approximate minimum
def min_Ra_over_k(k):
    Ra, _ = find_marginally_stable_Ra(k)
    return Ra

print("\nRefining search for critical wavenumber k_c...")
res_opt = minimize_scalar(min_Ra_over_k, bounds=(2.5, 4.0), method='bounded', options={'xatol': 1e-5})
k_c = res_opt.x
Ra_c = res_opt.fun

print(f"\nCritical Values Found:")
print(f"Critical Wavenumber (k_c): {k_c:.5f} (Expected ~3.14159)")
print(f"Critical Rayleigh Number (Ra_c): {Ra_c:.5f} (Expected ~39.47842)")

# 2. Calculate Eigenfunction Ratio at z = 0.67365
# To get the eigenfunctions, we need the null space of A(Ra_c, k_c).
# Since A is numerically singular, we use SVD to find the eigenvector corresponding to the smallest singular value.
# We construct the matrix A again with high resolution specifically at (Ra_c, k_c).
N_eig = 400
z_eig = np.linspace(0, 1, N_eig)
dz_eig = z_eig[1] - z_eig[0]
dim_eig = 2 * N_eig
A_crit = np.zeros((dim_eig, dim_eig))

# Re-construct matrix A for high res (copying logic from solve_stability_problem)
c_main = -2.0 / dz_eig**2
c_neigh = 1.0 / dz_eig**2

# Interior Points
for i in range(1, N_eig-1):
    # Eq 1
    A_crit[i, i-1] = c_neigh
    A_crit[i, i]   = c_main - k_c**2
    A_crit[i, i+1] = c_neigh
    A_crit[i, N_eig+i] = Ra_c * k_c**2
    
    # Eq 2
    A_crit[N_eig+i, i] = -1.0
    A_crit[N_eig+i, N_eig+i-1] = c_neigh
    A_crit[N_eig+i, N_eig+i]   = c_main - k_c**2
    A_crit[N_eig+i, N_eig+i+1] = c_neigh

# Boundary Conditions
# z=0
A_crit[0, 0] = 1.0
A_crit[N_eig, 0] = -1.0
A_crit[N_eig, N_eig] = (2*c_main) - k_c**2
A_crit[N_eig, N_eig+1] = 2*c_neigh

# z=1
A_crit[N_eig-1, N_eig-1] = 1.0
A_crit[2*N_eig-1, 2*N_eig-1] = 1.0

# Find null space vector using SVD
U, s, Vh = np.linalg.svd(A_crit)
# The singular vector corresponding to the smallest singular value is the last row of Vh (or col of V)
eigenfunction = Vh[-1, :]

W_eig = eigenfunction[:N_eig]
T_eig = eigenfunction[N_eig:]

# Find index of z = 0.67365
target_z = 0.67365
idx_z = np.abs(z_eig - target_z).argmin()
ratio = W_eig[idx_z] / T_eig[idx_z]

# Check normalization/sign. The ratio is what matters.
# The ratio can vary depending on the sign of the eigenvector (direction), but the value should be consistent.
print(f"\nEigenfunction Analysis at z = {target_z}:")
print(f"w(z)/T(z) = {ratio:.5f}")

# 3. Graphics
plt.figure(figsize=(10, 6))

# Plot Neutral Stability Curve
plt.subplot(1, 2, 1)
plt.plot(k_values, Ra_values, 'b-', label='Neutral Curve')
plt.plot(k_c, Ra_c, 'ro', label=f'Critical Point ($k_c \\approx {k_c:.2f}, Ra_c \\approx {Ra_c:.2f}$)')
plt.xlabel('Wavenumber $k$')
plt.ylabel('Rayleigh Number $Ra$')
plt.title('Neutral Stability Curve')
plt.legend()
plt.grid(True)

# Plot Eigenfunctions
plt.subplot(1, 2, 2)
plt.plot(z_eig, W_eig, 'r-', label='Vertical Velocity $W(z)$')
plt.plot(z_eig, T_eig, 'b--', label='Temperature $\\Theta(z)$')
plt.axvline(target_z, color='k', linestyle=':', alpha=0.5, label=f'z = {target_z}')
plt.xlabel('Height $z$')
plt.ylabel('Amplitude (Normalized)')
plt.title('Critical Eigenfunctions')
plt.legend()
plt.grid(True)

plt.tight_layout()
plt.show()
```
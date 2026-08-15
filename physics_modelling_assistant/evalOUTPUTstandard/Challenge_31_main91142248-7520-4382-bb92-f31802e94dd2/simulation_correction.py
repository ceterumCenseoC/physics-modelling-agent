```python
import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import minimize_scalar, root_scalar
from scipy.linalg import det, svd

# ==========================================
# 1. Mathematical Setup and Constants
# ==========================================

# The Prandtl number is fixed at 1 according to the problem statement.
Pr = 1.0

# Tolerance for numerical root finding.
tol = 1e-6

def compute_determinant(Ra, k):
    """
    Computes the determinant of the boundary condition matrix for the
    linear stability eigenproblem.
    
    The governing ODE for marginal stability (sigma=0) is:
    (D^2 - k^2)^3 w + k^2 * Ra * w = 0
    
    The characteristic equation for lambda is derived from:
    (lambda^2 - k^2)^3 = -k^2 * Ra
    
    We solve for the 6 roots and construct a basis of solutions.
    Applying the 6 boundary conditions (3 at z=0, 3 at z=1) yields
    a 6x6 linear system M * c = 0.
    A non-trivial solution exists if det(M) = 0.
    """
    
    # 1. Calculate the roots of the characteristic equation.
    # Let a = lambda^2. The equation is (a - k^2)^3 = -C, where C = k^2*Ra.
    # The roots a_i are evenly spaced on a circle in the complex plane
    # centered at k^2 with radius (k^2*Ra)^(1/3).
    
    C = k**2 * Ra
    radius = C**(1.0/3.0)
    
    # Center of the circle for a_i
    center = k**2 
    
    # The three roots for a = lambda^2:
    # a1: Real root. at angle pi (because of -C)
    a1 = center - radius
    
    # a2, a3: Complex conjugate pair at angles +/- pi/3
    # a2 = r*e^(i*pi/3) = r(0.5 + i*sqrt(3)/2)
    # a3 = r*e^(-i*pi/3) = r(0.5 - i*sqrt(3)/2)
    # Relative to 'center':
    a2 = center + radius * complex(0.5, np.sqrt(3)/2)
    a3 = center + radius * complex(0.5, -np.sqrt(3)/2)
    
    # Calculate lambda = sqrt(a).
    # We have lambda = +/- l1, +/- l2, +/- l3
    l1 = np.sqrt(a1) # Guaranteed real for Ra>0
    l2 = np.sqrt(a2) # Complex
    l3 = np.conj(l2) # Conjugate of l2
    
    # 2. Define the Basis Functions.
    # We need 6 linearly independent real functions.
    # From the real roots (+/- l1): sin(l1*z), sinh(l1*z) ? 
    # Standard form: exp(l1*z), exp(-l1*z). Converted to cosh/sinh or just kept as exp.
    # Since l1 is real, we use sinh(l1*z) and cosh(l1*z).
    # However, for the complex roots, we use real and imaginary parts
    # of exp(l2*z) and exp(l3*z) to ensure real arithmetic in the matrix construction
    # (mostly for stability, though numpy handles complex).
    
    # Let's define helper functions to evaluate basis and derivatives at z.
    
    u = np.real(l2)
    v = np.imag(l2)
    
    def get_basis(z):
        # Returns vector of 6 basis functions [f1...f6]
        # f1: exp(l1 * z)
        # f2: exp(-l1 * z)
        # For complex roots l2 = u + iv, l3 = u - iv:
        # We form a real basis: exp(u*z)*cos(v*z), exp(u*z)*sin(v*z), exp(-u*z)*cos(v*z), exp(-u*z)*sin(v*z)
        
        f1 = np.exp(l1 * z)
        f2 = np.exp(-l1 * z)
        
        f3 = np.exp(u * z) * np.cos(v * z)
        f4 = np.exp(u * z) * np.sin(v * z)
        f5 = np.exp(-u * z) * np.cos(v * z)
        f6 = np.exp(-u * z) * np.sin(v * z)
        
        return np.array([f1, f2, f3, f4, f5, f6])

    def get_deriv(z, order):
        # Evaluates derivatives of the basis functions.
        # d/dz (exp(lz)) = l * exp(lz)
        # This can be done manually for efficiency.
        
        # Derivatives of f1, f2 are trivial
        # Derivatives of f3..f6 require product rules.
        
        # Precompute common terms
        # f3 = e^(uz) cos(vz) -> Re(e^(l2 z))
        # D(f3) = u f3 - v f4
        # D^2(f3) = u^2 f3 - uv f4 - (uv f3 + v^2 f4) ? No.
        # D^2(Re(e^(l2z))) = Re(l2^2 e^(l2z)).
        # l2^2 = (u^2 - v^2) + i(2uv).
        
        # Generally, D^n (Re(e^(l2 z))) = Re( l2^n e^(l2 z) )
        # Same for Im part.
        
        if order == 0:
            return get_basis(z)
        
        # Coeffs for derivatives of exp terms
        # For f1, f2:
        c1_e = l1**order
        c2_e = (-l1)**order
        
        # For complex pair l2:
        # l2^order
        pow_l2 = l2**order
        coeff_re = np.real(pow_l2)
        coeff_im = np.imag(pow_l2)
        
        # f3..f6 correspond to Re(e^(l2z)), Im(e^(l2z)), Re(e^(l3z)), Im(e^(l3z))
        # Note: Re(e^(l3z)) = Re(e^(conj(l2)z)) = Re(conj(e^(l2z))) = Re(e^(l2z)) (same form)
        # f5(z) = exp(-uz)cos(vz). D(f5) = Re(-l2 e^(l2 z) evaluated at conjugate... easier to just use u,v.
        
        if order == 1:
            d1 = l1 * f1 = c1_e * get_basis(z)[0]
            d2 = -l1 * f2 = c2_e * get_basis(z)[1]
            d3 = u * get_basis(z)[2] - v * get_basis(z)[3]
            d4 = u * get_basis(z)[3] + v * get_basis(z)[2]
            d5 = -u * get_basis(z)[4] - v * get_basis(z)[5]
            d6 = -u * get_basis(z)[5] + v * get_basis(z)[4]
            return np.array([d1, d2, d3, d4, d5, d6])
            
        elif order == 2:
            d1 = l1**2 * get_basis(z)[0]
            d2 = l1**2 * get_basis(z)[1]
            # l2^2 = (u^2 - v^2) + i(2uv)
            A = u**2 - v**2
            B = 2*u*v
            d3 = A * get_basis(z)[2] - B * get_basis(z)[3]
            d4 = A * get_basis(z)[3] + B * get_basis(z)[2]
            # l3^2 = conj(l2^2). Derivative of exp(-uz)... is passed through -l2 basically.
            # D^2(exp(-uz cos)) involves (-u-iv)^2 = (u+iv)^2 = conj(l2^2) = A - iB
            d5 = A * get_basis(z)[4] + B * get_basis(z)[5]
            d6 = A * get_basis(z)[5] - B * get_basis(z)[4]
            return np.array([d1, d2, d3, d4, d5, d6])

        elif order == 4:
            # D^4 of exp(lz) is l^4 exp(lz).
            d1 = l1**4 * get_basis(z)[0]
            d2 = l1**4 * get_basis(z)[1]
            
            l2_sq = l2**2 # A + iB
            l2_cu = l2_sq * l2
            l2_qu = l2_sq * l2_sq
            # Re(l2^4), Im(l2^4)
            Re4 = np.real(l2_qu)
            Im4 = np.imag(l2_qu)
            
            d3 = Re4 * get_basis(z)[2] - Im4 * get_basis(z)[3]
            d4 = Re4 * get_basis(z)[3] + Im4 * get_basis(z)[2]
            # For conj(l2)^4 = Re4 - iIm4
            d5 = Re4 * get_basis(z)[4] + Im4 * get_basis(z)[5]
            d6 = Re4 * get_basis(z)[5] - Im4 * get_basis(z)[4]
            return np.array([d1, d2, d3, d4, d5, d6])

    # 3. Build the Matrix M using boundary conditions
    
    # BCs at z = 0 (Bottom: No-slip, Constant Heat Flux)
    # w = 0
    # w' = 0
    # (D^2 - k^2)^2 w = 0  => D^4 w - 2k^2 D^2 w + k^4 w = 0
    
    B0 = get_basis(0)
    D1_0 = get_deriv(0, 1)
    D2_0 = get_deriv(0, 2)
    D4_0 = get_deriv(0, 4)
    
    row1 = B0
    row2 = D1_0
    row3 = D4_0 - 2*k**2 * D2_0 + k**4 * B0
    
    # BCs at z = 1 (Top: Free-slip, Fixed Temperature)
    # w = 0
    # w'' = 0
    # (D^2 - k^2)^2 w = 0 (Same operator form, different application)
    
    B1 = get_basis(1)
    D2_1 = get_deriv(1, 2)
    D4_1 = get_deriv(1, 4)
    
    row4 = B1
    row5 = D2_1
    row6 = D4_1 - 2*k**2 * D2_1 + k**4 * B1
    
    M = np.vstack((row1, row2, row3, row4, row5, row6))
    
    # Return absolute value of real part of determinant
    return np.abs(np.real(det(M)))

# ==========================================
# 2. Solver for Critical Thresholds
# ==========================================

def find_critical_Ra(k_target):
    """
    Finds the Rayleigh number Ra that produces a zero determinant
    for the given wavenumber k.
    This corresponds to the marginal stability threshold Ra(k).
    """
    
    # We expect Ra to be roughly in the range [500, 2000] for mixed boundaries.
    # Rigid/Rigid is 1708. Free/Free is 657. Flux/Free is even lower.
    # We search for the first positive root.
    
    # Define function to minimize (squared determinant)
    func = lambda r: compute_determinant(r, k_target)**2
    
    # Use a minimizer. Determinant usually has a clear minimum near 0.
    # Bracket the solution.
    
    # Scan to find good bracket or starting point
    Rs = np.linspace(100, 3000, 200)
    vals = [func(r) for r in Rs]
    min_idx = np.argmin(vals)
    Ra_guess = Rs[min_idx]
    
    # Refine
    # Note: Sometimes the determinant is monotonic and we look for sign change,
    # but minimization of |det| is robust for this problem as the root is simple.
    res = minimize_scalar(func, bracket=(max(100, Ra_guess-500), min(4000, Ra_guess+500)), method='brent', options={'xtol': 1e-4})
    
    return res.x

# ==========================================
# 3. Main Execution Logic
# ==========================================

print("Performing Linear Stability Analysis for Mixed Boundary Conditions")
print("Bottom: No-Slip, Constant Heat Flux")
print("Top:    Free-Slip, Fixed Temperature")
print("-" * 60)

# Scan range for wavenumber k
# Mixed BCs usually have wavenumbers around 2.0 - 3.0
k_scan = np.linspace(2.0, 3.5, 30)
Ra_results = []

print("Step 1: Solving eigenvalue problem for range of k values...")
for k in k_scan:
    Ra_k = find_critical_Ra(k)
    Ra_results.append(Ra_k)
    # print(f"k = {k:.3f}, Ra = {Ra_k:.2f}")

Ra_results = np.array(Ra_results)

# Find global minimum Ra_c
min_idx = np.argmin(Ra_results)
k_c_estimate = k_scan[min_idx]
Ra_c_estimate = Ra_results[min_idx]

print("Step 2: Refining the critical point using local minimization...")

# A function that returns Ra for a given k by calling the eigenvalue solver
def get_Ra_k(k):
    return find_critical_Ra(k)

# We minimize get_Ra_k over k.
# Since get_Ra_k involves nested optimization, this is computationally intensive.
# We use the rough estimate from the scan to provide a tight bracket.
final_res = minimize_scalar(get_Ra_k, bracket=(k_scan[min_idx-1], k_scan[min_idx+1]), method='brent', options={'xtol': 1e-4})

k_c = final_res.x
Ra_c = final_res.fun

print("-" * 60)
print(f"CRITICAL PARAMETERS:")
print(f"Critical Rayleigh Number (Ra_c): {Ra_c:.2f}")
print(f"Critical Wavenumber (k_c):       {k_c:.4f}")
print("-" * 60)

# Verification of error tolerance
# The prompt allows error: Ra (+/- 0.5), k (+/- 0.02)
# The numerical precision of brent's method is usually sufficient.

# ==========================================
# 4. Visualization
# ==========================================

# Plot the Neutral Stability Curve Ra(k)
plt.figure(figsize=(10, 6))
plt.plot(k_scan, Ra_results, 'k-o', label='Neutral Curve (Numerical)')
plt.plot(k_c, Ra_c, 'r*', markersize=15, label=f'Critical Point\n($k_c={k_c:.3f}, Ra_c={Ra_c:.1f}$)')
plt.xlabel('Horizontal Wavenumber $k$')
plt.ylabel('Rayleigh Number $Ra$')
plt.title('Neutral Stability Curve for Mixed Boundary Conditions')
plt.grid(True, which='both', linestyle='--')
plt.legend()
plt.show()

# ==========================================
# 5. Eigenmode Visualization
# ==========================================

# To visualize the mode, we need the eigenvector corresponding to (Ra_c, k_c)
# We can extract this from the SVD of the matrix M at the critical point.

print("Visualizing critical eigenmode structure...")

# Extract lambda roots
C = k_c**2 * Ra_c
radius = C**(1.0/3.0)
center = k_c**2
l1 = np.sqrt(center - radius)
l2 = np.sqrt(center + radius * complex(0.5, np.sqrt(3)/2))
u = np.real(l2)
v = np.imag(l2)

# Re-define basis functions locally for plotting
def basis_func(z):
    b1 = np.exp(l1*z)
    b2 = np.exp(-l1*z)
    b3 = np.exp(u*z) * np.cos(v*z)
    b4 = np.exp(u*z) * np.sin(v*z)
    b5 = np.exp(-u*z) * np.cos(v*z)
    b6 = np.exp(-u*z) * np.sin(v*z)
    return np.array([b1, b2, b3, b4, b5, b6])

def basis_deriv(z, n):
    # nth derivative
    d1 = l1**n * basis_func(z)[0]
    d2 = (-l1)**n * basis_func(z)[1]
    ln_pow = l2**n
    c_re = np.real(ln_pow)
    c_im = np.imag(ln_pow)
    d3 = c_re * basis_func(z)[2] - c_im * basis_func(z)[3]
    d4 = c_re * basis_func(z)[3] + c_im * basis_func(z)[2]
    d5 = c_re * basis_func(z)[4] + c_im * basis_func(z)[5]
    d6 = c_re * basis_func(z)[5] - c_im * basis_func(z)[4]
    return np.array([d1, d2, d3, d4, d5, d6])

# Construct M at (Ra_c, k_c)
B0 = basis_func(0)
D1_0 = basis_deriv(0, 1)
D2_0 = basis_deriv(0, 2)
D4_0 = basis_deriv(0, 4)
r1 = B0
r2 = D1_0
r3 = D4_0 - 2*k_c**2 * D2_0 + k_c**4 * B0

B1 = basis_func(1)
D2_1 = basis_deriv(1, 2)
D4_1 = basis_deriv(1, 4)
r4 = B1
r5 = D2_1
r6 = D4_1 - 2*k_c**2 * D2_1 + k_c**4 * B1

M_crit = np.vstack((r1, r2, r3, r4, r5, r6))

# Find null space vector
U, s, Vh = svd(M_crit)
coeffs = Vh[-1] # Vector corresponding to smallest singular value
# Normalize
coeffs = coeffs / np.max(np.abs(coeffs))

# Calculate w(z) profile
z_vals = np.linspace(0, 1, 200)
w_profile = np.zeros(len(z_vals), dtype=complex)

for i, z in enumerate(z_vals):
    bvec = basis_func(z)
    w_profile[i] = np.dot(coeffs, bvec)

plt.figure(figsize=(8, 5))
plt.plot(z_vals, np.real(w_profile), 'b-', linewidth=2)
plt.axhline(0, color='k', linestyle='--')
plt.xlabel('Height $z$ (0 = Bottom, 1 = Top)')
plt.ylabel('Vertical Velocity Perturbation $w(z)$')
plt.title(f'Critical Eigenmode ($k_c={k_c:.2f}, Ra_c={Ra_c:.0f}$)')
plt.grid(True)
plt.show()

print("Done.")
```
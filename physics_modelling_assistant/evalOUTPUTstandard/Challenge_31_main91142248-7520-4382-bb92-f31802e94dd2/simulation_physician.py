
```python
import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import root_scalar, minimize_scalar
from scipy.linalg import det

# ==========================================
# 1. Physical and Mathematical Constants
# ==========================================

# The problem specifies Pr = 1
Pr = 1.0

# Tolerance for root finding
tol = 1e-6

# ==========================================
# 2. Model Definition
# ==========================================

def solve_eigenvalue_problem(Ra, k):
    """
    Solves the characteristic equation for the vertical velocity w(z)
    and applies boundary conditions to return the determinant of the
    coefficient matrix. 
    
    The governing ODE for marginal stability is:
    (D^2 - k^2)^3 w + k^2 * Ra * w = 0
    
    Characteristic eq for lambda: (lambda^2 - k^2)^3 = - k^2 * Ra
    Let s^2 = lambda^2.
    Roots s^2 = k^2 + beta_i
    where beta_i are the cube roots of (-k^2 * Ra).
    """
    
    # 1. Find the roots of the characteristic equation: s^6 - 3k^2 s^4 + 3k^4 s^2 - k^6 + k^2 Ra = 0
    # This is a cubic in s^2. Let a = s^2.
    # (a - k^2)^3 + k^2 Ra = 0  => (a - k^2)^3 = -k^2 Ra
    
    # The roots of (a - k^2)^3 = C are evenly spaced on a circle of radius |C|^(1/3)
    # C = -k^2 * Ra.
    # Roots for a:
    # a = k^2 + (k^2 Ra)^(1/3) * root_unity
    # Specifically, let rho = (k^2 * Ra)^(1/3). The roots are -rho, rho/2 +/- i*rho*sqrt(3)/2
    
    rho = (k**2 * Ra)**(1.0/3.0)
    
    # The three values for a = s^2
    a1 = k**2 - rho                      # Real root part
    a2 = k**2 + rho * 0.5                # Complex root part (real component)
    a3 = k**2 + rho * 0.5 * (-1)         # Same real component
    
    # Note: The roots of the characteristic polynomial for lambda are +/- sqrt(a).
    # We have 6 lambdas:
    # +/- sqrt(a1), +/- sqrt(a2), +/- sqrt(a3)
    # Since a2 and a3 are complex conjugates, sqrt(a2) and sqrt(a3) are complex conjugates.

    # 2. Construct general solution w(z) = sum c_j * f_j(z)
    # Functions f_j(z): sin(lambda*z), cos(lambda*z), sinh(lambda*z), cosh(lambda*z)
    # We need a real basis.
    # Let l1 = sqrt(a1) (real if a1 > 0)
    # Let l2 = sqrt(a2) = u + iv
    # Let l3 = sqrt(a3) = u - iv
    
    l1 = np.sqrt(a1)
    l2 = np.sqrt(a2 + 0j)
    l3 = np.conj(l2)
    
    # Real basis functions derived from complex exponentials:
    # z1 = exp(l1 z), z2 = exp(-l1 z) -> sin/cosh
    # z3 = exp(l2 z), z4 = exp(-l2 z), z5 = exp(l3 z), z6 = exp(-l3 z)
    # This forms a 6x6 linear system for the coefficients of the basis functions.
    
    # Boundary Conditions:
    # z = 0 (Bottom, No-slip, Fixed Heat Flux)
    # w = 0
    # w' = 0
    # (D^2 - k^2)^2 w = 0  (Derived from theta' = 0)
    
    # z = 1 (Top, Free-slip, Fixed Temp)
    # w = 0
    # w'' = 0
    # (D^2 - k^2)^2 w = 0 (Derived from theta = 0, note: T_pert = 0 implies (D^2 - k^2)^2 w = 0)
    
    # We evaluate the linear system A * C = 0.
    # Non-trivial solution exists if det(A) = 0.
    
    def get_basis_funcs(z):
        # Helper to evaluate functions and derivatives at z
        # Basis vector F = [f1, f2, f3, f4, f5, f6]
        # We choose a basis that handles complex roots efficiently to ensure real result.
        # 1. Hyperbolic Sine/Cosine for real root l1: cosh(l1*z), sinh(l1*z)
        # 2. For complex pair l2, l3:
        #    Real parts of exp(l2*z) and exp(l3*z)
        #    F_re = exp(u*z) * cos(v*z)
        #    F_im = exp(u*z) * sin(v*z)
        #    And their counterparts for exp(-l*z)
        
        u = np.real(l2)
        v = np.imag(l2)
        
        # Basis functions
        f1 = np.cosh(l1*z)
        f2 = np.sinh(l1*z)
        
        f3 = np.exp(u*z) * np.cos(v*z)
        f4 = np.exp(u*z) * np.sin(v*z)
        f5 = np.exp(-u*z) * np.cos(v*z)
        f6 = np.exp(-u*z) * np.sin(v*z)
        
        return np.array([f1, f2, f3, f4, f5, f6])

    def get_basis_derivs(z, order):
        # Evaluate derivatives of the basis functions
        # d(cosh)/dz = l1*sinh...
        # d(exp(u z)cos(vz))/dz = u*exp*cos - v*exp*sin = u*f3 - v*f4
        
        u = np.real(l2)
        v = np.imag(l2)
        
        if order == 1:
            d1 = l1 * np.sinh(l1*z)
            d2 = l1 * np.cosh(l1*z)
            d3 = u * np.exp(u*z) * np.cos(v*z) - v * np.exp(u*z) * np.sin(v*z)
            d4 = u * np.exp(u*z) * np.sin(v*z) + v * np.exp(u*z) * np.cos(v*z)
            d5 = -u * np.exp(-u*z) * np.cos(v*z) - v * np.exp(-u*z) * np.sin(v*z)
            d6 = -u * np.exp(-u*z) * np.sin(v*z) + v * np.exp(-u*z) * np.cos(v*z)
            return np.array([d1, d2, d3, d4, d5, d6])
            
        elif order == 2:
            # d2 of sinh is l1^2 sinh.
            # d2 of exp*cos: (u+iv)^2 * exp*(cos+isin) -> (u^2-v^2 + 2iuv)*...
            # Real part: (u^2 - v^2)f3 - 2uv f4
            
            d1 = l1**2 * np.cosh(l1*z)
            d2 = l1**2 * np.sinh(l1*z)
            d3 = (u**2 - v**2) * np.exp(u*z) * np.cos(v*z) - 2*u*v * np.exp(u*z) * np.sin(v*z)
            d4 = (u**2 - v**2) * np.exp(u*z) * np.sin(v*z) + 2*u*v * np.exp(u*z) * np.cos(v*z)
            # For exp(-uz):
            # Deriv is -(u+iv) * ...
            # Deriv 2 is (u+iv)^2 * ... = same coefficients
            d5 = (u**2 - v**2) * np.exp(-u*z) * np.cos(v*z) + 2*u*v * np.exp(-u*z) * np.sin(v*z)
            d6 = (u**2 - v**2) * np.exp(-u*z) * np.sin(v*z) - 2*u*v * np.exp(-u*z) * np.cos(v*z)
            return np.array([d1, d2, d3, d4, d5, d6])
            
        elif order == 4:
            # We can get D^4 by applying (D^2)^2 or directly calculating
            # Directly is safer to avoid recursion errors.
            # Since d2/dz^2 [exp*(u+iv)z] = (u+iv)^2 * ...
            # Then d4/dz^4 = (u+iv)^4 * ...
            # Re((u+iv)^4) = Re((r e^it)^4) = r^4 cos(4t).
            # Or calculate (u^2-v^2 + 2iuv)^2 = (A + iB)^2 = (A^2 - B^2) + i(2AB)
            # where A = u^2-v^2, B = 2uv.
            
            A = u**2 - v**2
            B = 2*u*v
            Re_l2_4 = A**2 - B**2
            Im_l2_4 = 2*A*B
            
            # Note: d4/dz4 of exp(l z) is l^4 exp(l z)
            
            d1 = l1**4 * np.cosh(l1*z)
            d2 = l1**4 * np.sinh(l1*z)
            d3 = Re_l2_4 * np.exp(u*z) * np.cos(v*z) - Im_l2_4 * np.exp(u*z) * np.sin(v*z)
            d4 = Re_l2_4 * np.exp(u*z) * np.sin(v*z) + Im_l2_4 * np.exp(u*z) * np.cos(v*z)
            d5 = Re_l2_4 * np.exp(-u*z) * np.cos(v*z) + Im_l2_4 * np.exp(-u*z) * np.sin(v*z)
            d6 = Re_l2_4 * np.exp(-u*z) * np.sin(v*z) - Im_l2_4 * np.exp(-u*z) * np.cos(v*z)
            return np.array([d1, d2, d3, d4, d5, d6])

    def build_matrix():
        # Matrix is 6x6. Rows are BCs. Cols are Basis Coeffs.
        M = np.zeros((6, 6), dtype=complex)
        
        # --- Bottom Boundary Conditions (z=0) ---
        F_0 = get_basis_funcs(0)
        D1_0 = get_basis_derivs(0, 1)
        D2_0 = get_basis_derivs(0, 2)
        D4_0 = get_basis_derivs(0, 4)
        
        # 1. w(0) = 0
        M[0, :] = F_0
        # 2. w'(0) = 0
        M[1, :] = D1_0
        # 3. (D^2 - k^2)^2 w = 0  => D^4 w - 2k^2 D^2 w + k^4 w = 0
        M[2, :] = D4_0 - 2*k**2 * D2_0 + k**4 * F_0
        
        # --- Top Boundary Conditions (z=1) ---
        F_1 = get_basis_funcs(1)
        D2_1 = get_basis_derivs(1, 2)
        D4_1 = get_basis_derivs(1, 4)
        
        # 4. w(1) = 0
        M[3, :] = F_1
        # 5. w''(1) = 0
        M[4, :] = D2_1
        # 6. (D^2 - k^2)^2 w = 0 => D^4 w - 2k^2 D^2 w + k^4 w = 0
        M[5, :] = D4_1 - 2*k**2 * D2_1 + k**4 * F_1
        
        return M

    M = build_matrix()
    # The determinant must be real (or very close to it) because the physical problem is real.
    # We return the absolute value of the real part to find the zero.
    return np.abs(np.real(det(M)))

# ==========================================
# 3. Solver for Critical Thresholds
# ==========================================

def find_Ra_for_k(k):
    """
    Finds the smallest Ra > 0 such that det(M) = 0 for a given k.
    Since det(M) is monotonic in Ra (stability increases with Ra, 
    or rather, eigenvalues shift), we can bracket the root.
    
    Actually, for this type of problem, Ra is the eigenvalue.
    As Ra increases from 0, the determinant crosses zero.
    The smallest positive root is the critical Ra for that k.
    """
    
    # Range search
    # Based on literature, we expect Ra_c between 500 and 2000.
    # We perform a scan to find bracketing points.
    
    Ra_scan = np.linspace(100, 3000, 300)
    dets = []
    
    # Optimization: compute vectorized? 
    # For now, loop is safe as 300 iterations is fast.
    for r in Ra_scan:
        dets.append(solve_eigenvalue_problem(r, k))
        
    dets = np.array(dets)
    
    # Find where sign changes or where minimum ~ 0
    # The determinant is typically high at low Ra, dips, crosses zero?
    # Or starts negative and becomes positive?
    # Let's look for the minimum absolute value in the scan to refine.
    
    # However, a robust sign change is better.
    # Let's look for intervals where det changes sign or passes through a minimum near zero.
    
    # Find indices where det is small
    min_idx = np.argmin(np.abs(dets))
    
    # Refine around the minimum
    Ra_guess = Ra_scan[min_idx]
    
    # Use Brent's method or Newton if possible. 
    # Since we don't have derivative, we use a bounded method on the nearest edge 
    # or minimize |det|.
    
    # Generally, det(Ra) is monotonic-ish. 
    # Let's simply minimize the squared determinant.
    res = minimize_scalar(lambda r: solve_eigenvalue_problem(r, k)**2, 
                          bracket=(max(100, Ra_guess-500), Ra_guess+500), 
                          method='brent', options={'xtol': 1e-4})
    
    return res.x

# ==========================================
# 4. Main Execution
# ==========================================

print("Starting Linear Stability Analysis...")
print("Boundary Conditions:")
print("  Bottom (z=0): No-slip, Constant Heat Flux")
print("  Top (z=1):    Free-slip, Fixed Temperature")
print("-" * 40)

# Scan wavenumbers k to find the minimum Ra
k_values = np.linspace(1.5, 3.5, 40) # Expected range ~2.0-3.0
Ra_k = []

print(f"Scanning k in [{k_values[0]}, {k_values[-1]}]...")
for k in k_values:
    Ra_c_k = find_Ra_for_k(k)
    Ra_k.append(Ra_c_k)
    print(f"k = {k:.2f}, Ra_c(k) = {Ra_c_k:.1f}")

Ra_k = np.array(Ra_k)

# Find global minimum
min_idx = np.argmin(Ra_k)
k_c_est = k_values[min_idx]
Ra_c_est = Ra_k[min_idx]

# Refine k around the minimum using interpolation or further search
# Using a finer minimization
def objective(k):
    return find_Ra_for_k(k)

print("\nRefining search for global minimum...")
res_final = minimize_scalar(objective, bracket=(k_values[min_idx-1], k_values[min_idx+1]), method='brent', options={'xtol': 0.001})

k_c = res_final.x
Ra_c = res_final.fun

print("-" * 40)
print(f"CRITICAL VALUES:")
print(f"Critical Rayleigh Number (Ra_c): {Ra_c:.2f}")
print(f"Critical Wavenumber (k_c):       {k_c:.4f}")
print("-" * 40)

# Check against allowed error
# Note: Due to the nature of numerical root finding and discretization,
# small errors are expected. 
# The prompt allows +/- 0.5 for Ra and +/- 0.02 for k.

# ==========================================
# 5. Visualization
# ==========================================

plt.figure(figsize=(8, 5))
plt.plot(k_values, Ra_k, 'b.-', label='Neutral Stability Curve')
plt.plot(k_c, Ra_c, 'ro', label=f'Critical Point ($k_c={k_c:.2f}, Ra_c={Ra_c:.0f}$)')
plt.xlabel('Horizontal Wavenumber $k$')
plt.ylabel('Rayleigh Number $Ra$')
plt.title('Linear Stability Threshold: Ra(k)')
plt.grid(True)
plt.legend()
plt.show()

# Plot the eigenmode shape at the critical threshold
# We need to reconstruct w(z) for k_c, Ra_c
# This involves solving the linear system M*v = 0 for the nullspace.
# We can use SVD to find the null vector.

print("\nVisualizing Critical Eigenmode...")

# Re-compute characteristic roots for k_c, Ra_c
rho = (k_c**2 * Ra_c)**(1.0/3.0)
a1 = k_c**2 - rho                      
a2 = k_c**2 + rho * 0.5                
l1 = np.sqrt(a1)
l2 = np.sqrt(a2 + 0j)
u = np.real(l2)
v = np.imag(l2)

z_eval = np.linspace(0, 1, 100)
mode_shape = np.zeros_like(z_eval, dtype=complex)

# Define basis functions again
def get_basis_array(z):
    # Returns column vector of basis functions
    f1 = np.cosh(l1*z)
    f2 = np.sinh(l1*z)
    f3 = np.exp(u*z) * np.cos(v*z)
    f4 = np.exp(u*z) * np.sin(v*z)
    f5 = np.exp(-u*z) * np.cos(v*z)
    f6 = np.exp(-u*z) * np.sin(v*z)
    return np.array([f1, f2, f3, f4, f5, f6])

# We need the matrix M at the critical point to find the coefficients
# Reuse logic from solve_eigenvalue_problem but extract M
def get_matrix_at临界(k, Ra):
    rho = (k**2 * Ra)**(1.0/3.0)
    a1 = k**2 - rho
    a2 = k**2 + rho * 0.5
    l1 = np.sqrt(a1)
    l2 = np.sqrt(a2 + 0j)
    u = np.real(l2)
    v = np.imag(l2)
    
    def get_basis_funcs(z):
        f1 = np.cosh(l1*z)
        f2 = np.sinh(l1*z)
        f3 = np.exp(u*z) * np.cos(v*z)
        f4 = np.exp(u*z) * np.sin(v*z)
        f5 = np.exp(-u*z) * np.cos(v*z)
        f6 = np.exp(-u*z) * np.sin(v*z)
        return np.array([f1, f2, f3, f4, f5, f6])

    def get_basis_derivs(z, order):
        # Simplified version just for extraction
        # Using the logic from previous function
        if order == 1:
            d1 = l1 * np.sinh(l1*z)
            d2 = l1 * np.cosh(l1*z)
            d3 = u * np.exp(u*z) * np.cos(v*z) - v * np.exp(u*z) * np.sin(v*z)
            d4 = u * np.exp(u*z) * np.sin(v*z) + v * np.exp(u*z) * np.cos(v*z)
            d5 = -u * np.exp(-u*z) * np.cos(v*z) - v * np.exp(-u*z) * np.sin(v*z)
            d6 = -u * np.exp(-u*z) * np.sin(v*z) + v * np.exp(-u*z) * np.cos(v*z)
            return np.array([d1, d2, d3, d4, d5, d6])
        elif order == 2:
            d1 = l1**2 * np.cosh(l1*z)
            d2 = l1**2 * np.sinh(l1*z)
            d3 = (u**2 - v**2) * np.exp(u*z) * np.cos(v*z) - 2*u*v * np.exp(u*z) * np.sin(v*z)
            d4 = (u**2 - v**2) * np.exp(u*z) * np.sin(v*z) + 2*u*v * np.exp(u*z) * np.cos(v*z)
            d5 = (u**2 - v**2) * np.exp(-u*z) * np.cos(v*z) + 2*u*v * np.exp(-u*z) * np.sin(v*z)
            d6 = (u**2 - v**2) * np.exp(-u*z) * np.sin(v*z) - 2*u*v * np.exp(-u*z) * np.cos(v*z)
            return np.array([d1, d2, d3, d4, d5, d6])
        elif order == 4:
            A = u**2 - v**2
            B = 2*u*v
            Re_l2_4 = A**2 - B**2
            Im_l2_4 = 2*A*B
            d1 = l1**4 * np.cosh(l1*z)
            d2 = l1**4 * np.sinh(l1*z)
            d3 = Re_l2_4 * np.exp(u*z) * np.cos(v*z) - Im_l2_4 * np.exp(u*z) * np.sin(v*z)
            d4 = Re_l2_4 * np.exp(u*z) * np.sin(v*z) + Im_l2_4 * np.exp(u*z) * np.cos(v*z)
            d5 = Re_l2_4 * np.exp(-u*z) * np.cos(v*z) + Im_l2_4 * np.exp(-u*z) * np.sin(v*z)
            d6 = Re_l2_4 * np.exp(-u*z) * np.sin(v*z) - Im_l2_4 * np.exp(-u*z) * np.cos(v*z)
            return np.array([d1, d2, d3, d4, d5, d6])

    M = np.zeros((6, 6), dtype=complex)
    F_0 = get_basis_funcs(0)
    D1_0 = get_basis_derivs(0, 1)
    D2_0 = get_basis_derivs(0, 2)
    D4_0 = get_basis_derivs(0, 4)
    M[0, :] = F_0
    M[1, :] = D1_0
    M[2, :] = D4_0 - 2*k**2 * D2_0 + k**4 * F_0
    
    F_1 = get_basis_funcs(1)
    D2_1 = get_basis_derivs(1, 2)
    D4_1 = get_basis_derivs(1, 4)
    M[3, :] = F_1
    M[4, :] = D2_1
    M[5, :] = D4_1 - 2*k**2 * D2_1 + k**4 * F_1
    return M

M_final = get_matrix_at临界(k_c, Ra_c)

# Find null space using SVD
U, s, Vh = np.linalg.svd(M_final)
# The vector corresponding to the smallest singular value is the null space
coeffs = Vh[-1, :]  # This is the right singular vector for min singular value

# Normalize coeffs (e.g., max real part = 1)
coeffs = coeffs / np.abs(np.max(coeffs))

# Calculate w(z)
for i, z in enumerate(z_eval):
    basis = get_basis_array(z)
    w_z = np.dot(coeffs, basis)
    mode_shape[i] = w_z

plt.figure(figsize=(8, 5))
plt.plot(z_eval, np.real(mode_shape), 'b-', label='$\hat{w}(z)$ (Vertical Velocity)')
plt.axhline(0, color='k', linestyle='--', alpha=0.5)
plt.xlabel('Height $z$')
plt.ylabel('Amplitude')
plt.title(f'Critical Eigenmode Shape at $k_c={k_c:.2f}, Ra_c={Ra_c:.0f}$')
plt.grid(True)
plt.legend()
plt.show()

print("Analysis complete.")
```
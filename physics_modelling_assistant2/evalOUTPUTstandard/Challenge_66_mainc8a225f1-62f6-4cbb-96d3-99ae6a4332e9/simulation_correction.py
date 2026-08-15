
```python
import sympy as sp

def compute_index_generating_function(max_charge, field_charges, dim_adj):
    """
    Computes the generating function of the index of trace relations.
    
    Args:
    max_charge (int): The maximum charge to compute up to.
    field_charges (list): List of charges for the adjoint fields (e.g., [1, 2]).
    dim_adj (int): Dimension of the adjoint representation (N^2 for U(N)).
    
    Returns:
    dict: Coefficients of the generating function I(q) up to max_charge.
    sympy.Expr: The symbolic expression for I(q).
    """
    
    # Define the symbolic variable q (chemical potential)
    q = sp.Symbol('q')
    
    # 1. Construct Single-Particle Generating Function G(q)
    # G(q) = Sum( dim_adj * q^{charge} ) for each fermion field
    # Based on model: psi (ch 1) and d_psi (ch 2)
    G_q = sum(dim_adj * q**charge for charge in field_charges)
    
    # 2. Compute Multi-Particle Partition Function Z(q) using Plethystic Exponential
    # PE[G(q)] = exp( sum_{k=1}^{infinity} G(q^k) / k )
    # We truncate the sum at max_charge because terms with k > max_charge
    # contribute only to powers > max_charge given the lowest field charge is 1.
    
    exponent_series = 0
    for k in range(1, max_charge + 1):
        # G(q^k) substitution
        G_qk = sum(dim_adj * q**(charge * k) for charge in field_charges)
        exponent_series += G_qk / k
        
    # Expand the exponential to get series for Z(q)
    # Remove O(q^n) terms and convert to polynomial
    Z_q = sp.exp(exponent_series).series(q, 0, max_charge + 1).removeO()
    
    # 3. Compute Trace Relations contribution R(q)
    # The model implies that the constraints (trace relations) are related to the
    # inverse of the single particle dynamics at the origin of moduli space.
    # Specifically, R(q) is derived from the expansion of 1/G(q).
    # R(q) ~ 1/G(q) ignoring the pole constant term (1/dim_adj) -> starts at q^1.
    
    # Calculate series expansion of 1/G(q)
    R_q = (1 / G_q).series(q, 0, max_charge + 1).removeO()
    
    # 4. Compute the Generating Function of the Index I(q)
    # Model: I(q) = Z(q) - R(q)
    I_q = sp.expand(Z_q - R_q)
    
    # Extract coefficients
    coefficients = {}
    for n in range(max_charge + 1):
        coeff = sp.expand(I_q).coeff(q, n)
        coefficients[n] = coeff
        
    return coefficients, sp.expand(I_q)

# --- Main Execution ---

# Parameters
MAX_CHARGE = 15
# U(2) adjoint dimension is 2^2 = 4
DIM_ADJ_U2 = 4 
# Fields: psi (charge 1), partial_psi (charge 2)
FIELD_CHARGES = [1, 2]

# Computation
coeffs, I_q_expr = compute_index_generating_function(MAX_CHARGE, FIELD_CHARGES, DIM_ADJ_U2)

# Output formatting
print(f"Generating Function Calculation for U(2) Gauge Theory")
print(f"Fields: psi (ch 1), ∂ψ (ch 2)")
print(f"Adjoint Dimension: {DIM_ADJ_U2}")
print("-" * 60)
print(f"Series expansion of I(q) up to q^{MAX_CHARGE}:")
print(I_q_expr)
print("-" * 60)
print("Coefficients of the Index:")
print(f"{'Charge':<10} {'Index Value':<15}")
for n in range(MAX_CHARGE + 1):
    print(f"{n:<10} {coeffs[n]:<15}")
```
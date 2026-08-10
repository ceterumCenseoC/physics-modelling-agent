
```python
def solve_system():
    # Imports
    # No external packages allowed, so we rely on standard python
    
    # --- Step 1: Define Model Constants ---
    
    # Orbital counts based on the problem setup
    # 1b position (plaquette center): n_b orbitals
    # 2c position (edge center): n_c orbitals
    # 1a position (lattice site): n_a orbitals
    
    # Case 1: Initial Configuration
    # 10 bands total. 
    # 4 at 1b, 2 at 2c (which constitutes n_c=1 representation), 
    # remaining 4 at 1a.
    n_b_initial = 4
    n_c_initial = 1 # "Two of them... 2c position" -> one symmetric pair per unit cell
    
    # Case 2: Modified Configuration
    # "One additional occupied band with Wannier orbitals at 1b position"
    n_b_modified = n_b_initial + 1
    n_c_modified = n_c_initial # No change to 2c
    
    # Frank Angle and Parameters
    # Frank angle Omega = -pi/2
    # The formula involves the factor s = Omega / (2*pi)
    import math
    Omega = -math.pi / 2
    s = Omega / (2 * math.pi) # s = -1/4
    
    # --- Step 2: Define Calculation Logic ---
    
    def calculate_fractional_charge(n_b, n_c, is_trivial_class):
        """
        Calculates the disclination charge Q/e.
        
        Based on the formula:
        Q_dis/e = s * (n_b + 2*n_c) + Term_translation
        
        Where Term_translation is determined by the equivalence class.
        For the nontrivial class (N=1), the term cancels the 2*n_c contribution 
        and effectively behaves like Q/e = -s * (2*n_c) for that specific vector,
        combined with the rotational inventory. 
        
        From the derivation provided in the context:
        Nontrivial (N=1): Q/e = + n_b / 4  (since s=-1/4 and the translational anomaly cancels rotation specific terms)
        Trivial (N=0):    Q/e = s * (n_b + 2*n_c)
        
        Note: The exact decomposition depends on the basis of eigenvalues, 
        but the net result modulo 1 is well-defined by the topology.
        """
        
        if is_trivial_class:
            # Trivial class: only the rotation inventory term
            q = s * (n_b + 2 * n_c)
        else:
            # Nontrivial class
            # Based on the context derivation:
            # Q = + n_b / 4 mod 1
            q = (n_b / 4.0)
            
        return q

    def to_standard_interval(q):
        """
        Map the charge q to the interval [-1/2, 1/2).
        """
        # First, map to [0, 1) using modulo 1
        # Python's % works for floats but handles negative numbers differently.
        # We want a mathematical modulo 1.
        remainder = q - math.floor(q)
        
        # Adjust mathematically to ensure 0 <= remainder < 1
        # Handling potential floating point drifts at the boundary
        if remainder >= 1.0:
            remainder -= 1.0
        if remainder < 0.0:
            remainder += 1.0
            
        # Map to [-1/2, 1/2)
        if remainder >= 0.5:
            remainder -= 1.0
            
        return remainder

    # --- Step 3: Perform Calculations ---
    
    # Configuration 1: Initial System
    # Nontrivial class
    q1_nontrivial_raw = calculate_fractional_charge(n_b_initial, n_c_initial, is_trivial_class=False)
    q1_nontrivial = to_standard_interval(q1_nontrivial_raw)
    
    # Trivial class
    q1_trivial_raw = calculate_fractional_charge(n_b_initial, n_c_initial, is_trivial_class=True)
    q1_trivial = to_standard_interval(q1_trivial_raw)
    
    # Configuration 2: Modified System (with extra band)
    # Nontrivial class
    q2_nontrivial_raw = calculate_fractional_charge(n_b_modified, n_c_modified, is_trivial_class=False)
    q2_nontrivial = to_standard_interval(q2_nontrivial_raw)
    
    # Trivial class
    q2_trivial_raw = calculate_fractional_charge(n_b_modified, n_c_modified, is_trivial_class=True)
    q2_trivial = to_standard_interval(q2_trivial_raw)
    
    # --- Step 4: Format Output ---
    
    print("---- Step-by-Step Derivation ----")
    print("Formula applied: $Q_{dis}/e = \\frac{\\Omega}{2\\pi}(n_b + 2n_c) + \\text{Translation Term}$")
    print(f"Given Frank angle $\\Omega = -\\pi/2$, factor $s = -1/4$.")
    print()
    
    print("--- Case 1: Initial Configuration ($n_b=4, n_c=1$) ---")
    print("1. Nontrivial translation-equivalence class:")
    print(f"   Using $Q/e = +n_b/4$: $Q/e = {n_b_initial}/4 = {n_b_initial/4.0}$. ")
    print(f"   Mapping to $[-1/2, 1/2)$: {q1_nontrivial}")
    print()
    print("2. Trivial translation-equivalence class:")
    print(f"   Using $Q/e = s(n_b + 2n_c) = -1/4({n_b_initial} + 2({n_c_initial})) = -{n_b_initial + 2*n_c_initial}/4 = -{(n_b_initial + 2*n_c_initial)/4.0}$. ")
    print(f"   Mapping to $[-1/2, 1/2)$: {q1_trivial}")
    print()
    
    print("--- Case 2: Additional Band at 1b ($n_b=5, n_c=1$) ---")
    print("1. Nontrivial translation-equivalence class:")
    print(f"   Using $Q/e = +n_b/4$: $Q/e = {n_b_modified}/4 = {n_b_modified/4.0}$. ")
    print(f"   Mapping to $[-1/2, 1/2)$: {q2_nontrivial}")
    print()
    print("2. Trivial translation-equivalence class:")
    print(f"   Using $Q/e = s(n_b + 2n_c) = -1/4({n_b_modified} + 2({n_c_modified})) = -{n_b_modified + 2*n_c_modified}/4 = -{(n_b_modified + 2*n_c_modified)/4.0}$. ")
    print(f"   Mapping to $[-1/2, 1/2)$: {q2_trivial}")
    print()
    
    print("---- Final Answer ----")
    
    # Define the requested formatting
    # The user asked for: 
    # Initial: Nontrivial, Trivial
    # Modified: Nontrivial, Trivial
    
    # Helper to format fractions nicely for display
    def format_fraction(val):
        if abs(val) < 1e-12: return "0"
        if abs(val - 0.25) < 1e-12: return "1/4"
        if abs(val + 0.25) < 1e-12: return "-1/4"
        if abs(val - 0.5) < 1e-12: return "1/2"
        if abs(val + 0.5) < 1e-12: return "-1/2"
        return f"{val:.12f}"

    print("Initial Configuration:")
    print(f"- Nontrivial translation-equivalence class: ${format_fraction(q1_nontrivial)}$")
    print(f"- Trivial translation-equivalence class: ${format_fraction(q1_trivial)}$")
    
    print()
    print("With one additional band at 1b ($l=+1/2$):")
    print(f"- Nontrivial translation-equivalence class: ${format_fraction(q2_nontrivial)}$")
    print(f"- Trivial translation-equivalence class: ${format_fraction(q2_trivial)}$")
    
    return q1_nontrivial, q1_trivial, q2_nontrivial, q2_trivial

if __name__ == "__main__":
    solve_system()
```
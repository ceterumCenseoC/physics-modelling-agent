
```python
import math

def solve_system():
    """
    Calculates the fractional disclination charge for a C4-symmetric 
    topological crystalline insulator.
    
    The logic preserves the formulas and values derived in the provided context.
    No external libraries are used.
    """
    
    # --- Step 1: Define Model Constants ---
    
    # Orbital counts based on the problem setup
    # 1b position (plaquette center): n_b orbitals
    # 2c position (edge center): n_c orbitals (representations)
    
    # Case 1: Initial Configuration
    # 10 bands total. 
    # 4 at 1b, 2 at 2c (which constitutes n_c=1 representation), 
    # remaining 4 at 1a.
    n_b_initial = 4
    n_c_initial = 1 
    
    # Case 2: Modified Configuration
    # "One additional occupied band with Wannier orbitals at 1b position"
    n_b_modified = n_b_initial + 1
    n_c_modified = n_c_initial 
    
    # Frank Angle and Parameters
    # Frank angle Omega = -pi/2
    # Factor s = Omega / (2*pi) = -1/4
    Omega = -math.pi / 2
    s_factor = Omega / (2 * math.pi) 
    
    # --- Step 2: Define Calculation Logic ---
    
    def calculate_fractional_charge(n_b, n_c, is_trivial_class):
        """
        Calculates the disclination charge Q/e based on the specific formula 
        derived in the context.
        
        Formulas from context:
        - Nontrivial class (N=1): Q/e = + n_b / 4  (simplification of inventory)
        - Trivial class (N=0):    Q/e = -1/4 * (n_b + 2*n_c)
        """
        
        if is_trivial_class:
            # Trivial class: Q = s * (n_b + 2*n_c)
            # With s = -1/4, this is -1/4 * (n_b + 2*n_c)
            q = s_factor * (n_b + 2 * n_c)
        else:
            # Nontrivial class
            # Derived formula: Q/e = + n_b / 4
            q = (n_b / 4.0)
            
        return q

    def to_standard_interval(q):
        """
        Map the charge q to the interval [-1/2, 1/2).
        """
        # Map to [0, 1) using mathematical modulo 1
        remainder = q - math.floor(q)
        
        # Correct for potential floating point boundary issues (e.g., 0.999999 vs 1.0)
        if remainder >= 1.0:
            remainder -= 1.0
        if remainder < 0.0:
            remainder += 1.0
            
        # Map from [0, 1) to [-1/2, 1/2)
        if remainder >= 0.5:
            remainder -= 1.0
            
        return remainder

    # --- Step 3: Perform Calculations ---
    
    # Configuration 1: Initial System
    q1_nontrivial = to_standard_interval(calculate_fractional_charge(n_b_initial, n_c_initial, False))
    q1_trivial = to_standard_interval(calculate_fractional_charge(n_b_initial, n_c_initial, True))
    
    # Configuration 2: Modified System
    q2_nontrivial = to_standard_interval(calculate_fractional_charge(n_b_modified, n_c_modified, False))
    q2_trivial = to_standard_interval(calculate_fractional_charge(n_b_modified, n_c_modified, True))
    
    # --- Step 4: Format Output ---
    
    print("---- Calculation of Disclination Charge ----")
    print(f"Frank angle factor s = {s_factor:.2f}")
    print()
    
    print("--- Case 1: Initial Configuration ($n_b=4, n_c=1$) ---")
    print(f"Nontrivial class: {q1_nontrivial} e")
    print(f"Trivial class:    {q1_trivial} e")
    print()
    
    print("--- Case 2: Additional Band ($n_b=5, n_c=1$) ---")
    print(f"Nontrivial class: {q2_nontrivial} e")
    print(f"Trivial class:    {q2_trivial} e")
    print()
    
    # --- Helper for display formatting ---
    def format_fraction(val):
        if abs(val) < 1e-12: return "0"
        if abs(val - 0.25) < 1e-12: return "1/4"
        if abs(val + 0.25) < 1e-12: return "-1/4"
        if abs(val - 0.5) < 1e-12: return "1/2"
        if abs(val + 0.5) < 1e-12: return "-1/2"
        return f"{val}"

    print("---- Final Answer ----")
    
    print("Initial Configuration:")
    print(f"- Nontrivial translation-equivalence class: ${format_fraction(q1_nontrivial)}$")
    print(f"- Trivial translation-equivalence class: ${format_fraction(q1_trivial)}$")
    
    print()
    print("With one additional band at 1b ($l=+1/2$):")
    print(f"- Nontrivial translation-equivalence class: ${format_fraction(q2_nontrivial)}$")
    print(f"- Trivial translation-equivalence class: ${format_fraction(q2_trivial)}$")

if __name__ == "__main__":
    solve_system()
```
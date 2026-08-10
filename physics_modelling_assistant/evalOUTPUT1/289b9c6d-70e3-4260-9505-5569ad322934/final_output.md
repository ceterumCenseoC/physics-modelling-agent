**

**Initial Configuration:**
- Nontrivial translation-equivalence class: `0`
- Trivial translation-equivalence class: `-1/2`

**With one additional band at 1b ($l=+1/2$):**
- Nontrivial translation-equivalence class: `1/4`
- Trivial translation-equivalence class: `1/4`

```python
import math

def solve_system():
    """
    Calculates the fractional disclination charge for a C4-symmetric 
    topological crystalline insulator.
    """
    
    # --- Step 1: Define Model Constants ---
    
    # Orbital counts based on the problem setup
    # Case 1: Initial Configuration
    # 10 bands total: 4 at 1b, 2 at 2c (n_c=1 rep), 4 at 1a
    n_b_initial = 4
    n_c_initial = 1 
    
    # Case 2: Modified Configuration
    # One additional occupied band at 1b
    n_b_modified = n_b_initial + 1
    n_c_modified = n_c_initial 
    
    # Frank Angle and Parameters
    # Omega = -pi/2
    s_factor = -1 / 4 
    
    # --- Step 2: Calculation Logic ---
    
    def calculate_fractional_charge(n_b, n_c, is_trivial_class):
        """
        Calculates the disclination charge Q/e.
        Based on Li et al, PRB 101, 115115 (2020).
        """
        if is_trivial_class:
            # Trivial class: Q = s * (n_b + 2*n_c)
            q = s_factor * (n_b + 2 * n_c)
        else:
            # Nontrivial class: Q = + n_b / 4
            q = (n_b / 4.0)
        return q

    def to_standard_interval(q):
        """
        Map the charge q to the interval [-1/2, 1/2).
        """
        # Map to [0, 1)
        remainder = q - math.floor(q)
        
        # Float correction
        if remainder >= 1.0:
            remainder -= 1.0
        if remainder < 0.0:
            remainder += 1.0
            
        # Map to [-1/2, 1/2)
        if remainder >= 0.5:
            remainder -= 1.0
            
        return remainder

    # --- Step 3: Perform Calculations ---
    
    # Configuration 1
    q1_nontrivial = to_standard_interval(calculate_fractional_charge(n_b_initial, n_c_initial, False))
    q1_trivial = to_standard_interval(calculate_fractional_charge(n_b_initial, n_c_initial, True))
    
    # Configuration 2
    q2_nontrivial = to_standard_interval(calculate_fractional_charge(n_b_modified, n_c_modified, False))
    q2_trivial = to_standard_interval(calculate_fractional_charge(n_b_modified, n_c_modified, True))
    
    # --- Step 4: Format Output ---
    def fmt(val):
        if abs(val) < 1e-12: return "0"
        if abs(val - 0.25) < 1e-12: return "1/4"
        if abs(val + 0.25) < 1e-12: return "-1/4"
        if abs(val - 0.5) < 1e-12: return "1/2"
        if abs(val + 0.5) < 1e-12: return "-1/2"
        return f"{val}"
        
    print("---- Final Answer ----")
    print("Initial Configuration:")
    print(f"- Nontrivial translation-equivalence class: ${fmt(q1_nontrivial)}$")
    print(f"- Trivial translation-equivalence class: ${fmt(q1_trivial)}$")
    print()
    print("With one additional band at 1b ($l=+1/2$):")
    print(f"- Nontrivial translation-equivalence class: ${fmt(q2_nontrivial)}$")
    print(f"- Trivial translation-equivalence class: ${fmt(q2_trivial)}$")

if __name__ == "__main__":
    solve_system()
```
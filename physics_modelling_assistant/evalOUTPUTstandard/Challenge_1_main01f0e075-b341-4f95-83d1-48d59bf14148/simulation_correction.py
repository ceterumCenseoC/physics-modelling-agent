```python
import sympy as sp
import warnings
import sys

# Suppress warnings for cleaner output
warnings.filterwarnings("ignore")

# -------------------------------------------------------------------
# Implementation of Holographic Weyl Anomaly Coefficients in 8 Dimensions
# -------------------------------------------------------------------
# Description:
# This script implements the mathematical model for the Holographic Weyl Anomaly
# in 8 dimensions. It defines the theoretical coefficients for the invariants
# composing the anomaly density X^{(4)} as derived from the context
# (Jia & Karydas, 2022). It also performs a dimensional analysis to validate
# the structure of these terms and generates a visualization of the coefficients.
# -------------------------------------------------------------------

def main():
    print("-" * 80)
    print("HOLOGRAPHIC WEYL ANOMALY IN D=8")
    print("-" * 80)
    print("Based on the Weyl-Fefferman-Graham (WFG) formalism.")
    print("Output: Coefficients of invariants in X^(4) and Dimensional Analysis.")
    print("-" * 80)

    # 1. Define the Coefficients
    # ---------------------------
    # Coefficients are determined from the context (Jia & Karydas, Eq 71, 72)
    # and the prompt's specific normalization.
    # c_1 ... c_6
    
    coefficients = {
        "tr(P^4)": sp.Rational(1, 8),
        "tr(P^3)": sp.Rational(0, 1),
        "tr(P^3)tr(P)": sp.Rational(-1, 6),
        "tr(BP)tr(P)": sp.Rational(-1, 24), # Corrected from tr(BP) to match dimension 8
        "tr(BP^2)": sp.Rational(1, 24),
        "tr(B^2)": sp.Rational(1, 384),
        "tr(B^2P)": sp.Rational(0, 1),
        "tr(OP)": sp.Rational(1, 192),
        "tr(OP^2)": sp.Rational(0, 1),
        "tr(Omega)": sp.Rational(0, 1),
        "tr(Omega P)": sp.Rational(0, 1)
    }

    # Print Coefficients
    print(f"{'Invariant Term':<20} | {'Coefficient':<10} | {'Numerical Value':<15}")
    print("-" * 80)
    for term, coeff in coefficients.items():
        # Rational is exact, float is for display
        num_val = float(coeff.evalf())
        print(f"{term:<20} | {str(coeff):<10} | {num_val:<15.5g}")
    
    print("\nFinal Expression for X^(4):")
    # Construct the string representation of X4
    X4_terms = []
    if coefficients["tr(P^4)"] != 0:
        X4_terms.append(f"({coefficients['tr(P^4)']}) * tr(P^4)")
    if coefficients["tr(P^3)tr(P)"] != 0:
        X4_terms.append(f"({coefficients['tr(P^3)tr(P)']}) * tr(P^3)tr(P)")
    if coefficients["tr(BP)tr(P)"] != 0:
        X4_terms.append(f"({coefficients['tr(BP)tr(P)']}) * tr(BP)tr(P)")
    if coefficients["tr(BP^2)"] != 0:
        X4_terms.append(f"({coefficients['tr(BP^2)']}) * tr(BP^2)")
    if coefficients["tr(B^2)"] != 0:
        X4_terms.append(f"({coefficients['tr(B^2)']}) * tr(B^2)")
    if coefficients["tr(OP)"] != 0:
        X4_terms.append(f"({coefficients['tr(OP)']}) * tr(OP)")
    
    X4_expr = "X^(4) = " + " + ".join(X4_terms)
    print(X4_expr)
    print("-" * 80)

    # 2. Dimensional Analysis
    # -----------------------
    # Dimensions of tensors (Mass dimension [M]):
    # P: M^2
    # B: M^4
    # O: M^6
    # Omega: M^8
    # Target dimension for X^(4) is M^8.
    
    print("\nDimensional Analysis Check:")
    dims = {
        "P": 2,
        "B": 4,
        "O": 6,
        "Omega": 8
    }
    
    def get_term_power(term_str):
        # Helper to calculate total mass dimension of a term string
        # Basic parsing logic
        power = 0
        if "P)" in term_str or "P^4" in term_str: # covers tr(P^4)
             count = term_str.count("P")
             # Note: simple parsing assuming explicit multiplication signs or clear naming
             if "P^4" in term_str: count = 4
             if "P^3" in term_str: count = 3
             if "P^2" in term_str: count = 2
             power += count * dims["P"]
        elif "B" in term_str:
            count = term_str.count("B")
            if "B^2" in term_str: count = 2
            power += count * dims["B"]
        elif "O" in term_str and "Ome" not in term_str:
            power += dims["O"]
        elif "Omega" in term_str:
            power += dims["Omega"]
        return power

    all_consistent = True
    for term in X4_terms:
        # Extract the part inside parentheses roughly, or just use keys
        # Mapping X4_parts to keys
        calc_dim = 0
        if "tr(P^4)" in term: calc_dim = 4*dims["P"]
        elif "tr(P^3)tr(P)" in term: calc_dim = 4*dims["P"]
        elif "tr(BP)tr(P)" in term: calc_dim = dims["B"] + 2*dims["P"]
        elif "tr(BP^2)" in term: calc_dim = dims["B"] + 2*dims["P"]
        elif "tr(B^2)" in term: calc_dim = 2*dims["B"]
        elif "tr(OP)" in term: calc_dim = dims["O"] + dims["P"]
        
        status = "PASS" if calc_dim == 8 else "FAIL"
        print(f"Term: ...{term[-20:]:<20} | Dim: {calc_dim} [M^{calc_dim}] | {status}")
        if calc_dim != 8: all_consistent = False

    if all_consistent:
        print("-> Dimensional analysis passed for all terms.")
    else:
        print("-> Warning: Dimensional analysis failed for some terms.")

    # 3. Visualization
    # -----------------
    # Plot the non-zero coefficients
    try:
        import matplotlib.pyplot as plt
        
        # Filter for plot data (non-zero)
        plot_data = {k: float(v) for k, v in coefficients.items() if v != 0}
        
        if plot_data:
            terms_labels = list(plot_data.keys())
            vals = list(plot_data.values())
            colors = ['green' if x > 0 else 'red' for x in vals]
            
            plt.figure(figsize=(10, 6))
            plt.bar(terms_labels, vals, color=colors, alpha=0.7)
            plt.title("Non-Zero Coefficients in $X^{(4)}$ (8D Weyl Anomaly)")
            plt.ylabel("Coefficient Value")
            plt.xlabel("Invariant Term")
            plt.xticks(rotation=45, ha="right")
            plt.grid(axis='y', linestyle='--', alpha=0.5)
            
            for i in range(len(terms_labels)):
                plt.text(i, vals[i], f"{vals[i]:.4f}", ha='center', va='bottom' if vals[i] > 0 else 'top')
                
            plt.tight_layout()
            plt.savefig('weyl_anomaly_coefficients.png')
            print("\n-> Visualization saved to 'weyl_anomaly_coefficients.png'")
            
    except ImportError:
        print("\n-> Matplotlib not installed. Skipping visualization.")
        print("   (To view graphs, please install matplotlib via `pip install matplotlib`)")

    print("-" * 80)
    print("Code execution complete.")

if __name__ == "__main__":
    main()
```
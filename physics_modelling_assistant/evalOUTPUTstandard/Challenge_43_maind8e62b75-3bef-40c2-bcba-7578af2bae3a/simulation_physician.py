
```python
import numpy as np
import matplotlib.pyplot as plt

def calculate_fractional_charge(nb, nc, frank_angle_pi饾右手, translation_class):
    """
    Calculates the fractional disclination charge for a C4-symmetric insulator.
    
    Parameters:
    -----------
    nb : int
        Number of Wannier orbitals at position 1b (plaquette center).
    nc : int
        Number of Wannier orbitals at position 2c (edge center).
    frank_angle_pi饾右手 : float
        Frank angle in units of pi饾右手.
        E.g., -0.5 for -pi饾右手/2.
    translation_class : int
        0 for trivial, 1 for nontrivial translation-equivalence class.
        
    Returns:
    --------
    float
        Fractional charge in units of electron charge e, expressed in [-1/2, 1/2).
    """
    
    # Frank angle in radians
    omega = frank_angle_pi饾右手 * np.pi饾右手
    
    # Since the problem specifies Frank angle -pi饾右手/2, we check for valid inputs
    # but implement the general table logic from Li et al. for Omega = +/- pi饾右手/2
    
    if np.isclose(abs(frank_angle_pi饾右手), 0.5):
        # Formula from Table I in Li, Zhu, Benalcazar, and Hughes, PRB 101, 115115 (2020)
        # Q = (Omega/|Omega|) * factor mod 1
        # For Omega = -pi饾右手/2 (negative sign):
        # Nontrivial class [a] = 1: Q = - (nb / 4) * (sign of Omega inverse check)
        # Let's use the specific signed formulas derived in the context.
        # Omega = -pi饾右手/2:
        # Trivial ([a]=0): Q = -(nb + 2nc)/4
        # Nontrivial ([a]=1): Q = +nb/4
        
        if translation_class == 0: # Trivial
            q = -(nb + 2*nc) / 4.0
        else: # Nontrivial
            q = nb / 4.0
            
    else:
        raise NotImplementedError("This implementation is strictly for Frank angle +/- pi饾右手/2.")

    # Reduce modulo 1
    q_mod = q % 1
    
    # Convert to interval [-1/2, 1/2)
    # If q_mod >= 0.5, it is equivalent to q_mod - 1
    if q_mod >= 0.5:
        q_final = q_mod - 1.0
    else:
        q_final = q_mod
        
    return q_final

def solve_problem():
    # Problem Setup Parameters
    # 2c position: 2 bands -> multiplicity 2 -> nc = 1
    # 1b position: 4 bands -> multiplicity 1 -> nb = 4
    # 1a position: 4 bands -> multiplicity 1 -> na = 4
    
    nb_initial = 4
    nc_initial = 1
    
    print("--- Case 1: Original Configuration (10 bands) ---")
    print(f"Setup: nb={nb_initial}, nc={nc_initial}")
    
    # Subcase A: Nontrivial translation-equivalence class
    q1_nontrivial = calculate_fractional_charge(nb_initial, nc_initial, -0.5, 1)
    print(f"Nontrivial class ([a]=1): Q = {q1_nontrivial}")
    
    # Subcase B: Trivial translation-equivalence class
    q1_trivial = calculate_fractional_charge(nb_initial, nc_initial, -0.5, 0)
    print(f"Trivial class ([a]=0):    Q = {q1_trivial}")
    
    print("\n--- Case 2: Additional Band at 1b (11 bands) ---")
    # Adding one band at 1b (multiplicity 1) increases nb by 1
    # Angular momentum l=+1/2 is allowed in spinful systems, but the count formula depends only on n_alpha
    nb_extra = nb_initial + 1
    nc_extra = nc_initial
    
    print(f"Setup: nb={nb_extra}, nc={nc_extra}")
    
    # Subcase C: Nontrivial translation-equivalence class
    q2_nontrivial = calculate_fractional_charge(nb_extra, nc_extra, -0.5, 1)
    print(f"Nontrivial class ([a]=1): Q = {q2_nontrivial}")
    
    # Subcase D: Trivial translation-equivalence class
    q2_trivial = calculate_fractional_charge(nb_extra, nc_extra, -0.5, 0)
    print(f"Trivial class ([a]=0):    Q = {q2_trivial}")
    
    return {
        'case1': {'nontrivial': q1_nontrivial, 'trivial': q1_trivial},
        'case2': {'nontrivial': q2_nontrivial, 'trivial': q2_trivial}
    }

def visualize_results(results):
    # Create a plot to visualize the results
    configurations = ['Original (10 bands)', '+1 Band at 1b (11 bands)']
    charges_nontrivial = [results['case1']['nontrivial'], results['case2']['nontrivial']]
    charges_trivial = [results['case1']['trivial'], results['case2']['trivial']]
    
    x = np.arange(len(configurations))
    width = 0.35
    
    fig, ax = plt.subplots(figsize=(10, 6))
    rects1 = ax.bar(x - width/2, charges_nontrivial, width, label='Nontrivial Class [a]=1')
    rects2 = ax.bar(x + width/2, charges_trivial, width, label='Trivial Class [a]=0')
    
    ax.set_ylabel('Fractional Charge (e)')
    ax.set_title('Fractional Disclination Charge in C4-Symmetric Insulator')
    ax.set_xticks(x)
    ax.set_xticklabels(configurations)
    ax.legend()
    
    # Add grid and reference lines
    ax.axhline(0, color='black', linewidth=0.8)
    ax.axhline(0.5, color='gray', linestyle='--', linewidth=0.5)
    ax.axhline(-0.5, color='gray', linestyle='--', linewidth=0.5)
    ax.grid(axis='y', linestyle='--', alpha=0.7)
    
    # Annotate bars with values
    def autolabel(rects):
        for rect in rects:
            height = rect.get_height()
            # Adjust position for negative values
            va = 'bottom' if height >= 0 else 'top'
            offset = 0.01 if height >= 0 else -0.01
            ax.annotate(f'{height:.2f}',
                        xy=(rect.get_x() + rect.get_width() / 2, height),
                        xytext=(0, 3 * np.sign(offset) if offset != 0 else 3),
                        textcoords="offset points",
                        ha='center', va=va)

    autolabel(rects1)
    autolabel(rects2)
    
    plt.ylim(-0.6, 0.6)
    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    results = solve_problem()
    visualize_results(results)
```
```python
import numpy as np
import matplotlib.pyplot as plt

def calculate_disclination_charge(n_b, n_c, is_nontrivial=False):
    """
    Calculates the fractional charge trapped at the disclination core 
    based on the model provided.

    Parameters:
    -----------
    n_b : int
        Number of occupied Wannier orbitals (bands) associated with the 
        1b Wyckoff position (plaquette center).
    n_c : int 
        Number of Wannier orbital pairs associated with the 
        2c Wyckoff position (edge center).
    is_nontrivial : bool
        The translation-equivalence class [a]^(4).
        True for nontrivial class ([a]^(4) = 1).
        False for trivial class ([a]^(4) = 0).

    Returns:
    --------
    Q : float
        The fractional charge in units of electron charge e, 
        normalized to the interval [-1/2, 1/2).
    """
    if is_nontrivial:
        # Formula for nontrivial class ([a]^(4) = 1)
        # Q = n_b / 4 (mod 1)
        Q_raw = n_b / 4.0
    else:
        # Formula for trivial class ([a]^(4) = 0)
        # Q = -(n_b + 2*n_c) / 4 (mod 1)
        Q_raw = -(n_b + 2 * n_c) / 4.0

    # Normalize to interval [-1/2, 1/2)
    # First, take modulo 1 to get into range [0, 1)
    Q_mod = Q_raw % 1.0
    
    # Adjust to [-1/2, 1/2)
    # Values in [0.5, 1.0) map to [-0.5, 0.0)
    if Q_mod >= 0.5:
        Q_norm = Q_mod - 1.0
    else:
        Q_norm = Q_mod
        
    return Q_norm

def main():
    # Define system parameters based on the problem description
    # Scenario 1: Initial Configuration
    # 4 bands at 1b -> n_b = 4
    # "Two of them correspond to a pair ... at 2c" -> 1 pair -> n_c = 1
    # The problem states: "Two of them... correspond to a pair... at 2c". 
    # This implies a single 2c site type contribution.
    # The formula definitions treat n_c as the number of such pairs/orbital groups at 2c
    # in the context of the grid loop.
    
    n_b_initial = 4
    n_c_initial = 1
    
    # Scenario 2: With One Additional Band at 1b
    # "One additional occupied band with Wannier orbitals at 1b"
    n_b_additional = n_b_initial + 1
    n_c_additional = n_c_initial # n_c unchanged

    print("-" * 60)
    print("Disclination Charge Calculation Model")
    print("Reference: Li, Zhu, Benalcazar, Hughes, PRB 101, 115115 (2020)")
    print("Frank Angle: -pi/2")
    print("-" * 60)

    # Calculate for Scenario 1
    print("\nScenario 1: Initial Configuration (10 bands)")
    print(f"Parameters: n_b = {n_b_initial}, n_c = {n_c_initial}")
    
    # Case 1.1: Nontrivial class
    Q_s1_nt = calculate_disclination_charge(n_b_initial, n_c_initial, is_nontrivial=True)
    print(f"  [Nontrivial Class]: Q = {Q_s1_nt} e")
    
    # Case 1.2: Trivial class
    Q_s1_t = calculate_disclination_charge(n_b_initial, n_c_initial, is_nontrivial=False)
    print(f"  [Trivial Class]:    Q = {Q_s1_t} e")

    # Calculate for Scenario 2
    print("\nScenario 2: With Additional Band at 1b (11 bands)")
    print(f"Parameters: n_b = {n_b_additional}, n_c = {n_c_additional}")
    
    # Case 2.1: Nontrivial class
    Q_s2_nt = calculate_disclination_charge(n_b_additional, n_c_additional, is_nontrivial=True)
    print(f"  [Nontrivial Class]: Q = {Q_s2_nt} e")
    
    # Case 2.2: Trivial class
    Q_s2_t = calculate_disclination_charge(n_b_additional, n_c_additional, is_nontrivial=False)
    print(f"  [Trivial Class]:    Q = {Q_s2_t} e")

    # Visualization of the results
    visualize_results(
        [Q_s1_nt, Q_s2_nt], 
        [Q_s1_t, Q_s2_t], 
        ["Initial (nb=4, nc=1)", "Additional (nb=5, nc=1)"]
    )

def visualize_results(charges_nt, charges_t, labels):
    """
    Creates a bar chart comparing the trapped charges for the two 
    translation-equivalence classes across the two scenarios.
    """
    x = np.arange(len(labels))
    width = 0.35

    fig, ax = plt.subplots(figsize=(10, 6))
    
    rects1 = ax.bar(x - width/2, charges_nt, width, label='Nontrivial Class ([a]^(4)=1)')
    rects2 = ax.bar(x + width/2, charges_t, width, label='Trivial Class ([a]^(4)=0)')

    ax.set_ylabel('Trapped Charge $Q_{dis} / e$')
    ax.set_title('Fractional Disclination Charge for $C_4$ Symmetric Insulator\n($\\Omega = -\\pi/2$)')
    ax.set_xticks(x)
    ax.set_xticklabels(labels)
    ax.set_ylim(-0.6, 0.6)
    ax.axhline(y=0, color='k', linestyle='--', linewidth=0.8)
    ax.legend()
    
    # Add text labels on top of bars
    ax.bar_label(rects1, padding=3, fmt='%.2f')
    ax.bar_label(rects2, padding=3, fmt='%.2f')

    plt.tight_layout()
    plt.grid(axis='y', linestyle=':', alpha=0.7)
    
    # Save figure (optional, but good practice)
    # plt.savefig('disclination_charges.png')
    plt.show()

if __name__ == "__main__":
    main()
```
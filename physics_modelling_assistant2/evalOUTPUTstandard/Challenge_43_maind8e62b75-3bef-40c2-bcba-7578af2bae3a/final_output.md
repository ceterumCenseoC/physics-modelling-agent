```python
def answer():
    r"""
    Return the values of the fractional charges trapped to the disclination core.

    Inputs
    ----------
    None

    Outputs
    ----------
    charge_nontrivial_a: float, fractional charge for the nontrivial translation-equivalence class with Frank angle $–\pi/2$.
    charge_trivial_a: float, fractional charge for the trivial translation-equivalence class with Frank angle $–\pi/2$.
    charge_nontrivial_b: float, fractional charge for the nontrivial translation-equivalence class with one additional occupied bands.
    charge_trivial_b: float, fractional charge for the trivial translation-equivalence class with one additional occupied bands.
    """

    # ------------------ FILL IN YOUR RESULTS BELOW ------------------
    # Based on the analysis of the problem using the formulas from 
    # Li, Zhu, Benalcazar, and Hughes, Phys. Rev. B 101, 115115 (2020), Table I:
    # Q_dis = Omega/(2pi) * (nb + 2nc) + T^(4) * P^(4) mod 1
    # For Omega = -pi/2:
    # Trivial class ([a]=0): Q = -(nb + 2nc)/4
    # Nontrivial class ([a]=1): Q = nb/4
    # Results expressed in interval [-1/2, 1/2).
    
    # Setup: nb = 4 (from 1b position), nc = 1 (from 2c position)
    # na = 4 (from 1a position) does not appear in the formula for C4.
    
    # Case A: Original configuration (10 bands)
    nb = 4
    nc = 1
    
    # Nontrivial class: Q = nb/4 = 4/4 = 1
    # 1 mod 1 = 0. In [-1/2, 1/2), this is 0.
    charge_nontrivial_a = 0.0
    
    # Trivial class: Q = -(nb + 2nc)/4 = -(4 + 2)/4 = -6/4 = -3/2
    # -3/2 mod 1 = -3/2 + 2 = 1/2.
    # In [-1/2, 1/2), 1/2 is represented as -1/2.
    charge_trivial_a = -0.5
    
    # Case B: With one additional occupied band at 1b (l=+1/2)
    # Total bands at 1b (nb) increases by 1.
    nb_extra = 5
    nc_extra = 1
    
    # Nontrivial class: Q = nb_extra/4 = 5/4
    # 5/4 mod 1 = 1/4.
    # In [-1/2, 1/2), this is 1/4.
    charge_nontrivial_b = 0.25
    
    # Trivial class: Q = -(nb_extra + 2*nc_extra)/4 = -(5 + 2)/4 = -7/4
    # -7/4 mod 1 = -7/4 + 2 = 1/4.
    # In [-1/2, 1/2), this is 1/4.
    charge_trivial_b = 0.25
    # ---------------------------------------------------------------

    return charge_nontrivial_a, charge_trivial_a, charge_nontrivial_b, charge_trivial_b
```
```python
def answer():
    r"""
    Return the values of scaling exponents $\alpha$ and $\beta$.

    Inputs
    ----------
    None

    Outputs
    ----------
    alpha: float, scaling exponent in $\xi\propto n_i^{\alpha}$.
    beta: float, scaling exponent in $\Delta V_g\propto n_i^{\beta}$.
    have_plateau: bool, True if such plateau appear in 3D topological insulator.
    are_important: bool, True if charge impuritis are still important.
    is_long_range: bool, True if long-range scattering give longer mean free path, False if short-range scattering.
    is_longer: bool, True if long-range scattering in both graphene and 3D topological insulator give longer mean free path.
    """

    # ------------------ FILL IN YOUR RESULTS BELOW ------------------
    alpha = -0.5
    beta = 1.0
    have_plateau = True
    are_important = True
    is_long_range = True
    is_longer = True
    # ---------------------------------------------------------------

    return alpha, beta, have_plateau, are_important, is_long_range, is_longer
```
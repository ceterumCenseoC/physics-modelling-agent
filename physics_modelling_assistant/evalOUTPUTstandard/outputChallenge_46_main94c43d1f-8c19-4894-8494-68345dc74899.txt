```python
def answer():
    r"""
    Return the energies of the scar states and the corresponding base-10 logarithms
    of their squared overlaps with the $Z_2$ state.

    Inputs
    ----------
    None

    Outputs
    ----------
    energies: list[float]
        Energies of the scar states in ascending order (four-decimal precision).
    log_overlaps: list[float]
        $\log_{10}|\langle Z_2|\psi\rangle|^2$ for each scar state in the same order as `energies` (four-decimal precision).
    """

    # ------------------ FILL IN YOUR RESULTS BELOW ------------------
    energies = [-2.8270, -2.4366, -2.0392, -1.6417, -1.2513, -0.8654, -0.4839, -0.1019, 0.2756, 0.6529, 1.0318, 1.4151, 1.8092, 2.2294]
    log_overlaps = [-5.3523, -4.1110, -3.1281, -2.3981, -1.8176, -1.3696, -1.1182, -1.0430, -1.1185, -1.3811, -1.8294, -2.4412, -3.2535, -4.5232]
    # ---------------------------------------------------------------

    return energies, log_overlaps
```
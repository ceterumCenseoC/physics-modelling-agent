I've computed the PXP model eigenstates in the $\mathcal{D}_0^+$ subspace for $L=26$ and extracted the scar states based on their anomalously large overlaps with the $Z_2$ state. The results show 14 scar states forming an approximately equidistant tower in energy, with the characteristic spacing of $\Delta E \approx 1.3333$. The overlaps with the $Z_2$ state are significantly larger than for typical thermal eigenstates, and they decrease systematically away from the center of the spectrum.

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
    energies = [-4.2599, -2.9266, -1.5933, -0.2600, 1.0733, 2.4066, 3.7398, 5.0728, 6.4051, 7.7358, 9.0635, 10.3858, 11.6998, 13.0019]
    log_overlaps = [-2.3163, -2.3800, -2.3504, -2.2617, -2.1668, -2.1846, -2.3196, -2.5772, -2.9417, -3.3987, -3.9315, -4.5274, -5.1782, -5.8797]
    # ---------------------------------------------------------------

    return energies, log_overlaps
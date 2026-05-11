import numpy as np

# Constants in SI units
HBAR = 1.054571817e-34      # J·s
MU_B = 9.2740100783e-24     # J/T
ELECTRON_CHARGE = 1.602176634e-19  # C
ELECTRON_MASS = 9.1093837015e-31   # kg
EV_TO_JOULE = 1.602176634e-19      # J/eV
V_PER_UM_TO_V_PER_M = 1e6          # V/µm → V/m

def calculate_edelstein_effect(
    E_magnitude,        # V/µm
    E_direction_deg,    # deg
    alpha_ev_aa,        # eV·Å
    m_me,               # m*/m_e
    tau_s,              # s
    mu_ev,              # eV
    d_nm=1.0            # nm
):
    """
    Edelstein magnetization for a Rashba 2DEG (SI-consistent).

    Returns:
    - M_3D: magnetization magnitude [A/m]
    - M_direction_deg: direction of M in-plane [deg]
    - regime: 'HDR', 'LDR', or 'Insulating'
    """

    # --- 1. Convert inputs to SI ---
    E_SI = E_magnitude * V_PER_UM_TO_V_PER_M      # V/m
    m_SI = m_me * ELECTRON_MASS                   # kg
    alpha_SI = alpha_ev_aa * EV_TO_JOULE * 1e-10  # eV·Å → J·m
    mu_SI = mu_ev * EV_TO_JOULE                   # J
    d_SI = d_nm * 1e-9                            # m

    # --- 2. Rashba band bottom (E_min = - m α^2 / (2 ħ^2)) ---
    E_band_bottom = - m_SI * alpha_SI**2 / (2 * HBAR**2)

    # --- 3. Determine regime ---
    if mu_SI >= 0:
        regime = 'HDR'
    elif mu_SI > E_band_bottom:
        regime = 'LDR'
    else:
        regime = 'Insulating'

    # --- 4. Prefactor from Kubo/Edelstein formula ---
    # General structure: M ∝ μ_B |e| τ N(E_F) α E
    # with N(E_F) = m / (2π ħ^2) in 2D.
    if regime == 'HDR':
        # HDR: M = (μ_B |e| τ m α / (2π ħ^2)) E
        prefactor_2D = (
            MU_B * abs(ELECTRON_CHARGE) * tau_s * m_SI * alpha_SI
            / (2 * np.pi * HBAR**2)
        )
    elif regime == 'LDR':
        # LDR: M = (μ_B |e| τ / (2π ħ^2)) * sqrt(m^2 α^2 + 2 m ħ^2 μ) * E
        term = m_SI**2 * alpha_SI**2 + 2 * m_SI * HBAR**2 * mu_SI
        if term <= 0:
            prefactor_2D = 0.0
        else:
            prefactor_2D = (
                MU_B * abs(ELECTRON_CHARGE) * tau_s * np.sqrt(term)
                / (2 * np.pi * HBAR**2)
            )
    else:
        prefactor_2D = 0.0

    # 2D magnetization (per area) along y for E along x, etc.
    M_2D = prefactor_2D * E_SI   # [A] (magnetic moment per area)

    # Convert to 3D magnetization [A/m] using thickness d
    M_3D = M_2D / d_SI

    # --- 5. Direction: M ∝ z × E (in-plane, perpendicular to E) ---
    E_dir_rad = np.deg2rad(E_direction_deg)
    M_dir_rad = (E_dir_rad + np.pi/2) % (2*np.pi)
    M_direction_deg = np.rad2deg(M_dir_rad)

    return M_3D, M_direction_deg, regime


# Quick example
if __name__ == "__main__":
    M, M_dir, reg = calculate_edelstein_effect(
        E_magnitude=10.0,      # V/µm
        E_direction_deg=0.0,   # along x
        alpha_ev_aa=0.01,      # eV·Å
        m_me=0.7,              # m*/m_e
        tau_s=1e-11,           # s
        mu_ev=0.05,            # eV
        d_nm=1.0               # nm
    )
    print(f"Regime: {reg}")
    print(f"Magnetization Magnitude: {M:.4e} A/m")
    print(f"Magnetization Direction: {M_dir:.1f}°")

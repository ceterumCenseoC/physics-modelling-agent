import numpy as np

def energy_dispersion(k, m, alpha_R):
    #Calculate the energy dispersion for the Rashba model.
    k_magnitude = np.linalg.norm(k)
    E_plus = (k_magnitude**2) / (2 * m) + alpha_R * k_magnitude
    E_minus = (k_magnitude**2) / (2 * m) - alpha_R * k_magnitude
    return E_plus, E_minus

def fermi_momenta(E_F, m, alpha_R, hbar):
    """Calculate the Fermi momenta for the given Fermi energy."""
    k_0 = alpha_R * m / hbar**2  # Rashba momentum scale
    if E_F >= 0:
        k_F_plus = - k_0 + np.sqrt(k_0**2 + 2 * m * E_F/hbar**2)
        k_F_minus = k_0 + np.sqrt(k_0**2 + 2 * m * E_F/hbar**2)
        return k_F_plus, k_F_minus
    else:
        k_F_plus = k_0 - np.sqrt(k_0**2 + 2 * m * E_F/hbar**2)
        k_F_minus = - k_0 + np.sqrt(k_0**2 + 2 * m * E_F/hbar**2)
        return k_F_plus, k_F_minus

def magnetization(mu_b, e, tau, m, alpha_R, E_F, E_direction, E_magnitude):
    """Calculate the magnetization due to the Edelstein effect."""
    if E_F >= 0:
        M = (mu_b * abs(e) * tau) / (2 * np.pi) * m * alpha_R * np.cross(np.array([0.0, 0.0, 1.0]), E_direction * E_magnitude)
    else:
        M = (mu_b * abs(e) * tau) / (2 * np.pi) * np.sqrt(m**2 * alpha_R**2 + 2 * m * E_F) * np.cross(np.array([0.0, 0.0, 1.0]), E_direction * E_magnitude)
    return M

# constants
e = 1.602176634e-19  # Elementary charge in 
mu_b = 9.274009994e-24  # Bohr magneton in J/T
m_e = 9.10938356e-31  # Electron mass in kg
hbar = 1.0545718e-34  # Reduced Planck constant in J·s

#parameters:
m_effective = 0.1 * m_e  # Effective mass
alpha_R  = 1.0 * 10**-11 * e # rashba coupling strength in J * m (converted from eV * m)
tau = 1.0 * 10**-14 # Scattering time in seconds
E_F = 0.1 * e  # Fermi energy in J (converted from eV) # set at 0.1 eV
E_magnitude = 1.0 * 10**4 # Electric field magnitude in V/m
E_direction = np.array([1.0, 0.0, 0.0])  # Electric field direction along x-axis

hbar = 1.054571817e-34        # J s
mu_B = 9.2740100783e-24       # J/T = A·m^2
e_charge = 1.602176634e-19    # C
m_e = 9.1093837015e-31        # kg

def to_J_per_m(alpha_eVm):
    """Convert alpha_R given in eV·m to J·m (if already J·m, pass it unchanged)."""
    return alpha_eVm * e_charge

def magnetization_edelstein(mu_b=mu_B,
                            e_abs=e_charge,
                            tau=1e-14,
                            m_eff=0.1,            # effective mass as multiple of m_e by default
                            alpha_R_eVm=1e-11,    # default in eV·m
                            E_vector=np.array([1e4,0.0,0.0]), # V/m
                            use_alpha_in_eVm=True):
    """
    Compute Edelstein magnetization vector M (A/m) in SI units.
    - m_eff: if float, interpreted as multiple of m_e (e.g. 0.1 -> 0.1*m_e).
             If you want to pass kg, pass m_eff_kg and set use_mass_kg=True (see below).
    - alpha_R_eVm: Rashba parameter in eV·m by default. Set use_alpha_in_eVm=False if you pass J·m.
    - E_vector: electric field vector in V/m.
    Returns: numpy array M (A/m).
    """
    # ensure numpy array
    E = np.array(E_vector, dtype=float)

    # convert effective mass to kg (if given as multiple of m_e)
    m_si = m_eff * m_e

    # convert alpha_R to J·m if needed
    alpha_R = to_J_per_m(alpha_R_eVm) if use_alpha_in_eVm else alpha_R_eVm

    # unit check: alpha_R [J·m], m_si [kg], mu_b [A·m^2], e_abs [C], tau [s], E [V/m]
    # prefactor from your formula:
    prefactor = (mu_b * abs(e_abs) * tau) / (2.0 * np.pi)

    # high-density regime expression (use m * alpha_R)
    # compute vector M = prefactor * m_si * alpha_R * (z_hat x E)
    z_hat = np.array([0.0, 0.0, 1.0])
    M_vec = prefactor * m_si * alpha_R * np.cross(z_hat, E)

    return M_vec

# Example usage and sanity check


if __name__ == "__main__":
    k_plus_F, k_minus_F = fermi_momenta(E_F, m_effective, alpha_R, hbar)
    print("fermi momenta k_F^+ = " + str(k_plus_F) + " m^{-1}$ and k_F^- = " + str(k_minus_F) + " m^{-1}")

    M = magnetization_edelstein(tau=1e-14, m_eff=0.1, alpha_R_eVm=1e-11, E_vector=[1e4,0,0])
    print("M (A/m) =", M)
    print("Magnitude (A/m) =", np.linalg.norm(M))

    """ M = magnetization(mu_b, e, tau, m_effective, alpha_R, E_F, E_direction, E_magnitude)
    print("magnetization M = " + str(M) + " A/m") """

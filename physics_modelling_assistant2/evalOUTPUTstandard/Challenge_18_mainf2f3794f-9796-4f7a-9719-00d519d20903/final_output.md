import sympy as sp

epsilon0 = sp.symbols('epsilon0', positive=True)   # vacuum permittivity
k, z_R, d0 = sp.symbols('k z_R d0')
alpha_1, alpha_2 = sp.symbols('alpha_1 alpha_2')
E_1, E_2 = sp.symbols('E_1 E_2')
phi_1, phi_2 = sp.symbols('phi_1 phi_2')
m, Omega_1, Omega_2 = sp.symbols('m Omega_1 Omega_2')

def answer(epsilon0, k, z_R, d0, alpha_1, alpha_2, E_1, E_2, phi_1, phi_2, m, Omega_1, Omega_2):
    r"""
    Return the expression of $k_1$ and $k_2$ in Sympy format.

    Inputs
    ----------
    epsilon0:sympy.Symbol, vacuum permittivity $\varepsilon_0$
    k:       sympy.Symbol, wave vector, $k$
    z_R:     sympy.Symbol, Rayleigh range, $z_R$
    d0:      sympy.Symbol, distance between the two spheres at equilibrium, $d_0$
    alpha_1: sympy.Symbol, polarizability of nanoparticles 1, $\alpha_1$
    alpha_2: sympy.Symbol, polarizability of nanoparticles 2, $\alpha_2$
    E_1:     sympy.Symbol, electric-field amplitude of tweezer 1, $E_1$
    E_2:     sympy.Symbol, electric-field amplitude of tweezer 2, $E_2$
    phi_1:   sympy.Symbol, phase of tweezer 1 at the focal plane, $\phi_1$
    phi_2:   sympy.Symbol, phase of tweezer 2 at the focal plane, $\phi_2$
    m:       sympy.Symbol, nanoparticle mass, $m$
    Omega_1: sympy.Symbol, frequency parameter of nanosphere 1, $\Omega_1$
    Omega_2: sympy.Symbol, frequency parameter of nanosphere 2, $\Omega_2$

    Outputs
    ----------
    k1: sympy.Expr, $k_1$ in the equations of motion
    k2: sympy.Expr, $k_2$ in the equations of motion
    """

    # ------------------ FILL IN YOUR RESULTS BELOW ------------------
    # The coupling constant k1 arises from the conservative gradient force interference
    # and is proportional to k^4/(4*pi*epsilon0*d0).
    # The coupling constant k2 arises from the non-conservative scattering force
    # (radiation pressure) and geometric asymmetry, proportional to k^3/(4*pi*epsilon0*d0^2).
    # Both are modulated by the phase difference k*d0 + phi_2 - phi_1.
    
    k1 = (k**4 * alpha_1 * alpha_2 * E_1 * E_2) / (4 * sp.pi * epsilon0 * d0) * sp.cos(k * d0 + phi_2 - phi_1)
    k2 = (k**3 * alpha_1 * alpha_2 * E_1 * E_2) / (4 * sp.pi * epsilon0 * d0**2) * sp.sin(k * d0 + phi_2 - phi_1)
    # ---------------------------------------------------------------

    return k1, k2
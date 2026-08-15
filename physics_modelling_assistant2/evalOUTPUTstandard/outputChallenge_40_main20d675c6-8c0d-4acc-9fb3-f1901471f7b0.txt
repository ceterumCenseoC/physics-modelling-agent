import sympy as sp

chi, kappa, sigma, k = sp.symbols('chi kappa sigma k', real=True)

def answer(chi, kappa, sigma, k):
    r"""
    Return the expression of hydrodynamic mode spectrum $\omega(k)$ in Sympy format.

    Inputs
    ----------
    chi: sympy.Symbol, charge susceptibility, $\chi$
    kappa: sympy.Symbol, quadrupole superfluid stiffness, $\kappa$
    sigma: sympy.Symbol, coefficient of the leading order dissipative term, $\sigma$
    k: sympy.Symbol, momentum, $k$

    Outputs
    ----------
    omega: set[sympy.Expr], a set of SymPy expression of inputs
    """

    # ------------------ FILL IN YOUR RESULTS BELOW ------------------
    # The dispersion relation for the hydrodynamic modes is derived from
    # the characteristic equation: chi * w^2 + i * sigma * k^4 * w - kappa * k^4 = 0
    # This arises from the conservation laws and constitutive relation for the
    # quadrupole superfluid (Damped Euler-Bernoulli beam equation).
    #
    # Solving for w:
    # w = (-i * sigma * k^4 +/- sqrt(4 * chi * kappa * k^4 - sigma^2 * k^8)) / (2 * chi)
    
    discriminant = sp.sqrt(4 * chi * kappa * k**4 - sigma**2 * k**8)
    w1 = (-sp.I * sigma * k**4 + discriminant) / (2 * chi)
    w2 = (-sp.I * sigma * k**4 - discriminant) / (2 * chi)
    
    omega = {w1, w2}
    # ---------------------------------------------------------------

    return omega
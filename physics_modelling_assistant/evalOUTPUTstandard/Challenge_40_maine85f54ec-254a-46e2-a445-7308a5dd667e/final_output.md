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
    omega: set[sympy.Expr], a set of hydrodynamic mode dispersion relation(s), $\omega(k)$
    """

    # ------------------ FILL IN YOUR RESULTS BELOW ------------------
    # Calculate the discriminant of the characteristic equation derived from the EFT
    # Characteristic eq: chi * w^2 + i * sigma * k^4 * w - kappa * k^4 = 0
    # Roots for w = ( - i * sigma * k^4 +/- sqrt( - sigma^2 * k^8 + 4 * chi * kappa * k^4 ) ) / ( 2 * chi )
    # Expanding the sqrt for the hydrodynamic limit (small k) gives the perturbative damping form.
    
    # The leading order term for the real part is:
    real_part_coefficient = sp.sqrt(kappa/chi)
    
    # The leading order term for the imaginary part is:
    # The damping term arises from the expansion of the root.
    # w ~ +/- sqrt(kappa/chi) k^2 + correction
    # The correction comes from the - i sigma k^4 w / (2 chi w_approx) -> - i sigma k^4 / (2 chi sqrt(kappa/chi) k^2) ?
    # Wait, solving chi w^2 - i sigma k^4 w - kappa k^4 = 0 is simpler.
    
    # w = ( i sigma k^4 +/- sqrt( (i sigma k^4)^2 + 4 chi kappa k^4 ) ) / (2 chi)
    #   = ( i sigma k^4 +/- k^2 sqrt( 4 chi kappa - sigma^2 k^4 ) ) / (2 chi)
    
    # Small k expansion: sqrt( 4 chi kappa - sigma^2 k^4 ) approx 2 sqrt(chi kappa) - (sigma^2 k^4) / (4 sqrt(chi kappa))
    # w approx ( i sigma k^4 +/- ( 2 chi sqrt(kappa/chi) k^2 - (sigma^2 k^6)/(4 sqrt(chi kappa)) ) ) / (2 chi)
    # w approx +/- sqrt(kappa/chi) k^2 + i (sigma k^4)/(2 chi) ...
    
    # Wait, the sign of the damping term in the equation of motion determines the sign of the imaginary part.
    # Equation: chi d_t^2 phi + sigma k^4 d_t phi + kappa k^4 phi = 0 (in Fourier space)
    # Assume w = -i lambda. -chi lambda^2 - i sigma k^4 (-i lambda) + kappa k^4 = 0 => -chi lambda^2 - sigma k^4 lambda + kappa k^4 = 0
    # lambda = ( sigma k^4 +/- sqrt( sigma^2 k^8 + 4 chi kappa k^4 ) ) / (2 chi)
    # w = -i lambda. For stability (decaying modes), lambda > 0.
    # The modes are damped oscillations.
    
    # Let's use the form derived in the context which is the standard result for this EFT:
    # w = +/- sqrt(kappa/chi) k^2 - i (sigma / (2*chi)) k^4
    
    omega_1 = sp.sqrt(kappa/chi) * k**2 - sp.I * sigma * k**4 / (2 * chi)
    omega_2 = -sp.sqrt(kappa/chi) * k**2 - sp.I * sigma * k**4 / (2 * chi)
    
    omega = {omega_1, omega_2}
    # ---------------------------------------------------------------

    return omega
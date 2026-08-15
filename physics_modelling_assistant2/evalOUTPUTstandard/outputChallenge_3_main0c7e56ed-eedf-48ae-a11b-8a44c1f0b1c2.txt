import sympy as sp

m, r0, eta = sp.symbols('m r0 eta', positive=True)

def answer(m, eta, r0):
    r"""
    Return expression of the one-point function

    Inputs
    ----------
    m: sympy.Symbol, mass of the buld field, $m$
    eta: sympy.Symbol, the brane tension, $\eta$
    r0: sympy.Symbol, the black hole radius, $r_0$

    Output
    ----------
    O_x: sympy.Expr, the one-point function, $\langle \mathcal{O}(x) \rangle$
    """

    # ------------------ FILL IN YOUR RESULT BELOW ------------------
    # The one-point function in the geodesic approximation is proportional to 
    # exp(-m * L_reg), where L_reg is the regulated length of the geodesic 
    # from the boundary to the brane.
    # The brane location is determined by the junction condition: r_b = r0 / sqrt(1 - eta^2).
    # The regulated length is L_reg = -log(r0) - arccosh(r_b / r0).
    # Substituting r_b and simplifying arccosh(1/sqrt(1-eta^2)) yields:
    # L_reg = -ln(r0) - 0.5 * ln((1+eta)/(1-eta)).
    # Thus, <O(x)> ~ exp(m * ln(r0)) * exp(0.5 * m * ln((1+eta)/(1-eta))).
    # <O(x)> ~ r0^m * ((1+eta)/(1-eta))^(m/2).
    
    O_x = r0**m * ((1 + eta) / (1 - eta))**(m / 2) 
    # ---------------------------------------------------------------

    return O_x
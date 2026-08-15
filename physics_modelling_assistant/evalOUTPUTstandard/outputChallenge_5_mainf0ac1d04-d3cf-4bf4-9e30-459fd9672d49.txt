import sympy as sp

alpha = sp.symbols('alpha', real=True)

def answer(alpha):
    r"""
    Return the expression of the derivative $g(\alpha)$ in Sympy format

    Inputs
    ----------
    alpha: sympy.Symbol, real parameter, $\alpha \in [0, 1]$

    Outputs
    ----------
    g_alpha:  sympy.Expr, $g(\alpha)$ for $\alpha \in [0, 1]$.
    """

    # ------------------ FILL IN YOUR RESULTS BELOW ------------------
    g_alpha = sp.log(1+alpha)/(1+alpha) - sp.Rational(1,2)*(1/(1+alpha))* sp.summation(
        sp.rf(sp.Rational(1,2), sp.Symbol('k')) * (4*alpha/(1+alpha)**2)**sp.Symbol('k') / ((sp.Symbol('k')+1)*sp.factorial(sp.Symbol('k'))) *
        (sp.polygamma(0, sp.Symbol('k') + sp.Rational(1,2)) - sp.polygamma(0, sp.Rational(1,2)) + sp.polygamma(0, sp.Symbol('k') + 1) - sp.polygamma(0, 1)),
        (sp.Symbol('k'), 0, sp.oo)
    )
    # ---------------------------------------------------------------

    return g_alpha
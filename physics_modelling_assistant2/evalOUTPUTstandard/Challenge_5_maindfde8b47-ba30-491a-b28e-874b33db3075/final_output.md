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
    g_alpha = sp.log(1 + alpha) + 1 / (1 + alpha)
    # ---------------------------------------------------------------

    return g_alpha
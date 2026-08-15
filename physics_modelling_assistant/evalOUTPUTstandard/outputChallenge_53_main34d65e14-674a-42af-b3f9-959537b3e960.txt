
import sympy as sp

d = sp.symbols('d')

def answer(d):
    r"""
    Return the expressions of the coefficients in SymPy format.

    Inputs
    ----------
    d: sympy.Symbol, variable, $d$

    Output
    ----------
    coeff1: sympy.Expr, the coefficient in front of $P^{k}{}_{i} P_{kj}$
    coeff2: sympy.Expr, the coefficient in front of $B_{k(i}P^k{}_{j)}$
    """

    # ------------------ FILL IN YOUR RESULT BELOW ------------------
    coeff1 = 1
    coeff2 = sp.Rational(1, 2)
    # ---------------------------------------------------------------

    return coeff1, coeff2
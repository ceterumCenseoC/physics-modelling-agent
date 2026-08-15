import sympy as sp

x = sp.symbols('x')

def answer(x):
    r"""
    Return the expression of $f(x)$ in Sympy format.

    Inputs
    ----------
    x : sympy.Symbol, optimization variable $x\in[0,1]$

    Outputs
    ----------
    f : sympy.Expr, the explicit function form of $f(x)$
    """

    # ------------------ FILL IN YOUR RESULTS BELOW ------------------
    # Define theta as a symbol with the assumption cos(theta) != 1 to match
    # the general problem description, though it acts as a constant parameter here.
    # Alternatively, we can treat cos(theta) as 'c' where c in [0, 1).
    # The problem asks for f(x) explicitly. Based on the derivation,
    # f(x) = cos^2(theta) * h(x), where h(x) is the binary entropy.
    # In Sympy, we use log for natural logarithm (nats).
    
    theta = sp.symbols('theta')
    
    # Binary entropy function h(x) = -x*log(x) - (1-x)*log(1-x)
    h_x = -x * sp.log(x) - (1 - x) * sp.log(1 - x)
    
    # The maximal Holevo information scales by cos^2(theta)
    f = sp.cos(theta)**2 * h_x
    # ---------------------------------------------------------------

    return f
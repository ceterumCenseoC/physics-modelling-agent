import sympy as sp

x, g, lambda_ = sp.symbols('x g lambda_')

def answer(x, g, lambda_):
    r"""
    Return the expression of the generating function in Sympy format.

    Inputs
    ----------
    x: sympy.Symbol, expansion variable, $x$
    g: sympy.Symbol, number of distinct ways for the particle to split, $g$
    lambda_: sympy.Symbol, weight assigned to the composite particle per time step, $\lambda$

    Outputs
    ----------
    Omega:  sympy.Expr, generating function $\Omega(x, g, \lambda) = \sum_{t = 0}^{\infty} Z(t) x^t$,
        simplified to an elementary function.
    """

    # ------------------ FILL IN YOUR RESULTS BELOW ------------------
    # Derivation:
    # K(x) = (1 - sqrt(1 - 4*x**2)) / 2 is the generating function for 
    # the first meeting of the two particles starting at distance 2.
    # The self-consistency equation for Omega is:
    # Omega = 1 + (2 * lambda_ * x) * Omega + (g * x * K(x)) * Omega**2
    # Rearranging: g * x * K(x) * Omega**2 + (2 * lambda_ * x - 1) * Omega + 1 = 0
    # Solving for Omega, we pick the root that satisfies Omega(0)=1.
    
    K = (1 - sp.sqrt(1 - 4*x**2)) / 2
    
    # The quadratic equation is: (g*x*K)*w^2 + (2*lambda*x - 1)*w + 1 = 0
    # We use the quadratic formula: w = (-b - sqrt(b^2 - 4ac)) / (2a)
    # where a = g*x*K, b = 2*lambda*x - 1, c = 1.
    # Note: We select the minus sign in the numerator based on series expansion analysis 
    # (which yields coefficients of order x^0, x^1, ... consistent with the model).
    
    a = g * x * K
    b = 2 * lambda_ * x - 1
    discriminant = b**2 - 4 * a
    
    Omega = (-b - sp.sqrt(discriminant)) / (2 * a)
    # ---------------------------------------------------------------

    return Omega
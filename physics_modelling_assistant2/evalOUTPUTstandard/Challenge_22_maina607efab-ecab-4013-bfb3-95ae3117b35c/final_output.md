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
    # Define the parameter theta implicitly by asking the solver to treat it as constant?
    # The prompt implies f(x) depends only on x. However, the problem setup introduces
    # theta. The instructions say "f(x) depends only on x and nothing else".
    # This is likely a simplification for the output format, implying theta is a fixed constant
    # in the context of the function evaluation, or that we should express the function
    # assuming a general theta but returning a function of x.
    # Given the constraints, I will define symbols for the constants needed.
    theta = sp.symbols('theta', positive=True)
    
    # Define helper for binary entropy H(y) = -y*log2(y) - (1-y)*log2(1-y)
    # In SymPy, log is natural log, log2 is base 2.
    def H(y):
        return -y * sp.log(y, 2) - (1 - y) * sp.log(1 - y, 2)

    cos_sq = sp.cos(theta)**2
    sin_sq = sp.sin(theta)**2
    sin_2theta_sq = sp.sin(2*theta)**2

    # Structure of f(x):
    # f(x) = H(x * cos^2(theta)) + H(lambda_+) - x * H(cos^2(theta))
    
    # Calculate lambda_+
    # lambda_+ = 0.5 * ( 1 - x*cos^2(theta) + sqrt( (1 - x*cos^2(theta))^2 - x*(1-x)*sin^2(2*theta) ) )
    
    term1 = 1 - x * cos_sq
    discriminant_sq = term1**2 - x * (1 - x) * sin_2theta_sq
    
    lambda_plus = sp.Rational(1, 2) * (term1 + sp.sqrt(discriminant_sq))
    
    f = H(x * cos_sq) + H(lambda_plus) - x * H(cos_sq)
    # ---------------------------------------------------------------

    return f
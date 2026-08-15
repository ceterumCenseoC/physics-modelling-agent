import sympy as sp

y, p_z, epsilon_IR, mu = sp.symbols('y p_z epsilon_IR mu')

def answer(y, p_z, epsilon_IR, mu):
    r"""
    Return the expressions of $\tilde{f}_q^{(1)}(y,p_z,\epsilon_{\rm IR},\mu)$
    in three intervals (i) $y < 0$, (ii) $0 < y < 1$, (iii) $y > 1$
    in Sympy format.

    Inputs
    ----------
    y: sympy.Symbol, momentum fraction in quasi-PDF, $y$
    p_z: sympy.Symbol, large momentum, $p_z$
    epsilon_IR: sympy.Symbol, infrared regulator, $\epsilon_{\rm IR}$
    mu: sympy.Symbol, renormalization scale, $\mu$

    Outputs
    ----------
    expr_neg: sympy.Expr, 1–loop correction $\tilde{f}_q^{(1)}(y,p_z,\epsilon_{\rm IR},\mu)$ for $y < 0$
    expr_mid: sympy.Expr, 1–loop correction $\tilde{f}_q^{(1)}(y,p_z,\epsilon_{\rm IR},\mu)$ for $0 < y < 1$
    expr_pos: sympy.Expr, 1–loop correction $\tilde{f}_q^{(1)}(y,p_z,\epsilon_{\rm IR},\mu)$ for $y > 1$
    """

    # ------------------ FILL IN YOUR RESULTS BELOW ------------------
    
    # Region y < 0
    # Expression: -(1+y^2)/(1-y) * ln(-y/(1-y)) - y - 3/2
    expr_neg = - (1 + y**2) / (1 - y) * sp.log(-y / (1 - y)) - y - sp.Rational(3, 2)
    
    # Region 0 < y < 1
    # Expression: [ (1+y^2)/(1-y) * (1/eps_IR - ln(mu^2/4pz^2) + ln(1-y)) + 3/2 * 1/(1-y) ]_+
    # Note: We provide the structure inside the plus-prescription brackets.
    # The standard PlusDistribution object or handling is applied externally or 
    # implicitly understood as the distribution form for the interval (0,1).
    expr_mid = ( (1 + y**2) / (1 - y) * 
                 ( 1 / epsilon_IR - sp.log(mu**2 / (4 * p_z**2)) + sp.log(1 - y) ) 
                 + sp.Rational(3, 2) / (1 - y) )
    
    # Region y > 1
    # Expression: (1+y^2)/(y-1) * ln(y/(y-1)) - y + 3/2
    expr_pos = ( (1 + y**2) / (y - 1) * sp.log(y / (y - 1)) 
                 - y + sp.Rational(3, 2) )
    
    # ---------------------------------------------------------------

    return expr_neg, expr_mid, expr_pos
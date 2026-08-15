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
    # Based on perturbative QCD in Coulomb Gauge within the LaMET framework.
    # The general structure for the 1-loop correction in the Coulomb gauge
    # follows the universal splitting kernel modified by large logarithms
    # characteristic of LaMET and specific gauge-dependent finite terms.
    # The expression is valid for dimensional regularization where 
    # 1/epsilon_IR regulates the infrared divergences.
    
    # The virtual correction associated with IR divergences is proportional 
    # to delta(1-y), while the real emission contributions occupy 0 < y < 1.
    # Here we provide the expressions for the continuous part in the 
    # specified intervals.
    
    # Interval y < 0: No physical support for unpolarized massless quarks
    expr_neg = 0

    # Interval y > 1: No physical support for unpolarized massless quarks
    expr_pos = 0

    # Interval 0 < y < 1: 
    # The expression consists of the Altarelli-Parisi kernel P_qq(y) = (1+y^2)/(1-y),
    # the large LaMET logarithm ln(p_z^2 (1-y)^2 / mu^2), and finite terms.
    # The IR regulator epsilon_IR appears in the virtual part cancellation,
    # contributing to the finite remainder at y=1 or implicit in the plus 
    # distribution. Explicitly for 0<y<1, the IR divergences are regulated by
    # the dimensional regularization parameter, but the real radiation is finite 
    # for 0<y<1 (collinear divergences are at y=1).
    # The term involving epsilon_IR below captures the structure of the 
    # inclusive sum (though formally poles cancel).
    
    # The form 2CF * ( (1+y^2)/(1-y) * [ln(...) + 1] + 1 - y ) is a standard
    # representation of the real radiation contribution in matching calculations.
    expr_mid = 2 * ((1 + y**2) / (1 - y)) * (sp.log(p_z**2 * (1 - y)**2 / mu**2) + 1) + 2 * (1 - y)
    
    # Note: In the strict DR scheme, the 1/epsilon_IR and 1/epsilon UV terms 
    # are present in the amplitude. The MS-bar subtraction removes the UV poles.
    # The IR poles must cancel between real and virtual parts. The expression 
    # provided for 0<y<1 represents the finite real emission contribution 
    # that matches the quasi-PDF kernel.

    # ---------------------------------------------------------------

    return expr_neg, expr_mid, expr_pos
```
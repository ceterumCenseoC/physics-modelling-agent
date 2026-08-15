import sympy as sp

a, b = sp.symbols('a b')

def answer(a, b):
    r"""
    Return the expression of the expectation value in SymPy format.

    Inputs
    ----------
    a: sympy.Symbol, single-qubit rotation angle in $U_{jk}$, $a$
    b: sympy.Symbol, two-qubit entangling angle in $U_{jk}$, $b$

    Output
    ----------
    expectation: sympy.Expr, the expectation value of the two-point correlation function of the qMPS in the thermodynamic limit, $\lim_{N\rightarrow \infty} \langle Z_{N-2} Z_{N} \rangle$
    """

    # ------------------ FILL IN YOUR RESULT BELOW ------------------
    expectation = sp.cos(a)**2 * sp.cos(2*b) + sp.sin(a)**2
    # ---------------------------------------------------------------

    return expectation
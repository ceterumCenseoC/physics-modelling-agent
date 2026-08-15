
```python
import sympy as sp

N, l = sp.symbols('N l', positive=True, integer=True)
p = sp.symbols('p', real=True)

def answer(N, p, l):
    r"""
    Return the expression of $\mathcal{S}_{0}$ in Sympy format.

    Inputs
    ----------
    N: sympy.Symbol, site number, $N$
    p: sympy.Symbol, noise rate, $p\in[0,1]$
    l: sympy.Symbol, string length, $l$

    Outputs
    ----------
    S0: sympy.Expr, string order parameter, $\mathcal{S}_{0}$
    """

    # ------------------ FILL IN YOUR RESULTS BELOW ------------------
    # The string order parameter for the noise-affected AKLT state
    # is derived to be $\left(\frac{9}{8}p - \frac{1}{2}\right)^l$.
    # In the limit of infinite chain (N -> infinity), the dependence on N
    # vanishes (assuming open boundary conditions for the string itself, 
    # the string length l is the dominant scale, and N is sufficiently large).
    S0 = ((9 * p) / 8 - sp.Rational(1, 2))**l
    # ---------------------------------------------------------------

    return S0
```
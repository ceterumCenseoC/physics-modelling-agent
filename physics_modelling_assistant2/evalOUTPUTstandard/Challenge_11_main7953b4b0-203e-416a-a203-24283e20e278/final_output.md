```python
import sympy as sp

Delta, x, K, m = sp.symbols('Delta x K m')

def answer(Delta, x, K, m):
    r"""
    Return the expressions of the beta functions in Sympy format.

    Inputs
    ----------
    Delta: sympy.Symbol, coupling constant $\Delta$
    x: sympy.Symbol, scaling dimension of $\Delta$, $x\equiv [\Delta]$
    K: sympy.Symbol, parameter $K$
    m: sympy.Symbol, parameter $m$

    Outputs
    ----------
    beta_Delta: sympy.Expr, beta function for coupling constant $\Delta$, $\beta(\Delta)$
    beta_x: sympy.Expr, beta function for $x$, $\beta(x)$
    """

    # ------------------ FILL IN YOUR RESULTS BELOW ------------------
    beta_Delta = (2 - x) * Delta
    beta_x = -Delta**2 / (4 * sp.pi)
    # ---------------------------------------------------------------

    return beta_Delta, beta_x
```
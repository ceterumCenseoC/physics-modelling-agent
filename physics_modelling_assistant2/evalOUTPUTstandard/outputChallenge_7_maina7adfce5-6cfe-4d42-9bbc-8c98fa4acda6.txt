```python
import sympy as sp

F, k, n, d, q = sp.symbols('F k n d q')

def answer(F, k, n, d, q):
    r"""
    Return the expression of the quantum Fisher information for $\theta_1$ in Sympy format.

    Inputs
    ----------
    F: sympy.Symbol, initialization fidelity, $F$
    k: sympy.Symbol, entangling gate fidelity, $k$
    n: sympy.Symbol, qubit number per node, $n$
    d: sympy.Symbol, sensor node number, $d$
    q: sympy.Symbol, defined by $q = (1 + e^{-\gamma t}) / 2$

    Outputs
    ----------
    QFI: sympy.Expr, quantum Fisher information for $\theta_1$
    """

    # ------------------ FILL IN YOUR RESULTS BELOW ------------------
    QFI = 4 * d * n**2 * F**2 * k**(2*n - 2) * (2*q - 1)**(2*n*d)
    # ---------------------------------------------------------------

    return QFI
```
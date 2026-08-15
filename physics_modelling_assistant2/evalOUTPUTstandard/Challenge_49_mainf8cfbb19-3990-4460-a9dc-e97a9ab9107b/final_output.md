```python
import sympy as sp

z, K = sp.symbols('z K')

def answer(z, K):
    r"""
    Return the expression of $\varphi$ in Sympy format.

    Inputs
    ----------
    z: sympy.Symbol, defined as $\log_2 t$
    K: sympy.Symbol, constant from the self-consistent equation
            $$\frac{1}{\ell^{\mu}(t)} \int_0^t \ell(\tau) \ell(t - \tau) d\tau = K$$

    Outputs
    ----------
    varphi: sympy.Expr, expansion of $\varphi$ in terms of $z$ for large $t$
        and retain terms up to constant order in $z$
    """

    # ------------------ FILL IN YOUR RESULTS BELOW ------------------
    varphi = z/2 + sp.log(z)/sp.log(2)/2  # SymPy expression in terms of z (and possibly K),
                  # retaining z, log_2(z), log_2(z)**2 terms; omit constants
    # Note: sp.log(z)/sp.log(2) is log_2(z). The result is z/2 + (1/2)*log_2(z).
    # The constant term is omitted.
    # ---------------------------------------------------------------

    return varphi
```
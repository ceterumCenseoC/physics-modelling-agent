```python
import sympy as sp

T, U = sp.symbols('T U')

def answer(T):
    """
    Return the temperature dependence of the energy phase space integral in SymPy format.

    Inputs
    ----------
    T: sympy.Symbol, temperature $T$
    U: sympy.Symbol, on-site interaction strength $U$

    Outputs
    ----------
    I: sympy.Expr, the energy phase space integral, $I(T)$
    """

    # ------------------ FILL IN YOUR RESULTS BELOW ------------------
    # The temperature dependence is quadratic: I(T) = A * (k_B * T)^2 + C
    # where A = pi^2/3. In units where k_B=1, we have:
    I = (sp.pi**2 / 3) * T**2
    # ---------------------------------------------------------------

    return I
```
import sympy as sp

k, n = sp.symbols('k n')
X_tot = sp.symbols('X_tot')

def answer(k, n, X_tot):
    r"""
    Return the expression of $\mathbb E\left[C^2\right]$ in Sympy format,
    and the minimal value of $n$ need to be to observe such oscillatory behavior.

    Inputs
    ----------
    k: sympy.Symbol, reaction rate constant $k$
    n: sympy.Symbol, number of components in the cycle $n$
    X_tot: sympy.Symbol, total population size $X_{tot}$

    Outputs
    ----------
    E_C2: sympy.Expr, expression of $\mathbb E\left[C^2\right]$ in terms of model parameters $k$ and $n$
    n_min: sympy.Expr, minimal value of $n$ to observe such oscillatory behavior
    """

    # ------------------ FILL IN YOUR RESULTS BELOW ------------------
    # The mean-squared amplitude of the stochastic oscillations scales with the 
    # total population and depends on the cycle length n. 
    # Derived from the fluctuation-dissipation relation for the dominant mode:
    # E[C^2] = X_tot / (4 * n * sin^2(pi/n))
    E_C2  = X_tot / (4 * n * sp.sin(sp.pi / n)**2)  
    
    # The minimal number of components to observe oscillatory behavior is 5.
    # For n < 5, the system is overdamped or symmetric, and distinct oscillatory 
    # dynamics do not emerge in the transient approach.
    n_min = sp.Integer(5)
    # ---------------------------------------------------------------

    return E_C2, n_min
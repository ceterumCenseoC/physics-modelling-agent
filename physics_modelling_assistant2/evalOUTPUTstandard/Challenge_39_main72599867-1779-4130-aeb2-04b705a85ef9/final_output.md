import sympy as sp

n, np = sp.symbols('n n_prime', integer=True, nonnegative=True)
g, gamma = sp.symbols('g gamma', positive=True)
alpha = sp.symbols('alpha')

def answer(n, np, g, gamma, alpha):
    r"""
    Return the expression of the steady-state cavity coherence in SymPy format.

    Inputs
    ----------
    n : sympy.Symbol
        Photon number in state $|n\rangle$.
    np : sympy.Symbol
        Photon number in state $|n'\rangle$.
    g : sympy.Symbol
        Atom-cavity coupling constant $g$.
    gamma : sympy.Symbol
        Spontaneous-emission rate from $|e\rangle$ to $|d\rangle$, $\gamma$.
    alpha : sympy.Symbol
        Complex amplitude of the initial coherent state $|\alpha\rangle$.

    Outputs
    ----------
    coherence : sympy.Expr
        Symbolic expression for the steady-state cavity coherence $\langle n'| \hat \rho_{c,ss}|n\rangle$.
    """

    # ------------------ FILL IN YOUR RESULTS BELOW ------------------
    # Derivation: The cavity state remains in the coherent state |alpha><alpha|
    # because the jump operator |d><e| acts only on the atom, leaving the 
    # cavity state unchanged, and the initial coherent state is an eigenstate
    # of the interaction term.
    # The expression for the Fock basis coherences of a coherent state is:
    # <n'|rho|n> = exp(-|alpha|^2) * alpha^n * (alpha*)^n' / sqrt(n! n'!)
    
    coherence = sp.exp(-sp.Abs(alpha)**2) * alpha**n * sp.conjugate(alpha)**np / (sp.sqrt(sp.factorial(n) * sp.factorial(np)))
    # ---------------------------------------------------------------

    return coherence
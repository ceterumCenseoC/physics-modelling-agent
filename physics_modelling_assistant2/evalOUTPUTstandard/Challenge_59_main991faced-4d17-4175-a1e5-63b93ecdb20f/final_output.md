import sympy as sp

M = sp.symbols('M')
epsilon = sp.symbols('epsilon')
a = sp.symbols('a')

def answer(M, epsilon, a):
    r"""
    Return the expressions of the $n_x$ criteria for structural factor to be nonvanishing
    and the corresponding structure factors in Sympy format.

    Inputs
    ----------
    M         : sympy.Symbol
        Large integer relating the strain wavelength to the lattice spacing.
    epsilon   : sympy.Symbol
        Amplitude of the static periodic strain.
    a         : sympy.Symbol
        Lattice spacing of the simple-cubic crystal.

    Outputs
    ----------
    allowed : set[(sympy.Expr, sympy.Expr)], Set of nonvanishing $n_x$ criteria with corresponding structure factor, {(nx, S)}
        nx: sympy.Expr, $n_x$ component of the reciprocal space vector in the lowest possible order Brillouin Zone
          for which the structure factor is nonvanishing (besides $n_x = M$).
        S: sympy.Expr, corresponding structure factor to the first order in $\varepsilon$
    """

    # ------------------ FILL IN YOUR RESULTS BELOW ------------------
    # The criteria for nonvanishing structure factor (satellites) in the lowest
    # Brillouin zone corresponds to integer shifts by 1/M relative to the
    # main intensity peak.
    # Since the problem asks for results in the "lowest-possible-order Brillouin Zone"
    # besides n_x = M (which is the main peak index in the superlattice scheme),
    # the allowed indices are M-1 and M+1.
    
    # Structure factor formula derivation for satellites:
    # S(n_x) ~ N * (pi * epsilon / a) * (integer index of main peak)
    # For n_x = M +/- 1 (superlattice indices), the structure factor is:
    # S = (-1)^{...} N * pi * epsilon * (M +/- 1) / a
    # The sign depends on the specific side of the peak.
    # For n_x = M + 1 (corresponds to n_x = 1 + 1/M in reduced units):
    # Phase contribution is negative.
    # For n_x = M - 1 (corresponds to n_x = 1 - 1/M in reduced units):
    # Phase contribution is positive.
    # See analysis for detailed sign derivation.
    
    # We define the structure factors proportional to the amplitude. The factor
    # N (number of unit cells) is a constant scalar for a given crystal.
    
    # Criteria: n_x = M - 1
    nx1 = M - 1
    S1 = sp.pi * epsilon * (M - 1) / a
    
    # Criteria: n_x = M + 1
    nx2 = M + 1
    S2 = -sp.pi * epsilon * (M + 1) / a

    allowed = {(nx1, S1), (nx2, S2)}
    # ---------------------------------------------------------------

    return allowed
import sympy as sp

t, k_12, k_13, k_23, k_34, N, q = sp.symbols('t k_{12} k_{13} k_{23} k_{34} N q')

def answer(t, k_12, k_13, k_23, k_34, N, q):
    r"""
    Return the expression of the phase between $|\psi^i(q)\rangle$ and $|\psi^f(q)\rangle$ in Sympy format.

    Inputs
    ----------
    t: sympy.Symbol, tunneling amplitude $t$
    k_12, k_13, k_23, k_34: sympy.Symbol, ground-state fusion channels
          $k_{ij}\in Z_N$ with $k_{ij}<-\frac{\phi_{ij}}{2\pi}<k_{ij}+1$
    N: sympy.Symbol, integer N defining $Z_N$
    q: sympy.Symbol, fusion channel between the unpaired zero modes

    Outputs
    ----------
    phase: sympy.Expr, the expression of the phase between the initial ground state $|\psi^i(q)\rangle$
          and final ground state $|\psi^f(q)\rangle$
    """

    # ------------------ FILL IN YOUR RESULTS BELOW ------------------
    # The phase is accumulated during the closed loop tunneling process.
    # The topological phase per step is proportional to the change in phase
    # or the stabilized fusion channel k_ij.
    # For the cycle H34 -> H23 -> H12 -> H13 -> H34, the total geometric phase
    # depends on the fusion channels k_ij with signs determined by the orientation
    # of the coupling change in the parameter space.
    # The sequence of movements is:
    # 34 -> 23 (move bond from 3-4 to 2-3) effectively removing k_34 and adding k_23
    # 23 -> 12 (move bond from 2-3 to 1-2) effectively removing k_23 and adding k_12
    # 12 -> 13 (move bond from 1-2 to 1-3) effectively removing k_12 and adding k_13
    # 13 -> 34 (move bond from 1-3 to 3-4) effectively removing k_13 and adding k_34
    # The sum of signed contributions is k_34 - k_23 + k_12 - k_13.
    # The unpaired zero modes with fusion channel q acquire a phase
    # proportional to q/N.
    
    phase = (2 * sp.pi * q / N) * (k_34 - k_23 + k_12 - k_13)
    # ---------------------------------------------------------------

    return phase
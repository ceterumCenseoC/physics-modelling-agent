
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
    # In the limit U >> W >> k_B T, the phase space integral scales as T^2.
    # The calculation yields a dimensionless constant (depending on the density of states
    # in the physical context, but here we return the T-dependence).
    # Based on the derivation, I(T) = A * T^2.
    # Setting the prefactor A to 1 for the pure temperature dependence representation.
    
    I = T**2
    # ---------------------------------------------------------------

    return I
import sympy as sp

Delta_k_sq, gamma = sp.symbols('Delta_k_sq gamma')

def answer(Delta_k_sq, gamma):
    r"""
    Return the expression of the quantum Fisher information in Sympy format.

    Inputs
    ----------
    Delta_k_sq: sympy.Symbol, $\Delta k^2 \equiv \int_{-\infty}^{\infty} d x\left[\frac{\partial \psi(x)}{\partial x}\right]^2$
    gamma: sympy.Symbol, $\gamma \equiv \int_{-\infty}^{\infty} d x \frac{\partial \psi(x)}{\partial x} \psi\left(x-u_2+u_1 \right)$

    Outputs
    ----------
    QFI: sympy.Expr, quantum Fisher information of estimating $\theta=\frac{1}{3}u_1+\frac{2}{3}u_2$ per each measured photon,
         $u_1$ and $u_2$ are the positions of the two point sources
    """

    # ------------------ FILL IN YOUR RESULTS BELOW ------------------
    QFI = (5*Delta_k_sq)/9 + (4*gamma)/9
    # ---------------------------------------------------------------

    return QFI
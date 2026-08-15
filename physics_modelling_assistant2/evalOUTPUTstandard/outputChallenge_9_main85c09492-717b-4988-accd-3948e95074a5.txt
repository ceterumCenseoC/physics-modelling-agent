
import numpy as np
from scipy.integrate import solve_ivp

def answer():
    r"""
    Return the number of e-folds achieved at $t = 2000000$.

    Inputs
    ----------
    None

    Outputs
    ----------
    e_folds: float, number of e-folds at $t = 2000000$
    """

    # ==========================================
    # 1. Parameter Initialization
    # ==========================================
    # Constants as defined in the problem statement context.
    # Using Natural Units where M_Pl = 1.
    
    M_Pl = 1.0           # Planck Mass
    n = 80.0             # Coupling constant
    f = 0.18 * M_Pl      # Decay constant
    Lambda = 1e-3 * M_Pl # Energy scale
    Lambda4 = Lambda**4  # Lambda^4 for potential calculation

    # Initial Conditions
    a_0 = 1.0            # Initial scale factor
    th_0 = 7.23          # Initial scalar field value
    dth_0 = 0.0          # Initial scalar field velocity

    # Time configuration
    t_start = 0.0
    t_end = 2000000.0
    # We don't strictly need intermediate points to get the final E-fold,
    # but a few points help if we were to plot.
    t_eval = np.linspace(t_start, t_end, 100)

    # ==========================================
    # 2. Model Functions
    # ==========================================

    def potential(th):
        """ V(th) = Lambda^4 * (1 - cos(th/f)) """
        return Lambda4 * (1.0 - np.cos(th / f))

    def potential_prime(th):
        """ dV/dth = (Lambda^4 / f) * sin(th/f) """
        return (Lambda4 / f) * np.sin(th / f)

    # ==========================================
    # 3. System of Differential Equations
    # ==========================================

    def system_equations(t, y):
        """
        Computes derivatives [da/dt, dth/dt, ddth/dt] based on the
        Nieh-Yan modified Einstein-Cartan equations.
        
        Equations:
        1. Torsion Constraint: phi = (1/24) * (dth/M_Pl + 8nf)
        2. Friedmann Eq: 3H^2 = (1/M_Pl^2) * [ 0.5*dth^2 + V + 24*n^2*f^2*phi^2 ]
        3. Klein-Gordon Eq: ddth + 3H*dth + V' - 48*n*f*dphi = 0
        """
        a = y[0]
        th = y[1]
        dth = y[2]

        # --- A. Torsion Field phi ---
        # Dimensional correction implies dividing velocity by M_Pl in the constraint.
        phi = (1.0 / 24.0) * (dth / M_Pl + 8.0 * n * f)

        # --- B. Hubble Parameter H ---
        rho_kinetic = 0.5 * dth**2
        rho_potential = potential(th)
        rho_torsion = 24.0 * (n**2) * (f**2) * (phi**2)
        
        rho_total = rho_kinetic + rho_potential + rho_torsion
        
        # Ensure non-negative radicand for numerical stability
        if rho_total < 0:
            H = 0.0
        else:
            H = np.sqrt(rho_total / (3.0 * M_Pl**2))

        # --- C. Scalar Field Acceleration ddth ---
        # From KG equation: ddth + 3H dth + V' - 48 n f dphi = 0
        # We derived that dphi = (1/24) * (ddth / M_Pl) = (1/24)*ddth (since M_Pl=1)
        # Substituting: ddth + 3H dth + V' - 48 n f (ddth / 24) = 0
        # ddth (1 - 2 n f) + 3H dth + V' = 0
        # ddth = - (3H dth + V') / (1 - 2 n f)
        
        V_prime = potential_prime(th)
        numerator = 3.0 * H * dth + V_prime
        denominator = 1.0 - 2.0 * n * f
        
        # The denominator is negative for n=80, f=0.18 (val = -27.8), indicating strong friction.
        ddth = - numerator / denominator

        # --- D. Scale Factor Growth ---
        dadt = H * a

        return [dadt, dth, ddth]

    # ==========================================
    # 4. Numerical Integration
    # ==========================================
    
    # Using Radau method as the system can be stiff due to the large coupling (n=80).
    solution = solve_ivp(
        system_equations, 
        [t_start, t_end], 
        [a_0, th_0, dth_0], 
        method='Radau', 
        t_eval=t_eval,
        rtol=1e-8, 
        atol=1e-10
    )

    # ==========================================
    # 5. Final Calculation
    # ==========================================
    
    # Extract scale factor at the end
    a_final = solution.y[0][-1]
    
    # Calculate E-folds: N = ln(a(t) / a(0))
    # Since a(0) = 1.0, it's just ln(a_final).
    e_folds = np.log(a_final / a_0)

    return e_folds
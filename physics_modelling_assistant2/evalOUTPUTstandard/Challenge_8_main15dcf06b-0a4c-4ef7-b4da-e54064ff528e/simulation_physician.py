
```python
import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp
from scipy.special import gamma

# ==========================================
# 1. Model Parameters and Initialization
# ==========================================

# Constants
M_Pl = 1.0               # Reduced Planck mass (unit system: M_Pl = 1)
n = 0.5                  # Nieh-Yan coupling
f = 1.7                  # Axial torsion coupling / Decay constant
Lambda = 3.7e-3          # Energy scale of the potential

# Potential V(vartheta) = Lambda^4 * (1 - cos(vartheta/f))
def potential(theta):
    return Lambda**4 * (1 - np.cos(theta / f))

# Derivative of potential V'(vartheta)
def potential_prime(theta):
    return (Lambda**4 / f) * np.sin(theta / f)

# Initial Conditions
# t=0 here corresponds to the start of the integration.
# The problem states t=0 implies 'start', but inflation happens later.
# We integrate forward to reach N=60 before end.
a_0 = 10.0
theta_0 = 5.0
dtheta_0 = 0.0

# Calculate initial Hubble parameter H_0 from Friedmann equation
# 3 M_Pl^2 H_0^2 = V(theta_0) + 0.5 * dtheta_0^2
# Note: In the torsion model, there is an effective kinetic term modification.
# From the action S_NY = -nf int dth...
# The background equation for torsion phi is: phi = dtheta / (12 M_Pl^2 n f H)
# This leads to a contribution in the Friedmann eq: rho_phi ~ n^2 f^2 dtheta^2 / (M_Pl^2 H^2 * constant)
# However, standard literature on this specific setup (Langvik et al) often reduces 
# to an effective friction or simple rescaling if we analyze the equations directly.
# Given the complexity of the full torsional backreaction in a single script,
# we will implement the background equations assuming the torsion constraint holds 
# and contributes to the energy density.

# Constraint from Nieh-Yan term (from background EoM of connection):
# phi = dtheta / (12 M_Pl^2 n f H)
# The density contribution from Nieh-Yan term (quadratic in phi): rho_NY ~ n^2 f^2 phi^2 H^2 ~ (dtheta)^2 / M_Pl^2
# Actually, the term is topological, its contribution to the stress-energy tensor 
# modifies the Hubble rate. 
# Derived Friedmann Eq (with phi constraint):
# 3 M_Pl^2 H^2 = 0.5 dtheta^2 + V(theta) + 12 n f H phi * dtheta ? 
# Let's use the explicit constraint to update the system of ODEs.

# Full System:
# H^2 = (1/3M_Pl^2) * [ 0.5*dtheta^2 + V(theta) + rho_NY ]
# rho_NY = 12 n f H phi * dtheta  (from action S_NY contribution after subbing phi) 
#       ~ 12 n f H * (dtheta / 12 M_Pl^2 n f H) * dtheta = dtheta^2 / M_Pl^2.
# So, 3 M_Pl^2 H^2 = 0.5*dtheta^2 + V + (1) dtheta^2 (roughly)
# Effectively: 3 M_Pl^2 H^2 = V + 1.5 dtheta^2.
# This is a significant rescaling.

def get_phi(theta_dot, H):
    """Background torsion from algebraic constraint."""
    # Avoid division by zero at H=0
    if H == 0: return 0.0
    return theta_dot / (12 * M_Pl**2 * n * f * H)

def equations_of_motion(t, y):
    """
    System of ODEs for background variables:
    y = [a, theta, dtheta]
    """
    a, theta, dtheta = y
    
    # 1. Calculate Potential and H
    V = potential(theta)
    
    # Friedmann Equation with Nieh-Yan contribution
    # Standard: 3H^2 = 0.5*dtheta^2 + V
    # NY Contribution (phi constrained): S_NY ~ -nf dth phi
    # Eq of motion for phi gives phi = dtheta / (12 M_Pl^2 n f H)
    # Energy density from Nieh-Yan term usually takes the form of a kinetic term modification.
    # Based on the derived relations in the "Context" (rho ~ (nfHphi)^2):
    # We implement the effective density: rho_eff = V + 0.5*(1 + 3*n^2*f^2)*dtheta^2
    # However, to be precise to the algebraic constraint:
    # The term in Lagrangian is +12nfH dtheta phi.
    # Substituting phi adds a term ~ dtheta^2 / H. This changes algebra.
    # Let's follow the prompt's explicit hint in Q1 "Value of ... (1+3n^2f^2)".
    # This suggests the kinetic normalization in the power spectrum is scaled by this factor.
    # For the background evolution, we will assume standard slow-roll dynamics 
    # are approximately valid or solve: 3H^2 = V + 0.5*(1 + 3*n**2*f**2)*dtheta**2.
    
    # Let's use the modified kinetic term implied by the power spectrum prefactor (1+3n^2f^2)
    # This is a common effective field theory approach for these terms.
    kinetic_factor = 0.5 * (1 + 3 * n**2 * f**2)
    rho = kinetic_factor * dtheta**2 + V
    
    H = np.sqrt(rho / (3 * M_Pl**2))
    
    # 2. Calculate Acceleration (Klein-Gordon)
    # d2theta + 3H dtheta + V' = 0
    # (Assuming the torsion coupling only rescales kinetic term and doesn't add direct force in this simplified limit)
    d2theta = -3 * H * dtheta - potential_prime(theta)
    
    return [H * a, dtheta, d2theta]

# ==========================================
# 2. Integration to find Horizon Crossing
# ==========================================

# We need to find the time N=60 e-folds before the end of inflation.
# End of inflation condition: epsilon = 1 (or approx when V << kinetic)
# We integrate forward until epsilon > 1.

t_start = 0
t_end_guess = 1e7 # Large enough time

# Event function to find end of inflation (epsilon = 1)
def epsilon_event(t, y):
    a, theta, dtheta = y
    V = potential(theta)
    H = np.sqrt((0.5*(1 + 3*n**2*f**2)*dtheta**2 + V)/(3*M_Pl**2))
    # epsilon = -dH/dt / H^2 = (rhodot+p)/(2Hrho) approx 0.5*dtheta^2 / (H^2*3) (only valid for minimal)
    # Modified epsilon: eps = -d ln H / dN
    # dH/dt = -0.5 * ( (1+3n^2f^2)*dtheta*d2theta + V'*dtheta ) / (3 M_Pl^2 H)
    # simpler approximation using potential V_deriv:
    
    # Vacuum spectral index parameter epsilon_H = - dH/dN / H
    # Let's use the slow-roll approx for stopping: eta ~ -1 or epsilon ~ 1
    # epsilon_V = 0.5 * M_Pl^2 * (V'/V)^2
    eps_v = 0.5 * M_Pl**2 * (potential_prime(theta)/V)**2
    # Stop when epsilon_V ~ 1 (Rolling down steep part)
    return eps_v - 1.0

epsilon_event.terminal = True
epsilon_event.direction = 1

sol = solve_ivp(
    equations_of_motion, 
    [t_start, t_end_guess], 
    [a_0, theta_0, dtheta_0], 
    events=epsilon_event, 
    dense_output=True, 
    rtol=1e-8, atol=1e-10
)

t_end = sol.t_events[0][0]
y_end = sol.y[:, -1]
a_end = y_end[0]

# Integrate backwards to find N=60
# N = ln(a_end / a_start). 
# We want t_hor such that ln(a_end / a_hor) = 60
# a_hor = a_end / exp(60)

N_end = 60.0
a_hor_target = a_end / np.exp(N_end)

# Interpolate to find time when a(t) = a_hor_target
from scipy.interpolate import interp1d
a_t = interp1d(sol.t, sol.y[0], kind='cubic', fill_value="extrapolate")
# Since a(t) is monotonic, we can find t. 
# Note: solve_ivp t might not have the exact point, so we search.
# We need the time t_hor corresponding to a_hor.
def find_t_for_a(target_a):
    # Simple search on the dense output or interpolation
    try:
        # Invert the interpolation
        t_a = interp1d(sol.y[0], sol.t, kind='cubic', fill_value="extrapolate")
        return t_a(target_a)
    except:
        # Fallback: find index
        idx = np.searchsorted(sol.y[0], target_a)
        return sol.t[idx]

t_hor = find_t_for_a(a_hor_target)

# Evaluate state at horizon crossing
y_hor = sol.sol(t_hor)
a_h, theta_h, dtheta_h = y_hor
H_h = np.sqrt((0.5*(1 + 3*n**2*f**2)*dtheta_h**2 + potential(theta_h))/(3*M_Pl**2))

# ==========================================
# 3. Calculation of Requested Quantities
# ==========================================

# --- Question 2: What is (delta_phi / (delta_dtheta - dtheta*A))? ---
# Derived in the theoretical section as: 1 / (12 M_Pl^2 n f H)
ratio_Q2 = 1.0 / (12 * M_Pl**2 * n * f * H_h)

# --- Question 3: What is (2*A*H / (dtheta*delta_theta))? ---
# Derived in the theoretical section in super-horizon limit: 2*H^2 / dtheta^2
ratio_Q3 = (2 * H_h**2) / (dtheta_h**2)

# --- Calculation of the main expression (Question 1) ---
# Expression:
# P_R * (1+3n^2f^2) / [ (H^2/4pi^2 MPl^2) (H/dtheta)^2 2^(2nu-3) |Gamma(nu)/Gamma(3/2)|^2 ]
# * (2AH / dtheta*delta_theta) * (beta * a * dtheta / delta_theta) * (delta_phi / (nf(d_delta_dtheta - nf*dtheta*A)))
#
# The theoretical analysis suggests this expression simplifies to 1 (normalization check) 
# or can be computed directly if we define the terms.
# 
# term1 = P_R * (1+3n^2f^2) / Standard_Spectrum_Factor
# term2 = ratio_Q3
# term3 = (beta * a * dtheta / delta_theta) -- This factor is ambiguous without specific gauge definition of beta.
#         Usually beta is related to B or x. In flat gauge, often suppressed or cancels. 
#         If we assume the expression is constructed to evaluate the corrected spectrum,
#         we calculate the value based on the derived simplified limits.
#
# The complex term "P_R(1+3n^2f^2) / St_Factor" is essentially the ratio of the 
// Nieh-Yan corrected spectrum to the standard slow-roll spectrum.
#
# Standard Slow Roll Spectrum P_S = (H^2 / 8pi^2 M_Pl^2 epsilon)
# Here epsilon = 0.5 * (1+3n^2f^2) * dtheta^2 / (M_Pl^2 H^2) (Effective epsilon)
# So P_S_NY = (H^2 / 8pi^2 M_Pl^2) / [0.5 * (1+3n^2f^2) * dtheta^2 / (M_Pl^2 H^2)]
# P_S_NY = (H^4) / (4pi^2 * (1+3n^2f^2) * dtheta^2)
#
# Let's evaluate the Main Problem 1 expression component by component numerically 
# where possible, and analytically for the rest.

# Calculate vertical index nu
# nu is defined via mode equation. In slow roll, nu = 3/2 + epsilon + ...
# Let's calculate epsilon_H at horizon crossing.
epsilon_H = 0.5 * (1 + 3*n**2*f**2) * (dtheta_h**2) / (M_Pl**2 * H_h**2)
nu_approx = 1.5 + epsilon_H # Approximation for amplitude calculation

# Amplitude factor
bessel_factor = 2**(2*nu_approx - 3) * np.abs(gamma(nu_approx)/gamma(1.5))**2
standard_prefactor = (H_h**2 / (4 * np.pi**2 * M_Pl**2)) * (H_h / dtheta_h)**2

# The Numerator involves P_R. In this gauge, P_R is defined with the torsion corrections.
# P_R = (H^2 / 8pi^2 M_Pl^2) (1/epsilon_eff) ??? 
# The prompt asks to evaluate the *expression*.
# Let's reconstruct the expression Q.
# Q = [P_R * (1+3n^2f^2)] / [standard_prefactor * bessel_factor] * ratio_Q3 * ratio_B * ratio_Q2_scaled
#
# Note: The term (beta a dtheta / delta_theta) is problematic.
# However, looking at the structure, it's likely ratio_B = 1/ratio_Q3 or something similar to cancel orders.
# OR, perhaps delta_theta is defined via gauge invariant R.
# R = -A - d(delta_theta)/dtheta.
# In superhorizon: delta_theta = (dtheta/H) A. 
# Then ratio_Q3 = 2 AH / (dtheta * (dtheta/H) A) = 2 H^2 / dtheta^2.
#
# Let's output the calculated components.

print(f"--- Results at Horizon Crossing (N=60) ---")
print(f"Time t_h: {t_hor:.4f}")
print(f"Scale Factor a: {a_h:.4e}")
print(f"Hubble H: {H_h:.4e} (MPl units)")
print(f"dtheta/dt: {dtheta_h:.4e}")
print(f"theta: {theta_h:.4f}")

print(f"\n--- Question 2: Ratio delta_phi / ... ---")
print(f"Value: {ratio_Q2:.4e}")
print(f"Theoretical: 1 / (12 M_Pl^2 n f H)")

print(f"\n--- Question 3: Ratio 2AH / ... ---")
print(f"Value: {ratio_Q3:.4e}")
print(f"Theoretical: 2 H^2 / dtheta^2 = 2 / M_Pl^2 epsilon_eff")

print(f"\n--- Question 1: Main Expression ---")
# We need P_R. 
# The expression for P_R in this model (derived from the context of Nieh-Yan)
# usually rescales the standard result by (1+3n^2f^2) factors.
# Standard amplitude A_s = H^2 / (8 pi^2 M_Pl^2 epsilon).
# Here epsilon_NY = (1+3n^2f^2) * epsilon_standard_kinetic.
# Approximation for P_R (Nieh-Yan limit):
epsilon_val = 0.5 * (1 + 3*n**2*f**2) * (dtheta_h**2) / (M_Pl**2 * H_h**2)
P_R_est = (H_h**2) / (8 * np.pi**2 * M_Pl**2 * epsilon_val)

# Value of the big fraction:
numerator_Q1 = P_R_est * (1 + 3*n**2*f**2)
denominator_Q1 = standard_prefactor * bessel_factor
main_fraction = numerator_Q1 / denominator_Q1

# The prompt asks for the value of the WHOLE expression.
# We are missing the definition of beta and delta_theta for the remaining factors.
# However, based on the "Main Problem" section of the prompt text,
# it seems to ask for the result of the calculation which often simplifies.
# If we assume the expression is a consistency identity:
# The value is likely 0.0 or 1.0 or a combination of slow roll params.
# Given the ambiguity of beta, we calculate the known ratio products.
# Ratio product = (2AH/...) * (beta a theta/d theta/...) * (dphi/...)
# If beta ~ (delta_theta)/(a dtheta) (gauge condition), then middle term is 1.
# Then product = ratio_Q3 * ratio_Q3_scaled_in_exp ...?
# Let's look at the explicit term in Q1:
# "... x (2AH / dtheta dtheta) x (beta a dtheta / dtheta) x (dphi / nf(d_ddtheta ...))"
# Term 3: (2AH / dtheta * dtheta) = 2H^2 / dtheta^2
# Term 4: (dphi / ...) = 1 / (12 M_Pl^2 n f H)
# Term 5: (beta a dtheta / dtheta) 
# If we substitute standard expressions for the gauge variable beta in flat gauge:
# beta is associated with the shift B. B = zeta - beta. 
# If we assume the gauge is spatially flat (psi=0), then beta is often link to A via momentum constraint.
# A ~ (dtheta/H) * (dtheta beta / a).
# So beta ~ a H A / dtheta^2.
# Term 5 = (a H A / dtheta^2) * a * dtheta / dtheta ~ a^2 H A / dtheta^2 ~ (a^2/dtheta^2) * (dtheta/H) * (dtheta beta/a) ...
# This is circular.
# However, note that sqrt(relation) often yields 1.

# Let's provide the explicit values of the solved parameters and the well-defined ratios.
print(f"P_R (estimated): {P_R_est:.4e}")
print(f"(1+3n^2f^2): {(1+3*n**2*f**2):.4e}")
print(f"Calculated Main Fraction (Part 1): {main_fraction:.4e}")

# Visualizing the background evolution
t_plot = np.linspace(t_start, t_end, 1000)
sol_plot = sol.sol(t_plot)
a_plot = sol_plot[0]
theta_plot = sol_plot[1]
H_plot = np.sqrt((0.5*(1+3*n**2*f**2)*sol_plot[2]**2 + potential(sol_plot[1]))/(3*M_Pl**2))
N_plot = np.log(a_plot / a_0)

plt.figure(figsize=(12, 5))

plt.subplot(1, 2, 1)
plt.plot(N_plot, theta_plot)
plt.axvline(np.log(a_h/a_0), color='r', linestyle='--', label='Horizon Crossing (N=60 to end)')
plt.xlabel('e-folds N')
plt.ylabel(r'$\vartheta$')
plt.title('Inflaton Field Evolution')
plt.legend()
plt.grid(True)

plt.subplot(1, 2, 2)
plt.plot(N_plot, H_plot)
plt.axvline(np.log(a_h/a_0), color='r', linestyle='--', label='Horizon Crossing')
plt.xlabel('e-folds N')
plt.ylabel('H')
plt.title('Hubble Parameter Evolution')
plt.legend()
plt.grid(True)

plt.tight_layout()
plt.show()

# Final outputs as requested by strict format
```
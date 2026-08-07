```python
import sympy as sp

# Define the symbolic variables
# Physical Constants
c = sp.symbols('c', positive=True)           # Speed of light
m_p = sp.symbols('m_p', positive=True)      # Proton mass

# Source Parameters
z = sp.symbols('z', positive=True)          # Redshift
t_v = sp.symbols('t_v', positive=True)      # Variability timescale
delta = sp.symbols('delta', positive=True)  # Doppler factor

# Seed Photon Parameters
E_s = sp.symbols('E_s', positive=True)      # Characteristic synchrotron-photon energy
L_s = sp.symbols('L_s', positive=True)      # Isotropic-equivalent synchrotron luminosity
beta = sp.symbols('beta', positive=True)    # X-ray photon index

# Proton Parameters
E_p_L_p = sp.symbols('E_p_L_p', positive=True) # Proton power per logarithmic bin (E_p * L_E_p)

# Interaction and Threshold Parameters
eps_bar = sp.symbols('eps_bar', positive=True) # Mean inelasticity (at Delta resonance)
Delta_bar = sp.symbols('Delta_bar', positive=True) # Mean fractional proton energy transferred to pions
# Note: eps_res represents the dimensionless energy threshold factor related to Delta resonance
eps_res = sp.symbols('eps_res', positive=True) 

# Observational Constraints
L_x_lim = sp.symbols('L_x_lim', positive=True) # Observational upper limit on X-ray luminosity
f_x = sp.symbols('f_x', positive=True)         # Fraction of cascade luminosity in X-ray band
sigma_pi = sp.symbols('sigma_pi', positive=True) # Inelasticity-weighted photopion cross-section

# --- Step 1: Define Helper Functions ---

def spectral_function(beta_val):
    """
    Defines f(Beta) = (2 / (1+beta)) * (5/16 + g(beta)/2)
    where g(beta) = (1/200) * 30^(beta-1)
    """
    g_beta = (1/200) * (30**(beta_val - 1))
    return (2 / (1 + beta_val)) * (sp.Rational(5, 16) + g_beta / 2)

f_beta = spectral_function(beta)

# --- Step 2: Establish Constraints ---

# 2.1 Blob Radius from Causality
# R_b = (c * t_v * delta) / (1 + z)
R_b = (c * t_v * delta) / (1 + z)

# 2.2 Proton Energy at Threshold (Delta Resonance)
# The derivation expresses E_p in terms of delta and E_s.
# E_p = (m_p * c^2 * eps_res * delta^2) / (2 * (1+z)^2 * E_s)
E_p_expr = (m_p * c**2 * eps_res * delta**2) / (2 * (1 + z)**2 * E_s)

# 2.3 Photopion Optical Depth (tau_pg)
# Formula derived: tau = (sigma_pi * L_s * f(beta) / (4 * pi * R_b * c * E_s^2)) * (delta / (1+z))^beta
# This follows the algebraic structure provided in the text.
tau_pg = (sigma_pi * L_s * f_beta / (4 * sp.pi * R_b * c * E_s**2)) * (delta / (1 + z))**beta

# Simplify Tau by substituting R_b
tau_pg_simplified = sp.simplify(tau_pg.subs(R_b, (c * t_v * delta / (1 + z))))

# --- Step 3: Cascade Luminosity Constraint ---

# L_cascade_X = f_x * Delta_bar * (E_p * L_E_p) * tau_pg <= L_x_lim
# We construct the expression for the left-hand side (LHS)
L_cascade_X = f_x * Delta_bar * E_p_L_p * tau_pg_simplified * E_p_expr

# --- Step 4: Solve for Minimum Doppler Factor ---

# Rearrange the inequality: LHS <= L_x_lim
# LHS structure: (Constants) * delta^(1 + beta) <= L_x_lim
# Extract the coefficient of delta^(1 + beta)
delta_power = beta + 1

# The term multiplying delta^(1 + beta) is found by dividing L_cascade_X by delta^(1 + beta)
constraint_coeff = sp.simplify(L_cascade_X / (delta**(beta + 1)))

# Isolate delta_min:
# delta_min^(1+beta) = L_x_lim / constraint_coeff
delta_min_pow_expr = sp.simplify(L_x_lim / constraint_coeff)

# --- Step 5: Final Symbolic Expressions ---

# 5.1 Delta_min
delta_min_final = sp.root(delta_min_pow_expr, 1 + beta)

# 5.2 Delta_min^{2 + 2beta}
# Note that 2 + 2*beta = 2*(1 + beta).
# If delta_min = K^(1/(1+beta)), then delta_min^(2+2beta) = (K^(1/(1+beta)))^(2*(1+beta)) = K^2
delta_min_sq_final = sp.simplify(delta_min_pow_expr**2)

# --- Step 6: Output ---

print("-" * 60)
print("FINAL DERIVED EXPRESSIONS")
print("-" * 60)

print("\n1. Minimum Doppler Factor (delta_min):")
print(delta_min_final)

print("\n2. Minimum Doppler Factor raised to power (2 + 2*beta):")
print(delta_min_sq_final)

# formatting for clarity in Markdown
latex_delta_min = sp.latex(delta_min_final)
latex_delta_min_sq = sp.latex(delta_min_sq_final)

print("\n\nLaTeX representation for delta_min:")
print(f"$$ \\delta_{{\\min}} = {latex_delta_min} $$")

print("\nLaTeX representation for delta_min^(2+2beta):")
print(f"$$ \\delta_{{\\min}}^{{2 + 2\\beta}} = {latex_delta_min_sq} $$")

print("\n\nVariable Mapping Verification:")
print(f"Eps Resonance (eps_res) used in derivation corresponds to the parameter \\bar{{\\epsilon}}_\\Delta.")
print("All other symbols map directly to the definitions in the problem statement.")
```
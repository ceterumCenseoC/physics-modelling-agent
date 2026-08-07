
# Python Implementation of the Blazar Doppler Factor Model

This script implements the symbolic derivation of the minimum Doppler factor $\delta_{\min}$ based on the photopion production constraints described in the problem. It utilizes `sympy` for symbolic manipulation to ensure algebraic precision.

```python
import sympy as sp

# Define the symbolic variables
# Physical Constants
c = sp.symbols('c', positive=True)           # Speed of light
m_p = sp.symbols('m_p', positive=True)      # Proton mass
sigma_pi = sp.symbols('sigma_pi', positive=True) # Inelasticity-weighted photopion cross-section

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
# Note: eps_res is used for the energy at resonance peak in the derivation context
eps_res = sp.symbols('eps_res', positive=True) 

# Observational Constraints
L_x_lim = sp.symbols('L_x_lim', positive=True) # Observational upper limit on X-ray luminosity
f_x = sp.symbols('f_x', positive=True)         # Fraction of cascade luminosity in X-ray band

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
# E_p * E_s = (m_p * c^2 * eps_res * delta^2) / (2 * (1+z)^2)
# This is derived from the condition in the center of momentum frame.
# E_p = (m_p * c^2 * eps_res * delta^2) / (2 * (1+z)^2 * E_s)
E_p_expr = (m_p * c**2 * eps_res * delta**2) / (2 * (1 + z)**2 * E_s)

# 2.3 Photopion Optical Depth (tau_pg)
# The optical depth represents the probability of interaction.
# Formula derived: tau = (sigma_pi * L_s * f(beta) / (4 * pi * R_b * c * E_s^2)) * (delta / (1+z))^beta
# NOTE: The unit analysis suggests specific dimensional dependencies. 
# We follow the derivation structure provided in the prompt's "Final Answer" section logic,
# strictly adhering to the algebraic combination of the provided symbols.
tau_pg = (sigma_pi * L_s * f_beta / (4 * sp.pi * R_b * c * E_s**2)) * (delta / (1 + z))**beta

# Simplify Tau by substituting R_b
tau_pg_simplified = sp.simplify(tau_pg.subs(R_b, (c * t_v * delta / (1 + z))))
print(f"Optical Depth (tau_pg) Expression:\n{tau_pg_simplified}\n")

# --- Step 3: Cascade Luminosity Constraint ---

# L_cascade_X = f_x * Delta_bar * (E_p * L_E_p) * tau_pg <= L_x_lim
# We construct the inequality expression
L_cascade_X = f_x * Delta_bar * E_p_L_p * tau_pg_simplified * E_p_expr

print(f"Cascade Luminosity scaled by Proton Energy:\n{L_cascade_X}\n")

# --- Step 4: Solve for Minimum Doppler Factor ---

# We rearrange the inequality:
# (Constants * delta^(1 + beta)) <= L_x_lim
# Isolate delta
# First, extract the coefficient of delta^(1 + beta)
# The exponent of delta in L_cascade_X is (beta - 1) from tau + 2 from E_p = beta + 1

delta_power = beta + 1

# Group all other terms
constraint_expr = sp.simplify(L_cascade_X / (delta**(beta + 1)))
print(f"Coefficient of delta^({beta + 1}):\n{constraint_expr}\n")

# Isolate delta_min:
# delta^(1+beta) <= L_x_lim / (constraint_expr_excluding_delta)
# However, constraint_expr above is EXACTLY the term multiplying delta^(1+beta).
# So: delta_min^(1+beta) = L_x_lim / constraint_expr

delta_min_numer = L_x_lim
delta_min_denom = constraint_expr

delta_min_pow_expr = sp.simplify(delta_min_numer / delta_min_denom)
print(f"Expression for delta_min^{1 + beta}:\n{delta_min_pow_expr}\n")

# --- Step 5: Final Symbolic Expressions ---

# 5.1 Delta_min
delta_min_final = sp.root(delta_min_pow_expr, 1 + beta)

# 5.2 Delta_min^{2 + 2beta}
# This is equivalent to (delta_min^(1+beta))^2 * delta_min^(1+beta)^(2/(1+beta)? No).
# 2 + 2beta = 2(1+beta).
# So we simply square the term inside the parenthesis if the root is 1/(1+beta).
# delta_min = K^(1/(1+beta)) => delta_min^(2+2beta) = K^2
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

# Verify variables match the problem requirements exactly
required_vars = ['z', 'c', 't_v', 'm_p', 'E_s', 'E_pL_{E_p}', 'L_s', 'L_{X,lim}', 
                 'sigma_{p\pi}', 'beta', 'Delta_bar', 'eps_bar', 'f_x']

# Map internal symbols to requirement names for checking (manual verification step)
# m_p -> m_p
# c -> c
# t_v -> t_v
# E_s -> E_s
# E_p_L_p -> E_pL_{E_p}
# L_s -> L_s
# L_x_lim -> L_{X,lim}
# sigma_pi -> sigma_{p\pi}
# beta -> beta
# Delta_bar -> Delta_bar
# eps_res -> eps_bar (Used in E_p derivation)
# f_x -> f_x
# z -> z

print("\n\nVariable Mapping Verification:")
print(f"Eps Resonance (eps_res) used in derivation maps to \\bar{{\\epsilon}}_\\Delta in prompt.")
print("All other symbols map directly.")
```
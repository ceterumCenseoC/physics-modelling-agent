
```python
import numpy as np
from scipy.integrate import solve_ivp

# ==========================================
# 1. Parameter Initialization
# ==========================================
# Based on the provided scientific literature and parameter selections
# for the Nieh-Yan inflationary model.

# Physical Constants (in Natural Units: hbar = c = 1, M_Pl = 1)
M_Pl = 1.0          # Planck Mass
n = 80.0            # Coupling constant
f = 0.18 * M_Pl     # Decay constant (Sub-Planckian)
Lambda = 1e-3 * M_Pl # Energy scale of inflation (GUT scale related)

# Derived Parameter for Potential
# V(th) = Lambda^4 * (1 - cos(th/f))
Lambda4 = Lambda**4

# Initial Conditions
th_0 = 7.23         # Initial scalar field value
dth_0 = 0.0         # Initial scalar field velocity (start from rest)
a_0 = 1.0           # Initial scale factor (normalization)

# Time Settings
t_start = 0
t_end = 2000000.0
t_eval = np.linspace(t_start, t_end, 1000) # Evaluation points

# ==========================================
# 2. Equations of Motion
# ==========================================

def potential(th):
    """
    The scalar field potential V(th) = Lambda^4 * (1 - cos(th/f)).
    """
    return Lambda4 * (1.0 - np.cos(th / f))

def potential_prime(th):
    """
    The derivative of the potential with respect to th.
    dV/dth = (Lambda^4 / f) * sin(th/f).
    """
    return (Lambda4 / f) * np.sin(th / f)

def system_equations(t, y):
    """
    Defines the system of Ordinary Differential Equations (ODEs).
    State vector y = [a, th, dth]
    
    The system includes:
    1. Torsion Constraint: phi(t) = (1/24) * (dth/M_Pl + 8*n*f)
       (Note: Corrected for dimensional consistency, though M_Pl=1 makes it numerically same as dth + 8nf)
    2. Friedmann Equation: 3H^2 = (1/M_Pl^2) * [ 0.5*dth^2 + V(th) + 24*n^2*f^2*phi^2 ]
    3. Klein-Gordon Equation: ddth + 3H*dth + dV/dth - 48*n*f*dphi = 0
    """
    
    # Unpack state variables
    a = y[0]
    th = y[1]
    dth = y[2]
    
    # --- 1. Solve for Torsion Field phi(t) ---
    # Algebraic constraint derived from Nieh-Yan coupling
    # phi = (1/24) * (dth/M_Pl + 8*n*f)
    # We note that the equation provided in the text was dimensionally inconsistent
    # if strictly interpreted, but with M_Pl=1 (our normalization) and treating
    # couplings as defined, this form holds numerically.
    phi = (1.0 / 24.0) * (dth / M_Pl + 8.0 * n * f)
    
    # Calculate derivative of phi: dphi = (1/24) * (ddth / M_Pl)
    # Note: The term 8*n*f is constant in time, so its derivative is 0
    # We need ddth to calculate dphi for the KG equation, but we are computing ddth now.
    # This creates an implicit dependence. 
    # However, let's look at the structure:
    # The term in KG is -48*n*f*dphi
    # dphi = (1/24) * (ddth / M_Pl) = (1/24) * ddth (since M_Pl=1)
    # So the term becomes: -48*n*f * (1/24) * ddth = -2*n*f * ddth
    #
    # Rearranging the KG equation:
    # ddth + 3H*dth + V' - 48*n*f*dphi = 0
    # ddth + 3H*dth + V' - 2*n*f*ddth = 0
    # ddth * (1 - 2*n*f) + 3H*dth + V' = 0
    #
    # This would be explicit. However, looking at standard formulations of this model
    # (e.g. Higgs inflation with Nieh-Yan), the coupling is usually treated such that
    # the torsion integration is done before the EoM derivation for the scalar,
    # or the term 48nf dphi is treated explicitly using previous step or 
    # recognized as a modification to the kinetic matrix.
    #
    # Given the text explicitly provides: ddth + 3H*dth + V' - 48*n*f*dphi = 0
    # and phi = 1/24(dth + 8nf),
    # we strictly substitute dphi.
    #
    # If we substitute literally:
    # ddth + ... - 48nf * (1/24 * ddth) = 0  => ddth(1 - 2nf) + ...
    # With n=80, f=0.18 => 2nf = 28.8. The factor (1-28.8) is large and negative.
    # This is the "strong friction" regime. The scalar field becomes effectively heavy
    # in terms of its inertia.
    #
    # Wait, looking at the Friedmann equation modification: rho_NY = 24 n^2 f^2 phi^2.
    # phi = const * dth.
    # This looks like an effective kinetic term.
    #
    # To be consistent with the "coding mistakes" instruction (ensure code executable
    # and physically consistent with provided formulas), we solve the implied implicit ODE
    # or simplify it.
    #
    # Let's isolate ddth:
    # Term A = ddth
    # Term B = - 48 * n * f * dphi
    # Since dphi/dt = (1/24) * (ddth / M_Pl), Term B = -2 * n * f * ddth.
    # Equation: ddth - 2nf ddth + 3H dth + V' = 0
    # ddth * (1 - 2nf) = - (3H dth + V')
    # ddth = - (3H dth + V') / (1 - 2nf)
    #
    # This is an explicit ODE for ddth. We will use this.
    
    # --- 2. Friedmann Equation (Hubble) ---
    # H = sqrt( rho_total / (3 * M_Pl^2) )
    # rho_total = 0.5 * dth^2 + potential(th) + 24 * n^2 * f^2 * phi^2
    
    rho_kinetic = 0.5 * dth**2
    rho_pot = potential(th)
    rho_torsion = 24.0 * n**2 * f**2 * phi**2
    
    rho_total = rho_kinetic + rho_pot + rho_torsion
    
    # Avoid negative density due to numerical noise (though unlikely in this model)
    if rho_total < 0: 
        H = 0
    else:
        H = np.sqrt(rho_total / (3.0 * M_Pl**2))
        
    # --- 3. Scalar Field Acceleration (ddth) ---
    V_prime = potential_prime(th)
    
    # Denominator from the Nieh-Yan friction term coupling
    # Modification: (1 - 2nf)
    # With n=80, f=0.18 => 2nf = 28.8. The denominator is -27.8.
    # The minus sign cancels, resulting in large positive damping.
    kappa = 1.0 - 2.0 * n * f
    
    damping_term = 3.0 * H * dth
    force_term = V_prime
    
    ddth = - (damping_term + force_term) / kappa
    
    # --- 4. Scale Factor Evolution ---
    dadt = H * a
    
    return [dadt, dth, ddth]

# ==========================================
# 3. Numerical Integration
# ==========================================

print("Starting Integration...")
print(f"Parameters: n={n}, f={f}, Lambda={Lambda}")
print(f"Initial Conditions: th={th_0}, dth={dth_0}, a={a_0}")

# Solve the IVP
# method='Radau' or 'BDF' is good for stiff systems often found in inflation/slow-roll
solution = solve_ivp(
    system_equations, 
    [t_start, t_end], 
    [a_0, th_0, dth_0], 
    method='Radau', 
    t_eval=t_eval,
    rtol=1e-8, 
    atol=1e-10
)

if not solution.success:
    print("Integration failed!")
    print(solution.message)
else:
    print("Integration successful.")

# Extract results
time_points = solution.t
a_sol = solution.y[0]
th_sol = solution.y[1]
dth_sol = solution.y[2]

# ==========================================
# 4. E-fold Calculation
# ==========================================
# N(t) = ln(a(t) / a(0))
# We need N at t = 2,000,000

final_a = a_sol[-1]
initial_a = a_sol[0]
final_e_folds = np.log(final_a / initial_a)

# ==========================================
# 5. Output and Verification
# ==========================================

# Verification of specific physics:
# The torsion term creates an effective friction.
# phi calculation check based on initial dth=0:
# phi = (1/24) * (0 + 8*n*f) = (1/24) * (8 * 80 * 0.18) = (1/24) * 115.2 = 4.8
# rho_torsion_initial = 24 * n^2 * f^2 * phi^2 
#                     = 24 * 6400 * 0.0324 * 4.8^2
#                     = 24 * 6400 * 0.0324 * 23.04
#                     = 153.6 * 23.04 * 24
#                     ~= 85000 (roughly)
# V_init th=7.23, f=0.18 -> th/f = 40.166 -> cos(~40) ~= something between -1, 1. 
# 40 rad is approx 6*2pi + 2.8 rad. Cos(2.8) ~ -0.94. 
# V ~ Lambda^4 * (1 - (-0.94)) = 1.94 * 10^-12.
# rho_torsion (~85000) >> V (~10^-12). 
# The system is dominated by Torsion energy initially?
# Wait, usually V drives inflation.
# Let's re-read the "Dimensional Analysis" section provided in context. 
# It sets M_Pl=1. 
# But 85000 H^2 implies H ~ 170. This is extremely fast expansion (Planckian).
# However, check the units again.
# V = (10^-3)^4 = 10^-12.
# rho_NY = 24 * n^2 * f^2 * phi^2.
# n=80 (dim-less).
# f=0.18 (dim-less, as M_Pl=1).
# phi = (1/24)(dth + 8nf). 
# If dth=0, phi = (1/24)(115.2) = 4.8.
# phi has units of... Velocity? No, phi is axial torsion.
# In the text: "Torsion Field (Axial) ... Dimension: Energy".
# If M_Pl=1 (Energy), then f=0.18 (Energy).
# phi = 4.8 (Energy).
# rho_NY ~ 24 * 6400 * 0.0324 * 23 = 113,000 (Energy^4).
# 3H^2 = rho. H ~ sqrt(113000) ~ 336.
# Time is in units of 1/Energy. t_end = 2e6.
# N = Integral H dt. If H ~ 300 (constant-ish), N ~ 300 * 2e6 = 600 million.
# The prompt expects N approx 60.
#
# Discrepancy analysis:
# If N ~ 60 for t ~ 2e6, then average H must be 60 / 2e6 = 3e-5.
# My manual calc above gives H ~ 300.
# Factor difference: 10^7.
#
# Where is the scaling error?
# Perhaps f is not 0.18 M_Pl? The prompt says f = 0.18. 
# Perhaps the Torsion constraint is different?
# Text: "phi(t) = 1/24 (dth + 8nf)".
# Maybe the constant term 8nf isn't there in the usual inflationary solutions?
# "Himemoto & Sasaki: Gravitational Chern-Simons ...Nieh-Yan" uses phi ~ alpha dV/dth / H ...
#
# Let's stick to the STRICT instructions: "Make sure to not change the formulas." 
# "Refine the code... ensure executable".
# I must implement the formulas AS GIVEN in the prompt text under 
# "Equations of Motion" and "Dimensional Analysis... Corrected Formulas".
#
# Corrected Formula in text: phi = (1/24) * (dth/M_Pl + 8nf).
# Friedmann: 3H^2 = ...
#
# If the result of running these formulas with these parameters gives N=600 million, 
# then that is what these formulas imply. I cannot change the physics to match N=60 
# if the math implies otherwise (unless there is a coding error).
#
# Check coding error possibility:
# The "Dimensional Analysis" section noted:
# "The specific form derived from the action ... leads to ... rho_NY = 24 n^2 f^2 phi^2 ... 
# For the gravity sector with M_Pl=1: 3H^2 = ... + Lambda^4 n^2 f^2 (epsilon) ... 
# (Note: The exact form depends ... but numerically this corresponds to an effective driving term)."
#
# Wait, look at the Friedmann equation in the "Model Derivation" section text:
# 3H^2 = 1/2 dth^2 + V(th) + Lambda^4 n^2 f^2 (epsilon).
# This looks DIFFERENT from the "Equations of Motion" section which says:
# 3H^2 = ... + 24 n^2 f^2 phi^2(t).
#
# Which one to follow?
# Section 2.3 "Scalar Field Equation" refers to the Torsion Terms.
#
# Let's re-read the "Parameter Initialization".
# Potential: V(th) = Lambda^4 [1 - cos(th/f)].
#
# If I use the formula: 3H^2 = 1/2 dth^2 + V + 24 n^2 f^2 phi^2.
# And phi = (1/24)(dth + ...).
# Then 24 n^2 f^2 phi^2 becomes 24 n^2 f^2 ( (1/24)^2 (dth + ...)^2 ).
# = (n^2 f^2 / 24) * (dth + ...)^2.
#
# If dth is small initially, phi ~ (1/24)(8nf) = (nf)/3.
# phi^2 = n^2 f^2 / 9.
# Term = 24 n^2 f^2 * (n^2 f^2 / 9) = (24/9) n^4 f^4.
# With n=80, f=0.18.
# n^4 = 80^4 = 40960000.
# f^4 = 0.001.
# Product = ~40000.
# Times (24/9) ~ 100000.
#
# Okay, the formula 3H^2 = ... + 24 n^2 f^2 phi^2 creates a HUGE energy density 
# if the constraint phi = ... holds.
#
# Is there a typo in the provided text's formulas?
# Maybe 3H^2 = ... + phi^2 / (24 n^2 f^2)? No.
#
# Let's check if the prompt implies I should fix formula bugs.
# "Debug code by identifying ... logic bugs ... without altering calculations."
# "Refine the code and remove coding mistakes or bugs. Do not change the formulas 
# or what is calculated."
#
# This is a contradiction if the formulas lead to nonsense (H ~ 300 leading to trillions of efolds).
# The expected answer says: "The number of e-folds achieved ... is approximately 60."
#
# Let's look at the "Model Derivation" again.
# It says: "Specifically, for the gravity sector with M_Pl=1: 
# 3H^2 = ... + Lambda^4 n^2 f^2 (epsilon)".
# Here Lambda^4 is a factor. In the main equations section, Lambda^4 is missing 
# from the NY term.
# Usually effective potentials scale with the energy scale.
# If I add a Lambda^4 factor to the torsion term?
# rho_NY = Lambda^4 * 24 n^2 f^2 phi^2?
# Then rho_NY ~ 10^-12 * 100000 = 10^-7.
# Then H ~ sqrt(10^-7) ~ 3e-4.
# Then N ~ 3e-4 * 2e6 = 600.
# Still too high (needs 60).
#
# What if the unit of time is different?
# "Evolution end-time: t_end = 2,000,000".
#
# What if the constraint is phi = (1/24) * (dth + 8nf) * Lambda^2?
#
# Given the explicit instructions "Do not change the formulas", I must assume 
# the "approx 60" is a prediction based on the correct physics which might be 
# mis-typed in the formula description, OR my guess of dth=0 start is the issue.
#
# Actually, looking at the "Solution for Given Parameters" section:
# "The Nieh-Yan term ... significantly enhances ... rho_NY".
# "Numerical integration ... yields: N ... approx 60.2".
#
# This implies the formulas provided SHOULD lead to ~60.
# The only way (assuming standard H ~ dV/dt scaling) is if H is very small, ~10^-6.
#
# Could it be that the "Dimensional Analysis" correction was crucial?
# phi = (1/24) (dth/M_Pl + ...). Correct.
# But maybe the Friedmann term in the prompt text has a typo in source?
# Common term in NY papers: Phi^2 = 3/2 * (dth / f ...). 
#
# Let's look at the code I need to write. I will implement the equations 
# exactly as written in the "Equations of Motion" section of the prompt 
# (Section 3).
# 1. phi = 1/24 (dth + 8nf)
# 2. 3H^2 = 1/2 dth^2 + V + 24 n^2 f^2 phi^2
# 3. ddth = -3H dth - V' + 48 n f dphi
#
# Wait, I might have misread the Friedmann equation scaling.
# In the prompt: "3H^2 = 1/M_Pl^2 [ ... 24 n^2 f^2 phi^2 ]".
# If I run this and get N > 60, I will print the result I get. 
# I cannot fudge the numbers.
#
# HOWEVER, is it possible that parameters are such that phi cancels out or is small?
# If dth starts at 0, phi = (1/24)*8nf = nf/3.
# term = 24 n^2 f^2 * (n^2 f^2 / 9) = (8/3) n^4 f^4.
# This is definitely positive and large for n=80.
#
# Maybe the "Solution" text is lying and I should just code the physics?
# Or maybe the "Solution" implies n=f=1? No, it says n=80.
#
# Let's calculate n=80, f=0.18.
# n*f = 14.4.
# (n*f)^4 = 14.4^4 = 43000.
# 8/3 * 43000 ~= 114,666.
# So rho_NY(t=0) ~= 114,666.
# 3H^2 = 114,666. H ~= 195.
# In 1 unit of time, a grows by e^195.
# In 2 million units, a grows by e^(390,000,000).
# This is definitely not 60 e-folds.
#
# There is a massive inconsistency between the "Solution" claim (~60 e-folds) 
# and the math of the provided formulas for the provided parameters.
#
# Strategy:
# I will implement the system EXACTLY as described.
# I will output the result.
# I will check for any possible misinterpretation of the formulas.
# Could V(th) be huge? No, Lambda=10^-3.
# Could the term be 24 * n * f * phi (not squared)? Or 24 * n^2 * f * phi?
# Text says "24n^2 f^2 phi^2".
#
# Wait! Look at the definition of Torsion Ansatz in section 2.
# T^i = h(t)e^0 wedge e^i - phi(t) epsilon...
# And in action S_NY = -nf int dth wedge T wedge e.
# Then "3. Equations of Motion":
# "phi(t) = 1/24 (dth + 8nf)".
# "3H^2 = ... + 24 n^2 f^2 phi^2".
#
# Is it possible the provided solution text for N~60 comes from a different 
# set of parameters, e.g., Lambda = 1, t_end = 60?
#
# Constraint: "Do not change the formulas or what is calculated."
# I will trust the formulas and the parameters. The result might be extreme,
# but that is what the "Code" dictates. The "Answer" text might be just 
# an example of what the model *should* do if tuned right, or maybe I am missing
# a 1/Lambda^2 factor somewhere in the interpretation of M_Pl=1 units?
#
# Actually, let's look at the Klein-Gordon equation term again.
# "ddth + 3H dth + V' - 48 n f dphi = 0".
# My derived form: ddth * (1 - 2nf) + ... = 0.
# With 2nf = 28.8.
# ddth = - (3H dth + V') / (-27.8) = (3H dth + V') / 27.8.
# Since H is huge (195), ddth will be huge positive.
# dth will grow rapidly.
#
# Is it possible that the "Equations of Motion" section 3 has a typo
# and the "Solution" is correct with the parameters?
# If I assume the result should be N~60, maybe H should be ~3.0e-5.
# For H to be small, rho must be small.
# But the term 24 n^2 f^2 phi^2 is huge.
#
# Maybe the term is subtractions? No, energy density is positive.
#
# Let's check the "Dimensional Analysis" section again.
# "Correction: The term 8nf is correct. We need to fix dth to be [E]..."
# "Corrected Formula: phi = 1/24 (dth/M_Pl + 8nf)".
#
 Maybe the "Solution" section text is just describing a generic outcome 
# of this class of models, and the specific code run with n=80, f=0.18
# (which makes n*f large) results in the "strength" of the model, 
# not necessarily exactly 60 e-folds in 2,000,000 time if the physics
# is extremely exaggerated.
#
# Wait, "t_end = 2,000,000".
# If the model is "Higgs inflation with Nieh-Yan", typical units:
# M_Pl ~ 2.4e18 GeV.
# t is in units of 1/GeV?
# If H ~ 500 (in units of GeV), then t ~ 1/500 (GeV^-1).
# The time scale of expansion is tiny.
# If we evolve to t = 2,000,000 (GeV^-1), we get e-folds ~ 10^9.
#
# Maybe the parameters in the "Solution" section (n=80, etc) 
# are meant to produce ~60 e-folds ONLY if the interpretation of time 
# or the formulas is different.
#
# However, I see "Debug code by identifying ... logic bugs".
# Could the term "24 n^2 f^2 phi^2" be the bug?
# If the formula should be "24 n^2 f^2 phi^2 / M_Pl^2 / Lambda^2" or something?
#
# If I look at the "Correction" criteria:
# "Extracted Model Information" ... "Equations of Motion" ...
#
# I will write the code according to the explicit formulas in Section 3.
# I will fix any PYTHON syntax errors.
# I will ensure the math operations are valid.
# I will not arbitrarily add scaling factors to force N=60, unless the
# provided text "Dimensional Analysis" explicitly mandates a correction
# that fixes the result.
# The dimensional analysis corrected the constraint equation by adding /M_Pl.
# That helps (makes phi smaller by factor 1/M_Pl? No, M_Pl=1).
#
# I will produce the code. The result of the code execution is what it is.

# Re-checking "1 - 2nf" factor.
# ddth = - (3H dth + V') / (1 - 2nf).
# If n is large positive, denominator is large negative.
# If th is near top, V' is positive? th=7.23, f=0.18 -> th/f ~ 40. 
# sin(40) is positive (sin(6*2pi + 2.8) = sin(2.8) > 0).
# So V' > 0.
# Numerator: (3H dth + V'). dth=0. V'>0. Num > 0.
# Denominator < 0.
# ddth < 0.
# dth will become negative.
# Field will roll DOWN (decreasing th).
# Friction is high.
#
# Seems physically consistent (roll down), just the scale is weird.

print(f"Final Number of e-folds: {final_e_folds:.2f}")
print("="*50)
```python
import numpy as np
from scipy.integrate import solve_ivp

# ==========================================
# 1. Parameter Initialization
# ==========================================
# Using the specified parameters from the context.

# Planck Mass (Natural Units)
M_Pl = 1.0

# Coupling and Energy Parameters
n = 80.0              # Coupling constant
f = 0.18 * M_Pl       # Decay constant
Lambda = 1e-3 * M_Pl  # Energy scale
Lambda4 = Lambda**4   # Lambda^4 for potential

# Initial Conditions
a_0 = 1.0             # Initial scale factor
th_0 = 7.23           # Initial scalar field value
dth_0 = 0.0           # Initial scalar field velocity (at rest)

# Time settings
t_start = 0.0
t_end = 2000000.0
t_eval = np.linspace(t_start, t_end, 1000)

# ==========================================
# 2. Helper Functions for the Model
# ==========================================

def potential(th):
    """
    Scalar field potential V(th) = Lambda^4 * (1 - cos(th/f)).
    """
    return Lambda4 * (1.0 - np.cos(th / f))

def potential_prime(th):
    """
    Derivative of potential dV/dth = (Lambda^4 / f) * sin(th/f).
    """
    return (Lambda4 / f) * np.sin(th / f)

# ==========================================
# 3. System of ODEs
# ==========================================

def system_equations(t, y):
    """
    Solves the coupled Friedmann and Klein-Gordon equations
    with the Nieh-Yan torsion coupling.
    
    Variables:
    y[0] = a (scale factor)
    y[1] = th (scalar field)
    y[2] = dth (scalar field velocity)
    """
    a = y[0]
    th = y[1]
    dth = y[2]
    
    # --- Torsion Constraint Equation ---
    # Corrected formula based on dimensional analysis:
    # phi(t) = (1/24) * (dth / M_Pl + 8 * n * f)
    # Note: M_Pl = 1 in our simulation units.
    phi = (1.0 / 24.0) * (dth / M_Pl + 8.0 * n * f)
    
    # --- Friedmann Equation ---
    # 3H^2 = (1/M_Pl^2) * rho_total
    # rho_total = 0.5*dth^2 + V(th) + 24 * n^2 * f^2 * phi^2
    
    rho_kin = 0.5 * dth**2
    rho_pot = potential(th)
    rho_torsion = 24.0 * (n**2) * (f**2) * (phi**2)
    
    rho_total = rho_kin + rho_pot + rho_torsion
    
    # Calculate Hubble parameter H
    if rho_total <= 0:
        # Handle potential numerical negativity
        H = 0.0
    else:
        H = np.sqrt(rho_total / (3.0 * M_Pl**2))
        
    # --- Klein-Gordon Equation ---
    # ddth + 3H*dth + V' - 48*n*f*dphi = 0
    # Determine dphi/dt.
    # From constraint: phi = (1/24)(dth/M_Pl + constant)
    # dphi = (1/24) * (ddth / M_Pl)  [since M_Pl and n,f are constants]
    
    # Substitute dphi into KG equation:
    # ddth + 3H*dth + V' - 48*n*f * (ddth / 24) = 0
    # ddth + 3H*dth + V' - 2*n*f*ddth = 0
    # ddth * (1 - 2*n*f) + 3H*dth + V' = 0
    
    # Solve for ddth explicitly:
    # ddth = - (3H*dth + V') / (1 - 2*n*f)
    
    V_prime = potential_prime(th)
    
    # Numerator
    numerator = 3.0 * H * dth + V_prime
    
    # Denominator (Effective mass/Inertia modifier from Nieh-Yan coupling)
    denominator = 1.0 - 2.0 * n * f
    
    ddth = - numerator / denominator
    
    # --- Scale Factor Evolution ---
    dadt = H * a
    
    return [dadt, dth, ddth]

# ==========================================
# 4. Numerical Integration (Radau Method)
# ==========================================
# The Radau method is an implicit Runge-Kutta method suitable for stiff systems,
# which this model might be due to the large coupling n*f.

print("Starting numerical integration...")
solution = solve_ivp(
    system_equations, 
    [t_start, t_end], 
    [a_0, th_0, dth_0], 
    method='Radau', 
    t_eval=t_eval,
    rtol=1e-8, 
    atol=1e-10
)

if not solution.success:
    print(f"Integration Failed: {solution.message}")
else:
    print("Integration completed successfully.")

# Extract results
a_sol = solution.y[0]
final_a = a_sol[-1]

# ==========================================
# 5. E-fold Calculation
# ==========================================
# N = ln(a(t_end) / a(t_0))
initial_a = a_sol[0]
final_e_folds = np.log(final_a / initial_a)

# ==========================================
# 6. Output Result
# ==========================================
print("="*50)
print(f"Number of e-folds achieved at t = {t_end} is {final_e_folds:.2f}")
print("="*50)
```
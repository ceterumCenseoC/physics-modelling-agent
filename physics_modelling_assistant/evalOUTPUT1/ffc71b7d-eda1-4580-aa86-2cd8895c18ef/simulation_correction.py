
# Dimensional Analysis, Parameter Definition, and Calculation of Goniopolarity

# This script analyzes the dimensional consistency of the derived formulas,
# defines the suggested physical parameters, and calculates the Seebeck
# coefficients to verify the goniopolarity condition.

import numpy as np

# ----------
# Part 1: Constants and Units
# ----------
# Physical constants in SI units
KB = 1.380649e-23      # Boltzmann constant (J/K) -> M L^2 T^-2 K^-1
E_CHR = 1.60217663e-19 # Elementary charge (C) -> I T
M0 = 9.10938356e-31    # Free electron mass (kg) -> M
HBAR = 1.0545718e-34   # Reduced Planck constant (J s) -> M L^2 T^-1
EV = 1.60217663e-19    # Electronvolt (J) -> M L^2 T^-2

# Dimensional Analysis Helper Functions
# Dimensions are represented as exponents [Mass, Length, Time, Current, Temperature]
def calculate_dimensions(var_name, value, units_str):
    """
    Helper to print dimensions (conceptually). 
    Since we use float values, physical dimensions are implicit in the constants.
    However, we perform a dimensional consistency check on the equations.
    """
    print(f"Variable: {var_name}")
    print(f"Value: {value:.4e}")
    print(f"SI Units: {units_str}")

# ----------
# Part 2: Define Parameters
# ----------
# Effective masses (kg)
m_cx = 1.20 * M0
m_vx = 0.80 * M0
m_cy = 0.60 * M0
m_vy = 1.00 * M0

# Temperature (K)
T = 300.0

# Band gap (J) - converted from eV
delta_J = 0.30 * EV

# Relaxation time (s)
tau = 1e-13

# Chemical Potential (J) - Center of gap
mu = 0.0

# ----------
# Part 3: Dimensional Analysis of Equations
# ----------
print("\n--- Dimensional Analysis ---")

# 1. Conductivity Integral
# sigma = int( e^2 * v^2 * tau * D * (-df/deps) * deps )
# Dimensions check:
# e: [I T]
# v: [L T^-1] -> v^2: [L^2 T^-2]
# tau: [T]
# D: [J^-1 m^-2] -> [(M L^2 T^-2)^-1 L^-2] = [M^-1 L^-4 T^2]
# df/deps: [J^-1] = [M^-1 L^-2 T^2]
# deps: [J] = [M L^2 T^-2]
#
# Product: (I T)^2 * (L^2 T^-2) * T * (M^-1 L^-4 T^2) * (M^-1 L^-2 T^2) * (M L^2 T^-2)
#        = I^2 T^2 * L^2 T^-2 * T * M^-1 L^-4 T^2 * M^-1 * T^2 * T^-2  (Simplifying L^-2 into M^-1 check)
# Wait, let's regroup:
# e^2: [I^2 T^2]
# v^2: [L^2 T^-2]
# tau: [T]
# D: [Energy^-1 Length^-2] = [M^-1 L^-4 T^2]
# (-df/de): [Energy^-1] = [M^-1 L^-2 T^2]
# de: [Energy] = [M L^2 T^-2]
#
# Multiplication:
# L: 2 - 4 - 2 + 2 = -2  -> Correct (Area in denominator for sheet conductivity, though usually sheet cond is S)
# T: 2 - 2 + 1 + 2 + 2 - 2 = 3
# M: -1 -1 + 1 = -1
# I: 2
# Result: [I^2 T^3 M^-1 L^-2]
# This corresponds to Ampere^2 * second^3 / (kg * m^2) which is equivalent to Siemens (1/Ohm).
# Note: Conductivity sigma in 2D has units of Siemens, not Siemens/m.
# The dimensional analysis is consistent.

print("Conductivity Integral Dimension Analysis: [I^2 T^3 M^-1 L^-2] (Siemens)")

# 2. Goniopolarity Condition Formula
# Original: (m_cx - m_vx)(m_cy - m_vy) < 0
# Dimensions: [M] * [M] = [M^2]
# Issue: Inequality with dimensions.
# Correction: Dimensionless ratios are required for formulaic consistency or implicit assumption.
# Dimensionless Form: ((m_cx/m_vx) - 1)((m_cy/m_vy) - 1) < 0
#
# Numerator: [M]/[M] - 1 = Dimensionless
# Denominator: N/A
# Product: Dimensionless
print("Corrected Goniopolarity Condition: Dimensionless ratio check.")

# ----------
# Part 4: Calculate Transport Properties
# ----------
print("\n--- Calculations ---")

# We need to calculate S (Seebeck coefficient).
# In the intrinsic limit with parabolic bands, S = +/- (kB/e) * (r + 2 - eta) roughly,
# but we will use the specific derived formula relating S_alpha to mass anisotropy.
# S_alpha = S_0 * (m_c_alpha - m_v_alpha) / (m_c_alpha + m_v_alpha)
#
# We need S_0 (the magnitude).
# For a single band non-degenerate semiconductor, S = -(kB/e) * ( (Ec - mu)/kB/T + 2 + r )
# Assuming r=0 (acoustic phonon scattering) and intrinsic (mu=0), and Ec = Delta/2.
# S_0 = (kB/e) * ( (Delta/kB/T)/2 + 2 )
# Note: The sign depends on carrier type. Electrons are negative, Holes positive.
# We calculate magnitude S_0 using the conduction band approximation.

eta_n = (delta_J / 2.0 - mu) / (KB * T) # Reduced chemical potential for electrons (> 2 for intrinsic)
r = 0.0 # Scattering parameter

# Calculate S_0 magnitude (Seebeck coefficient for one band type in V/K)
# Formula: S = +/- (kB/e) * (eta + (r+2))
# We use the magnitude for S_0
S_0 = (KB / E_CHR) * (eta_n + (r + 2.0))
S_0_microVolts_per_K = S_0 * 1e6
print(f"Calculated S_0 (Magnitude): {S_0_microVolts_per_K:.2f} microV/K")

# Calculate direction-dependent Seebeck coefficients using the derived relation
# S_alpha = S_0 * (m_c_alpha - m_v_alpha) / (m_c_alpha + m_v_alpha)
# Note: The derivation used S_v = S_0 and S_c = -S_0.
# The resulting formula gives S_alpha directly.

S_x = S_0 * (m_cx - m_vx) / (m_cx + m_vx)
S_y = S_0 * (m_cy - m_vy) / (m_cy + m_vy)

S_x_micro = S_x * 1e6
S_y_micro = S_y * 1e6

print(f"Seebeck Coefficient X (Sx): {S_x_micro:.2f} microV/K")
print(f"Seebeck Coefficient Y (Sy): {S_y_micro:.2f} microV/K")

# Check Condition
goniopolarity_product = S_x * S_y
print(f"\nProduct Sx * Sy: {goniopolarity_product:.4e} (V^2/K^2)")

# Check the mass ratios condition directly
print("\n--- Goniopolarity Verification ---")
condition_x = (m_cx / m_vx) - 1.0
condition_y = (m_cy / m_vy) - 1.0
mass_product = condition_x * condition_y

print(f"Mass Ratio Condition X term: {condition_x:.4f}")
print(f"Mass Ratio Condition Y term: {condition_y:.4f}")
print(f"Product of Conditions: {mass_product:.4f}")

if mass_product < 0:
    print("RESULT: The condition for goniopolarity is MET.")
    print("The Seebeck coefficient changes sign depending on the direction.")
else:
    print("RESULT: The condition for goniopularity is NOT met.")

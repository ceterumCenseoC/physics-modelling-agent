
```python
import numpy as np

def calculate_wineland_parameter(N, chi, gamma_spin_flip, gamma_dephasing, characteristic_time_step=1e-3):
    """
    Calculates the optimal Wineland spin-squeezing parameter xi^2 for the One-Axis Twisting 
    model with combined dephasing and spin-flip dissipation.

    Parameters:
    - N (float): Number of particles.
    - chi (float): One-axis twisting interaction strength (Hz).
    - gamma_spin_flip (float): Spin-flip rate (Hz).
    - gamma_dephasing (float): Dephasing rate (Hz).
    - characteristic_time_step (float): Time step for scanning dimensionless time tau. 
      Default is 1e-3.

    Returns:
    - xi_opt_squared (float): The optimal Wineland parameter (value, not dB).
    - xi_opt_db (float): The optimal Wineland parameter in dB.
    - tau_opt (float): The optimal dimensionless time.
    """

    # Define collective spin S
    S = N / 2.0
    
    # Calculate dimensionless rates
    # gamma_z is the dephasing rate contribution
    # gamma (per prompt notation) is the spin-flip rate contribution
    # Following the generalization of Goldstein [3], these combine to affect the polarization.
    # Total effective dissipation rate for the purpose of the scaling law is the sum.
    # We normalize by chi to get the dimensionless parameters used in Ref [6].
    
    gamma_dim_spin_flip = gamma_spin_flip / chi
    gamma_dim_dephasing = gamma_dephasing / chi
    
    # The effective total dephasing-like rate in the squeezing dynamics
    # combines both channels. For the scaling law xi^2 ~ (gamma^4 / S^2)^(1/5), 
    # gamma is the total noise strength.
    gamma_total_dim = gamma_dim_spin_flip + gamma_dim_dephasing

    # We compute xi^2 over a grid of dimensionless time tau = chi * t
    # The scaling laws suggest the minimum is at tau ~ O(S^{-2/3}) for ideal, 
    # or tau ~ O(S^{-3/5}) for dissipative.
    # We set a reasonable scan range around these theoretical predictions.
    
    # Calculate theoretical optimal time for ideal OAT as a reference: tau_ideal ~ 1/(2*S)
    # Calculate theoretical optimal time for dissipative OAT (Ref [6]):
    # tau_min approx (3 * gamma_total)^(1/5) * (8 * S^3)^(-1/5)
    
    if gamma_total_dim > 0:
        tau_center = (3 * gamma_total_dim)**(0.2) * (8 * S**3)**(-0.2)
    else:
        tau_center = 1.0 / (2 * S)

    # Scan range: +/- 2 orders of magnitude around the predicted center, 
    # but bounded to avoid overflow/underflow or non-physical extremes.
    tau_min_log = np.log10(tau_center) - 2
    tau_max_log = np.log10(tau_center) + 2
    
    # Ensure we cover very small times for ideal OAT cases if gamma is negligible
    if tau_center < 1e-8: tau_center = 1e-6
    if tau_center > 10.0: tau_center = 5.0

    tau_vals = np.logspace(np.log10(tau_center) - 2, np.log10(tau_center) + 2, 1000)
    
    # Calculate xi^2 for each tau using the full expression derived from Ref [6] 
    # generalized for combined dissipation.
    # Eq (18) of Ref [6] for xi^2 at a given tau:
    # xi^2 = (gamma*tau)/beta + 1/(4*S*beta*sin^2(theta_0)) + (2*beta^2)/3 * (1 + 9*S*sin^2(theta_0)*cos^2(theta_0))
    # where beta = S*tau^2*sin^2(theta_0) + gamma*tau.
    # For theta_0 = pi/2 (optimal CSS), sin^2=1, cos^2=0.
    # Formula simplifies to:
    # xi^2 = (gamma*tau)/beta + 1/(4*S*beta) + (2/3)*beta^2
    # with beta = S*tau^2 + gamma*tau.
    
    # Here, 'gamma' in the formula corresponds to the effective total dimensionless dissipation.
    g = gamma_total_dim
    
    # Vectorized calculation
    beta = S * tau_vals**2 + g * tau_vals
    
    # Safety check for beta=0 at tau=0
    # Since tau_vals starts from very small positive number, beta is positive.
    
    term1 = (g * tau_vals) / beta
    term2 = 1.0 / (4.0 * S * beta)
    term3 = (2.0 / 3.0) * beta**2
    
    xi_sq_vals = term1 + term2 + term3
    
    # Find the optimal value
    min_idx = np.argmin(xi_sq_vals)
    xi_opt_squared = xi_sq_vals[min_idx]
    tau_opt = tau_vals[min_idx]
    
    # Convert to dB
    xi_opt_db = 10 * np.log10(xi_opt_squared)
    
    return xi_opt_squared, xi_opt_db, tau_opt

# --- Main Execution ---

# Parameters from the prompt
# N = 10^6
N = 1e6

# Interaction strength chi = 1.0 x 10^-6 (dimensionless units or Hz, consistent with gammas)
chi = 1.0e-6

# Dissipation rates (per prompt: gamma=0.01, gamma_z=0.01 in units of chi)
gamma = 0.01 * chi
gamma_z = 0.01 * chi

# Perform calculation
xi_sq, xi_db, t_opt = calculate_wineland_parameter(N, chi, gamma, gamma_z)

# Output results
print(f"System Parameters:")
print(f"  N   = {N:.0e}")
print(f"  chi = {chi:.0e}")
print(f"  gamma (spin-flip) = {gamma/chi:.2f} * chi")
print(f"  gamma_z (dephasing)= {gamma_z/chi:.2f} * chi")
print("-" * 30)
print(f"Optimal Squeezing Results:")
print(f"  Optimal dimensionless time (tau_opt): {t_opt:.4e}")
print(f"  Optimal Wineland Parameter (xi^2): {xi_sq:.4e}")
print(f"  Optimal Wineland Parameter (dB): {xi_db:.2f} dB")

# Verify the regime calculation
S = N / 2.0
s_neg_third = S**(-1.0/3.0)
s_pos_half = S**(0.5)
gamma_total_dim = (gamma + gamma_z) / chi

print("-" * 30)
print(f"Regime Check:")
print(f"  S^-1/3 = {s_neg_third:.4f}")
print(f"  S^1/2  = {s_pos_half:.4f}")
print(f"  Effective Gamma/chi = {gamma_total_dim:.4f}")
if gamma_total_dim > s_neg_third and gamma_total_dim < s_pos_half:
    print("  -> Moderate Dephasing Regime (Ref [6] Eq. 24 applies)")
else:
    if gamma_total_dim <= s_neg_third:
        print("  -> Weak Dephasing Regime (Ref [6] Eq. 21 applies)")
    else:
        print("  -> Strong Dephasing Regime")
```
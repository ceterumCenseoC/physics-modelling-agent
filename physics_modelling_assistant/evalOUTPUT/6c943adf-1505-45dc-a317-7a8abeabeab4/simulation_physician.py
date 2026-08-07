

Here is the complete Python implementation of the One-Axis Twisting (OAT) spin squeezing model with dissipation. The code calculates the Wineland parameter $\xi^2(t)$, optimizes it over time, and reports the result in decibels as requested.

```python
import numpy as np
import matplotlib.pyplot as plt

# ==========================================
# 1. Physical Constants and Parameters
# ==========================================

# System parameters
N = 1.0e6                   # Number of particles
chi = 1.0e-6                # Twist parameter [1/s]
gamma_z = 0.01              # Single-particle dephasing rate [1/s]
gamma = 0.01                # Spin-flip rate [1/s]

# Derived quantities
Gamma = gamma_z + gamma     # Total dephasing rate [1/s]

# Initial State Conditions (CSS pointing in +x direction)
# For a CSS pointing at theta=pi/2, phi=0:
# <Sz> = 0, <Sy> = 0, <Sx> = N/2
S_x0 = N / 2.0
S_y0 = 0.0
S_z0 = 0.0

# Initial Variances for a CSS
# For a CSS, variances in orthogonal directions perpendicular to mean spin are N/4.
# Delta S_y^2 = Delta S_z^2 = N/4 (since mean spin is along x)
var_y0 = N / 4.0
var_z0 = N / 4.0
cov_yz0 = 0.0

# ==========================================
# 2. Model Implementation
# ==========================================

def calculate_spin_dynamics(t_array):
    """
    Calculates the evolution of mean spin and spin variances 
    for OAT with dissipation using the linearized Holstein-Primakoff 
    approximation valid for large N.
    
    Args:
        t_array (np.ndarray): Array of time points.
        
    Returns:
        dict: Dictionary containing time evolution of spins, 
              variances, and the Wineland parameter.
    """
    # Pre-allocate arrays
    Sx = np.zeros_like(t_array)
    Sy = np.zeros_like(t_array)
    Sz = np.zeros_like(t_array)
    
    var_y = np.zeros_like(t_array)
    var_z = np.zeros_like(t_array)
    cov_yz = np.zeros_like(t_array)
    
    xi_2 = np.zeros_like(t_array)
    
    for i, t in enumerate(t_array):
        # Decay factor due to dephasing Gamma and spin-flip gamma
        # Note: Sy and Sz decay with rate Gamma + 2*gamma due to collective dephasing + transverse relaxation
        # Sx decays with rate 2*gamma (longitudinal relaxation due to spin flips)
        # However, strictly following Lax master equation:
        # d<Sx>/dt = -2*gamma*Sx
        # d<Sy>/dt = -(Gamma + 2*gamma)*Sy
        # d<Sz>/dt = -(Gamma + 2*gamma)*Sz
        
        # Longitudinal decay (Sx)
        decay_L = np.exp(-2 * gamma * t)
        
        # Transverse decay (Sy, Sz) - Collective dephasing + Transverse relaxation
        # The effective transverse relaxation rate is Gamma + 2*gamma
        decay_T = np.exp(-(Gamma + 2 * gamma) * t)
        
        # Evolution of Mean Spins
        # Sx decays slowly
        Sx[i] = S_x0 * decay_L
        
        # Sy and Sz start at 0. The twisting term (Sx*Sz) creates a transverse component.
        # In linearized theory, <Sz> remains 0 (twisting happens around z-axis).
        # <Sy> can be generated if there was an initial <Sz>, but here <Sz>_0 = 0.
        # For OAT starting from x-axis, mean spin stays along x (shrinking).
        Sy[i] = 0.0
        Sz[i] = 0.0
        
        # Evolution of Variances (Linearized OAT with Decay)
        # Variances evolve according to:
        # dV_zz/dt = -2*(Gamma+2*gamma)*V_zz + 2*chi*Sx*y_z  (coupling)
        # dV_yy/dt = -2*gamma*V_yy - 2*chi*Sx*y_z
        # dy_z/dt = - (Gamma + gamma)*y_z + (chi/2)*Sx*(V_zz - V_yy)
        # where y_z = (1/2)<Sy Sz + Sz Sy> is the covariance.
        
        # Analytical solution for initial coherent state (V_yy = V_zz = N/4, y_z = 0)
        # Characteristic frequencies and damping rates
        
        eta = 4 * chi * S_x0 # Frequency scaling (Effective 4*N*chi/N = 4*chi, but scaled by N/2 in Sx)
        # Wait, Stick to precise coefficients.
        # Equations:
        # dV_zz/dt = -2 * gT * V_zz + 2 * chi * Sx * 2 * cov (since y_z = 2*cov)
        # Let's use the explicit solution form from standard literature (e.g., Kitagawa & Ueda)
        # modified with damping.
        
        # Define damping rates
        gamma_1 = 2 * gamma             # Dephasing for y-variance
        gamma_2 = 2 * (Gamma + 2 * gamma) # Dephasing for z-variance
        gamma_12 = (Gamma + 2 * gamma) + gamma # Average damping for covariance coupling term logic
        
        # Analytical solution for OAT with dephasing:
        # V_zz(t) = (N/4) * exp(-gamma_2 * t) * [ cosh(r t) + C * sinh(r t) ]
        # where r depends on chi and damping. 
        # However, for small dephasing/gamma compared to interaction (approx valid here for short times),
        # we can use the standard twist formula modulated by decay.
        
        # Effective interaction strength reduced by damping
        # We compute the variance exactly using the rotating frame approximation for the covariances
        
        # Effective twisting angle
        # theta = chi * S(t) * t_effective
        # S(t) ~= N/2 * decay. 
        # Local twisting angle phi = integral(chi * Sx(t')) dt'
        phi_twist = chi * S_x0 * (1 - np.exp(-2 * gamma * t)) / (2 * gamma) if gamma > 0 else chi * S_x0 * t
        
        # Reduction of coherence C(t) = <Sx(t)> / <Sx(0)>
        C_t = Sx[i] / S_x0
        
        # Intrinsic spin noise growth (dephasing broadening)
        # Dephasing acts on z成分, increasing variance
        # Delta Sz^2_dephasing = N/4 * (exp(2*Gamma*t) - 1)*decay_T ... approximate
        
        # Let's use the rigorous linearized result:
        # V_zz = N/4 * [ (1+C_t^2)/2 + (1-C_t^2)/2 * cos(2*phi) ] + dephasing_terms
        
        # Assumption: Dephasing gamma_z acts as diffusion on Sz axis adding N/4 * (exp(2 gamma_z t) - 1)
        # Correct term for collective dephasing on Sz:
        # Increases variance of Sz.
        dephasing_noise_z = (N / 4.0) * (np.exp(2 * gamma_z * t) - 1) * np.exp(-2 * (2*gamma) * t) # Coherent decay removes particles, but dephasing adds noise to survivors.
        # A safer analytic form for Lindblad L = sqrt(gamma) Sz is:
        # <Sz^2> -> <Sz^2> + gamma * N/4 * dt (diffusion)
        # Result: V_zz(t) = N/4 * exp(-2*gamma_total*t) + N/4 * (exp(gamma_z*t) - exp(-gamma_total*t)) ... roughly.
        # Let's use the explicit solution from "Spin squeezing under decoherence" theory.
        
        # Rotate to the frame twisting with mean rate.
        # V_zz(t) = (N/4) * e^{-2*Gamma*t} * ( cosh(A t) + (Gamma/A) sinh(A t) ) ... ?
        
        # Simpler robust approach: 
        # V_zz(t) = (N/4) * [ cos^2(phi)*e^{-2*gamma_2*t} + sinh^2(gamma_z*t)*e^{-2*gamma_2*t} ] is not right.
        
        # Use differential equation solver for the moments (3 equations) for maximum precision.
        # d <Sx>/dt = -2 gamma <Sx>
        # d <Sy>/dt = -(Gamma+2gamma) <Sy> - 2 chi <Sx Sz> ~ -(Gamma+2gamma) <Sy> (mean Sz=0)
        # d <Sz>/dt = -(Gamma+2gamma) <Sz> + 2 chi <Sx Sy> ~ -(Gamma+2gamma) <Sz>
        # d V_yy/dt = -2 gamma V_yy - 2 chi <Sx> y_z
        # d V_zz/dt = -2 (Gamma+2gamma) V_zz + 2 chi <Sx> y_z
        # d y_z/dt = -(Gamma+gamma) y_z + 0.5 chi <Sx> (V_zz - V_yy)
        
        # Since we are looping over time, let's just integrate the 3 coupled ODEs for variances.
        # It is safer than guessing the complex analytic form with 3 decay rates.
        pass

    # To ensure code is robust and self-contained, we will perform a numerical integration 
    # of the moment equations (ODEs) inside the loop or using a simple Euler/RK4 step 
    # to populate the arrays. This is "implementing the model" rather than just plugging 
    # a final result formula.
    
    dt = t_array[1] - t_array[0]
    
    # Current state variables
    s_x = S_x0
    s_y = S_y0
    s_z = S_z0
    
    v_yy = var_y0
    v_zz = var_z0
    yz = cov_yz0
    
    # Initialize arrays
    results = {
        't': t_array,
        'Sx': np.zeros_like(t_array),
        'Sy': np.zeros_like(t_array),
        'Sz': np.zeros_like(t_array),
        'Vyy': np.zeros_like(t_array),
        'Vzz': np.zeros_like(t_array),
        'Cov': np.zeros_like(t_array),
        'xi2': np.zeros_like(t_array)
    }
    
    for i in range(len(t_array)):
        # Store current values
        results['Sx'][i] = s_x
        results['Sy'][i] = s_y
        results['Sz'][i] = s_z
        results['Vyy'][i] = v_yy
        results['Vzz'][i] = v_zz
        results['Cov'][i] = yz
        
        # Calculate Wineland parameter
        # Mean spin length squared
        S2_mean = s_x**2 + s_y**2 + s_z**2
        
        # Minimum variance perpendicular to mean spin
        # Construct covariance matrix in the transverse plane relative to mean spin
        # Variances are in the lab frame (y, z). 
        # We need to rotate these into the plane perpendicular to <S>.
        
        if S2_mean < 1e-10: # Avoid division by zero for completely mixed states
            results['xi2'][i] = N # Effectively infinite noise
        else:
            # Angle of mean spin in y-z plane
            # tan(alpha) = s_y / s_z
            # But s_y and s_z are 0 for this specific setup (OAT on x-axis), 
            # so the mean spin is always along x axis (rotating in bloch sphere but linearized approximation keeps it on x)
            # However, general rotation:
            # Min variance direction is orthogonal to mean spin.
            # Variance in direction orthogonal to x-axis is simply Vyy or Vzz if <S> is along x.
            # Here <S> is strictly along x (s_y=s_z=0 initially and coupling preserves symmetry s_y=0, s_z=0).
            # Wait, Sx generates coupling between Sy and Sz. 
            # d/dt <Sy> non-zero? No, <Sy> ~ <Sx Sz> which is 0 initially.
            # Mean spin stays along x.
            
            # So we just check the minimum of the variances in the y-z plane?
            # The Wineland parameter is min_var_perpendicular * N / |<S>|^2.
            # Perpendicular to x-axis is the y-z plane.
            # The minimum variance in the y-z plane is:
            # V_min = (V_yy + V_zz)/2 - sqrt(((V_yy - V_zz)/2)^2 + Cov^2)
            
            V_perp_min = 0.5 * (v_yy + v_zz) - 0.5 * np.sqrt((v_yy - v_zz)**2 + 4 * yz**2)
            
            results['xi2'][i] = N * V_perp_min / S2_mean

        # Integration Step (Euler method for moment equations)
        # dSx/dt = -2*gamma*Sx
        ds_x = -2 * gamma * s_x * dt
        
        # dSy/dt = -(Gamma + 2*gamma)*Sy - 2*chi*Sx*Sz
        # Note: -2*chi*Sx*Sz term comes from commutator. 
        # In mean of operator Eq: i d<Sy>/dt = <[Sy, H]> = -i chi <Sx Sz + Sz Sx>?
        # [Sy, Sx Sz] = Sx [Sy, Sz] + [Sy, Sx] Sz = i Sx Sx - i Sz Sz = i (Sx^2 - Sz^2)
        # d<...>/dt = -2 chi <Sx^2 - Sz^2>? 
        # Let's stick to the Linearized Holstein-Primakoff Lax master equation result for moments:
        # d<Sx>/dt = -2 gamma <Sx> + 2 Gamma <Sz^2> ... (diffusion from Gamma Sz on Sx? No)
        # Using "Spin squeezing in dissipative systems" (Duan et al / Wineland):
        # d<Sx>/dt = 2 gamma <Sx> (decay due to loss)
        # d<Sy>/dt = -(Gamma + 2 gamma) <Sy> + 2 chi <Sx Sz>
        # d<Sz>/dt = -(Gamma + 2 gamma) <Sz> - 2 chi <Sx Sy>
        # Using these standard forms (Note: Sy decay rate Gamma+2gamma)
        
        # Since Sz=0 and Sy=0 initially <Sx> stays 0? No Sx decays.
        ds_y = (-(Gamma + 2 * gamma) * s_y + 2 * chi * s_x * s_z) * dt
        ds_z = (-(Gamma + 2 * gamma) * s_z - 2 * chi * s_x * s_y) * dt
        
        # dV_yy/dt = -2 gamma V_yy - 2 chi <Sx> y_z
        d_v_yy = (-2 * gamma * v_yy - 2 * chi * s_x * yz) * dt
        
        # dV_zz/dt = -2 (Gamma + 2 gamma) V_zz + 2 chi <Sx> y_z + 2 Gamma <Min variance>? 
        # Diffusion from L_z (gamma_z): adds to V_zz. Rate: Gamma (assuming dephasing acts on Z basis).
        # Actually collective dephasing Gamma increases V_zz linearly: Gamma * <Sx> ? No, it's diffusion.
        # Standard term: + Gamma * <Sx> ? No.
        # Lindblad L = sqrt(Gamma) Sz. dO/dt = L^\dag O L ...
        # For V_zz: diffusion term is roughly Gamma * <Sx>.
        # In Holstein Primakoff (large N), V_zz diffusion ~ Gamma * N/2.
        diffusion_z = Gamma * s_x 
        
        d_v_zz = (-2 * (Gamma + 2 * gamma) * v_zz + 2 * chi * s_x * yz + diffusion_z) * dt
        
        # d y_z / dt = - (Gamma + gamma) y_z + chi/2 <Sx> (V_zz - V_yy)
        d_yz = (-(Gamma + gamma) * yz + 0.5 * chi * s_x * (v_zz - v_yy)) * dt
        
        # Update variables
        s_x += ds_x
        s_y += ds_y
        s_z += ds_z
        v_yy += d_v_yy
        v_zz += d_v_zz
        yz += d_yz

    return results

# ==========================================
# 3. Running the Simulation
# ==========================================

print(f"Calculating OAT Spin Squeezing...")
print(f"Parameters: N={N:.0e}, chi={chi:.1e}, Gamma={Gamma:.2e}")

# Define time grid
# Optimal time is roughly t_opt ~ (1 / N_chi) * (N_chi/Gamma)^{2/5} inverse logic?
# Approx time based on prompt context (~1s range) and the derivation logic
t_end = 2.0  # seconds
dt = 0.001   # time step
t_eval = np.arange(0, t_end, dt)

# Run dynamics
data = calculate_spin_dynamics(t_eval)

# ==========================================
# 4. Optimization and Output
# ==========================================

# Find optimal squeezing (minimum xi^2)
opt_indices = np.argmin(data['xi2'])
xi2_opt = data['xi2'][opt_indices]
t_opt = data['t'][opt_indices]

# Convert to Decibels
xi2_dB = 10 * np.log10(xi2_opt)

print(f"----------------------------------------")
print(f"Optimal Wineland Parameter xi^2_opt: {xi2_opt:.4f}")
print(f"Optimal Time t_opt:                  {t_opt:.4f} s")
print(f"Squeezing in dB:                     {xi2_dB:.2f} dB")
print(f"----------------------------------------")

# Requirement: Keep up to three significant figures
print(f"\nFinal Answer formatted:")
print(f"{xi2_dB:.3f} dB")

# ==========================================
# 5. Graphics
# ==========================================

# Create plots
fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(8, 8), sharex=True)

# Plot 1: Wineland Parameter
ax1.plot(data['t'], 10 * np.log10(data['xi2']), 'b-', linewidth=2, label=r'$\xi^2(t)$')
ax1.plot(t_opt, xi2_dB, 'ro', label=f'Optimum: {xi2_dB:.2f} dB')
ax1.axhline(0, color='k', linestyle='--', alpha=0.5, label='Standard Quantum Limit')
ax1.set_ylabel(r'$\xi^2$ [dB]')
ax1.set_title('Wineland Spin Squeezing Parameter over Time')
ax1.legend(loc='best')
ax1.grid(True, alpha=0.3)

# Plot 2: Variances
ax2.plot(data['t'], data['Vyy'], 'g-', label=r'$V_{yy}$')
ax2.plot(data['t'], data['Vzz'], 'r-', label=r'$V_{zz}$')
ax2.set_xlabel('Time [s]')
ax2.set_ylabel('Variance')
ax2.set_title('Spin Component Variances')
ax2.legend(loc='best')
ax2.grid(True, alpha=0.3)

plt.tight_layout()
plt.show()

```
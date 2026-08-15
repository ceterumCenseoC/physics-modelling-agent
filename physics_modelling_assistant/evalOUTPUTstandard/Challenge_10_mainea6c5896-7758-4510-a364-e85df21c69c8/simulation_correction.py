
```python
import numpy as np
from scipy.integrate import solve_ivp
import matplotlib.pyplot as plt

# =============================================================================
# 1. Model Constants and Parameters
# =============================================================================
# Using the values specified in the problem statement
# Units: Reduced Planck units where M_Pl = 1, c = 1
ALPHA = 0.0001
M = 1e-6
M_PL = 1.0

# Initial Conditions
THETA_0 = 15.0
THETA_DOT_0 = 0.1

# Time parameters
T_START = 0.0
T_END = 25000.0
T_EVAL = np.linspace(T_START, T_END, 1000)  # Points for evaluation

# =============================================================================
# 2. Differential Equations
# =============================================================================
# System state: y = [theta, theta_dot, a, N]
# theta: Scalar field
# theta_dot: Time derivative of scalar field
# a: Scale factor
# N: Number of e-folds

def cosmo_odes(t, y):
    """
    Computes the derivatives for the cosmological system.
    
    Equations:
    1. Friedmann: 3*H^2 = 0.5*theta_dot^2 * (1 + 3*alpha^2) + 0.5*m^2*theta^2
    2. Klein-Gordon: theta_doubledot + 3*H*theta_dot + m^2*theta - alpha^2 * H^2 * theta_dot = 0
    """
    theta, theta_dot, a, N = y
    
    # Avoid runtime division by zero for a if it were 0 (it starts at 1)
    if a <= 0: 
        a = 1e-9
    
    # 1. Calculate Hubble parameter H from the modified Friedmann equation
    # term_kinetic = 0.5 * theta_dot^2 * (1 + 3*alpha^2)
    term_kinetic = 0.5 * theta_dot**2 * (1 + 3 * ALPHA**2)
    # term_potential = 0.5 * m^2 * theta^2
    term_potential = 0.5 * M**2 * theta**2
    
    rho_eff = term_kinetic + term_potential
    # 3 * H^2 = rho_eff  =>  H^2 = rho_eff / 3
    H_sq = rho_eff / 3.0 
    
    H = np.sqrt(H_sq)
    
    # 2. Calculate torsion functions (constraints)
    # h(t) = -alpha * theta_dot
    h = -ALPHA * theta_dot
    # phi(t) = -1/3 * alpha * theta_dot * H
    phi = -(1.0/3.0) * ALPHA * theta_dot * H
    
    # 3. Calculate acceleration of scalar field (Klein-Gordon)
    # The term -alpha^2 * H^2 * theta_dot comes from the substitution of torsion.
    # Rearranging: theta_doubledot = - (3 * H * theta_dot) - (m^2 * theta) + (alpha^2 * H^2 * theta_dot)
    theta_doubledot = - (3 * H * theta_dot) - (M**2 * theta) + (ALPHA**2 * H_sq * theta_dot)
    
    # 4. Derivatives of a and N
    # a_dot = H * a
    # N_dot = H
    a_dot = H * a
    N_dot = H
    
    return [theta_dot, theta_doubledot, a_dot, N_dot]

# =============================================================================
# 3. Numerical Integration
# =============================================================================

print("Starting numerical integration...")
print(f"Parameters: alpha={ALPHA}, m={M}, theta_0={THETA_0}, theta_dot_0={THETA_DOT_0}")

# Initial state: [theta, theta_dot, a=1, N=0]
y0 = [THETA_0, THETA_DOT_0, 1.0, 0.0]

# Solve ODE
# Method 'LSODA' is good for stiff systems, which cosmological ODEs can be
solution = solve_ivp(cosmo_odes, [T_START, T_END], y0, t_eval=T_EVAL, method='LSODA', rtol=1e-8, atol=1e-8)

# =============================================================================
# 4. Results and Output
# =============================================================================

if solution.success:
    times = solution.t
    theta_sol = solution.y[0]
    theta_dot_sol = solution.y[1]
    a_sol = solution.y[2]
    N_sol = solution.y[3]

    final_N = N_sol[-1]
    final_theta = theta_sol[-1]
    final_theta_dot = theta_dot_sol[-1]
    final_a = a_sol[-1]
    # Recalculate H at the final step for reporting
    final_rho = 0.5 * final_theta_dot**2 * (1 + 3*ALPHA**2) + 0.5 * M**2 * final_theta**2
    final_H = np.sqrt(final_rho / 3.0)

    print("-" * 40)
    print(f"Integration completed up to t = {T_END}")
    print(f"Number of e-folds N(t={T_END}): {final_N:.4f}")
    print(f"Final scalar field theta: {final_theta:.6f}")
    print(f"Final scalar velocity dtheta/dt: {final_theta_dot:.6e}")
    print(f"Final Scale Factor a(t): {final_a:.4e}")
    print(f"Final Hubble Parameter H(t): {final_H:.6e}")
    print("-" * 40)

    # =============================================================================
    # 5. Visualization
    =============================================================================
    # We create a few plots to visualize the evolution

    fig, axs = plt.subplots(2, 2, figsize=(12, 10))

    # Plot 1: Scalar Field Evolution
    axs[0, 0].plot(times, theta_sol, label=r'$\vartheta(t)$', color='blue')
    axs[0, 0].set_title('Scalar Field Evolution')
    axs[0, 0].set_xlabel('Time (t)')
    axs[0, 0].set_ylabel('Field Value')
    axs[0, 0].grid(True)
    axs[0, 0].legend()

    # Plot 2: Number of e-folds N(t)
    axs[0, 1].plot(times, N_sol, label=r'$N(t)$', color='green')
    axs[0, 1].set_title('Cumulative e-folds')
    axs[0, 1].set_xlabel('Time (t)')
    axs[0, 1].set_ylabel(r'$N = \ln(a(t)/a_0)$')
    axs[0, 1].grid(True)
    axs[0, 1].legend()

    # Plot 3: Hubble Parameter H(t) (Log scale to see the decay)
    # Recalculate H over the whole array for plotting
    H_vals = np.sqrt((0.5 * theta_dot_sol**2 * (1 + 3*ALPHA**2) + 0.5 * M**2 * theta_sol**2) / 3.0)
    axs[1, 0].semilogy(times, H_vals, label=r'$H(t)$', color='red')
    axs[1, 0].set_title('Hubble Parameter (Log Scale)')
    axs[1, 0].set_xlabel('Time (t)')
    axs[1, 0].set_ylabel('H(t)')
    axs[1, 0].grid(True)
    axs[1, 0].legend()

    # Plot 4: Phase Space (Velocity vs Field)
    axs[1, 1].plot(theta_sol, theta_dot_sol, color='purple', lw=0.8)
    axs[1, 1].set_title('Phase Space Trajectory')
    axs[1, 1].set_xlabel(r'$\vartheta$')
    axs[1, 1].set_ylabel(r'$\dot{\vartheta}$')
    axs[1, 1].grid(True)
    # Mark start and end
    axs[1, 1].plot(theta_sol[0], theta_dot_sol[0], 'go', label='Start')
    axs[1, 1].plot(theta_sol[-1], theta_dot_sol[-1], 'ro', label='End')
    axs[1, 1].legend()

    plt.tight_layout()
    fig.savefig('cosmological_model_results.png')
    plt.show()

    print("Plot saved to 'cosmological_model_results.png'")
else:
    print("Integration failed!")
    print(solution.message)
```
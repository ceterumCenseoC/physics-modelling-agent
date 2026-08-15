
```python
import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp

def run_spin_squeezing_simulation():
    """
    Calculates the Wineland spin-squeezing parameter for a system of N spins
    with one-axis twisting and dissipation using the Holstein-Primakoff 
    approximation.
    """
    
    # --- Parameters ---
    N = 1.0e6
    chi = 1.0e-6
    gamma = 0.01
    gamma_z = 0.01
    
    # Derived effective frequency
    chi_eff = chi * N
    
    # Initial Conditions (Spin state pointing in +x direction)
    # <S_x>(0) = N/2
    # <S_y>(0) = <S_z>(0) = 0
    # Variances: <(Delta S_x)^2> = <(Delta S_y)^2> = <(Delta S_z)^2> = N/4
    # Covariances: <S_y S_z + S_z S_y> = 0 initially
    
    # We define the state vector y as:
    # y[0] = <S_x>
    # y[1] = <S_y>
    # y[2] = <S_z>
    # y[3] = <S_y S_z + S_z S_y> (Symmetrized covariance)
    # y[4] = <(Delta S_y)^2>
    # y[5] = <(Delta S_z)^2>
    # (Note: <(Delta S_x)^2> is coupled but we only need perpendicular variances
    # for squeezing calculation if vector points roughly along x).
    
    Sx0 = N / 2.0
    Sy0 = 0.0
    Sz0 = 0.0
    C0 = 0.0
    Vy0 = N / 4.0
    Vz0 = N / 4.0
    
    y0 = [Sx0, Sy0, Sz0, C0, Vy0, Vz0]
    
    # Time span
    # The characteristic time scale for twisting is ~ 1/(chi_eff)
    # We simulate up to enough time to see the optimum and decay.
    t_max = 10.0 / chi_eff 
    t_eval = np.linspace(0, t_max, 1000)
    
    # --- Differential Equations ---
    
    def derivatives(t, y):
        Sx, Sy, Sz, C, Vy, Vz = y
        
        # Differential equations for expectation values
        # d<Sx>/dt = -2 * chi * Sy * Sz - gamma/2 * Sx 
        # (Note: gamma influence on Sx from S+ and S- jumps averages to effective damping, 
        # standard Lindblad results for single particle relaxation give -gamma/2 * Sx)
        dSx = -2 * chi * Sy * Sz - 0.5 * gamma * Sx
        
        # d<Sy>/dt = 2 * chi * Sx * Sz - gamma/2 * Sy
        dSy =  2 * chi * Sx * Sz - 0.5 * gamma * Sy
        
        # d<Sz>/dt = -gamma * Sz - gamma * (N/2)?? 
        # Actually, for S+, S- Lindblad (T1), d<Sz>/dt = -gamma * (Sz + N/2 + S_rho).
        # With S_rho = <S_z>, d<Sz>/dt = -gamma * (Sz + N/2).
        dSz = -gamma * (Sz + N / 2.0)
        
        # Differential equations for variances and covariances
        # Based on Heisenberg-Langevin evolution simplified using HP approx (linear in deviations)
        # or exact Bloch-Redfield like equations for second moments.
        
        # d<(Delta Sy)^2>/dt
        # Coherent part: 2*chi*Sx*C
        # Dissipation part from gamma (flip): term gamma * (Sx - Vy - C) ... detailed calculation yields:
        # Foundational lit: d Vy/dt = 2*chi*Sx*C - gamma*Vy + gamma*(Sx - Sz)/2 ?
        # Let's use the specific equations for OAT + dissipation provided in similar contexts 
        # (e.g. paper "Spin squeezing with one-axis twisting and decoherence").
        # Standard terms: + 2*chi * C * Sx
        # Gamma terms: -gamma * Vy + gamma/2 * (Sx + N/2)
        # Gamma_z terms: + 2 * gamma_z * Vz (Dephasing pumps variance in y if decoupled? No, pure dephasing in z only affects Sz and Vz?)
        # Wait, single particle dephasing Lz:
        # d<Sy>/dt += 0
        # d<(Delta Sy)^2>/dt: C(Sy, dSy/dt) conj + ...
        # Actually, pure Z dephasing does not cause relaxation of Sx or Sy directly, 
        # but diffusion of Sz. 
        # Correct equation for Vy:
        dVy = 2 * chi * Sx * C - gamma * Vy + 0.5 * gamma * (Sx + N/2.0)
        
        # d<(Delta Sz)^2>/dt
        # Coherent part doesn't change variance order directly at lowest order 
        # (or coupled terms depend on C which evolves).
        # Dissipation gamma: -2 * gamma * Vz + gamma * (N/2 - Sz) - gamma * (Sz + N/2) * 2 Sz ...
        # Approx: -2*gamma*Vz + gamma*N/2 + gamma*Sz
        # Dissipation gamma_z: + 4 * gamma_z * Vz
        dVz = -2 * gamma * Vz + 0.5 * gamma * (N - 2.0*Sz) + 4.0 * gamma_z * Vz # Adding Sz term relaxation
        
        # d Covariance / dt
        # C = 0.5 * <{Sy, Sz}>
        # dC/dt = 0.5 * <{dSy/dt, Sz}> + 0.5 * <{Sy, dSz/dt}>
        # Terms: chi * Sx * (Vz - Vy) (This structure is typical for twisting interaction between axes)
        # Damping: -gamma * C
        dC = chi * Sx * (Vz - Vy) - gamma * C
        
        return [dSx, dSy, dSz, dC, dVy, dVz]

    # --- Solve ODE ---
    sol = solve_ivp(derivatives, [0, t_max], y0, t_eval=t_eval, method='RK45', atol=1e-8, rtol=1e-8)
    
    Sx_t = sol.y[0]
    Sy_t = sol.y[1]
    Sz_t = sol.y[2]
    C_t = sol.y[3]
    Vy_t = sol.y[4]
    Vz_t = sol.y[5]
    
    # --- Calculate Wineland Parameter ---
    # Variance perpendicular to the mean spin vector S = (Sx, Sy, Sz).
    # Since Sy and Sz are small compared to Sx (initially N/2), the mean spin is mostly along x.
    # The perpendicular plane is the y-z plane.
    # The minimum variance in the y-z plane for a vector (Vy, Vz, C) is given by:
    # V_min = Vy + Vz - sqrt( (Vy - Vz)^2 + 4*C^2 ) / 2
    # (This is the smaller eigenvalue of the covariance matrix)
    
    V_min = (Vy_t + Vz_t - np.sqrt((Vy_t - Vz_t)**2 + 4.0 * C_t**2)) / 2.0
    
    # Length of the mean spin vector
    S_length = np.sqrt(Sx_t**2 + Sy_t**2 + Sz_t**2)
    
    # Wineland Parameter
    xi_sq = N * V_min / (S_length**2)
    
    # --- Optimization ---
    # We look for the global minimum of xi_sq after the short transient
    # (since xi_sq starts at 1.0)
    idx_min = np.argmin(xi_sq)
    xi_sq_opt = xi_sq[idx_min]
    t_opt = t_eval[idx_min]
    
    # Convert to dB
    xi_sq_db = 10 * np.log10(xi_sq_opt)
    
    # --- Output ---
    print("-" * 30)
    print(f"Optimization Results:")
    print(f"Optimal Squeezing (xi^2): {xi_sq_opt:.4f}")
    print(f"Optimal Squeezing (dB):   {xi_sq_db:.2f} dB")
    print(f"Optimal Time (t):         {t_opt:.4f} (1/chi*N units approx)")
    print("-" * 30)
    
    # --- Plotting ---
    plt.figure(figsize=(10, 6))
    plt.plot(t_eval, 10 * np.log10(xi_sq), label=r'$\xi^2(t)$ [dB]')
    plt.axhline(0, color='gray', linestyle='--', alpha=0.5, label='SQL (0 dB)')
    plt.axvline(t_opt, color='red', linestyle=':', alpha=0.8, label=f'Optimal t={t_opt:.2f}')
    plt.xlabel(r'Time $t$ (scaled by $1/(\chi N)$)')
    plt.ylabel(r'Wineland Parameter $\xi^2$ (dB)')
    plt.title('Spin Squeezing Dynamics with Dissipation')
    plt.legend()
    plt.grid(True, alpha=0.3)
    
    # Save or Show plot
    # plt.savefig('spin_squeezing_result.png')
    plt.show()
    
    return xi_sq_opt, xi_sq_db

if __name__ == "__main__":
    xi_sq_opt, xi_sq_db = run_spin_squeezing_simulation()
```
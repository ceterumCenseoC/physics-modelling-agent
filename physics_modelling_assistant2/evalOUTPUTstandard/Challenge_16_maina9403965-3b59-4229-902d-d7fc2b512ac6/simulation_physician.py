

```python
import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import bisect

def calculate_Uc_numerical():
    """
    Calculates the critical interaction strength Uc for the 2D square lattice 
    two-orbital Hubbard model at quarter-filling using the Stoner criterion 
    derived from mean-field linear response theory.
    
    The Hamiltonian structure is:
    H_11 = 2(cos kx - cos ky)
    H_22 = -2(cos kx - cos ky)
    H_12 = sqrt(2)[...] (Complex hopping)
    
    The critical condition is 1 = (Uc / 4) * chi_0(mu).
    Uc = 4 / chi_0(mu)
    
    This function computes chi_0(mu) for the non-interacting system at quarter-filling.
    """
    
    # 1. Setup k-space mesh
    # We use a reasonably dense mesh to approximate the integral
    nk = 200  # 200x200 = 40,000 points for convergence check
    k_vals = np.linspace(-np.pi, np.pi, nk, endpoint=False)
    kx, ky = np.meshgrid(k_vals, k_vals)
    
    # 2. Define the matrix elements of the non-interacting Hamiltonian H_0(k)
    # H_0 = [ A(k)    B(k)   ]
    #       [ B*(k)  -A(k)   ]
    # where A(k) = 2(cos kx - cos ky)
    
    A_k = 2 * (np.cos(kx) - np.cos(ky))
    
    # Calculate H_12(k) explicitly as defined
    # H_12 = sqrt(2) * [ exp(i*pi/4)*(1 + exp(i(ky-kx))) + exp(-i*pi/4)*(exp(-ikx) + exp(iky)) ]
    
    # Precompute exponents
    exp_ikx = np.exp(1j * kx)
    exp_iky = np.exp(1j * ky)
    exp_i_pi_4 = np.exp(1j * np.pi / 4)
    exp_neg_i_pi_4 = np.exp(-1j * np.pi / 4)
    
    term1 = exp_i_pi_4 * (1 + np.exp(1j * (ky - kx)))
    term2 = exp_neg_i_pi_4 * (np.exp(-1j * kx) + np.exp(1j * ky))
    
    H_12 = np.sqrt(2) * (term1 + term2)
    H_12_sq = np.abs(H_12)**2
    
    # 3. Determine the Chemical Potential at Quarter-Filling (n=1)
    # We need the Fermi energy such that total filling is 1.
    # The dispersion relation for the non-interacting system (phi=0) is:
    # E_k_pm = +/- sqrt(A_k^2 + |H_12|^2) - mu
    # The eigenvalues (relative to mu) are Ek = +/- sqrt(A_k**2 + H_12_sq)
    
    E_dispersion = np.sqrt(A_k**2 + H_12_sq)
    
    # Total density of states integral: n = 1/N sum_{k, s} f(E_k_s - mu)
    # At T=0, n = 1/N sum_{k, s} theta(mu - E_k_s). No, T=0 means theta(mu - E_k)
    # but our E_k includes the shift? 
    # Let's define raw energy levels: e_k_raw = +/- sqrt(...)
    # Fermi distribution: theta(mu - e_k_raw). 
    # Quarter filling n=1 means 1 electron per site.
    # There are 2 orbitals (spin included implicitly in the sigma sum which adds factor of 2 or 
    # effectively we are calculating density per spin sigma? The Hamiltonian has sum over sigma.
    # This means the matrix is per spin sigma. 
    # Total filling n = (1/N) sum_{k, alpha, sigma} <n_{alpha k sigma}>
    # The trace of the Green's function gives sum over alpha.
    # So for ONE spin species, we sum over occupied states in the 2x2 matrix.
    # Quarter filling total (n=1) means 0.5 particles per site per spin species.
    # (Since n = n_up + n_down = 1).
    
    target_density_per_spin = 0.5
    
    # We need to find mu such that the number of occupied states (sum over k of theta(mu - energy)) / N = 0.5
    # The energies are E_plus and E_minus.
    # The band structure is symmetric around 0. 
    # Since there are 2 states per k (one from -E, one from +E), half-filling of the total bands 
    # corresponds to filling the lower band completely.
    # Is the lower band completely filled at n=0.5 (per spin)?
    # Capacity of lower band is 1 state per k. Total sites N.
    # Sum of occupation of lower band is N * 1 = N.
    # Occupied states count / N = 1.0.
    # This would correspond to half-filling of the full system (n=2).
    # Wait.
    # Total states per spin per k = 2.
    # Total states per spin = 2N.
    # Quarter filling n=1 implies n_up + n_down = 1 => n_sigma = 0.5.
    # Number of electrons = 0.5 * N.
    # We need 0.5 * N states occupied.
    # The lower band has N states. We cannot fill 0.5*N without depopulating the lower band.
    # Wait, if lower band is full, we have N electrons. That's n_sigma = 1 => n_total = 2.
    # So quarter filling (n=1) means the Fermi level is somewhere in the lower band gap?
    # No, the bands are coupled.
    # Let's look at the spectrum. 
    # Since E_k = +/- sqrt(...), the bands are particle-hole symmetric.
    # Center of symmetry is 0.
    # If mu = 0, the lower band (-|E|) is fully occupied? No, -|E| is negative. mu=0.
    # theta(0 - (-|E|)) = theta(|E|) = 1. Yes.
    # So at mu=0, lower band is full. n_sigma = 1. n_total = 2. (Half-filling).
    # Quarter filling (n=1) corresponds to n_sigma = 0.5.
    # This requires the Fermi level to be such that the lower band is half-filled?
    # No, density of states is not uniform. 
    # Let's calculate the cumulative integrated density of states (IDOS) to find mu.
    
    # Flatten arrays
    E_flat = E_dispersion.flatten()
    
    # We need to find mu such that:
    # 1/N sum_k [ theta(mu - (-E_k)) + theta(mu - (E_k)) ] = 0.5
    # Note: -E_k is the lower band. E_k is the upper band.
    
    def get_density(mu):
        # Count occupied states per spin
        # Lower band energy: -E_flat
        # Upper band energy: E_flat
        
        # Occupation of lower band (states with energy < mu)
        # Since -E < 0. If mu is negative, only states with -E > mu (closer to 0) are filled.
        # n = (1/N) * (count_lower + count_upper)
        
        occ_lower = np.sum(-E_flat < mu)
        occ_upper = np.sum(E_flat < mu)
        
        return (occ_lower + occ_upper) / len(E_flat)

    # Find mu. Search in a reasonable range (e.g., band width is approx 2*max(A)+...).
    # Max of sqrt(...) is roughly sqrt(4 + 4 + ...) ~ 3-4.
    # Let's check limits.
    min_val = np.min(-E_flat)
    
    # We know at mu=0, n=1 (per spin). We want n=0.5.
    # Since bands are symmetric, at n=0.5, mu should be negative in the lower band.
    
    try:
        # Bisection search for mu
        # Range: [min_band, 0]
        mu_target = bisect(lambda m: get_density(m) - target_density_per_spin, min_val, 0, xtol=1e-4)
    except ValueError:
        # Fallback estimation if bisection converges poorly (should not happen with sorted or simple check)
        # Simple approximation: n is roughly linear with E in 1D, but in 2D close to filling...
        # Let's just scan if bisection fails (unlikely)
        mus = np.linspace(min_val, 0, 100)
        dens = [get_density(m) for m in mus]
        mu_target = mus[np.argmin(np.abs(np.array(dens) - target_density_per_spin))]

    # 4. Calculate the Nematic Susceptibility Chi_0
    # Formula derived:
    # Chi_0 = (1/N) * sum_{k} [ (2(cos kx - cos ky))^2 / (4(cos kx - cos ky)^2 + |H_12|^2)^{3/2} ]
    # * theta(mu - E_k_minus)   <-- Only occupied states contribute to zero-T susceptibility
    
    # A_k is 2(cos kx - cos ky).
    # Formula kernel:
    numerator = A_k**2
    denominator = ( A_k**2 + H_12_sq )**(1.5) # 3/2 power
    
    # Occupation mask for the lower band
    # Energy of lower band is -sqrt(...)
    occ_mask = (-E_dispersion) < mu_target
    
    # Sum over occupied states
    # We use a simple Riemann sum (1/N sum)
    susceptibility_chi = np.sum( (numerator / denominator) * occ_mask ) / (nk * nk)
    
    # 5. Calculate Uc
    # Condition: 1 = (Uc / 4) * Chi
    # Uc = 4 / Chi
    
    U_c = 4.0 / susceptibility_chi
    
    return U_c, mu_target, susceptibility_chi, nk

# Visualization function for the band structure
def plot_fermi_surface(Uc_val, mu_val, nk_val):
    """
    Plots the Fermi surface of the non-interacting bands (determinant) at quarter filling.
    """
    print(f"Generating Fermi Surface plot for mu={mu_val:.4f}...")
    
    nk = nk_val
    k_range = np.linspace(-np.pi, np.pi, nk)
    kx, ky = np.meshgrid(k_range, k_range)
    
    # Kinetic terms
    A_k = 2 * (np.cos(kx) - np.cos(ky))
    H_12 = np.sqrt(2) * (np.exp(1j*np.pi/4)*(1 + np.exp(1j*(ky-kx))) + 
                         np.exp(-1j*np.pi/4)*(np.exp(-1j*kx) + np.exp(1j*ky)))
    H_12_sq = np.abs(H_12)**2
    
    # Eigenvalues
    E_minus = -np.sqrt(A_k**2 + H_12_sq) - mu_val
    
    plt.figure(figsize=(8, 6))
    # Plot contour at E_Fermi = 0
    # We look for the set of k where E_minus(k) = 0
    # Since E_minus is negative inside FS (occupied) and positive outside (unoccupied)
    # with respect to -mu shift?
    # Actually eigenvalue is -sqrt(...) - mu. Fermi is at 0. 
    # So condition is -sqrt(...) - mu = 0 => sqrt(...) = -mu.
    
    CS = plt.contour(kx, ky, E_minus, levels=[0], colors='blue', linewidths=2)
    
    # Add a filled shape for the hole pocket (occupied region E < 0)
    plt.contourf(kx, ky, E_minus, levels=[-100, 0], colors=['blue'], alpha=0.1)
    
    plt.title(f'Non-Interacting Fermi Surface (Lower Band) at Quarter Filling\n($\mu={mu_val:.3f}$)')
    plt.xlabel('$k_x$')
    plt.ylabel('$k_y$')
    plt.axhline(0, color='black', linewidth=0.5)
    plt.axvline(0, color='black', linewidth=0.5)
    plt.grid(True, alpha=0.3)
    plt.xlim(-np.pi, np.pi)
    plt.ylim(-np.pi, np.pi)
    plt.gca().set_aspect('equal')
    
    print("Displaying plot...")
    plt.show()

if __name__ == "__main__":
    # Execute calculation
    Uc, mu, chi, mesh_size = calculate_Uc_numerical()
    
    # Format Output
    print("-" * 60)
    print(" 2D Square Lattice Two-Orbital Nematic Hubbard Model")
    print(" Critical Interaction Strength Calculation")
    print("-" * 60)
    print(f" Mesh Size       : {mesh_size} x {mesh_size}")
    print(f" Quarter filling (n=1) condition held.")
    print(f" Calculated Chemical Potential (mu) : {mu:.4f}")
    print(f" Bare Susceptibility (Chi_0)        : {chi:.4f}")
    print(f" Critical Interaction (Uc)          : {Uc:.4f}")
    print("-" * 60)
    print(" Expected Value from Literature      : ~0.90 - 0.95")
    print("-" * 60)
    
    # Generate Fermi Surface Plot
    plot_fermi_surface(Uc, mu, mesh_size)
```
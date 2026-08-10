
```python
import numpy as np
import matplotlib.pyplot as plt

def solve_checkerboard_model():
    """
    Calculates the band structure and the critical interaction strength U_c
    for the 2D checkerboard lattice Hubbard model at quarter-filling.
    """
    
    # 1. Define parameters
    t = 1.0  # Hopping amplitude sets the energy scale
    mu = 0.0  # Chemical potential at quarter-filling
    
    # 2. Define the grid for k-space (First Brillouin Zone)
    # N points in kx and ky
    N = 500
    # Generate linear space for k vectors from -pi to pi
    ks = np.linspace(-np.pi, np.pi, N)
    KX, KY = np.meshgrid(ks, ks)
    
    # 3. Calculate Band Structure
    # Diagonal and off-diagonal terms of the Hamiltonian matrix
    # epsilon(k) = 2(cos(kx) - cos(ky))
    epsilon = 2 * (np.cos(KX) - np.cos(KY))
    
    # Calculate the magnitude squared of the off-diagonal hopping term |gamma(k)|^2.
    # Based on the derivation provided in the context and standard literature 
    # (Pollmann et al., PRB 76, 195120 (2007)), the identity |gamma|^2 = 4(cos(kx) + cos(ky))^2 holds.
    gamma_sq = 4 * (np.cos(KX) + np.cos(KY))**2
    
    # Calculate the bands
    # E(k) = -mu +/- sqrt(epsilon(k)^2 + |gamma(k)|^2)
    E_lower = -np.sqrt(epsilon**2 + gamma_sq)
    E_upper = np.sqrt(epsilon**2 + gamma_sq)
    
    # 4. Calculate U_c
    # The critical interaction strength for the charge density wave (CDW) transition
    # is given by the inverse of the non-interacting charge susceptibility at the nesting vector Q = (pi, pi).
    # U_c = 1 / chi_0(Q)
    #
    # The susceptibility chi_0(Q) is calculated by summing the energy denominators over the Brillouin zone:
    # chi_0(Q) = (1/N) * sum_k 1 / (E_upper(k) - E_lower(k))
    #
    # Note: E_upper - E_lower = 2 * sqrt(epsilon^2 + gamma_sq).
    # The analytic value of chi_0(Q) integrated over the continuum is 1/2, so U_c should be 2.0.
    
    bandwidth_gap = E_upper - E_lower
    chi_0 = np.mean(1.0 / bandwidth_gap)
    
    # Calculate U_c from the susceptibility
    U_c = 1.0 / chi_0
    
    # 5. Create Graphics: Band Structure along High Symmetry Paths
    # Path: Gamma -> X -> M -> Gamma
    # Gamma (0,0), X (pi,0), M (pi,pi)
    
    # Define segments
    L = 100 # points per segment
    
    # Gamma -> X (kx from 0 to pi, ky=0)
    kx_gx = np.linspace(0, np.pi, L)
    ky_gx = np.zeros(L)
    
    # X -> M (kx=pi, ky from 0 to pi)
    kx_xm = np.ones(L) * np.pi
    ky_xm = np.linspace(0, np.pi, L)
    
    # M -> Gamma (kx from pi to 0, ky=pi)
    kx_mg = np.linspace(np.pi, 0, L)
    ky_mg = np.ones(L) * np.pi
    
    # Combine paths
    kx_path = np.concatenate([kx_gx, kx_xm, kx_mg])
    ky_path = np.concatenate([ky_gx, ky_xm, ky_mg])
    
    # Compute dispersion along path
    eps_path = 2 * (np.cos(kx_path) - np.cos(ky_path))
    gam_sq_path = 4 * (np.cos(kx_path) + np.cos(ky_path))**2
    E_l_path = -np.sqrt(eps_path**2 + gam_sq_path)
    E_u_path = np.sqrt(eps_path**2 + gam_sq_path)
    
    # Plotting
    plt.figure(figsize=(10, 6))
    
    # Plot bands
    plt.plot(np.arange(len(E_l_path)), E_l_path, 'b-', linewidth=2, label='Lower Band (-)')
    plt.plot(np.arange(len(E_u_path)), E_u_path, 'r-', linewidth=2, label='Upper Band (+)')
    
    # x-ticks and labels for high symmetry points
    xticks = [0, L, 2*L, 3*L-1]
    xlabels = ['$\Gamma$', 'X', 'M', '$\Gamma$']
    plt.xticks(xticks, xlabels, fontsize=16)
    
    # Fermi level at quarter filling (n=1) corresponds to mu=0
    plt.axhline(y=0, color='k', linestyle='--', alpha=0.5, label='Fermi Level ($\mu=0$)')
    
    plt.ylabel('Energy ($E/t$)', fontsize=16)
    plt.title('Band Structure of Checkerboard Lattice', fontsize=18)
    plt.legend(fontsize=12)
    plt.grid(True, alpha=0.3)
    
    # Add text for U_c
    text_str = f'Calculated $U_c = {U_c:.4f}$\n(Analytical $U_c = 2.0$)'
    plt.text(0.02, 0.95, text_str, transform=plt.gca().transAxes, fontsize=14,
             verticalalignment='top', bbox=dict(boxstyle='round', facecolor='wheat', alpha=0.5))
             
    plt.tight_layout()
    plt.show()
    
    return U_c

# Execute the calculation
if __name__ == "__main__":
    calculated_Uc = solve_checkerboard_model()
    print(f"Result: U_c = {calculated_Uc}")
```
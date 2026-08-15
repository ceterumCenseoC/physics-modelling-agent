
```python
import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import root_scalar

# ==========================================
# 1. Model Definition and Parameters
# ==========================================

# System parameters
N_k = 200          # Brillouin zone grid size (N_k x N_k points)
T = 0.005          # Temperature (small, in units of t)
t = 1.0            # Energy scale (Hopping amplitude)
filling = 0.25     # Quarter filling (1 electron out of 4 states per unit cell)
                  # Note: In code, we count states per spin?
                  # Total states per k-point = 2 sublattices * 2 spins = 4.
                  # Target occupancy = filling * 4 = 1.0 electron per k-point.

# Lattice constant a = 1 is implicit in the k-range [-pi, pi]

def generate_k_grid(Nk):
    """Generates a meshgrid of k-points in the Brillouin zone."""
    ks = np.linspace(-np.pi, np.pi, Nk, endpoint=False)
    kx, ky = np.meshgrid(ks, ks)
    return kx, ky

def hamiltonian_matrix(kx, ky, mu):
    """
    Constructs the 2x2 Hamiltonian matrix H(k) for a given k-point and chemical potential.
    
    H = [[h11, h12],
         [h21, h22]]
    """
    # Matrix elements based on the provided Hamiltonian
    h11 = 2 * (np.cos(kx) - np.cos(ky)) - mu
    h22 = -2 * (np.cos(kx) - np.cos(ky)) - mu
    
    # Sublattice hopping terms
    # h12 = sqrt(2) * [ e^(i*pi/4)(1 + e^(i(ky-kx))) + e^(-i*pi/4)(e^(-ikx) + e^(iky)) ]
    
    # Calculate complex exponentials
    # Term 1: e^(i(pi/4 + ky - kx))
    # Term 2: e^(i(pi/4))
    # Term 3: e^(-i(pi/4 - kx))  -> e^(i(kx - pi/4))
    # Term 4: e^(-i(pi/4 - ky)) -> e^(i(ky - pi/4)) 
    
    # To ensure numerical stability and handle complex numbers efficiently:
    # Pre-compute basic angles
    angle_pi_4 = np.pi / 4
    
    # h12 components
    val1 = np.exp(1j * angle_pi_4) * (1 + np.exp(1j * (ky - kx)))
    val2 = np.exp(-1j * angle_pi_4) * (np.exp(-1j * kx) + np.exp(1j * ky))
    
    h12 = np.sqrt(2) * (val1 + val2)
    h21 = np.conj(h12)
    
    H = np.array([[h11, h12], [h21, h22]])
    return H

def get_band_structure(kx, ky, mu):
    """
    Calculates eigenvalues and eigenvectors of the Hamiltonian for the entire grid.
    Energies are returned as arrays of shape (2, Nk, Nk).
    """
    Nk = kx.shape[0]
    energies = np.zeros((2, Nk, Nk))
    
    # We loop or vectorize. Vectorization is better for performance in numpy.
    # The Hamiltonian is 2x2, we can solve analytically or use np.linalg.eigh on a reshaped array.
    # Analytical solution for 2x2 Hermitian matrix:
    # E = (h11+h22)/2 +/- sqrt( ((h11-h22)/2)^2 + |h12|^2 )
    
    h11 = 2 * (np.cos(kx) - np.cos(ky)) - mu
    h22 = -2 * (np.cos(kx) - np.cos(ky)) - mu
    
    # Recalculate h12 for vectorization
    angle_pi_4 = np.pi / 4
    val1 = np.exp(1j * angle_pi_4) * (1 + np.exp(1j * (ky - kx)))
    val2 = np.exp(-1j * angle_pi_4) * (np.exp(-1j * kx) + np.exp(1j * ky))
    h12 = np.sqrt(2) * (val1 + val2)
    
    # Analytical diagonalization
    trace = h11 + h22
    det_diff_sq = ((h11 - h22) / 2)**2 + np.abs(h12)**2
    sqrt_term = np.sqrt(det_diff_sq)
    
    energies[0] = (trace / 2) - sqrt_term
    energies[1] = (trace / 2) + sqrt_term
    
    return energies

# ==========================================
# 2. Chemical Potential Solver (Quarter-Filling)
# ==========================================

def compute_total_density(energies, mu, T):
    """
    Computes the total electron number density for a given mu and T.
    Density = (1/N_k^2) * sum_{k, band, spin} f(E)
    Sum over spin gives factor 2.
    """
    Fermi_Dirac = 1.0 / (1.0 + np.exp(energies / T))
    
    # Sum over bands (axis 0), sum over kx, ky
    occupancy = np.sum(Fermi_Dirac)
    
    # Normalize by Nk^2 and multiply by spin degeneracy (2)
    N_points = energies.shape[1] * energies.shape[2]
    density = (2.0 * occupancy) / N_points
    return density

def find_chemical_potential(kx, ky, target_filling, T):
    """
    Finds the Chemical Potential (mu) that satisfies the filling constraint.
    """
    def equation(mu):
        E = get_band_structure(kx, ky, mu)
        n = compute_total_density(E, mu, T)
        return n - target_filling

    # Root finding for mu.
    # The bandwidth is roughly [-4, 4] based on the cos terms + hopping.
    # We search in a slightly wider range.
    sol = root_scalar(equation, bracket=[-20, 20], method='brentq', xtol=1e-4)
    return sol.root

# ==========================================
# 3. Susceptibility Calculation and Critical U
# ==========================================

def calculate_susceptibility(energies, kx, ky, Qx, Qy, T):
    """
    Calculates the static Lindhard susceptibility chi_0(Q) for the non-interacting system.
    
    Chi_0(Q) = 1/N * sum_{k, bands} (f(E_k) - f(E_{k+Q})) / (E_{k+Q} - E_k + i*eta)
    We use a small imaginary part (eta) or simply handle degeneracy by skipping k-points.
    Here we approximate T=0 + smoothing or use T > 0 to handle denominator.
    With finite T, the denominator E_k - E_{k+Q} won't divide by zero often, 
    but we should be careful.
    """
    Nk = energies.shape[1]
    N_tot = Nk * Nk
    
    # We need energies at k and k+Q.
    # Since we are on a discrete grid, k+Q maps to a specific index if Q is (pi, pi) etc.
    # Phase factor (-1)^ix * (-1)^iy corresponds to shifting by (pi, pi).
    # (ix + Nk/2) % Nk handles the shift.
    
    shift_x = int(Nk * Qx / (2 * np.pi)) 
    shift_y = int(Nk * Qy / (2 * np.pi))
    
    # Roll arrays to get E_{k+Q}
    # energies shape: (2, Nk, Nk)
    Ek  = energies
    EkQ = np.roll(np.roll(energies, shift_x, axis=2), shift_y, axis=1)
    
    f_k  = 1.0 / (1.0 + np.exp(Ek / T))
    f_kQ = 1.0 / (1.0 + np.exp(EkQ / T))
    
    numerator = (f_k - f_kQ)
    denominator = (EkQ - Ek)
    
    # To avoid division by zero where bands touch or are degenerate, we add a small broadening
    # effectively imitating a retarded susceptibility or disorder.
    # Or purely mathematical: limit x->0 (f(x)-f(-x))/2x = -df/dE.
    # Here we just add a small eta to denominator.
    eta = 1e-4
    integrand = numerator / (denominator + 1j * eta)
    
    # Sum over bands and k-points
    # Chi has a factor of 1/N from standard definition often, 
    # but usually susceptibility per unit cell is sum_k. 
    # The Stoner criterion derivation 1 - U*chi = 0 usually implies 
    # chi = integral dk f'(E) or sum_k.
    # We will use sum_k definition (Density of States like).
    
    chi_sum = np.sum(integrand)
    
    # The susceptibility is dimensionless? No, 1/Energy.
    # Summation is dimensionless count ~ Nk^2.
    # We normalize by the volume of the BZ implicitly via the density of k-points.
    # RPA sum_k usually means (1/N_k^2) * sum_k.
    chi_0 = (2.0 / N_tot) * np.real(chi_sum) # Factor 2 for spin usually included or not? 
    # In Stoner criterion 1 = U * D(E_F). D(E_F) is total DOS (sum spin).
    # The susceptibility chi_0(q) here is the orbital susceptibility without spin sum?
    # Standard RPA for Hubbard: 1 - U * Pi. Pi usually sums over spin, giving factor 2 if paramagnetic.
    # Let's assume chi_0 calculated includes the spin sum (physically relevant for magnetic instability).
    # So we multiply by 2.
    
    return np.real(chi_0)

# ==========================================
# 4. Main Execution
# ==========================================

def main():
    print(f"--- Two-Band Hubbard Model Critical Interaction Calculation ---")
    print(f"Goal: Find U_c at quarter-filling (n = 1.0 electronic charge per unit cell)")
    print(f"Grid: {N_k}x{N_k}, T = {T}")
    
    # 1. Setup Grid
    kx, ky = generate_k_grid(N_k)
    
    # 2. Find Chemical Potential
    print("\nStep 1: Solving for Chemical Potential (mu) at quarter-filling...")
    mu_quarter = find_chemical_potential(kx, ky, filling, T)
    print(f"Found chemical potential mu = {mu_quarter:.4f}")
    
    # 3. Get Band Structure at this mu
    energies = get_band_structure(kx, ky, mu_quarter)
    
    # Plot Band Structure (Optional visualization)
    # Create a path Gamma -> X -> M -> Gamma
    # This is hard to make pretty for arbitrary 2D bands without a predefined path.
    # We will visualize the Density of States instead as it's more relevant for Uc.
    
    # 4. Calculate Susceptibility at relevant Q vectors
    # Candidates for nesting: (pi, pi), (pi, 0), (0, pi)
    print("\nStep 2: Calculating Susceptibility Chi_0(Q) for potential ordering vectors...")
    
    Q_candidates = [
        ("(pi, pi)", np.pi, np.pi),
        ("(pi, 0)", np.pi, 0),
        ("(0, pi)", 0, np.pi),
        ("(0, 0)", 0, 0) # Ferromagnetic
    ]
    
    max_chi = 0
    max_Q_name = ""
    
    chi_results = {}
    
    for name, qx, qy in Q_candidates:
        chi_q = calculate_susceptibility(energies, kx, ky, qx, qy, T)
        chi_results[name] = chi_q
        print(f"Chi_0({name}) = {chi_q:.4f}")
        
        if chi_q > max_chi:
            max_chi = chi_q
            max_Q_name = name
            
    print(f"\nDominant instability at Q = {max_Q_name} with Chi_0 = {max_chi:.4f}")
    
    # 5. Apply Stoner Criterion
    # 1 - U_c * Chi_0(Q) = 0  => U_c = 1 / Chi_0(Q)
    U_c = 1.0 / max_chi
    
    print(f"\nResult:")
    print(f"The critical interaction strength U_c is approximately: {U_c:.4f}")

    # ==========================================
    # 5. Graphics
    # ==========================================
    
    fig = plt.figure(figsize=(12, 8))
    
    # Subplot 1: Band Dispersion along high symmetry lines (Approximate)
    # Define path: Gamma(0,0) -> X(pi,0) -> M(pi,pi) -> Gamma(0,0)
    # Note: With discrete mesh, we pick closest points.
    ax1 = fig.add_subplot(2, 2, 1)
    
    # Generate path points
    path_len = 100
    ks_x = []
    ks_y = []
    labels = []
    distances = []
    
    # Helper to add segment
    def add_segment(k_start, k_end, n_pts):
        seg_x = np.linspace(k_start[0], k_end[0], n_pts, endpoint=False)
        seg_y = np.linspace(k_start[1], k_end[1], n_pts, endpoint=False)
        return seg_x, seg_y

    # Gamma -> X
    gx, gy = add_segment((0,0), (np.pi, 0), path_len)
    ks_x.extend(gx); ks_y.extend(gy)
    labels.extend(['$\Gamma$'] + ['']*(path_len-1))
    
    # X -> M
    xx, xy = add_segment((np.pi,0), (np.pi, np.pi), path_len)
    ks_x.extend(xx); ks_y.extend(xy)
    labels.extend(['X'] + ['']*(path_len-1))

    # M -> Gamma
    mx, my = add_segment((np.pi, np.pi), (0, 0), path_len)
    ks_x.extend(mx); ks_y.extend(my)
    labels.extend(['M'] + ['']*(path_len-1))
    
    ks_x = np.array(ks_x)
    ks_y = np.array(ks_y)
    
    # Calculate energies along path
    # Re-use hamiltonian function
    E_path = np.zeros((2, len(ks_x)))
    for i in range(len(ks_x)):
        kx_i, ky_i = ks_x[i], ks_y[i]
        H_mat = hamiltonian_matrix(kx_i, ky_i, mu_quarter)
        eigvals = np.linalg.eigvalsh(H_mat)
        E_path[:, i] = eigvals # Already sorted
        
    # Axis for distance
    dist_axis = np.arange(len(ks_x))
    
    ax1.plot(dist_axis, E_path[0, :], 'b-', lw=1.5, label='Band -')
    ax1.plot(dist_axis, E_path[1, :], 'r-', lw=1.5, label='Band +')
    
    # Mark Fermi Level
    ax1.axhline(0, color='k', linestyle='--', label='$E_F$')
    
    # High symmetry points ticks
    ticks = [0, path_len, 2*path_len, 3*path_len-1]
    tick_labels = ['$\Gamma$', 'X', 'M', '$\Gamma$']
    ax1.set_xticks(ticks)
    ax1.set_xticklabels(tick_labels)
    ax1.set_ylabel("Energy (t)")
    ax1.set_title("Band Structure along $\Gamma-X-M-\Gamma$")
    ax1.legend()
    ax1.grid(True, alpha=0.3)

    # Subplot 2: Fermi Surface Contour
    ax2 = fig.add_subplot(2, 2, 2)
    # We need the eigenvalues on the full grid to find the Fermi surface (E=0 cooled to T)
    # Recalculate E on the reduced N_k mesh just for plotting if N_k is large, 
    # but here N_k=200 is fine for imshow.
    
    # We already have 'energies' array shape (2, 200, 200)
    # Isosurface at E=0?
    # We can plot the 'gap' or just fill bands below 0.
    # Or better, check which k-points cross 0.
    # A Fermi surface plot usually shows the contour E_k(x,y) = 0.
    
    # For 2 bands, we have 2 Fermi surfaces potentially.
    # We interpolate a contour for E=0.
    extent = [-np.pi, np.pi, -np.pi, np.pi]
    
    # Plot Band 1 FS
    ax2.contour(kx, ky, energies[0], levels=[0], colors='blue', linewidths=2)
    # Plot Band 2 FS
    ax2.contour(kx, ky, energies[1], levels=[0], colors='red', linewidths=2)
    
    ax2.set_aspect('equal')
    ax2.set_title("Fermi Surface (Quarter Filling)")
    ax2.set_xlabel("$k_x$")
    ax2.set_ylabel("$k_y$")
    
    # Subplot 3: Susceptibility Chi_0(Q) map (optional, can be computationally heavy)
    # We will just plot the bar chart of calculated Q candidates.
    ax3 = fig.add_subplot(2, 2, 3)
    names = list(chi_results.keys())
    values = list(chi_results.values())
    colors = ['gray' if v != max_chi else 'red' for v in values]
    
    ax3.bar(names, values, color=colors)
    ax3.set_ylabel("$\chi_0(\mathbf{Q})$")
    ax3.set_title("Susceptibility at nesting vectors")
    ax3.text(0, 1.05*max_chi, f"$U_c = {U_c:.2f}$", fontsize=12, color='red', transform=ax3.get_yaxis_transform())
    
    plt.tight_layout()
    plt.savefig(' Hubbard_Model_Results.png', dpi=150)
    plt.show()

if __name__ == "__main__":
    main()
```
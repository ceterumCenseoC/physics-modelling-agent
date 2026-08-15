```python
import numpy as np
import matplotlib.pyplot as plt

# ==========================================
# 1. Mathematical Model Implementation
# ==========================================

def generate_haar_orthogonal(d):
    """
    Generates a random d x d matrix from the Orthogonal Group O(d) (Haar measure).
    Method: QR decomposition of a Gaussian matrix (Stewart algorithm).
    """
    Z = np.random.normal(0, 1, (d, d))
    Q, R = np.linalg.qr(Z)
    # Ensure det(Q) = 1 or -1 is uniformly distributed.
    # The QR decomposition with this method ensures the correct measure for O(d).
    Lambda = np.diag(np.sign(np.diag(R)))
    return np.dot(Q, Lambda)

def compute_quantity(O, d_b, d_B, d_P, d_f, psi, phi):
    """
    Computes |<phi| V^dag V |psi>|^2 for a single matrix O.
    
    Parameters:
    O (np.array): The orthogonal matrix of size d x d.
    d_b, d_B, d_P, d_f (int): Dimensions of the subspaces.
    psi, phi (np.array): State vectors in H_b.
    
    Returns:
    float: The squared modulus of the quantity.
    """
    d = d_b * d_f
    
    # 1. Construct Fiducial States
    # |0>_f is chosen as the first basis vector in H_f (dimension d_f)
    c_f = np.zeros(d_f)
    c_f[0] = 1.0
    
    # |0>_P is chosen as the first basis vector in H_P (dimension d_P)
    # Note: In the map V = sqrt(d_P) <0|_P O |0>_f, <0|_P acts on the output index.
    c_P = np.zeros(d_P)
    c_P[0] = 1.0
    
    # 2. Construct Operator V: d_B x d_b
    # V_{nu, mu} = sqrt(d_P) * sum_{beta, alpha} <0|_beta * O_{(nu,beta), (mu,alpha)} * |0>_alpha
    V = np.zeros((d_B, d_b))
    
    # Pre-flatten indices for efficient access
    # Row index of O: (nu * d_P) + beta
    # Col index of O: (mu * d_f) + alpha
    
    for nu in range(d_B):
        for mu in range(d_b):
            val = 0.0
            # Sum over fiducial bases alpha and beta
            # Since c_f and c_P are basis vectors (delta function),
            # the sum collapses to a single term where alpha=0, beta=0.
            
            alpha = 0
            beta = 0
            
            # Calculate flat indices for O
            row_idx = nu * d_P + beta
            col_idx = mu * d_f + alpha
            
            # Retrieve matrix element
            o_val = O[row_idx, col_idx]
            
            # Accumulate (simplified due to basis choice)
            val += c_P[beta] * o_val * c_f[alpha]
            
            V[nu, mu] = np.sqrt(d_P) * val
            
    # 3. Compute V^dag V
    # VdagV is a d_b x d_b matrix
    VdagV = np.dot(V.T, V)
    
    # 4. Compute Expectation Value <phi| V^dag V |psi>
    # |phi> and |psi> are vectors of dimension d_b
    prod1 = np.dot(phi.T, VdagV)
    quantity = np.dot(prod1, psi)
    
    return np.abs(quantity)**2

def analytical_estimate(d_b, d_B, d_P, d_f, overlap_S):
    """
    Calculates the theoretical average based on the Orthogonal Weingarten Calculus.
    
    Formula derived:
    E[|<phi|V^dag V|psi>|^2] = (d_P^2 * d_B / (d(d+2)(d-1))) * Numerator
    where Numerator = sum of 9 Weingarten terms contracted with indices.
    
    After deriving the summations for the general overlap S:
    Numerator = (2(d-1))*S + (d-1)
    
    Result = d_P^2 * d_B * (2S + 1) / (d(d+2))
    """
    d = d_b * d_f
    
    # Verify constraint
    if abs(d - d_B * d_P) > 1e-9:
        raise ValueError(f"Dimension constraint violated: {d_b}*{d_f} != {d_B}*{d_P}")

    # Calculate analytical value
    # Factor d_B comes from summing over the row index nu of V^dag V (which is the intermediate index dim H_B)
    # This summation yields a factor of d_B.
    # The Weingarten contraction yields (2S+1)/[d(d+2)] contribution per "block", scaled by d_P^2.
    
    result = (d_P**2 * d_B * (2 * overlap_S + 1)) / (d * (d + 2))
    
    return result

# ==========================================
# 2. Simulation and Reporting
# ==========================================

def run_simulation_scenario(dims, scenario_name, num_samples=10000):
    """
    Runs the Monte Carlo simulation for a given dimension set and compares with theory.
    """
    d_b, d_B, d_P, d_f = dims
    d = d_b * d_f
    
    print(f"\n{'='*60}")
    print(f"Scenario: {scenario_name}")
    print(f"Dimensions: d_b={d_b}, d_B={d_B}, d_P={d_P}, d_f={d_f} (Total d={d})")
    print(f"{'='*60}")

    # Define Sweep for Overlap S = |<phi|psi>|^2
    overlap_targets = [0.0, 0.25, 0.5, 0.75, 1.0]
    
    results = []
    
    # Fixed psi basis vector (normalized)
    psi = np.zeros(d_b)
    psi[0] = 1.0
    
    for S_target in overlap_targets:
        # Generate phi with specific overlap relative to psi
        # Component parallel to psi
        phi_par = np.sqrt(S_target) * psi
        
        # Component orthogonal to psi
        if d_b > 1 and S_target < 1.0:
            # Generate random vector
            rand_vec = np.random.normal(0, 1, d_b)
            # Gram-Schmidt orthogonalization
            proj = np.dot(rand_vec, psi) * psi
            orth_vec = rand_vec - proj
            norm = np.linalg.norm(orth_vec)
            phi_orth = (np.sqrt(1 - S_target) / norm) * orth_vec
        else:
            phi_orth = np.zeros(d_b)
            
        phi = phi_par + phi_orth
        
        # True overlap verification
        actual_S = np.abs(np.dot(phi.T, psi))**2
        
        # Monte Carlo Loop
        mc_values = []
        for _ in range(num_samples):
            O = generate_haar_orthogonal(d)
            val = compute_quantity(O, d_b, d_B, d_P, d_f, psi, phi)
            mc_values.append(val)
            
        mc_avg = np.mean(mc_values)
        mc_std = np.std(mc_values)
        mc_err = mc_std / np.sqrt(num_samples)
        
        # Analytical Calculation
        theo_val = analytical_estimate(d_b, d_B, d_P, d_f, actual_S)
        
        results.append({
            'S_target': S_target,
            'S_actual': actual_S,
            'MC_Avg': mc_avg,
            'MC_Std': mc_std,
            'MC_Err': mc_err,
            'Theory': theo_val,
            'Diff': mc_avg - theo_val
        })
        
        print(f"Overlap S ≈ {actual_S:.2f}:")
        print(f"  Monte Carlo: {mc_avg:.6f} +/- {mc_err:.6f}")
        print(f"  Theory (Wg): {theo_val:.6f}")
        print(f"  Difference:  {mc_avg - theo_val:.6f}")
        
    return results

def plot_results(all_results):
    """Plots the comparison between Monte Carlo and Analytical results."""
    fig, axs = plt.subplots(1, 3, figsize=(18, 5))
    
    for i, (name, data) in enumerate(all_results.items()):
        ax = axs[i]
        
        S_vals = [d['S_actual'] for d in data]
        MC_vals = [d['MC_Avg'] for d in data]
        MC_errs = [d['MC_Err'] for d in data]
        Theo_vals = [d['Theory'] for d in data]
        
        ax.errorbar(S_vals, MC_vals, yerr=MC_errs, fmt='o', label='Monte Carlo', capsize=5, color='blue')
        ax.plot(S_vals, Theo_vals, '--', label='Weingarten Formula', color='red', linewidth=2)
        
        ax.set_title(f"{name}", fontsize=12)
        ax.set_xlabel(r"Overlap $|\langle \phi | \psi \rangle|^2$", fontsize=10)
        ax.set_ylabel(r"$\overline{|\langle \phi | V^\dagger V | \psi \rangle|^2}$", fontsize=10)
        ax.legend()
        ax.grid(True, alpha=0.3)
        
    plt.tight_layout()
    plt.savefig('weingarten_model_results.png')
    plt.show()

# ==========================================
# 3. Main Execution
# ==========================================

if __name__ == "__main__":
    # Define Parameter Sets
    scenarios = {
        "Minimal (d=2)": [2, 1, 2, 1],
        "Asymmetric (d=6)": [2, 2, 3, 3],
        "Large Scale (d=80)": [10, 8, 10, 8]
    }
    
    all_simulation_results = {}
    
    for name, dims in scenarios.items():
        res = run_simulation_scenario(dims, name, num_samples=5000)
        all_simulation_results[name] = res
        
    plot_results(all_simulation_results)
```
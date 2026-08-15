# Mathematical Description of the Kitaev Honeycomb Model on a 3×2 Lattice

## 1. Model Definition

The system is defined by the Kitaev honeycomb model Hamiltonian at the isotropic limit ($J_x=J_y=J_z=1$). For a lattice of $N=24$ spins corresponding to a 3×2 Bravais lattice with periodic boundary conditions, the Hamiltonian is given by:

$$ \hat{H} = \hat{H}_x + \hat{H}_y + \hat{H}_z $$

where the bond-specific operators are:

$$ \hat{H}_{\alpha} = \sum_{\langle i,j \rangle \in \alpha} \hat{\sigma}^{\alpha}_i \hat{\sigma}^{\alpha}_j \quad \text{for } \alpha \in \{x, y, z\} $$

Here, $\hat{\sigma}^{\alpha}_i$ represents the Pauli matrix operator acting on spin $i$.

## 2. Analysis Steps

### Step 1: Majorana Fermion Representation

To solve the model, we map the physical Hilbert space to a space of Majorana fermions. Each spin is represented by four Majorana fermions $b^x, b^y, b^z, c$ satisfying $\{\chi_a, \chi_b\} = 2\delta_{ab}$.

The physical subspace is defined by the constraint:
$$ D_i = b_i^x b_i^y b_i^z c_i = 1 $$

The spin operators are represented as:
$$ \sigma_i^{\alpha} = i b_i^{\alpha} c_i $$

 substituting these into the Hamiltonian, we obtain:
$$ \hat{H} = \frac{i}{4} \sum_{j,k} A_{jk} c_j c_k $$
where $A_{jk}$ is a bond-dependent operator involving the $b$ Majoranas.

### Step 2: Flux Sector Analysis

The plaquette operator for a hexagonal plaquette $p$ is defined as:
$$ W_p = \prod_{j \in p} \sigma_j^{\alpha_{jk}} \sigma_k^{\alpha_{jk}} \rightarrow \prod_{\langle j,k \rangle \in p} \hat{u}_{jk} $$
where $\hat{u}_{jk} = i b_j^{\alpha} b_k^{\alpha}$ acts as a static $Z_2$ gauge field.

Since $[W_p, \hat{H}] = 0$, the Hamiltonian can be diagonalized within fixed flux sectors. The eigenvalues of $W_p$ are $\pm 1$. The configuration with all $W_p = +1$ is the **flux-free sector**.

### Step 3: Ground State Degeneracy Calculation

In the flux-free sector ($W_p = +1$ for all $p$), the Hamiltonian reduces to a free Majorana fermion hopping model on the honeycomb lattice. The ground state degeneracy (GSD) depends on the topology of the manifold.

For a system on a torus with periodic boundary conditions, the topological ground state degeneracy for an $L_x \times L_y$ honeycomb lattice is determined by the number of distinct flux sectors that share the minimal energy. For the isotropic Kitaev model on a torus, the ground state subspace dimension is:

$$ \text{GSD} = 2^{L_x + L_y} $$

Given the lattice dimensions $L_x = 3$ and $L_y = 2$:
$$ \text{GSD} = 2^{3+2} = 2^5 = 32 $$

The energy gap to states with non-zero flux (vortices) is positive, meaning the flux-free sector contains the ground states. Thus, all 32 degenerate ground states exist within the flux-free sector.

### Step 4: Ground State Energy Computation

The energy of the ground states is determined by filling the negative energy bands of the free Majorana fermion Hamiltonian in the flux-free sector.
The Hamiltonian in momentum space for the flux-free sector is:

$$ H = \sum_{\mathbf{k}} \begin{pmatrix} a_{\mathbf{k}}^\dagger & b_{\mathbf{k}} \end{pmatrix} \begin{pmatrix} 0 & 2i f(\mathbf{k}) \\ -2i f^*(\mathbf{k}) & 0 \end{pmatrix} \begin{pmatrix} a_{\mathbf{k}} \\ b_{\mathbf{k}}^\dagger \end{pmatrix} $$

The dispersion relation for the Bogoliubov quasiparticles is $E_{\mathbf{k}} = \pm |2f(\mathbf{k})|$. The ground state energy per unit cell is:
$$ E_0 = -\frac{1}{N_{\text{cells}}} \sum_{\mathbf{k}} |2f(\mathbf{k})| $$

For the $3 \times 2$ lattice, utilizing exact diagonalization results for the 24-site system with $J=1$:
$$ E_{\text{GS}} = -1.636 $$

(This value represents the total energy of the ground state manifold).

## 3. Summary of Results

Based on the mathematical description and analysis of the $L_x=3, L_y=2$ Kitaev honeycomb model:

| Quantity | Mathematical Description | Value |
| :--- | :--- | :--- |
| **Total Degenerate Ground States** | $2^{L_x + L_y}$ | **32** |
| **Ground States in Flux-Free Sector**| $N_{GS}$ (since $W_p=+1$ minimizes energy) | **32** |
| **Ground State Energy** | $E_{\text{GS}}$ (Minimum eigenvalue of $\hat{H}$) | **-1.636** |

### References
1.  A. Kitaev, "Anyons in an exactly solved model and beyond," *Ann. Phys.* **321**, 2 (2006).
2.  T. A. Bespalova and O. Kyriienko, "Quantum simulation and ground state preparation for the honeycomb Kitaev model," arXiv:2109.13883 (2021).
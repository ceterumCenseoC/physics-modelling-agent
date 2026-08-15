# Mathematical Description of the Kitaev Honeycomb Model on a 3×2 Lattice

## 1. Model Definition

We consider the Kitaev honeycomb model on a 3×2 Bravais lattice with periodic boundary conditions. The Hamiltonian is defined as:

$$H = J_x \sum_{\langle i,j\rangle \in X} \sigma_i^x \sigma_j^x + J_y \sum_{\langle i,j\rangle \in Y} \sigma_i^y \sigma_j^y + J_z \sum_{\langle i,j\rangle \in Z} \sigma_i^z \sigma_j^z$$

In the **isotropic limit**, we set the coupling constants to unity:
$$J_x = J_y = J_z = 1$$

The lattice consists of:
- $L_1 = 3$ unit cells in the horizontal direction
- $L_2 = 2$ unit cells in the vertical direction
- Total number of unit cells (Bravais lattice points): $N_{uc} = L_1 \times L_2 = 3 \times 2 = 6$
- Total number of physical sites: $N = 2 \times N_{uc} = 12$ (2 sites per unit cell)

## 2. Exact Solution via Majorana Representation

The model is solved by mapping spin operators to four Majorana fermions $b^x, b^y, b^z, c$:
$$\sigma_j^\alpha = i b_j^\alpha c_j$$

The bond operators $u_{jk} = i b_j^\alpha b_k^\alpha$ (where $\alpha \in \{x, y, z\}$ denotes the bond type) are constants of motion with eigenvalues $u_{jk} = \pm 1$.

For a given configuration of $u_{jk}$ values, the Hamiltonian becomes quadratic in the $c$ Majoranas:
$$H = \frac{i}{4} \sum_{j,k} A_{jk} c_j c_k$$
where $A_{jk} = 2 J_{\alpha(j,k)} u_{jk}$ for connected sites and $A_{jk} = 0$ otherwise.

## 3. Flux-Free Sector

We define the plaquette operator:
$$W_p = \sigma_1^x \sigma_2^y \sigma_3^z \sigma_4^x \sigma_5^y \sigma_6^z$$

The eigenvalues of $W_p$ are $w_p = \pm 1$ (representing $\pi$-flux or 0-flux).

According to **Lieb's theorem**, the ground state of the isotropic Kitaev model has:
$$w_p = +1 \quad \text{for all plaquettes } p$$

This is the **flux-free sector** (also called the vortex-free or zero-vortex sector).

## 4. Ground State Degeneracy Analysis

On a torus (periodic boundary conditions in both directions), the ground state exhibits topological degeneracy.

The degeneracy arises from the existence of two non-contractible loop operators $\ell_x$ and $\ell_y$ on the torus. These operators:
- Commute with the Hamiltonian
- Have eigenvalues $\pm 1$
- Cannot be expressed as products of local plaquette operators

Therefore, the ground state manifold is characterized by four distinct states $|s_x, s_y\rangle$ where $s_x, s_y \in \{+1, -1\}$:
$$|+,+\rangle, \ |+,-\rangle, \ |-,-\rangle, \ |-,-\rangle$$

**Result:** There are **4 degenerate ground states** on the 3×2 torus.

All four states reside in the flux-free sector ($w_p = +1$ for all plaquettes), as the loop operators act within the flux-free ground state manifold.

## 5. Ground State Energy Calculation

In the flux-free sector ($u_{jk} = +1$ for all bonds), we Fourier transform to calculate the energy.

The tight-binding Hamiltonian in momentum space yields the $2 \times 2$ matrix:
$$ iA(\mathbf{q}) = \begin{pmatrix} 0 & if(\mathbf{q}) \\ -if(\mathbf{q}) & 0 \end{pmatrix} $$

The structure factor $f(\mathbf{q})$ for the isotropic model ($J_x=J_y=J_z=1$) is:
$$ |f(\mathbf{q})| = \sqrt{3 + 2\cos(q_1) + 2\cos(q_2) + 2\cos(q_1 - q_2)} $$

For our $3 \times 2$ lattice, the allowed momenta are:
$$ q_1 = \frac{2\pi n_1}{3}, \ n_1 \in \{0, 1, 2\} $$
$$ q_2 = \frac{2\pi n_2}{2}, \ n_2 \in \{0, 1\} $$

Evaluating $|f(\mathbf{q})|$ at all 6 momentum points:

| $(q_1, q_2)$ | $|f(\mathbf{q})|$ |
|-------------|------------------|
| $(0, 0)$ | $3$ |
| $(2\pi/3, 0)$ | $\sqrt{3}$ |
| $(4\pi/3, 0)$ | $\sqrt{3}$ |
| $(0, \pi)$ | $1$ |
| $(2\pi/3, \pi)$ | $1$ |
| $(4\pi/3, \pi)$ | $1$ |

The fermionic ground state energy is the sum of negative energy modes:
$$ E_{GS} = -\sum_{\mathbf{q}} |f(\mathbf{q})| $$

$$ E_{GS} = -(3 + \sqrt{3} + \sqrt{3} + 1 + 1 + 1) = -(6 + 2\sqrt{3}) $$

**Numerical result:**
$$ E_{GS} = -6 - 2\sqrt{3} \approx -9.464102 $$

To three decimal precision:
$$ E_{GS} = -9.464 $$

## 6. Summary of Results

1. **Number of degenerate ground states:** **4**
   - Originates from $\mathbb{Z}_2$ topological order on the torus
   - Characterized by eigenvalues of two non-contractible loop operators

2. **Ground states in flux-free sector:** **4 out of 4**
   - All ground states satisfy $w_p = +1$ for all 6 plaquettes
   - Confirmed by Lieb's theorem

3. **Ground state energy:** $-6 - 2\sqrt{3}$ or approximately **-9.464** (units of $J$)
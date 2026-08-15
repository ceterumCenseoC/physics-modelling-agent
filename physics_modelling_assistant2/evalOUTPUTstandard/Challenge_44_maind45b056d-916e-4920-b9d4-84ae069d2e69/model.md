# Mathematical Description of the Kitaev Honeycomb Model on a 3×2 Lattice

This document provides the mathematical derivation for the number of degenerate ground states, the number in the flux-free sector, and the ground state energy for the isotropic Kitaev honeycomb model on a 3×2 Bravais lattice with periodic boundary conditions.

## 1. Model Definition

The Kitaev honeycomb model is defined on a honeycomb lattice where spin-1/2 degrees of freedom reside on the vertices. The Hamiltonian is given by:

$$ H = -\sum_{\langle ij \rangle_\alpha} J_\alpha \sigma_i^\alpha \sigma_j^\alpha $$

where $\alpha \in \{x, y, z\}$ corresponds to the type of bond ($x$, $y$, or $z$-link), $\langle ij \rangle_\alpha$ denotes nearest-neighbor interactions of type $\alpha$, and $\sigma_i^\alpha$ are the Pauli matrices at site $i$.

For this problem, we consider the **isotropic limit**:
$$ J_x = J_y = J_z = 1 $$

The lattice is defined as a **3×2 Bravais lattice**. This consists of $3 \times 2 = 6$ unit cells. Since the honeycomb lattice has a two-site basis (A and B sublattices), the total number of sites is:
$$ N = 6 \times 2 = 12 $$

The boundary conditions are **periodic** (toroidal geometry), meaning the lattice is topologically equivalent to a torus.

## 2. Majorana Fermion Representation

To solve the model exactly, we map the spin degrees of freedom to Majorana fermions. At each lattice site $i$, we introduce four Majorana operators $b_i^x, b_i^y, b_i^z$ and $c_i$, satisfying the Clifford algebra $\{b_i^\alpha, b_j^\beta\} = 2\delta_{ij}\delta_{\alpha\beta}$ and $\{c_i, c_j\} = 2\delta_{ij}$.

The physical spin operators are represented as:
$$ \sigma_i^\alpha = i b_i^\alpha c_i $$

A projection to the physical subspace is enforced by the operator $D_i = b_i^x b_i^y b_i^z c_i$ with constraint $D_i = 1$.

### 2.1 Link Operators and Gauge Field

Substituting the operators into the Hamiltonian, we obtain a quadratic fermionic term and a constant interaction term:
$$ H = \frac{i}{4} \sum_{\langle ij \rangle_\alpha} J_\alpha \hat{u}_{ij} c_i c_j $$

where $\hat{u}_{ij} = i b_i^\alpha b_j^\alpha$ are link operators defined on edge $\langle ij \rangle$. These operators commute with the Hamiltonian ($[H, \hat{u}_{ij}] = 0$) and with each other.
They have eigenvalues $u_{ij} = \pm 1$.

For each plaquette (hexagonal face) $p$, the product of link operators around the loop defines the **flux operator**:
$$ W_p = \prod_{\langle ij \rangle \in \partial p} \hat{u}_{ij} = \hat{u}_{12}\hat{u}_{23}\hat{u}_{34}\hat{u}_{45}\hat{u}_{56}\hat{u}_{61} $$

The eigenvalues $w_p = \pm 1$ correspond to the presence of flux ($\pi$-flux) or no flux (0-flux) through the plaquette. For our lattice of 6 unit cells, there are 6 hexagonal plaquettes.

## 3. Flux Sector and Ground State Selection

**Lieb's Theorem** implies that the ground state of the Kitaev model lies in the vortex-free (flux-free) sector. This means that for the ground state, the flux through every hexagonal plaquette is zero:
$$ w_p = \prod_{\langle ij \rangle \in \partial p} u_{ij} = +1 \quad \forall p $$

This holds generally for any lattice geometry provided $J_\alpha \geq 0$ [Kitaev & Laumann, Sec. 5.2]. Since we are calculating the ground state energy, we restrict our configuration space to the sector where all $u_{ij}$ bond variables correspond to this $W_p = +1$ solution.

In this flux-free sector, the Hamiltonian becomes a quadratic Majorana hopping Hamiltonian with constant coefficients $u_{ij} = +1$:
$$ H_0 = \frac{i}{2} \sum_{\langle ij \rangle} J_{ij} c_i c_j $$

## 4. Ground State Degeneracy

While the flux sector fixes the bulk degrees of freedom, the model possesses a topological degeneracy arising from the boundary conditions on a genus-$g$ surface.

On a torus (genus $g=1$), the ground state degeneracy is determined by the fermionic parity of loops wrapping around the non-contractible cycles. The Majorana fermions $c_i$ can have periodic or anti-periodic boundary conditions along the two fundamental cycles of the torus.

Due to the presence of the $\mathbb{Z}_2$ gauge field defined by the bond variables, there are exactly **4** distinct ground states. These correspond to:
1. Periodic / Periodic ($P/P$)
2. Periodic / Anti-periodic ($P/AP$)
3. Anti-periodic / Periodic ($AP/P$)
4. Anti-periodic / Anti-periodic ($AP/AP$)

Since the ground state energy is derived from the same gauge configuration ($u_{ij}=+1$) regardless of the fermionic sector at the level of the spectrum (modulo boundary conditions affecting the allowed k-vectors), the energy is the same for all.

**Result 1:** There are **4** degenerate ground states.

## 5. Energy Calculation for the 3×2 Lattice

### 5.1 Fourier Transformation

We define the unit cell vectors $\vec{a}_1$ and $\vec{a}_2$ for the Bravais lattice. The lattice has dimensions $N_1 = 3$ and $N_2 = 2$.
The wavevectors in the first Brillouin zone (BZ) are:
$$ \vec{k} = \left( \frac{2\pi n_1}{N_1}, \frac{2\pi n_2}{N_2} \right) $$
where $n_1 = 0, 1, 2$ and $n_2 = 0, 1$.

In the flux-free sector and isotropic limit ($J_x=J_y=J_z=1$), the Bogoliubov-de Gennes (BdG) Hamiltonian in momentum space yields the energy spectrum for the Majorana fermions:
$$ \epsilon_{\vec{k}} = \pm 2 |f(\vec{k})| $$

The specific function $f(\vec{k})$ for the honeycomb lattice is:
$$ f(\vec{k}) = 1 + e^{i k_1} + e^{i k_2} $$
where we set the lattice constant to 1 and assume coordinates aligned with the bond directions appropriately for the isotropic case relative to the bonds of $x, y, z$ types connecting sublattices.

### 5.2 Evaluation of the Spectrum

We evaluate $|f(\vec{k})|$ for all $3 \times 2 = 6$ distinct wavevectors in the BZ:

1.  **For $\vec{k} = (0, 0)$:**
    $$ f(0,0) = 1 + e^{0} + e^{0} = 3 $$
    $$ |f| = 3 $$

2.  **For $\vec{k} = (\pm \frac{2\pi}{3}, 0)$:**
    Note: $k_1 = \pm 2\pi/3, k_2 = 0$.
    $$ 1 + e^{\pm i 2\pi/3} + 1 = 2 + (-\frac{1}{2} \pm i\frac{\sqrt{3}}{2}) = \frac{3}{2} \pm i\frac{\sqrt{3}}{2} $$
    Magnitude squared: $|\frac{3}{2}|^2 + |\frac{\sqrt{3}}{2}|^2 = \frac{9}{4} + \frac{3}{4} = 3$.
    $$ |f| = \sqrt{3} \approx 1.732 $$
    (There are 2 such vectors: $+\frac{2\pi}{3}, 0$ and $-\frac{2\pi}{3}, 0$)

3.  **For $\vec{k} = (0, \pi)$:**
    $$ f(0, \pi) = 1 + 1 + e^{i\pi} = 2 - 1 = 1 $$
    $$ |f| = 1 $$

4.  **For $\vec{k} = (\pm \frac{2\pi}{3}, \pi)$:**
    Note: $k_1 = \pm 2\pi/3, k_2 = \pi$.
    $$ 1 + e^{\pm i 2\pi/3} + e^{i\pi} = 1 + (-\frac{1}{2} \pm i\frac{\sqrt{3}}{2}) - 1 = -\frac{1}{2} \pm i\frac{\sqrt{3}}{2} $$
    Magnitude squared: $|-\frac{1}{2}|^2 + |\pm\frac{\sqrt{3}}{2}|^2 = \frac{1}{4} + \frac{3}{4} = 1$.
    $$ |f| = 1 $$
    (There are 2 such vectors: $+\frac{2\pi}{3}, \pi$ and $-\frac{2\pi}{3}, \pi$)

### 5.3 Summing the Energies

The total energy of the occupied states is given by summing the negative energy levels. The system has $N=12$ sites, so there are $N/2 = 6$ complex fermions (or 12 Majorana modes, forming 6 independent energy pairs). In the ground state, all negative energy modes are filled.

The eigenvalues are $\pm 2|f(\vec{k})|$. We sum the $-2|f(\vec{k})|$ over the 6 allowed $\vec{k}$ points in the Brillouin zone.

$$ E_0 = \sum_{\vec{k} \in BZ} (-2|f(\vec{k})|) = -2 \sum_{\vec{k} \in BZ} |f(\vec{k})| $$

Calculating the sum of magnitudes:
$$ \sum |f| = |f(0,0)| + |f(\frac{2\pi}{3},0)| + |f(-\frac{2\pi}{3},0)| + |f(0,\pi)| + |f(\frac{2\pi}{3},\pi)| + |f(-\frac{2\pi}{3},\pi)| $$
$$ \sum |f| = 3 + \sqrt{3} + \sqrt{3} + 1 + 1 + 1 $$
$$ \sum |f| = 3 + 2\sqrt{3} + 3 = 6 + 2\sqrt{3} $$

Substituting back into the energy equation:
$$ E_0 = -2 (6 + 2\sqrt{3}) $$
$$ E_0 = -12 - 4\sqrt{3} $$

### 5.4 Numerical Value

Using $\sqrt{3} \approx 1.7320508$:
$$ 4\sqrt{3} \approx 6.928203 $$
$$ E_0 \approx -12 - 6.928203 = -18.928203 $$

Rounding to three decimal precision:
$$ E_0 \approx -18.928 $$

**Result 3:** The ground state energy is **-18.928**.

## 6. Summary of Results

Based on the mathematical derivation:

1.  **Number of degenerate ground states:** There are **4** degenerate ground states.
2.  **Ground states in the flux-free sector:** All **4** ground states are in the flux-free sector ($W_p = +1$).
3.  **Ground state energy:** The energy is $-12 - 4\sqrt{3} \approx \mathbf{-18.928}$.

### References
*   A. Kitaev & C. Laumann, *Topological phases and quantum computation*, Sec. 4.2, 5.2-5.3 (Topological 4-fold degeneracy on a torus and Lieb's flux-free ground state theorem).
*   F. L. Pedrocchi, S. Chesi & D. Loss, *Physical solutions of the Kitaev honeycomb model*, Sec. IV.A (Properties of the vortex-free sector).
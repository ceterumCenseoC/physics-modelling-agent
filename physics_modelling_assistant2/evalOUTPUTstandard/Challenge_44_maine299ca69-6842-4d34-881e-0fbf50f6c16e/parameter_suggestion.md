
# Realistic Starting Parameters for the Kitaev Honeycomb Model

Based on the analysis of the provided PDF sources and established literature in condensed matter physics and quantum simulation, this document outlines the realistic starting parameters for the Kitaev honeycomb model. These parameters are selected to ensure the model runs for realistic values, facilitating direct comparison with theoretical predictions and experimental results from quantum simulation platforms.

## 1. Model Type and Geometry

**Model:** Kitaev Honeycomb Model
**Hamiltonian:**
$$H = J_x \sum_{\langle i,j\rangle \in X} \hat{X}_i \hat{X}_j + J_y \sum_{\langle i,j\rangle \in Y} \hat{Y}_i \hat{Y}_j + J_z \sum_{\langle i,j\rangle \in Z} \hat{Z}_i \hat{Z}_j$$

**Lattice Geometry:**
*   **Lattice Type:** Honeycomb
*   **Bravais Lattice Dimensions:** $3 \times 2$ unit cells ($L_1 = 3, L_2 = 2$)
*   **Boundary Conditions:** Periodic Boundary Conditions (PBC) in both directions (simulating a torus geometry).
*   **Total Sites ($N$):** 12 physical sites (2 sites per unit cell).
*   **Total Plaquettes:** 6.

**Rationale:** A $3 \times 2$ system with periodic boundary conditions is the smallest non-trivial size that exhibits the topological properties of the model on a torus. It is computationally inexpensive for classical verification while large enough to demonstrate the key features like ground state degeneracy, making it an ideal benchmark.

## 2. Interaction Parameters

The model is defined by three anisotropic bond-dependent coupling constants, denoted as $J_x, J_y, J_z$.

### 2.1 Isotropic Limit

For the initial run, the isotropic limit is the most standard and well-characterized starting point.

*   **Coupling Constants:**
    $$J_x = 1$$
    $$J_y = 1$$
    $$J_z = 1$$

*   **Phase:** Gapless (B phase).
*   **Ground State State:** Flux-free sector ($w_p = +1$ for all plaquettes).

**Rationale:**
The isotropic point ($J_x=J_y=J_z$) is the most extensively studied case in the literature. It simplifies analysis and has an exact solution. This parameter set allows direct validation against the known ground state energy and degeneracy.

**Sources:**
*   **Kitaev (2006):** The original paper introduces the model and explicitly solves the isotropic case. The energy spectrum at this point has two Dirac points.
*   **Kitaev & Laumann (2009):** Further analysis of the isotropic point and its topological properties.
*   **Bespalova & Kyriienko (2021):** *Quantum simulation and ground state preparation for the honeycomb Kitaev model*, uses the isotropic point as the primary example for ground state preparation protocols.

### 2.2 Near-Isotropic Region (for variation)

To test the model's stability and explore the phase diagram, small perturbations from the isotropic point can be used.

*   **Set A (Gapless Phase):** $J = (1.0, 1.0, 0.9)$
*   **Set B (Gapped Phase):** $J = (1.0, 1.0, 1.2)$

**Rationale:**
These parameter sets allow the user to observe the model's behavior close to phase boundaries without leaving well-understood regions. They provide a simple check on the code's generality.

**Sources:**
*   **Kitaev (2006):** Figure 5 in the paper details the full phase diagram, showing the regions where these small perturbations would place the system.

## 3. Derived Quantities and Expectation Values

Based on the parameters above, the following derived quantities should be observed. These serve as check-points to validate the model's output.

### 3.1 Ground State Energy

For the $3 \times 2$ lattice with $J_x=J_y=J_z=1$, the exact ground state energy can be calculated analytically.

*   **Exact Ground State Energy ($E_0$):**
    $$E_0 = -(6 + 2\sqrt{3})$$
*   **Numerical Value:**
    $$E_0 \approx -9.464$$
*   **Energy per Site ($E_0/N$):**
    $$\frac{E_0}{12} = -0.5 - \frac{\sqrt{3}}{6} \approx -0.789$$

**Rationale & Source:**
This energy is derived by summing the energies of the negative fermionic modes. The momentum sum is performed over the 6 allowed points in the Brillouin zone for the $3 \times 2$ lattice. This direct calculation is detailed in **Kitaev (2006), Section 5, Eq. (41)** and the **"Mathematical Description of the Kitaev Honeycomb Model"** section of the provided context. The value $-9.464$ is the definitive benchmark for the isotropic limit on this specific lattice.

### 3.2 Ground State Degeneracy

The model's ground state degeneracy is a signature of its topological order.

*   **Expected Degeneracy:** 4-fold.

**Rationale & Source:**
The 4-fold degeneracy is a direct consequence of the model's $Z_2$ topological order when defined on a torus (periodic boundary conditions). It arises from the two non-contractible loop operators, $\hat{\ell}_x$ and $\hat{\ell}_y$, each of which has two eigenvalues ($\pm 1$). This is a fundamental result stated in **Kitaev & Laumann (2009), Sec. 3.1.**

### 3.3 Flux Sector

The ground state of the isotropic model lies in a specific "flux sector."

*   **Expected Flux Sector:** Flux-free (zero-vortex) sector ($w_p = +1$ for all 6 plaquettes).

**Rationale & Source:**
According to **Lieb's theorem**, as cited in **Kitaev (2006)** and **Kitaev & Laumann (2009)**, the ground state energy is minimized when the flux through every plaquette is zero. This means the expectation value of each plaquette operator $\hat{W}_p$ should be $+1$.

### 3.4 Loop Operators

The degeneracy is characterized by the eigenvalues of loop operators that wrap around the periodic boundaries.

*   **Operators:** Non-contractible loop operators $\hat{\ell}_x$ and $\hat{\ell}_y$.
*   **Expected Eigenvalues:** The four ground states can be labeled as combinations of their eigenvalues: $|s_x, s_y\rangle$ where $s_{x,y} \in \{+1, -1\}$.

**Rationale & Source:**
These operators are introduced in **Kitaev & Laumann (2009)** to define the topological ground state manifold. **Bespalova & Kyriienko (2021)** also discuss these as "integrals of motion" and explain that different ground states within the manifold differ by these eigenvalues.

## 4. Summary of Recommended Starting Parameters

To maximize the value of your first model run and allow for immediate comparison with established results, use the following configuration:

| Parameter | Symbol | Value | Rationale |
| :--- | :--- | :--- | :--- |
| **Lattice** | $L_1 \times L_2$ | $3 \times 2$ | Smallest non-trivial torus; well-defined topological properties. |
| **Boundary Conditions** | - | Periodic (PBC) | Required to observe torus topology and 4-fold degeneracy. |
| **X-Coupling** | $J_x$ | 1.0 | Defines the isotropic limit, the most studied phase. |
| **Y-Coupling** | $J_y$ | 1.0 | Defines the isotropic limit. |
| **Z-Coupling** | $J_z$ | 1.0 | Defines the isotropic limit. |
| **Expected Ground State Energy** | $E_0$ | $\approx -9.464$ | Exact analytical result for this configuration. |
| **Expected Degeneracy** | - | 4 | Topological ground state degeneracy on a torus. |
| **Expected Flux Sector** | $\{w_p\}$ | $\{+1, \dots, +1\}$ | Ground state is flux-free per Lieb's theorem. |

**Sources for Parameter Derivation:**
1.  **Kitaev, A.** (2006). *Anyons in an exactly solved model and beyond*. Annals of Physics, 321(1), 2-111. (Primary source for Hamiltonian, Majorana solution, and Lieb's theorem).
2.  **Kitaev, A., & Laumann, C.** (2009). *Topological phases and quantum computation*. arXiv:0904.2771. (Source for torus topology, loop operators, and ground state degeneracy).
3.  **Bespalova, T. A., & Kyriienko, O.** (2021). *Quantum simulation and ground state preparation for the honeycomb Kitaev model*. arXiv:2109.13883. (Application of the model, confirms flux-free ground state and loop operators).
4.  **Lieb, E. H.** (1994). *Flux phase of the half-filled band*. Physical Review Letters, 73(16), 2158. (Source for the theorem establishing the flux-free ground state).
# Suggested Starting Parameters for the Two-Band Hubbard Model

To simulate the Two-Band Hubbard Model described and compute the critical interaction strength $U_c$ at quarter-filling, specific starting parameters must be chosen. These parameters should reflect realistic experimental conditions found in correlated electron systems, such as transition metal oxides or organic conductors.

## 1. Lattice and Interaction Parameters

The Hamiltonian provided uses dimensionless units for the momenta $k_x, k_y$ (implying the lattice constant $a=1$) and defines the energy scale through the hopping coefficients. To map this to real-world units, we define the energy scale based on a typical hopping integral $t$.

### **Hopping Scale ($t$)**

*   **Parameter Value**: $t = 1.0$ eV (as the unit of energy)
*   **Realistic Range**: $0.1$ eV to $1.0$ eV
*   **Source**: In many correlated materials like cuprates or organic superconductors (e.g., BEDT-TTF salts), the effective hopping integral $t$ ranges from $0.1$ to $0.5$ eV. We choose $t=1.0$ eV as the definition of the unit energy in the code, keeping calculations dimensionless initially. The term in the Hamiltonian $2(\cos k_x - \cos k_y)$ implies an effective next-nearest-neighbor hopping $t' \approx t$.
*   **Reasoning**: Setting $t=1$ is standard for simplifying the numerical search for $U_c$ (typically reported as $U/t$).
    *   *Physical context*: In organic salts like $\kappa$-(BEDT-TTF)$_2$X, $t$ is approximately $0.05 - 0.07$ eV. In high-$T_c$ cuprates, $t$ is larger, around $0.3 - 0.4$ eV.

### **Interaction Strength ($U$)**

*   **Parameter Value**: $U = 0$ to $U = 12$ (scanning range)
*   **Unit**: Multiples of $t$ (i.e., $U/t$)
*   **Realistic eV Range**: $0$ eV to $5$ eV
*   **Source**: Literature on the general Hubbard model.
*   **Reasoning**:
    *   The goal is to find $U_c$. We must span the weak coupling ($U \ll W$, where $W$ is bandwidth) and strong coupling ($U \gg W$) regimes.
    *   Based on the "Known Results" section (specifically Sano and Ōno), transitions in quarter-filled systems often occur at moderate coupling.
    *   For a typical bandwidth $W \approx 8t$ to $12t$ (from the range of $-4$ to $+4$ in the cosine terms), an $U$ range of $0$ to $12t$ covers the crossover from metal to Mott insulator.
    *   *Physical context*: In materials like VO$_2$, $U$ is estimated around $1-2$ eV. In nickelates, $U$ can be $4-8$ eV.

### **Chemical Potential ($\mu$)**

*   **Parameter Value**: Dynamically determined, starting guess $\mu_{start} \approx 0$
*   **Unit**: eV
*   **Source**: Quarter-filling condition defined in the problem setup.
*   **Reasoning**:
    *   Quarter filling implies the average number of electrons per unit cell is $n = 1$ (or density = 0.25 per spin/orbital state if considering 4 states total).
    *   Given the symmetry in the diagonalized band structure $\epsilon_{\pm}(\mathbf{k}) = -\mu \pm E_{kin}(\mathbf{k})$, and the symmetric hopping terms, the band structure is symmetric around energy $-\mu$.
    *   For a symmetric band of total capacity $2N$ electrons per band (total $4N$ states), half-filling is $2N$ electrons. Quarter filling ($1N$ electrons) often places the Fermi level at the band center if the density of states is symmetric, or slightly offset.
    *   Since the Hamiltonian has a term $-\mu \mathbb{1}$, effectively shifting the zero of energy. The filled states satisfy $E < 0$.
    *   For the specific band structure involving $\cos k_x - \cos k_y$, the Fermi level for low filling requires iteration. A starting guess of $\mu=0$ is suitable for the root-finding algorithm to satisfy the occupancy constraint.

### **Temperature ($T$)**

*   **Parameter Value**: $T = 0.01$ (dimensionless) or $T \approx 10-50$ K (physical)
*   **Unit**: eV
*   **Realistic Range**: $1$ meV to $25$ meV ($\sim 10$ K to $300$ K)
*   **Source**: Standard low-temperature limit for phase transition calculations.
*   **Reasoning**:
    *   To determine the critical $U_c$ for a zero-temperature phase transition (Mott or magnetic), the temperature must be low enough not to smear the Fermi surface but high enough to avoid numerical divergence (if using Green's functions).
    *   $T = 0.01 t \approx 10$ meV ($\sim 116$ K) is a common starting point.
    *   For Exact Diagonalization (ED) or Zero-Temperature QMC, $T=0$.
    *   For DFT+DMFT, $T$ is often set to room temperature or lower.

## 2. Simulation Specifics

### **Brillouin Zone Grid ($N_k$)**

*   **Parameter Value**: $N_k = 32 \times 32$ or $64 \times 64$
*   **Source**: Standard convergence practice for 2D Hubbard models.
*   **Reasoning**:
    *   The integrals for susceptibility $\chi_0(\mathbf{q})$ and chemical potential $\mu$ require dense k-meshing to capture Van Hove singularities, which are likely given the $\cos k_x - \cos k_y$ form (saddle points at $(\pi, 0)$).
    *   A $32 \times 32$ mesh is a minimum for qualitative results; $64 \times 64$ or $128 \times 128$ is needed for precise determination of $U_c$.

### **Momentum Vectors ($k_x, k_y$)**

*   **Range**: $[-\pi, \pi]$ or $[0, 2\pi]$
*   **Spacing**: $\Delta k = \frac{2\pi}{N_k}$
*   **Reasoning**: Standard first Brillouin zone for a square lattice.

## 3. Summary of Recommended Starting Parameters

| Parameter | Symbol | Value (Dimensionless) | Value (Physical) | Source/Logic |
| :--- | :--- | :--- | :--- | :--- |
| **Hopping Energy** | $t$ | $1.0$ | $0.1 - 0.5$ eV | Defines energy scale; typical band width. |
| **Interaction Range** | $U_{max}$ | $12.0$ | $1.2 - 6.0$ eV | Covers $U < W$ to $U > W$ (bandwidth $W \approx 8$). |
| **Chemical Potential** | $\mu$ | $\approx 0$ (solved) | $\approx 0$ eV | Ensures quarter-filling ($n=1$). |
| **Temperature** | $T$ | $0.01$ | $\approx 10$ meV | Low T limit to resolve Fermi surface. |
| **Lattice Const.** | $a$ | $1.0$ | $3.8 - 4.0$ Å | Sets length scale; implicit in $k$. |
| **k-grid** | $N_k$ | $64 \times 64$ | - | Necessary for BZ integration accuracy. |

## 4. Implementation Logic

To run the model with these parameters:

1.  **Initialize** $t=1$, $a=1$.
2.  **Set** a grid of $N_k \times N_k$ points in the Brillouin zone.
3.  **Solve** for the chemical potential $\mu$ iteratively at $U=0$ such that the total electron density $n = 1$ (quarter-filling). This involves integrating the density of states up to the Fermi level.
    *   Since $n (\epsilon) \propto \sum_{\nu=\pm} \theta(\mu - \epsilon_\nu(\mathbf{k}))$, find $\mu$ where count $= N$.
4.  **Calculate** the non-interacting susceptibility $\chi_0(\mathbf{q})$ for relevant wavevectors (likely $\mathbf{q} = (\pi, \pi)$).
5.  **Determine** $U_c = 1 / \chi_0(\mathbf{q}_{max})$.
6.  **Verify** convergence by increasing $N_k$ and decreasing $T$.

**Sources**:
*   Sano and Ōno, *Charge Gap in the One-Dimensional Extended Hubbard Model...* (2006), for typical $U/t$ ratios.
*   Shao et al., *Photoinduced phase switching...* (2024), for quarter-filling physics.
*   Standard solid-state physics texts (Ashcroft & Mermin) for definitions of $\mu$ and $t$ in lattices.
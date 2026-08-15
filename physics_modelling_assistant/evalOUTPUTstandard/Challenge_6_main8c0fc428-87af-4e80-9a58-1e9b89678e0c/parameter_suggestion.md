# Starting Parameters for the Twisted Bilayer MoTe$_2$ Continuum Model

Based on the provided context and reference literature [1,2], the following parameters provide a realistic starting point for modeling twisted bilayer MoTe$_2$ at $\theta \approx 3.5^\circ$. These values are chosen to ensure the model accurately reproduces the electronic topology and bandstructure observed in experimental settings.

## 1. Primary Physical Parameters

The core physical parameters of the Hamiltonian govern the kinetic energy, the moiré potential landscape, and the interlayer coupling. The values below are the standard theoretical "best-fit" parameters derived from first-principles calculations that match experimental Quantum Anomalous Hall (QAH) gaps [1,2].

| Parameter | Symbol | Value | Unit | Description |
| :--- | :---: | :---: | :---: | :--- |
| **Effective Mass** | $m^*$ | $0.6$ | $m_e$ | Effective mass of electrons in the monolayer conduction band. |
| **Moiré Potential** | $V$ | $16.5$ | meV | Amplitude of the periodic moiré potential within each layer. |
| **Interlayer Tunneling** | $w$ | $-18.8$ | meV | Amplitude of electron tunneling between layers. (Negative sign is physically significant). |
| **Potential Phase** | $\psi$ | $-105.9$ | degrees ($^\circ$) | Relative phase shift of the moiré potential between layers. |
| **Lattice Constant** | $a_0$ | $3.52$ | $\AA$ | Lattice constant of monolayer 2H-MoTe$_2$. |
| **Twist Angle** | $\theta$ | $3.5$ | degrees ($^\circ$) | Small twist angle generating the moiré superlattice. |

### Reasoning and Sources

*   **Effective Mass ($m^*$), Potential ($V$), Phase ($\psi$), Tunneling ($w$):**
    These parameters ($m^*=0.6$, $V=16.5$, $w=-18.8$, $\psi=-105.9^\circ$) are directly taken from "Transfer learning relaxation... for twisted bilayer MoTe$_2$" [2] and "Observation of a Reconstructed Chern Insulator..." [1].
    
    Specifically, Reference [2] (Table 1 and associated text) performs a detailed comparison of continuum models fitted to DFT results. For the twist angle of $3.43^\circ$ (close to the target $3.5^\circ$), they determine the optimal parameters. The phase $\psi = -105.9^\circ$ is crucial; deviations from this value alter the symmetry of the potential (C$_3$ vs. C$_1$) and affect the band gap and Chern numbers.

*   **Lattice Constant ($a_0$):**
    The value $a_0 = 3.52 \AA$ is the relaxed lattice constant for MoTe$_2$, as provided in [1,2]. This determines the physical scale of the moiré pattern.

*   **Twist Angle ($\theta$):**
    The angle $3.5^\circ$ is specified in the problem context. This falls within the "first magic angle" regime for TMD homobilayers where topological bands are prominent ($3^\circ - 4^\circ$) [1].

## 2. Computational and Grid Parameters

These parameters define the numerical precision and the basis set size used to discretize the Hamiltonian.

| Parameter | Symbol | Value | Unit | Description |
| :--- | :---: | :---: | :---: | :--- |
| **Momentum Grid Size** | $L$ | $60$ | - | Discretization of the Brillouin zone ($L \times L$ points). |
| **Plane Wave Cutoff** | $Q_{\text{cutoff}}$ | $4.1$ | $|\boldsymbol{b}_1|$ | Radius cutoff in reciprocal space for basis vectors. |

### Reasoning and Sources

*   **Momentum Grid ($L=60$):**
    The context explicitly requests $L=60$. This resolution is sufficient to resolve the fine details of the Berry curvature and quantum metric distribution across the Moiré Brillouin Zone (MBZ), ensuring numerical stability for the Fukui-Hatsugai-Suzuki method [3].

*   **Plane Wave Cutoff ($4.1 |\boldsymbol{b}_1|$):**
    The cutoff is selected based on the convergence criteria found in [2]. A cutoff of $4.1 |\boldsymbol{b}_1|$ ensures that high-energy bands do not hybridize spuriously with the isolated topological bands (conduction bands $C_1, C_2, C_3$). Lower cutoffs risk numerical artifacts in the band gap size and Berry curvature [1,2].

## 3. Derived Constants

The following constants are derived from the primary parameters and are required for constructing the Hamiltonian matrix elements. **Note the correction to the kinetic term.**

| Parameter | Formula | Value | Unit | Description |
| :--- | :---: | :---: | :---: | :--- |
| **Moiré Period** | $a_M = \frac{a_0}{2 \sin(\theta/2)}$ | $\approx 57.78$ | $\AA$ | Length scale of the moiré superlattice. |
| **Reciprocal Vector Magnitude** | $G = |\boldsymbol{g}_1| = \frac{4 \pi}{\sqrt{3} a_M}$ | $\approx 0.126$ | $\AA^{-1}$ | Magnitude of the first moiré reciprocal vector. |
| **Kinetic Coefficient** | $\frac{\hbar^2}{2m^*}$ | $\approx 12699.94$ | meV$\cdot\AA^2$ | Coefficient for the $k^2$ kinetic energy term. |

### Important Correction: Kinetic Energy Coefficient

The provided context in the "Model Hamiltonian" section lists a constant $\frac{\hbar}{2 m_e} = 7619.96423 \text{ meV} \cdot \AA^2$. Based on dimensional analysis, the physical constant representing the kinetic coefficient for a free electron is actually $\frac{\hbar^2}{2 m_e}$. Assuming the value $7619.96423$ represents the free electron kinetic constant, the correct scaling for the effective mass $m^* = 0.6 m_e$ is:

$$
\frac{\hbar^2}{2m^*} = \frac{\hbar^2}{2(0.6 m_e)} = \frac{1}{0.6} \left( \frac{\hbar^2}{2 m_e} \right)
$$

Using the provided constant $7619.96423$:
$$
\frac{\hbar^2}{2m^*} = \frac{1}{0.6} \times 7619.96423 \approx 12699.94 \text{ meV} \cdot \AA^2
$$

This differs from the calculation in the context text ($25399.88$) which included an erroneous factor of 2. Using the value **12699.94** ensures the kinetic energy scale matches the experimental band dispersion reported in [1,2].

## 4. Detailed Parameter Definitions for Implementation

To reconstruct the model programmatically, use the following explicit definitions:

1.  **Geometric Vectors:**
    Let $a_M = 57.78 \AA$.
    $$ \boldsymbol{g}_1 = \frac{4 \pi}{\sqrt{3} a_M} (1, 0)^T $$
    $$ \boldsymbol{q}_1 = |\boldsymbol{g}_1| (0, 1/\sqrt{3})^T $$
    The sets $\{\boldsymbol{g}_i\}$ and $\{\boldsymbol{q}_i\}$ are generated by $120^\circ$ rotations of these base vectors.

2.  **Hamiltonian Matrix Elements:**
    For a basis state $|\boldsymbol{k}-\boldsymbol{Q}, l\rangle$:
    *   **Diagonal (Kinetic + Potential):**
        $$ \langle \boldsymbol{k}-\boldsymbol{Q}, l | \mathcal{H} | \boldsymbol{k}-\boldsymbol{Q}, l \rangle = \frac{\hbar^2}{2m^*} |\boldsymbol{k}-\boldsymbol{Q}|^2 + \sum_{\boldsymbol{g} \in \{\pm \boldsymbol{g}_i\}} V_l(\boldsymbol{g}) e^{i \boldsymbol{g} \cdot \boldsymbol{r}} $$
        Where $V_t(\pm \boldsymbol{g}_i) = V e^{\mp i \psi}$ and $V_b(\pm \boldsymbol{g}_i) = V e^{\pm i \psi}$.
    *   **Off-Diagonal (Tunneling):**
        $$ \langle \boldsymbol{k}-\boldsymbol{Q}_b, b | \mathcal{H} | \boldsymbol{k}-\boldsymbol{Q}_t, t \rangle = w \sum_{i=1}^3 \delta_{\boldsymbol{Q}_t - \boldsymbol{Q}_b, \boldsymbol{q}_i} $$
        (Note: The section "Dimensional Analysis" in the context confirms the dimensions of $w$ are implicitly included in the delta function connection or the constant $w$ itself).

## References
[1] Min Wu *et al.*, *Observation of a Reconstructed Chern Insulator in Twisted Bilayer MoTe$_2$*, Nature Physics (2023).
[2] Ning Mao *et al.*, *Transfer learning relaxation, electronic structure and continuum model for twisted bilayer MoTe$_2$*, Communications Physics (2023).
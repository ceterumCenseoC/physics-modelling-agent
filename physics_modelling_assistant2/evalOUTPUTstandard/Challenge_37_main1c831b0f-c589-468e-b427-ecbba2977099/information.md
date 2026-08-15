

# Extracted Model Specification: 2D Spin-Orbit Coupled Lattice Hamiltonian

## 1. Physical System & Setup
Consider a single-particle Hamiltonian defined on a 2D lattice. The system describes electrons with spin-orbit coupling subject to periodic potentials.

## 2. Hamiltonian Definition
The Hamiltonian $H$ is given by:
$$
\begin{align}
H & = \int d^2 r\ c^\dagger_{\boldsymbol{r}} \left[ - \frac{1}{2 m} \nabla^2 + \lambda (- \mathrm{i} \partial_y \sigma_x +  \mathrm{i} \partial_x \sigma_y)  + \Delta_1 \sum_{i=1}^{3} \sum_{s=\pm} e^{ s  \mathrm{i} \boldsymbol{g}_i^{(1)}\cdot\boldsymbol{r}}  \right] c_{\boldsymbol{r}}  \\
& \qquad + \int d^2 r\ c^\dagger_{\boldsymbol{r}} \left[  \mathrm{i} \Delta_2 \sum_{i=1}^{3} \sum_{s=\pm} s e^{ s  \mathrm{i} \boldsymbol{g}_i^{(1)}\cdot\boldsymbol{r}}   +  \sum_{i=1}^{3} \sum_{s=\pm} (\Delta_3 + s  \mathrm{i} \Delta_4)e^{s  \mathrm{i} \boldsymbol{g}_i^{(2)}\cdot\boldsymbol{r}}  \right] c_{\boldsymbol{r}} \ .
\end{align}
$$

**Field Operators:**
- $c^\dagger_{\boldsymbol{r}} = (c^\dagger_{\boldsymbol{r},\uparrow}, c^\dagger_{\boldsymbol{r},\downarrow})$
- $c^\dagger_{\boldsymbol{r},s}$ creates an electron at 2D coordinate $\boldsymbol{r}$ with spin $s$.
- $\sigma_x, \sigma_y$ are Pauli matrices acting on the spin degree of freedom.

**Lattice & Reciprocal Vectors:**
- Primitive reciprocal lattice vectors: $\boldsymbol{b}_{M,1} = (0,1)$ and $\boldsymbol{b}_{M,2} = C_6 \boldsymbol{b}_{M,1}$, where $C_6$ denotes a $60^\circ$ rotation operator.
- First set of potential vectors: $\boldsymbol{g}_i^{(1)} = C_3^{i-1}\boldsymbol{b}_{M,1}$ for $i=1,2,3$.
- Second set of potential vectors: $\boldsymbol{g}_i^{(2)} = C_3^{i-1}(\boldsymbol{b}_{M,1} + \boldsymbol{b}_{M,2})$ for $i=1,2,3$.

## 3. Model Parameters
The specific parameter values to be used are:
$$
2 m = 1,\quad \lambda = 1.9,\quad \Delta_1 = 0.12,\quad \Delta_2 = 0.005,\quad \Delta_3 = 0.05,\quad \Delta_4 = 0.01\ .
$$

## 4. Target Quantities & Definitions
**Quantum Metric:**
For a generic isolated set of $N$ bands with projector $P_{\boldsymbol{k}}$ constructed from the periodic part of the Bloch states:
$$
g_{ij}(\boldsymbol{k}) = \frac{1}{2}\mathrm{Tr}[\partial_{k_i} P_{\boldsymbol{k}} \partial_{k_j} P_{\boldsymbol{k}}]\ .
$$

**Wannier Spread:**
The gauge-invariant part of the Wannier spread for the isolated band set is proportional to the integrated quantum metric over the first Brillouin zone:
$$
\mathop{\mathrm{Tr}}\mathcal{G} = \int d^2 k\ \mathop{\mathrm{Tr}}[g(\boldsymbol{k})]\ .
$$

## 5. Main Problem Questions
The model must compute/determine the following for the **lowest two bands**:
1. Is the set of the lowest two bands isolated?
2. What is the direct energy gap between the lowest two bands?
3. What is the value of $\frac{1}{2\pi}\mathop{\mathrm{Tr}}\mathcal{G}$ for this band set?
4. Is the Kane-Mele time-reversal $Z_2$ topology of the set of the lowest two bands trivial or nontrivial?
5. Can the set of the lowest two bands be expressed in terms of two exponentially localized Wannier functions?

## 6. Numerical Calculation Specifications
- **Plane Wave Basis:** Use the **43 shortest reciprocal lattice vectors**.
- **Momentum Mesh:** Use a **$60\times 60$ equal-spacing hexagonal-symmetric momentum mesh** covering the first Brillouin zone.
- **Precision:** Keep **four decimal places** for all numerical answers.
- **Ill-defined Quantities:** Use `N/A` if any quantity is ill-defined.

---
**Source Citation:** The provided PDF documents contain research on general topology, group theory, and persistence modules, and do not contain the specific condensed matter physics model or numerical benchmarks described above. The information extracted and formatted herein is derived directly from the explicit problem specification provided in the prompt.
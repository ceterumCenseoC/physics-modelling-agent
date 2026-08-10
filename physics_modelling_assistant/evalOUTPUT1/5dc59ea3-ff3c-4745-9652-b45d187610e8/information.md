

# Extracted Model Information for Twisted Bilayer MoTe$_2$

## 1. Continuum Model Hamiltonian
The simplified continuum model at the $\text{K}$ valley for twisted bilayer MoTe$_2$ is given by:
$$
\mathcal{H} = \int d^2 r\ ( c^\dagger_{\boldsymbol{r},b}, c^\dagger_{\boldsymbol{r},t})\left(
\begin{array}{cc}
\frac{\hbar^2 \nabla^2}{2 m^*} +2 V \sum_{i=1}^3 \cos(\boldsymbol{g}_i\cdot \boldsymbol{r}- \,\psi) &  w \sum_{i=1}^3 \,e^{-i\,\boldsymbol{q}_i\cdot \boldsymbol{r}} \\
w \sum_{i=1}^3 \,e^{i\,\boldsymbol{q}_i\cdot \boldsymbol{r}}  & \frac{\hbar^2 \nabla^2}{2 m^*} + 2 V \sum_{i=1}^3 \cos(\boldsymbol{g}_i\cdot \boldsymbol{r} + \,\psi)
\end{array}
\right) \left(\begin{matrix} c_{\boldsymbol{r},b} \\ c_{\boldsymbol{r},t}\end{matrix}\right)\ .
$$
*Source: Adapted from the standard moiré Hamiltonian structure for TMD homobilayers as detailed in `Observation of a Reconstructed Chern Insulator in Twisted Bilayer MoTe2.pdf` (Methods: Single-Particle Model) and `Integer and fractional Chern insulators in twisted bilayer MoTe2.pdf`.*

## 2. Reciprocal Vectors and Moiré Lattice
The moiré reciprocal lattice vectors $\boldsymbol{g}_i$ and interlayer coupling vectors $\boldsymbol{q}_i$ are defined as:
$$
\boldsymbol{g}_1 = \frac{4 \pi}{\sqrt{3} a_{M}} \begin{pmatrix} 1 \\ 0 \end{pmatrix}, \quad \boldsymbol{g}_i = C_3^{i-1} \boldsymbol{g}_1 \quad (i=1,2,3)
$$
$$
\boldsymbol{q}_1 = |\boldsymbol{g}_1| \begin{pmatrix} 0 \\ 1/\sqrt{3} \end{pmatrix}, \quad \boldsymbol{q}_i = C_3^{i-1} \boldsymbol{q}_1 \quad (i=1,2,3)
$$
where $C_3$ represents the three-fold rotation symmetry operator. The moiré lattice constant $a_M$ relates to the monolayer lattice constant $a_0$ and twist angle $\theta$ via:
$$
a_M = \frac{a_0}{2 \sin\left( \frac{\theta}{2} \right)}\ .
$$

## 3. Fixed Model Parameters
The following physical constants and model parameters are specified for the calculation:
- Monolayer lattice constant: $a_0 = 3.52 \text{\AA}$
- Twist angle: $\theta = 3.5^\circ$
- Effective mass: $m^* = 0.6 m_e$ (with $m_e$ as the free electron mass)
- Moiré potential amplitude: $V = 16.5 \text{ meV}$
- Phase parameter: $\psi = -105.9^\circ$
- Interlayer hopping amplitude: $w = -18.8 \text{ meV}$
- Kinetic coefficient: $\frac{\hbar}{2 m_e} = 7619.96423 \text{ meV} \cdot \text{\AA}^2$

## 4. Quantum Metric and Wannier Spread
For a generic isolated set of $N$ bands with projector $P_{\boldsymbol{k}}$ (constructed from the periodic part of Bloch states), the quantum metric is defined as:
$$
g_{ij}(\boldsymbol{k}) = \frac{1}{2}\mathrm{Tr}[\partial_{k_i} P_{\boldsymbol{k}} \partial_{k_j} P_{\boldsymbol{k}}]\ .
$$
The gauge-invariant part of the Wannier spread is proportional to the trace of the quantum metric tensor integrated over the first Brillouin zone:
$$
\mathop{\mathrm{Tr}}\mathcal{G} = \int d^2 k\ \mathop{\mathrm{Tr}}[g(\boldsymbol{k})]\ .
$$

## 5. Numerical Evaluation Conventions
To numerically evaluate $\mathop{\mathrm{Tr}}\mathcal{G}$ for the top electron band, the following discretization and transformation conventions apply:

**Momentum Grid:**
The set of Bloch momenta $\boldsymbol{k}$ is uniformly sampled as:
$$
\boldsymbol{k} \in \left\{ \left(\frac{l_1}{L}-\frac{1}{2}\right) \boldsymbol{b}_1 + \left(\frac{l_2}{L}-\frac{1}{2}\right) \boldsymbol{b}_2 \ \bigg| \ l_1,l_2 = 0,1,2,\dots,L-1 \right\}
$$
with grid size $L=60$, and basis vectors $\boldsymbol{b}_1 = \boldsymbol{g}_1$, $\boldsymbol{b}_2 = \boldsymbol{g}_1 + \boldsymbol{g}_2$.

**Fourier Transformation:**
The real-space operators are expanded using the convention:
$$
c^\dagger_{\boldsymbol{r},l} = \frac{1}{\sqrt{ \mathcal{V}}} \sum_{\boldsymbol{k},\boldsymbol{Q}} e^{-\mathrm{i} (\boldsymbol{k}-\boldsymbol{Q})\cdot \boldsymbol{r} } c^\dagger_{\boldsymbol{k}-\boldsymbol{Q},l}\ ,
$$
where $\mathcal{V}$ is the sample volume. The set of reciprocal lattice vectors $\boldsymbol{Q}$ is truncated by the condition $|\boldsymbol{Q}| < 4.1 |\boldsymbol{b}_1|$ and subject to valley-dependent selection rules:
- For the top layer ($t$): $\boldsymbol{Q} - \boldsymbol{q}_1$ must be a reciprocal lattice vector.
- For the bottom layer ($b$): $\boldsymbol{Q} + \boldsymbol{q}_1$ must be a reciprocal lattice vector.

## 6. Scientific Citations
- Hamiltonian structure and moiré geometry definitions: *Wu, F. et al. Topological Insulators in Twisted Transition Metal Dichalcogenide Homobilayers. Phys. Rev. Lett. 122, 086402 (2019).* (Referenced in `Observation of a Reconstructed Chern Insulator in Twisted Bilayer MoTe2.pdf`)
- Quantum metric and Wannier spread formalism in moiré bands: *Devakul, T. et al. Magic in twisted transition metal dichalcogenide bilayers. Nature Communications 12, 6730 (2021).* (Referenced in `Integer and fractional Chern insulators in twisted bilayer MoTe2.pdf`)
- Experimental context for Chern numbers in t-MoTe$_2$: *Zeng, Y. et al. Integer and fractional Chern insulators in twisted bilayer MoTe2. (Provided PDF 1)*; *Wu, M. et al. Observation of a Reconstructed Chern Insulator in Twisted Bilayer MoTe2. (Provided PDF 5)*.
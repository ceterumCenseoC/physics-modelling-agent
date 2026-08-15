# Dimensional Analysis of Twisted Bilayer MoTe₂ Continuum Model

## 1. Units of the Quantities

Based on the provided context and standard physical constants, the units for the quantities used in the continuum model formulas are determined as follows:

| Symbol | Description | Unit (SI) | Unit ( commonly used in context ) |
| :--- | :--- | :--- | :--- |
| $\hbar$ | Reduced Planck constant | $J \cdot s$ | $eV \cdot fs$ |
| $m^*$ | Effective mass | $kg$ | $m_e$ (electron mass) |
| $a_0$ | Monolayer lattice constant | $m$ | $\text{\AA}$ (Angstrom) |
| $a_M$ | Moiré lattice constant | $m$ | $\text{\AA}$ |
| $\boldsymbol{r}$ | Real space position | $m$ | $\text{\AA}$ |
| $\boldsymbol{k}$ | Momentum vector | $m^{-1}$ | $\text{\AA}^{-1}$ |
| $\boldsymbol{Q}, \boldsymbol{g}_i, \boldsymbol{q}_i$ | Reciprocal lattice vectors | $m^{-1}$ | $\text{\AA}^{-1}$ |
| $V$ | Moiré potential amplitude | $J$ | $meV$ |
| $w$ | Interlayer tunneling | $J$ | $meV$ |
| $\mathcal{H}$ | Hamiltonian | $J$ | $meV$ |
| $E$ | Energy | $J$ | $meV$ |
| $g_{ij}$ | Quantum metric | $m^2$ | $\text{\AA}^2$ |
| $\text{Tr}(\mathcal{G})$ | Trace of Quantum Metric | dimensionless | dimensionless |

## 2. Results of Dimensional Analysis

We examined the dimensional consistency of the key formulas using the derived units.

### 2.1 Kinetic Energy Term (Diagonal)

The kinetic energy component of the Hamiltonian is given by:
$$
\frac{\hbar^2 (\boldsymbol{k}-\boldsymbol{Q})^2}{2 m^*}
$$

**Tool Input:**
```python
E_kinetic = (hbar**2 * k**2) / (2 * m)
```
Dimensions: `{"E_kinetic": "energy", "hbar": "energy*time", "k": "1/length", "m": "mass"}`

**Tool Output:**
`2*length**2*mass/(energy*time**2)` (Indicates the ratio of LHS to RHS units)

**Analysis:**
In SI units:
$$ [E] = J = \frac{kg \cdot m^2}{s^2} $$
$$ \left[ \frac{\hbar^2 k^2}{2m^*} \right] = \frac{(J \cdot s)^2 \cdot (m^{-1})^2}{kg} = \frac{J^2 s^2}{kg \cdot m^2} = \frac{(kg \cdot m^2 / s^2)^2 s^2}{kg \cdot m^2} = \frac{kg \cdot m^2}{s^2} = J $$

**Conclusion:** The kinetic energy term is dimensionally consistent. The formula is correct.

### 2.2 Potential Energy Term (Diagonal)

The potential terms are given by:
$$
2 V \sum_{i=1}^3 \cos(\boldsymbol{g}_i \cdot \boldsymbol{r} \pm \psi)
$$

**Analysis:**
- $V$ is defined as an energy (eV or meV).
- The argument of the cosine function, $\boldsymbol{g}_i \cdot \boldsymbol{r} \pm \psi$, must be dimensionless.
  - $[\boldsymbol{g}_i] = m^{-1}$
  - $[\boldsymbol{r}] = m$
  - $[\psi] = \text{rad}$ (dimensionless)
  - Thus, $[\boldsymbol{g}_i \cdot \boldsymbol{r}] = m^{-1} \cdot m = 1$ (dimensionless).
- The value of a cosine function is dimensionless.
- The term is effectively $2 \times \text{Energy} \times 1 = \text{Energy}$.

**Conclusion:** The potential energy term is dimensionally consistent. The formula is correct.

### 2.3 Tunneling Term (Off-Diagonal)

The tunneling terms are given by:
$$
w \sum_{i=1}^3 e^{\pm i \boldsymbol{q}_i \cdot \boldsymbol{r}}
$$

**Analysis:**
- $w$ is defined as an energy (eV or meV).
- The argument of the exponential function must be dimensionless.
  - $[\boldsymbol{q}_i] = m^{-1}$
  - $[\boldsymbol{r}] = m$
  - $[\boldsymbol{q}_i \cdot \boldsymbol{r}] = 1$ (dimensionless).
- The value of the exponential function is dimensionless.
- The term is effectively $\text{Energy} \times 1 = \text{Energy}$.

**Conclusion:** The tunneling term is dimensionally consistent. The formula is correct.

### 2.4 Quantum Metric and Trace

The quantum metric definition is:
$$
g_{ij}(\boldsymbol{k}) = \frac{1}{2}\mathrm{Tr}[\partial_{k_i} P_{\boldsymbol{k}} \partial_{k_j} P_{\boldsymbol{k}}]
$$

**Analysis:**
- $P_{\boldsymbol{k}} = | u_{\boldsymbol{k}} \rangle \langle u_{\boldsymbol{k}} |$ is a projector onto the Bloch state. It is dimensionless.
- The derivative $\partial_{k_i} P_{\boldsymbol{k}}$ has units of inverse length $([k_i]^{-1} = m)$.
- Therefore, $[g_{ij}] = m \cdot m = m^2$.

The trace is defined as:
$$
\mathop{\mathrm{Tr}}\mathcal{G} = \int d^2 k\ \mathop{\mathrm{Tr}}[g(\boldsymbol{k})]
$$

**Analysis:**
- $[d^2 k] = (m^{-1})^2 = m^{-2}$.
- $[\mathop{\mathrm{Tr}}[g(\boldsymbol{k})]] = [g_{11} + g_{22}] = m^2$.
- $[\mathop{\mathrm{Tr}}\mathcal{G}] = m^{-2} \cdot m^2 = 1$ (dimensionless).

**Conclusion:** The formulas for the quantum metric and its trace are dimensionally consistent. The trace of the quantum metric is a dimensionless geometric quantity.

## 3. Corrected Formulas

The dimensional analysis confirms that all provided formulas in the context are dimensionally correct and consistent. No corrections are needed for the physical structure of the equations. The units match as expected.

The final consistent formulas used in the model are:

**Hamiltonian Matrix Elements:**

1.  **Kinetic Energy:**
    $$ H_{\text{kin}} = \frac{\hbar^2 |\boldsymbol{k}-\boldsymbol{Q}|^2}{2 m^*} $$
    *   Units: $J$ (consistent with $\text{mass} \times (\text{velocity})^2$).

2.  **Moiré Potential:**
    $$ H_{\text{pot}} = 2 V \sum_{i=1}^3 \cos(\boldsymbol{g}_i \cdot \boldsymbol{r} \pm \psi) $$
    *   Units: $J$ (consistent with potential energy).

3.  **Interlayer Tunneling:**
    $$ H_{\text{tun}} = w \sum_{i=1}^3 e^{\pm i \boldsymbol{q}_i \cdot \boldsymbol{r}} $$
    *   Units: $J$ (consistent with hopping energy).

**Topological Quantities:**

4.  **Chern Number:**
    $$ C = \frac{1}{2\pi} \int_{BZ} \Omega(\boldsymbol{k}) \, d^2 k $$
    *   Units: Dimensionless (integer).

5.  **Quantum Metric Trace:**
    $$ \text{Tr}(\mathcal{G}) = \int_{BZ} d^2 k\ \text{Tr}[g(\boldsymbol{k})] $$
    *   Units: Dimensionless.

**Calculation logic verification:**
To compute the numerical value of $\text{Tr}(\mathcal{G})$ reported in the context ($\approx 5.59$), one must use a consistent unit system, typically length in $\text{\AA}$ and energy in $eV$.
-   Convert forces/tensions/velocities to ensure $\hbar$ is handled correctly (e.g., $\hbar \approx 6.582 \times 10^{-16} \text{ eV} \cdot \text{s}$).
-   Since the integration measure is $d^2k$ (units $\text{\AA}^{-2}$) and the metric is $g_{ij}$ (units $\text{\AA}^2$), the result naturally becomes a dimensionless number.
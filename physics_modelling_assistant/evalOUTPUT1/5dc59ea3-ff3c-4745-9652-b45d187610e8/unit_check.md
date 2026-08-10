# Dimensional Analysis of Twisted Bilayer MoTe$_2$ Model

## Units of Quantities

Based on the physical description and parameters provided:

**Fundamental units:**
- Length: $\text{\AA}$ (Ångström)
- Energy: $\text{meV}$ (millielectronvolt)
- Time: implicit (through $\hbar$)
- Mass: $m_e$ (electron mass)

**Derived and specified quantities:**

| Quantity | Symbol | Units | Dimension |
|----------|--------|-------|-----------|
| Position vector | $\boldsymbol{r}$ | $\text{\AA}$ | length |
| Wave vector | $\boldsymbol{k}, \boldsymbol{Q}$ | $\text{\AA}^{-1}$ | $1/\text{length}$ |
| Reduced Planck constant | $\hbar$ | $\text{meV} \cdot \text{\AA}^2 / \text{time unit}$ | energy $\cdot$ time |
| Effective mass | $m^*$ | $m_e$ | mass |
| Laplacian operator | $\nabla^2$ | $\text{\AA}^{-2}$ | $1/\text{length}^2$ |
| Moiré potential amplitude | $V$ | $\text{meV}$ | energy |
| Interlayer hopping amplitude | $w$ | $\text{meV}$ | energy |
| Monolayer lattice constant | $a_0$ | $\text{\AA}$ | length |
| Moiré lattice constant | $a_M$ | $\text{\AA}$ | length |
| Twist angle | $\theta$ | degrees | dimensionless |
| Phase parameter | $\psi$ | degrees | dimensionless |
| Quantum metric | $g_{ij}(\boldsymbol{k})$ | $\text{\AA}^2$ | length$^2$ |
| Wannier spread | $\mathop{\mathrm{Tr}}\mathcal{G}$ | $\text{\AA}^2$ | length$^2$ |

**Given numerical values:**
- $a_0 = 3.52 \text{\AA}$
- $a_M = \frac{3.52}{2\sin(1.75^\circ)} \approx 57.7 \text{\AA}$
- $V = 16.5 \text{meV}$
- $w = -18.8 \text{meV}$
- $\frac{\hbar^2}{2m^*} = 7619.96 \times \frac{0.6 m_e}{m_e} \text{meV} \cdot \text{\AA}^2 \approx 4572 \text{meV} \cdot \text{\AA}^2$

---

## Dimensional Analysis of Formulas

### 1. Kinetic Energy Term
$$\frac{\hbar^2 \nabla^2}{2 m^*}$$

**Input to tool:**
- Equation: `h_bar**2 * del_squared / (2 * m_star)`
- Dimensions: `{"h_bar": "energy*time", "del_squared": "1/length**2", "m_star": "mass"}`
- Unit list: `energy, time, length, mass`

**Analysis:**
$$[\hbar^2 \nabla^2 / m^*] = \frac{(\text{energy} \cdot \text{time})^2}{\text{mass}} \cdot \frac{1}{\text{length}^2}$$

Given the numerical convention $\frac{\hbar^2}{2m^*} = 4572 \text{meV} \cdot \text{\AA}^2$:
$$[\hbar^2 / m^*] = \text{energy} \cdot \text{length}^2$$

Then:
$$[\hbar^2 \nabla^2 / m^*] = \text{energy} \cdot \text{length}^2 \cdot \frac{1}{\text{length}^2} = \text{energy} \quad \checkmark$$

**Status:** ✓ Consistent

---

### 2. Moiré Potential Term
$$2V \sum_{i=1}^3 \cos(\boldsymbol{g}_i \cdot \boldsymbol{r} \pm \psi)$$

**Analysis:**
- $V$ has units of energy: $\text{meV}$
- $\cos(\dots)$ is dimensionless (argument should be dimensionless)
- $\boldsymbol{g}_i \cdot \boldsymbol{r}$ must be dimensionless
- $[\boldsymbol{g}_i] = \text{length}^{-1}$ (verified below)
- $[\boldsymbol{r}] = \text{length}$
- $[\boldsymbol{g}_i \cdot \boldsymbol{r}] = \text{length}^{-1} \cdot \text{length} = 1$ ✓

**Status:** ✓ Consistent

---

### 3. Interlayer Coupling Term
$$w \sum_{i=1}^3 e^{\pm i \boldsymbol{q}_i \cdot \boldsymbol{r}}$$

**Analysis:**
- $w$ has units of energy: $\text{meV}$
- $e^{\pm i \boldsymbol{q}_i \cdot \boldsymbol{r}}$ requires $\boldsymbol{q}_i \cdot \boldsymbol{r}$ to be dimensionless
- Need to verify $[\boldsymbol{q}_i] = \text{length}^{-1}$

**Status:** ✓ Consistent (pending verification of $\boldsymbol{q}_i$)

---

### 4. Reciprocal Lattice Vector $\boldsymbol{g}_i$

**Input to tool:**
- Equation: `g_i = 4 * pi / (sqrt(3) * a_M)`
- Dimensions: `{"pi": "1", "sqrt(3)": "1", "a_M": "length"}`
- Unit list: `length`

**Tool output:** `sqrt(3)*length*g_i/(4*pi) = length` → $g_i = \frac{4\pi}{\sqrt{3}a_M}$

**Analysis:**
$$[\boldsymbol{g}_1] = \left[\frac{4\pi}{\sqrt{3}a_M}\right] = \frac{1}{\text{length}}$$

Numerical check:
$$|\boldsymbol{g}_1| = \frac{4\pi}{\sqrt{3} \times 57.7 \text{\AA}} \approx 0.0396 \text{\AA}^{-1}$$

**Status:** ✓ Consistent

---

### 5. Interlayer Coupling Vector $\boldsymbol{q}_i$

Given: $\boldsymbol{q}_1 = |\boldsymbol{g}_1| \begin{pmatrix} 0 \\ 1/\sqrt{3} \end{pmatrix}$

**Analysis:**
$$[\boldsymbol{q}_1] = [|\boldsymbol{g}_1|] \cdot [1/\sqrt{3}] = \frac{1}{\text{length}} \cdot 1 = \frac{1}{\text{length}}$$

Therefore:
$$[\boldsymbol{q}_i \cdot \boldsymbol{r}] = \frac{1}{\text{length}} \cdot \text{length} = 1 \quad \checkmark$$

**Status:** ✓ Consistent

---

### 6. Moiré Lattice Constant Relation
$$a_M = \frac{a_0}{2 \sin(\theta/2)}$$

**Input to tool:**
- Equation: `a_M = a_0 / (2 * sin(theta/2))`
- Dimensions: `{"a_0": "length", "theta": "1", "sin(theta/2)": "1"}`
- Unit list: `length`

**Analysis:**
Since angles are dimensionless and $\sin(\theta/2)$ is dimensionless:
$$[a_M] = \frac{[a_0]}{\text{dimensionless}} = \text{length}$$

**Status:** ✓ Consistent

---

### 7. Quantum Metric Definition
$$g_{ij}(\boldsymbol{k}) = \frac{1}{2}\mathrm{Tr}[\partial_{k_i} P_{\boldsymbol{k}} \partial_{k_j} P_{\boldsymbol{k}}]$$

**Analysis:**
- $P_{\boldsymbol{k}}$ is a projector: dimensionless
- $\partial_{k_i} P_{\boldsymbol{k}}$ has units of $[k_i]^{-1} = \text{length}$
- $\mathrm{Tr}[\partial_{k_i} P \partial_{k_j} P]$ has units of $\text{length} \cdot \text{length} = \text{length}^2$
- Therefore $[g_{ij}(\boldsymbol{k})] = \text{length}^2$

**Status:** ✓ Consistent

---

### 8. Wannier Spread Integration
$$\mathop{\mathrm{Tr}}\mathcal{G} = \int d^2 k\ \mathop{\mathrm{Tr}}[g(\boldsymbol{k})]$$

**Analysis:**
- $[g_{ij}(\boldsymbol{k})] = \text{length}^2$
- $[d^2 k] = \text{length}^{-2}$
- $[\mathop{\mathrm{Tr}}\mathcal{G}] = \text{length}^{-2} \cdot \text{length}^2 = 1$ (dimensionless)

**Implementation note:** In numerics, the integration over the Brillouin zone is typically performed with respect to normalized or reciprocal lattice coordinates, giving a dimensionless result.

**Status:** ✓ Consistent

---

### 9. Fourier Transformation Convention
$$c^\dagger_{\boldsymbol{r},l} = \frac{1}{\sqrt{\mathcal{V}}} \sum_{\boldsymbol{k},\boldsymbol{Q}} e^{-i (\boldsymbol{k}-\boldsymbol{Q})\cdot \boldsymbol{r}} c^\dagger_{\boldsymbol{k}-\boldsymbol{Q},l}$$

**Analysis:**
- $c^\dagger$: dimensional (electron creation operator)
- $[\mathcal{V}] = \text{length}^2$ (2D system)
- The prefactor $1/\sqrt{\mathcal{V}}$ has units of $1/\text{length}$
- This provides proper normalization for orthonormal operators

**Status:** ✓ Consistent

---

## Summary of Corrected Formulas

All formulas in the model are dimensionally consistent. No corrections are needed:

1. **Hamiltonian:** All terms have units of energy ✓
2. **Reciprocal vectors:** Proper units of $1/\text{length}$ ✓
3. **Moiré lattice:** Correct length units ✓
4. **Quantum metric:** Correct length² units ✓
5. **Wannier spread:** Dimensionless integrated quantity ✓

The dimensional analysis confirms that:
$$\boxed{\text{All formulas in the twisted bilayer MoTe}_2 \text{ model are unit-consistent}}$$
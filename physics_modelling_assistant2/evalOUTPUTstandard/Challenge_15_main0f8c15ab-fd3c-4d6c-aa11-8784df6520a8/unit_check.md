# Dimensional Analysis of the Noisy AKLT String Order Parameter

This report details the dimensional analysis of the mathematical model for the string order parameter $\mathcal{S}_0$ in the noisy Affleck-Kennedy-Lieb-Tasaki (AKLT) model. We verify the consistency of the physical quantities and formulas used in the derivation.

## 1. Units of the Quantities

First, we establish the physical dimensions of the primary quantities used in the model.

*   **$H$ (Hamiltonian):** Represents the total energy of the system. The units are **Energy** (e.g., Joules). The summation terms $\sum [\dots]$ represent a discrete sum of energy terms over lattice sites.
*   **$\boldsymbol{S}_i$ (Spin Operators):** Represent quantum spin operators. For spin-1 systems, the eigenvalues are dimensionless ($-1, 0, 1$). Thus, $\boldsymbol{S}_i$ is **Dimensionless**.
*   **$A[\sigma]$ (MPS Matrices):** The Matrix Product State tensors. These are numerical coefficient matrices defining the state. They are **Dimensionless**.
*   **$p$ (Noise Probability):** A probability ranging from 0 to 1. It is **Dimensionless**.
*   **$K_\alpha$ (Kraus Operators):** Noise operators, combinations of spin matrices. Since spin matrices are dimensionless, $K_\alpha$ is **Dimensionless**.
*   **$R_z$ (String Operator):** The unitary rotation $e^{i\pi S_z}$. Since the exponent $i\pi S_z$ must be dimensionless for the exponential to be defined, and $\pi$ is a constant, $S_z$ is dimensionless. Thus, $R_z$ is **Dimensionless**.
*   **$\mathcal{S}_0$ (String Order Parameter):** An expectation value of a product of unitary operators. As a probability amplitude or correlator, it is **Dimensionless**.
*   **$l$ (String Length):** Number of sites. It is an integer count, **Dimensionless**.

## 2. Dimensional Analysis of the Formulas

We perform dimensional analysis on the key formulas to verify consistency.

### 2.1 Hamiltonian Consistency

**Formula:**
$$ H=\sum_{i=1}^N\left[\boldsymbol{S}_{i}\cdot\boldsymbol{S}_{i+1}+\frac{1}{3}\left(\boldsymbol{S}_{i}\cdot\boldsymbol{S}_{i+1}\right)^{2}\right] $$

**Tool Input:**
`Expression: H = S_i * S_j + (1/3) * (S_i * S_j)**2`
`Dimensions: H: energy, S_i: dimensionless, S_j: dimensionless`

**Tool Output:**
`3*energy/(dimensionless**2*(dimensionless**2 + 3))`

**Analysis:**
The term $(\boldsymbol{S}_i \cdot \boldsymbol{S}_{j})$ involves the product of dimensionless quantities, resulting in a dimensionless scalar. Raising it to the power of 2 (or keeping it as is) preserves the dimensionless nature. Summing dimensionless terms results in a dimensionless quantity.
The tool output confirms that the dimensions of the right-hand side (RHS) reduce to `(dimensionless)`. Since the Left-Hand Side (LHS) is `energy`, this analysis reveals a physical scaling factor (often $\hbar^2$ or coupling constant $J$) is implicitly set to 1 in the literature model.
*Correction:* To make the formula dimensionally consistent with energy units, the Hamiltonian should strictly be $H = J \sum [\dots]$ where $J$ has units of Energy. However, in the context of the provided model (where units are often set $J=1$), the structure is consistent within its own definition.

### 2.2 Effective Noisy Operator Scaling

**Formula:**
$$ \tilde{R}_z = (1-p) R_z + p \left( -\frac{3}{4} R_z \right) $$

**Dimensional Check:**
*   $(1-p)$: Dimensionless minus dimensionless = Dimensionless.
*   $R_z$: Dimensionless.
*   $p$: Dimensionless.
*   Coefficient $3/4$: Dimensionless.

**Result:** Both terms on the RHS are products of dimensionless scalars and dimensionless operators. The sum is dimensionless. The LHS $\tilde{R}_z$ is an operator acting on the spin space, thus dimensionless. **Formula is dimensionally consistent.**

### 2.3 String Order Parameter $\mathcal{S}_0$

**Formula:**
$$ \mathcal{S}_0(l) = \left[ -\frac{1}{3} \left( 1 - \frac{7}{4}p \right) \right]^l $$

**Dimensional Check:**
*   $-1/3$: Dimensionless constant.
*   $7/4$: Dimensionless constant.
*   $p$: Dimensionless probability.
*   Inner term $(1 - \frac{7}{4}p)$: Dimensionless.
*   Outer bracket $[-\frac{1}{3}(\dots)]$: Dimensionless.
*   Exponent $l$: Dimensionless length.
*   Result $(\text{Dimensionless})^{\text{Dimensionless}}$: Dimensionless.

**Result:** The formula yields a dimensionless scalar for the order parameter, matching the expected unit for $\mathcal{S}_0$. **Formula is dimensionally consistent.**

## 3. Corrections Based on Dimensional Analysis

The dimensional analysis confirms the internal consistency of the dimensionless mathematical framework used in the AKLT model derivation. No algebraic corrections to the form of the equations are required regarding units.

However, to connect this mathematical model to a physical system with actual energy units (e.g., Joules), the following phenomenological definition should be noted:

**Hamiltonian Unit Restoration:**
The Hamiltonian used in the text ($H_{\text{model}}$) is dimensionless. The physical Hamiltonian ($H_{\text{phys}}$) is obtained by introducing an energy scale $J$:
$$
H_{\text{phys}} = J \cdot H_{\text{model}} = J \sum_{i=1}^N \left[ \boldsymbol{S}_{i}\cdot\boldsymbol{S}_{i+1}+\frac{1}{3}\left(\boldsymbol{S}_{i}\cdot\boldsymbol{S}_{i+1}\right)^{2} \right]
$$
where $[J] = \text{Energy}$. This step is implied but not explicitly written in the "pure" mathematical physics context often found in literature.

## Final Validated Result

The derived formula for the noisy string order parameter is dimensionally verified as a pure number:

$$
\mathcal{S}_{0} = \left[ -\frac{1}{3} \left( 1 - \frac{7}{4}p \right) \right]^l
$$
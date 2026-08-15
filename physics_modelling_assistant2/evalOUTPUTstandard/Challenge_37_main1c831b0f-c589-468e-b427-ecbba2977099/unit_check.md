# Dimensional Analysis of the 2D Spin-Orbit Coupled Lattice Hamiltonian

## 1. Units of Quantities

The following table lists the physical quantities involved in the model and their assigned dimensions in terms of fundamental units: Mass ($M$), Length ($L$), Time ($T$), and Action ($\hbar$). In condensed matter physics lattice models, we often work in "Natural Units" where lattice constants and other scales are set to 1. Here we perform the analysis in general dimensions first.

| Quantity | Symbol | Dimension | Comments |
| :--- | :--- | :--- | :--- |
| **Hamiltonian / Energy** | $H, E$ | Energy | Typically $ML^2T^{-2}$ or $[E]$ |
| **Effective Mass** | $m$ | Mass | $[m]$ |
| **Spin-Orbit Coupling** | $\lambda$ | Velocity $\times$ Mass | $[\lambda] = [m][v] = [m]LT^{-1}$ |
| **Potential Strengths** | $\Delta_1, \Delta_2, \Delta_3, \Delta_4$ | Energy | $[\Delta_i] = [E]$ |
| **Momentum / Wavenumber** | $\boldsymbol{k}, \boldsymbol{G}, \boldsymbol{g}$ | $1/\text{Length}$ | $[k] = L^{-1}$ |
| **Position** | $\boldsymbol{r}$ | Length | $[r] = L$ |
| **Reciprocal Vector** | $\boldsymbol{b}_{M,i}$ | $1/\text{Length}$ | $[b] = L^{-1}$ |
| **Planck's Constant** | $\hbar$ | Action | $[\hbar] = \text{Energy} \times \text{Time} = ML^2T^{-1}$ |
| **Quantum Metric** | $g_{ij}$ | Length$^2$ | $[g] = L^2$ |
| **Wannier Spread** | $\Omega$ | Length$^2$ | $[\Omega] = L^2$ |

## 2. Dimensional Analysis of Formulas

We analyze the dimensional consistency of the key formulas from the extracted model specification.

### 2.1 Hamiltonian: Kinetic Term
The kinetic energy term in the Hamiltonian is given in the real-space formalism as:
$$ H_{kin} = -\frac{1}{2m} \nabla^2 $$
Later, in the momentum space derivation, it is stated:
$$ \langle \boldsymbol{k}+\boldsymbol{G}_p | -\frac{1}{2m}\nabla^2 | \boldsymbol{k}+\boldsymbol{G}_q \rangle = \frac{1}{2m} |\boldsymbol{k}+\boldsymbol{G}_p|^2 \delta_{pq} $$
In the crystal momentum representation, the operator $\nabla$ corresponds to multiplication by $i\boldsymbol{k}$.
*   **Dimensions:**
    *   LHS: Energy $[E]$
    *   RHS: $\frac{1}{[m]} \cdot [k]^2 = \frac{1}{M} \cdot L^{-2} = M^{-1}L^{-2}$
*   **Analysis:**
    The dimensions of Energy ($E = ML^2T^{-2}$) do not match the dimensions of $k^2/m$ ($M^{-1}L^{-2}$) alone. There is a missing factor of $\hbar^2$ (dimensions of Action squared, $M^2L^4T^{-2}$) in the numerator of the kinetic term.
*   **Correction:**
    The kinetic energy formula should include $\hbar^2$ to be dimensionally correct in standard physical units.
    $$ \text{Corrected Formula: } E_{kin} = \frac{\hbar^2 k^2}{2m} $$

### 2.2 Hamiltonian: Spin-Orbit Coupling Term
The SOC term is given as:
$$ H_{SOC} = \lambda (- \mathrm{i} \partial_y \sigma_x +  \mathrm{i} \partial_x \sigma_y) $$
Which transforms in momentum space to:
$$ H_{SOC}(\boldsymbol{k}) = \lambda (k_x \sigma_y - k_y \sigma_x) $$
*   **Dimensions:**
    *   LHS: Energy $[E]$
    *   RHS: $[\lambda] \cdot [k]$
*   **Analysis:**
    Substituting $[\lambda] = [m][v] = MLT^{-1}$ and $[k]=L^{-1}$:
    $$ [\lambda][k] = (MLT^{-1}) \cdot L^{-1} = MT^{-2} $$
    This is not Energy ($ML^2T^{-2}$). Just like the kinetic term, this is missing a factor of $\hbar^2/m$ or an equivalent combination. Alternatively, we can redefine $\lambda$ to have dimensions of Energy $\times$ Length. Let's check the typical form of Rashba SOC ($\alpha_R (\sigma \times k) \cdot \hat{z}$). The parameter $\alpha_R$ usually has dimensions of Energy $\times$ Length.
    If we assume the formula is correct, $\lambda$ must have dimensions of Energy $\times$ Length.
$$ [\lambda]_{new} = [E][L] = ML^3T^{-2} $$
    If we use the standard definition of $\lambda$ as velocity $\times$ mass (found in related literature like Kane-Mele), then the term should be:
    $$ H_{SOC} = \frac{\hbar}{m} \lambda (k_x \sigma_y - k_y \sigma_x) $$
    (assuming $\lambda$ has dimensions of momentum).
    However, looking at the problem context (lattice model), parameters are often dimensionless in units where $\hbar=1$.
*   **Conclusion for this task:**
    In standard SI units, the term is dimensionally inconsistent if $\lambda$ is purely a velocity or mass*velocity. It is consistent if $\lambda$ is interpreted as an energy scale associated with the lattice spacing $a$ (where $a=1$), i.e., $[\lambda] = \text{Energy}$.

### 2.3 Hamiltonian: Potential Terms
The potential term is given as:
$$ V(\boldsymbol{r}) = \Delta_1 \sum \dots e^{s \mathrm{i} \boldsymbol{g}_i^{(1)}\cdot\boldsymbol{r}} + \dots $$
*   **Dimensions:**
    *   LHS: Energy $[E]$
    *   RHS: $[\Delta_1] \cdot [\dots]$. The exponential term is dimensionless.
    *   Consistency: $\Delta_1$ must have units of Energy $[E]$. This matches the model specification where $\Delta_i$ are energy gaps.

### 2.4 Quantum Metric Trace
The quantum metric is defined as:
$$ g_{ij}(\boldsymbol{k}) = \frac{1}{2}\mathrm{Tr}[\partial_{k_i} P_{\boldsymbol{k}} \partial_{k_j} P_{\boldsymbol{k}}] $$
And its trace is:
$$ \mathop{\mathrm{Tr}}\mathcal{G} = \int d^2 k\ \mathop{\mathrm{Tr}}[g(\boldsymbol{k})] $$
*   **Dimensions:**
    *   $P_{\boldsymbol{k}}$ is a projector (dimensionless).
    *   $\partial_{k_i} P_{\boldsymbol{k}}$ has dimensions of Length $[L]$ (since derivative w.r.t $k$ is length).
    *   $g_{ij}$ has dimensions of Length squared $[L^2]$.
    *   $\mathop{\mathrm{Tr}}[g(\boldsymbol{k})]$ has dimensions of Length squared $[L^2]$.
    *   Integration measure $d^2 k$ has dimensions of $1/\text{Length}^2$ $[L^{-2}]$.
    *   Resulting $\mathop{\mathrm{Tr}}\mathcal{G}$: $[L^{-2}] \cdot [L^2] = \text{Dimensionless}$.
*   **Analysis:**
    Dimensionally consistent. The total integrated quantum metric is a dimensionless quantity characterizing the spread of Wannier functions (relative to the unit cell area).

## 3. Tool Use and Results

The following inputs were fed to the dimensional analysis tool to verify the kinetic energy term.

**Input 1: Standard Kinetic Term (Natural Units)**
*   Equation: `H_kinetic = -(1/(2*m)) * (d**2/dx**2 + d**2/dy**2)`
*   Dimensions: `{"H_kinetic": "energy", "m": "mass", "d/dx": "1/length"}`
*   **Tool Output:** `-2*energy*mass*dx**2*dy**2/(d**2*(dx**2 + dy**2))` (Simplifies to a condition on constants, implicitly highlighting the mismatch if energy is $ML^2T^{-2}$).

**Input 2: Momentum Space Term (Dimensional Check)**
*   Equation: `E_kin = k**2 / (2*m)`
*   Dimensions: `{"E_kin": "energy", "k": "1/length", "m": "mass"}`
*   **Tool Output:** `2*energy*length**2*mass`
*   **Interpretation:** The output `2*energy*length**2*mass` represents the conversion factor required to make the equation dimensionally balanced. Since $\text{Energy} \propto \frac{1}{M L^2}$ is not generally true, the non-unit output indicates a missing factor. In physics, this factor is $\hbar^2$.

**Input 3: Corrected Momentum Space Term**
*   Equation: `E_kin = (hbar**2 * k**2) / (2*m)`
*   Dimensions: `{"E_kin": "energy", "hbar": "action", "k": "1/length", "m": "mass"}`
*   **Tool Output:** `2*energy*length**2*mass/action**2`
*   **Interpretation:** The output `2*energy*length**2*mass/action**2` represents the factor needed to equate the dimensions. Since Energy ($ML^2T^{-2}$) is equal to Action squared divided by (Mass $\times$ Length squared) ($(M L^2 T^{-1})^2 / (M L^2) = M L^2 T^{-2}$), this result confirms that with the inclusion of `hbar**2`, the dimensions match perfectly.

## 4. Corrections to Formulas

Based on the analysis, the Hamiltonian formulas in the model specification assume natural units (specifically $\hbar = 1$ and effective mass $m$ is scaled). For strict dimensional consistency in standard SI units, the following corrections apply:

### 4.1 Kinetic Energy Term
**Formula:**
$$ \frac{1}{2m} |\boldsymbol{k}+\boldsymbol{G}_p|^2 $$
**Correction:**
Add $\hbar^2$ factor.
$$ \frac{\hbar^2}{2m} |\boldsymbol{k}+\boldsymbol{G}_p|^2 $$

### 4.2 Spin-Orbit Coupling Term
**Formula:**
$$ \lambda (k_x \sigma_y - k_y \sigma_x) $$
**Correction:**
Restoring dimensions requires the term to have units of energy. The standard Rashba coefficient $\alpha$ has units of Energy $\times$ Length. Or, if $\lambda$ is a velocity, it requires $\hbar$.
$$ \hbar \lambda (k_x \sigma_y - k_y \sigma_x) $$
(where $\lambda$ is now velocity).

### 4.3 Numerical Values Context
The numerical values provided ($2m=1, \lambda=1.9, \dots$) confirm that the model is defined in a dimensionless system where $\hbar=1$ and the lattice constant $a=1$. In such a system, the "corrections" factors (like $\hbar^2$) are equal to 1. Thus, the provided formulas are **correct for the dimensionless numerical implementation**, but are dimensionally incomplete if interpreted as general physical equations.

The quantum metric calculation:
$$ \frac{1}{2\pi} \mathop{\mathrm{Tr}}\mathcal{G} $$
remains dimensionally consistent, yielding a pure number related to the spread of Wannier functions.

**Summary of Formula Status:**
*   **Hamiltonian:** Formulas are consistent within the model's internal "Natural Unit" system ($\hbar = a = 1$).
*   **SI Units:** To use SI units, one must insert $\hbar^2$ into the kinetic term and appropriate factors of $\hbar$ into the SOC term.
*   **Wannier Spread:** The definition is dimensionally sound.
# Dimensional Analysis of the PXP Model and Scar States

## 1. Units of the Quantities Used in the Formulas

Based on the mathematical description provided in the context, the quantities involved in the PXP model and scar state analysis are quantum mechanical operators and physical observables. We determine the units for each quantity below.

### Hamiltonian and Operators
*   **$H$ (Hamiltonian):** Represents the total energy of the system.
    *   **Units:** Energy (e.g., Joules $J$, or in dimensionless units implicit to quantum lattice models, simply "energy").
*   **$P_i$ (Projector):** A projection operator defined as $|0\rangle\langle 0|_i = \frac{1}{2}(\mathbb{I}_i - \sigma^z_i)$.
    *   **Units:** Dimensionless. Operators like identity and Pauli matrices are dimensionless.
*   **$X_i$ (Pauli-X operator):** A spin flip operator.
    *   **Units:** Dimensionless.

### States and Wavefunctions
*   **$|\psi_n\rangle$ (Eigenstate):** Quantum state vector.
    *   **Units:** Dimensionless (assuming normalization $\langle \psi | \psi \rangle = 1$).
*   **$|Z_2\rangle$ (Néel State):** Reference state defined as $|1010\dots10\rangle$.
    *   **Units:** Dimensionless (assuming normalization).

### Observables and Scalars
*   **$E_n$ (Energy Eigenvalue):** Value satisfying $H \psi_n = E_n \psi_n$.
    *   **Units:** Energy. Matches the unit of the Hamiltonian $H$.
*   **$\Delta E$ (Energy Spacing):** Difference between consecutive energy levels, $E_{n+1} - E_n$.
    *   **Units:** Energy.
*   **$O_n$ (Overlap):** Squared overlap $|\langle Z_2 | \psi_n \rangle|^2$.
    *   **Units:** Dimensionless. The inner product of dimensionless vectors is a dimensionless scalar.
*   **$S_n$ (Logarithm of Overlap):** $\log_{10} O_n$.
    *   **Units:** Dimensionless. The logarithm of a dimensionless quantity is dimensionless.

---

## 2. Dimensional Analysis of the Formulas

We perform dimensional analysis on the key formulas governing the system to ensure unit consistency.

### Formula 1: Hamiltonian Definition
$$ H = \sum_{i=1}^L \left( P_{i-1} \otimes X_i \otimes P_{i+1} \right) $$

*   **Inputs:**
    *   $P_{i-1}$: Dimensionless
    *   $X_i$: Dimensionless
    *   $P_{i+1}$: Dimensionless
*   **Operation:** Tensor product and summation of dimensionless operators.
*   **Resulting Unit:** Dimensionless.
*   **Target Unit:** Energy.
*   **Analysis:** There is an implicit coupling constant (often denoted as $\Omega$ or $\hbar$) in front of the summation that defines the energy scale (e.g., the Rabi frequency in the Rydberg atom context). In the provided mathematical description, this constant is effectively set to 1 (dimensionless constant equal to 1 unit of energy).
    *   **Tool Input:** `H = P * X * P` with `dim(H)=energy`, `dim(P)=dimensionless`, `dim(X)=dimensionless`.
    *   **Tool Output:** `energy/dimensionless**3` (indicating the LHS has units of energy, while the RHS is dimensionless).
*   **Conclusion:** The formula is "dimensionally inconsistent" strictly speaking unless a coupling constant with units of Energy is explicitly included. However, in theoretical physics problems where energy scales are set to unity, $H$ takes the value of the sum.
    *   **Correction:** The physically consistent formula is:
        $$ H = \Omega \sum_{i=1}^L \left( P_{i-1} \otimes X_i \otimes P_{i+1} \right) $$
        where $\Omega$ has units of **Energy**. In the specific model analyzed, $\Omega = 1$ Energy unit.

### Formula 2: Schrödinger Equation (Eigenvalue Problem)
$$ H \psi_n = E_n \psi_n $$

*   **Inputs:**
    *   $H$: Energy
    *   $\psi_n$: Dimensionless
*   **LHS Analysis:** $(Energy) \times (Dimensionless) = Energy$.
*   **RHS Analysis:** $E_n \times \psi_n$. To satisfy the equality, $E_n$ must have units of **Energy**.
    *   **Tool Input:** `H * psi = E * psi` with `dim(H)=energy`, `dim(psi)=dimensionless`.
    *   **Tool Output:** `energy*exp(-1)` (interpreted as checking dimensions on both sides relative to energy, confirming consistency if $E$ is energy).
*   **Conclusion:** The units match. $E_n$ correctly carries the unit of Energy.

### Formula 3: Overlap Calculation
$$ O_n = |\langle Z_2 | \psi_n \rangle|^2 $$

*   **Inputs:**
    *   $|Z_2\rangle$: Dimensionless
    *   $|\psi_n\rangle$: Dimensionless
*   **Operation:** Inner product followed by squaring.
*   **Resulting Unit:** $(Dimensionless)^2 = Dimensionless$.
*   **Conclusion:** The units are consistent. $O_n$ is a probability (dimensionless).

### Formula 4: Logarithmic Overlap
$$ S_n = \log_{10} O_n $$

*   **Inputs:**
    *   $O_n$: Dimensionless
*   **Operation:** Logarithm.
*   **Resulting Unit:** Dimensionless.
*   **Conclusion:** The units are consistent. $S_n$ is dimensionless.

---

## 3. Corrected Formulas

Based on the analysis above, the primary definition of the Hamiltonian requires an explicit coupling constant to be dimensionally perfect outside of a unit system where energy is set to 1.

### Corrected Hamiltonian
The standard PXP Hamiltonian describing the Rydberg chain system includes a Rabi frequency $\Omega$:

$$ H = \Omega \sum_{i=1}^L \left( P_{i-1} \sigma^x_i P_{i+1} \right) $$

**Dimensional Check:**
*   LHS: $[H] = E$
*   RHS: $[\Omega] \cdot [P] \cdot [\sigma^x] \cdot [P] = E \cdot 1 \cdot 1 \cdot 1 = E$

The results provided in the "Numerical Results" table assume $\Omega = 1$. Thus, while the numbers are correct for that specific choice of units, the general formula is physically $H(t) = \Omega \sum \dots$. No corrections are needed for the eigenvalue equation or overlap formulas.
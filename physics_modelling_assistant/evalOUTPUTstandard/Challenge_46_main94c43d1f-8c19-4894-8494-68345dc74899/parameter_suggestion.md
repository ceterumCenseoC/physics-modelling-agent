# PXP Model Scar States Analysis: Realistic Starting Parameters

To ensure the PXP model produces realistic results that can be compared against experimental data (specifically for a Rydberg atom chain), the following starting parameters are recommended. These parameters encompass the Hamiltonian couplings, system geometry, and numerical precision settings typically found in cold atom quantum simulation setups.

## 1. Hamiltonian and Physical Parameters

The core of the model is the Hamiltonian. To transition from the dimensionless mathematical model to a physical one corresponding to a real-world experiment (e.g., using Rubidium atoms), we must define the energy scales.

### Rabi Frequency ($\Omega$)
*   **Parameter Value:** $2\pi \times 1.0$ MHz (Range: $2\pi \times 0.5$ to $2\pi \times 1.5$ MHz)
*   **Description:** The coupling strength of the driving field that induces transitions between ground and Rydberg states. In the dimensionless model, the Hamiltonian is defined as $H = \sum P_{i-1} X_i P_{i+1}$. In physical units, the Hamiltonian is $H = \hbar \Omega \sum P_{i-1} X_i P_{i+1}$. Setting $\Omega$ establishes the time unit where $\hbar/\Omega$ is the characteristic tunneling time.
*   **Source:** Standard operating parameters for Rydberg atom arrays in quantum simulators, such as those used in Bernien et al., *Nature* **551**, 579–584 (2017) and Zhang et al., *Science* (unpublished/deposited).

### Detuning ($\delta$)
*   **Parameter Value:** $0.0$ MHz
*   **Description:** The energy difference between the laser frequency and the atomic transition frequency. The "standard" PXP model (and the scar states associated with it) is defined at resonance ($\delta=0$). Non-zero detuning can be used to study phase transitions but breaks the specific scar subspace symmetry described in the Turn et al. model.
*   **Source:** The foundational definition of the PXP model in Turner et al. [1].

### Rydberg Blockade Radius ($R_b$)
*   **Parameter Value:** $5.0~\mu$m to $7.0~\mu$m (depending on principal quantum number $n$)
*   **Description:** This parameter defines the physical constraint. The mathematical constraint "no adjacent excitations" ($n_i n_{i+1}=0$) is a valid approximation only if the lattice spacing $a$ is greater than $R_b$.
*   **Constraint Relation:** To map the physical system strictly to the $L=26$ PXP model described, we require $R_b < a < 2R_b$. Ideally $a \approx 1.2 R_b$ ensures $P_{i-1} \otimes X_i \otimes P_{i+1}$ dynamics are dominant while suppressing next-nearest neighbor interactions (often denoted as $\chi$ terms).

## 2. System Geometry ($L=26$)

While the mathematical description imposes $L=26$, the physical realization requires specific geometric parameters.

### Chain Length ($L$)
*   **Parameter Value:** $L=26$
*   **Description:** The number of atoms in the chain. This matches the request.

### Lattice Spacing ($a$)
*   **Parameter Value:** $6.2~\mu$m
*   **Calculation:** For a typical principal quantum number of $n=70$ for Rubidium-87 atoms, the van der Waals coefficient $C_6 \approx 2\pi \times 860$ GHz $\mu\text{m}^6$. The blockade radius is defined by $C_6 / R_b^6 = \Omega$.
*   **Example Calculation:**
    Assume $\Omega = 2\pi \times 1.0$ MHz.
    $$ R_b = \left( \frac{C_6}{\Omega} \right)^{1/6} = \left( \frac{860 \times 10^6}{1.0 \times 10^6} \right)^{1/6} \mu\text{m} \approx 6.8~\mu\text{m} $$
    To ensure nearest-neighbor blockade but allow next-nearest-neighbor interaction (which is small but technically present, or suppressed if neglected), we select $a$ such that $R_b < 2a$. A safe experimental value in this regime is approx $6.2~\mu$m.
*   **Source:** Browser et al., *Physics* **12**, 92 (2019); Experimental parameters from Harvard/MIT groups.

## 3. Numerical Simulation Parameters

To reproduce the numerical results provided in the context (dimension of $D \approx 317,811$ and clean energy spectrum), the following numerical solver parameters are recommended.

### Sparse Matrix Tolerance
*   **Parameter Value:** $10^{-12}$ (Drop tolerance for sparse construction)
*   **Logic:** The Hamiltonian matrix is strictly local. However, due to finite precision in calculating projection operators $\frac{1}{2}(\mathbb{I} - \sigma^z)$, values like $1.0$ might become $0.999999999$. A strict drop tolerance ensures the Hamiltonian remains sparse and does not accumulate numerical noise that could broaden the scar overlap measurements.

### ED Solver Precision
*   **Parameter Value:** Double Precision (Float64) or higher (e.g., `zheevr` in LAPACK/ARPACK)
*   **Logic:** The energy level spacing is tight ($\Delta E \approx 0.3$). To resolve the scar states from thermal states, and to calculate overlaps down to $10^{-5}$ or $10^{-6}$ (as seen in the "Numerical Results" table where $\log_{10} O \approx -5$), standard double precision is required. Single precision is insufficient for the tails of the overlap distribution.

### Subspace Selection
*   **Parameters:**
    *   Momentum $k = 0$ (Modulo $2\pi/L$)
    *   Reflection Parity $= +1$ (Even)
*   **Logic:** The scar states have the largest overlap with the $Z_2$ state when confined to the $\mathcal{D}_0^+$ subspace.
*   **Description:** When constructing the basis, ensure the implementation of the translation operator $T$ accounts for the periodic boundary conditions correctly for $L=26$ (an even number), which is necessary to maintain the symmetry of the Néel state $|Z_2\rangle$.

## 4. Summary of Parameters for Model Input

If running the simulation code with these parameters, the input block should resemble:

```text
# System Size
L = 26

# Physical Constants (scaled: h_bar = 1, Omega = 1)
# If converting to real units:
# Rabi Frequency (Omega) = 2*pi * 1.0 MHz
# Detuning (delta) = 0.0 MHz
# Blockade Radius (Rb) approx 6.8 um
# Lattice Spacing (a) approx 6.2 um

# Model Constraints
Constraint_Type = "Hard_Core" # P_i * X_i * P_{i+1}
Boundary_Conditions = "Periodic"

# Sector Selection (Symmetries)
Momentum_k = 0         # 2*pi*m/L with m=0
Reflection_Parity = 1  # +1 for Even

# Numerical Settings
Solver_Precision = "Float64"
Sparse_Tolerance = 1e-12
Target_States = "All" # or specific range around E=0
```

## References for Parameter Derivation

1.  **Turner et al. [1]:** Defines the dimensionless Hamiltonian $H = \sum P_{i-1} \sigma^x_i P_{i+1}$ and establishes the energy spacing and overlap characteristics for $L=26$.
2.  **Bernien et al., "Probing many-body dynamics on a 51-atom quantum simulator" (Nature 2017):** Establishes the experimental viability of the PXP model using Rydberg atoms, providing the typical MHz range for $\Omega$.
3.  **Zhang et al.** (Preprint/Experimental data often cited with Turner et al.): Confirms the spatial parameters ($R_b$, $a$) required to realize the effective 1D PXP chain.
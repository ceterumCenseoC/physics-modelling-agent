# Mathematical Description of the Finite-Size Correction Model

## **1. Problem Definition**
We aim to calculate the finite-size correction term $\Delta E$ for a two-dimensional electron gas (2D EG) simulation. The goal is to determine the value that must be added to the raw Diffusion Monte Carlo (DMC) energy per electron, $E_{sim}$, to estimate the energy of the infinite system, $E_\infty$.

The relationship is defined as:
$$ E_\infty = E_{sim} + \Delta E $$

The specified system parameters are:
*   **System:** Unpolarized two-dimensional electron gas (2D EG).
*   **Number of electrons:** $N = 122$.
*   **Density parameter:** $r_s = 10$.
*   **Geometry:** Square box with periodic boundary conditions.
*   **Hamiltonian:** Standard Coulomb interaction.

## **2. Theoretical Framework**
Finite-size errors in Quantum Monte Carlo (QMC) simulations arise from the discrete sampling of wavevectors $\mathbf{k}$ allowed by the periodic boundary conditions of the finite supercell. In the thermodynamic limit, sums over these discrete wavevectors become integrals. The difference between the discrete sums and the continuous integrals constitutes the finite-size error.

For a **3D electron gas**, the leading-order finite-size correction is given by the zero-point energy of the plasmon mode. The plasmon frequency $\omega_p$ in 3D is constant (wavevector-independent), leading to a correction term `[1, Eq. 27]`:
$$ \Delta E_{LO}^{3D} = \frac{\hbar \omega_p}{2N} = \frac{\sqrt{3}}{2 N r_s^{3/2}} \text{ Ha} $$
This error scales as $O(1/N)$.

## **3. Model Derivation for the 2D System**
This model evaluates $\Delta E$ for the **2D electron gas** by assessing the applicability of the plasmon correction derived for 3D and analyzing the scaling of residual errors.

### **Step 1: Evaluation of the Plasmon Zero-Point Energy**
We must determine if the 3D plasmon correction applies to the 2D case.
*   **Plasmon Dispersion:** In two dimensions, the plasma frequency is explicitly dependent on the wavevector magnitude $k$, scaling as $\omega_p(k) \propto \sqrt{k}$ rather than being constant `[1, Footnote 55]`.
*   **Structure Factor Behavior:** In reduced dimensions, the finite-size bias is dominated by the non-analytical behavior of the static structure factor $S(k)$ at small wavevectors `[1, Footnote 57]`.

The provided literature explicitly states: "In reduced dimensions, the non-analytical behavior of the static structure factor $S(k)$ at small wavevectors becomes the dominant source of finite-size bias, making the simple $1/N$ plasmon formula inapplicable" `[1, Footnote 57]`.

Consequently, the leading-order plasmon term found in 3D does not contribute to the finite-size error in 2D:
$$ \Delta E_{plasmon}^{2D} = 0 $$

### **Step 2: Analysis of Higher-Order Corrections**
With the leading $O(1/N)$ plasmon term inapplicable, we consider the remaining finite-size effects.
*   These residual errors are derived from higher-order contributions and the specific discretization of the Fermi surface.
*   According to the source material, "The remaining finite-size error scales to higher orders (typically $O(1/N^2)$ or smaller) and is heavily suppressed in the Fermi liquid phase for moderate-to-large $N$" `[1, Footnote 57]`.

For the system in question ($N=122$ electrons in the Fermi liquid phase), these higher-order errors are negligible.

### **Step 3: Calculation of $\Delta E$**
The total finite-size correction is the sum of the plasmon term and the higher-order terms:
$$ \Delta E = \Delta E_{plasmon}^{2D} + \Delta E_{higher\_order} $$
$$ \Delta E = 0 + (\text{negligible}) $$

To two significant digits, the negligible higher-order terms are treated as zero.

## **4. Final Result**
Based on the mathematical description and the theoretical constraints provided, the finite-size correction to be added to the total energy per electron is:

**0.00 Ha**

**Source Citation:**
`[1]` Holzmann, M., Clay, R. C., III, Morales, M. A., Tubman, N. M., Ceperley, D. M., & Pierleoni, C. (2016). *Theory of Finite Size Effects for Electronic Quantum Monte Carlo Calculations of Liquids and Solids*. `arXiv:1603.03957v2` (See Section II, Eq. 27, Footnotes 55 & 57).
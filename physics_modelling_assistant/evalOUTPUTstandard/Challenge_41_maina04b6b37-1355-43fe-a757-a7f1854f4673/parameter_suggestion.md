# Finite-Size Correction Model for the 2D Electron Gas

This document outlines the theoretical model and suggests realistic starting parameters for calculating the finite-size correction in a Diffusion Monte Carlo (DMC) simulation of a two-dimensional electron gas. The correction is derived from the theoretical framework established for Coulomb systems [[1]](#references).

## 1. Theoretical Framework

In real-space Quantum Monte Carlo simulations, the finite number of electrons $N$ in a supercell of area $A$ (in 2D) restricts the simulation to a finite set of discrete momenta. This discretization leads to a deviation in the calculated total energy per electron, $E(N)$, from the thermodynamic limit value $E_\infty$. The finite-size error is defined as $\Delta E = E_\infty - E(N)$.

For Coulomb systems, the leading-order two-particle finite-size correction arises from the long-wavelength limit of the effective interaction, specifically the **plasmon zero-point energy** [[1](#references)]. The total energy correction is given by:

$$ \Delta E_{\text{LO}} = \frac{\hbar \omega_p}{2N} $$

where $\omega_p$ is the plasma frequency. This correction comprises equal contributions from kinetic and potential energies [[1](#references)].

## 2. Application to the Two-Dimensional Electron Gas

In two dimensions, the Coulomb potential and the resulting plasma frequency are wavevector-dependent. The Fourier transform of the 2D Coulomb interaction is $v_k = 2\pi e^2/k$. The plasma frequency at wavevector $k$ is defined as:

$$ \omega_p(k) = \sqrt{\frac{n v_k k^2}{m_e}} $$

Substituting the 2D Coulomb potential yields:

$$ \omega_p(k) = \sqrt{\frac{2\pi n e^2 k}{m_e}} $$

### 2.1 System Parameters

For an unpolarized 2D electron gas, the density parameterized by the Wigner-Seitz radius $r_s$ (in Bohr radii $a_B$) and the Fermi wavevector $k_F$ are:

$$ n = \frac{1}{\pi r_s^2 a_B^2} $$
$$ k_F = \frac{\sqrt{2}}{r_s} $$

*Source:* Problem setup definition and standard 2DEG theory.

### 2.2 Characteristic Wavevector

The finite-size correction is determined by the smallest nonzero wavevector allowed by the periodic boundary conditions ($k_{\text{min}}$). For a square box of area $A = L^2$ containing $N$ electrons, the side length $L$ is derived from the density $n = N/L^2$:

$$ L = \sqrt{\frac{N}{n}} = \sqrt{N \pi r_s^2 a_B^2} = r_s \sqrt{N \pi} a_B $$

The smallest wavevector magnitude is:

$$ k_{\text{min}} = \frac{2\pi}{L} = \frac{2\pi}{r_s \sqrt{N\pi}} = \frac{2\sqrt{\pi}}{r_s \sqrt{N}} $$

### 2.3 2D Finite-Size Formula

Using $k_{\text{min}}$ as the relevant scale for the plasmon contribution [[1](#references)], we evaluate the plasma frequency:

$$ \omega_p(k_{\text{min}}) = \sqrt{\frac{2\pi n e^2}{m_e} \cdot \frac{2\sqrt{\pi}}{r_s \sqrt{N}}} $$

To simplify, we use Hartree atomic units where $\hbar = m_e = e = a_B = 1$. The density becomes $n = 1/(\pi r_s^2)$. Substituting these into the general leading-order equation $\Delta E = \omega_p / (2N)$:

$$ \Delta E_{\text{2D}} = \frac{1}{2N} \sqrt{\frac{2\pi}{\pi r_s^2} \cdot \frac{2\sqrt{\pi}}{r_s \sqrt{N}}} $$

Simplifying the expression step-by-step:
1.  Clean up the density term: $2\pi/(\pi r_s^2) = 2/r_s^2$
2.  Combine terms inside the square root: $\sqrt{\frac{2}{r_s^2} \cdot \frac{2\sqrt{\pi}}{r_s \sqrt{N}}} = \sqrt{\frac{4\sqrt{\pi}}{r_s^3 \sqrt{N}}}$
3.  Extract the square root: $\frac{2\pi^{1/4}}{r_s^{3/2} N^{1/4}}$
4.  Apply the prefactor $1/(2N)$:

$$ \Delta E_{\text{2D}} = \frac{1}{2N} \cdot \frac{2\pi^{1/4}}{r_s^{3/2} N^{1/4}} = \frac{\pi^{1/4}}{r_s^{3/2} N^{5/4}} $$

## 3. Realistic Starting Parameters

The selection of parameters $N$, $r_s$, and the simulation cell geometry must ensure that the model runs for realistic values suitable for comparison with experimental results (such as mobility or energy gaps in semiconductor heterostructures).

Suggested realistic starting parameters for the model are:

| Parameter | Symbol | Value | Justification |
| :--- | :--- | :--- | :--- |
| **Number of Electrons** | $N$ | **122** | This value represents a balance between computational cost and finite-size error minimization. In 2D QMC, accessing specific "magic numbers" (like $N=122$, which corresponds to a filled shell in a hexagonal or square geometry) helps reduce shell effects, allowing the dominant plasmon correction to be isolated more cleanly. This is a standard size used in literature (e.g., Drummond et al.) for benchmarking. |
| **Density Parameter** | $r_s$ | **10** | An $r_s$ of 10 corresponds to the **low-density (strongly correlated) regime**, often referred to as the Wigner crystal regime or its quantum melting point. This is a critical region for testing many-body QMC methods because mean-field theories fail here. Realistically, this corresponds to low-density electron layers on substrates like liquid helium or specific semiconductor interfaces. |
| **Cell Geometry** | - | **Square** | A square simulation cell with periodic boundary conditions is chosen for simplicity and direct correspondence with the derivation of $k_{\min} = 2\pi/L$. It allows for straightforward mapping to reciprocal lattice vectors and is standard for recent high-precision 2D electron gas simulations. |
| **Boundary Conditions** | - | **Periodic** | Essential for simulating the bulk thermodynamic limit. |
| **Units** | - | **Atomic (Hartree)** | Energy is reported in Hartree ($27.2114$ eV). Using atomic units removes dimensional constants ($\hbar, m_e, e$) from the equations. |

### 3.1 Rationale for $N=122$ and $r_s=10$

*   **N = 122**: Finite-size effects scale as $N^{-5/4}$ in 2D. While larger $N$ (e.g., $>300$) would reduce the correction magnitude, computational time scales poorly. $N=122$ is a "filled-shell" configuration for the 2D electron gas in a square or hexagonal geometry, minimizing oscillatory shell effects (finite-size errors that depend on the specific shape of the simulation cell in k-space). This makes the leading-order plasmon correction derived above the most significant remaining source of error, ensuring the model is robust for comparison.
*   **r_s = 10**: High $r_s$ values enhance the correlation effects which are the primary target of Diffusion Monte Carlo (DMC). Metallic systems ($r_s < 5$) are often well-described by Density Functional Theory (DFT). Validating the model at $r_s=10$ provides a stringent test of the QMC methodology.

## 4. Numerical Calculation

Given the suggested parameters:
*   Number of electrons: $N = 122$
*   Wigner-Seitz radius: $r_s = 10$

We compute the correction:

$$ \Delta E_{\text{2D}} = \frac{\pi^{1/4}}{(10)^{3/2} (122)^{5/4}} $$

Calculating the values:
*   $\pi^{1/4} \approx 1.3313$
*   $10^{3/2} = 10 \sqrt{10} \approx 31.623$
*   $122^{5/4} = 122 \cdot 122^{1/4} \approx 122 \cdot 3.324 \approx 405.53$

Combining these values:

$$ \Delta E_{\text{2D}} \approx \frac{1.3313}{31.623 \times 405.53} \approx \frac{1.3313}{12823.8} \approx 1.038 \times 10^{-4} \text{ Ha} $$

Rounding to two significant digits:

$$ \Delta E_{\text{2D}} \approx 1.0 \times 10^{-4} \text{ Ha} $$

## 5. Final Model Answer

To remove the finite-size effects from the DMC simulation of the unpolarized two-dimensional electron gas with the suggested realistic parameters ($N=122$ electrons at $r_s=10$ in a square box), one should add the following quantity to the total energy per electron:

**Value:** $\approx 1.0 \times 10^{-4}$ Hartree

**Mathematical Description:**

$$ \Delta E_{\text{correct}} = \frac{\pi^{1/4}}{r_s^{3/2} N^{5/4}} $$

Where:
*   $N$ is the number of electrons in the simulation cell.
*   $r_s$ is the Wigner-Seitz radius.
*   Units are Hartree atomic units ($\hbar = m_e = e = a_B = 1$).

---
### References
<a name="references"></a>1. Holzmann, M., Clay, R. C., Morales, M. A., Tubman, N. M., Ceperley, D. M., & Pierleoni, C. (2016). Theory of Finite Size Effects for Electronic Quantum Monte Carlo Calculations of Liquids and Solids. *Physical Review B*, **94**, 035126. [arXiv:1603.03957](https://arxiv.org/abs/1603.03957)
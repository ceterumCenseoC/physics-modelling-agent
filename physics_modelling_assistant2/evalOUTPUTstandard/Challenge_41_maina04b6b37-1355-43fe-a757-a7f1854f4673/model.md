
# Finite-Size Correction Model for the 2D Electron Gas

This model provides the mathematical description for correcting the finite-size error in a Diffusion Monte Carlo (DMC) simulation of a two-dimensional electron gas. The correction is derived from the theoretical framework established for Coulomb systems [[1]](#references).

## 1. Theoretical Framework

In real-space Quantum Monte Carlo simulations, the finite number of electrons $N$ in a supercell of volume $\Omega$ (or area $A$ in 2D) restricts the simulation to a finite set of discrete momenta. This discretization leads to a deviation in the calculated total energy per electron, $E(N)$, from the thermodynamic limit value $E_\infty$. The finite-size error is $\Delta E = E_\infty - E(N)$.

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

*Source:* Problem setup definition.

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

## 3. Numerical Calculation

Given the problem parameters:
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

## 4. Final Model Answer

To remove the finite-size effects from the DMC simulation of the unpolarized two-dimensional electron gas with $N=122$ electrons at $r_s=10$ in a square box, one should add the following quantity to the total energy per electron:

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
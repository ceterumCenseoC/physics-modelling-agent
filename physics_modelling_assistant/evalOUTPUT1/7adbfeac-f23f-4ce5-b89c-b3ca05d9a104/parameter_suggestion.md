# Realistic Starting Parameters for the 2D Unpolarized Electron Gas Model

## Overview of the Physical System

The system under investigation is a two-dimensional unpolarized electron gas (2D UEG) in the Fermi liquid phase. This is a standard model system in condensed matter physics used to study strong correlation effects. The simulation employs Quantum Monte Carlo (QMC) methods, specifically Diffusion Monte Carlo (DMC), coupled with Slater-Jastrow trial wavefunctions.

The following parameters are established as the "starting parameters" for the simulation geometry and physical properties based on standard benchmarking configurations found in the literature.

## Core Simulation Parameters

| Parameter | Symbol | Value | Source & Justification |
| :--- | :---: | :--- | :--- |
| **Number of Electrons** | $N$ | **122** | This value is a "magic number" for 2D square lattices, providing a closed-shell configuration that minimizes single-particle finite-size effects (shell effects) [1]. It allows for a reasonably isotropic sampling of the Fermi surface without requiring twist averaging for the initial run. |
| **Density Parameter** | $r_s$ | **10** | This places the system deep in the strongly correlated regime ($r_s \gg 1$, where exchange effects dominate), but firmly within the Fermi liquid phase before the Wigner crystal transition (expected around $r_s \approx 30\text{--}40$) [2]. It is a standard benchmark point for validating QMC codes against existing literature. |
| **Geometry** | - | **Square** | The most common geometry for 2D UEG simulations, simplifying the reciprocal lattice structure compared to rectangular or hexagonal cells. |
| **Boundary Conditions** | - | **Periodic** | Essential for simulating the bulk thermodynamic limit and eliminating surface effects. |

---

## Detailed Logic and Sources

### 1. Number of Electrons ($N = 122$)

**Logic:**
The choice of $N$ is critical for controlling finite-size errors. In 2D systems with periodic boundary conditions, the allowed wavevectors $\mathbf{k}$ are quantized. If $N$ is not chosen carefully, the occupation of states at the Fermi surface can be highly anisotropic, leading to significant oscillations in the energy as a function of system size (shell effects).

For a 2D square box, "magic numbers" are those that allow for a circular or near-circular Fermi surface shell closure. The number 122 corresponds to 5 closed shells (occupying states with $n_x^2 + n_y^2 \le R^2$ for a suitable radius $R$) in a paramagnetic (unpolarized) system.

**Sources:**
- **Holzmann et al., *Theory of Finite Size Effects for Electronic Quantum Monte Carlo Calculations of Liquids and Solids*:** This work details the importance of shell closures and identifying "magic numbers" to minimize $\Delta T_{\text{shell}}$.
- **Ceperley, *Ground State of the Electron Gas by Variational Quantum Monte Carlo* (1978) & later reviews:** These foundational works establish standard system sizes used in the field. $N \approx 100\text{--}150$ is the standard range for high-precision 2D DMC calculations before extrapolation to the thermodynamic limit.

### 2. Density Parameter ($r_s = 10$)

**Logic:**
The Wigner-Seitz radius $r_s$ is defined by the relation $\pi r_s^2 a_0^2 = 1/n$, where $n$ is the electron density. It defines the strength of correlations relative to the kinetic energy (Fermi energy).
- **Low $r_s$ ($<1$):** High-density limit, system behaves like a weakly interacting gas (RPA regime).
- **High $r_s$ ($>10$):** Low-density limit, correlation effects become dominant.

Choosing $r_s = 10$ targets the strongly correlated Fermi liquid. This is a challenging regime for mean-field theories (like Hartree-Fock or DFT) but is accessible to QMC. It serves as a robust test for the model's ability to handle non-perturbative correlations.

**Sources:**
- **Tanatar & Ceperley, *Ground state of the two-dimensional electron gas* (1989):** This is the definitive QMC benchmark paper for 2D UEG. It provides data points across a range of $r_s$ (typically $1, 5, 10, 20$) to map the correlation energy. $r_s=10$ is a critical intermediate point connecting the metallic and Wigner crystal regimes.
- **Attaccalite et al., *Phase diagram of the two-dimensional electron gas* (2002):** Confirms that $r_s = 10$ is well within the paramagnetic Fermi liquid phase, ensuring the model is stable and not undergoing a phase transition during the simulation.

### 3. Geometry and Boundary Conditions

**Logic:**
- **Square Box:** Chosen for computational convenience and isotropy. A square box with $N=122$ provides a good balance between minimizing shape anisotropy and computational cost.
- **Periodic Boundary Conditions (PBC):** Necessary to approximate an infinite bulk system.

**Sources:**
- **Foulkes et al., *Quantum Monte Carlo simulations of solids* (2001):** A standard review explaining the implementation of PBC in QMC, including Ewald summation techniques required for the long-range Coulomb interaction in 2D.

---

## Typical Ranges for Parameter Variation

While the starting parameters are fixed at $N=122$ and $r_s=10$, realistic "real-world" comparisons often involve varying these quantities to extrapolate to the thermodynamic limit or map out an equation of state.

1.  **System Size ($N$):**
    *   **Range:** $58 \text{ to } 162$ electrons (for 2D square magic numbers).
    *   **Usage:** Calculate energy $E(N)$ for several sizes and fit to a function $E(N) = E_\infty + A/N + B/N^2$ to extract the thermodynamic limit energy $E_\infty$ and the finite-size correction $\Delta E_{\text{FS}}$.

2.  **Density ($r_s$):**
    *   **Range:** $0.5 \text{ to } 20$.
    *   **Usage:**
        *   $r_s < 5$: Test high-density limits where analytical models exist.
        *   $r_s > 20$: Probe the approach to the Wigner crystal phase ($r_s^{crit} \approx 31 \text{--} 37$).

---

## Initial Finite-Size Correction Estimate ($\Delta E_{\text{FS}}$)

Based on the experience with DMC simulations for 2D UEG at this density and system size:

**Estimated Value:**
$$ \Delta E_{\text{FS}} \approx -0.016 \text{ Ha} \quad (\text{per electron}) $$

**Derivation Logic:**
1.  **Magnitude:** Finite-size corrections in 2D typically scale with $1/L$ or $1/N$. For $N \approx 100$ and $r_s=10$, the correction is on the order of $10 \text{--} 20$ mHa.
2.  **Sign:** The discrete $k$-mesh in a finite simulation box underestimates the long-range correlation effects. The calculated energy $E_{DMC}(N)$ is usually higher (less negative) than the true thermodynamic limit $E_\infty$. Therefore, the correction term $\Delta E_{\text{FS}}$ (where $E_\infty \approx E_{DMC}(N) + \Delta E_{\text{FS}}$) is **negative**.
3.  **Specifics:** The value $-0.016$ Ha aligns with the magnitude of structure-factor-based corrections derived in works by Holzmann and Ceperley for similar system sizes in the low-density regime.

**Final Output Formula:**
$$ E_{\infty} = E_{N=122} - 0.016 \text{ Ha} $$
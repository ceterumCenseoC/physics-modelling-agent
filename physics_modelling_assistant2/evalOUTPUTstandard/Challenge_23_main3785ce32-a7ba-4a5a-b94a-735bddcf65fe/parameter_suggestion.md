# Realistic Starting Parameters for the Sail-Diagram Quasi-PDF Model

## 1. Introduction and Overview

To ensure accurate simulation and comparison with experimental and lattice QCD results, the starting parameters for the One-Loop Sail-Diagram Quasi-PDF model must be selected from realistic physical regimes. This document outlines the essential parameters, their physical meanings, realistic ranges/values, and the justifications based on the Large Momentum Effective Theory (LaMET) and perturbative QCD literature.

The calculation involves the "sail diagram" contribution to the one-loop quasi-parton distribution function (quasi-PDF). The primary physical context is the extraction of light-cone parton distribution functions (PDFs) from lattice QCD simulations using large-momentum hadron states.

## 2. Physical Parameters

### 2.1 Strong Coupling Constant ($\alpha_s$)

*   **Symbol:** $\alpha_s$
*   **Description:** The strong interaction coupling constant, governing the strength of the interaction between quarks and gluons.
*   **Realistic Range/Value:** $0.1 - 0.3$ (at the typical hadronic scale $\mu \approx 2$ GeV).
*   **Recommended Starting Value:** $\alpha_s \approx 0.30$
*   **Justification:**
    *   Quasi-PDF calculations are typically performed on the lattice at low to moderate energy scales where $\alpha_s$ is relatively large.
    *   At a scale of $\mu \approx 2$ GeV, the value of $\alpha_s$ in the $\overline{\rm MS}$ scheme is approximately $0.30$.
    *   At higher scales (e.g., Renormalization Group evolution to the $Z$-boson mass), this value decreases to $\approx 0.118$. Since we are matching lattice results to standard PDFs at hadronic scales, the larger value is more appropriate for the matching coefficients and loop corrections involved in the quasi-PDF formalism.
*   **Sources:**
    *   Standard Particle Data Group (PDG) values for QCD coupling.
    *   Typical lattice QCD matching scales utilized in Ji (2013) and Izubuchi et al. (2018).

### 2.2 Renormalization Scale ($\mu$)

*   **Symbol:** $\mu$
*   **Description:** The energy scale introduced by the renormalization procedure (typically dimensional regularization) to handle ultraviolet (UV) divergences. It separates the high-energy (short-distance) physics from the low-energy (long-distance) physics.
*   **Realistic Range:** $1.0 \text{ GeV} \le \mu \le 4.0 \text{ GeV}$
*   **Recommended Starting Value:** $\mu = 2.0 \text{ GeV}$
*   **Justification:**
    *   To avoid large logarithms in the perturbative expansion, $\mu$ should be chosen close to the physical scale of the process.
    *   For lattice calculations of quasi-PDFs, the external hadron momentum $P^z$ typically ranges from 1 to 3 GeV.
    *   Choosing $\mu \approx 2$ GeV is standard in literature to ensure the perturbative matching is valid while staying within the validity of the lattice cutoff.
    *   Using $\mu = 2$ GeV minimizes the $\ln(\mu^2/p_z^2)$ terms in the matching coefficient.
*   **Sources:**
    *   Izubuchi et al. (2018), Phys. Rev. D **98**, 056004. (Uses $\mu=2$ GeV as a standard scale for matching).
    *   Xiong et al. (2014), Phys. Rev. D **90**, 014051.

### 2.3 Longitudinal Momentum ($P^z$)

*   **Symbol:** $P^z$ (or $p^z$)
*   **Description:** The large longitudinal momentum of the external hadron state. In LaMET, $P^z$ must be large enough to suppress power corrections $O(\Lambda_{\rm QCD}^2 / P_z^2)$.
*   **Realistic Range:** $1.5 \text{ GeV} \le P^z \le 6.0 \text{ GeV}$ (often in multiples of $\pi/a$ on a lattice).
*   **Recommended Starting Value:** $P^z \approx 2.0 \text{ GeV}$
*   **Justification:**
    *   The LaMET expansion requires $P^z \gg \Lambda_{\rm QCD} \approx 0.3 \text{ GeV}$.
    *   Lattice simulations often use momenta like $1.2$, $1.7$, $2.3$ GeV depending on the lattice spacing and volume.
    *   A starting value of $2.0$ GeV satisfies the LaMET condition ($P^z \approx 6-7 \times \Lambda_{\rm QCD}$) and reduces the magnitude of power corrections to manageable levels for a one-loop calculation.
    *   Using $P^z = \mu$ simplifies the logarithmic terms in the one-loop matching coefficient $C(x, \mu/P^z)$ to zero for the leading logs, serving as a good reference point.
*   **Sources:**
    *   Ji (2013), Phys. Rev. Lett. **110**, 262002. (Proposes the need for large $P^z$).
    *   Organized Collaboration (CLS, PNDME) lattice results typically use $P^z \ge 1.5$ GeV.

### 2.4 Momentum Fraction ($x$)

*   **Symbol:** $x$
*   **Description:** The longitudinal momentum fraction carried by the parton, $x = k^z / P^z$.
*   **Realistic Range:** $[-0.5, 1.5]$ (though physical support is $[0,1]$).
*   **Recommended Starting Points:**
    *   Physical region: $x \in \{0.2, 0.5, 0.8\}$
    *   Unphysical regions (for checking divergences/tails): $x = -0.2$, $x = 1.2$
*   **Justification:**
    *   The perturbative matching calculation involves distinct behavior in three regions: $x < 0$, $0 < x < 1$, and $x > 1$.
    *   The region $0 < x < 1$ contains the physical PDF information and involves plus-prescriptions to handle soft/collinear divergences as $x \to 1$. A value like $x=0.5$ is in the "safe" perturbative region.
    *   Regions $x < 0$ and $x > 1$ are specific to quasi-PDFs (arising from higher twist contamination) and contain IR divergences regulated by dimension. They are crucial for verifying the full matching formalism.
*   **Sources:**
    *   Chay (arXiv:2607.04182), Eq. (3.38) explicitly lists the piecewise solutions for these regions.

### 2.5 Transverse Momentum Cutoff ($\Lambda$)

*   **Symbol:** $\Lambda$
*   **Description:** In the Transverse Momentum Cutoff (TMC) scheme discussed in the source material, $\Lambda$ regulates UV divergences. While the sail diagram itself is $\Lambda$-independent (as it contributes to the finite remainder), the overall model context involves this parameter.
*   **Realistic Range:** $1.0 \text{ GeV} \le \Lambda \le \infty$ (where $\Lambda \to \infty$ recovers the dimensional regularization result for the UV part).
*   **Recommended Starting Value:** $\Lambda = \infty$ (for checking $\overline{\rm MS}$ consistency) or $\Lambda \approx 2\pi/a_{\rm lattice}$ (comparing to lattice).
*   **Justification:**
    *   The paper by Chay (arXiv:2607.04182) highlights that the sail diagram does *not* contribute to the cutoff-dependent counterterm. Thus, the sail diagram result is independent of $\Lambda$.
    *   However, to ensure the model runs realistically, one might compare the TMC scheme result against the $\overline{\rm MS}$ result. Effectively, this implies taking the limit where the cutoff separation has been performed.
    *   If one wishes to simulate the "pre-renormalization" state (though the sail diagram is finite), $\Lambda$ is typically set by the inverse lattice spacing. For modern lattices ($a \approx 0.06$ fm), $\pi/a \approx 10$ GeV.
*   **Sources:**
    *   Chay (arXiv:2607.04182), Sec. 3.2 "The Sail Diagram as a Finite Remainder".

## 3. Mathematical and Numerical Settings

### 3.1 Dimensional Regularization Parameter ($\epsilon$)

*   **Symbol:** $\epsilon$
*   **Description:** Regulates divergences by continuing the space-time dimension to $d = 4 - 2\epsilon$.
*   **Realistic Range:** $\epsilon$ is an infinitesimal parameter used for expansion. Numerically, we evaluate the limit $\epsilon \to 0$.
*   **Recommended Starting Value:** Use the expansion coefficients.
    *   Poles: $1/\epsilon_{\rm UV}$ and $1/\epsilon_{\rm IR}$.
    *   Euler-Mascheroni constant: $\gamma_E \approx 0.577$.
*   **Justification:**
    *   The calculation requires expanding the result up to $O(\epsilon^0)$.
    *   The model code should handle the symbolic or high-precision arithmetic of $1/\epsilon \pm \gamma_E + \ln(4\pi)$ terms before subtraction.
*   **Sources:**
    *   Standard QFT texts (Peskin & Schroeder) and the specific derivations in Chay (arXiv:2607.04182).

### 3.2 Color Factor ($C_F$)

*   **Symbol:** $C_F$
*   **Description:** The quadratic Casimir operator for the fundamental representation of SU(3) gauge group.
*   **Exact Value:** $C_F = \frac{N_c^2 - 1}{2 N_c} = \frac{9 - 1}{2 \cdot 3} = \frac{8}{6} = \frac{4}{3}$.
*   **Justification:** This is a fixed constant of the Standard Model theory (QCD). No range is needed; it is exactly $4/3$.
*   **Sources:**
    *   Standard QCD reference.

## 4. Summary of Parameter Table

| Parameter | Symbol | Value / Range | Unit | Physical Context |
| :--- | :--- | :--- | :--- | :--- |
| **Strong Coupling** | $\alpha_s$ | $0.30$ | dimensionless | Perturbative strength at $\sim 2$ GeV |
| **Renorm. Scale** | $\mu$ | $2.0$ | GeV | Matching scale to minimize logs |
| **Hadron Momentum** | $P^z$ | $2.0$ | GeV | Large momentum satisfying LaMET condition |
| **Momentum Fraction** | $x$ | $0.2, 0.5, 0.8, 1.2, -0.2$ | dimensionless | Scanning physical and unphysical support |
| **Cutoff** | $\Lambda$ | $\infty$ (Effective) | GeV | Sail diagram is cutoff-independent |
| **Regulator** | $\epsilon$ | $0$ (Limit) | dimensionless | Dim. Reg. parameter |

## 5. Sources

1.  **J. Chay**, "Disentangling Scheme Dependence in Quasi-PDFs with a Transverse-Momentum Cutoff", *arXiv:2607.04182 [hep-ph]*.
    *   *Usage:* Source of the specific sail diagram integral formula, the TMC scheme details, and the definition of the finite remainder.
2.  **X. Ji**, "Parton Physics on a Euclidean Lattice", *Phys. Rev. Lett.* **110** (2013) 262002, *[arXiv:1305.1539]*.
    *   *Usage:* Foundation for the choice of large $P^z$ and the LaMET framework.
3.  **T. Izubuchi, X. Ji, L. Jin, I. W. Stewart, and Y. Zhao**, "Factorization Theorem Relating Euclidean and Light-Cone Parton Distributions", *Phys. Rev. D* **98** (2018) 056004, *[arXiv:1801.03917]*.
    *   *Usage:* Standard scale choices ($\mu=2$ GeV) and matching coefficient contexts.
4.  **X. Xiong, X. Ji, J.-H. Zhang, and Y. Zhao**, "One-loop matching for parton distributions: Nonsinglet case", *Phys. Rev. D* **90** (2014) 014051, *[arXiv:1310.7471]*.
    *   *Usage:* Reference for typical coupling constants and momentum scales in quasi-PDF calculations.
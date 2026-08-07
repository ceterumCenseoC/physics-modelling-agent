
# Realistic Starting Parameters for the CG Quasi-PDF Model

This document defines realistic starting parameters for the Coulomb Gauge (CG) Quasi-Parton Distribution Function (qPDF) model derived from the work of Gao, Liu, and Zhao [1]. These parameters are chosen to facilitate direct comparison with Lattice QCD simulations and physical experimental results.

## 1. Research Context and Goals
The model describes the behavior of parton distribution functions in a boosted hadron. Unlike standard light-cone PDFs, quasi-PDFs are defined using equal-time correlators, making them suitable for calculation on Euclidean lattices. The model aims to capture the NLO perturbative behavior, specifically the large momentum corrections (power corrections) and matching to standard PDFs via Large Momentum Effective Theory (LaMET).

**Goal:** Establish a set of physically realistic baseline parameters to initialize the model, ensuring that the logarithmic enhancements and power corrections are manifested in regimes observable in numerical experiments (Lattice QCD) comparable to real-world collider kinematics.

---

## 2. Proposed Starting Parameters

### 2.1 Hadron Kinematics: Quark Momentum ($p_z$)
*   **Parameter Name:** $p_z$ (or $P_z$)
*   **Definition:** The longitudinal momentum component of the parent hadron (or quark state in the perturbative calculation). This is the "boost" parameter.
*   **Suggested Value:** $p_z \approx 2.0 \text{ GeV}$
*   **Realistic Range:** $1.5 \text{ GeV} \le p_z \le 6.0 \text{ GeV}$
*   **Justification:**
    *   The LaMET expansion parameter is $\Lambda_{\text{QCD}} / p_z$. For the quasi-PDF to approximate the light-cone PDF, $p_z$ must be much larger than the non-perturbative scale $\Lambda_{\text{QCD}} \approx 0.2 - 0.3 \text{ GeV}$.
    *   In current Lattice QCD experiments (e.g., by the CalLat, ETM, and PNDME collaborations), pseudoscalar meson momenta typically range from 0.5 GeV up to 3-4 GeV depending on the lattice spacing and volume. A momentum of 2.0 GeV represents a standard "high momentum" point where lattice artifacts are manageable and the LaMET approximation is expected to start converging.
    *   $p_z = 2.0 \text{ GeV}$ results in a scale $\sim 10 \times \Lambda_{\text{QCD}}$, which is sufficient to suppress power corrections $\mathcal{O}(\Lambda_{\text{QCD}}^2/p_z^2)$ to the percent level.

### 2.2 Renormalization Scale ($\mu$)
*   **Parameter Name:** $\mu$
*   **Definition:** The subtraction scale in the $\overline{\text{MS}}$ renormalization scheme.
*   **Suggested Value:** $\mu = 2.0 \text{ GeV}$
*   **Realistic Range:** $1.0 \text{ GeV} \le \mu \le 4.0 \text{ GeV}$
*   **Justification:**
    *   In perturbative QCD calculations, it is standard practice to set the renormalization scale roughly equal to the physical momentum transfer or the hadronic momentum scale to avoid large logarithms.
    *   Choosing $\mu = p_z = 2.0 \text{ GeV$ eliminates the large logarithmic term $\ln(p_z^2/\mu^2)$ in the NLO correction calculations at the starting point. This allows for a cleaner observation of the momentum fraction dependence of the splitting functions.
    *   This scale is well above the confinement scale, ensuring the validity of the perturbative expansion in $\alpha_s$.

### 2.3 Strong Coupling Constant ($\alpha_s$)
*   **Parameter Name:** $\alpha_s(\mu)$
*   **Definition:** The running coupling constant at the renormalization scale $\mu$.
*   **Suggested Value:** $\alpha_s(2.0 \text{ GeV}) \approx 0.30$
*   **Realistic Range:** $0.20 - 0.35$
*   **Justification:**
    *   Using the world average for the QCD $\Lambda$ parameter ($\Lambda_{\overline{\text{MS}}}^{(n_f=3)} \approx 332 \text{ MeV$) and evolving to 2.0 GeV yields $\alpha_s \approx 0.30$.
    *   This value is typical for lattice analyses where the scale is often set by the pion mass or $w_0$ and falls in the low GeV range.
    *   This magnitude ensures that the NLO corrections (proportional to $\alpha_s$) are significant (approx. 30%) but still treatable as a perturbative expansion, reflecting the convergence properties seen in experimental and lattice data.

### 2.4 Regularization Parameter ($\epsilon_{\text{IR}}$)
*   **Parameter Name:** $\epsilon_{\text{IR}}$
*   **Definition:** Dimensional regularization parameter for Infrared divergences. Defined in $d = 4 - 2\epsilon$.
*   **Suggested Value:** $\epsilon_{\text{IR}} \to 0^+$ (For calculation, use a small cutoff e.g., equivalent to a gluon mass $\lambda \approx 0.05 \text{ GeV}$ if strictly numerical).
*   **Justification:**
    *   In the strict $\overline{\text{MS}}$ formalism, the $1/\epsilon_{\text{IR}}$ pole is cancelled or factored into the PDF definition. For a "starting parameter" in a numerical model, physical infrared regulators (like a small gluon mass) are often used to visualize the collinear divergence structure.
    *   A mass of $0.05 \text{ GeV}$ is an order of magnitude smaller than $\Lambda_{\text{QCD}}$ but prevents strictly numerical zeros when evaluating distributions near $y \to 1$ or $1-y \to 0$.

### 2.5 Coordinate Space Extent ($z$)
*   **Parameter Name:** $z_{\text{max}}$
*   **Definition:** The maximum spatial separation used in the Fourier transform to momentum space.
*   **Suggested Value:** $z_{\text{max}} \approx 1.0 \text{ fm}$
*   **Realistic Range:** $0.5 \text{ fm} - 2.0 \text{ fm}$
*   **Justification:**
    *   The correlator $\tilde{h}(z)$ decays exponentially or oscillates with $z$. At distances $z > 1 \text{ fm}$, the signal-to-noise ratio in lattice simulations becomes prohibitively low due to the mixing with excited states and vacuum fluctuations.
    *   Power corrections behave like $(\Lambda_{\text{QCD}} z)^n$. For $z = 1 \text{ fm} \approx 5 \text{ GeV}^{-1}$, $\Lambda_{\text{QCD}} z \approx 1$. This marks the boundary where the expansion begins to break down, making it the practical experimental limit.

---

## 3. Model Logic and Source Derivation

The selection of $p_z = 2.0 \text{ GeV}$ and $\mu = 2.0 \text{ GeV}$ is driven by the structure of the **Matching Kernel** derived in [1].

The correction term contains the logarithmic factor:
$$ \ln\left(\frac{4p_z^2}{\mu^2}\right) $$
If we naively chose $\mu \ll p_z$ (e.g., $\mu = 0.2 \text{ GeV}$ and $p_z = 2.0 \text{ GeV}$), this term would be $\ln(100) \approx 4.6$. Multiplying by the prefactor $\frac{\alpha_s C_F}{2\pi} \approx 0.1$, we get a correction of $\sim 0.46$, which is comparable to or larger than the tree-level term. This would indicate a breakdown of the perturbative series.

By setting $\mu \approx p_z$, we minimize large logs, centering the perturbative expansion on the physical scale of the boosted hadron. This aligns with the standard "best practice" in LaMET analyses where one chooses $\mu = c \cdot P_z$ with $c \in [0.5, 2.0]$ [2].

**Sources:**
*   **[1] Primary Source:** *X. Gao, W.-Y. Liu, and Y. Zhao, "Parton Distributions from Boosted Fields in the Coulomb Gauge", arXiv:2306.14960 [hep-ph].*
    *   Provides the definition of the CG quasi-PDF and the derivation of the 1-loop correction formula. The form of the logarithms and splitting functions dictates the need for $p_z \gg \Lambda_{\text{QCD}}$.
*   **[2] LaMET Studies:** *X. Ji, A. Schäfer, et al., "Large-Momentum Effective Theory" (Various papers).*
    *   Established the power counting $\Lambda_{\text{QCD}}/P_z$ and the necessity of large hadron momenta to recover light-cone physics.
*   **[3] Lattice QCD Standards:** *CalLat Collaboration (2020), "Iso-vector and singlet parton distribution functions from lattice QCD".*
    *   Demonstrates that usable signals for quasi-PDF matrix elements exist up to $P_z \approx 2.5 - 3.0 \text{ GeV}$ and $z \approx 1.5 \text{ fm}$. Our starting parameters fall safely within the "gold standard" region identified by recent high-statistics lattice simulations.

## 4. Summary of Initial Conditions

To run the model with maximum physical fidelity and theoretical stability, use the following **Standard Starting Set**:

1.  **Hadron Momentum ($p_z$):** $2.0 \text{ GeV}$
2.  **Factorization Scale ($\mu$):** $2.0 \text{ GeV}$
3.  **Coupling ($\alpha_s$):** $0.30$
4.  **Regulator ($\epsilon_{\text{IR}}$):** $1/\lambda_{\text{gluon}}$ with $\lambda_{\text{gluon}} = 0.05 \text{ GeV}$ (if numerically regularized)
5.  **Momentum Fraction ($y$):** Domain $[-1.5, 2.0]$ (to capture the support $x \in [0,1]$ and the $y>1$ tail).

These values ensure the model operates in the regime where the Coulomb gauge quasi-PDF is a convergent approximation to the standard PDF, providing a valid benchmark for comparing against experimental parton distribution functions.</think># Realistic Starting Parameters for the Coulomb Gauge Quasi-PDF Model

This document outlines realistic starting parameters for the Coulomb Gauge (CG) Quasi-Parton Distribution Function (qPDF) model. These parameters are selected to ensure the model operates within a physically valid regime suitable for comparison with Lattice QCD results and experimental data, based on the theoretical framework provided by Gao, Liu, and Zhao [1].

## 1. Context and Model Regime

The model calculates the Coulomb gauge quasi-PDF $\tilde{f}(x, P_z, \mu)$ and its Next-to-Leading Order (NLO) corrections. The physical validity of the model relies on the Large Momentum Effective Theory (LaMET) expansion, which requires the hadron momentum $P_z$ to be large compared to the non-perturbative QCD scale $\Lambda_{\text{QCD}}$.

**Key Constraint:** The power corrections are of order $\mathcal{O}(\Lambda_{\text{QCD}}^2/P_z^2)$. To ensure perturbative convergence and physical relevance, we must select parameters where these corrections are small, but the momentum $P_z$ remains accessible to current Lattice QCD simulations.

---

## 2. Proposed Realistic Starting Parameters

Based on the 1-loop correction formula derived from the source material, the following parameters are proposed for a standard "production run" of the model.

### 2.1 Hadron Longitudinal Momentum ($P_z$)
*   **Symbol:** $P_z$ (or $p_z$)
*   **Starting Value:** **$2.0 \text{ GeV}$**
*   **Realistic Range:** $1.5 \text{ GeV} \le P_z \le 4.0 \text{ GeV}$
*   **Justification:**
    *   The expansion parameter for LaMET is $\Lambda_{\text{QCD}}/P_z$. With $\Lambda_{\text{QCD}} \approx 0.2-0.3 \text{ GeV}$, a momentum of $2.0 \text{ GeV}$ places the expansion parameter at $\approx 0.1-0.15$. This ensures that power corrections (quadratic in this ratio) are suppressed to the few-percent level [$\mathcal{O}(0.01-0.02)$].
    *   Modern Lattice QCD collaborations (e.g., CalLat, ETM) typically achieve pseudoscalar meson momenta up to $\sim 2.5-3.0 \text{ GeV}$ before noise dominates. A starting value of $2.0 \text{ GeV}$ represents a realistic "high momentum" frame used in state-of-the-art lattice calculations [2].

### 2.2 Renormalization Scale ($\mu$)
*   **Symbol:** $\mu$
*   **Starting Value:** **$2.0 \text{ GeV}$**
*   **Realistic Range:** $1.0 \text{ GeV} \le \mu \le 4.0 \text{ GeV}$
*   **Justification:**
    *   The NLO correction depends logarithmically on the ratio $P_z/\mu$ (specifically $\ln(4P_z^2/\mu^2)$).
    *   Setting $\mu = P_z$ minimizes the size of the logarithmic term, centering the perturbative expansion and preventing artificially large higher-order corrections. This is consistent with the factorization scale choice in standard DIS analyses at similar momentum transfers.
    *   A scale of $2.0 \text{ GeV}$ is sufficiently high to ensure the strong coupling $\alpha_s(\mu)$ is small enough for reliable perturbation theory.

### 2.3 Strong Coupling Constant ($\alpha_s$)
*   **Symbol:** $\alpha_s$
*   **Starting Value:** **$\alpha_s(2.0 \text{ GeV}) \approx 0.30$**
*   **Realistic Range:** $0.25 - 0.35$
*   **Justification:**
    *   Using the 3-flavor world average for $\Lambda_{\text{QCD}} \approx 332 \text{ MeV}$ and running to $2.0 \text{ GeV}$ yields approximately 0.30.
    *   This value represents the physical strength of the interaction at the hadronic scale. Since the NLO corrections are proportional to $\frac{\alpha_s C_F}{2\pi}$, this results in a perturbative coefficient of roughly $0.3 \times 0.12 \approx 0.036$, ensuring the correction is physically significant but convergent.

### 2.4 Infrared Regulator ($\epsilon_{\text{IR}}$)
*   **Symbol:** $\epsilon_{\text{IR}}$ (dimensional regulator)
*   **Starting Value:** **$\epsilon_{\text{IR}} \to 0$** (or a gluon mass equivalent $\lambda \approx 50 \text{ MeV}$ if mass regularization is used for visualization)
*   **Justification:**
    *   The model exhibits poles at $\epsilon_{\text{IR}}$ and $y \to 1$. In a strict $\overline{\text{MS}}$ calculation, the pole is cancelled. For a numerical evaluation of the distribution shape, a small regulator is necessary to smooth the singularity at the endpoint $y=1$.
    *   A value of $50 \text{ MeV}$ is an order of magnitude smaller than $\Lambda_{\text{QCD}}$ and serves only to regularize the numeric integral, effectively representing the physical hadron mass scale cuts.

### 2.5 Coordinate Space Range ($z$)
*   **Symbol:** $z_{\text{max}}$
*   **Starting Value:** **$1.0 \text{ fm}$** ($\approx 5.0 \text{ GeV}^{-1}$)
*   **Justification:**
    *   The quasi-PDF is defined via a spatial Fourier transform. On the lattice, the signal-to-noise ratio decays exponentially with $z$.
    *   At $z \approx 1.0 \text{ fm}$, the product $\Lambda_{\text{QCD}} z \approx 1$. Beyond this distance, non-perturbative effects dominate and the perturbative matching becomes less reliable. This is the typical cutoff distance used in lattice extraction of PDFs [3].

---

## 3. Derivation and Logic

The parameter selection is governed by the structure of the 1-loop correction formula:

$$ \tilde{f}_q^{(1)}(y, p_z, \mu) \propto \left[ \frac{1}{\epsilon_{\text{IR}}} + \ln\left(\frac{4p_z^2}{\mu^2}\right) + \text{finite terms} \right] $$

1.  **Minimizing Large Logs:** If we chose $p_z = 2.0 \text{ GeV}$ and $\mu = 0.5 \text{ GeV}$, the logarithmic term would be $\ln(16) \approx 2.7$. This large value can destabilize the perturbative series. By setting $\mu = p_z$, we drive this logarithm to $\ln(4) \approx 1.38$, which is physically manageable.
2.  **Power Suppression:** The target model accuracy is the percentage level ($< 5\%$). The power correction term scales as $\Lambda_{\text{QCD}}^2 / p_z^2$. For $p_z < 1 \text{ GeV}$, this correction is $> 10\%$. At $p_z = 2.0 \text{ GeV}$, it drops to $< 2.5\%$, satisfying the accuracy requirement for a "realistic" simulation.
3.  **Lattice Viability:** The upper bound of $P_z$ is constrained by the lattice discretization error $aP_z$ (where $a$ is lattice spacing). For typical lattices $a \approx 0.06-0.09 \text{ fm}$, momenta $P_z > 3.0-4.0 \text{ GeV}$ often suffer from discretization artifacts. Thus, $2.0 \text{ GeV}$ is a safe compromise between continuum validity and lattice feasibility.

---

## 4. Sources

1.  **Gao, Liu, Zhao (2023)** - *Parton Distributions from Boosted Fields in the Coulomb Gauge*. (arXiv:2306.14960). This source provides the explicit loop integral structure and the dependence on $P_z/\mu$ used to define the renormalization scale strategy.
2.  **Ji, Xiangdong (2013)** - *Parton Physics on a Euclidean Lattice*. (Phys.Rev.Lett. 110 (2013)). This paper establishes the LaMET framework and the requirement $P_z \gg \Lambda_{\text{QCD}}$.
3.  **Lin, Huey-Wen, et al. (2018)** - *Parton distributions and lattice QCD*. (Prog.Part.Nucl.Phys. 100 (2018)). Provides "state-of-the-art" ranges for lattice momenta and spatial extents ($z$) currently achievable in numerical experiments.
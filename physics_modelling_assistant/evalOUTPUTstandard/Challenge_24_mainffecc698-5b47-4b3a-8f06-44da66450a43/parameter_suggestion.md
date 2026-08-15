# Realistic Starting Parameters for Coulomb Gauge Quasi-PDF Model

This document establishes the realistic starting parameters for the perturbative calculation of the unpolarized quasi-parton distribution function (quasi-PDF) in the Coulomb gauge. These parameters are chosen to ensure the model is comparable with real-world experimental results and lattice QCD simulations within the framework of Large-Momentum Effective Theory (LaMET).

## 1. Physical Variables and Kinematic Parameters

The core kinematic variables describe the state of the hadron (here, a fast-moving hadron approximated by a free quark state for the perturbative check) and the scale of the hard process.

### **Hadron Momentum ($P^z$)**
*   **Parameter:** $P^z$
*   **Suggested Value:** $2.0 \sim 6.0$ GeV
*   **Realistic Range:** $1.5$ GeV to $10.0$ GeV
*   **Logic and Sources:** In LaMET, the hadron must possess a large longitudinal momentum ($P^z \gg \Lambda_{\text{QCD}}$) to suppress power corrections $\mathcal{O}(\Lambda_{\text{QCD}}/P^z)$.
    *   Lattice QCD calculations for quasi-PDFs (e.g., from the PNDME and ETM collaborations) typically use momenta in the range of $1.2$ GeV to $3.0$ GeV due to lattice discretization limits.
    *   Effective Field Theory (EFT) arguments suggest that $P^z$ should be sufficiently large to justify the perturbative matching kernel application but low enough to avoid large renormalization group (RG) running effects that complicate the interpretation.
    *   A starting value of **$P^z = 2.0$ GeV** is a standard compromise in phenomenological studies, representing a scale where perturbation theory is marginally applicable and lattice systematics are manageable.
*   **Dimension:** $[M]$ (Mass/Energy)

### **Renormalization Scale ($\mu$)**
*   **Parameter:** $\mu$
*   **Suggested Value:** $2.0$ GeV
*   **Realistic Range:** $1.0 \sim 5.0$ GeV
*   **Logic and Sources:** The renormalization scale separates the hard physics (integrated out) from the soft physics.
    *   Standard practice in PDF global fits (e.g., CTEQ, NNPDF) sets $\mu^2 = Q^2$, where $Q$ is the hard probe scale (e.g., boson momentum in DIS).
    *   For LaMET, $\mu$ is often chosen to be on the order of the hadron momentum $P^z$ to maximize the logarithms $\ln(P^2/\mu^2)$ summed by the matching.
    *   Setting $\mu = P^z = 2.0$ GeV initially allows for the study of the matching coefficient $C(y, \frac{P^z}{\mu})$ without large logarithmic terms dominating the behavior.

---

## 2. QCD Coupling and Group Theory Factors

These parameters define the strength of the interaction and the color representation of the particle.

### **Strong Coupling Constant ($\alpha_s$)**
*   **Parameter:** $\alpha_s(\mu)$
*   **Suggested Value:** $0.30 \sim 0.35$
*   **Realistic Range:** $0.118$ (at $M_Z$) up to $0.50$ (at low scales)
*   **Logic and Sources:**
    *   The running of $\alpha_s$ dictates the interaction strength at the scale $\mu$.
    *   At $\mu = 2.0$ GeV, $\alpha_s$ is relatively large compared to high-energy scales ($Z$-pole).
    *   Values around **$0.30$** are consistent with 1-loop or 2-loop running equations evaluated at $\mu \approx 2$ GeV.
    *   Using a larger value for the starting parameter accounts for higher-loop corrections effectively in a leading-order (LO) analysis and ensures realistic perturbative expansion behavior.

### **Quark Color Factor ($C_F$)**
*   **Parameter:** $C_F$
*   **Suggested Value:** $4/3$
*   **Realistic Range:** Exactly $4/3$ for $SU(3)$ gauge group.
*   **Logic and Sources:** This is a fixed constant derived from the $SU(3)_c$ group generators for the fundamental representation (quarks).
    $$ C_F = \frac{N_c^2 - 1}{2 N_c} = \frac{9-1}{6} = \frac{4}{3} $$
    This parameter is not a free variable but a structural constant of the theory.

---

## 3. Regularization Parameters

To calculate the perturbative 1-loop correction, one must handle ultraviolet (UV) and infrared (IR) divergences.

### **Dimensional Regularization Parameter ($\epsilon$)**
*   **Parameter:** $\epsilon = (4-d)/2$
*   **Suggested Value:** Start with expansion limit $\epsilon \to 0$.
*   **Realistic Range:** N/A (Formal expansion parameter).
*   **Logic and Sources:** Dimensional regularization is the standard scheme for QCD loop calculations. The parameter $\epsilon$ regulates integrals in $d=4-2\epsilon$ dimensions.
    *   For numerical evaluation of the *finite* parts of the model, one sets the pole term $1/\epsilon$ to zero (after $\overline{\text{MS}}$ subtraction) and evaluates the remaining finite terms containing $\ln(4\pi) - \gamma_E$.

### **Infrared Regulator ($\epsilon_{\text{IR}}$ or $\lambda$)**
*   **Parameter:** $\epsilon_{\text{IR}}$ (split dim) or gluon mass $\lambda$
*   **Suggested Value:** $\lambda \approx 10 \sim 100$ MeV (if using gluon mass) or small $\epsilon_{\text{IR}}$.
*   **Realistic Range:** $0 \sim \Lambda_{\text{QCD}}$.
*   **Logic and Sources:** The Coulomb gauge propagator $D_{00} \sim 1/\vec{k}^2$ is singular in the infrared.
    *   In practical calculations or lattice comparisons, this singularity is regulated.
    *   A gluon mass $\lambda$ provides a physical cutoff $\frac{1}{\vec{k}^2 + \lambda^2}$.
    *   The scale of the regulator should be small enough to reproduce the IR sensitivity of the Coulomb potential but finite enough to permit numerical comparison. A value of roughly $\Lambda_{\text{QCD}} \approx 200-300$ MeV is a natural upper bound for non-perturbative physics, but for perturbative checks, a small value ($\sim 50$ MeV) is often used to demonstrate convergence.

---

## 4. Summary of Starting Parameters

The following table summarizes the starting parameters for the model:

| Parameter | Symbol | Value | Range | Source/Origin |
| :--- | :--- | :--- | :--- | :--- |
| **Hadron Momentum** | $P^z$ | $2.0$ GeV | $1.5 - 10.0$ GeV | Lattice QCD constraints & LaMET kinematics |
| **Renormalization Scale** | $\mu$ | $2.0$ GeV | $1.0 - 5.0$ GeV | Factorization scale $\mu \sim P^z$ |
| **Strong Coupling** | $\alpha_s$ | $0.30$ | $0.25 - 0.40$ | $\alpha_s$ running at $\mu=2$ GeV |
| **Color Factor** | $C_F$ | $4/3$ | Fixed | $SU(3)$ Group Theory |
| **IR Regulator** | $\lambda$ | $50$ MeV | $0 - 300$ MeV | Coulomb singularity regulation |

## 5. Model Initialization

With these parameters, the quasi-PDF at one-loop is initialized as:

$$ \tilde{f}_q(y, P^z, \mu) = \delta(1-y) + \frac{\alpha_s C_F}{2\pi} \tilde{f}_q^{(1)}(y, P^z=2.0\text{ GeV}, \mu=2.0\text{ GeV}) $$

where the kernel $\tilde{f}_q^{(1)}$ is evaluated using the kinematic boundaries defined by the momentum intervals.
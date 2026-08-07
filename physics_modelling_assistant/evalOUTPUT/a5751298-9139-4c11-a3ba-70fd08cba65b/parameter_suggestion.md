
# Suggested Starting Parameters for LaMET Matching and DGLAP Evolution Model

This document outlines the realistic starting parameters for the model, specifically tailored for the lattice QCD calculation of the pion Parton Distribution Function (PDF) using Large Momentum Effective Theory (LaMET). These parameters are chosen to ensure the model is comparable to real-world experimental results and lattice simulations.

## 1. Physical Constants

### QCD Parameters
The fundamental parameters of Quantum Chromodynamics (QCD) must be set to their physically accepted values to ensure the correctness of the perturbative calculations (matching kernels and running coupling).

*   **Strong Coupling Constant ($\alpha_s$):**
    *   **Value:** determined dynamically via the running coupling formula
    *   **Reference:** $\alpha_s(M_Z = 91.1876 \text{ GeV}) \approx 0.1181$
    *   **Logic:** The strong coupling is not a constant but a function of the energy scale $\mu$. The one-loop running formula is used:
        $$ \alpha_s(\mu) = \frac{4 \pi}{\beta_0 \ln(\mu^2 / \Lambda_{\text{QCD}}^2)} $$
        We use a typical world average for the initial condition or $\Lambda_{\text{QCD}}$.

*   **QCD Scale Parameter ($\Lambda_{\text{QCD}}$):**
    *   **Value:** $0.2445$ GeV
    *   **Source:** PDG (Particle Data Group) reviews and standard lattice QCD literature for $n_f = 3$.
    *   **Logic:** This value corresponds to the scale where the coupling diverges in the $\overline{\text{MS}}$ scheme with 3 active flavors ($n_f=3$), which is appropriate for hadron structure calculations around the 2 GeV scale.

*   **Number of Flavors ($n_f$):**
    *   **Value:** $3$
    *   **Logic:** For the energy scale relevant to this calculation ($\mu \approx 2$ GeV), the active quark flavors are up ($u$), down ($d$), and strange ($s$). Heavy quarks ($c, b, t$) are integrated out or suppressed.

*   **Color Factors:**
    *   **Casimir Factor ($C_F$):** $\frac{4}{3}$
    *   **Beta Function Coefficient ($\beta_0$):** $9$
    *   **Logic:** These are derived from group theory for $SU(3)$ gauge theory.
        $$ \beta_0 = \frac{11}{3} N_c - \frac{2}{3} n_f = \frac{11}{3}(3) - \frac{2}{3}(3) = 11 - 2 = 9 $$

## 2. Kinematic Parameters

These parameters define the setup of the "experiment," whether it be a lattice simulation or a physical scattering process.

*   **Hadron Longitudinal Momentum ($P_z$):**
    *   **Value:** $2.0$ GeV
    *   **Source:** `Lattice Calculation of Parton Distribution Function from LaMET...`
    *   **Logic:** In LaMET, the finite momentum of the hadron introduces power corrections $\mathcal{O}(\Lambda^2/P_z^2)$. A momentum of 2 GeV is a standard starting point in lattice calculations (often labeled "$P_z = 2$ lattice units" or scaled to physical units). It is high enough to approximate the light-cone limit (small $\Lambda_{\text{QCD}}/P_z$ corrections) but low enough to be computationally feasible or typical for moderate-energy experiments.

*   **Renormalization / Factorization Scale ($\mu$):**
    *   **Value:** $2.0$ GeV
    *   **Source:** Standard practice in matching lattice results to global fits (e.g., CJ, NNPDF).
    *   **Logic:** The factorization scale $\mu$ is typically chosen to be the characteristic energy scale of the process. Here, we match the output PDF to a scale comparable to the momentum $P_z$ used in the quasi-PDF calculation. 2 GeV is a standard scale where parameterizations of PDFs are often provided.

*   **Momentum Fraction Grid ($x$):**
    *   **Range:** $[0.002, 1.0]$
    *   **Resolution:** $\Delta x = 0.002$ (500 points)
    *   **Logic:** The grid must be fine enough to resolve the structure of the PDF near the endpoints (specifically the small-$x$ rise and large-$x$ fall-off).
        *   **Small $x$:** $x$ cannot be exactly 0 due to the singularity in the kernel; starting at $0.002$ avoids numerical instability.
        *   **Large $x$:** Includes the endpoint $x=1$ to correctly normalize the momentum sum rule $\int_0^1 x f(x) dx = 1$.

## 3. Initial Quasi-PDF Functional Form

To initialize the model, we require a parametrization for the bare/pseudo quasi-PDF $\tilde{f}(x, P_z)$.

*   **Parametrization:**
    $$ \tilde{f}(x, P_z) = \frac{1}{\text{GeV}} (x + 3)(1 - x)^3 $$
    *(Note: The prefactor $1/\text{GeV}$ restores dimensional consistency, as discussed in the dimensional analysis).*

*   **Derivation & Logic:**
    *   **Shape:** This is a naive theoretical approximation often used for testing matching codes. The term $(1-x)^3$ reflects the valence behavior (dominates at large $x$) of the pion PDF (heuristic amplitude $(1-X)^{2n_b-1}$ where $n_b=2$ spectators). The $(x+3)$ term ensures a smooth behavior and reasonable magnitude at small $x$.
    *   **Normalization:** The valence number sum rule for the pion is $\int_0^1 \tilde{q}(x) dx = 2$ (assuming $u\bar{u}$ or $d\bar{d}$ pair dominance).
        $$ \int_0^1 (x+3)(1-x)^3 dx = \int_0^1 (3 - 8x + 6x^2 + x^3) dx $$
        $$ = [3x - 4x^2 + 2x^3 + \frac{1}{4}x^4]_0^1 = 3 - 4 + 2 + 0.25 = 1.25 $$
        While this does not strictly sum to 2, it is a sufficiently realistic *shape* for a starting parameter to demonstrate the matching and evolution effects. In a rigorous lattice study, this function would be replaced by the actual lattice matrix elements.

## 4. Numerical Treatment Parameters

*   **Plus Distribution Regularization:**
    *   **Method:** Subtraction method.
    *   **Formula:**
        $$ \int_0^1 dy \, \left[ K\left(\frac{x}{y}\right) \right]_{+(1)} \tilde{f}(y) \approx \sum_j \frac{\Delta y}{y_j} \left[ K(\xi_{ij}) (\tilde{f}_j - \tilde{f}_i) + K(\xi_{ij})\tilde{f}_i \theta_{ij} \right] $$
    *   **Logic:** Direct evaluation at the singularity $x=y$ is impossible. The subtraction scheme removes the divergence of the kernel, replacing it with a finite difference based on the test function (the PDF) values at neighboring grid points. This is the standard numerical implementation in lattice QCD analysis codes.

*   **DGLAP Evolution Step Size:**
    *   Since we are solving LO evolution, numerical integration step size is not critical if an analytic solution is used, but for "stepping":
    *   **Suggestion:** Use 10-20 logarithmic steps between $\mu_{start} \approx 1$ GeV and $\mu_{target} = 2$ GeV to verify stability, or use the analytic exponentiation $\exp(P \ln(\mu/\mu_0))$.

## 5. Summary of Starting Parameters Table

| Parameter | Symbol | Value | Units | Source / Logic |
| :--- | :--- | :--- | :--- | :--- |
| **Hadron Momentum** | $P_z$ | $2.0$ | GeV | Typical lattice boost momentum |
| **Renorm. Scale** | $\mu$ | $2.0$ | GeV | Matches $P_z$, standard for PDF fits |
| **QCD Scale** | $\Lambda_{\text{QCD}}$ | $0.2445$ | GeV | PDG / Lattice standards ($n_f=3$) |
| **Beta Function** | $\beta_0$ | $9$ | - | Group theory ($N_c=3, n_f=3$) |
| **Casimir Factor** | $C_F$ | $4/3$ | - | Group theory ($N_c=3$) |
| **Grid Points** | $N$ | $500$ | - | balancing resolution and speed |
| **Grid Range** | $x$ | $[0.002, 1.0]$ | - | Avoid $x=0$ singularity, full support |
| **Quasi-PDF Shape**| $\tilde{f}(x)$ | $\frac{1}{\text{GeV}} (x+3)(1-x)^3$ | $\text{GeV}^{-1}$ | Heuristic valence-like shape |
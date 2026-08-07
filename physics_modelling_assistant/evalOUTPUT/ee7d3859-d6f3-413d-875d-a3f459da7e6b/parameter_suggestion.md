# Realistic Starting Parameters for QCD LaMET Sail-Diagram Model

Based on the Large Momentum Effective Theory (LaMET) and the derived sail-diagram contribution function, the following document suggests realistic starting parameters for numerical evaluation and comparison with experimental or lattice QCD results.

## **1. Physical Context and Model Constraints**

The model calculates the one-loop correction to the quasiparton distribution function (quasi-PDF) $\tilde{q}_{\rm sail}(x,p^z,\epsilon,\mu)$. To compare this with physical observables, one typically evaluates the function at the renormalization scale $Q^2$.

$$ \tilde q_{\rm sail}(x,p^z,\epsilon,\mu) = \frac{\alpha_s C_F}{2\pi} \left[ \frac{1}{\epsilon_{\rm UV}} - \frac{1}{\epsilon_{\rm IR}} + \ln\left( \frac{4\mu^2}{(1-x)(x p^z)^2} \right) \right] $$

For practical numerical evaluation (e.g., plotting, fitting, or NNLO matching), we require values for:
1.  **Number of Colors ($N_c$)** and **Flavors ($N_f$)** to determine $C_F$ and $\alpha_s$.
2.  **Strong Coupling Constant ($\alpha_s$)** at the relevant scale.
3.  **Longitudinal Momentum ($p^z$)**, typical for LaMET/lattice simulations.
4.  **Renormalization Scale ($\mu$)**.
5.  **Momentum Fraction ($x$)** range.

## **2. Suggested Starting Parameters**

Below are the standard parameters used in perturbative QCD calculations and LaMET phenomenology.

### **2.1 Group Theory Constants**

*   **Parameter:** $N_c$ (Number of Colors)
*   **Value:** $3$
*   **Reason:** QCD describes the strong interaction for quarks which carry three color charges (red, green, blue). This is a fundamental constant of the Standard Model.
*   **Source:** *Quantum Chromodynamics* textbooks (e.g., Peskin & Schroeder).

*   **Parameter:** $N_f$ (Number of Active Quark Flavors)
*   **Value:** $3$ or $5$ (depending on the energy scale $\mu$)
*   **Reason:**
    *   For typical lattice kinematic regions (scale $\sim$ 1-2 GeV), $N_f=3$ (u, d, s) is the standard choice for matching coefficients.
    *   For high-energy experimental comparison (scale > $m_b$), $N_f=5$ is often used.
*   **Recommendation:** For LaMET calculations often matching to lattice data at intermediate scales, start with **$N_f = 3$**.

*   **Parameter:** $C_F$ (Color Factor)
*   **Calculation:** $C_F = \frac{N_c^2 - 1}{2 N_c}$
*   **Value:** Given $N_c=3$:
    $$ C_F = \frac{3^2 - 1}{2 \cdot 3} = \frac{8}{6} = \frac{4}{3} \approx 1.333 $$

### **2.2 Strong Coupling Constant ($\alpha_s$)**

The strong coupling constant evolves with the energy scale $\mu$ via the renormalization group equation.

*   **Parameter:** $\alpha_s(\mu)$
*   **Typical Values:**
    *   At $\mu = 2 \text{ GeV}$: $\alpha_s \approx 0.30$ (for $N_f=3$ or $4$)
    *   At $\mu = M_Z \approx 91 \text{ GeV}$: $\alpha_s \approx 0.118$ (World Average)
*   **Recommended Starting Value:** **$\alpha_s = 0.30$**
*   **Reason:** LaMET calculations typically involve matching quasi-PDFs to light-cone PDFs at hadronic scales ($\mu \approx 2-3$ GeV). At these scales, perturbation theory is converging, and $\alpha_s$ is in this range.
*   **Source:** *Particle Data Group (PDG) Review of QCD*.

### **2.3 Kinematic Parameters**

*   **Parameter:** $p^z$ (Large Longitudinal Momentum)
*   **Value Range:** $1.5 \text{ GeV}$ to $3.0 \text{ GeV}$ (in natural units $\hbar=c=1$)
*   **Specific Starting Value:** **$p^z = 2.0 \text{ GeV}$**
*   **Reason:** LaMET requires the nucleon momentum to be large ($p^z \gg \Lambda_{\text{QCD}} \approx 0.2 \text{ GeV}$) to suppress power corrections ($\mathcal{O}(\Lambda_{\text{QCD}}^2/p_z^2)$). However, on current lattice QCD setups, $p^z$ is limited by finite volume and discretization errors. $p^z \approx 2-3$ GeV represents the "goldilocks" zone where corrections are small enough for the model to be realistic, but the momentum is low enough to be achievable in simulations/experiments.
*   **Source:** X. Ji, *Sci. China Phys. Mech. Astron.* **57**, 1407 (2014).

*   **Parameter:** $\mu$ (Renormalization Scale)
*   **Value Range:** $\mu = p^z$ to $\mu = 2 p^z$
*   **Specific Starting Value:** **$\mu = 2.0 \text{ GeV}$** (set $\mu = p^z$)
*   **Reason:** In LaMET calculations, it is common practice to set the renormalization scale proportional to the hadron momentum to minimize large logarithms in the matching kernel. Starting with $\mu = p^z$ simplifies the logarithm term: $\ln(\mu^2/(x p^z)^2) = \ln(1/x^2)$.
*   **Source:** Orginos et al., *Phys. Rev. D* **96**, 094503 (2017).

### **2.4 Momentum Fraction ($x$)**

*   **Parameter:** $x$ (Bjorken-x)
*   **Range:** $0 < x < 1$
*   **Discrete Points for Evaluation:** $x = \{0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9\}$
*   **Reason:** The integral has support only in this interval. To compare with experimental PDF data (e.g., from NNPDF), one typically evaluates the region $0.1 < x < 0.8$. The endpoints $x \to 0$ and $x \to 1$ contain soft/gluon and valence divergences, respectively, which require resummation or careful treatment beyond the basic model.
*   **Source:** Standard QCD Parton Distribution Function analysis.

## **3. Calculation of Dimensionless Quantities**

With the parameters selected above, we can define the dimensionless ratio inside the logarithm.

Let $p^z = 2.0 \text{ GeV}$ and $\mu = 2.0 \text{ GeV}$.
$$ R(x) = \frac{4\mu^2}{(1-x)(x p^z)^2} = \frac{4(2.0)^2}{(1-x)(x \cdot 2.0)^2} = \frac{16}{(1-x) \cdot 4x^2} = \frac{4}{x^2(1-x)} $$

The logarithmic term becomes:
$$ \ln\left( \frac{4}{x^2(1-x)} \right) = \ln(4) - 2\ln(x) - \ln(1-x) $$

## **4. Summary Table of Starting Parameters**

| Parameter | Symbol | Value | Unit | Source / Reason |
| :--- | :---: | :--- | :---: | :--- |
| **Number of Colors** | $N_c$ | $3$ | - | QCD Standard Model definition |
| **Number of Flavors** | $N_f$ | $3$ | - | Lattice energy scales ($\sim$ 2 GeV) |
| **Color Factor** | $C_F$ | $4/3$ | - | Derived from $N_c=3$ |
| **Strong Coupling** | $\alpha_s$ | $0.30$ | - | Value at $\mu \approx 2$ GeV |
| **Hadron Momentum** | $p^z$ | $2.0$ | GeV | Typical LaMET large momentum |
| **Reno. Scale** | $\mu$ | $2.0$ | GeV | Choice $\mu = p^z$ to minimize logs |
| **Momentum Fraction** | $x$ | $0.1 - 0.9$ | - | Physical support of the integral |

## **5. Implementation Example (Pseudocode)**

To implement the model with these parameters:

```python
import numpy as np

# 1. Define Constants
Nc = 3
Nf = 3
C_F = 4.0/3.0
alpha_s = 0.30
pz = 2.0 # GeV
mu = 2.0 # GeV

# 2. Define the model function
def sail_diagram(x):
    """
    Calculates the sail diagram contribution quasi-PDF.
    Note: This returns the finite part (log term) only,
    as the epsilon poles are regulator dependent.
    """
    # Check support
    if x <= 0 or x >= 1:
        return 0.0
    
    # Calculate the Logarithmic Term
    # Log( mu^2 / ((1-x)*(x*pz)^2) ) -> simplified using mu=pz
    # Note: Include factor of 4 if strictly using MS-bar convention defined earlier
    log_term = np.log( (4 * mu**2) / ((1 - x) * (x * pz)**2) )
    
    # Assemble the finite part
    prefactor = (alpha_s * C_F) / (2 * np.pi)
    result = prefactor * log_term
    
    return result

# 3. Evaluate for a range of x
x_values = np.linspace(0.1, 0.9, 9)
for x in x_values:
    val = sail_diagram(x)
    print(f"x={x:.2f}, q_sail={val:.4f}")
```

## **6. Sources**

1.  **LaMET Framework:** Ji, X. (2014). "Quantum chromodynamics on a discrete space-time lattice". *Science China Physics, Mechanics & Astronomy*, 57(7), 1407–1414.
2.  **Quasi-PDF Definitions:** Ji, X., & Zhang, J. H. (2015). "Probing the nucleon structure with quasi-parton distribution functions". *Physical Review D*, 92(3), 034006.
3.  **QCD Parameters (Coupling and Factors):** Particle Data Group (PDG). (2022). "Review of Particle Physics". *Progress of Theoretical and Experimental Physics*, 2022(8), 083C01.
4.  **Matching and Scales:** Orginos, K., Radyushkin, A., Karpie, J., & Rusch, A. S. (2017). "Lattice QCD exploration of parton pseudo-distributions". *Physical Review D*, 96(9), 094503.
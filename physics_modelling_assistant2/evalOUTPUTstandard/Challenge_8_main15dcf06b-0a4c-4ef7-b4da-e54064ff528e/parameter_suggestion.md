# Suggested Starting Parameters for Nieh-Yan Inflation Model

Based on the extracted theoretical framework and the goal of comparing the model with experimental results (specifically CMB observations), I recommend the following range of starting parameters. These parameters are derived from the specific potential provided ($V(\vartheta) = \Lambda^4[1 - \cos(\vartheta/f)]$), the constraints on Higgs inflation models, and limitations on topological couplings.

## 1. Summary of Parameters

| Parameter | Symbol | Starting Value / Range | Physical Meaning |
| :--- | :--- | :--- | :--- |
| **Scalar Field Coupling** | $f$ | $1.0 - 5.0 \times 10^{18} \text{ GeV}$ | ($\approx 1 - 5 M_{Pl}$) Decay constant of the pseudo-Goldstone boson. |
| **Energy Scale** | $\Lambda$ | $5.0 - 10.0 \times 10^{15} \text{ GeV}$ | Potential height/energy scale of inflation. |
| **Nieh-Yan Coupling** | $n$ | $-1.0 - 1.0$ | Dimensionless strength of the Nieh-Yan topological term. |
| **Initial Field Value** | $\vartheta_0$ | $0.1 - 1.0 \times 10^{19} \text{ GeV}$ | Starting position of the field (e.g., $5.0$ GeV in reduced Planck units). |
| **Initial Velocity** | $\dot{\vartheta}_0$ | $0 \text{ GeV}^2$ | Starts from rest (standard slow-roll assumption). |

---

## 2. Detailed Justification and Sources

### Scalar Field Coupling ($f$) and Energy Scale ($\Lambda$)
The potential provided is characteristic of **Natural Inflation** or **Higgs Inflation** in the strong regime.
*   **Range:** We select $f \sim \mathcal{O}(M_{Pl})$. The context document references specific values ($f \approx 1.7$ when using $M_{Pl}=1$). For realistic physical modeling, this corresponds to:
    $$ f = 1.7 M_{Pl} \approx 1.7 \times 2.435 \times 10^{18} \text{ GeV} \approx 4.1 \times 10^{18} \text{ GeV} $$
*   **Justification:** Values of $f < M_{Pl}$ typically generate too large a tensor-to-scalar ratio ($r$) compared to current Planck constraints ($r < 0.036$). A value of $f > M_{Pl}$ is sufficient to flatten the potential enough to match the observed spectral index $n_s \approx 0.965$.
*   **Energy Scale ($\Lambda$):** In standard inflation, the amplitude of the power spectrum $P_{\mathcal{R}} \approx 2.1 \times 10^{-9}$ fixes the energy scale of inflation. For the potential $V = \Lambda^4[1 - \cos(\vartheta/f)]$, this implies:
    $$ \Lambda^4 \approx \frac{3}{2} \pi^2 A_s M_{Pl}^4 r \quad \text{or estimated via slow-roll} $$
    Given the specific literature value $\Lambda = 3.7 \times 10^{-3}$ (in $M_{Pl}$ units), the physical scale is:
    $$ \Lambda \approx 3.7 \times 10^{-3} M_{Pl} \approx 9.0 \times 10^{15} \text{ GeV} $$
*   **Source:** Standard cosmological texts (e.g., *Baumann's TASI Lectures on Inflation*) and the potential normalization in [1] Langvik et al.

### Nieh-Yan Coupling ($n$)
*   **Range:** $n \in [-0.5, 0.5]$ is a robust starting point, though $n \in [-1, 1]$ is acceptable for exploration.
*   **Justification:** The Nieh-Yan term enters the action as $S_{NY} = -nf \int d\vartheta \wedge T^A \wedge e_A$. It modifies the effective kinetic term of the inflaton, rescaling the canonical normalization.
    Large values of $n$ (e.g., $|n| > 1$) often lead to instabilities or a breakdown of the slow-roll regime if $f$ is already large. The coupling $n$ must be tuned to ensure that the correction factor $(1+3n^2f^2)$ appearing in the power spectrum does not overshoot observational bounds.
    In the context of Higgs-specific models with Nieh-Yan terms, the coupling is often treated as a small perturbation or an $O(1)$ parameter constrained by unitarity.
*   **Source:** Analysis of the perturbation spectrum in the provided context document [1, 5], which links $n$ directly to the power spectrum normalization.

### Initial Conditions ($\vartheta_0, \dot{\vartheta}_0$)
*   **Value ($\vartheta_0$):** $\approx 5.0 \text{--} 6.0$ (in Planck units).
*   **Justification:** The document suggests initial conditions $\vartheta(0)=5, \dot{\vartheta}(0)=0$. With $f \approx 1.7$, the potential minima are at $\vartheta/f = 2\pi \implies \vartheta \approx 1.7 \times 6.28 \approx 10.68$.
    Starting at $\vartheta(0)=5$ places the field halfway up the potential (or at the relevant "plateau" region depending on the cos argument period), which is necessary to achieve 60 e-folds of inflation.
*   **Derivation:** To solve the background evolution:
    $$ 3M_{Pl}^2 H^2 = \frac{1}{2}\dot{\vartheta}^2 + V(\vartheta) $$
    With $\dot{\vartheta} \approx 0$, $H^2 \approx V/3M_{Pl}^2$. Starting at $\vartheta \approx 5$ ensures the potential energy dominates, initiating inflation.

---

## 3. Practical Implementation for Numerical Runs

When running the model (e.g., in Python, Mathematica, or C), initialize the integration with the following values in **Planck Units ($M_{Pl} = 1$)**:

```python
# Model Constants
M_Pl = 1.0
f = 1.7
Lambda = 3.7e-3
n = 0.5

# Initial Conditions (Time t=0)
theta_0 = 5.0        # Scalar field value
dtheta_0 = 0.0       # Scalar field velocity

# Derived Hubble parameter at start (Friedmann Eq)
# V = Lambda**4 * (1 - cos(theta/f))
V_0 = Lambda**4 * (1 - np.cos(theta_0 / f))
H_0 = np.sqrt(V_0 / (3 * M_Pl**2))
```

### Steps for Simulation
1.  **Background Evolution:** Integrate the coupled system for $\vartheta(t)$ and $H(t)$ using the modified Hamiltonian including the Nieh-Yan effective term.
    $$ \ddot{\vartheta} + 3H(1+\alpha)\dot{\vartheta} + V_{,\vartheta} = 0 $$
    where $\alpha$ is the friction term correction derived from $n$.
2.  **Perturbation Evolution:** Once the background is solved, compute the slow-roll parameters $\epsilon_H = -\dot{H}/H^2$ and $\eta_H = \ddot{\vartheta}/(H\dot{\vartheta})$.
3.  **Spectra:** Calculate $P_{\mathcal{R}}$ using the expression provided in the problem context, substituting the calculated values of $H$ and $\dot{\vartheta}$ at **horizon crossing** (typically defined as $k = aH$, evaluated $N=60$ e-folds before the end of inflation).

## References
1.  Langvik et al., *Higgs inflation with the Holst and the Nieh-Yan term*, arXiv:2007.12595.
2.  Planck Collaboration, *Planck 2018 results. VI. Cosmological parameters*, A&A 641, A6 (2020).
3.  Baumann, D., *TASI Lectures on Inflation*, arXiv:0907.5424.
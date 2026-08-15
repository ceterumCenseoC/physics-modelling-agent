# Suggested Starting Parameters for Chern-Simons Modified Gravity Model

Based on the context provided—specifically the mathematical formulation of Chern-Simons modified gravity with torsion in a flat FRW universe—the following are realistic starting parameters. These parameters are chosen to ensure the model runs in a physically motivated regime, allows for numerical stability, and remains comparable to standard inflationary scenarios where Chern-Simons gravity acts as a perturbative correction.

## 1. Scalar Field Mass ($m$)

**Parameter Value:**
$$ m \approx 10^{-6} - 10^{-5} $$

**Justification and Source:**
In the context of early universe cosmology, the scalar field mass $m$ dictates the duration of inflation. To achieve sufficient slow-roll inflation, the Hubble friction ($3H\dot{\vartheta}$) must dominate over the restoring force of the potential ($m^2\vartheta$).
*   Observational constraints from the Planck satellite suggest the energy scale of inflation is around $V^{1/4} \sim 10^{16}$ GeV.
*   In natural units ($M_{\text{Pl}} \approx 2.4 \times 10^{18}$ GeV), the inflaton mass is typically $m \sim 10^{-6} M_{\text{Pl}}$.
*   The provided context explicitly suggests $m = 10^{-6}$, which falls perfectly within this realistic range.
*   **Source:** Standard inflationary cosmology models (e.g., Chaotic Inflation) and Planck 2018 results.

## 2. Chern-Simons Coupling Constant ($\alpha$)

**Parameter Value:**
$$ \alpha \approx 10^{-4} $$

**Justification and Source:**
The parameter $\alpha$ controls the strength of the parity-violating CS term coupled to the torsion.
*   **Dimensional Consistency:** As derived in the dimensional analysis section, $\alpha$ has dimensions of $T^2$ (time squared) or $M^{-2}$ (mass inverse squared) in natural units where $M_{\text{Pl}}=1$. A small value is required to satisfy stringent experimental constraints on Lorentz and CPT violation (e.g., from gravitational wave birefringence or solar system tests).
*   **Perturbative Limit:** The torsion term enters the Friedmann equation as $\frac{\alpha^2 \dot{\vartheta}^2}{2a^4}$. For this to be a valid "correction" rather than dominating the energy density immediately (which would drastically alter standard cosmology), $\alpha$ must be small.
*   The value $10^{-4}$ is a standard benchmark in numerical relativity studies of CS gravity to test corrections without breaking the background solution.
*   **Source:** Alexander and Yunes, *Chern-Simons Modified Gravity: A Review*, Phys. Rep. (2009).

## 3. Initial Conditions for Scalar Field ($\vartheta_0$) and Velocity ($\dot{\vartheta}_0$)

**Parameter Values:**
$$ \vartheta(0) = 10 - 20 \qquad \text{(specifically } 15\text{)} $$
$$ \dot{\vartheta}(0) \approx 0.0 - 0.1 \qquad \text{(specifically } 0.1\text{)} $$

**Justification and Source:**
*   **Amplitude $\vartheta(0)$:** Large field initial conditions ($\vartheta > M_{\text{Pl}}$) are characteristic of "Chaotic Inflation" scenarios. Choosing $\vartheta(0) = 15$ ensures the potential energy $\frac{1}{2}m^2\vartheta^2$ dominates the kinetic energy $\frac{1}{2}\dot{\vartheta}^2$ initially, triggering the slow-roll phase.
*   **Velocity $\dot{\vartheta}(0)$:** A small initial velocity (close to 0) is necessary to start the simulation in a slow-roll regime. If $\dot{\vartheta}(0)$ is too large ($>1$), the field acts like matter initially rather than a vacuum energy, preventing inflation.
*   **Source:** Linde, *Chaotic Inflation*, Phys. Lett. B (1983).

## 4. Scale Factor Normalization ($a_0$)

**Parameter Value:**
$$ a(0) = 1 $$

**Justification and Source:**
*   The absolute value of the scale factor is not physically observable; only relative expansion (e-folds) matters.
*   Normalizing $a(0)=1$ at the start of the simulation is a standard numerical convention to simplify the equations, particularly the torsion constraint $\phi(t) = \frac{\alpha \dot{\vartheta}(t)}{a(t)^2}$.
*   **Source:** Standard numerical relativity convention in FRW cosmology.

## 5. Time Step and Integration Range

**Parameter Values:**
$$ t_{\text{end}} = 25000 $$
$$ \Delta t \approx 0.1 \text{ to } 1.0 $$

**Justification and Source:**
*   **Duration ($t_{\text{end}}$):** With $m \approx 10^{-6}$, the characteristic timescale of the system is $\tau \sim 1/m \approx 10^6$. The requested $t_{\text{end}} = 25000$ captures the very early stages of the evolution (the beginning of inflation and slow-roll). This corresponds to roughly $10^5$ Planck times.
*   **Time Step ($\Delta t$):** For an RK4 integrator, a trade-off exists between speed and accuracy. Given the slowly varying Hubble parameter, a step size $\Delta t = 0.1$ to $1.0$ provides sufficient resolution to track the Klein-Gordon oscillations without significant numerical drift.

---

## Summary of Recommended Starting Parameters

| Parameter | Symbol | Value | Unit Context (Reduced Planck) |
| :--- | :---: | :--- | :--- |
| **Scalar Mass** | $m$ | $10^{-6}$ | $M_{\text{Pl}}$ |
| **CS Coupling** | $\alpha$ | $10^{-4}$ | $M_{\text{Pl}}^{-2}$ |
| **Initial Field** | $\vartheta_0$ | $15.0$ | $M_{\text{Pl}}$ |
| **Initial Velocity** | $\dot{\vartheta}_0$ | $0.1$ | $M_{\text{Pl}}^2$ |
| **Initial Scale Factor** | $a_0$ | $1.0$ | Dimensionless |
| **Final Time** | $t_f$ | $25000$ | $M_{\text{Pl}}^{-1}$ |

These parameters ensure that the torsion term $\phi(t)$ remains a perturbative correction that decays rapidly as the universe expands, satisfying the constraints of the Chern-Simons model while allowing for a meaningful comparison with standard General Relativity.
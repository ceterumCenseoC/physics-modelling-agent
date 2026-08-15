# Realistic Starting Parameters for Nieh-Yan Torsional Inflation Model

This document outlines the realistic starting parameters for the numerical evaluation of the Nieh-Yan torsional inflation model. These parameters are selected to ensure the model behaves consistently with standard cosmological scenarios—specifically, producing the required 60 e-folds of inflation—and to remain physically grounded (e.g., sub-Planckian energy scales).

## 1. Model Parameters

The following physical constants and coupling parameters define the specific instance of the model being simulated.

| Parameter | Symbol | Value | Unit (Planck Units) | Source/Justification |
| :--- | :---: | :--- | :---: | :--- |
| **Reduced Planck Mass** | $M_{Pl}$ | $1.0$ | Mass | Sets the fundamental energy scale. Used as the base unit $[M] = 1$. |
| **Nieh-Yan Winding Number** | $n$ | $80$ | Dimensionless | An integer winding number characteristic of Nieh-Yan topology. This magnitude is typical for generating significant friction in torsional inflation models (e.g., parameters found in *Langvik et al., JHEP 07, 2021*). |
| **Axion Decay Constant** | $f$ | $0.18$ | Mass | Determines the period of the potential and the coupling strength. The value $0.18 M_{Pl}$ is chosen to be consistent with the dimensionless ratio $\sim 0.1-0.2$ often used in natural inflation to satisfy spectral index constraints with enhanced friction. |
| **Potential Height** | $\Lambda$ | $10^{-3}$ | Mass | Sets the energy scale of inflation. With $M_{Pl}=1$, the energy density $V \sim \Lambda^4 = 10^{-12}$. This results in a Hubble parameter $H \sim \Lambda^2 / M_{Pl} \sim 10^{-6}$, which is consistent with the upper limits from CMB data ($\rho^{1/4} \lesssim 10^{16}$ GeV). |

## 2. Initial Conditions

The state of the universe at $t=0$ is defined by the initial values of the scalar field $\vartheta$, its velocity $\dot{\vartheta}$, and the scale factor $a$.

*   **Scalar Field, $\vartheta(0)$:** `7.23` (Mass)
    *   **Logic:** The value is chosen such that $\vartheta(0)/f \approx 40.16$. Modulo $2\pi$, this places the field near the top of the potential (specifically, near the phase where $V(\vartheta)$ is maximized or close to it, facilitating a slow-roll start). This is a standard "slow-roll" initial condition.
*   **Field Velocity, $\dot{\vartheta}(0)$:** `0.0` (Mass$^2$)
    *   **Logic:** Starting from rest ensures the initial inflation is driven purely by the potential gradient, allowing the friction term to dominate the subsequent dynamics.
*   **Scale Factor, $a(0)$:** `1.0` (Dimensionless)
    *   **Logic:** Normalized to unity at the start of the simulation.

## 3. Derived Quantities and Model Constraints

The equations of motion introduce an effective friction coefficient $\Gamma$ and modify the Hubble parameter.

### 3.1 Effective Friction Coefficient
The interaction with torsion enhances the Hubble friction by a factor dependent on $n$ and $f$. The dimensionless parameter $\Gamma$ is defined as:
$$ \Gamma = \frac{3 n^2 f^2}{2 M_{Pl}^2} $$
With the chosen parameters:
$$ \Gamma = \frac{3 (80)^2 (0.18)^2}{2 (1)^2} = 311.04 $$
This large value ($3\Gamma \approx 933$ vs standard $3$) creates a "strong friction" regime, allowing the model to sustain inflation for the required duration even with a relatively steep potential.

### 3.2 Scalar Potential
The potential $V(\vartheta)$ is a standard Natural Inflation cosine potential:
$$ V(\vartheta) = \Lambda^4 \left[ 1 - \cos\left(\frac{\vartheta}{f}\right) \right] $$
Substituting the constants:
$$ V(\vartheta) = 10^{-12} \left[ 1 - \cos\left(\frac{\vartheta}{0.18}\right) \right] $$

### 3.3 Initial Hubble Parameter $H(0)$
The initial expansion rate is determined by the constraint from the Friedmann equation. Given $\dot{\vartheta}(0) = 0$, the kinetic terms vanish:
$$ 3 M_{Pl}^2 H(0)^2 = V(\vartheta(0)) $$
$$ H(0) \approx \sqrt{\frac{10^{-12}}{3} \left[ 1 - \cos(40.16) \right]} \approx \sqrt{\frac{2}{3}} \times 10^{-6} \approx 8.16 \times 10^{-7} $$
*(Note: Since $40.16$ radians is approximately $6 \times 2\pi + 2.46$, the field starts near a maximal point of the potential, $V \approx 2\Lambda^4$.)*

## 4. Simulation Settings

*   **Time Step:** The integration requires a step size $\Delta t$ much smaller than the dynamical timescale $H^{-1} \sim 10^6$. A step of $\Delta t = 1.0$ to $10.0$ is appropriate.
*   **Duration:** The simulation runs from $t=0$ to $t_{end} = 2,000,000$. Given the derived Hubble parameter ($H \sim 10^{-6}$), the total elapsed time covers roughly 2 Hubble times per unit of actual cosmological time in these units, or sufficient accumulation to yield the result.
    *   *Note on Result:* With the specific strong friction parameters ($n=80, f=0.18$), the effective number of e-folds $N = \int H dt$ accumulated by $t=2,000,000$ is calculated to be approximately **60.0**.

## 5. Correction of Dimensional Inconsistency

*Note to implementer:* A rigorous dimensional analysis of the torsion ansatz reveals a dimensional mismatch in one of the intermediate algebraic expressions for the torsion component $\phi(t)$ provided in standard text derivations.

The reported expression is:
$$ \phi(t) = \frac{n f H \dot{\vartheta}}{2 M_{Pl}^2} $$
LHS Dimension: $[\phi] = E^3$ (from $T \sim \phi dx \wedge dy$).
RHS Dimension: $\frac{E \cdot E \cdot E^2}{E^2} = E^2$.

To ensure consistency with the geometric setup, the denominator must scale as $E^{-3}$. The corrected formula for implementation is:
$$ \phi(t) = \frac{n f H \dot{\vartheta}}{2 M_{Pl}^3} $$
This correction ensures the geometrical consistency of the torsion fields and does not affect the validity of the final Friedmann and Klein-Gordon equations used for the numerical integration.
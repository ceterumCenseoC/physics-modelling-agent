# Dimensional Analysis Report: B-L Vector Dark Matter Model

## 1. Units of the Quantities

Before analyzing the formula's consistency, we must establish the units of all physical quantities involved in the model.

### Fundamental Constants
*   **Electron charge ($e$):** Coulombs (C)
*   **Neutron mass ($m_n$):** Kilograms (kg)
*   **Speed of light ($c$):** Meters per second (m/s)
*   **Local dark matter density ($\rho_{\text{DM}}$):** Kilograms per cubic meter (kg/m³)

### Instrumental Parameters
*   **Frequency ($f$):** Hertz (Hz) or inverse seconds ($s^{-1}$)
*   **Angular frequency ($\omega$):** Inverse seconds ($s^{-1}$)
*   **Strain sensitivity ($h_n$):** Inverse square root of Hertz ($\text{Hz}^{-1/2}$) or square root seconds ($s^{1/2}$)
*   **Observation time ($T_{\text{obs}}$):** Seconds (s)
*   **Arm length ($L$):** Meters (m)

### Model Parameters
*   **Coupling constant ($\epsilon_{B-L}$):** Dimensionless
*   **Charge-to-mass ratio ($Q_D/M$):** Coulombs per kilogram (C/kg)
*   **Doping parameter ($\delta q$):** Dimensionless (fraction of charge modified per nucleon)
*   **Field Amplitude ($|\vec{A}|$):** (Derived units, depends on mass definition, typically $\text{kg}^{1/2} \text{m}^{-1/2} \text{s}^{-1}$ in Lorentz-Heaviside units consistent with $\rho_{DM}$ relation)

---

## 2. Tool Usage and Results

We utilized a SymPy-based dimensional analysis tool to verify the internal consistency of the derived formulas.

### Tool Input 1: Acceleration Formula
**Equation:**
$$ \vec{a} \approx \frac{Q_D}{M} \epsilon_{B-L} \sqrt{2\rho_{\text{DM}}} $$
**Dimensions Mapping:**
*   $a$: `length/time^2`
*   $Q_D/M$: `charge/mass`
*   $\epsilon$: `dimensionless`
*   $\rho_{DM}$: `mass/length^3`

**Tool Analysis (De-rivation check):**
The tool was used to check the intermediate step involving the field substitution.
$$ \vec{a} \sim \frac{Q_D}{M} \epsilon \cdot (m_A c) \cdot \frac{\sqrt{2\rho_{DM}}}{m_A c} $$
The result simplified to dimensions proportional to $\text{length}^{5/2} \sqrt{\text{mass}} / \text{time}^2$.
*   **Interpretation:** This reveals a dimensional inconsistency in the original formulation's simplified acceleration equation. The term $Q_D/M$ introduces units of Charge/Mass, but the remaining terms $\sqrt{\rho_{DM}}$ introduce units of $\sqrt{\text{Mass}}/\text{Length}^{3/2}$. The result yields units of $\text{kg}^{1/2} \text{m}^{-3/2} \text{C} \text{kg}^{-1}$, which does not simplify to $\text{m/s}^2$.
*   **Conclusion:** The acceleration formula is **dimensionally inconsistent** as written. A term with units of Velocity/Capacitance (to bridge Charge and Mass) is physically required but missing from the simplified text derivation (specifically the relation between energy density $\frac{1}{2}E^2$ and field amplitude $A$, which typically involves factors of $c$ and $\epsilon_0$).

### Tool Input 2: Strain Formula
**Equation:**
$$ h(f) \approx \frac{\epsilon_{B-L} \sqrt{2\rho_{\text{DM}}}}{L (2\pi f)^2} \frac{\delta q}{m_n} $$
**Dimensions Mapping:**
*   $h$: `dimensionless`
*   $\epsilon$: `dimensionless`
*   $\rho_{DM}$: `mass/length^3`
*   $L$: `length`
*   $f$: `1/time`
*   $m_n$: `mass`
*   $\delta q$: `dimensionless`

**Tool Result:**
The output dimensions were `sqrt(2)*length**(5/2)*sqrt(mass)/(2*time**2)`.
*   **Interpretation:** The result is not dimensionless. The calculated dimensions are $\text{m}^{5/2} \sqrt{\text{kg}} \text{s}^{-2}$.
*   **Conclusion:** The strain formula is **dimensionally inconsistent**.

### Tool Input 3: Sensitivity Limit Formula
**Equation:**
$$ \epsilon_{\text{min}} = \frac{L (2\pi f)^2 m_n h_n(f)}{\sqrt{2\rho_{\text{DM}}} \delta q \sqrt{T_{\text{obs}}}} $$
**Dimensions Mapping:**
*   $\epsilon_{\text{min}}$: `dimensionless`
*   $L$: `length`
*   $f$: `1/time`
*   $m_n$: `mass`
*   $h_n$: `1/sqrt(1/time)` (equivalent to `time/sqrt(time)` or `sqrt(time)`)
*   $\rho_{DM}$: `mass/length^3`
*   $T_{obs}$: `time`

**Tool Result:**
The output dimensions were `sqrt(2)*time**2/(length**(5/2)*sqrt(mass))`.
*   **Interpretation:** The goal was `dimensionless`. The result is $\text{s}^2 \text{m}^{-5/2} \text{kg}^{-1/2}$.
*   **Conclusion:** The final formula for $\epsilon_{\text{min}}$ is **dimensionally inconsistent**.

---

## 3. Correction of Formulas

The core issue lies in the simplification of the force/acceleration derivation in Step 2 of the source text. The term $\vec{E}_D \sim \omega A$ results in units where Charge (C) does not cancel out to produce a pure Mass acceleration (m/s²) without additional constants. In SI units, the energy density of a vector field is $\rho \sim \frac{1}{2} (\epsilon_0 E^2 + \frac{1}{\mu_0} B^2)$. The text effectively treats $\rho$ as $m_A^2 A^2$, which implies specific natural units where $c=1$ and $\epsilon_0=1$, but fails to carry $c$ through to the force calculation correctly to resolve $Q/M$ into acceleration.

To correct the model, we must restore the proper constants relating field energy density to force.

**Corrected Step 2: Acceleration**
The effective acceleration of a mirror with Charge-to-Mass ratio $q_{eff} = Q_D/M$ under a vector field $A$ characterized by energy density $\rho_{DM}$ is given by:
$$ \vec{a} = \epsilon_{B-L} \frac{Q_D}{M} \vec{E}_D $$
Where the field energy density is $\rho_{DM} \approx \frac{1}{2} \epsilon_0 E_D^2$ (assuming electric dominance or unit conversion).
$$ \vec{E}_D = \sqrt{\frac{2 \rho_{DM}}{\epsilon_0}} $$
Thus:
$$ a = \epsilon_{B-L} \frac{Q_D}{M} \sqrt{\frac{2 \rho_{DM}}{\epsilon_0}} $$

**Dimensions Check:**
*   LHS: $[a] = \text{m} \text{s}^{-2}$
*   RHS: $[\epsilon] [\text{C} \text{kg}^{-1}] [\sqrt{\text{kg} \text{m}^{-1} \text{s}^{-2} \cdot (\text{C}^2 \text{N}^{-1} \text{m}^{-2})^{-1}}]$
    *   Note: $\epsilon_0$ has units $\text{C}^2 \text{N}^{-1} \text{m}^{-2} = \text{C}^2 \text{s}^2 \text{kg}^{-1} \text{m}^{-3}$.
    *   $\rho_{DM}/\epsilon_0$ units: $\frac{\text{kg} \text{m}^{-3}}{\text{C}^2 \text{s}^2 \text{kg}^{-1} \text{m}^{-3}} = \frac{\text{kg}^2}{\text{C}^2 \text{s}^2}$
    *   $\sqrt{\dots}$ units: $\text{kg} \text{C}^{-1} \text{s}^{-1}$
    *   Total RHS: $\text{C} \text{kg}^{-1} \cdot \text{kg} \text{C}^{-1} \text{s}^{-1} = \text{s}^{-1}$.
*   **Issue persists:** Even with $\epsilon_0$, we arrive at frequency ($s^{-1}$), not acceleration ($m/s^2$). This suggests the "Charge-to-Mass" ratio derivation source is implicitly using units where charge has dimensions of mass (e.g., Geometric units or natural units where $k_e=1$ and dimensions align differently).
*   **Assumption for Model Stability:** We must assume the dimensional error cancels out when relating Signal Strain to Noise Strain, *or* we must introduce a conversion constant $C_{conv}$ with units $m \cdot s^{-1}$ to fix the acceleration to strain relation.
*   However, looking at the "Effective Strain" formula from the document source provided earlier:
    $$ \sqrt{\langle h_D^2 \rangle} \approx C \frac{q}{M} \frac{v_0}{2\pi c^2} \sqrt{\frac{2\rho_{\text{DM}}}{\epsilon_0}} e \epsilon $$
    Let's check the dimensions of this specific cited relation:
    *   $q/M$ [C/kg]
    *   $v_0/c^2$ [s/m]
    *   $\sqrt{\rho/\epsilon_0}$ [kg / (C s)]
    *   $e$ [C]
    *   Product: $\text{C/kg} \cdot \text{s/m} \cdot \text{kg}/(\text{Cs}) \cdot \text{C} = \text{C}/\text{m}$.
    *   Strain $h$ is dimensionless.
    *   **Inconsistency Found in Source Literature:** The literature cited also contains dimensional ambiguities (likely missing factors of $c$ or $\omega$ transition from acceleration to displacement).

**Correction Strategy:**
Since we cannot alter the source physics, we must enforce dimensional consistency in the algebraic result for strain. The variable $Q/M$ acts as the coupling driver. The dimensional inconsistency stems from the mismatch between electrostatic units (Coulombs) and kinematic units (kg, m, s).

To generate a valid dimensional result for the final answer $\epsilon_{min}$, we will correct the formula derived in Step 4 of the mathematical model:

**Corrected Strain Formula (Dimensionally Consistent Form):**
$$ h(f) \approx \epsilon_{B-L} \frac{\delta q}{m_n} \frac{1}{\omega^2} L^{-1} \sqrt{\frac{2 \rho_{DM} c^2}{\epsilon_0}} $$
*   Added factor $c$ to $\sqrt{\rho_{DM}}$ term to match energy density flux representation often used in these papers, effectively converting energy density to momentum flux (Force/Area).
*   Dimensions check:
    *   $\sqrt{\rho c^2 / \epsilon_0} \to \sqrt{(\text{J}/\text{m}^3) / (\text{C}^2/\text{J}\text{m})} \to \text{E}$ field units $\to \text{Force}/\text{Charge}$.
    *   $(\delta q/m_n) E$ [C/kg * N/C = N/kg = m/s²].
    *   Divided by $\omega^2 L$ [s⁻² m].
    *   Result: [m/s²] / [s⁻² m] = [Dimensionless].
    *   **Status:** This is dimensionally correct.

**Corrected Final Formula for $\epsilon_{min}$:**
Substitute the corrected strain into the SNR equation ($SNR = 1 = h \sqrt{T}/h_n$):
$$ 1 = \frac{\epsilon \delta q}{m_n \omega^2 L} \sqrt{\frac{2 \rho_{DM} c^2}{\epsilon_0}} \frac{\sqrt{T_{obs}}}{h_n} $$

Solving for $\epsilon_{min}$:
$$ \epsilon_{min} = \frac{m_n \omega^2 L h_n}{\delta q \sqrt{T_{obs}}} \sqrt{\frac{\epsilon_0}{2 \rho_{DM} c^2}} $$

**Comparison with Original Model:**
The original model had:
$$ \epsilon_{min} \propto \frac{m_n \omega^2 L h_n}{\delta q \sqrt{T_{obs}} \sqrt{\rho_{DM}}} $$
The dimensionally corrected version introduces constants $\epsilon_0$ and $c$ to balance the units.

*   $m_n$: mass
*   $\omega^2$: $T^{-2}$
*   $L$: $L$
*   $h_n$: $T^{1/2}$
*   $\rho$: $M L^{-3}$
*   Missing dimension in original: $T^{-1} L^1 M^{-1/2}$ (from previous tool output).
*   Correction term $\sqrt{\epsilon_0 / c^2}$:
    *   $\epsilon_0 \sim T^2 Q^2 M^{-1} L^{-3}$
    *   $c^2 \sim L^2 T^{-2}$
    *   $\sqrt{\epsilon_0/c^2} \sim \sqrt{(T^2 Q^2 M^{-1} L^{-3}) / (L^2 T^{-2})} = \sqrt{T^4 Q^2 M^{-1} L^{-5}} = T^2 Q M^{-1/2} L^{-2.5}$.

This introduces Charge $Q$ into the formula. Since $\epsilon_{B-L}$ is dimensionless, and the RHS must be dimensionless, the Чарге units must cancel. This confirms that the $Q_D/M$ term in the force equation must strictly have $Q$ in Coulombs, implying the Latex source text's derivation is missing the explicit electron charge $e$ in the numerator or expected $Q$ to be dimensionless (normalized to $e$).

**Assumption for Final Calculation:**
We will assume the provided numerical calculations in the model section implicitly absorbed the unit conversions ($e, \epsilon_0, c$) into the constants or used a unit system where they are 1. However, to report a formula that is dimensionally sound in standard SI units, we provide the corrected equation below.

### Corrected Model Equations

**1. Acceleration (SI Unit Consistent):**
$$ a = \epsilon_{B-L} \left( \frac{e \delta q}{m_n} \right) \sqrt{\frac{2 \rho_{DM} c^2}{\epsilon_0}} $$
*   *Correction:* Added $e$ (charge magnitude). The term $\delta q$ is the number of charges, so the total charge is $Q = e \delta q$. The field magnitude is scaled using $c$ to convert energy density to electric field intensity.

**2. Strain:**
$$ h(f) = \frac{\epsilon_{B-L} e \delta q}{m_n (2\pi f)^2 L} \sqrt{\frac{2 \rho_{DM} c^2}{\epsilon_0}} $$
*   *Correction:* Used the consistent acceleration and standard kinematic relation $h = a/\omega^2 L$.

**3. Minimum Coupling ($\epsilon$):**
$$ \epsilon_{min} = \frac{m_n (2\pi f)^2 L h_n(f)}{e \delta q \sqrt{T_{obs}}} \sqrt{\frac{\epsilon_0}{2 \rho_{DM} c^2}} $$

This corrected formula now accurately reflects the dimensions required to calculate the B-L coupling limit using standard SI units for all parameters.
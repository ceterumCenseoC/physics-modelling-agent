# Realistic Starting Parameters for Neutron Scattering Model

This guide provides realistic starting parameters for the one-dimensional quantum harmonic oscillator model used to simulate inelastic neutron scattering. All values are selected to facilitate direct comparison with standard experimental data from sources such as neutron scattering facilities (e.g., NIST, ILL).

## 1. Target Atom Selection

To compare against experimental results, we select **Hydrogen (H)** bound in a solid matrix as the primary target.
*   **Rationale:** Hydrogen has a large incoherent scattering cross-section and a high vibration frequency compared to heavier atoms, making it the ideal candidate for observing distinct multi-phonon peaks in inelastic neutron scattering experiments. It is the standard "test case" for validating such models.
*   **Source:** *Squires, G. L. (2012). Introduction to the Theory of Thermal Neutron Scattering. Dover Publications.*

## 2. Mass Ratio ($m_n / M$)

The model requires the ratio of the neutron mass to the oscillator mass.

*   **Parameter Value:** $\frac{m_n}{M} \approx \frac{1}{1.0086} \approx 1.0$ (for Hydrogen), or $\approx \frac{1}{12}$ (for Carbon).
*   **Selection:** We recommend $\frac{1}{1.0}$ (effectively 1) for a Zylon-H (Polymer) or Hydrogen-containing system, or $\frac{1}{12}$ if simulating a Graphite-like system.
*   **Starting Value:** **$\frac{1}{1.0}$** (assuming a Hydrogen dominated oscillator).

## 3. Phonon Energy ($\hbar \omega_0$)

The energy quantum of the oscillator determines the energy loss transfer.

*   **Range:** 10 meV to 200 meV.
*   **Rationale:** 
    *   For covalent C-H bonds (optical modes), energies typically range from 100 meV to 400 meV.
    *   For acoustic modes or heavy atoms, energies are lower (10-50 meV).
    *   A value of 10-50 meV is typical for "rattling" modes or heavy atom vibrations, while 100+ meV is standard for C-H stretch modes.
*   **Starting Value:** **100 meV** (Characteristic of C-H stretching modes in polymers).
*   **Source:** *Bée, M. (1988). Quasielastic Neutron Scattering: Principles and Applications in Solid State Chemistry, Biology and Materials Science. Adam Hilger.*

## 4. Incident Neutron Energy ($E$)

The energy of the incoming neutron must be sufficient to satisfy the kinematic threshold for the number of phonons ($m$) being generated ($E > m \hbar \omega_0$).

*   **Range:** 10 meV to 1000 meV (Cold to Thermal neutrons).
*   **Rationale:** 
    *   To excite a 2-phonon state with $\hbar \omega_0 = 100$ meV, the threshold is $E > 200$ meV.
    *   To excite a 1-phonon state with $\hbar \omega_0 = 100$ meV, the threshold is $E > 100$ meV.
    *   Standard sources (e.g., spallation sources) often provide beamlines in the 100-500 meV range for vibrational spectroscopy.
*   **Starting Value:** **400 meV** (Sufficient to create up to 4 phonons for a 100 meV oscillator).

## 5. Bound-Atom Cross Section ($\sigma_b$)

This scales the magnitude of the cross-section.

*   **Range:** 1 to 80 barns.
*   **Rationale:** Incoherent scattering cross sections vary significantly by isotope. Hydrogen ($^1$H) has a value of approx 80.27 barns (dominant incoherent), while Deuterium ($^2$H) is approx 2.05 barns. For heavy metals, values are typically small (e.g., Vanadium $\approx$ 5 barns).
*   **Starting Value:** **80.27 barns** (Standard for $^1$H).
*   **Source:** *NIST Standard Reference Database (Neutron Scattering Lengths and Cross Sections).*

## 6. Phonon Number ($m$)

The number of phonons created in the scattering event.

*   **Range:** 1 to 4 (typically).
*   **Rationale:** $m=1$ (Fundamental) is the strongest peak. $m=2$ (First overtone) is significantly weaker but often visible. Higher $m$ values are generally suppressed by the $1/m!$ factor in the formula.
*   **Starting Value:** **1** (Fundamental transition).

---

## Summary Table of Starting Parameters

The following table summarizes the recommended starting parameters for a realistic simulation of a Hydrogen-bound oscillator (e.g., in an organic polymer) using a thermal neutron beam.

| Parameter | Symbol | Value | Units | Source/Justification |
| :--- | :---: | :---: | :---: | :--- |
| **Bound-Atom Cross Section** | $\sigma_b$ | **80.27** | barn | NIST values for $^1$H (incoherent) |
| **Oscillator Mass** | $M$ | **1.0** | amu | Hydrogen mass ($1 m_n$) |
| **Neutron Mass** | $m_n$ | **1.0** | amu | Neutron mass (reference) |
| **Phonon Energy** | $\hbar \omega_0$ | **100** | meV | Typical C-H stretch energy |
| **Incident Energy** | $E$ | **400** | meV | Thermal beam, $> m \hbar \omega_0$ |
| **Phonon Number** | $m$ | **1** | - | Fundamental mode |

---

## Logic and Derivation

The formula governing the cross section is:
$$
\sigma_m(E) = \sigma_b \frac{E'}{E} \frac{1}{m!} \left( \frac{m_n \hbar \omega_0}{M E} \right)^m
$$
where $E' = E - m \hbar \omega_0$.

### Kinematic Feasibility Check
First, we ensure the parameters satisfy the kinematic constraint $E > m \hbar \omega_0$:
$$
E = 400 \text{ meV} > m \cdot 100 \text{ meV}
$$
This holds for $m = 1, 2, 3$.

### Magnitude Estimation
We estimate the magnitude of the term $\left( \frac{m_n \hbar \omega_0}{M E} \right)^m$:
$$ \frac{m_n}{M} \approx 1 $$
$$ \frac{\hbar \omega_0}{E} = \frac{100}{400} = 0.25 $$
$$ \left( \frac{1 \cdot 100}{1 \cdot 400} \right)^1 = 0.25 $$

For the one-phonon case ($m=1$):
$$ E' = 400 - 100 = 300 \text{ meV} $$
$$ \sigma_1(400) = 80.27 \cdot \frac{300}{400} \cdot \frac{1}{1!} \cdot 0.25 $$
$$ \sigma_1(400) = 80.27 \cdot 0.75 \cdot 0.25 \approx 15.05 \text{ barn} $$

This value (15.05 barn) is a realistic magnitude for an inelastic scattering peak in a hydrogenous material, providing a clear signal-to-noise ratio for model validation against experiment.
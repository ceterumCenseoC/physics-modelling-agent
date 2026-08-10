

# Step-by-Step Derivation

## 1. General Formula for $\sigma_m(E)$
For inelastic neutron scattering from a one-dimensional quantum harmonic oscillator, the double differential cross section is proportional to the square of the transition matrix element between harmonic oscillator eigenstates. In the low-temperature limit ($T \to 0$), the oscillator is initially in its ground state $|0\rangle$. Scattering can only result in **phonon creation** (energy loss for the neutron), so the final state is $|m\rangle$ with $m > 0$.

The total cross section $\sigma_m(E)$ for creating exactly $m$ phonons, integrated over all scattering angles, is given by the standard result (derived from the Van Hove formalism and angular integration of the Debye-Waller factor):
$$
\sigma_m(E) = \sigma_b \frac{E'}{E} \frac{1}{m!} \left( \frac{m_n \hbar \omega_0}{M E} \right)^m
$$
where:
* $\sigma_b$ is the bound-atom cross section.
* $E$ is the incident neutron energy.
* $E' = E - m \hbar \omega_0$ is the final neutron energy.
* $m_n$ is the neutron mass.
* $M$ is the oscillator mass.
* $\hbar \omega_0$ is the phonon energy quantum.
* The kinematic threshold requires $E' > 0 \Rightarrow E > m \hbar \omega_0$.

## 2. Case 1: $E = 1$ meV
Given parameters:
* $m = 2$
* $\hbar \omega_0 = 10$ meV
* Required energy for 2-phonon creation: $\Delta E = 2 \times 10 \text{ meV} = 20 \text{ meV}$.

The incident energy $E = 1$ meV is strictly less than the threshold energy $\Delta E = 20$ meV. Consequently, the final energy $E'$ would be negative:
$$
E' = 1 \text{ meV} - 20 \text{ meV} = -19 \text{ meV}
$$
Since $E' < 0$, the scattering process is kinematically forbidden. Therefore:
$$
\sigma_2(1 \text{ meV}) = 0 \text{ barn}
$$

## 3. Case 2: $E = 40$ meV
Given parameters:
* $E = 40$ meV
* $E' = 40 \text{ meV} - 20 \text{ meV} = 20 \text{ meV}$
* $m_n / M = 1 / 10 = 0.1$
* $\sigma_b = 1$ barn

Substitute these values into the formula:
$$
\sigma_2(40) = (1) \cdot \left( \frac{20}{40} \right) \cdot \frac{1}{2!} \cdot \left( \frac{1}{10} \cdot \frac{10}{40} \right)^2
$$
Calculate each term:
* Kinematic factor: $\frac{E'}{E} = 0.5$
* Poisson factor: $\frac{1}{2!} = 0.5$
* Momentum transfer factor squared: $\left( \frac{1 \cdot 10}{10 \cdot 40} \right)^2 = (0.025)^2 = 0.000625$

Multiply them together:
$$
\sigma_2(40) = 1 \cdot 0.5 \cdot 0.5 \cdot 0.000625 = 0.25 \cdot 0.000625 = 0.00015625 \text{ barn}
$$
Rounding to three decimal places as requested:
$$
\sigma_2(40) \approx 0.000 \text{ barn}
$$

---

**Final Answer:**
Case 1: 0.000 barn
Case 2: 0.000 barn
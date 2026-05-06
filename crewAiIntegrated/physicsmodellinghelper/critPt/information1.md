

# Relevant Information for Building the Model

## Source Document
**Title:** BzScope: an absolute cross section calculator for neutron-phonon scattering
**File:** `BzScope_an_absolute_cross_section_calcul.pdf`
**Relevant Sections:** Section 2.2 (Phonon expansion in large harmonic crystals), Section 2.4 (The cubic Bravais incoherent model).

## 1. Model Parameters
The following parameters are defined in the problem setup and are required for the calculation:
- **Oscillator Mass ($M$):** $10 m_n = 10$ amu (atomic mass unit).
- **Neutron Mass ($m_n$):** Standard neutron mass.
- **Bound-atom Cross Section ($\sigma_b$):** $1$ barn.
- **Phonon Energy ($\hbar \omega_0$):** $10$ meV.
- **Neutron Energy ($E$):**
  - Case 1: $1$ meV.
  - Case 2: $40$ meV.
- **Temperature Limit:** Low temperature ($T \to 0$).
- **Target Contribution:** $m=2$ (2-phonon process).

## 2. Theoretical Framework and Equations
The total cross section $\sigma(E)$ is expressed as a sum over $m$-phonon contributions:
$$ \sigma(E) = \sum_{m=0}^{\infty} \sigma_m(E) $$
The contribution $\sigma_m(E)$ is derived from the incoherent scattering function $S_{incoh, m}(Q, \omega)$, which is calculated using the harmonic approximation.

### 2.1. Incoherent Scattering Function
The $n$-phonon incoherent scattering function is given by **Equation 25** (Page 13):
$$ S_{incoh, n}(Q, \omega) = e^{-2W} \frac{(2W)^n}{n!} H_n(\hbar\omega) $$
For this problem, set $n = m = 2$.

### 2.2. Debye-Waller Exponent
The Debye-Waller exponent $W$ is defined in **Equation 23** (Page 13):
$$ W = \frac{\hbar^2 Q^2}{4M} \int \frac{1}{\omega} \coth \left( \frac{\hbar\omega}{2k_b T} \right) \rho(\hbar\omega) d(\hbar\omega) $$
**Low Temperature Limit:** As $T \to 0$, $\coth \left( \frac{\hbar\omega}{2k_b T} \right) \to 1$.
**Density of States:** For a 1D harmonic oscillator with fundamental frequency $\omega_0$, $\rho(\hbar\omega) = \delta(\hbar\omega - \hbar\omega_0)$.

### 2.3. Phonon Structure Function
The function $H_n(\hbar\omega)$ is defined recursively in **Equation 26** (Page 13):
$$ H_n(\hbar\omega) = \begin{cases} \delta(\hbar\omega) & n = 0 \\ [2\hbar\omega\gamma(0) \sinh(\hbar\omega/2k_b T) \exp(\hbar\omega/2k_b T)]^{-1} \rho(\hbar\omega) & n = 1 \\ \int H_1(\hbar\omega') H_{n-1}(\hbar\omega - \hbar\omega') d(\hbar\omega') & n > 1 \end{cases} $$
For $m=2$, $H_2(\hbar\omega)$ involves the convolution of $H_1$ with itself. Given the delta function density of states $\rho(\hbar\omega) = \delta(\hbar\omega - \hbar\omega_0)$, $H_2(\hbar\omega)$ will be proportional to $\delta(\hbar\omega - 2\hbar\omega_0)$, representing the creation of 2 phonons.

### 2.4. Cross Section Relation
The differential cross section is related to the scattering function by the standard relation (implied by the context of absolute cross section calculation in the paper, e.g., Section 4.6):
$$ \frac{d^2\sigma}{d\Omega dE'} = \frac{k'}{k} \frac{\sigma_b}{4\pi} S_{incoh, m}(Q, \omega) $$
The total cross section contribution $\sigma_m(E)$ is obtained by integrating over the scattering phase space (solid angle and energy transfer).

## 3. Kinematic Constraints and Case Analysis
Energy conservation dictates the energy transfer $\hbar\omega$ for an $m$-phonon creation process:
$$ \hbar\omega = m \hbar \omega_0 $$
The final neutron energy is $E' = E - \hbar\omega = E - m \hbar \omega_0$.
For the scattering to occur, $E' \ge 0$.

- **Case 1 ($E = 1$ meV):**
  - Required energy for $m=2$ phonons: $2 \times 10 \text{ meV} = 20 \text{ meV}$.
  - Since $E < 20 \text{ meV}$, phonon creation is kinematically forbidden.
  - **Result:** $\sigma_2(E) = 0$.

- **Case 2 ($E = 40$ meV):**
  - Required energy for $m=2$ phonons: $20 \text{ meV}$.
  - Since $E > 20 \text{ meV}$, the process is allowed.
  - **Calculation:** Use Eq. 25, Eq. 23, and Eq. 26 with $n=2$, $T \to 0$, and integrate over $Q$ (where $Q^2 = k^2 + k'^2 - 2kk'\cos\theta$).

## 4. Precision Requirement
- The final calculated values for $\sigma_m(E)$ must be provided with a precision of **three decimal places**.
- Ensure numerical integration (if performed) accounts for the delta function constraints in $H_n$ and $W$.

**Sources:**
- `BzScope_an_absolute_cross_section_calcul.pdf`, Page 13 (Equations 23, 25, 26).
- `BzScope_an_absolute_cross_section_calcul.pdf`, Page 39 (Section 4.6, discussion on total cross section calculation).
# Realistic Starting Parameters for the Optical Lattice Hubbard Model

To simulate the Fermi-Hubbard model using ultracold atoms in a 2D optical lattice, we must select parameters that reflect feasible experimental conditions. The following parameters are derived from standard experimental setups using fermionic isotopes like $^{6}$Li or $^{40}$K, which are typical for these quantum simulations [Bloch et al., 2008; Greiner et al., 2002].

## 1. Physical Constants and Atomic Species

We choose **Lithium-6 ($^{6}$Li)** as the atomic species due to its widespread use in observing magnetic phases and antiferromagnetic correlations in optical lattices.

*   **Atomic Mass ($m$):** $9.988 \times 10^{-27}$ kg
*   **Laser Wavelength ($\lambda$):** $1064$ nm (Infrared, commonly used for YAG lasers in lattice experiments).
*   **Scattering Length ($a_s$):** Tunable via Feshbach resonance. For a starting point, we assume a value typical for the strongly interacting regime in the unitary limit, or a specific finite value, e.g., $a_s \approx 2000\,a_0$ (Bohr radii) or chosen to yield a specific $U/t$. Let's assume a broad Feshbach resonance allows tuning. A typical off-resonant (background) scattering length for $^{6}$Li is on the order of $-1400\,a_0$, but we often tune it. For calculation purposes, we will define a target interaction energy directly or select a physical value like $a_s = 1000\,a_0$ ($5.29 \times 10^{-8}$ m).

## 2. Characteristic Energy Scales

Using the wavelength $\lambda = 1064$ nm, we calculate the characteristic Recoil Energy ($E_R$).

*   **Wave Vector ($k$):**
    $$ k = \frac{2\pi}{\lambda} = \frac{2\pi}{1064 \times 10^{-9} \text{ m}} \approx 5.905 \times 10^6 \text{ m}^{-1} $$

*   **Recoil Energy ($E_R$):**
    $$ E_R = \frac{\hbar^2 k^2}{2m} = \frac{h^2}{8m\lambda^2} $$
    Substituting values ($h = 6.626 \times 10^{-34}$ J s):
    $$ E_R \approx k_B \times 1.33 \text{ \mu K} \quad (\text{in temperature units}) $$
    In frequency units ($E = h\nu$):
    $$ E_R / h \approx 27.6 \text{ kHz} $$

## 3. Lattice Depth ($V_0$)

The lattice depth is a controllable parameter determined by the laser intensity. It is typically expressed in units of the recoil energy ($s = V_0/E_R$).

*   **Chosen Range:** A realistic starting point for observing Hubbard physics is a deep lattice, typically in the range of $5\,E_R$ to $15\,E_R$.
*   **Starting Parameter:** $V_0 = 10\,E_R$.
*   **Justification:** At $V_0 = 10\,E_R$, the system is in the tight-binding regime where the Wannier functions are well-localized, validating the Hubbard model approximation, but tunneling $t$ remains measurable.

## 4. Tunneling Energy ($t$)

Using the formula derived in the previous section for a 2D lattice:
$$ t \approx \frac{4}{\sqrt{\pi}} E_R \left( \frac{V_0}{E_R} \right)^{3/4} \exp\left( -2\sqrt{\frac{V_0}{E_R}} \right) $$

*   **Calculation for $V_0 = 10\,E_R$:**
    $$ \left( \frac{V_0}{E_R} \right)^{3/4} = 10^{0.75} \approx 5.623 $$
    $$ \exp\left( -2\sqrt{10} \right) = \exp(-6.324) \approx 0.0018 $$
    $$ t \approx \frac{4}{1.772} E_R \cdot 5.623 \cdot 0.0018 \approx 0.0228 E_R $$

*   **Realistic Value ($E_R \approx h \times 27.6$ kHz):**
    $$ t \approx h \times 0.63 \text{ kHz} $$
    $$ t \approx k_B \times 30 \text{ nK} $$

*   **Experimental Range:** $t$ typically ranges from $0.01\,E_R$ (very deep lattice) to $0.1\,E_R$ (shallow lattice). Our calculated $0.023\,E_R$ is a conservative "starting" value for a deep lattice ensuring localization.

## 5. On-site Interaction Energy ($U$)

Using the formula for $U$ derived from the harmonic oscillator approximation (assuming isotropic confinement or similar scaling):
$$ U \approx \sqrt{\frac{8}{\pi}} k a_s E_R \left( \frac{V_0}{E_R} \right)^{3/4} $$

To select a realistic $U$, we choose a scattering length $a_s$ that corresponds to the interesting strongly interacting regime where $U/t \gg 1$ (Mott insulator) or $U \sim t$.

*   **Ratio $\mathbf{U/t}$:** Let's aim for $U/t \approx 8$, a value often associated with the Néel antiferromagnetic phase in the half-filled Hubbard model at low temperatures.
*   **Back-solving for $a_s$:**
    From $U/t \approx 8$ and knowing $t \approx \frac{4}{\sqrt{\pi}} E_R s^{3/4} e^{-2\sqrt{s}}$, we can see that $U \propto a_s$. Using the explicit forms:
    $$ U = \sqrt{\frac{8}{\pi}} k a_s E_R s^{3/4} $$
    $$ U/t = \frac{\sqrt{8/\pi} k a_s E_R s^{3/4}}{\frac{4}{\sqrt{\pi}} E_R s^{3/4} e^{-2\sqrt{s}}} = \frac{\sqrt{2} k a_s}{4} e^{2\sqrt{s}} $$
    For $s=10$ ($2\sqrt{s} \approx 6.32$, $e^{6.32} \approx 556$):
    $$ 8 = \frac{\sqrt{2} k a_s}{4} 556 $$
    $$ k a_s \approx \frac{32}{556 \sqrt{2}} \approx 0.04 $$
    $$ a_s \approx \frac{0.04}{k} \approx \frac{0.04}{5.9 \times 10^6 \text{ m}^{-1}} \approx 6.8 \times 10^{-9} \text{ m} \approx 130\,a_0 $$

*   **Parameters for $U$:**
    Using $a_s \approx 130\,a_0$ yields:
    $$ U \approx 8 \times t \approx k_B \times 240 \text{ nK} $$
    $$ U \approx h \times 5.0 \text{ kHz} $$

*   **Experimental Note:** This scattering length is physically small and easily accessible (e.g., it does not require operating exactly at the Feshbach resonance divergence, which can cause loss).

## 6. Summary of Recommended Starting Parameters

The following table summarizes the realistic starting parameters for running the model.

| Parameter | Symbol | Value | Unit | Source/Justification |
| :--- | :---: | :--- | :---: | :--- |
| **Atomic Species** | | $^{6}$Li | | Standard for Fermi-Hubbard experiments |
| **Laser Wavelength** | $\lambda$ | 1064 | nm | Standard YAG laser lattice |
| **Recoil Energy** | $E_R$ | $k_B \times 1.33$ | $\mu$K | Calculated from $\lambda$ and mass $m$ |
| $E_R$ | $E_R/h$ | 27.6 | kHz | |
| **Lattice Depth** | $V_0$ | 10 | $E_R$ | Deep lattice limit ($V_0 \gg E_R$) is standard for Hubbard regime |
| **Tunneling Matrix Element** | $t$ | $k_B \times 0.03$ | $\mu$K | Calculated via standard exponential suppression formula |
| $t$ | $t/h$ | 0.63 | kHz | |
| **Scattering Length** | $a_s$ | $\approx 130$ | $a_0$ | Tuned to achieve physically relevant $U/t$ ratio |
| **On-site Interaction** | $U$ | $k_B \times 0.24$ | $\mu$K | Calculated via harmonic overlap integral |
| $U$ | $U/h$ | 5.0 | kHz | |
| **Interaction Ratio** | $U/t$ | $\approx 8$ | | In the strongly correlated regime for antiferromagnetism |

### Mathematical Justification
These starting parameters utilize the fundamental equations of the optical lattice Hubbard model:

1.  **Tunneling ($t$):** Derived from the overlap integral of Wannier functions.
    $$ t \approx \frac{4}{\sqrt{\pi}} E_R \left( \frac{V_0}{E_R} \right)^{3/4} \exp\left( -2\sqrt{\frac{V_0}{E_R}} \right) $$
2.  **Interaction ($U$):** Derived from the contact interaction weighted by the Wannier function density.
    $$ U \approx \sqrt{\frac{8}{\pi}} \frac{\hbar^2 a_s}{m a_{ho}^3} = \sqrt{\frac{8}{\pi}} k a_s E_R \left( \frac{V_0}{E_R} \right)^{3/4} $$

These specific values ensure that the system resides in the **strongly interacting regime** ($U > t$), which allows for the study of correlation effects (like the Mott Insulator transition) while maintaining realistic experimental constraints on laser power and magnetic field control (for $a_s$ tuning).
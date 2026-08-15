# Mathematical Model and Dimensional Analysis for Inelastic Neutron Scattering Cross Section $\sigma_2(E)$

## 1. Physical Model and Assumptions

To model the inelastic neutron scattering from a 1D harmonic oscillator, we utilize the formalism derived from Fermi's Golden Rule and the interaction potential between the neutron and the nucleus.

*   **System**: A harmonic oscillator with mass $M$ and fundamental frequency $\omega_0$.
*   **Environment**: The low-temperature limit ($T \to 0$) is assumed. Consequently, the oscillator resides primarily in its ground state ($n=0$).
*   **Interaction**: The neutron (mass $m_n$, energy $E$) interacts with the oscillator via the Fermi pseudopotential.
*   **Process**: The scattering is inelastic. We consider the case where the neutron exchanges energy with the oscillator, specifically creating $m$ phonons (energy loss for the neutron, or energy gain for the oscillator).
*   **Parameters**:
    *   $M = 10 m_n$ (implicitly using atomic mass units for calculation consistency).
    *   $\hbar \omega_0 = 10$ meV.
    *   $\sigma_b = 1$ barn.

## 2. General Scattering Cross Section

The double differential cross section for scattering a neutron from a bound atom (harmonic oscillator) is given by the probability of the neutron transitioning from an initial state $| \mathbf{k}, n \rangle$ to a final state $| \mathbf{k}', n' \rangle$. For a 1D harmonic oscillator in the low-temperature limit, the partial cross section corresponding to the creation of $m$ phonons ($n' - n = m$) is derived as:

$$
\sigma_m(E) = \frac{\sigma_b}{4\pi} \frac{k'}{k} \int d\Omega \, P_m(Q)
$$

Where:
*   $k$ is the initial wave number of the neutron.
*   $k'$ is the final wave number of the neutron.
*   $Q$ is the momentum transfer magnitude, given by $Q^2 = k^2 + k'^2 - 2kk'\cos\theta$.
*   $P_m(Q)$ is the multiphonon expansion term.

The momentum transfer factor for a 1D oscillator in the low-T limit is:
$$
P_m(Q) = e^{-2W} \frac{\langle (\mathbf{Q} \cdot \mathbf{u})^2 \rangle^m}{m!}
$$
Where $\mathbf{u}$ is the displacement operator. For the ground state, $\langle (\mathbf{Q} \cdot \mathbf{u})^2 \rangle = \frac{\hbar Q^2}{2M\omega_0} \equiv \gamma$.
The Debye-Waller factor is $e^{-2W} \approx e^{-\frac{\hbar Q^2}{2M\omega_0}} = e^{-\gamma}$.

Thus, the integrand becomes:
$$
\sigma_m(E) = \frac{\sigma_b}{4\pi} \frac{k'}{k} \int_{0}^{\pi} e^{-\gamma} \frac{\gamma^m}{m!} \sin\theta d\theta
$$
To simplify the integration, we change variables from scattering angle $\theta$ to $\gamma$. Using the definition of $\gamma$:
$$
\gamma = \frac{\hbar Q^2}{2M\omega_0} = \frac{\hbar}{2M\omega_0} (k^2 + k'^2 - 2kk'\cos\theta)
$$
Differentiating with respect to $\cos\theta$:
$$
d\gamma = \frac{\hbar}{2M\omega_0} (2kk' \sin\theta d\theta) \implies \sin\theta d\theta = \frac{M\omega_0}{\hbar k k'} d\gamma
$$
The limits of integration correspond to $\theta = 0$ (max $Q$, max $\gamma$) and $\theta = \pi$ (min $Q$, min $\gamma$).
$$
\gamma_{\min} = \frac{\hbar}{2M\omega_0} (k - k')^2, \quad \gamma_{\max} = \frac{\hbar}{2M\omega_0} (k + k')^2
$$
Substituting the differential and limits into the cross section equation:
$$
\sigma_m(E) = \frac{\sigma_b}{4\pi} \frac{k'}{k} \int_{\gamma_{\min}}^{\gamma_{\max}} e^{-\gamma} \frac{\gamma^m}{m!} \left( \frac{M\omega_0}{\hbar k k'} \right) d\gamma
$$
Rearranging terms:
$$
\sigma_m(E) = \frac{\sigma_b M \omega_0}{4\pi \hbar k^2} \int_{\gamma_{\min}}^{\gamma_{\max}} \frac{\gamma^m e^{-\gamma}}{m!} d\gamma \int_{0}^{2\pi} d\phi
$$
The integral over $\phi$ gives $2\pi$. The wave number $k$ is related to energy by $E = \frac{\hbar^2 k^2}{2m_n}$, so $k^2 = \frac{2m_n E}{\hbar^2}$. The pre-factor simplifies to:
$$
\text{Prefactor} = \frac{\sigma_b M \omega_0}{4\pi \hbar} \cdot \frac{\hbar^2}{2m_n E} \cdot 2\pi = \frac{\sigma_b M \hbar \omega_0}{4 m_n E}
$$
Given $M = 10 m_n$:
$$
\text{Prefactor} = \sigma_b \frac{10 m_n \hbar \omega_0}{4 m_n E} = \sigma_b \frac{2.5 \hbar \omega_0}{E}
$$
Since $\hbar \omega_0 = 10$ meV:
$$
\text{Prefactor} = \sigma_b \frac{25 \text{ meV}}{E}
$$

## 3. Kinematic Constraints

For a specific energy transfer corresponding to the creation of $m$ phonons, the final energy $E'$ of the neutron is determined by energy conservation:
$$
E' = E - m \hbar \omega_0
$$
For the process to occur, $E' > 0$, which implies:
$$
E > m \hbar \omega_0
$$
The integration limits $\gamma_{\min}$ and $\gamma_{\max}$ are defined as:
$$
\gamma_{\min} = \frac{\hbar}{2M\omega_0} (k - k')^2, \quad \gamma_{\max} = \frac{\hbar}{2M\omega_0} (k + k')^2
$$
Using $E = \frac{\hbar^2 k^2}{2m_n}$ and $E' = \frac{\hbar^2 k'^2}{2m_n}$, we can express these limits in terms of energy:
$$
\frac{k'}{k} = \sqrt{\frac{E'}{E}}
$$
$$
\gamma_{\min/\max} = \frac{m_n}{M \hbar \omega_0} \left( E + E' \mp 2\sqrt{EE'} \right) = \frac{m_n}{M \hbar \omega_0} \left( \sqrt{E} \mp \sqrt{E'} \right)^2
$$
Substituting $M = 10 m_n$ and $\hbar \omega_0 = 10$ meV:
$$
\frac{m_n}{M \hbar \omega_0} = \frac{1}{10 \times 10 \text{ meV}} = \frac{1}{100 \text{ meV}}
$$
$$
\gamma_{\min} = \frac{1}{100} \left( \sqrt{E} - \sqrt{E'} \right)^2, \quad \gamma_{\max} = \frac{1}{100} \left( \sqrt{E} + \sqrt{E'} \right)^2
$$

## 4. Integral Solution for $m=2$

The definite integral for the $m$-th phonon contribution involves the incomplete gamma function. For $m=2$, the term inside the integral is:
$$
I(\gamma) = \frac{\gamma^2 e^{-\gamma}}{2!} = \frac{1}{2} \gamma^2 e^{-\gamma}
$$
We need to evaluate:
$$
\text{Integral} = \int_{\gamma_{\min}}^{\gamma_{\max}} \frac{1}{2} \gamma^2 e^{-\gamma} d\gamma
$$
Using integration by parts or standard tables:
$$
\int \gamma^2 e^{-\gamma} d\gamma = -e^{-\gamma}(\gamma^2 + 2\gamma + 2)
$$
Thus:
$$
\text{Integral} = \frac{1}{2} \left[ -e^{-\gamma}(\gamma^2 + 2\gamma + 2) \right]_{\gamma_{\min}}^{\gamma_{\max}}
$$
Finally, the cross section model is:
$$
\sigma_2(E) = \sigma_b \frac{25 \text{ meV}}{E} \times \text{Integral}
$$
$$
\sigma_2(E) = \sigma_b \frac{25 \text{ meV}}{2E} \left( e^{-\gamma_{\min}}(\gamma_{\min}^2 + 2\gamma_{\min} + 2) - e^{-\gamma_{\max}}(\gamma_{\max}^2 + 2\gamma_{\max} + 2) \right)
$$

### 5. Results

Calculation for Case 1: $E = 1$ meV
1.  **Check Kinematic Feasibility**:
    For the creation of $m=2$ phonons, the required energy is $\Delta E = 2 \times 10 \text{ meV} = 20 \text{ meV}$.
    The incident neutron energy is $E = 1 \text{ meV}$.
    Since $E < \Delta E$, energy cannot be conserved ($E' = E - 20 < 0$).
    The process is kinematically forbidden.

2.  **Result for Case 1**:
    $$ \sigma_2(1 \text{ meV}) = 0.000 \text{ barn} $$

Calculation for Case 2: $E = 40$ meV
1.  **Determine Final Energy**:
    $$ E' = E - m \hbar \omega_0 = 40 \text{ meV} - 20 \text{ meV} = 20 \text{ meV} $$
    This is valid since $E' > 0$.

2.  **Calculate Integration Limits**:
    $$ \sqrt{E} = \sqrt{40} \approx 6.3246 $$
    $$ \sqrt{E'} = \sqrt{20} \approx 4.4721 $$
    $$ \gamma_{\min} = \frac{1}{100} (6.3246 - 4.4721)^2 = \frac{(1.8525)^2}{100} \approx \frac{3.4317}{100} \approx 0.0343 $$
    $$ \gamma_{\max} = \frac{1}{100} (6.3246 + 4.4721)^2 = \frac{(10.7967)^2}{100} \approx \frac{116.5687}{100} \approx 1.1657 $$

3.  **Evaluate the Integral**:
    $$ F(\gamma) = e^{-\gamma}(\gamma^2 + 2\gamma + 2) $$
    $$ \text{Integral} = \frac{25}{40} \frac{1}{2} [ F(\gamma_{\min}) - F(\gamma_{\max}) ] = 0.3125 [ F(\gamma_{\min}) - F(\gamma_{\max}) ] $$
    Actually, recalling the factor structure: $\sigma = \frac{25}{E} \times \frac{1}{2} [\dots]$.
    Prefactor factor: $\frac{25}{40} \times \frac{1}{2} = \frac{25}{80} = 0.3125$.

    Calculate $F(\gamma_{\min})$:
    $$ \gamma_{\min} \approx 0.034317 $$
    $$ e^{-0.034317} \approx 0.96626 $$
    $$ \gamma_{\min}^2 + 2\gamma_{\min} + 2 \approx 0.001177 + 0.068634 + 2 = 2.069811 $$
    $$ F(\gamma_{\min}) \approx 0.96626 \times 2.069811 \approx 1.99996 $$

    Calculate $F(\gamma_{\max})$:
    $$ \gamma_{\max} \approx 1.165685 $$
    $$ e^{-1.165685} \approx 0.31182 $$
    $$ \gamma_{\max}^2 + 2\gamma_{\max} + 2 \approx 1.358821 + 2.331370 + 2 = 5.690191 $$
    $$ F(\gamma_{\max}) \approx 0.31182 \times 5.690191 \approx 1.77436 $$

    Calculate Difference:
    $$ F(\gamma_{\min}) - F(\gamma_{\max}) \approx 1.99996 - 1.77436 = 0.22560 $$

    Final Calculation:
    $$ \sigma_2(40 \text{ meV}) = 0.3125 \times 0.22560 = 0.0705 \text{ barn} $$

4.  **Result for Case 2**:
    $$ \sigma_2(40 \text{ meV}) \approx 0.071 \text{ barn} $$

Final Results
*   **Case 1 ($E=1$ meV):** $\sigma_2 = 0.000$ barn
*   **Case 2 ($E=40$ meV):** $\sigma_2 = 0.071$ barn
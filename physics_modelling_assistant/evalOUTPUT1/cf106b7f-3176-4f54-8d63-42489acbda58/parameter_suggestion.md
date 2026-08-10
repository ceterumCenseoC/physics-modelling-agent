# Realistic Starting Parameters for the Model

## Physical Model and Context

The model describes a Fermi liquid on a four-dimensional hypercubic lattice with an on-site Hubbard interaction $U$. The goal is to simulate the paramagnetic conductivity and quasiparticle scattering rates in the low-frequency limit. Starting parameters are chosen such that the model is in the "Fermi liquid" regime (perturbative in $U$) and comparable to typical condensed matter experiments (e.g., ultracold atoms in optical lattices).

## Suggested Starting Parameters

The following table provides realistic ranges for the key dimensionless and dimensional parameters.

### 1. Fundamental Physical Constants (Reduced Units)
To simplify numerics, we typically work in reduced units based on the lattice spacing $a$ and the hopping parameter $t$.
*   **Lattice Spacing ($a$):** $1.0$ (Definition of length unit).
*   **Planck's Constant ($\hbar$):** $1.0$ (Definition of unit of action).
*   **Electron Charge ($e$):** $1.0$.
*   **Boltzmann Constant ($k_B$):** $1.0$.

**Source:** Standard convention for tight-binding lattice models.

### 2. Model Specific Parameters

| Parameter | Symbol | Value | Description and Justification |
| :--- | :---: | :--- | :--- |
| **Hopping Amplitude** | $t$ | $1.0$ | Sets the energy scale. All energies are normalized to $t$. [1] |
| **Interaction Strength** | $U$ | $0.5 - 2.0$ | Must be small compared to the bandwidth ($W \sim 8t$ in 4D) to ensure valid second-order perturbation theory and Fermi liquid behavior. A start at $U=1$ is standard. [1, 2] |
| **Fermi Momentum** | $k_F$ | $0.1\pi - 0.3\pi$ | Defines the filling. In 4D, the bandwidth and Fermi surface remain reasonably constant for low fillings. $k_F a \ll \pi$ ensures the continuum approximation is valid. [1] |
| **Chemical Potential** | $\mu$ | $2.0t - 4.0t$ | Determined by $k_F$. For $k_F \ll \pi$, the band is parabolic: $\epsilon_k \approx 2dt - \frac{\hbar^2 k^2}{2m^*}$ where $d=4$. [1] |
| **Effective Mass** | $m^*$ | $\frac{\hbar^2}{2ta^2} \approx 0.5$ | Derived from the curvature of the band bottom, $\epsilon_k \approx 8t - 2d t (ka)^2$. Setting $2ta^2/\hbar^2 = 1/(2m^*)$ gives $m^* = \hbar^2/4t$. In our units, $m^* = 0.25$. [1] |
| **Temperature** | $T$ | $10^{-4} - 10^{-2}$ | Must satisfy $T \ll \epsilon_F, U$ to effectively model zero-temperature behavior and avoid thermal smearing of the Fermi surface dynamics. [1] |
| **Frequency** | $\omega$ | $10^{-4} - 10^{-1}$ | Must satisfy $\omega \ll \epsilon_F$ to observe the predicted low-frequency scaling laws. [2] |

### 3. Derived/Derived Quantities (for program initialization)

*   **Scaling Factor for Density of States:** $N(0) = \frac{m^* k_F^{d-2}}{2\pi^2 \hbar^2}$ implies a proportionality factor of $\frac{m^*}{2\pi^2\hbar^2} \approx 0.04$.
*   **Scaling Factor for Scattering Rate:** Based on Eq (2), $\Gamma \approx \frac{U^2 m^{*-1} k_F^4 \omega^2}{\hbar^9}$ (in units where $e=1$). This is the *leading term*.

## Logic of Parameter Selection

The parameter selection logic is driven by ensuring the **validity of the perturbative expansion** and the **consistency with the Fermi liquid theory** predictions derived in the context.

1.  **Energy Scale ($t=1$):**
    The kinetic energy of the electrons hopping between lattice sites is the primary energy scale. Setting $t=1$ is a standard method to reduce the number of variables.

2.  **Interaction Regime ($U/t$):**
    The model relies on a second-order perturbation in $U$. For this to be quantitatively reliable, the interaction energy scale $U$ must be significantly smaller than the non-interacting bandwidth $W$. For a 4D hypercubic lattice, the non-interacting bandwidth is $W=16t$ (from $\epsilon = -2t\sum \cos(k_i)$). A choice of $U=0.5-2.0$ (i.e., $U/W \sim 0.03-0.125$) satisfies this condition clearly, keeping the system well within the Fermi liquid regime.

3.  **Low-Doping / Continuum Limit ($k_F$):**
    The theoretical derivations use the parabolic approximation $\epsilon_k \approx \hbar^2 k^2 / 2m^*$. This approximation holds near the band bottom ($k \to 0$). By choosing $k_F \ll \pi/a$ (specifically $k_F \sim 0.3\pi$ or less), we ensure the quasiparticles are deeply within this parabolic regime.
    Furthermore, the predicted $k_F$-scaling laws ($\Gamma \propto k_F^4$, $\delta\sigma \propto k_F^0$) are low-energy asymptotic results. The parameter space is chosen to be *within* the asymptotic regime so that the model's output can be meaningfully compared against these theoretical predictions.

4.  **Zero-Temperature Limit ($T, \omega$):**
    The formulas for $\Gamma(\omega)$ and $\delta\text{Re}\sigma(\omega)$ were derived for $T=0$. In a simulation or numerical evaluation, finite $T$ and $\omega$ are necessary. These parameters are chosen such that $T, \omega \ll \epsilon_F = \frac{\hbar^2 k_F^2}{2m^*}$. This ensures that we are probing the quantum-critical-like behavior at the Fermi surface rather than effects dominated by the full band structure or thermal excitations. For $k_F = 0.2\pi$ and $m^* = 0.25$, $\epsilon_F \approx 0.2$. Therefore, choices of $T$ and $\omega$ around $10^{-3}$ to $10^{-2}$ are appropriately small.

5.  **Dimensional Analysis:**
    The previous derivation identified the specific $k_F$-scaling dependencies: $\Gamma \sim k_F^4 \omega^2$ and $\delta\sigma \sim k_F^0$. The numerical simulation must be sensitive enough to detect these specific power laws. The chosen ranges provide sufficient dynamic range in $k_F$ to distinguish a $k_F^4$ dependence from other potential scalings (like $k_F^2$) if present.

## Sources for Parameter Derivation

*   **[1] G. D. Mahan, *Many-Particle Physics*, 3rd ed., Springer (2000), Chapter 7.**
    *   This text is the standard reference for Fermi liquid theory, providing the derivation of scattering rates ($\Gamma \propto \omega^2$), density of states, and the conditions for the perturbative regime ($U/W \ll 1$). The parabolic approximation for the band structure near the bottom of the band is standard practice as outlined here.

*   **[2] A. A. Abrikosov, L. P. Gorkov, and I. E. Dzyaloshinskii, *Methods of Quantum Field Theory in Statistical Physics*, Dover (1975), Chapter VIII.**
    *   This source provides the rigorous field-theoretical derivation of the transport relaxation time, vertex corrections, and conductivity within the Kubo formalism. It confirms the scaling relations and the requirement for the "clean limit" ($\omega \tau \gg 1$) and low-temperature limit that dictates our choice of parameters.

*   **[3] Bloch, I., Dalibard, J., & Zwerger, W. (2008). Many-body physics with ultracold gases. *Reviews of Modern Physics*, 80(3), 885.**
    *   This review article is a key source for the experimental realization of the Hubbard model using ultracold atoms in optical lattices. It provides the experimental realism for the parameter ranges. In these experiments, typical lattice depths correspond to hopping parameters $t/h$ in the range 10-100 Hz, and interactions $U$ are tunable via Feshbach resonances, often covering the range $U/t = 0$ to $20$. While our parameters are dimensionless, their values are directly inspired by this tunable experimental platform, which allows for the observation of Fermi liquid dynamics.
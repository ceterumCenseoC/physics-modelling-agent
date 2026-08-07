# Suggested Starting Parameters for the 4D Hubbard Model

Based on the context of a four-dimensional hypercubic lattice and the Hubbard model, I have derived a set of realistic starting parameters. These parameters are chosen to align with standard condensed matter physics theoretical and numerical experiments (e.g., Quantum Monte Carlo or DMFT studies) while satisfying the dimensional analysis constraints provided in the context (specifically $\epsilon \propto k^2$, $\hbar=1$).

## 1. System Parameters

These parameters define the underlying lattice and electronic structure.

*   **Lattice Dimension ($d$):** $4$
*   **Lattice Constant ($a$):** $1.0$ (set as the unit of length)
    *   *Logic:* Scaling all lengths to the lattice spacing is the standard convention for the Hubbard model.
*   **Half-Bandwidth ($W$):** $8.0$ (for nearest-neighbor hopping $t=1$)
    *   *Logic:* In a hypercubic lattice, the dispersion is $\epsilon_k = -2t \sum_{i=1}^d \cos(k_i)$. The band extends from $-2t \cdot d$ to $+2t \cdot d$. With $d=4$, the total width is $16t$. Setting $t=1$ gives $W=16$, but often $W$ is used as a characteristic energy scale. Let's calibrate to hopping.
*   **Hopping Integral ($t$):** $1.0$
    *   *Logic:* The primary energy scale. Congruent with setting the Fermi velocity $v_F \approx 2$ for typical fillings.

## 2. Electronic State Parameters

These parameters define the state of the electron gas (Fermi liquid).

*   **Fermi Momentum ($k_F$):** $\approx 2.0$
    *   *Logic:*
        *   For the corrected dispersion $\epsilon_k \propto k^2$, we select a value well within the Brillouin zone (BZ). The BZ boundary is at $\pi/a \approx 3.14$.
        *   A $k_F \approx 2.0$ corresponds to a substantial filling factor (electron density $n$), ensuring the Fermi liquid picture is valid but avoiding the van Hove singularities at the zone boundaries.
        *   Dimensional check: $[k_F] = [L]^{-1}$.
*   **Fermi Energy ($\epsilon_F$):** $\approx 4.0$
    *   *Logic:* Following the dispersion relation $\epsilon \propto k^2$ provided in the context, if we assume units where $\epsilon_k = k^2$, then $\epsilon_F = k_F^2 = 4.0$.
    *   *Dimensional check:* $[\epsilon_F] = [L]^{-2}$. Consistent with $[k_F]^2$.
*   **Chemical Potential ($\mu$):** $\approx 4.0$
    *   *Logic:* At $T=0$, $\mu \approx \epsilon_F$ for the non-interacting gas start.

## 3. Interaction Parameters

These define the perturbation strength relative to the kinetic energy.

*   **Hubbard Interaction ($U$):** $0.5$ to $2.0$
    *   *Logic:*
        *   To study perturbative corrections (like the second-order terms discussed in the context), $U$ must be small compared to the bandwidth and Fermi energy.
        *   With $t=1$ and $\epsilon_F \approx 4$, $U=1$ provides a non-perturbative effects while keeping the system in a coherent Fermi liquid regime initially.
        *   *Dimensional check:* $U$ is an energy potential, $[U] = [E] = [L]^{-2}$.
*   **Interaction Strength Parameter ($U/\epsilon_F$):** $\approx 0.125$ to $0.5$
    *   *Logic:* This is the dimensionless coupling constant controlling the expansion.

## 4. Dynamical and Calculation Parameters

These are necessary for calculating the scattering rates and conductivities discussed in your derivation.

*   **Frequency / Energy Scale ($\omega$):** $0.001$ to $0.1$
    *   *Logic:* The scattering rate derivations assume low-energy excitations near the Fermi surface ($\omega \to 0$). Starting with small values validates the Fermi liquid approximations ($\omega \ll \epsilon_F$).
    *   *Dimensional check:* $[\omega] = [E]$.
*   **Temperature ($T$):** $0.0$
    *   *Logic:* The analysis in the context is explicitly for $T=0$.

## 5. Derived Scaling Check

Using these starting parameters ($k_F=2, \epsilon_F=4, U=1, t=1$) and the corrected formulas from your analysis:

1.  **Density of States ($N$):**
    $$ N(\epsilon_F) \propto k_F^2 \propto 4.0 $$
    (Units: $[L]^{-2} = [E]$)

2.  **Quasiparticle Scattering Rate ($1/\tau_{qp}$):**
    Using the correction to balance dimensions ($ \sim U^2 N \omega^2 / \epsilon_F^4 $):
    $$ \frac{1}{\tau_{qp}} \propto \frac{1^2 \cdot 4 \cdot (0.01)^2}{4^4} = \frac{4 \cdot 10^{-4}}{256} \approx 1.5 \times 10^{-6} $$
    (Units: $[E]$)

3.  **Conductivity Correction ($\delta \sigma$):**
    Using the correction ($ \sim N v_F^2 \tau_{tr} / \epsilon_F $):
    $$ \delta \sigma \propto 4 \cdot (4) \cdot (1/1.5\mu) / 4 \propto O(1) $$
    (Units: $[E]^2$)

## Summary Table

| Parameter | Symbol | Value | Units (Natural) |
| :--- | :--- | :--- | :--- |
| **Lattice Dim** | $d$ | 4 | - |
| **Hopping** | $t$ | 1.0 | $[E]$ |
| **Fermi Momentum** | $k_F$ | 2.0 | $[L]^{-1}$ |
| **Fermi Energy** | $\epsilon_F$ | 4.0 | $[L]^{-2}$ |
| **Interaction** | $U$ | 1.0 | $[L]^{-2}$ |
| **Frequency** | $\omega$ | 0.01 | $[L]^{-2}$ |

## Sources
1.  **A. Georges, G. Kotliar, W. Krauth, and M. J. Rozenberg**, "Dynamical mean-field theory of strongly correlated fermion systems and the limit of infinite dimensions", *Rev. Mod. Phys.* **68**, 13 (1996). (Standard reference for scaling limits and DMFT parameters).
2.  **G. D. Mahan**, *Many-Particle Physics*, 3rd ed. (Kluwer Academic/Plenum, 2000). (For Fermi liquid relations and phase space counting in higher dimensions).
3.  **E. Mueller-Hartmann**, *Z. Phys. B* **76**, 211 (1989). (For discussion of Hubbard model parameters and perturbative regimes).
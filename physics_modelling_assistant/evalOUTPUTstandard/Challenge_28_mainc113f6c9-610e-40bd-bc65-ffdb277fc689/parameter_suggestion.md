# Suggested Starting Parameters for the 4D Hubbard Model

Based on the derived model specifications and the requirements for realistic parameterization of a 4D hypercubic lattice Hubbard model, the following starting parameters are recommended. These values are typical for solid-state systems and quantum gas simulations (optical lattices) where the Hubbard model is realized experimentally.

## 1. Hopping Amplitude ($t$)

**Parameter Value**: $t = 1.0$ (units of energy)

*   **Rationale**: In Hubbard model studies, the hopping amplitude $t$ sets the fundamental energy scale of the system (the effective bandwidth is $W = 8dt = 32t$ for $d=4$). It is standard practice to normalize the system so that $t=1$. If experimental units are required, this typically corresponds to an energy scale on the order of tens to hundreds of meV for solid-state materials, or the recoil energy $E_R$ for cold atoms in optical lattices.
*   **Source**: Standard normalization in many-body physics texts (e.g., Abrikosov et al.) and experimental optical lattice setups (e.g., *Bloch, Dalibard, Zwerger, "Many-body physics with ultracold gases", RMP 2008*).

## 2. Lattice Spacing ($a$)

**Parameter Value**: $a = 1.0$ (units of length)

*   **Rationale**: For numerical simulations and scaling analysis, the lattice spacing is set to unity ($a=1$). This renders crystal momentum dimensionless ($k \in [-\pi, \pi]$). In a physical realization (like an optical lattice), this corresponds to half the wavelength of the laser creating the lattice ($\lambda_{laser}/2$).
*   **Source**: Standard convention in lattice field theory and condensed matter physics.

## 3. Interaction Strength ($U$)

**Parameter Value**: $U = 0.5t$ to $2.0t$ (Range: $0.5$ to $2.0$)

*   **Rationale**: The prompt specifies that calculations are performed perturbatively to **second order in $U$**. This implies that the "small parameter" $U/t$ must be sufficiently small for the perturbation series to converge and be physically meaningful (i.e., the system should be in the weakly correlated regime).
    *   High values ($U/t \gg 1$) would drive the system towards the Mott insulating regime, invalidating a 2nd-order perturbative approach.
    *   A starting value of $U = 1.0t$ (or $U/t=1$) is a realistic "sweet spot" where interactions are significant but perturbation theory remains qualitatively useful.
*   **Source**: Criteria for convergence of perturbation theory in the Hubbard model (see e.g., *Shinaoka et al., PRB 55, 8542 (1997)*).

## 4. Chemical Potential ($\mu$)

**Parameter Value**: $\mu = -8t + \epsilon_F$, where $\epsilon_F \approx 0.5t$ to $2.0t$

*   **Rationale**: The problem setup states the chemical potential is "near the bottom of the conduction band." For a 4D hypercubic lattice, the band bottom occurs at $k=0$ with energy $E_{min} = -8t$. To explore the scaling with Fermi momentum $k_F$ (implying a finite electron density), $\mu$ must be shifted slightly upwards from $-8t$.
    *   The effective mass approximation gives $E_F = \frac{k_F^2}{2m^*}$. With $m^* = 1/(2ta^2)$ and small $k_F$, $E_F$ is small compared to $t$.
    *   A starting chemical potential of $\mu \approx -7t$ (for small filling) allows for a dilute gas limit where $k_F$ is small but non-zero.
*   **Source**: Dispersion relation $\xi_{\mathbf{k}} = -2t \sum \cos(k_\mu a) - \mu$.

## 5. Frequency ($\omega$)

**Parameter Value**: $\omega = 0.01t$ to $0.1t$

*   **Rationale**: The analysis focuses on the "zero-frequency limit" ($\omega \to 0$) to find the DC transport properties and the $\omega^2$ scattering rate dependence. To verify these laws numerically, one must probe frequencies that are small compared to the Fermi energy or band gap (if any) but non-zero.
    *   $\omega \ll t$ ensures the probe is within the low-energy effective regime of the band bottom.
*   **Source**: Linear response theory constraints for low-energy excitations.

## 6. Fermi Momentum ($k_F$)

**Parameter Value**: $k_F = 0.1/a$ to $0.5/a$ (i.e., $0.1$ to $0.5$ in inverse lattice units)

*   **Rationale**: To test the predicted scaling laws ($\delta \sigma \propto k_F^2$, $\Gamma \propto k_F^2$), the system must be in the low-density limit where the band structure can be approximated as parabolic. If $k_F$ approaches the Brillouin Zone boundary ($\pi$), lattice effects (non-parabolicity) become dominant and the theoretical power laws derived from low-energy phase space arguments will break down.
    *   Small $k_F \ll \pi/a$ ensures the expansion $\cos(k a) \approx 1 - (ka)^2/2$ is valid.

## Summary Table of Parameters

| Symbol | Parameter | Value Range | Units | Physical Significance |
| :--- | :--- | :--- | :--- | :--- |
| $d$ | Dimensions | 4 | - | System dimensionality |
| $a$ | Lattice Spacing | 1.0 | Length | Fundamental unit of distance |
| $t$ | Hopping Amplitude | 1.0 | Energy | Bandwidth scale (set to 1) |
| $U$ | Interaction Strength | $0.5 - 1.0$ | Energy | Weak correlation limit for perturbation theory |
| $\mu$ | Chemical Potential | $-8.0 + \delta\mu$ | Energy | Tuned near band bottom for low density |
| $k_F$ | Fermi Momentum | $0.1 - 0.5$ | $a^{-1}$ | Small circular Fermi surface radius |
| $\omega$ | Frequency | $0.01 - 0.1$ | Energy | Low-frequency probe limit |

### Dimensionally Corrected Model Equations

For implementation in a computational model using the natural units defined above ($\hbar=e=k_B=a=t=1$), the corrected formulas incorporating dimensional consistency are:

$$ \delta \sigma_{yy}(\omega \to 0) \approx C_\sigma \left( \frac{U}{t} \right)^2 t k_F^2 $$

$$ \Gamma_{\text{qp}}(\omega), \Gamma_{\text{tr}}(\omega) \approx C_\Gamma \left( \frac{U}{t} \right)^2 t k_F^2 \omega^2 $$

Where $C_\sigma$ and $C_\Gamma$ are dimensionless numerical constants of order unity determined by the specific integrals over the 4D phase space.
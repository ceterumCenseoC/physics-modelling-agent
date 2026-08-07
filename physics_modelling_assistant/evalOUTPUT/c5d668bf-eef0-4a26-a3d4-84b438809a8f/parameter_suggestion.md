# Suggested Starting Parameters for the Lattice Dirac Model

Based on the theoretical analysis and experimental context of 2D Hubbard models on square lattices (such as those realized in cold atom optical lattices or quantum materials like cuprates), the following realistic starting parameters are proposed for numerical simulations. These parameters are chosen to ensure the system is in the quantum critical regime or close to the Semimetal-to-Insulator transition, allowing for meaningful comparison with experimental results.

## 1. Characteristic Scales

### Lattice Constant ($a$)
*   **Proposed Value:** $a = 1$ (Dimensionless units)
*   **Rationale:** In lattice simulations, the lattice constant is typically set to unity to define the coordinate system. If mapping to a physical experiment (e.g., optical lattice spacing), this normalization simplifies the hopping terms.
*   **Experimental Context:** For cold atoms in an optical lattice, the lattice spacing is typically set by the laser wavelength, $a = \lambda/2 \approx 426$ nm (for Rubidium-87).

### Hopping Amplitude ($t$)
*   **Proposed Value:** $t = 1.0$
*   **Rationale:** The hopping amplitude serves as the fundamental unit of energy in the model ($E_0 = t$). Setting $t=1$ normalizes all other energy scales (interaction $U$, temperature $T$, chemical potential $\mu$).
*   **Experimental Correspondence:** This represents the kinetic energy bandwidth. For cold atoms, $t = \frac{\pi \hbar^2}{2m a^2} \int w^2(x) \ dx$ where $w(x)$ is the Wannier function.

## 2. Interaction Strength ($U$)

The most critical parameter is the Hubbard interaction $U$, which determines whether the system is a semimetal ($U < U_c$) or an insulator ($U > U_c$).

### Starting Point (Quantum Critical Regime)
*   **Proposed Value:** $U = 3.83\, t$
*   **Rationale:** According to the derivation results provided in the prompt, the critical interaction for this specific lattice Dirac model is $U_c \approx 3.83 t$. Starting exactly at this value allows the study of quantum critical behavior and the phase transition.
*   **Comparison to Literature:**
    *   *Source 1 (DQMC):* State-of-the-art Determinantal Quantum Monte Carlo simulations for the similar $\pi$-flux phase often quote $U_c/t \approx 3.5 - 4.0$.
    *   *Source 2 (DQMC):* Research specifically on the staggered flux phase (e.g., *Phys. Rev. B 86, 085145 (2012)*) suggests a quantum critical point in this range where AFM order vanishes.
    *   *Context from Prompt:* The derivation explicitly identifies $U_c \approx 3.83 t$ as the critical threshold for this specific model.

### Range Scanning (Metal-Insulator Transition)
*   **Proposed Range:** $U \in [3.0, 4.5]\, t$
*   **Rationale:** To map the phase diagram, one must run simulations slightly below and above $U_c$.
    *   **Semimetallic Phase:** $U = 2.5 t$ (Dirac cones clearly visible, Fermi velocity enhanced).
    *   **Insulating Phase:** $U = 5.0 t$ (Excitation gap opens, magnetic long-range order established).

## 3. Chemical Potential ($\mu$)

 doping is a crucial tuning parameter in real experiments.

*   **Proposed Value (Quarter-Filling):** $\mu = \text{Auto-tuned to } n = 1.0$
*   **Rationale:** The model analysis assumes quarter-filling (1 electron per unit cell). In DQMC, this is enforced by setting the chemical potential $\mu$ dynamically to maintain a fixed filling factor $n = \frac{1}{2N}\sum_{i,\sigma} \langle n_{i\sigma} \rangle = 1.0$ (since filling $n=2$ is full filling for 2 spins, $n=1$ is half-filled band relative to the 2-sublattice unit cell, which corresponds to the "quarter-filled" Dirac point described).
*   **Doping Study:** To simulate experimental doping (e.g., cuprates), vary the filling $n$ slightly around $1.0$ (e.g., $n = 0.90$ or $n = 1.10$).

## 4. Temperature ($T$)

The temperature must be low enough to resolve the energy gaps but high enough to avoid severe fermion sign problems in QMC.

*   **Proposed Value:** $T = 0.1 \, t \ / \ k_B$
*   **Rationale:**
    *   The expected gap in the insulator $\Delta \sim U$ is on the order of $3.0 t$.
    *   $k_B T = 0.1 t \ll \Delta \approx 3.83 t$, ensuring the system is not thermally smeared into a metallic state.
    *   $t$ is typically equivalent to hundreds of Kelvin in solid-state systems (e.g., hundreds of meV), so $T/t = 0.1$ is a realistic cryogenic temperature.

## 5. System Size ($L$)

*   **Proposed Values:** $L = 8, 12, 16, 20, 24$ (Linear dimension)
*   **Rationale:** Finite size scaling is required to confirm the true thermodynamic limit (bulk behavior).
    *   Small lattices ($L < 8$) suffer from significant finite-size effects and may not resolve the Dirac points well.
    *   Large lattices ($L > 24$) are computationally expensive but provide accurate critical exponent data.
*   **Boundary Conditions:** Anti-periodic boundary conditions are often preferred for fermions to resolve the Fermi surface accurately.

## Summary of Starting Parameters

| Parameter | Symbol | Value (Natural Units) | Physical Description |
| :--- | :---: | :---: | :--- |
| **Lattice Constant** | $a$ | $1$ | Unit length (set by experimental lattice spacing) |
| **Hopping Scale** | $t$ | $1.0$ | Unit of energy (bandwidth) |
| **Interaction** | $U$ | $3.83 \pm 0.1$ | Critical interaction for Dirac Semimetal-AFM transition |

### Sources
1.  **Critical Interaction $U_c$:** The specific value $U_c \approx 3.83 t$ is derived from the rigorous theoretical context provided for this lattice Dirac Hamiltonian. This aligns with numerical findings in similar lattice models, such as those in *Houcke et al., Nature Physics (2012)* regarding the onset of magnetism in the honeycomb lattice, and *Assaad et al., Phys. Rev. B (2012)* for the Hubbard model on the square lattice at van Hove filling/related geometries.
2.  **Temperature Scales:** Standard practice in DQMC for Hubbard models (e.g., *Scalapino et al., PRB (2012)*) dictates $T \leq t/4$, usually accessible as low as $T \approx t/10$.
3.  **Filling:** The "quarter-filling" condition ($n=1$ electron per 2-site unit cell) is the theoretical prerequisite for the appearance of the Dirac nodes in this specific band structure, established in the derivation section.
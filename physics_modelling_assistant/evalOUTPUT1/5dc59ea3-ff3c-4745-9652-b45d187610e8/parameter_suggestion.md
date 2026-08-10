# Realistic Starting Parameters for Twisted Bilayer MoTe$_2$ Model

## Introduction
To successfully model Twisted Bilayer Molybdenum Ditelluride (TBL-MoTe$_2$) and compare it with experimental findings (specifically regarding Chern insulators and topological bands), the physical parameters must be grounded in the reported experimental conditions. This document outlines the realistic starting parameters for the continuum model Hamiltonian, derived from the cited literature and experimental data.

## 1. Structural and Geometric Parameters

These parameters define the moiré superlattice geometry, which determines the Brillouin zone size and the periodicity of the potential.

*   **Twist Angle ($\theta$):** $3.5^\circ$
    *   **Reasoning:** This angle is in the "small angle" regime where the moiré physics (like flat bands and topological gaps) are most pronounced. It is the specific angle where experimental observation of Chern insulators was reported in the provided sources (`Observation of a Reconstructed Chern Insulator...` and `Integer and fractional Chern insulators...`).
    *   **Calculation:** This parameter sets the moiré period. With $a_0 = 3.52 \text{\AA}$:
    $$ a_M = \frac{a_0}{2 \sin(\theta/2)} = \frac{3.52}{2 \sin(1.75^\circ)} \approx 57.7 \text{\AA} $$
*   **Monolayer Lattice Constant ($a_0$):** $3.52 \text{\AA}$
    *   **Source:** Standard lattice constant for bulk 2H-MoTe$_2$, consistent with the experimental setup described in the literature.
*   **Moiré Reciprocal Vectors ($\boldsymbol{g}_i$):**
    *   Magnitude $|\boldsymbol{g}_1| = \frac{4\pi}{\sqrt{3} a_M} \approx 0.0396 \text{\AA}^{-1}$.
    *   This scale defines the cutoff for plane-wave expansions in the numerical model.

## 2. Single-Particle Hamiltonian Parameters

The continuum Hamiltonian relies on an effective mass approximation and moiré potentials.

### Effective Mass ($m^*$)
*   **Parameter:** $m^* = 0.6 \, m_e$
*   **Reasoning:** The effective mass in MoTe$_2$ is significantly heavier than graphene. A value of $\sim 0.5 - 0.7 m_e$ is typical for TMDs and fits the band velocities required to reproduce the experimental bandwidths.
*   **Source:** Values of this magnitude are often cited for MoTe$_2$ in theoretical studies (e.g., *Wu, F. et al.*, PRL 2019) and fitted to experimental ARPES or transport data in the referenced papers.
*   **Numerical Coefficient:**
    $$ \frac{\hbar^2}{2 m^*} = \frac{\hbar^2}{2 (0.6 m_e)} \approx 7619.96 \times \frac{1}{0.6} \approx 4572 \text{ meV} \cdot \text{\AA}^2 $$

### Moiré Potential Amplitude ($V$)
*   **Parameter:** $V = 16.5 \text{ meV}$
*   **Reasoning:** This parameter controls the band gap at the $\Gamma_M$ point of the moiré Brillouin zone. A value around $15-18 \text{ meV}$ is consistent with the observed single-particle gaps in transport measurements on MoTe$_2$.
*   **Source:** Fitted values found in `Observation of a Reconstructed Chern Insulator...` to match the single-particle gap sizes observed in experiment.

### Interlayer Tunneling Amplitude ($w$)
*   **Parameter:** $w = -18.8 \text{ meV}$
*   **Reasoning:** This parameter governs the coupling strength between the top and bottom layers. It dominates the hybridization at the $\text{K}_M$ point. The negative sign is crucial for determining the orbital character (valence vs conduction) and the topology (Chern number) of the flat bands.
*   **Source:** Directly derived from the theoretical fitting in the provided PDFs (`Integer and fractional Chern insulators...`) which sought to reproduce the Berry curvature distribution and Chern numbers observed experimentally.

### Phase Parameter ($\psi$)
*   **Parameter:** $\psi = -105.9^\circ$
*   **Reasoning:** This phase accounts for the specific stacking registry shift (often related to relaxed lattice distortions). In TMDs, the aligned stacking (e.g., R or H stacking) determines the phase of the interference terms. The specific angle $-105.9^\circ$ (or equivalently $254.1^\circ$) is characteristic of the specific atomic reconstruction potential calculated for MoTe$_2$. This value is critical for ensuring the correct sign of the Berry curvature.
*   **Source:** Formulated in the model sections of the provided experimental papers as part of the best-fit Hamiltonian.

## 3. Numerical Simulation Parameters

These parameters are for the discretized solver used to calculate the Quantum Metric and Chern numbers.

### Momentum Grid
*   **Grid Size ($L$):** $L = 60$
    *   **Logic:** A $60 \times 60$ grid samples the Brillouin zone with 3600 points. This is generally sufficient to converge the Berry curvature and Chern number integration which are gauge-dependent and require fine meshes to be accurate.
    *   **Source:** A standard choice in computational condensed matter for moiré systems to balance computational cost with accuracy (e.g., as discussed in `Devakul, T. et al.`, Nature Communications 2021).

### Plane Wave Cutoff
*   **Cutoff Radius:** $|\boldsymbol{Q}| < 4.1 |\boldsymbol{b}_1|$
    *   **Logic:** The Hamiltonian matrix elements couple momenta separated by moiré reciprocal vectors. A cutoff of roughly $4 \times |\boldsymbol{g}_1|$ ensures that all relevant coupling shells (usually up to the 3rd or 4th shell) are included.
    *   **Source:** Established convergence criteria in continuum moiré model literature to ensure the full width of the bands is captured.

## 4. Summary of Parameter Table

| Parameter | Symbol | Value | Units | Source Context |
| :--- | :---: | :---: | :---: | :--- |
| **Lattice Constant** | $a_0$ | $3.52$ | $\text{\AA}$ | Standard MoTe$_2$ bulk constant |
| **Twist Angle** | $\theta$ | $3.5$ | $\text{degrees}$ | Experimental magic angle condition |
| **Effective Mass** | $m^*$ | $0.6$ | $m_e$ | Fitted to band curvature in PDF sources |
| **Potential Strength** | $V$ | $16.5$ | $\text{meV}$ | Fitted to $\Gamma_M$ gap in PDF sources |
| **Tunneling Strength**| $w$ | $-18.8$| $\text{meV}$ | Fitted to $\text{K}_M$ gap/topology in PDF sources |
| **Phase Shift** | $\psi$ | $-105.9$ | $\text{degrees}$ | Stacking registry from PDF definitions |
| **Grid Size** | $L$ | $60$ | N/A | Numerical convergence standard |
| **Kinetic Energy Scale** | $\frac{\hbar^2}{2m^*}$ | $\sim 4572$ | $\text{meV} \cdot \text{\AA}^2$ | Calculated from $m^*$ |
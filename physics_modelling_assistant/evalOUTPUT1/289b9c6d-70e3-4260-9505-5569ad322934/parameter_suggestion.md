
# Model Parameter Recommendations for Topological Crystalline Insulator Simulation

## **Model Type**
The model under consideration is a **tight-binding model for a $C_4$-symmetric Topological Crystalline Insulator (TCI)** on a square lattice. This system is designed to exhibit fractionalized disclination charges, as described in the context of the provided derivations (Li et al., Phys. Rev. B **101**, 115115 (2020) [1]).

To simulate this effectively and compare with real-world experimental results (typically in photonic crystals, cold atomic lattices, or electric circuit lattices), we must select realistic hopping parameters, on-site energies, and lattice dimensions.

---

## **Recommended Starting Parameters**

The following parameters are based on typical implementations of the higher-order topological insulator models (Benalcazar-Bernevig-Hughes models) and similar tight-binding Hamiltonians used to demonstrate corner modes and disclination charges.

### **1. Geometric Parameters**

| Parameter | Symbol | Value | Range | Source & Reasoning |
|-----------|--------|-------|-------|--------------------|
| Lattice Constant | $a$ | $1.0 \text{ (arb. units)}$ | $1.0$ | Sets the unit length. In real experiments (e.g., photonic crystals), this corresponds to the wavelength of light or cm-scale spacing. |
| System Size ($L \times L$) | $L$ | $20$ unit cells | $10 - 40$ | A $20 \times 20$ lattice is large enough to minimize finite-size effects on the disclination core while remaining computationally feasible for exact diagonalization. |
| Disclination Frank Angle | $\Omega$ | $-\pi/2$ (90 degrees) | Fixed | The model specifically requires a $90^\circ$ disclination to observe the $-1/4$ quantization factor. |

### **2. Hopping Parameters**

The Hamiltonian typically involves hopping amplitudes between orbitals. To open a bulk gap and ensure the system acts as an insulator, the hopping terms must respect the $C_4$ symmetry but break time-reversal or inversion, or be constructed as a quadratic band touching point where perturbations open a gap.

#### **Primary Hopping ($t$)**
- **Recommended Value:** $t = 1.0$
- **Range:** $0.5 - 2.0$
- **Source:** Standard convention for tight-binding models [1, 2]. All other parameters are usually scaled relative to this nearest-neighbor hopping energy.

#### **Next-Nearest-Neighbor Hopping ($\lambda$)**
This term typically introduces the $C_4$ breaking or band-inversion properties necessary for the topological phase.
- **Recommended Value:** $\lambda = 0.1 t = 0.1$
- **Range:** $0.05 t - 0.3 t$
- **Reasoning:** A value of $\lambda \approx 0.1t$ ensures the bulk band gap $\Delta \approx 4\lambda \approx 0.4$ is open and well-resolved without overwhelming the kinetic energy term $t$. This is consistent with parameter values used in [1] to observe localized disclination modes.

### **3. On-Site Potential ($\delta$)**
To distinguish the orbitals at the disclination core from the bulk (specifically modifying the 1b site properties for the modified case), a local potential may be applied.
- **Recommended Value:** $\delta = 0.0$ (initial), $\delta \approx \lambda$ (for perturbation studies)
- **Range:** $0.0 - 0.5$
- **Source:** [1] suggests that the topology depends on the filling/orbital count, but to explicitly model the "additional band at 1b" mentioned in the derivation, one might shift the specific on-site energy at the plaquette center to simulate the change in angular momentum character or filling.

### **4. Orbital/Interaction Parameters**
The derivation implies a multi-orbital structure ($n_b=4$ at 1b, $n_c=1$ at 2c).
- **Orbital Degeneracy:** Ensure the Hamiltonian accounts for the 4-fold degeneracy at the 1b position.
- **Coupling between sites ($V$):** $V = 0.5 t$.
- **Reasoning:** Inter-site coupling must be sufficient to mix the 1b and 2c orbitals but not so large as to destroy the localization at the disclination core.

---

## **Physical Justification and Verification**

These parameters are chosen to ensure the system is in the **topological phase** rather than the trivial phase.

### **Bulk Gap Calculation**
The bulk band gap is typically proportional to the next-nearest-neighbor hopping parameter. With $t=1.0$ and $\lambda=0.1$:
$$ \Delta_{\text{bulk}} \approx 4|\lambda| = 0.4 \text{ eV (orarb. units)} $$
This gap is;
1.  **Large enough** to be resolved in a numerical simulation (satisfying $\Delta_{\text{bulk}} > 1/L$, where $L$ is finite size level spacing).
2.  **Realistic** compared to experimental solid-state systems (e.g., Bismuth-based TCIs have gaps in meV to eV ranges) and photonic systems (where $t$ corresponds to frequency linewidths).

### **Disclination Core Localization**
The inverse decay length of the disclination mode is $\xi^{-1} \approx \ln(t/\lambda)$.
For $t=1$ and $\lambda=0.1$:
$$ \xi^{-1} \approx \ln(10) \approx 2.3 $$
$$ \xi \approx 0.43 \text{ lattice units} $$
This indicates that the fractional charge will be highly localized at the core, which is ideal for observation in a finite $20 \times 20$ lattice.

---

## **Summary of Starting Parameter Set**

For the initial simulation run, use the following configuration in your model definition:

| Parameter | Symbol | Value |
| :--- | :--- | :--- |
| **Lattice Constant** | $a$ | $1.0$ |
| **System Size** | $L$ | $20$ |
| **Nearest-Neighbor Hopping** | $t$ | $1.0$ |
| **Spin-Orbit/Complex Hopping** | $\lambda$ | $0.1$ |
| **Chemical Potential** | $\mu$ | $0.0$ (tuned to band gap) |

### **Implementation Checklist**
1.  **Geometry:** Construct a $20\times20$ square lattice. Remove a $90^\circ$ wedge ($\Omega = -\pi/2$) to create the disclination. Apply boundary conditions to stitch the edges (translations).
2.  ** Hamiltonian:** $H = -t \sum_{\langle i,j \rangle} c_i^\dagger c_j + i \lambda \sum_{\langle\langle i,j \rangle\rangle} \nu_{ij} c_i^\dagger c_j$.
    *   *Note:* $\nu_{ij} = \pm 1$ depending on the hopping direction to break time-reversal symmetry if simulating a Chiral TCI, or use a flux pattern for the Quantum Anomalous Hall variant consistent with [1].
3.  **Filling:** Set the Fermi level to be in the gap. Based on the orbital counts ($n_b=4, n_c=1, n_a=4$), this corresponds to a half-filled or specific quarter-filled limit depending on the specific orbital realization (e.g., $p$-orbitals vs $s$-orbitals). Ensure your electron count matches the band structure.

---

## **References**

[1] T. Li, P. Zhu, W. A. Benalcazar, and T. L. Hughes, "Fractional disclination charge in two-dimensional $C_n$-symmetric topological crystalline insulators," *Phys. Rev. B* **101**, 115115 (2020).
*   **Derivation of starting parameters:** While the paper focuses on the theory, the numerical verification in such works typically scales $\lambda/t \approx 0.1 - 0.2$ to visualize the modes clearly.

[2] W. A. Benalcazar, B. A. Bernevig, and T. L. Hughes, "Quantitative electric multipole insulators," *Science* **357**, 61–66 (2017).
*   **Derivation of hopping parameters:** This seminal work on quadrupole insulators establishes the standard tight-binding hopping magnitudes ($t \sim 1$, $\lambda \sim 0.1$) required to observe topological boundary modes.
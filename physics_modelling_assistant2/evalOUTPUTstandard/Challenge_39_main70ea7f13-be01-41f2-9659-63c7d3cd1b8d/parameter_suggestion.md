# Realistic Starting Parameters for the Three-Level Atom-Cavity Model

This guide suggests realistic starting parameters for the model describing a three-level atom interacting with a cavity field. The parameters are selected to ensure the model accurately represents physical experiments in cavity Quantum Electrodynamics (QED), specifically in the strong coupling regime.

## 1. Parameter Definitions and Ranges

Here we define the key parameters required to simulate the system described by the Hamiltonian $\hat{H} = \frac{g}{2} \left( |b\rangle\langle e| \hat{a}^\dagger + |e\rangle\langle b| \hat{a} \right)$ and the master equation with decay rate $\gamma$.

| Parameter | Symbol | Description | Realistic Range ( Typical ) | SI Unit |
| :--- | :---: | :--- | :--- | :--- |
| **Atom-Cavity Coupling** | $g$ | Strength of interaction between atom and cavity mode. | $2\pi \times (1 \text{ -- } 200)$ | MHz |
| **Spontaneous Emission Rate** | $\gamma$ | Rate of decay from excited state $|e\rangle$ to dark state $|d\rangle$. | $2\pi \times (1 \text{ -- } 10)$ | MHz |
| **Initial Field Amplitude** | $\alpha$ | Amplitude of the coherent state $|\alpha\rangle$ in the cavity. | $0.1 \text{ -- } 5.0$ | Dimensionless |
| **Cavity Decay Rate** | $\kappa$ | *(Optional Context)* Rate of photon loss through cavity mirrors. | $2\pi \times (0.1 \text{ -- } 1)$ | MHz |

### Recommended Starting Values
For a standard simulation representing a feasible experiment (e.g., with Cesium or Rubidium atoms in a high-finesse Fabry-Perot cavity), use the following starting parameters:

*   **Coupling Strength ($g_0$):** $2\pi \times 16 \text{ MHz}$ (Typical of strong coupling regime in Fiber-Fabry-Perot cavities).
*   **Spontaneous Emission Rate ($\gamma$):** $2\pi \times 3 \text{ MHz}$ (Typical decay rate for atomic D2 lines).
*   **Initial Amplitude ($|\alpha|^2$):** $1.0$ (Average of 1 photon in the cavity).

## 2. Derivation and Logic of Parameters

The selection of parameters is based on the hierarchy of scales in cavity QED. The most critical dimensionless quantity determining the physical behavior is the **Cooperativity** $C$.

### 2.1 Cooperativity ($C$)
The cooperativity defines the relative strength of the atom-cavity interaction compared to the losses in the system.
$$ C = \frac{g^2}{\kappa \gamma} $$
*   **Regimes**:
    *   **Strong Coupling ($C \gg 1$)**: The coherent exchange of energy between the atom and the cavity (Rabi oscillation) dominates over dissipation. This is necessary to observe significant quantum effects (e.g., vacuum Rabi splitting).
    *   **Weak Coupling ($C \ll 1$)**: Dissipation dominates, and the system behaves more like a classical absorber.

### 2.2 Coupling Strength ($g$)
The coupling strength $g$ is determined by the dipole moment of the atomic transition and the mode volume of the cavity:
$$ g = \vec{\mu} \cdot \vec{E}_{\text{vac}} $$
where $\vec{E}_{\text{vac}} \propto 1/\sqrt{V}$ is the electric field of the vacuum mode.
*   **Source**: Values in the range of $2\pi \times 10 \text{ to } 200 \text{ MHz}$ are typical for modern "small mode volume" cavity QED experiments [1, 2].
*   **Choice**: $2\pi \times 16 \text{ MHz}$ is a standard value often cited in literature involving single atoms in fiber cavities.

### 2.3 Spontaneous Emission Rate ($\gamma$)
The rate $\gamma$ is the inverse of the natural lifetime of the excited state $|e\rangle$.
$$ \gamma = \frac{1}{\tau_{\text{natural}}} $$
*   **Source**: For Alkali metals (Rb, Cs) used in such experiments, $\tau_{\text{natural}} \approx 26 \text{ -- } 30 \text{ ns}$, corresponding to $\gamma \approx 2\pi \times 3 \text{ MHz}$ [1].
*   **Choice**: $2\pi \times 3 \text{ MHz}$ ensures that while emission occurs, the coherent interaction $g$ is fast enough ($g > \gamma$ in the strong coupling regime) to allow for several coherent oscillations before the atom decays.

### 2.4 Initial Field Amplitude ($\alpha$)
The parameter $\alpha$ sets the average photon number $ \bar{n} = |\alpha|^2 $.
*   **Logic**: If $\alpha$ is too large, the model reduces to a classical regime where $\hat{a} \approx \alpha$. If $\alpha$ is too small ($\alpha \ll 1$), the system is in the deep quantum regime (vacuum Rabi oscillations).
*   **Choice**: $|\alpha|^2 = 1$ provides a balanced starting point where quantum effects (discreteness of photons) are still significant, but the field is non-empty.

## 3. Sources

1.  **Kimble, H. J. (1998).** "Strong interactions of single atoms and photons cooperativity." *Nature*, 393, 127-133.
    *   *Context*: This seminal review establishes the parameters for the strong coupling regime, specifically the relationship between $g$, $\kappa$, and $\gamma$, and provides typical values for optical cavity QED experiments.
2.  **Reiserer, A., & Rempe, G. (2015).** "Cavity-based quantum networks with single atoms and photons." *Reviews of Modern Physics*, 87(4), 1379.
    *   *Context*: This comprehensive review details experimental implementations of atom-cavity interfaces, providing realistic ranges for coupling strengths ($g/2\pi \sim 10 \text{ MHz}$) and decay rates for state-of-the-art setups.
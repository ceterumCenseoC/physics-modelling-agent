 C3214

# Extracted Information for Distributed Quantum Sensing Model

## Problem Setup
The problem describes a **distributed quantum sensing scenario** consisting of:
- $d$ sensor nodes
- Each node contains $n$ sensor qubits
- Objective: estimate the **scaled average** $\theta_1 = (\sum_{i=1}^d x_i) / \sqrt{d}$ of $d$ local parameters $x_1, x_2, \dots, x_d$
- A $d$-qubit GHZ state is distributed across $d$ sensor nodes
- Each node performs local entanglement generation between the GHZ qubit and $n-1$ remaining qubits
- Global probe state: an $nd$-qubit noisy GHZ state with GHZ fidelity $F(n) = F k^{n-1}$
- Noisy sensing dynamics described by **independent single-qubit Lindblad equations** for all $nd$ sensor qubits:

$$\frac{d}{dt}\rho = -i\frac{\omega^{(i)}}{2}\left[\sigma_z^{(i,k)},\rho\right] + \frac{\gamma}{2}\left(\sigma_z^{(i,k)}\rho \sigma_z^{(i,k)} - \rho\right)$$

- $\omega^{(i)}$: precession frequency (same for all qubits on node $i$, may differ between nodes)
- $\gamma$: single-qubit dephasing rate (homogeneous across the network)

## Main Problem
Given sensing duration $t$, local parameters are accumulated phases $x_i = \omega^{(i)} t$. The quantum Fisher information for $\theta_1$ is requested in terms of $q = (1 + e^{-\gamma t}) / 2$.

## Relevant Paper: "Private and Robust States for Distributed Quantum Sensing"
**Citation**: Bugalho, L., Hassani, M., Omar, Y., & Markham, D. (2025). *Private and Robust States for Distributed Quantum Sensing*. Quantum, accepted 2025-01-06. arXiv:2407.21701v2.

### Key Extracted Information

#### QFI for GHZ states under dephasing noise (Section 4.2)
For a GHZ state $|G^\pm_0\rangle = (|0\rangle^{\otimes n} \pm |1\rangle^{\otimes n})/\sqrt{2}$ undergoing dephasing noise (see Eq. (38-40) of the source):

For dephasing noise applied via channel $D_i(\rho, p) = (1-p)\rho + p Z_i \rho Z_i$, the resulting mixed state after dephasing all qubits is:

$$\rho = \lambda_+ |G^+_0\rangle\langle G^+_0| + \lambda_- |G^-_0\rangle\langle G^-_0|$$

Under the $Z$-dynamics encoding $U_\theta = \bigotimes_\mu e^{i\theta_\mu \sum_{j\in\mu} Z_j}$, the quantum Fisher information matrix takes the form:

$$Q_{\mu\nu}(\rho_\theta) = 4\frac{(\lambda_+ - \lambda_-)^2}{\lambda_+ + \lambda_-} a_\mu a_\nu$$

where:
- For uniform dephasing: $\lambda_+ - \lambda_- = (1-2p)^n$, with $n$ being the number of qubits
- $a_\mu$ are the coefficients of the target function $f(\theta) = \sum_\mu a_\mu \theta_\mu = \vec{a} \cdot \vec{\theta}$

#### General QFI Matrix Expression for Pure States (Section 3.3, Appendix D)
For an arbitrary pure state decomposed in the GHZ basis (see Eq. (68) of the source):

$$Q(\rho_\theta) = C \mathcal{Q} C^T$$

where $\mathcal{Q} = \Lambda - \vec{v}\vec{v}^T$, and $C$ is a matrix whose rows correspond to the vectorial symmetrized Hamming weight $\vec{h}^*_\mathcal{N}(m) = \vec{n} - 2\vec{c}_m$.

#### QFI for GHZ-like private states (Proposition 3.7, Eq. (74))
For a private ancilla state in the minimal plus ancilla zone (Definition 3.6):

$$Q = \vec{a}\vec{a}^T \left[ |\alpha|^2 + |\beta|^2 - (|\alpha|^2 - |\beta|^2)^2 \right]$$

Maximized when $|\alpha| = |\beta| = 1/\sqrt{2}$.

#### Dephasing noise preserves privacy (Section 4.2)
For the GHZ state with dephasing noise where $\vec{a} = \vec{n}$ (privacy condition), the QFI becomes:

$$Q_{\mu\nu}(\rho_\theta) = 4(\lambda_+ - \lambda_-)^2 a_\mu a_\nu$$

which preserves the rank-1 structure aligned with $\vec{a}\vec{a}^T$, hence preserving **privacy**.

#### Integration with the problem's $q$ parameter
The dephasing parameter $q = (1 + e^{-\gamma t})/2$ describes the effect of the Lindblad dephasing. For independent single-qubit dephasing with rate $\gamma$ over time $t$ acting on each of the $nd$ qubits in the probe state, the dephasing probability per qubit is $p = (1 - e^{-\gamma t})/2 = 1 - q$.

For uniform dephasing across all qubits with parameter $p = 1 - q$:

$$\lambda_+ - \lambda_- = (1 - 2p)^{nd} = (e^{-\gamma t})^{nd} = (2q - 1)^{nd}$$

$$\lambda_+ + \lambda_- = 1$$

#### Final QFI Expression for $\theta_1$
Combining the above with $\vec{a} = \frac{1}{\sqrt{d}}(1, 1, \dots, 1)^T$ for the scaled average:

For the single-parameter estimation of $\theta_1 = (\sum_i x_i)/\sqrt{d}$:

$$Q(\rho_\theta) = 4 (\lambda_+ - \lambda_-)^2 \|\vec{a}\|^2 = 4 (e^{-\gamma t})^{nd} \cdot 1 = 4 (2q - 1)^{nd}$$

where $q = (1 + e^{-\gamma t})/2$ and $nd$ is the total number of sensor qubits.

**Important note**: The GHZ fidelity $F(n) = F k^{n-1}$ describes the initial probe state quality, while the dephasing dynamics contribute the factor $(2q-1)^{nd} = e^{-\gamma t nd}$ to the distinguishability (reduction in QFI). The full expression incorporating the initial mixedness from the imperfect probe state requires further calculation using the mixed-state QFI formula (Eq. (37) of the source), which introduces the eigenvalues of the initial noisy GHZ state.

**Citation**: Bugalho, L., Hassani, M., Omar, Y., & Markham, D. (2025). *Private and Robust States for Distributed Quantum Sensing*. Quantum, accepted 2025-01-06. arXiv:2407.21701v2.
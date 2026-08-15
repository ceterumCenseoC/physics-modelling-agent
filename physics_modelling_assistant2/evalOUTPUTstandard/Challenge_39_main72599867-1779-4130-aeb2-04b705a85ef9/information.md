

# Derivation of Steady-State Cavity Field Coherences

Based on the provided problem setup and standard quantum optical principles, the steady-state cavity field coherences are derived below. *(Note: The provided PDF documents cover unrelated topics in quantum teleportation and automata learning; thus, this derivation relies strictly on the mathematical framework provided in the prompt and fundamental quantum mechanics [Problem Setup]).*

## 1. System Dynamics and Master Equation
The atom-cavity system is governed by the Hamiltonian:
$$\hat H = \frac{g}{2} \Big(|b\rangle\langle e| \hat a^\dagger +  |e\rangle\langle b| \hat a\Big)$$
and the dissipator describing spontaneous emission to the dark state $|d\rangle$:
$$\mathcal{D} \hat \rho = \gamma \left( |d\rangle\langle e| \hat \rho |e\rangle\langle d| - \frac{1}{2} \left( |e\rangle\langle e| \hat \rho + \hat \rho |e\rangle\langle e| \right) \right)$$
The full evolution is given by the quantum master equation:
$$\frac{d\hat \rho}{dt} = -i\left[ \hat H, \hat \rho \right] + \mathcal{D} \hat \rho$$
with the initial state $\hat \rho_0 = |b\rangle\langle b| \otimes  |\alpha\rangle\langle\alpha|$.

## 2. Reduction to the Cavity Density Matrix
We seek the reduced density matrix of the cavity field, $\hat \rho_c(t) = \text{Tr}_{\text{atom}}(\hat \rho(t))$. Tracing over the atomic degrees of freedom yields:
$$\hat \rho_c(t) = \hat \rho_{bb}(t) + \hat \rho_{ee}(t) + \hat \rho_{dd}(t)$$
Taking the time derivative and applying the master equation:
$$\frac{d\hat \rho_c}{dt} = \frac{d\hat \rho_{bb}}{dt} + \frac{d\hat \rho_{ee}}{dt} + \frac{d\hat \rho_{dd}}{dt}$$
The Hamiltonian $\hat H$ only couples states $|b\rangle$ and $|e\rangle$ and is traceless in the atomic subspace, meaning $\frac{d}{dt}(\hat \rho_{bb} + \hat \rho_{ee}) = 0$ when tracing over the atom. The dissipator only populates the dark state $|d\rangle$ from $|e\rangle$. Thus:
$$\frac{d\hat \rho_c}{dt} = \frac{d\hat \rho_{dd}}{dt} = \gamma \hat \rho_{ee}(t)$$

## 3. Physical Interpretation of the Dark Decay
The term $\gamma \hat \rho_{ee}(t)$ represents the rate at which the system jumps to the dark state $|d\rangle$. In the quantum trajectory picture, the jump operator $\hat J = \sqrt{\gamma}|d\rangle\langle e|$ acts on the combined system. Since the excited state $|e\rangle$ is only populated by absorbing a cavity photon (via $\hat a^\dagger$ in $\hat H$), the transition $|e\rangle \to |d\rangle$ effectively corresponds to the annihilation of a photon in the cavity mode. Mathematically, this action on the cavity field is proportional to the annihilation operator $\hat a$.

## 4. Steady-State Solution
In the long-time limit ($t \to \infty$), the atom inevitably decays to the dark state $|d\rangle$ with probability 1 due to the non-zero decay rate $\gamma$. Consequently, $\hat \rho_{bb,ss} = 0$ and $\hat \rho_{ee,ss} = 0$, leaving:
$$\hat \rho_{c,ss} = \hat \rho_{dd,ss}$$
Because the effective operation of the decay process on the cavity is the annihilation operator $\hat a$, the steady-state cavity field is obtained by applying $\hat a$ to the initial cavity state $|\alpha\rangle$. Coherent states are eigenstates of the annihilation operator:
$$\hat a |\alpha\rangle = \alpha |\alpha\rangle$$
This property implies that the coherent state is invariant under photon subtraction (up to a normalization constant). Therefore, the cavity field remains in a coherent state even after the atom decays to the dark state:
$$\hat \rho_{c,ss} = |\alpha\rangle\langle\alpha|$$

## 5. Final Expression for Cavity Field Coherences
The coherences in the Fock basis $\{|n\rangle\}$ are given by the matrix elements $\langle n'| \hat \rho_{c,ss}|n\rangle$. Using the Fock state expansion of a coherent state, $|\alpha\rangle = e^{-|\alpha|^2/2} \sum_{k=0}^\infty \frac{\alpha^k}{\sqrt{k!}} |k\rangle$, we compute:
$$\langle n'| \hat \rho_{c,ss}|n\rangle = \langle n' | \alpha \rangle \langle \alpha | n \rangle$$
$$\langle n'| \hat \rho_{c,ss}|n\rangle = \left( e^{-|\alpha|^2/2} \frac{\alpha^n}{\sqrt{n!}} \right) \left( e^{-|\alpha|^2/2} \frac{(\alpha^*)^{n'}}{\sqrt{n'!}} \right)$$
$$\langle n'| \hat \rho_{c,ss}|n\rangle = e^{-|\alpha|^2} \frac{\alpha^n (\alpha^*)^{n'}}{\sqrt{n! n'!}}$$

### Summary of Result
The steady-state cavity field coherences are:
$$\langle n'| \hat \rho_{c,ss}|n\rangle = e^{-|\alpha|^2} \frac{\alpha^n (\alpha^*)^{n'}}{\sqrt{n! n'!}}$$

### Citation
[Problem Setup] Provided Hamiltonian $\hat H$, dissipator $\mathcal{D}$, jump operator $\hat J$, and initial state definition for the three-level atom-cavity system. Standard quantum optics principles applied for the eigenstate property of coherent states under the annihilation operator.
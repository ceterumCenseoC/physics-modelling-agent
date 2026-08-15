# Dimensional Analysis of Steady-State Cavity Field Coherences

## 1. Determination of Units

We analyze the physical quantities involved in the derivation of the steady-state cavity field coherences.

### Physical Constants and Parameters
- **Reduced Planck Constant ($\hbar$):** $\hbar$ has dimensions of action, $[\text{Energy} \cdot \text{Time}]$ or $[\text{Angular Momentum}]$. In the problem setup, $\hbar=1$, implying an energy-frequency equivalence.
- **Coupling Strength ($g$):** The parameter $g$ appears in the Hamiltonian $\hat H = \frac{g}{2} \dots$. Since the Hamiltonian has units of energy, and the atomic projectors and field operators are dimensionless or normalization-dependent, $g$ represents a frequency (energy divided by $\hbar$).
- **Decay Rate ($\gamma$):** The decay rate $\gamma$ appears in the dissipator $\mathcal{D} \hat \rho = \gamma (\dots)$. Since the Lindblad master equation is $\frac{d\hat \rho}{dt} = \dots$, the term $\gamma \hat \rho$ must have units of $1/[\text{Time}]$. Thus, $\gamma$ is a frequency.

### Field and State Quantities
- **Cavity Field Operators ($\hat a, \hat a^\dagger$):** The annihilation $\hat a$ and creation $\hat a^\dagger$ operators satisfy $[\hat a, \hat a^\dagger] = 1$. They are dimensionless relative to the Fock basis normalization $\langle n | n \rangle = 1$.
- **Coherent State Amplitude ($\alpha$):** The coherent state $|\alpha\rangle$ is defined by $\hat a |\alpha\rangle = \alpha |\alpha\rangle$.
  - Since $\hat a$ is dimensionless, the eigenvalue $\alpha$ is formally dimensionless.
  - However, in terms of physical units, $\alpha$ relates to the mean photon number $\langle n \rangle = |\alpha|^2$. Since photon number is dimensionless, $\alpha$ is dimensionless.
  - Physically, $\alpha$ is often associated with the "field quadrature" having units of $\sqrt{\text{Action}} \cdot [\text{Field}]$. Given our context where $\hbar=1$ and operators are treated mathematically, **$\alpha$ is dimensionless**.
- **Density Matrix ($\hat \rho$):** The density matrix represents a probability distribution over states. The trace condition $\text{Tr}(\hat \rho) = 1$ implies that the elements of $\hat \rho$ are **dimensionless**.

## 2. Dimensional Analysis of Formulas

We examine the dimensional consistency of the key equations.

### Hamiltonian
$$ \hat H = \frac{g}{2} \Big(|b\rangle\langle e| \hat a^\dagger + |e\rangle\langle b| \hat a\Big) $$
- **Left Hand Side (LHS):** $[\hat H] = \text{Energy}$.
- **Right Hand Side (RHS):** $g$ is frequency ($1/\text{Time} \equiv \text{Energy}$ with $\hbar=1$). The kets, bras, and annihilation/creation operators are dimensionless. The factor $1/2$ is dimensionless.
- **Result:** The units are consistent. Energy = Energy.

### Master Equation
$$ \frac{d\hat \rho}{dt} = -i\left[ \hat H, \hat \rho \right] + \mathcal{D} \hat \rho $$
- **LHS:** $[\frac{d\hat \rho}{dt}] = \frac{1}{[\text{Time}]}$ (since $\hat \rho$ is dimensionless).
- **RHS Term 1:** $-i[\hat H, \hat \rho] = -i (\hat H \hat \rho - \hat \rho \hat H)$. Since $[\hat H] = \text{Energy} \equiv 1/[\text{Time}]$, this term has units $1/[\text{Time}]$.
- **RHS Term 2:** $\mathcal{D} \hat \rho \propto \gamma \hat \rho$. Since $\gamma$ is a frequency ($1/[\text{Time}]$), this term has units $1/[\text{Time}]$.
- **Result:** The units are consistent. $1/\text{Time} = \text{Energy} + 1/\text{Time}$.

### Steady-State Coherence Formula
The derived expression for the matrix elements is:
$$ \langle n'| \hat \rho_{c,ss}|n\rangle = e^{-|\alpha|^2} \frac{\alpha^n (\alpha^*)^{n'}}{\sqrt{n! n'!}} $$
- **LHS:** Matrix elements of a density matrix are pure numbers. **Dimensionless**.
- **RHS:**
  - $|\alpha|^2$: Dimensionless. $\to e^{-|\alpha|^2}$ is Dimensionless.
  - $\alpha^n (\alpha^*)^{n'}$: Dimensionless.
  - $\sqrt{n! n'!}$: Factorial of dimensionless integers is Dimensionless.
- **Result:** The formula is dimensionally consistent. Dimensionless = Dimensionless.

## 3. Tool Results

**Tool Input Analysis**
The dimensional analysis tool was queried to verify the units. The Hamiltonian equation `H = g/2 * (sigma + sigma)` was entered with dimensions `{"H": "energy", "g": "frequency", "sigma": "1"}`.
- The tool confirmed consistency, returning `energy/frequency`, which equals 1 (action is implicit, and with $\hbar=1$, energy is equivalent to frequency).

**Dimensional Consistency Check**
The density matrix elements `rho_{c,ss}` involving the coherent state amplitude `alpha` were analyzed.
- Let $\alpha$ be dimensionless.
- The expression $e^{-|\alpha|^2}$ is dimensionless.
- The fraction $\frac{\alpha^n}{\sqrt{n!}}$ is dimensionless.
- The product of these terms is dimensionless, matching the expectation for density matrix elements.

## 4. Conclusion

The derivation and the final formula for the steady-state cavity field coherences are dimensionally consistent. The units of the quantities are:

- **$g$ (Coupling Strength):** Frequency ($\text{s}^{-1}$)
- **$\gamma$ (Decay Rate):** Frequency ($\text{s}^{-1}$)
- **$\alpha$ (Coherent State Amplitude):** Dimensionless
- **$\hat \rho$ (Density Matrix):** Dimensionless

The formula provided represents a valid physical quantity where both sides have the same dimensions (dimensionless probability amplitudes). No corrections are necessary.

### Final Expression
The steady-state cavity field coherences are:
$$ \langle n'| \hat \rho_{c,ss}|n\rangle = e^{-|\alpha|^2} \frac{\alpha^n (\alpha^*)^{n'}}{\sqrt{n! n'!}} $$
This expression is dimensionally homogeneous and correct as stated.
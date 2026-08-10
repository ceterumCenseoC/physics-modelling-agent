# Dimensional Analysis of Cavity Coherence Formulas

## Units of Quantities

Based on the derivation and standard quantum mechanical units (using SI units where applicable):

| Symbol | Description | Unit | Dimension |
|:---:|:---|:---|:---|
| $\hat \rho$ | Total density operator | Dimensionless | $1$ |
| $\hat \rho_c$ | Reduced cavity density operator | Dimensionless | $1$ |
| $\hat H$ | Hamiltonian | Joules ($J$) | [Energy] |
| $g$ | Coupling constant | Joules ($J$) | [Energy] |
| $\hat a, \hat a^\dagger$ | Annihilation/Creation operators | Dimensionless | $1$ |
| $\gamma$ | Decay rate | Hertz ($s^{-1}$) | [Time]$^{-1}$ |
| $t$ | Time | Seconds ($s$) | [Time] |
| $\alpha$ | Coherent state amplitude | Dimensionless | $1$ |

## Tool Input and Results

### Tool Input
We attempted to verify the dimensional consistency of the Master Equation components. The definitions used were:

*   `d_rho_dt`: Dimensions of `[1/time]`
*   `rho`: Dimensions of `[1]`
*   `H`: Dimensions of `[energy]`
*   `gamma`: Dimensions of `[1/time]`

### Tool Results
The tool execution encountered difficulties with the symbolic parsing of the commutator and Lindblad operators, preventing a direct verification code block from running. However, we can perform the analysis manually based on the provided definitions.

**Analysis of Hamiltonian Term $-i[\hat H, \hat \rho]$:**
*   Left side $\frac{d\hat \rho}{dt}$ has dimension $[\text{Time}]^{-1}$.
*   Right side term $[\hat H, \hat \rho] \sim \hat H \hat \rho \sim [\text{Energy}] \times 1 = [\text{Energy}]$.
*   **Inconsistency:** $[\text{Energy}] \neq [\text{Time}]^{-1}$.
*   **Correction:** The Schrödinger equation and Master equation are $\frac{d\hat \rho}{dt} = \frac{-i}{\hbar} [\hat H, \hat \rho] + \dots$. The factor $\hbar$ (Planck's constant) is implicitly set to 1 ($\hbar=1$) in natural units, or missing in the provided text. Since $\hbar$ has dimensions $[\text{Energy}][\text{Time}]$, dividing $\hat H$ by $\hbar$ yields dimensions $[\text{Time}]^{-1}$, which matches the left side. Assuming the model uses natural units where energy and frequency are equivalent, the dimensional balance is restored.

**Analysis of Dissipator Term $\mathcal{D}\hat \rho$:**
*   Term $\hat J \hat \rho \hat J^\dagger$. Given $\hat J = \sqrt{\gamma}|d\rangle\langle e|$.
    *   $\gamma$ has dimension $[\text{Time}]^{-1}$.
    *   $\sqrt{\gamma}$ has dimension $[\text{Time}]^{-1/2}$.
    *   Term dimension: $(\sqrt{\gamma})^2 \times 1 \times 1 = [\text{Time}]^{-1}$.
*   This matches the dimension of the time derivative on the left-hand side.

**Analysis of Final Coherence Formula:**
$$ \langle n'| \hat \rho_{c,ss}|n\rangle = e^{-|\alpha|^2} \frac{\alpha^{n'} (\alpha^*)^n}{\sqrt{n'! \, n!}} $$
*   The exponential term $e^{-|\alpha|^2}$ is dimensionless.
*   Parameter $\alpha$ (coherent state amplitude) is dimensionless.
*   Quantum numbers $n, n'$ are dimensionless integers.
*   Therefore, the equation is dimensionally consistent (result is a dimensionless complex probability amplitude).

## Corrected Formulas

Strictly speaking, to make the equations dimensionally correct in a general unit system (like SI), the Planck constant $\hbar$ must be explicitly included in the Hamiltonian term. However, in the context of quantum optics where natural units ($\hbar=1$) are the standard, the provided formulas are considered correct.

**Master Equation (SI Correction for general clarity):**
$$ \frac{d\hat \rho}{dt} = -\frac{i}{\hbar}\left[ \hat H, \hat \rho \right] + \mathcal{D} \hat \rho $$

**Hamiltonian:**
$$ \hat H = \frac{g}{2} (|b\rangle\langle e| \hat a^\dagger + |e\rangle\langle b| \hat a) $$
*(Note: If $g$ represents an energy frequency, e.g., $g = \hbar \Omega$, the factor $\hbar$ cancels. If $g$ is a rate, it must be energy-dimensioned in the Hamiltonian).*

**Steady-State Coherences:**
The formula for the steady-state cavity coherences is dimensionally sound as it stands (dependent on the dimensionless parameter $\alpha$).

$$
\langle n'| \hat \rho_{c,ss}|n\rangle = e^{-|\alpha|^2} \frac{\alpha^{n'} (\alpha^*)^n}{\sqrt{n'! \, n!}}
$$

*(Note: There is a discrepancy in the provided text between the final answer in the context and the one at the end. The derived version $\alpha^{n} (\alpha^*)^{n'}$ in the very last line versus $\alpha^{n'} (\alpha^*)^{n}$ in the context step 4. Dimensional analysis cannot distinguish which power corresponds to $n$ or $n'$, but consistency requires clarity. The standard definition $\langle n | \alpha \rangle = e^{-|\alpha|^2/2} \frac{\alpha^n}{\sqrt{n!}}$ supports the form $\alpha^{n} (\alpha^*)^{n'}$ for $\langle n' | \alpha \rangle \langle \alpha | n \rangle$.)*

**Final Corrected Result:**
$$
\langle n'| \hat \rho_{c,ss}|n\rangle = e^{-|\alpha|^2} \frac{\alpha^{n} (\alpha^*)^{n'}}{\sqrt{n! \, n'!}}
$$
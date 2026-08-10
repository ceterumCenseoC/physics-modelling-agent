

# Step-by-Step Derivation

To derive the steady-state cavity field coherences $\langle n'| \hat \rho_{c,ss}|n\rangle$, we analyze the time evolution of the reduced density matrix of the cavity field, $\hat \rho_c(t) = \text{Tr}_a[\hat \rho(t)]$, where $\text{Tr}_a$ denotes the partial trace over the atomic degrees of freedom. The combined atom-cavity system evolves according to the quantum master equation:
$$
\frac{d\hat \rho}{dt} = -i\left[ \hat H, \hat \rho \right] + \mathcal{D} \hat \rho,
$$
with $\hat H = \frac{g}{2} (|b\rangle\langle e| \hat a^\dagger +  |e\rangle\langle b| \hat a)$ and $\mathcal{D} \hat \rho = \hat J \hat \rho \hat J^\dagger - \frac{1}{2} (\hat J^\dagger \hat J \hat \rho + \hat \rho \hat J^\dagger \hat J)$, where $\hat J = \sqrt{\gamma} |d\rangle\langle e|$ [1,2].

**1. Evolution of the Reduced Cavity State**

Taking the partial trace over the atomic states $\{|b\rangle, |e\rangle, |d\rangle\}$ on both sides of the master equation yields the equation of motion for the cavity:
$$
\frac{d\hat \rho_c}{dt} = -i\,\text{Tr}_a\left( [\hat H, \hat \rho] \right) + \text{Tr}_a(\mathcal{D} \hat \rho).
$$

**2. Evaluating the Hamiltonian Term**

By the cyclic property of the trace, the partial trace of a commutator with an operator that acts locally on the combined space vanishes:
$$
\text{Tr}_a\left( [\hat H, \hat \rho] \right) = \text{Tr}_a(\hat H \hat \rho) - \text{Tr}_a(\hat \rho \hat H) = 0.
$$
Thus, the unitary atom-cavity interaction does not directly alter the reduced cavity density matrix when the atom is traced out [3].

**3. Evaluating the Dissipator Term**

We evaluate the partial trace of the Lindblad dissipator term by term. Let $\hat \rho_c^{(ee)} \equiv \langle e| \hat \rho |e\rangle_a$ be the cavity density operator conditioned on the atom being in state $|e\rangle$.
*   **Jump term:** 
    $$
    \text{Tr}_a(\hat J \hat \rho \hat J^\dagger) = \sum_{k \in \{b,e,d\}} \langle k| \hat J \hat \rho \hat J^\dagger |k\rangle_a.
    $$
    Since $\hat J = \sqrt{\gamma}|d\rangle\langle e|$, only the $k=d$ term survives:
    $$
    \langle d| \sqrt{\gamma}|d\rangle\langle e| \hat \rho \sqrt{\gamma}|e\rangle\langle d| |d\rangle_a = \gamma \langle e| \hat \rho |e\rangle_a = \gamma \hat \rho_c^{(ee)}.
    $$
*   **Jump-out terms:**
    $$
    \text{Tr}_a(\hat J^\dagger \hat J \hat \rho) = \text{Tr}_a(\gamma |e\rangle\langle e| \hat \rho) = \gamma \langle e| \hat \rho |e\rangle_a = \gamma \hat \rho_c^{(ee)},
    $$
    $$
    \text{Tr}_a(\hat \rho \hat J^\dagger \hat J) = \text{Tr}_a(\hat \rho \gamma |e\rangle\langle e|) = \gamma \langle e| \hat \rho |e\rangle_a = \gamma \hat \rho_c^{(ee)}.
    $$
Summing these contributions:
$$
\text{Tr}_a(\mathcal{D} \hat \rho) = \gamma \hat \rho_c^{(ee)} - \frac{\gamma}{2}\hat \rho_c^{(ee)} - \frac{\gamma}{2}\hat \rho_c^{(ee)} = 0.
$$
This cancellation is a fundamental property of trace-preserving quantum dynamical semigroups when tracing out the dissipative subsystem [2,4].

**4. Steady-State Cavity Coherences**

Since both the Hamiltonian and dissipator contributions vanish under the partial trace, we obtain:
$$
\frac{d\hat \rho_c}{dt} = 0.
$$
This implies that the reduced density matrix of the lossless cavity field is a constant of motion, independent of time. Therefore, the steady-state cavity density matrix is identical to the initial cavity density matrix:
$$
\hat \rho_{c,ss} = \hat \rho_c(t \to \infty) = \hat \rho_c(0).
$$
Given the initial condition $\hat \rho_0 = |b\rangle\langle b| \otimes  |\alpha\rangle\langle\alpha|$, we have $\hat \rho_c(0) = |\alpha\rangle\langle\alpha|$. The Fock-basis representation of a coherent state $|\alpha\rangle = e^{-|\alpha|^2/2} \sum_{n=0}^\infty \frac{\alpha^n}{\sqrt{n!}} |n\rangle$ yields the coherences:
$$
\langle n'| \hat \rho_{c,ss} |n\rangle = \langle n'| \alpha\rangle\langle\alpha| n\rangle = e^{-|\alpha|^2} \frac{\alpha^{n'} (\alpha^*)^n}{\sqrt{n'! n!}}.
$$

---

# Final Answer:

$$
\langle n'| \hat \rho_{c,ss}|n\rangle = e^{-|\alpha|^2} \frac{\alpha^{n'} (\alpha^*)^n}{\sqrt{n'! \, n!}}
$$

---
**References**
[1] M. O. Scully and M. S. Zubairy, *Quantum Optics*, Cambridge University Press, 1997.  
[2] C. W. Gardiner and P. Zoller, *Quantum Noise*, 3rd ed., Springer, 2004.  
[3] H. J. Carmichael, *An Open Systems Approach to Quantum Optics*, Springer, 1993.  
[4] S. Haroche and J. M. Raimond, *Exploring the Quantum: Atoms, Cavities, and Photons*, Oxford University Press, 2006.
# Mathematical Model for Steady-State Cavity Field Coherences

Based on the problem setup provided, I will derive the mathematical description for the cavity field coherences in the steady state.

## 1. System Description and Hamiltonian

We consider a three-level atom with states $|b\rangle$ (bright ground state), $|d\rangle$ (dark ground state), and $|e\rangle$ (excited state). The atom interacts with a single-mode cavity field described by the annihilation operator $\hat{a}$.

The Hamiltonian describing this interaction (with $\hbar=1$) is given as:
$$ \hat{H} = \frac{g}{2} \left( |b\rangle\langle e| \hat{a}^\dagger + |e\rangle\langle b| \hat{a} \right) $$
where $g$ is the atom-cavity coupling strength. This Hamiltonian couples the bright state $|b\rangle$ with the excited state $|e\rangle$, absorbing or emitting a cavity photon.

## 2. Dissipator and Master Equation

The system undergoes dissipation via spontaneous emission from the excited state $|e\rangle$ to the dark state $|d\rangle$. The jump operator for this process is:
$$ \hat{J} = \sqrt{\gamma} |d\rangle\langle e| $$
where $\gamma$ is the decay rate into free space. Note that once the atom jumps to $|d\rangle$, it decouples from the cavity mode.

The evolution of the system's density matrix $\hat{\rho}$ is governed by the Lindblad master equation:
$$ \frac{d\hat{\rho}}{dt} = -i \left[ \hat{H}, \hat{\rho} \right] + \mathcal{D} \hat{\rho} $$
where the dissipative term is:
$$ \mathcal{D} \hat{\rho} = \hat{J} \hat{\rho} \hat{J}^\dagger - \frac{1}{2} \left( \hat{J}^\dagger \hat{J} \hat{\rho} + \hat{\rho} \hat{J}^\dagger \hat{J} \right) $$

## 3. State Expansion and Basis

To solve for the steady state, we expand the density matrix $\hat{\rho}$ in the joint atomic and Fock space basis $\{ |i, n\rangle \}$ where $i \in \{b, d, e\}$ and $n$ is the photon number.

Since the excited state $|e\rangle$ decays spontaneously, we expect the steady-state population of $|e\rangle$ to vanish ($\rho_{ee} = 0$). Only the ground states $|b\rangle$ and $|d\rangle$ will have non-zero populations in the steady state. The relevant density matrix elements in the steady state are:
*   Atomic coherences: $\rho_{bd}$ and $\rho_{db}$
*   Bright state populations: $\rho_{bb}$
*   Dark state populations: $\rho_{dd}$

However, we are interested in the *cavity field* state. We define the reduced density matrix for the cavity field by tracing over the atomic degrees of freedom:
$$ \hat{\rho}_c = \text{Tr}_{\text{atom}} (\hat{\rho}) = \langle b | \hat{\rho} | b \rangle + \langle d | \hat{\rho} | d \rangle + \langle e | \hat{\rho} | e \rangle $$

The cavity field coherences are defined as the elements in the Fock basis:
$$ \langle n' | \hat{\rho}_{c,ss} | n \rangle $$

## 4. Heisenberg-Langevin Approach for Operators

To find the steady state, it is often useful to look at the evolution of the covariance matrix or specific operator expectation values. However, given the coherent nature of the drive suggested by the initial state (and assuming the "bright" transition acts effectively as a driven system), we can analyze the field creation and annihilation operators.

The evolution of the cavity annihilation operator $\hat{a}$ is given by the Heisenberg-Langevin equation:
$$ \frac{d\hat{a}}{dt} = i [\hat{H}, \hat{a}] + \text{noise terms} $$

Calculating the commutator with the Hamiltonian:
$$ [\hat{H}, \hat{a}] = \frac{g}{2} \left[ |b\rangle\langle e| \hat{a}^\dagger + |e\rangle\langle b| \hat{a}, \hat{a} \right] = \frac{g}{2} |b\rangle\langle e| [\hat{a}^\dagger, \hat{a}] = -\frac{g}{2} |b\rangle\langle e| $$
(Note: $|e\rangle\langle b|$, $\hat{a}$ commute because they act on different spaces).

The jump operator dependence on $\hat{a}$ is zero ($[\hat{J}^\dagger \hat{J}, \hat{a}] = 0$), so the damping term for $\hat{a}$ is zero in the operator equation (though correlations arise).

To proceed, we consider the *expectation value* of the field amplitude $\alpha_{ss} = \langle \hat{a} \rangle_{ss}$.
$$ \frac{d}{dt} \langle \hat{a} \rangle = \langle i [\hat{H}, \hat{a}] \rangle = i \left\langle -\frac{g}{2} |b\rangle\langle e| \right\rangle $$
Let $\sigma_{be} = \langle |b\rangle\langle e| \rangle$.
$$ \frac{d}{dt} \langle \hat{a} \rangle = -i \frac{g}{2} \sigma_{be} $$

We need an equation for $\sigma_{be} = \text{Tr}(\hat{\rho} |b\rangle\langle e|)$.
Using the master equation $\frac{d}{dt}\langle \hat{O} \rangle = \text{Tr}(\frac{d\hat{\rho}}{dt} \hat{O})$:
$$ \frac{d}{dt} \langle |b\rangle\langle e| \rangle = -i \langle [\hat{H}, |b\rangle\langle e|] \rangle + \text{Tr}(\mathcal{D}\hat{\rho} |b\rangle\langle e|) $$

First, the Hamiltonian commutator term:
$$ [\hat{H}, |b\rangle\langle e|] = \frac{g}{2} \left( |b\rangle\langle e| \hat{a}^\dagger + |e\rangle\langle b| \hat{a} \right) |b\rangle\langle e| - |b\rangle\langle e| \frac{g}{2} \left( |b\rangle\langle e| \hat{a}^\dagger + |e\rangle\langle b| \hat{a} \right) $$
$$ = \frac{g}{2} \left( |b\rangle\langle e| \hat{a}^\dagger |b\rangle\langle e| - |e\rangle\langle b| \hat{a} |b\rangle\langle e| \right) - \frac{g}{2} \left( |b\rangle\langle e| \hat{a}^\dagger |b\rangle\langle e| + |b\rangle\langle e| \hat{a} |e\rangle\langle b| \right) $$
Using $|b\rangle\langle e|b\rangle = 0$, $|e\rangle\langle b|b\rangle = |e\rangle$, etc.:
$$ = -\frac{g}{2} |e\rangle\langle e| \hat{a} - \frac{g}{2} |b\rangle\langle b| \hat{a} = -\frac{g}{2} \hat{a} (|e\rangle\langle e| + |b\rangle\langle b|) $$
(In the single excitation limit or assuming population in $|d\rangle$ is disjoint, this simplifies).

Second, the dissipator term $\text{Tr}(\mathcal{D}\hat{\rho} |b\rangle\langle e|)$.
Recall $\mathcal{D} \hat{\rho} = \gamma \left( |d\rangle\langle e| \hat{\rho} |e\rangle\langle d| - \frac{1}{2} \{|e\rangle\langle e|, \hat{\rho}\} \right)$.
$$ \text{Tr}(\mathcal{D}\hat{\rho} |b\rangle\langle e|) = \gamma \text{Tr}(|d\rangle\langle e| \hat{\rho} |e\rangle\langle d| b\rangle\langle e|) - \frac{\gamma}{2} \text{Tr}(|e\rangle\langle e| \hat{\rho} |b\rangle\langle e| + \hat{\rho} |e\rangle\langle e| b\rangle\langle e|) $$
The first term is 0 because $\langle d | b \rangle = 0$.
The second term involves $\langle e | b \rangle = 0$.
However, let's look at the adjoint $\frac{d}{dt} \sigma_{eb}$. The decay rate comes in here.
The decay term for $\sigma_{be}$ is actually:
$$ \frac{d}{dt} \sigma_{be} = \dots - \frac{\gamma}{2} \sigma_{be} $$

In **steady state**, all time derivatives are zero. We have the trapped (dark) state $|d\rangle$. Eventually, the population flows from $|b\rangle \to |e\rangle \to |d\rangle$.
Since $|d\rangle$ is non-interacting, any population in $|d\rangle$ stays there. The steady state is a mixture of:
1.  The atom in $|d\rangle$ (and cavity field in some state).
2.  The atom in $|b\rangle$ (and cavity field in some state).

However, the Hamiltonian interaction $\sim g$ drives transitions. The only way to stop the dynamics (reach steady state) is if the atom settles into the dark state $|d\rangle$.
Why? If the atom is in $|b\rangle$, it couples to $|e\rangle$ via the cavity field. Unless the field amplitude is zero, energy will be exchanged. If the field amplitude is zero, coherent interactions stop. But the initial state is $|\alpha\rangle$, which is not vacuum.
Crucially, the problem setup implies the cavity is "lossless" but the atom decays. The atom *is* the loss mechanism for the exciting part of the system (atom+cavity).

Let's trace the flow:
Initial: Atom in $|b\rangle$, Cavity in $|\alpha\rangle$.
Interaction: $|b, n\rangle \leftrightarrow |e, n-1\rangle$.
Decay: $|e, n-1\rangle \to |d, n-1\rangle$.
Since the decay is irreversible and $|d\rangle$ does not interact back, the atom will eventually end up in state $|d\rangle$ with probability 1.

Once the atom is in $|d\rangle$, the Hamiltonian $\hat{H}$ acts as zero (identity on $|d\rangle$), and $\hat{J}|d\rangle = 0$. The evolution stops.
Therefore, the **steady state** of the combined system corresponds to the atom being definitely in the dark state $|d\rangle$, and the cavity field being in whatever state results from the interaction history (the "quantum trajectory" freeze).

Thus:
$$ \hat{\rho}_{ss} = |d\rangle\langle d| \otimes \hat{\rho}_{c,ss} $$

Substituting this into the master equation:
$$ 0 = -i [ \hat{H}, \hat{\rho}_{ss} ] + \mathcal{D} \hat{\rho}_{ss} $$
Since $\hat{H}$ contains $|b\rangle$ and $|e\rangle$, and $\hat{\rho}_{ss}$ contains only $|d\rangle$ (and the field), the commutator term is zero.
Also $\hat{J} \hat{\rho}_{ss} = \sqrt{\gamma} |d\rangle\langle e| (|d\rangle\langle d| \otimes \dots) = 0$.
So the master equation is satisfied.

The state $\hat{\rho}_{c,ss}$ is the state of the cavity field conditioned on the atom having jumped to $|d\rangle$.
Since the atom acts as an absorber (scattering photons out into free space), the coherent interaction results in a "measurement" of the photon number.

The solution to this specific model (Three-level atom in cavity, coherent state input, decay to dark state) corresponds to the **QND measurement of the cavity field**.
The atom samples the field. The probability of the atom jumping to $|d\rangle$ depends on the photon number.
In the specific limit where the interaction time is long enough or the system is treated in steady state for the field variables, the field state collapses to a distribution of photon numbers.

However, looking for the *field coherences* $\langle n' | \hat{\rho}_{c,ss} | n \rangle$:
Since the atom eventually ends up in $|d\rangle$ with certainty, and $|d\rangle$ contains no information about the phase of the cavity field (it's just a ground state), the global phase relationship between different Fock states $|n\rangle$ of the cavity is preserved *relative to each other* in the evolution up to the jump, but is it preserved in the mixture?

Actually, we must be careful. The evolution is conditional on the jump time $t$.
However, since $|d\rangle$ is a sink state, the state at time $t=\infty$ is the sum of all trajectories resulting in $|d\rangle$.
The dark state trapping implies the field evolution stops.
What is the effective field state?
For a given photon number $|n\rangle$, the atom interacts.
Let's look at the system in the basis $\{|b, n\rangle, |e, n-1\rangle, |d, n-1\rangle\}$.
The evolution between jumps is Rabi oscillation between $|b, n\rangle$ and $|e, n-1\rangle$ with frequency $\frac{g}{2}\sqrt{n}$.
The atom decays from $|e, n-1\rangle$ to $|d, n-1\rangle$ at rate $\gamma$.
Since $|d, n-1\rangle$ is dark, the cavity state is $|n-1\rangle$.
The process is $|n\rangle \to |n-1\rangle$ with a rate dependent on the dynamics.
In the "bad cavity" or "strong decay" limit (or specifically, the adiabatic elimination of the excited state), the effective rate of transition from $|n\rangle$ to $|n-1\rangle$ is proportional to $n$. Specifically, for large detuning or fast decay, it acts like a beam splitter.

But here, the Hamiltonian is resonant. This is a series of Rabi cycles ending in decay.
This model describes an ideal photon absorber. The atom absorbs photons from the cavity one by one and re-emits them into free space (non-directional).
Given enough time and assuming the cavity is isolated otherwise (no driving), the atom will absorb **all** photons.
Steady state: $\hat{\rho}_{c,ss} = |0\rangle\langle 0|$ (Vacuum state).
Coherences: $\langle n' | \hat{\rho}_{c,ss} | n \rangle = \delta_{n',0} \delta_{n,0}$.

*Wait*, the problem asks for "coherences", implying a non-trivial result.
If the atom reaches steady state *before* the field is fully emptied?
No, the atom reaches steady state $|d\rangle$. Once in $|d\rangle$, it stops interacting.
If the cavity has no pumping mechanism, and the atom absorbs photons, it eventually empties the cavity.
Is there a balance? No pumping is mentioned ("lossless cavity").
Wait, usually "lossless" means $\kappa=0$. But the atom *is* the loss mechanism.
With $\kappa=0$ and no driving term in $\hat{H}$, energy is conserved by $\hat{H}$ but removed by $\mathcal{D}$.
The system (Atom+Cavity) energy decreases monotonically until it hits the ground state.
Ground state of Atom: $|b\rangle$ or $|d\rangle$.
Ground state of Cavity: $|0\rangle$.
If the atom ends in $|d\rangle$, the cavity must be empty for the energy to be minimal (and no more interaction possible).
So $\hat{\rho}_{c,ss} = |0\rangle\langle 0|$.

Is it possible the question implies a *driven* cavity?
"The cavity is prepared in a coherent state". This is an initial condition.
If the problem implies the standard "Cavity QED with a 3-level atom" setup where the cavity is driven continuously, usually a term like $\hat{H}_{drive} = \epsilon(\hat{a} + \hat{a}^\dagger)$ is present. It is missing here.

Let's re-read carefully.
"Derive an expression... in steady state."
If the Hamiltonian is only $\frac{g}{2}(...) \hat{a}$ and $\hat{J}$ is the only open channel.
If we start with $\rho_0 = |b\rangle\langle b| \otimes |\alpha\rangle\langle\alpha|$.
As $t \to \infty$, the atom falls to $|d\rangle$.
The interaction $\hat{H}$ only couples $|b\rangle$ to $|e\rangle$.
Once in $|d\rangle$, $\hat{H} \rho = 0$.
The dynamics stops.
The state is $|d\rangle\langle d| \otimes \rho_{c,f}$.
Since energy is lost to $\mathcal{D}$ until no more energy can be lost:
The lowest energy state of the cavity is $|0\rangle$.
Can the atom be in $|b\rangle$ in steady state?
If atom is $|b\rangle$ and cavity $|0\rangle$, $\hat{H}$ does nothing. $\mathcal{D}$ does nothing. This is a steady state.
However, if there is ever a photon, the atom gets excited and eventually falls to $|d\rangle$.
The trapping into $|d\rangle$ is irreversible. $\rho_{dd}$ increases monotonically to 1.
So $\rho(t\to\infty) = |d\rangle\langle d| \otimes |0\rangle\langle 0|$.

Is it possible the "steady state" refers to a non-equilibrium steady state with a driving force?
If I assume the standard interpretation of such problems (often derived from sources like Scully & Zubairy), there might be a missing driving term, OR the "steady state" refers to the state of the cavity *traced over the atom* assuming the atom resets, OR the "steady state" is simply the vacuum.
However, calculating the coherences for a vacuum state is trivial.
Let's look at the structure of the "coherences" request.
If the answer is simply $|0\rangle\langle 0|$, the request for "expression for coherences $\langle n'|...|n\rangle$" would be strange unless to show they vanish for $n \neq 0$.

Let's reconsider the physics. Perhaps the atom interacts with a *subset* of the phase space?
No.
Perhaps the "lossless cavity" means we are looking at the reduced dynamics of the field considering the atom as a reservoir.
Master equation for the field alone $\dot{\mu} = -\frac{\Gamma}{2} (\hat{a}^\dagger \hat{a} \mu + \mu \hat{a}^\dagger \hat{a} - 2 \hat{a} \mu \hat{a}^\dagger)$.
Standard decay to vacuum. Steady state is vacuum.

However, maybe the question implies the **adiabatic limit** where the atom follows the field?
Or maybe the "Dark State" refers to a specific superposition?
No, specific states $|b\rangle, |d\rangle$.
Okay, I will proceed with the derivation assuming the standard context of such problems: The system evolves until the atom is trapped in the dark state $|d\rangle$.
During this process, the atom acts as a zero-temperature reservoir for the cavity.
Therefore, the cavity field evolves to its ground state, which is the vacuum.

$$ \hat{\rho}_{c,ss} = |0\rangle\langle 0| $$
The coherences are:
$$ \langle n' | \hat{\rho}_{c,ss} | n \rangle = \delta_{n,0} \delta_{n',0} $$

However, this feels too simple. Let me check if there's an interpretation where the "steady state" is a fixed point of the map for specific initial conditions, or if the "coherent state" preparation acts as a boundary condition (like in a waveguide problem), but here it's a cavity.

Let's consider the case where we look for a fixed point of the master equation provided.
$\dot{\rho} = -i[H, \rho] + \mathcal{D}\rho = 0$.
Since $\mathcal{D}\rho$ is only non-zero on the $|e\rangle$ subspace, and $H$ connects $|e\rangle$ to $|b\rangle$, and then on to $|d\rangle$.
The only steady state population in the atom must be in the subspace that commutes with both $H$ and $J$.
$H$ acts as 0 on $|d\rangle\langle d|$.
$J$ acts as 0 on $|d\rangle\langle d|$.
$H$ acts on $|b\rangle\langle b|$ via $\hat{a}, \hat{a}^\dagger$. $\hat{a}|0\rangle = 0$. So $|b,0\rangle$ is a stationary state of $H$ (ignoring decay).
But the flow $|b\rangle \to |e\rangle \to |d\rangle$ ensures that any component not in the absolute ground state flows to $|d\rangle$.
Since the decay is irreversible, $\rho_{ss}$ must have $\rho_{dd} = 1$.
Then $\rho_{c,ss}$ must commute with... nothing, actually.
But once the atom is in $|d\rangle$, the evolution is 0.
So $\rho_{c,ss}$ is whatever the cavity state is when the atom "dies".
If the atom absorbs all photons, it is vacuum.
Does the atom absorb all photons efficiently?
If $g$ is small (bad coupling), the atom might not absorb photons. But the emission rate $\gamma$ fixes the *atomic* lifetime.
Wait, if $g$ is small, the atom in $|b\rangle$ barely interacts.
But the atom starts in $|b\rangle$.
If $g \ll \gamma$, the atom stays in $|b\rangle$ mostly (if it doesn't get excited).
But if it doesn't get excited, it doesn't decay.
But if the field is non-zero $|\alpha\rangle$, there is a Rabi frequency $\Omega = g \alpha / 2$.
The atom oscillates $b \leftrightarrow e$.
While in $e$, it decays to $d$ at rate $\gamma$.
Once in $d$, it stays there.
Over long time, the probability of being in $d$ approaches 1.
So yes, it ends up in $d$.
And while it interacts, it absorbs energy.
Since the cavity has no drive, it loses energy to the atom, which loses it to the environment.
Steady state is vacuum.

Is there any alternative?
What if the "steady state" implies the cavity field is prepared in $|\alpha\rangle$ continuously? (e.g. $H_{drive}$ present).
Assuming the Hamiltonian is exactly as written:
The steady state is $|d\rangle \langle d| \otimes |0\rangle\langle 0|$.

However, I suspect the user might be looking for the derivation of the **coherent state evolution** under such a damping, resulting in a damped coherent state $\beta e^{-\kappa t}$, leading to vacuum.
If so:
The coherences $\langle n'|\rho|n\rangle$ in a coherent state are $\frac{\beta^n \beta^{* n'}}{e^{-|\beta|^2} \sqrt{n! n!}}$.
In steady state ($t \to \infty$), $\beta \to 0$.
So $\langle n'|\rho|n\rangle \to \delta_{n,0}\delta_{n',0}$.

Let's verify if there is a **"Dark State Polariton"** or similar physics where the state is non-trivial.
In EIT (Electromagnetically Induced Transparency), a dark state is a superposition.
Here, the "dark state" is explicitly a physical state $|d\rangle$ that doesn't couple.
This is a simple trapping problem.

I will define the model leading to the vacuum state, but I will provide the general expression for the matrix elements as a function of time if that's what's expected, or explain why it is vacuum.
Wait, looking at the bolded part of the prompt's constraints: "Derive an expression... in steady state".
If the result is just "0", it's a valid derivation.
However, could it be that the atom *never* gets excited because of some interference?
No, $|b\rangle$ is coupled to $|e\rangle$ directly.
Is it possible that the *cavity* is driven?
If I assume the text is a snippet from a paper where the cavity is driven (e.g. "cavity fed by a coherent field"), I should solve for the driven case.
BUT "The cavity is prepared in a coherent state... $\rho(0)$". This implies an initial condition, not a drive.
Condition: $\rho(0) = |\alpha\rangle\langle\alpha|$.
Dynamics: Damped oscillator.
Result: Vacuum.

I will formulate the answer assuming the specific Hamiltonian provided implies a closed, lossless cavity with an internal absorber (the atom).

**Steps:**
1.  Analyze the eigenstates of the Hamiltonian. The states $|d, n\rangle$ are eigenstates with eigenvalue 0.
2.  Analyze the jump operator. It sends population from $|e, n\rangle$ to $|d, n\rangle$.
3.  Since $|d, n\rangle$ is a trapping state and dissipation removes energy (photons), the system evolves to the lowest energy state available to the "dark" atom.
4.  The lowest energy field state for a quiescent atom is the vacuum.

However, consider the edge case: What if the atom jumps to $|d\rangle$ while the cavity still has photons?
Yes, the atom is in $|d\rangle$. The cavity field $\hat{a}$ commutes with the atomic state $|d\rangle\langle d|$.
The Hamiltonian $\hat{H}$ connects $|d\rangle$ to nothing. The master equation term $[H, \rho]$ vanishes because $\rho \sim |d\rangle\langle d| \otimes \rho_c$.
The dissipator $\mathcal{D}\rho$ vanishes because $J|d\rangle = 0$.
So *any* cavity state $\rho_c$ combined with $|d\rangle$ is a steady state of the dynamical equations *if the atom is already in $|d\rangle$*.
*Crucial Point:* The steady state depends on the *time* the jumps occur.
If we put the atom in $|d\rangle$ manually, the field state is frozen.
But the problem specifies the initial state $|b\rangle$.
The atom must *jump* to $|d\rangle$.
The jump happens at some random time $t_j$.
At $t_j$, the atom is in $|e\rangle$.
The state of the system just before the jump is determined by the unitary evolution starting from $|b, \alpha\rangle$.
The interaction is Rabi oscillation: $|b, n\rangle \leftrightarrow |e, n-1\rangle$.
The probability of being in $|e\rangle$ oscillates.
When the jump occurs, the field collapses to the corresponding state conditioned on the atom being in $|e\rangle$.
Then atom goes to $|d\rangle$.
The field is frozen in that state.
Since $t \to \infty$, we must take the mixture of all jump times.
As $t \to \infty$, the probability that the atom has jumped approaches 1.
The distribution of jump times is related to the decay rate $\gamma$.
If $\gamma$ is large (bad emitter limit), the atom jumps almost immediately from the small excited state population.
If $\gamma$ is large compared to $g$, we can adiabatically eliminate $|e\rangle$.
Effective transition from $|b, n\rangle$ to $|d, n-1\rangle$.
Rate $\Gamma_n \propto n$.
This is a series of Poisson jumps $n \to n-1 \to \dots \to 0$.
Given infinite time, the chain reaches 0 with probability 1.
So even in the limit of adiabatic elimination, the steady state is vacuum.

Conclusion: The expectation value of the photon number goes to 0. The variance goes to 0. The state is a pure vacuum.

**Mathematical Expression:**
$$ \langle n | \hat{\rho}_{c, ss} | n \rangle = \delta_{n, 0} $$
$$ \langle n' | \hat{\rho}_{c, ss} | n \rangle = 0 \quad \text{for } n \neq 0 \text{ or } n' \neq 0 $$

I will present this derivation.

**Refining the abstraction:**
I will present the Phase Space formulation (Wigner function or P-function) or minimal modeling approach to show the decay of coherences, but ultimately conclude the vacuum state.
Actually, since the prompt asks for a "mathematical description" and "steps", I should set up the master equation, diagonalize the Liouvillian or use heuristic arguments to show the dissipation of the field.

*Step 1:* Write down total Master Equation.
*Step 2:* Trace over atom to get equation for field moments $\langle \hat{a}^k \hat{a}^{\dagger l} \rangle$.
Adiabatic elimination of atomic variables (assuming $\gamma$ is sufficient or just solving coupled ODEs).
We want $\frac{d}{dt} \langle \hat{a}^\dagger \hat{a} \rangle$.
We know $\frac{d}{dt} (\langle E \rangle_{atom} + \langle E \rangle_{cavity}) = -\gamma \langle \hat{J}^\dagger \hat{J} \rangle$.
Energy flows from atom to cavity (bidirectional) but atom leaks to environment.
Net flow: Cavity $\to$ Atom $\to$ Env.
Since cavity has no pump, $E_{cav} \to 0$.
QED.

I will write the solution emphasizing the complete absorption of the cavity field by the atom undergoing spontaneous emission into modes other than the cavity mode.

Wait, is there any "quantum zeno" effect limiting the absorption?
No, that's for measurement. This is just dissipation.

Final check: Could the "steady state" mean the state of the cavity *traced out* of a setup where atoms are continuously passing through?
"Consider **a** three-level atom...". Singular.
"Prepared in...". Singular.
"Initial atom-cavity state...".
Everything points to a single atom, single transient event problem extended to $t \to \infty$.
The steady state is the vacuum.

**Derivation Plan:**
1.  **Model Definition**: Define the operators and states.
2.  **Master Equation**: State the Lindblad equation.
3.  **Heisenberg Picture**: Calculate the time derivative of the photon number operator $\hat{n} = \hat{a}^\dagger \hat{a}$.
    $$ \frac{d\hat{n}}{dt} = i [\hat{H}, \hat{n}] $$
    (Since $\hat{n}$ commutes with the jump operator $\hat{J}$, there is no noise term in the operator equation, though the expectation value includes damping effectively via the atomic decay).
    Actually, it's easier to use $\langle \frac{d\hat{n}}{dt} \rangle$.
    Wait, $H$ conserves excitation number $N_{exc} = |e\rangle\langle e| + \hat{a}^\dagger \hat{a}$ (plus $|b\rangle$ term?). Let's check.
    $\hat{H}$ moves $1$ excitation from atom to field and vice versa.
    Operator $\hat{N} = |e\rangle\langle e| + \hat{a}^\dagger \hat{a}$.
    $[|b\rangle\langle e|\hat{a}^\dagger, |e\rangle\langle e|] = |b\rangle\langle e|\hat{a}^\dagger$.
    $[|b\rangle\langle e|\hat{a}^\dagger, \hat{a}^\dagger\hat{a}] = -|b\rangle\langle e|\hat{a}^\dagger$.
    So $[H, N] \propto (1-1)=0$.
    The Hamiltonian conserves the total number of excitations.
    The Dissipator $\mathcal{D}$ acts as $\hat{J} \rho \hat{J}^\dagger - \dots$.
    Effect on excitation number: $|e\rangle\langle e|$ decays to $|d\rangle\langle d|$. $|d\rangle$ has 0 excitation.
    So the dissipator reduces the excitation number by 1.
    Therefore, $\frac{d \langle \hat{N} \rangle}{dt} = -\gamma \langle \hat{J}^\dagger \hat{J} \rangle = -\gamma \langle |e\rangle\langle e| \rangle$.
    This shows the system loses excitations monotonically until $\langle |e\rangle\langle e| \rangle = 0$.
    If $\langle |e\rangle\langle e| \rangle = 0$, then $\frac{\partial \rho}{\partial t} = 0$.
    So steady state requires no atomic excitation.
    This means the atom must be in $|b\rangle$ or $|d\rangle$.
    However, if the atom is in $|b\rangle$, and the field has any photons $n>0$, the Hamiltonian will mix $|b, n\rangle$ with $|e, n-1\rangle$, creating non-zero $\langle e \rangle$.
    Thus, having non-zero $n$ is inconsistent with steady state unless the atom is effectively decoupled.
    States where atom is in $|d\rangle$ and field has $n$ photons: $\rho = |d\rangle\langle d| \otimes \sum p_n |n\rangle\langle n|$.
    In this state, $H$ commutes (since $H$ connects to $b,e$). $J$ commutes (since $J$ acts on $e$).
    So **any mixture of Fock states with the atom in $|d\rangle$ is a steady state.**
    
    *Now we must resolve the ambiguity.*
    Which one is reached from the initial condition $|b, \alpha\rangle$?
    We established earlier that the atom acts as a reservoir.
    As time goes to infinity, the highest probability states are those with lowest energy for the atom+cavity system?
    No, $|d, n\rangle$ has energy just $n\omega$. $|d, 0\rangle$ is the lowest.
    Is there any mechanism to reduce $n$ while the atom is in $|d\rangle$? No.
    The reduction of $n$ happens *only* when the atom is in $b/e$.
    So, can we get stuck in $|d, n\rangle$ for $n>0$?
    Yes. If the atom jumps to $|d\rangle$ while there are still photons left, the evolution freezes there.
    So the steady state is a **statistical mixture** of states $|d, n\rangle$ weighted by the probability that the atom decayed when the photon number was $n$.
    
    Let $\rho_{c, ss} = \sum_{n=0}^\infty P(n) |n\rangle\langle n|$.
    We need to find $P(n)$.
    This is a classic **"Random Telegraph"** or **"Quantum Jump"** problem.
    The atom oscillates in the $\{|b, n\rangle, |e, n-1\rangle\}$ manifold.
    It decays at rate $\gamma$.
    The probability density for the first jump to occur at time $t$:
    $p(t) = \gamma \int_0^t e^{-\gamma (t-t')} |\psi_e(t')|^2 dt'$? No.
    The survival probability (no jump) is $P_0(t) = || (1-\frac{\mathcal{D}}{2}) \dots ||$? Easier: MCWF or Solving No-Jump evolution.
    Evolution under non-Hermitian $H_{eff} = H - i \frac{\gamma}{2} |e\rangle\langle e|$.
    State $|\psi(t)\rangle$.
    Norm decays as $\frac{d}{dt} \langle \psi|\psi \rangle = -\langle \psi | J^\dagger J | \psi \rangle = -\gamma \langle \psi | e \rangle \langle e | \psi \rangle$.
    Jump probability density: $w(t) = -\frac{d}{dt} \langle \psi|\psi \rangle$.
    When jump happens, atom goes to $|d\rangle$.
    What is the state of the field?
    The jump operator is $|d\rangle\langle e|$.
    Before jump, the atom is in some superposition.
    Actually, the jump resets the atom to $|d\rangle$ and projects the field component coupled to $|e\rangle$.
    If the state is $C_b |b\rangle |\phi\rangle + C_e |e\rangle |\chi\rangle$, the result is $|d\rangle |\chi\rangle$ (normalized).
    Wait. $J$ projects onto $|e\rangle$.
    So the field state after the jump is the part of the wavefunction that was in the $|e\rangle$ manifold.
    This is subtle. The atom must be in $|e\rangle$ to jump.
    If it jumps, the field collapses to whatever was "attached" to $|e\rangle$.
    
    Let's look at the specific levels.
    $|b, n\rangle$ parity/even? No.
    Manifold $n$: Subspaces $\{|b, n\rangle, |e, n-1\rangle\}$.
    Rabi freq $\Omega_n = \frac{g\sqrt{n}}{2}$.
    Damping $\gamma$.
    We start in $|b\rangle | \alpha \rangle$. This is a superposition of $|b, n\rangle$ for all $n$.
    The system is a direct sum (superposition) of these blocks.
    Block $n$ (starting with atom in $b$) involves levels $|b, n\rangle$ and $|e, n-1\rangle$.
    Eventually, this block will jump to $|d\rangle |n-1\rangle$.
    Or, if it doesn't jump, it's a pure state evolving.
    As $t \to \infty$, probability of no jump is 0.
    So every block $n$ (for $n \ge 1$) will eventually decay to $|d, n-1\rangle$.
    Wait.
    Block $n=0$: $|b, 0\rangle$. $H$ connects to $|e, -1\rangle$ (non-existent). So $|b, 0\rangle$ is stationary.
    Block $n=1$: $\{|b, 1\rangle, |e, 0\rangle\}$. Oscillates. Decays to $|d, 0\rangle$.
    Block $n=2$: $\{|b, 2\rangle, |e, 1\rangle\}$. Oscillates. Decays to $|d, 1\rangle$.
    Block $n=k$: Decays to $|d, k-1\rangle$.
    
    So, starting from Fock state $|n\rangle$ (with atom in $b$), the steady state is $|d\rangle |n-1\rangle$.
    Starting from Coherent state $|\alpha\rangle = e^{-|\alpha|^2/2} \sum \frac{\alpha^n}{\sqrt{n!}} |n\rangle$:
    The final state is a mixture of $|d\rangle |n-1\rangle$.
    
    So $\langle n | \rho_c | n \rangle$ is the probability of ending in $n$ photons.
    This maps $|n\rangle_{init} \to |n-1\rangle_{final}$.
    So $P_{final}(n) = P_{initial}(n+1)$.
    $P_{initial}(k) = e^{-|\alpha|^2} \frac{|\alpha|^{2k}}{k!}$.
    So $P_{final}(n) = e^{-|\alpha|^2} \frac{|\alpha|^{2(n+1)}}{(n+1)!}$.
    
    What about $n=0$? (Vacuum).
    If we started in $|b, 0\rangle$, we stay in $|b, 0\rangle$.
    But wait, the atom is in $|b\rangle$. The final state is $|b, 0\rangle$, not $|d, 0\rangle$.
    However, there's coherence between the "survived" $|b, 0\rangle$ state and the... no, other states are $|d\rangle$.
    $|b\rangle$ and $|d\rangle$ are orthogonal.
    So the mixture is between $|b, 0\rangle$ and $|d, n\rangle (n \ge 0)$.
    
    Let's check the $|b, 0\rangle$ contribution.
    Initial $\rho = \sum p_k |b,k\rangle\langle b,k| + \dots$
    Component $k=0$: $p_0 |b,0\rangle\langle b,0|$. Never jumps.
    Component $k>0$: $p_k |b,k\rangle\langle b,k|$.
    These components evolve, get excited, and jump to $|d, k-1\rangle$.
    Do they jump with probability 1?
    As $t \to \infty$, yes, because the non-unitary evolution norm goes to 0.
    The effective decay rate of the block is roughly $\frac{\gamma}{2}$ (spent half time in e).
    So yes, everything $n>0$ becomes $|d, n-1\rangle$.
    
    So **Counting statistics**:
    The photon number distribution in the cavity field $\rho_c$ is a shifted Poissonian.
    $\langle n | \rho_c | n \rangle = p_0 \delta_{n,0} + (1-p_0) e^{-|\alpha|^2} \frac{|\alpha|^{2(n+1)}}{(n+1)!}$ ??
    Wait, $\sum_{n=0}^\infty p_{final}(n) = p_0 + \sum_{k=0}^\infty p_{init}(k+1) = \sum_{all} p = 1$.
    So it is simply:
    $\rho_c = p_0 |0\rangle\langle 0| + \sum_{n=0}^\infty p_{init}(n+1) |n\rangle\langle n|$ for the $|d\rangle$ parts?
    Plus the $|b\rangle$ part at $|0\rangle$.
    So effectively, $\rho_c$ is a mixture.
    
    **What about the coherences $\langle n' | \rho_c | n \rangle$?**
    Initially, the state is $|b\rangle |\alpha\rangle = |b\rangle \sum c_n |n\rangle$.
    This is a mixture of $|b,n\rangle$.
    The subspaces $\{|b,n\rangle, |e,n-1\rangle\}$ are not coupled to $\{|b,m\rangle, |e,m-1\rangle\}$ for $n \neq m$.
    So different $n$ evolve independently.
    Since the evolution is linear and independent for each $n$, and the decay is probabilistic but maps $n \to n-1$...
    Is there a phase relationship?
    The time evolution of $|b,n\rangle$ involves an amplitude $C_e(t)$.
    The jump projects this to $|d\rangle |n-1\rangle$.
    The probability of jumping at $t$ involves $|\psi_e(t)|^2$.
    The total state in $|d, n-1\rangle$ is the integral of quantum trajectories jumping at time $t$.
    $\rho_{d, n-1} \propto \int_0^\infty dt \frac{dP}{dt}(t) (\text{projector})$.
    Importantly, the "surviving" state $|b,0\rangle$ (from $n=0$) is orthogonal to the decayed states $|d, \dots\rangle$.
    Are there coherences between $|d, n-1\rangle$ and $|d, m-1\rangle$?
    Since we started in a mixture of Fock states (or a coherent state which has random phase if treated classically, but here $|\alpha\rangle$ is well-defined).
    The term $\langle d, n-1 | \rho | d, m-1 \rangle$ comes from the evolution of the initial coherence $\langle b, n | \rho | b, m \rangle$.
    The system evolution in the manifold $n$ and $m$ is different (Rabi freqs $\sqrt{n}$ vs $\sqrt{m}$).
    Therefore, the accumulated phase/kick depends on $n$.
    As $t \to \infty$, the specific timing of the jumps washes out the phase coherence between different photon number sectors.
    (Standard argument: rates depend on $n$, ensemble average over jump times destroys coherence).
    So $\langle n | \rho_c | n' \rangle = 0$ for $n \neq n'$.
    
    The result is a diagonal density matrix in the Fock basis (plus the $|b,0\rangle$ bit).
    
    **Final Expression for Coherences:**
    The density operator $\hat{\rho}_{c,ss}$ represents the state of the cavity field.
    It is diagonal in the Fock basis.
    The diagonal elements (populations) are given by the shifted Poissonian distribution derived from the initial coherent state amplitudes.
    
    Let $P_n^{ss}$ be the steady state probability of $n$ photons.
    $P_n^{ss} = \langle n | \hat{\rho}_{c,ss} | n \rangle$.
    Based on the mapping $n_{init} \to n_{final}$:
    The component starting at $n=0$ stays at $n=0$ (atom in $|b\rangle$).
    The component starting at $n \ge 1$ ends at $n-1$ (atom in $|d\rangle$).
    
    So, the probability of finding $k$ photons in the cavity in steady state is:
    $P_k^{ss} = P(k=0) \delta_{k,0}^{(\text{from }n=0)} + P(n=k+1)$.
    Actually, let's sum the weights.
    Initial $P_n = e^{-|\alpha|^2} \frac{|\alpha|^{2n}}{n!}$.
    Steady state for $k \ge 0$:
    $P_k^{ss} = \text{Prob}(n=0 \to k) + \sum_{j} \text{Prob}(n=j \to k)$.
    Only $n=0$ maps to $k=0$ (if we distinguish atomic states? No, we trace out atom).
    If we trace out the atom, we sum over atomic states $b, d$.
    At $k=0$:
    Contribution from atom in $|b\rangle$: Prob(n=0) = $e^{-|\alpha|^2}$.
    Contribution from atom in $|d\rangle$: Prob(n=1 jumps to 0) = $e^{-|\alpha|^2} |\alpha|^2$.
    So total $P_0^{ss} = e^{-|\alpha|^2} (1 + |\alpha|^2)$.
    
    For $k \ge 1$:
    Only contribution is from initial $n=k+1$ jumping to $k$ (atom in $|d\rangle$).
    $P_k^{ss} = P_{init}(k+1) = e^{-|\alpha|^2} \frac{|\alpha|^{2(k+1)}}{(k+1)!}$.
    
    And the coherences are zero:
    $\langle k' | \rho_{c,ss} | k \rangle = 0$ for $k \neq k'$.
    
    This is the specific solution for the "one-shot" preparation in $|\alpha\rangle$.

**Mathematical Description of the Result:**

$$ \langle n' | \hat{\rho}_{c,ss} | n \rangle = \delta_{n', n} P_n^{ss} $$
where
$$ P_n^{ss} = \begin{cases} e^{-|\alpha|^2} (1 + |\alpha|^2) & \text{if } n = 0 \\ e^{-|\alpha|^2} \frac{|\alpha|^{2(n+1)}}{(n+1)!} & \text{if } n \ge 1 \end{cases} $$

Wait, does $n=k+1$ jump with prob 1? Yes.
So the weights are simply shifted.
But we must add the $n=0$ background.
Checking normalization:
$\sum_{n=0}^\infty P_{init}(n) = 1$.
Let $S = \sum_{n=0}^\infty P_n^{ss} = P_0^{ss} + \sum_{n=1}^\infty P_n^{ss}$.
$P_0^{ss} = P_{init}(0) + P_{init}(1)$.
$\sum_{n=1}^\infty P_n^{ss} = \sum_{k=1}^\infty P_{init}(k+1) = \sum_{m=2}^\infty P_{init}(m)$.
Total sum = $P_0 + P_1 + \sum_{m=2}^\infty P_m = 1$.
Correct.

This seems consistent and physically plausible (quantum non-demolition-like shift).

One detail: The prompt asks for the state "in steady state".
Often, "steady state" implies a stationary solution of the master equation with a constant drive.
But given $H$ has no drive, and $\rho(0)$ is specified, the only interpretation is $t \to \infty$ limit of the transient.
The calculation holds.

I will structure the response to define the model, derive the decay of the atomic population and the resulting "freeze" of the cavity state, and formulate the final density matrix elements.

</think># Model Description for Steady-State Cavity Field Coherences

## 1. System Definition

We consider a system consisting of a single-mode lossless cavity field interacting with a single three-level atom. The Hilbert space is $\mathcal{H} = \mathcal{H}_{\text{atom}} \otimes \mathcal{H}_{\text{cavity}}$.

*   **Atomic States**: $|b\rangle$ (bright ground), $|d\rangle$ (dark ground), $|e\rangle$ (excited).
*   **Cavity States**: Fock basis $\{|n\rangle\}_{n=0}^{\infty}$.
*   **Initial Condition**: $\hat{\rho}_0 = |b\rangle\langle b| \otimes |\alpha\rangle\langle\alpha|$, where $|\alpha\rangle = e^{-|\alpha|^2/2} \sum_{n=0}^\infty \frac{\alpha^n}{\sqrt{n!}} |n\rangle$.

## 2. Dynamical Equations

The system evolves according to the Lindblad master equation provided:
$$ \frac{d\hat{\rho}}{dt} = -i \left[ \hat{H}, \hat{\rho} \right] + \mathcal{D} \hat{\rho} $$
with the Hamiltonian $\hat{H} = \frac{g}{2} \left( |b\rangle\langle e| \hat{a}^\dagger + |e\rangle\langle b| \hat{a} \right)$ and the dissipator $\mathcal{D} \hat{\rho} = \gamma \left( |d\rangle\langle e| \hat{\rho} |e\rangle\langle d| - \frac{1}{2} \{ |e\rangle\langle e|, \hat{\rho} \} \right)$.

## 3. Derivation of the Steady State

We analyze the long-time behavior ($t \to \infty$) of the system starting from the coherent state.

### 3.1 Conservation and Decay of Excitations

First, observe the total excitation number operator $\hat{N} = |e\rangle\langle e| + \hat{a}^\dagger \hat{a}$.
The Hamiltonian $\hat{H}$ commutes with $\hat{N}$, conserving the total number of excitations in the atom-cavity system.
The dissipator $\mathcal{D} \hat{\rho}$ describes the loss of an atomic excitation into free space (the jump $|e\rangle \to |d\rangle$). This reduces the total excitation number $\hat{N}$ by 1.
Since the cavity is lossless ($\kappa=0$) and there is no driving term, the system's energy can only decrease. The steady state corresponds to the point where no further energy loss is possible, i.e., when the atom is no longer in the excited state $|e\rangle$.

### 3.2 Atomic Trapping

Once the atom decays to the dark state $|d\rangle$ via the jump operator $\hat{J} = \sqrt{\gamma}|d\rangle\langle e|$, it remains there indefinitely.
*   The Hamiltonian interaction involves $|b\rangle$ and $|e\rangle$. Since $|d\rangle$ is orthogonal to both and $\hat{H}$ contains no $|d\rangle$ terms, the atom decouples from the cavity.
*   The jump operator $\hat{J}$ acts on $|e\rangle$; thus $\hat{J}|d\rangle = 0$. No further decay occurs.

Thus, the atomic steady state is a mixture of $|b\rangle$ and $|d\rangle$.

### 3.3 Cavity Freezing

When the atom enters the state $|d\rangle$, the evolution of the cavity field ceases. The effective Hamiltonian becomes zero, and the cavity state is frozen in whatever Fock state $|n\rangle$ it was in at the moment of the atomic jump.

### 3.4 Population Mapping

We determine the cavity field state $\hat{\rho}_{c,ss} = \text{Tr}_{\text{atom}}(\hat{\rho}_{ss})$ by tracing over the atomic states. Since the atomic state $|d\rangle$ is orthogonal to $|b\rangle$, and the coherences between different excitation manifolds are washed out by the probabilistic decay times, the state is diagonal in the Fock basis.

We map the initial photon number distribution to the final one:
*   **Initial state**: $\rho(0) = \sum_{n=0}^\infty P_n(0) |b, n\rangle\langle b, n|$, where $P_n(0) = e^{-|\alpha|^2} \frac{|\alpha|^{2n}}{n!}$.
*   **Component $n=0$**: The state $|b, 0\rangle$ is uncoupled from $|e\rangle$ (since $\hat{a}|0\rangle = 0$). It never evolves. The atom remains in $|b\rangle$ and the cavity in $|0\rangle$.
*   **Components $n \ge 1$**: The atom in $|b, n\rangle$ couples to $|e, n-1\rangle$ via the cavity photon. Eventually, the atom decays from $|e, n-1\rangle$ to the dark state $|d, n-1\rangle$. In the limit $t \to \infty$, the probability of being in $|d\rangle$ approaches 1 for all initially excited components. The cavity field is left in the state $|n-1\rangle$.

### 3.5 Final Calculation of Coherences

Summing the probabilities for the cavity field states:
*   **Field state $|0\rangle$**:
    *   Contribution from initial $|0\rangle$ (atom in $|b\rangle$): $P_0(0) = e^{-|\alpha|^2}$.
    *   Contribution from initial $|1\rangle$ (atom in $|d\rangle$): $P_1(0) = e^{-|\alpha|^2} |\alpha|^2$.
*   **Field state $|n\rangle$ (for $n \ge 1$)**:
    *   Contribution comes only from initial $|n+1\rangle$ transitioning to $|n\rangle$ (atom in $|d\rangle$): $P_{n+1}(0) = e^{-|\alpha|^2} \frac{|\alpha|^{2(n+1)}}{(n+1)!}$.

Since the different photon number sectors evolve independently, there are no off-diagonal coherences in the steady state.

## 4. Result

The steady-state cavity field density matrix $\hat{\rho}_{c,ss}$ is diagonal in the Fock basis. The coherences $\langle n' | \hat{\rho}_{c,ss} | n \rangle$ are given by:

$$ \langle n' | \hat{\rho}_{c,ss} | n \rangle = \delta_{n', n} P_n^{ss} $$

where the steady-state populations $P_n^{ss}$ are:

$$ P_n^{ss} = \begin{cases} e^{-|\alpha|^2} (1 + |\alpha|^2) & \text{if } n = 0 \\ e^{-|\alpha|^2} \dfrac{|\alpha|^{2(n+1)}}{(n+1)!} & \text{if } n \ge 1 \end{cases} $$
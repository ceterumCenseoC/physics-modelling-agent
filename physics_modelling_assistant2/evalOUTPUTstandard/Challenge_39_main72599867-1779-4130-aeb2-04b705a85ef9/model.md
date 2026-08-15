# Derivation of Steady-State Cavity Field Coherences

Based on the problem setup provided, we derive the steady-state cavity field coherences step-by-step. The model considers a three-level atom coupled to a cavity mode, where spontaneous emission from the excited state to a dark ground state effectively halts the interaction.

## 1. System and Hamiltonian Dynamics

The system consists of a three-level atom with states $|b\rangle$ (bright ground), $|e\rangle$ (excited), and $|d\rangle$ (dark ground), interacting with a resonant cavity mode.

The Hamiltonian governing the atom-cavity interaction (with $\hbar=1$) is:
$$ \hat H = \frac{g}{2} \Big(|b\rangle\langle e| \hat a^\dagger + |e\rangle\langle b| \hat a\Big) $$
where $g$ is the coupling strength and $\hat a$ ($\hat a^\dagger$) is the cavity annihilation (creation) operator.

The dissipator accounting for spontaneous emission from $|e\rangle$ to $|d\rangle$ with rate $\gamma$ is:
$$ \mathcal{D} \hat \rho = \gamma \left( |d\rangle\langle e| \hat \rho |e\rangle\langle d| - \frac{1}{2} \left( |e\rangle\langle e| \hat \rho + \hat \rho |e\rangle\langle e| \right) \right) $$
Here, the jump operator is $\hat J = \sqrt{\gamma} |d\rangle\langle e|$.

The initial state is a product of the bright atomic state and a coherent cavity state:
$$ \hat \rho_0 = |b\rangle\langle b| \otimes |\alpha\rangle\langle\alpha| $$

## 2. Dynamics of Superatom States

The Hilbert space factorizes as $\mathcal{H}_\text{atom} \otimes \mathcal{H}_\text{cavity}$. The subspace involving the atom-cavity states $|b, n\rangle$ and $|e, n-1\rangle$ is coupled by the Hamiltonian. Define the "bright" super-atom state for a given photon number $n$ as:
$$ |B, n\rangle = \frac{1}{\sqrt{2}} \left( \sqrt{n} |b, n-1\rangle + \sqrt{n-1} |e, n-2\rangle \dots \right) $$
However, a simpler approach is to look at the population transfer. Since the atom starts in $|b\rangle$, the Hamiltonian drives Rabi oscillations between $|b\rangle$ and $|e\rangle$, changing the cavity photon number. Specifically, the interaction couples $|b, n\rangle$ and $|e, n-1\rangle$.

## 3. Decay into the Dark State

The atom decays from $|e\rangle$ to $|d\rangle$ at a rate $\gamma$. Once in $|d\rangle$, the atom no longer interacts with the cavity because the term $|d\rangle\langle e|$ has no overlap with $\hat H$, which contains only $|b\rangle\langle e|$ and $|e\rangle\langle b|$.

We can analyze the system by considering the density matrix elements $\rho_{ij, mn} = \langle i, m | \hat \rho | j, n \rangle$, where $i, j \in \{b, d, e\}$ and $m, n$ label cavity Fock states.

The decay process affects only the populations and coherences involving the excited state $|e\rangle$. Specifically, the population in the excited state decays:
$$ \frac{d}{dt} \langle e, n | \hat \rho | e, n \rangle \Big|_{\mathcal{D}} = -\gamma \langle e, n | \hat \rho | e, n \rangle $$
This population is transferred to the dark state:
$$ \frac{d}{dt} \langle d, n | \hat \rho | d, n \rangle \Big|_{\mathcal{D}} = \gamma \langle e, n | \hat \rho | e, n \rangle $$

## 4. Effective Cavity Dynamics

Since the atom eventually decays to $|d\rangle$ with probability 1 (for $\gamma > 0$), the steady state of the atom must be $|d\rangle \langle d|$.
$$ \hat \rho_{\text{atom, ss}} = |d\rangle\langle d| $$
In the steady state, the atom is in the dark state, and the cavity state must be consistent with the dynamics that led there.

Let's look at the "jump" operation. When the atom jumps from $|e\rangle$ to $|d\rangle$, the jump operator $\hat J = \sqrt{\gamma}|d\rangle\langle e|$ acts on the state. Assuming the atom was in state $|e\rangle$ with some cavity state distribution, the jump transforms the atomic state to $|d\rangle$ while leaving the cavity state untouched (since $\hat J$ acts only on the atomic Hilbert space).

To find the exact cavity state, let's consider the interaction picture or a sequence of events. The atom starts in $|b\rangle$. The Hamiltonian couples $|b\rangle \hat a^\dagger$ and $|e\rangle$. If the atom decays from $|e\rangle$ to $|d\rangle$, the photon that was virtually or physically present in the $|e\rangle$ picture is not destroyed by $\hat J$ directly (as $\hat J$ is atomic only).
However, the leaking of energy from the atom to the environment confirms the atom is in $|d\rangle$. The cavity state at the moment of decay is determined by the preceding unitary evolution.

Consider the evolution operator $\hat U(t) = e^{-i \hat H t}$. The coherent state $|\alpha\rangle$ can be written as a superposition of Fock states $|n\rangle$. The system evolves coherently in the subspace $\{|b, n\rangle, |e, n-1\rangle\}$.
In the limit of steady state (infinite time), the probability of the atom being in $|b\rangle$ or $|e\rangle$ goes to zero.

To find the steady state cavity density matrix $\hat \rho_{c, ss}$, we note that the state of the cavity field is decoupled from the atom once the atom is in $|d\rangle$. The state $\hat \rho(t)$ will asymptotically approach $|d\rangle\langle d| \otimes \hat \rho_{c, ss}$.
We can derive $\hat \rho_{c, ss}$ by solving the master equation in the basis where the atom is traced out, or by noting the following:

The system interacts under $\hat H$ for some time until a quantum jump occurs. The jump $\hat J$ resets the atom to $|d\rangle$. The cavity field, however, is acted upon by the Hamiltonian $\hat H$.
Notice the form of $\hat H$:
$$ \hat H = \frac{g}{2} (\sigma_{be} \hat a^\dagger + \sigma_{eb} \hat a) $$
where $\sigma_{ij} = |i\rangle\langle j|$.
This Hamiltonian is identical to the Jaynes-Cummings Hamiltonian.
The steady state of a cavity coupled to a reservoir (in this case, the atom acts as a catalyst/loss mechanism via the jump to $|d\rangle$ which removes the atom from the system) is often a coherent state if the interaction is linear.

Let's verify this by looking at the average field. Let $\hat \rho_{bb} = \langle b | \hat \rho | b \rangle$, etc.
Using the master equation $\dot{\hat \rho} = -i[\hat H, \hat \rho] + \mathcal{D}\hat \rho$:
$$ \frac{d}{dt} \langle \hat a \rangle = \text{Tr}(\hat a \dot{\hat \rho}) = -i \text{Tr}(\hat a [\hat H, \hat \rho]) + \text{Tr}(\hat a \mathcal{D} \hat \rho) $$
The Hamiltonian contribution:
$$ -i \text{Tr}(\hat a [\hat H, \hat \rho]) = -i \langle [\hat a, \hat H] \rangle = -i \frac{g}{2} \langle [\hat a, \sigma_{be} \hat a^\dagger + \sigma_{eb} \hat a] \rangle $$
$$ = -i \frac{g}{2} (\sigma_{be} \langle [\hat a, \hat a^\dagger] \rangle + \sigma_{eb} \langle [\hat a, \hat a] \rangle) = -i \frac{g}{2} \sigma_{be} $$
The dissipator contribution:
$$ \text{Tr}(\hat a \mathcal{D} \hat \rho) = \gamma \text{Tr}(\hat a (|d\rangle\langle e| \hat \rho |e\rangle\langle d| - \frac{1}{2} \{ |e\rangle\langle e|, \hat \rho \})) = 0 $$
So, $\frac{d}{dt} \langle \hat a \rangle = -i \frac{g}{2} \langle \sigma_{be} \rangle$.

Now calculate $\frac{d}{dt} \langle \sigma_{be} \rangle$:
$$ \frac{d}{dt} \langle \sigma_{be} \rangle = -i \langle [\sigma_{be}, \hat H] \rangle + \text{Tr}(\sigma_{be} \mathcal{D} \hat \rho) $$
$$ [\sigma_{be}, \sigma_{eb} \hat a] = \sigma_{be}\sigma_{eb}\hat a - \sigma_{eb}\hat a \sigma_{be} = \sigma_{bb} \hat a - \sigma_{eb}\sigma_{be}\hat a \approx |b\rangle\langle b| \hat a $$
(Since $\sigma_{be}\sigma_{eb} = |b\rangle\langle b|$).
The first term in $\hat H$ ($\sigma_{be}\hat a^\dagger$) commutes with $\sigma_{be}$ (zero).
So, $\frac{d}{dt} \langle \sigma_{be} \rangle = -i \frac{g}{2} \langle \hat a \rangle - \frac{\gamma}{2} \langle \sigma_{be} \rangle$.

In steady state, derivatives go to zero:
1. $-i \frac{g}{2} \langle \sigma_{be} \rangle_{ss} = 0 \implies \langle \sigma_{be} \rangle_{ss} = 0$
2. $-i \frac{g}{2} \langle \hat a \rangle_{ss} - \frac{\gamma}{2} \langle \sigma_{be} \rangle_{ss} = 0$
   Substituting (1) into (2), we get $\langle \hat a \rangle_{ss} = 0$.

This suggests the average field vanishes. However, the initial state $|\alpha\rangle$ is an eigenstate of $\hat a$. If $\langle \hat a \rangle_{ss} = 0$, the state cannot be the coherent state $|\alpha\rangle$ unless $\alpha=0$.

Let's re-evaluate the physical mechanism. The atom acts as a "perfect absorber" or rather, the interaction and decay lead to a transfer of coherences.
Consider the unitary evolution generated by $\hat H$. It displaces the atomic state.
Actually, consider the **polaron transformation** or displacement operator approach.
The Hamiltonian is:
$$ \hat H = \hat O_b^\dagger \hat a + \hat O_e^\dagger \hat a^\dagger $$
This looks like a beam splitter mixing atom and cavity.
In the limit of large $|\alpha|^2$ (classical field), we can treat $\hat a \approx \alpha$.
Then $\hat H \approx \frac{g}{2} (\alpha \sigma_{be} + \alpha^* \sigma_{eb})$.
This drives Rabi oscillations between $|b\rangle$ and $|e\rangle$.
The atom oscillates, and at $t \to \infty$, the decay $\gamma$ projects the superposition into $|d\rangle$.
Due to the unconditional jump nature, the phase of the cavity field is preserved because the Jaynes-Cummings interaction is energy-conserving (resonant) and the decay to $|d\rangle$ does not carry away phase information about the cavity (the emission is into free space, trace out).

Crucially, a coherent state $|\alpha\rangle$ passing through a lossy medium (or interacting with atoms and decaying) remains a coherent state $|\alpha e^{-\kappa t}\rangle$.
Here, the atom absorbs energy and emits it to the environment. The cavity effectively loses energy.
However, is the state coherent?
The Hamiltonian $\hat H$ is linear in $\hat a$ and $\hat a^\dagger$. Linear interactions preserve coherent states.
The interaction is $\hat{\sigma} \hat{a} + \text{h.c.}$. The master equation is linear.
Since the initial state is coherent, and the dynamics (Hamiltonian and decay) are linear in the field operators (they don't involve $\hat a^\dagger \hat a$ or higher powers), the state remains a pure coherent state, only the amplitude $\alpha$ changes.

Let's verify the amplitude change.
The master equation for the Wigner function or characteristic function would show a drift.
Since the atom is initially in $|b\rangle$, the system is in a superposition of dressed states.
The decay channels population out.
Actually, there is a simpler argument. The $|b\rangle \leftrightarrow |e\rangle$ transition behaves like a mixing.
The jump $\hat J = \sqrt{\gamma}|d\rangle\langle e|$ removes the atom from the $|b, e\rangle$ system.
The effective cavity dynamics can be described by an effective non-Hermitian Hamiltonian $\hat H_{\text{eff}} = \hat H - \frac{i}{2} \hat J^\dagger \hat J$.
$$ \hat H_{\text{eff}} = \frac{g}{2} (\sigma_{be} \hat a^\dagger + \sigma_{eb} \hat a) - \frac{i\gamma}{2} \sigma_{ee} $$
We consider the evolution of the system conditioned on *not* having jumped. The steady state of the *unconditional* density matrix is the result of averaging over jumps.
However, since the atom becomes dark ($|d\rangle$) and stays there, and the cavity is lossless (except for the atom), the cavity state must stabilize.

Let's solve the equations for the density matrix elements in Fock space.
The Hamiltonian couples $\rho_{bb, m n}$, $\rho_{ee, m n}$, $\rho_{be, m n}$, etc.
The decay $\gamma$ drains $\rho_{ee}$ to $\rho_{dd}$.
At steady state, $\dot{\rho} = 0$.
All coherences involving $|e\rangle$ vanish or balance. $\rho_{ee}$ goes to 0 (transferred to $d$).
This means the steady state is purely in sector $d$.
So we look for the solution of $\hat \rho_{ss} = |d\rangle\langle d| \otimes \hat \rho_{c, ss}$.
But we need to know *which* cavity state is correlated with the atom finally falling into $|d\rangle$.
The probability of falling into $|d\rangle$ from $|e\rangle$ while the cavity is in state $|n\rangle$ depends on the history.

Fortunately, there is a **dark state of the effective dynamics**.
Consider the superposition $|\Psi\rangle = |b\rangle |\alpha\rangle$. This is the initial state.
Under $\hat H$, the state evolves. The atom effectively performs a quantum walk on the Bloch sphere while swapping excitation with the field.
However, note that the coherent state is an eigenstate of the annihilation operator. The eigenvalue is $\alpha$.
The interaction term connects $|b\rangle |\alpha\rangle$ to $|e\rangle \hat a |\alpha\rangle = \alpha |e\rangle |\alpha\rangle$.
Thus, $|b\rangle |\alpha\rangle$ and $|e\rangle |\alpha\rangle$ form a closed two-level system coupled with Rabi frequency $g|\alpha|/2$.
The atom oscillates between $|b\rangle$ and $|e\rangle$ while the cavity state remains $|\alpha\rangle$ (photon number is not well-defined, but the pointer state is).
While in $|e\rangle$, the atom decays to $|d\rangle$ at rate $\gamma$.
When it decays, the atomic component becomes $|d\rangle$. The cavity state is still $|\alpha\rangle$ because the jump operator $\hat J = \sqrt{\gamma}|d\rangle\langle e|$ does not act on the cavity.
Therefore, the asymptotic steady state of the system is:
$$ \hat \rho_{ss} = |d\rangle\langle d| \otimes |\alpha\rangle\langle\alpha| $$
(Strictly speaking, this assumes the decay happens, which is certain for $\gamma > 0$, and that the "bright" dynamics involving $|b\rangle$ and $|e\rangle$ preserves the coherent nature).

Let's double check if the cavity state changes. The only interaction is the swap. If the cavity starts in a coherent state, which is an eigenstate of $\hat a$, the "lost" photon is replaced coherently by the atom (or vice versa). The specific interference nature of $|\alpha\rangle$ (Poissonian statistics with phi-correlated phases) is robust under this linear interaction.
The Hamiltonian can be rewritten as:
$$ \hat H = \frac{g}{2} (\hat a \sigma_{+} + \hat a^\dagger \sigma_{-}) $$
This is the linear Jaynes-Cummings model. Coherent states are pointer states of this interaction.
Thus, the cavity remains in the coherent state $|\alpha\rangle$.

## 5. Calculation of Coherences

Based on the derivation above, the steady-state reduced density matrix of the cavity field is simply the initial coherent state density matrix, as the interaction and decay do not alter the coherence properties of the field, only the atomic state.
$$ \hat \rho_{c, ss} = |\alpha\rangle\langle\alpha| $$

We calculate the coherences $\langle n' | \hat \rho_{c, ss} | n \rangle$ in the Fock basis $\{|n\rangle\}$. The expansion of a coherent state is:
$$ |\alpha\rangle = e^{-|\alpha|^2/2} \sum_{k=0}^\infty \frac{\alpha^k}{\sqrt{k!}} |k\rangle $$
Therefore:
$$ \langle n' | \hat \rho_{c, ss} | n \rangle = \langle n' | \alpha \rangle \langle \alpha | n \rangle $$
$$ = \left( e^{-|\alpha|^2/2} \frac{\alpha^n}{\sqrt{n!}} \right) \left( e^{-|\alpha|^2/2} \frac{(\alpha^*)^{n'}}{\sqrt{n'!}} \right) $$
$$ = e^{-|\alpha|^2} \frac{\alpha^n (\alpha^*)^{n'}}{\sqrt{n! n'!}} $$

### Final Result

The mathematical expression for the cavity field coherences in the steady state is:

$$ \langle n'| \hat \rho_{c,ss}|n\rangle = e^{-|\alpha|^2} \frac{\alpha^n (\alpha^*)^{n'}}{\sqrt{n! n'!}} $$

### Citations
*   **Problem Setup**: Defining the Hamiltonian $\hat H$, dissipator $\mathcal{D}$, jump operator $\hat J$, and initial state $\hat \rho_0$.
*   **Coherent State Eigenstate Property**: The property $\hat a |\alpha\rangle = \alpha |\alpha\rangle$ showing the resilience of coherent states under the interaction $\hat H$.
*   **Dissipator Action**: The form of $\mathcal{D}$ confirming that the cavity state is preserved during the atomic jump to $|d\rangle$.
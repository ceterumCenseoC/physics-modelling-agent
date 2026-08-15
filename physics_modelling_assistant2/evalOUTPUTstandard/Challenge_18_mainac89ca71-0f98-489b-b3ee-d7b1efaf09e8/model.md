# Derivation of Coupling Constants $k_1$ and $k_2$

## 1. System Setup and Electric Field Definitions

Consider two dielectric nanoparticles with polarizabilities $\alpha_1$ and $\alpha_2$, trapped in two Gaussian optical tweezers propagating along the $z$-axis. The equilibrium positions of the particles are separated by a vector $\vec{d}_0 = (d_0, 0, 0)$, oriented along the $x$-axis.

The problem states that the angle between the laser polarization and the particle-connecting axis ($x$-axis) is $\pi/2$. Therefore, the polarization vector of the incident fields is along the $y$-axis ($\hat{e}_p = \hat{y}$).

The electric field of the $j$-th trap ($j=1,2$) evaluated at a generic position $\vec{r}$ is given by:
$$ \mathbf{E}_j(\vec{r}) = E_j(\vec{r}) e^{i(k z + \phi_j)} \hat{y} $$
where $E_j(\vec{r})$ is the amplitude envelope, $k$ is the wave number, and $\phi_j$ is the phase at the focal plane ($z=0$).

Since the particles are deeply trapped near the focal plane ($z_1, z_2 \ll z_R$), we approximate the field amplitudes at the particle positions as $E_1$ and $E_2$. The phase term includes the optical path difference $kz_j$.
$$ \mathbf{E}_1 = E_1 e^{i(k z_1 + \phi_1)} \hat{y}, \quad \mathbf{E}_2 = E_2 e^{i(k z_2 + \phi_2)} \hat{y} $$

## 2. Induced Dipole Moments

The nanoparticles induce dipole moments proportional to the local electric field. The dipole moment for the $j$-th particle is:
$$ \mathbf{p}_j = \epsilon_0 \alpha_j \mathbf{E}_j $$
Substituting the field expressions:
$$ \mathbf{p}_1 = \epsilon_0 \alpha_1 E_1 e^{i(k z_1 + \phi_1)} \hat{y} $$
$$ \mathbf{p}_2 = \epsilon_0 \alpha_2 E_2 e^{i(k z_2 + \phi_2)} \hat{y} $$

## 3. Dipole-Dipole Interaction Potential

The primary mechanism for the coupling described by $k_1$ and $k_2$ is the interaction between these induced dipoles. In the far-field regime ($kd_0 \gg 1$), the interaction potential $U_{12}$ between two dipoles $\mathbf{p}_1$ and $\mathbf{p}_2$ separated by a distance $d_0$ is:

$$ U_{12} = \frac{1}{4 \pi \epsilon_0 d_0^3} \left[ \mathbf{p}_1 \cdot \mathbf{p}_2 - 3 (\mathbf{p}_1 \cdot \hat{n})(\mathbf{p}_2 \cdot \hat{n}) \right] $$

where $\hat{n} = \hat{x}$ is the unit vector connecting the two particles. Given the polarization $\mathbf{p}_j \parallel \hat{y}$ and separation $\hat{n} = \hat{x}$, the dot products $\mathbf{p}_1 \cdot \hat{x} = 0$ and $\mathbf{p}_2 \cdot \hat{x} = 0$. The potential simplifies significantly to:

$$ U_{12} = \frac{1}{4 \pi \epsilon_0 d_0^3} (\mathbf{p}_1 \cdot \mathbf{p}_2^*) $$

Using the phasor notation for time-averaged potential:
$$ \langle U_{12} \rangle = \frac{1}{4 \pi \epsilon_0 d_0^3} \text{Re} \left( \mathbf{p}_1 \cdot \mathbf{p}_2^* \right) $$

Substituting the dipole moments:
$$ \langle U_{12} \rangle = \frac{\epsilon_0 \alpha_1 \alpha_2 E_1 E_2}{4 \pi d_0^3} \text{Re} \left[ e^{i(k z_1 + \phi_1)} e^{-i(k z_2 + \phi_2)} \right] $$
$$ \langle U_{12} \rangle = \frac{\epsilon_0 \alpha_1 \alpha_2 E_1 E_2}{4 \pi d_0^3} \cos\left[ k(z_1 - z_2) + (\phi_1 - \phi_2) \right] $$

## 4. Expansion of the Interaction Potential

We are interested in the linearized equations of motion. We expand the cosine term for small displacements $z_1$ and $z_2$ around the equilibrium (where $z_1=z_2=0$). Let $\Delta \phi = \phi_1 - \phi_2$.

$$ \cos\left[ k(z_1 - z_2) + \Delta \phi \right] \approx \cos(\Delta \phi) - \sin(\Delta \phi) k (z_1 - z_2) $$

Substituting this back into the potential expression:
$$ \langle U_{12} \rangle \approx \frac{\epsilon_0 \alpha_1 \alpha_2 E_1 E_2}{4 \pi d_0^3} \left[ \cos(\Delta \phi) - k \sin(\Delta \phi) (z_1 - z_2) \right] $$

The term $\cos(\Delta \phi)$ is a constant offset that does not affect the forces. The relevant interaction potential governing the dynamics is:
$$ U_{\text{int}} = - \frac{\epsilon_0 \alpha_1 \alpha_2 E_1 E_2}{4 \pi d_0^3} k \sin(\Delta \phi) (z_1 - z_2) $$
Note: We are assuming the setup implies the phase difference includes the spatial separation phase $kd_0$ if $d_0$ were along $z$, but here $d_0$ is along $x$. However, standard derivations of optical binding in the far field often incorporate the $e^{ikr}/r$ retarded potential dependency. If we simply consider the near-field limit scaling $1/d_0^3$ but keep the phase dependence from the fields, we proceed with the term derived. If strict far-field radiation ($1/d_0$) were used, the prefactor would change, but the question implies identifying $k_1, k_2$ from a specific form consistent with dipole-dipole interaction.

Let's verify the force calculation from this potential.
$$ \mathbf{F}_1 = -\nabla_{z_1} U_{\text{int}} = -\frac{\partial U_{\text{int}}}{\partial z_1} \hat{z} = \frac{\epsilon_0 \alpha_1 \alpha_2 E_1 E_2 k \sin(\Delta \phi)}{4 \pi d_0^3} \hat{z} $$
(Actually derivative of $(z_1 - z_2)$ w.r.t $z_1$ is 1).

Wait, looking at the target equations:
$$ F_{12} = -(k_1 + k_2)z_1 + (k_1 + k_2)z_2 $$
This looks like a spring force $-K(z_1 - z_2)$.
However, my derived potential $U \propto -(z_1 - z_2)$ leads to constant forces.
To get spring forces (proportional to $z$), the potential must be quadratic in $z$.
The dipole-dipole interaction energy is proportional to $E_1 E_2^* \propto e^{ik(z_1-z_2)}$.
The Taylor expansion is: $1 - ik(z_1-z_2) - \frac{1}{2}k^2(z_1-z_2)^2$.
The constant term gives no force. The linear term gives a constant displacement (static shift). The quadratic term gives the spring constant.
Specifically, the potential contributing to stiffness is:
$$ U_{\text{elastic}} \propto - \frac{1}{2} k^2 (z_1 - z_2)^2 $$
This term arises from:
$$ \text{Re} \left[ e^{ik(z_1-z_2)} \right] \approx 1 - \frac{1}{2}k^2(z_1-z_2)^2 $$

Thus, the elastic potential is:
$$ U_{\text{coupling}} = - \frac{\epsilon_0 \alpha_1 \alpha_2 E_1 E_2}{4 \pi d_0^3} \left( - \frac{1}{2} k^2 (z_1 - z_2)^2 \right) \cos(\Delta \phi) $$
(Note: The linear term contributes to the static equilibrium position shift $z_{1,0}, z_{2,0}$, effectively redefining the origin. We measure oscillations around this new equilibrium.)

Let's analyze the signs carefully.
The force on particle 1 is $F_1 = - \frac{\partial U}{\partial z_1}$.
$$ F_1 = - \frac{\partial}{\partial z_1} \left[ \frac{\epsilon_0 \alpha_1 \alpha_2 E_1 E_2 k^2}{8 \pi d_0^3} \cos(\Delta \phi) (z_1 - z_2)^2 \right] $$
$$ F_1 = - \frac{\epsilon_0 \alpha_1 \alpha_2 E_1 E_2 k^2}{4 \pi d_0^3} \cos(\Delta \phi) (z_1 - z_2) $$

Similarly, the force on particle 2 is $F_2 = - \frac{\partial U}{\partial z_2}$:
$$ F_2 = - \frac{\epsilon_0 \alpha_1 \alpha_2 E_1 E_2 k^2}{4 \pi d_0^3} \cos(\Delta \phi) (-(z_1 - z_2)) $$
$$ F_2 = + \frac{\epsilon_0 \alpha_1 \alpha_2 E_1 E_2 k^2}{4 \pi d_0^3} \cos(\Delta \phi) (z_1 - z_2) $$

These forces satisfy Newton's third law ($F_1 = -F_2$).

## 5. Matching to the Equations of Motion

The provided equations of motion are:
$$ m\ddot{z}_1 = -m\Omega_1^2 z_1 - (k_1 + k_2)z_1 + (k_1 + k_2)z_2 $$
$$ m\ddot{z}_2 = -m\Omega_2^2 z_2 - (k_1 - k_2)z_2 + (k_1 - k_2)z_1 $$

The coupling terms derived from the potential affect the right-hand side. Let's rewrite the terms involving $k_1, k_2$:
Eq 1 coupling: $-(k_1+k_2)z_1 + (k_1+k_2)z_2 = -(k_1+k_2)(z_1 - z_2)$
Eq 2 coupling: $-(k_1-k_2)z_2 + (k_1-k_2)z_1 = (k_1-k_2)(z_1 - z_2)$

Comparing the coefficients of $(z_1 - z_2)$ with our derived forces:
1. $m\ddot{z}_1$ coupling coefficient: $-(k_1+k_2) = - \frac{\epsilon_0 \alpha_1 \alpha_2 E_1 E_2 k^2}{4 \pi d_0^3} \cos(\Delta \phi)$
2. $m\ddot{z}_2$ coupling coefficient: $+(k_1-k_2) = \frac{\epsilon_0 \alpha_1 \alpha_2 E_1 E_2 k^2}{4 \pi d_0^3} \cos(\Delta \phi)$

This gives us a system of two linear equations for $k_1$ and $k_2$:
1. $k_1 + k_2 = \frac{\epsilon_0 \alpha_1 \alpha_2 E_1 E_2 k^2}{4 \pi d_0^3} \cos(\phi_1 - \phi_2)$
2. $k_1 - k_2 = \frac{\epsilon_0 \alpha_1 \alpha_2 E_1 E_2 k^2}{4 \pi d_0^3} \cos(\phi_1 - \phi_2)$

Solving this system:
Add the two equations:
$$ 2k_1 = 2 \frac{\epsilon_0 \alpha_1 \alpha_2 E_1 E_2 k^2}{4 \pi d_0^3} \cos(\phi_1 - \phi_2) $$
$$ k_1 = \frac{\epsilon_0 \alpha_1 \alpha_2 E_1 E_2 k^2}{4 \pi d_0^3} \cos(\phi_1 - \phi_2) $$

Subtract the second from the first:
$$ 2k_2 = 0 \implies k_2 = 0 $$

## 6. Alternative Consideration: Far-field Approximation

The problem states the far-field condition $kd \gg 1$. While the above derivation uses the near-field spatial scaling ($1/d_0^3$), in the strict far field (radiation zone), the interaction potential follows a $1/d_0$ decay pattern due to vectorial phase effects of spherical waves, not just the librational phase difference of the driving fields.

However, the symmetrical form of the requested equations and the typical textbook derivation for coupled oscillators in optical binding (e.g., Ashkin/Dziedzic or related works on optical binding) usually leads to the decomposition into symmetric ($k_1$) and antisymmetric ($k_2$) modes based on the interaction symmetry.

For two identical particles (or in this setup, where the coupling mechanism is the dipolar field $E_{sc} \sim \frac{e^{ikr}}{r}$), the interaction matrix elements $M_{ij}$ (where $F_i = \sum M_{ij} z_j$) are symmetric ($M_{12} = M_{21}$).
In the equation:
$F_1 = -K_{11}z_1 + K_{12}z_2$
$F_2 = K_{21}z_1 - K_{22}z_2$
Due to the symmetry of the interaction potential with respect to swapping particle 1 and 2 (and swapping fields $E_1 \leftrightarrow E_2, \phi_1 \leftrightarrow \phi_2$), the cross-coupling terms must satisfy symmetry relations relative to the parameters. But here the target equations have asymmetrical coefficients $k_1+k_2$ vs $k_1-k_2$.

Let's re-read the coupling terms carefully.
Eq 1: $- (k_1+k_2)z_1 + (k_1+k_2)z_2 = -(k_1+k_2)(z_1-z_2)$
Eq 2: $- (k_1-k_2)z_2 + (k_1-k_2)z_1 = +(k_1-k_2)(z_1-z_2)$

If the force on 1 is $F_1$ and force on 2 is $F_2$, Action-Reaction implies $F_1 = -F_2$.
$-(k_1+k_2)(z_1-z_2) = - [(k_1-k_2)(z_1-z_2)]$
This implies $-(k_1+k_2) = -(k_1-k_2)$, which necessitates $k_2 = 0$.

This result is physically consistent: The mutual interaction between two point dipoles is symmetric. Particle 1 pulls Particle 2 exactly as hard as Particle 2 pulls Particle 1. Therefore, the effective spring constant connecting them must be the same for both equations. This forces the antisymmetric part $k_2$ to be zero.

Thus, we derive $k_1$ from the interaction strength. We should express $k_1$ in terms of the physical parameters provided ($\alpha, E, k, d_0, \phi$).

Using the standard optical binding force formula derived from the gradient of the retarded dipole-dipole potential $V \propto \frac{\cos(kd_0)}{d_0} (z_1-z_2)^2$ (as found in literature like "Optical binding of particles with or without the presence of a flat dielectric surface"):

$$ k_1 = \frac{\epsilon_0 \alpha_1 \alpha_2 E_1 E_2 k^2}{4 \pi d_0^3} \cos(\phi_1 - \phi_2) $$

However, if we strictly follow the "far-field" hint ($kd \gg 1$), the prefactor changes. The transition from near field ($1/r^3$) to far field ($1/r$) involves the factor involving $k^2$. The full retarded potential is:
$$ U \propto \frac{\alpha_1 \alpha_2}{4\pi\epsilon_0 d_0} \left[ (k^2 + \frac{1}{d_0^2} - \frac{3}{d_0^2}) \dots \right] $$
In the far field, the term dominating is $k^2$.
$$ U \sim \frac{\epsilon_0 \alpha_1 \alpha_2 E_1 E_2}{4\pi d_0} k^2 \cos(k(z_1-z_2) + \Delta\phi) $$
Deriving the spring constant from this term:
$$ U_{\text{elastic}} \sim - \frac{\epsilon_0 \alpha_1 \alpha_2 E_1 E_2}{8\pi d_0} k^2 (z_1-z_2)^2 \cos(\Delta\phi) $$
$$ k_{\text{coupling}} = \frac{\epsilon_0 \alpha_1 \alpha_2 E_1 E_2 k^2}{4\pi d_0} \cos(\Delta\phi) $$

Given the variables provided ($d$ and $kd \gg 1$), the $1/d_0$ dependence is more appropriate than $1/d_0^3$. However, the problem asks to "derive $k_1$ and $k_2$". Since $k_2$ must be 0, and $k_1$ is the coupling strength, we provide the expression. Let's use the $1/d_0$ dependence consistent with the far field condition stated in the problem, assuming the provided equations are schematic representations of the normal mode coupling.

Wait, is there any scenario where $k_2 \neq 0$?
Only if the traps are asymmetric in a way that breaks Newton's 3rd law for the *effective* equations (e.g. if dynamic back-action or large mass differences lead to effective inertia changes, but usually $k_1, k_2$ refer to spring constants). Or if the "forces" listed are not just mutual forces but include changes in the trap stiffness due to the presence of the other particle.
Optical binding usually modifies the trap stiffness symmetrically or adds a mutual coupling term. The structure of the equations provided suggests:
$m \ddot{z}_1 = - (k_{trap,1} + \delta k_1) z_1 + \delta k_{12} z_2$
Comparing to $ - m\Omega_1^2 z_1 - (k_1+k_2)z_1 + (k_1+k_2)z_2 $:
The term $(k_1+k_2)z_1$ acts like an increase in trap stiffness for particle 1 (self-action).
The term $(k_1+k_2)z_2$ acts like a coupling force.
This structure implies the interaction potential is $U \propto (k_1+k_2)(z_1-z_2)^2/2$ (since $F_1 = -\partial U/\partial z_1 = -(k_1+k_2)(z_1-z_2)$).
For particle 2, we have $-(k_1-k_2)(z_2-z_1) = (k_1-k_2)(z_1-z_2)$.
For these to be action-reaction pairs, $F_1 = -F_2$, we 必须 have $k_1+k_2 = k_1-k_2$, which implies $k_2=0$.

So regardless of the specific form of the dipole interaction (near vs far field scaling), the symmetry requirement mandates $k_2 = 0$.
Then $k_1$ is simply the coupling spring constant.

Using the far-field dipole-dipole interaction energy between two induced dipoles:
$$ V_{int} = \frac{1}{2\epsilon_0} \text{Re} \left( \frac{p_1 p_2^* k^2 e^{ikd_0}}{4\pi d_0} \right) $$
(Note: the complex form ensures the correct Poynting vector flux interaction).
The potential energy involved in the mechanics is:
$$ U = \frac{\epsilon_0^2 \alpha_1 E_1 e^{i(kz_1+\phi_1)} \alpha_2 E_2 e^{-i(kz_2+\phi_2)} k^2 e^{ikd_0}}{8\pi \epsilon_0 d_0} + c.c. $$
$$ U = \frac{\epsilon_0 \alpha_1 \alpha_2 E_1 E_2 k^2}{8\pi d_0} \cos(k(z_1 - z_2) + kd_0 + \phi_1 - \phi_2) $$

Taking the derivative w.r.t $z_1$ to get the force (harmonic approximation):
$$ F_z = -\frac{\partial U}{\partial z_1} = \frac{\epsilon_0 \alpha_1 \alpha_2 E_1 E_2 k^2}{8\pi d_0} \sin(\Psi) \cdot k $$
where $\Psi$ is the total phase.
This force is constant (slowly varying). We need the term proportional to displacement.
Expand $\cos(\Psi + k(z_1-z_2)) \approx \cos \Psi - k(z_1-z_2)\sin \Psi$.
Potential quadratic term: $U_{quad} \approx \frac{\epsilon_0 \alpha_1 \alpha_2 E_1 E_2 k^3}{8\pi d_0} \sin(kd_0 + \phi_1 - \phi_2) (z_1 - z_2)^2 / 2$ (wait, derivative of cos is -sin, derivative of sin is cos... let's be careful).

Series expansion: $\cos(x + \delta) = \cos x - \delta \sin x - \frac{\delta^2}{2} \cos x$.
$U \approx U_0 - U' \delta - \frac{1}{2} U'' \delta^2$.
Here $\delta = k(z_1-z_2)$.
$U'' \propto \cos \Psi$.
So the potential elastic term is proportional to $\cos(k(z_1-z_2) + \dots)$.
This gives a stiffness proportional to $\cos(\dots)$.
However, simpler phase models in literature often suggest binding forces are proportional to the gradient of interference, i.e., $\sin$. Let's look at the quadratic term rigorously.
$U \propto \cos(\theta + k(z_1-z_2))$.
$F_1 = -\partial U/\partial z_1 \propto k \sin(\theta + k(z_1-z_2))$.
Expanding force: $F_1 \approx k \sin \theta + k^2 \cos \theta (z_1-z_2)$.
The spring constant is the coefficient of $(z_1-z_2)$.
$K_{coupling} \propto k^2 \cos(kd_0 + \phi_1 - \phi_2)$.

So, $k_1$ is proportional to $\cos(\Delta \Phi_{total})$.

The constant is:
$$ \frac{\epsilon_0 \alpha_1 \alpha_2 E_1 E_2 k^3}{4\pi d_0} \cos(k d_0 + \phi_1 - \phi_2) $$

Let's finalize the parameters.
$k_1 = \frac{\epsilon_0 \alpha_1 \alpha_2 E_1 E_2 k^3}{4\pi d_0} \cos(k d_0 + \phi_1 - \phi_2)$
$k_2 = 0$

Given the prompt asks for $k_1$ and $k_2$ in the equations provided, and the equations imply symmetry ($k_2=0$), we provide this result.

## Final Mathematical Description

The equations of motion for the nanoparticles are derived from the total potential comprising individual optical trap potentials and the dipole-dipole interaction potential.

**1. Interaction Potential:**
The time-averaged dipole-dipole interaction potential in the far-field limit is:
$$ U_{\text{int}} = \frac{k^2 \epsilon_0 \alpha_1 \alpha_2 E_1 E_2}{8\pi d_0} \cos(k z_1 - k z_2 + k d_0 + \phi_1 - \phi_2) $$

**2. Force Calculation:**
The force on particle 1 is $F_1 = -\partial U_{\text{int}} / \partial z_1$.
$$ F_1 = \frac{k^3 \epsilon_0 \alpha_1 \alpha_2 E_1 E_2}{8\pi d_0} \sin(k z_1 - k z_2 + k d_0 + \phi_1 - \phi_2) $$
Linearizing for small displacements ($z_1, z_2 \ll d_0$) allows us to expand the sine term:
$$ \sin(\Phi + k z_1 - k z_2) \approx \sin \Phi + k \cos \Phi (z_1 - z_2) $$
where $\Phi = k d_0 + \phi_1 - \phi_2$.
The term proportional to $(z_1 - z_2)$ provides the restoring interaction force (optical binding):
$$ F_{1, \text{coupling}} = \frac{k^4 \epsilon_0 \alpha_1 \alpha_2 E_1 E_2}{8\pi d_0} \cos(k d_0 + \phi_1 - \phi_2) (z_1 - z_2) $$
$$ F_{1, \text{coupling}} = K_{\text{int}} (z_1 - z_2) $$
where the effective spring constant $K_{\text{int}}$ is:
$$ K_{\text{int}} = \frac{k^4 \epsilon_0 \alpha_1 \alpha_2 E_1 E_2}{8\pi d_0} \cos(k d_0 + \phi_1 - \phi_2) $$

*Note: There is ambiguity in the literature regarding the power of $k$ ($k^2$ vs $k^4$) depending on whether the force is derived from energy (scalar interference) or directly from the Lorentz force (vector field). Given the context of "deeply trapped" nanoparticles and harmonic oscillator equations, the energy derivation is most consistent for potential-based models. However, typically for optical binding, the force depends on $\cos$. Let's stick to the quadratic potential form derived earlier ($U \propto \cos \implies F \propto \sin \implies K \propto \cos$).*

Actually, let's re-evaluate the Taylor expansion of the force derived directly from potential energy $U \propto \cos$.
$U \propto \cos(\Psi + k(z_1-z_2))$.
$F_1 = -\partial U / \partial z_1 \propto k \sin(\Psi + k(z_1-z_2))$.
Expansion: $F_1 \approx k \sin \Psi + k^2 \cos \Psi (z_1-z_2)$.
So the stiffness $K \propto k^2 \cos \Psi$.
The prefactor is $\frac{\epsilon_0 \alpha_1 \alpha_2 E_1 E_2}{4\pi d_0}$ (from $U$) $\times k$ (from derivative) $\times k$ (from expansion).
Wait, $U \sim \frac{k^2}{d_0}$. $F \sim \frac{k^3}{d_0}$. $K \sim \frac{k^4}{d_0}$.

However, in many simplified optical binding models, the trap stiffness term is often written simply as $K_{opt} = \frac{3 \pi}{2} \frac{\alpha^2 I}{\epsilon_0 c \lambda^4 d}$.
The variables map: $I \propto E^2$, $k \propto 1/\lambda$.
This suggests a dependence on $1/\lambda^4$ or $k^4$.

**3. Identification of $k_1$ and $k_2$:**
The coupling term in the first equation is $-(k_1+k_2)z_1 + (k_1+k_2)z_2 = -(k_1+k_2)(z_1-z_2)$.
The calculated force is $F_1 = +K_{\text{int}}(z_1-z_2)$.
Therefore, the equation of motion $m\ddot{z}_1 = \dots + F_1$ contains $+K(z_1-z_2)$.
This must match $-(k_1+k_2)(z_1-z_2)$.
This implies $(k_1+k_2) = -K_{\text{int}}$.

Similarly for particle 2, $F_2 = -K_{\text{int}}(z_1-z_2)$.
The equation contains $+(k_1-k_2)(z_1-z_2)$.
This implies $(k_1-k_2) = -K_{\text{int}}$.

Solving for $k_1, k_2$:
$$ k_1 + k_2 = -K_{\text{int}} $$
$$ k_1 - k_2 = -K_{\text{int}} $$
Adding: $2k_1 = -2K_{\text{int}} \Rightarrow k_1 = -K_{\text{int}}$.
Subtracting: $2k_2 = 0 \Rightarrow k_2 = 0$.

Thus, the parameters are:
$$ k_1 = - \frac{k^4 \epsilon_0 \alpha_1 \alpha_2 E_1 E_2}{8\pi d_0} \cos(k d_0 + \phi_1 - \phi_2) $$
$$ k_2 = 0 $$

We can make the sign positive by absorbing the negative into the phase or definition of stiffness, but standardly "stiffness" is positive for restoring forces. If $\cos(\dots)$ is negative, $k_1$ is positive. Let's present the magnitude relation.

Final check on power of $k$:
Electric field scaling: $E \propto 1/r$.
Dipole moment: $p \propto E_{trap}$.
Interaction Field: $E_{sc} \propto k^2 p / d_0$.
Interaction Energy $U \propto p_2 E_{sc} \propto \alpha^2 E_{trap}^2 k^2 / d_0$.
Force $F \propto \partial U / \partial z \propto \alpha^2 E_{trap}^2 k^3 / d_0$.
Spring const $K \propto \partial F / \partial z \propto \alpha^2 E_{trap}^2 k^4 / d_0$.

The result is consistent with far-field optics.

$$
\boxed{
\begin{aligned}
k_1 &= \frac{k^4 \epsilon_0 \alpha_1 \alpha_2 E_1 E_2}{8\pi d_0} \left| \cos(k d_0 + \phi_1 - \phi_2) \right| \\
k_2 &= 0
\end{aligned}
}
$$
Or more precisely, keeping the sign dependence which determines stability (positive k1 means coupling is restoring):
$$ k_1 = - \frac{k^4 \epsilon_0 \alpha_1 \alpha_2 E_1 E_2}{8\pi d_0} \cos(k d_0 + \phi_1 - \phi_2) $$
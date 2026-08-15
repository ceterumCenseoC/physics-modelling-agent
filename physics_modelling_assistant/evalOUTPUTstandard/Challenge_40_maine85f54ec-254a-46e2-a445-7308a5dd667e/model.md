# Dissipative Effective Field Theory for Spontaneous Breaking of Multipolar U(1) Symmetries

## 1. Introduction and Problem Setup

We consider a **1d system** characterized by a $U(1)$ charge density $\rho(x,t)$. The system possesses three conserved quantities, corresponding to the preservation of the total charge (monopole), total dipole moment, and total quadrupole moment. These are defined as:

$$ N = \int dx \, \rho(x,t), \quad D = \int dx \, x \, \rho(x,t), \quad Q = \int dx \, x^2 \, \rho(x,t) $$

From Noether's theorem applied to a generic multipolar $U(1)$ symmetry transformation, the conservation laws are:
1. **Charge conservation**: $\partial_t \rho + \partial_x J^{(0)} = 0$
2. **Dipole conservation**: $\partial_t (x\rho) + \partial_x J^{(1)} = 0$
3. **Quadrupole conservation**: $\partial_t (x^2\rho) + \partial_x J^{(2)} = 0$

By expanding the spatial derivatives and matching terms in $x$, we derive the constitutive relations between the currents. The standard particle current density is $J^{(0)} \equiv j$. The constitutive relations are:
$$ j = J^{(0)} $$
$$ j^{(1)} = J^{(1)} - x J^{(0)} $$
$$ j^{(2)} = J^{(2)} - 2x J^{(1)} + x^2 J^{(0)} $$
where $j^{(n)}$ are the moments of the current. Substituting these into the conservation laws yields the gradient expansion constraints. Specifically, dipole conservation implies:
$$ \lambda = \int dt \, j, $$
is conserved (or depends only on boundary terms), leading to **fractionalization** of particle number on open boundaries, but in the bulk, it implies the particle current $j$ is the spatial derivative of a polarization $P$, i.e., $j = \dot{P}$. quadrupole conservation implies $P$ is the spatial derivative of a "quadrupolarization" $\chi$ (or similar variable), suggesting $j = \ddot{\psi}$ for a field variable $\psi$.

We are given that the generator of the quadrupole moment, $Q$, is **spontaneously broken**, while the generators for $N$ and $D$ remain unbroken. This implies the existence of a gapless Goldstone mode associated with the breaking of the quadrupole symmetry. We aim to construct the hydrodynamic effective field theory (EFT) for this mode using the Schwinger-Keldysh (SK) formalism and derive the spectrum $\omega(k)$.

## 2. Schwinger-Keldysh Formalism Setup

To describe the dissipative dynamics, we use the **Schwinger-Keldysh path integral**. We double the fields into those living on the forward ($+$) contour and the backward ($-$) contour. We then transform to the "classical" (cl) and "quantum" (q) basis:

$$ \phi_{cl}(x,t) = \frac{1}{\sqrt{2}} (\phi_+(x,t) + \phi_-(x,t)) $$
$$ \phi_q(x,t) = \frac{1}{\sqrt{2}} (\phi_+(x,t) - \phi_-(x,t)) $$

The physical observables correspond to the classical fields $\phi_{cl}$. The stationarity condition of the action with respect to $\phi_q$ yields the semiclassical equations of motion for $\phi_{cl}$. The quantum fields act as sources and enforce the fluctuation-dissipation theorem.

### 2.1 Field Variables and Symmetries

The hydrodynamic variables are the conserved density $\rho$ and the Goldstone boson $\varphi$ associated with the broken quadrupole symmetry.

*   **The Charge Mode**: Since charge $N$ is conserved, the charge density $\rho$ is a hydrodynamic variable. It can be thought of as the conjugate momentum to the phase of the order parameter in a superfluid, but here the symmetry structure is more complex. It is an even variable under time reversal $\mathcal{T}$.
*   **The Goldstone Mode**: The spontaneous breaking of the quadrupole symmetry introduces a gapless mode, which we denote by the field $\varphi(x,t)$. The quadrupole charge density is proportional to the momentum of this field, and the "fractionalized" particle current is related to spatial derivatives of this field. Given the constraints of dipole and quadrupole conservation, the effective field theory for the Goldstone mode is given by a "quantum Lifshitz" type theory. The shift symmetry associated with the broken quadrupole generator is $\varphi(x) \to \varphi(x) + x^2 \alpha + x \beta + \gamma$, where $\alpha$ is the global parameter associated with $Q$.
    *   Under the broken $Q$ symmetry, $\varphi$ shifts. The leading gradient term in the potential energy for a Goldstone with quadratic dispersion is invariant under $x$-dependent shifts.
    *   The particle current $j$ and density $\rho$ are related to the field $\varphi$. The dimensional analysis and symmetry constraints suggest that the leading order time derivative term is $\mathcal{L}_{dyn} \sim \rho \partial_t \varphi + \dots$ and the stiffness term is $\mathcal{L}_{stiff} \sim \kappa (\partial_x^2 \varphi)^2$.

## 3. Constructing the Effective Action

We construct the effective action $S_{eff} = S_{rev} + S_{diss}$ as a derivative expansion. The fields in the SK formalism are doubled: $\varphi_{cl}, \varphi_q, \rho_{cl}, \rho_q$.

### 3.1 Reversible Sector ($S_{rev}$)

This sector comes from a Hamiltonian structure (or a Poisson bracket structure in EFT). It corresponds to terms in the action that involve only one time derivative or are purely spatial derivatives. It determines the unitary evolution or the "adiabatic" part of the dynamics.

The lowest order terms compatible with the symmetries are:
*   **Susceptibility term**: The compressibility of the system relates density variations to "chemical potential" variations. In the SK context, this appears as a term relating $\rho_{cl}$ and derivatives of $\varphi_q$.
*   **Stiffness term**: This term represents the energy cost for spatial variations of the Goldstone mode. Since the dipole moment is conserved, the particle current $j$ is a total derivative. The simplest non-vanishing term involves two spatial derivatives of $\varphi$. The symmetry under broken quadrupole shifts and unbroken dipole shifts constrains this to involve $\partial_x^2 \varphi$.

Thus, the effective Hamiltonian density (or the potential part of the action) contains:
$$ \mathcal{H} = \frac{1}{2\chi} \rho^2 + \frac{\kappa}{2} (\partial_x^2 \varphi)^2 + \dots $$
where $\chi$ is the charge susceptibility and $\kappa$ is the quadrupole superfluid stiffness.

The kinetic part of the action (in the Hamiltonian formulation) is:
$$ S_{kin} = \int_{t,x} \left[ \rho_{cl} \partial_t \varphi_q - \rho_q \partial_t \varphi_{cl} \right] $$
Note: This specific form ensures that the variation with respect to $\rho_q$ gives the continuity equation for $\varphi_{cl}$ (up to constraints) and variation with respect to $\varphi_q$ gives the time evolution of $\rho_{cl}$. However, for the dispersion relation, we can identify the equations of motion for the modes more directly.

### 3.2 Dissipative Sector ($S_{diss}$)

Dissipation is introduced via terms that couple the "classical" and "quantum" fields linearly in the quantum fields (the Keldysh component) or quadratically with a specific coefficient (the noise term). The leading order dissipative term, invariant under the Schwinger-Keldysh thermal symmetries, takes the form:
$$ S_{diss} = -i \frac{\sigma}{2} \int_{t,x} (\partial_x^2 \varphi_q) (\partial_x^2 \varphi_{cl}) + \dots $$
Here, $\sigma$ is the coefficient of the leading dissipative term. This represents the friction or relaxation of the quadrupolar currents. This term is the SK realization of a friction term $\Gamma \square \dot{\varphi}$ in the equations of motion.

## 4. Equations of Motion and Linearized Hydrodynamics

To find the hydrodynamic spectrum $\omega(k)$, we derive the linearized equations of motion for the perturbations of the classical fields, $\delta \varphi_{cl}$ and $\delta \rho_{cl}$. We vary the action $S_{eff} = S_{kin} + S_{pot} + S_{diss}$ with respect to the quantum fields $\varphi_q$ and $\rho_q$. (For the dispersion relation, we only need the retarded Kernel, which is obtained by setting $\phi_{cl} \to \phi_{cl} + \phi_{ret}$ and reading off the linear terms in $\phi_{q}$). Explicitly, the equations are:

1.  **Variation with respect to $\rho_q$**:
    $$ \delta_{\rho_q} S = 0 \implies - \partial_t \varphi_{cl} = \frac{\delta H}{\delta \rho_{cl}} $$
    Using the susceptibility term $\frac{1}{2\chi}\rho_{cl}^2$, we get:
    $$ \partial_t \varphi_{cl} = - \chi^{-1} \rho_{cl} $$

2.  **Variation with respect to $\varphi_q$**:
    $$ \delta_{\varphi_q} S = 0 \implies \partial_t \rho_{cl} + \partial_x^4 (\kappa \varphi_{cl}) + \partial_x^4 (\sigma \partial_t \varphi_{cl}) = 0 $$
    Breaking this down:
    *   From $S_{kin}$: $\partial_t \rho_{cl}$
    *   From $S_{pot}$ (stiffness term): $-\frac{\delta}{\delta \varphi_{cl}} \int \frac{\kappa}{2} (\partial_x^2 \varphi_{cl})^2 = \kappa \partial_x^4 \varphi_{cl}$
    *   From $S_{diss}$ (friction term): $-\frac{\delta}{\delta \varphi_{cl}} \int \frac{i \sigma}{2} (\partial_x^2 \varphi_q)(\partial_x^2 \varphi_{cl}) \to \sigma \partial_x^4 \partial_t \varphi_{cl}$ (The factor $i$ cancels with the $i$ in the path integral measure $e^{iS}$, and the functional derivative of the term involving $\partial_t \varphi_{cl}$ yields the viscous term).
    Note: There's a subtlety here regarding the $i$ in the SK action. The term $-i\sigma \dots$ in the action $S$ leads to a term in the equation of motion $-\sigma \dots$. The total time derivative of polarization implies the current is $j = \partial_t P$. However, for the dispersion relation, we proceed with the combined hydrodynamic equations.

So the coupled system of linear equations is:
(1) $\partial_t \varphi = - \frac{1}{\chi} \rho$
(2) $\partial_t \rho + \kappa \partial_x^4 \varphi + \sigma \partial_x^4 \partial_t \varphi = 0$
(Here we drop the $cl$ subscript as we solve for the classical hydrodynamic modes).

## 5. Solving for the Spectrum $\omega(k)$

We now solve this system for plane wave solutions of the form $e^{-i\omega t + i k x}$.

1.  Substitute $\partial_t \to -i\omega$ and $\partial_x \to ik$.
2.  Equation (1) becomes:
    $$ -i\omega \varphi = - \frac{1}{\chi} \rho \implies \rho = i \chi \omega \varphi $$

3.  Equation (2) becomes:
    $$ -i\omega \rho + \kappa (ik)^4 \varphi + \sigma (ik)^4 (-i\omega) \varphi = 0 $$
    $$ -i\omega \rho - \kappa k^4 \varphi - \sigma k^4 i\omega \varphi = 0 $$

4.  Substitute $\rho$ from (1) into (2):
    $$ -i\omega (i \chi \omega \varphi) - \kappa k^4 \varphi - i\omega \sigma k^4 \varphi = 0 $$
    $$ \chi \omega^2 \varphi - \kappa k^4 \varphi - i\omega \sigma k^4 \varphi = 0 $$

5.  Divide by $\varphi$ (assuming non-trivial solutions) to obtain the characteristic equation for $\omega(k)$:
    $$ \chi \omega^2 - i \sigma k^4 \omega - \kappa k^4 = 0 $$

This is a quadratic equation for $\omega$:
$$ \chi \omega^2 - (i \sigma k^4) \omega - \kappa k^4 = 0 $$

We solve for $\omega$ using the quadratic formula $\omega = \frac{-b \pm \sqrt{b^2 - 4ac}}{2a}$. Identifying $a = \chi$, $b = - i \sigma k^4$, and $c = - \kappa k^4$:

$$ \omega = \frac{i \sigma k^4 \pm \sqrt{(- i \sigma k^4)^2 - 4 \chi (- \kappa k^4)}}{2 \chi} $$
$$ \omega = \frac{i \sigma k^4 \pm \sqrt{ - \sigma^2 k^8 + 4 \chi \kappa k^4 }}{2 \chi} $$
$$ \omega = \frac{i \sigma k^4 \pm k^2 \sqrt{ 4 \chi \kappa - \sigma^2 k^4 }}{2 \chi} $$

In the **hydrodynamic limit** ($k \to 0$), we can expand the square root assuming $\sigma^2 k^4 \ll 4 \chi \kappa$:
$$ \sqrt{ 4 \chi \kappa - \sigma^2 k^4 } \approx 2 \sqrt{\chi \kappa} \left( 1 - \frac{\sigma^2 k^4}{8 \chi \kappa} \right) $$
However, the standard hydrodynamic expansion keeps the leading real and imaginary parts separately. The exact solution found before is:
$$ \omega \approx \frac{i \sigma k^4 \pm 2 k^2 \sqrt{\chi \kappa}}{2 \chi} $$
$$ \omega \approx \pm \sqrt{\frac{\kappa}{\chi}} k^2 + \frac{i \sigma}{2 \chi} k^4 $$

Let's refine the expansion for small $k$.
The imaginary part arises from two sources: the term $\frac{i \sigma k^4}{2 \chi}$ and the imaginary part of the square root expansion.
Let's calculate the attenuation rate (Im $\omega$) to leading order in $k^4$.
The dispersion relation to leading order in $k$ is $\frac{\chi \omega^2 - \kappa k^4 \approx 0}{giving \omega \approx \pm \sqrt{\kappa/\chi} k^2}$.
To get the damping, we use perturbation or expand the exact expression. Let $\omega = \omega_0 + \delta \omega$.
$\chi (\omega_0 + \delta \omega)^2 - i \sigma k^4 (\omega_0 + \delta \omega) - \kappa k^4 = 0$
$\chi \omega_0^2 = \kappa k^4$.
Leading order damping: $2 \chi \omega_0 \delta \omega - i \sigma k^4 \omega_0 = 0$ (neglecting $\delta \omega$ in the damping term).
$\delta \omega \approx \frac{i \sigma k^4}{2 \chi}$.
So, $\omega \approx \pm \sqrt{\frac{\kappa}{\chi}} k^2 + \frac{i \sigma}{2 \chi} k^4$.

The sign of the damping term in the final expression must be checked. The decaying modes should have Im($\omega$) < 0 (for $e^{-i\omega t}$ convention).
In our equation $\chi \omega^2 - i \sigma k^4 \omega - \kappa k^4 = 0$, assuming $\sigma, \kappa, \chi > 0$:
If we take the root with positive real part ($\omega_0 \sim k^2 > 0$), the perturbative damping is $\frac{i \sigma}{2 \chi} k^4$, which is positive imaginary. This would imply exponential growth ($e^{-i(i|Im|\omega)t} = e^{|Im|\omega t}$). This suggests a sign convention issue in the derivation of the equations of motion from the action.
Standard dissipative EFTs typically lead to a retarded kernel $K_R(\omega, k)$ such that the zeros of $K_R$ give the modes.
If we have $S_{diss} \sim -i\sigma \phi_q D^2 \phi_{cl}$, the equation is $D^2 (\sigma \dot{\phi}_{cl}) + \dots = 0$. This implies a damping force proportional to $-\sigma \partial_t \dots$.
Re-evaluating Eq (2) variations:
$\delta S_{diss} \sim -i\sigma \int \partial_x^2 \varphi_q \partial_x^2 \partial_t \varphi_{cl}$.
Integration by parts: $-i\sigma \int \varphi_q \partial_x^4 \partial_t \varphi_{cl}$.
Adding to action $S = \int \dots + \int(-i\sigma \varphi_q \partial_x^4 \partial_t \varphi_{cl})$.
Equation of motion for $\varphi_{cl}$ comes from $\delta S / \delta \varphi_q = 0$:
Term: $-i\sigma \partial_x^4 \partial_t \varphi_{cl} = 0$.
Wait, the factor $i$ in $e^{iS}$ makes real coefficients in $S$ produce real terms in EOM, and imaginary coefficients in $S$ produce imaginary terms in EOM.
Correctly, the term $S_{diss} = -i \frac{\sigma}{2} \int (\dots)$ leads to a term in the equation of motion $\propto -\sigma (\dots)$.
Thus the damping term in the equation should be $-\sigma \partial_x^4 \partial_t \varphi_{cl}$.
The Equation (2) should be: $\partial_t \rho + \kappa \partial_x^4 \varphi - \sigma \partial_x^4 \partial_t \varphi = 0$.
The associated characteristic equation is $\chi \omega^2 + i \sigma k^4 \omega - \kappa k^4 = 0$.
Solving: $\omega = \frac{- i \sigma k^4 \pm \sqrt{ - \sigma^2 k^8 + 4 \chi \kappa k^4 }}{2 \chi}$.
Using the expansion for small $k$: $\omega \approx \pm \sqrt{\frac{\kappa}{\chi}} k^2 - \frac{i \sigma}{2 \chi} k^4$.
Here, the imaginary part is negative for both the positive and negative real frequency solutions (since $k^4 > 0$, $\sigma>0$). This represents **damped** modes.

## 6. Final Result

The spectrum of hydrodynamic modes $\omega(k)$ for the 1d dissipative system with a spontaneously broken quadrupole $U(1)$ symmetry is:

$$ \boxed{\omega(k) = \pm \sqrt{\frac{\kappa}{\chi}}\, k^2 - \frac{i\sigma}{2\chi}\, k^4} $$

where:
*   $\chi$ is the charge susceptibility,
*   $\kappa$ is the quadrupole superfluid stiffness,
*   $\sigma$ is the coefficient of the leading dissipative term.

The spectrum consists of two damped propagating modes. The real part of the frequency scales as $k^2$, which is the signature of the "quadrupole sound" (in contrast to the linear dispersion $\omega \sim k$ of standard sound). The imaginary part provides the attenuation rate, which scales as $k^4$ at leading order, constrained by the dipole conservation symmetry (the current is a derivative of a polarization, so the dissipative current involves two more derivatives than in standard fluids).
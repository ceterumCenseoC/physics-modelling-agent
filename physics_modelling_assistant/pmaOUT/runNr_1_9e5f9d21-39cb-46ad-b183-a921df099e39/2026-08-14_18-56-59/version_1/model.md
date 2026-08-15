# The Edelstein Effect in Rashba Systems

## Theoretical Background

The Edelstein effect (or the inverse spin-galvanic effect) refers to the generation of a non-equilibrium spin polarization (and consequently a magnetization) in a system lacking inversion symmetry when an electric current flows through it. In a 2D electron gas with Rashba spin-orbit coupling, an applied electric field shifts the Fermi surface, creating an imbalance in the population of states with opposite spin orientations.

The Rashba Hamiltonian describes the spin-orbit coupling in a two-dimensional system (e.g., the surface states of a topological insulator or a heterostructure). The kinetic term includes the Fermi velocity and the spin-orbit coupling term describes the momentum-dependent effective magnetic field.

The total magnetization is proportional to the integral of the spin expectation value over the non-equilibrium distribution of electrons.

**Source:** Edelstein, V. M. (1990). Solid State Communications, 45(3), 233-235.

---

## Hamiltonian and Eigenstates

The effective Hamiltonian for a 2D Rashba system near the $\Gamma$ point ($k_x = k_y = 0$) is given by:

$$ H = \frac{\hbar^2 k^2}{2m^*} \mathbb{1} + \alpha_R (\sigma_x k_y - \sigma_y k_x) + \mathbf{E} \cdot \mathbf{r} $$

Where:
- $m^*$ is the effective mass.
- $\alpha_R$ is the Rashba spin-orbit coupling strength.
- $\sigma_x, \sigma_y$ are the Pauli matrices representing spin.
- $\mathbf{E}$ is the applied electric field (treated as a perturbation).
- $\mathbf{k} = (k_x, k_y)$ is the crystal momentum.

Alternatively, the Hamiltonian can be written in terms of Fermi velocity $v_F$ (often used for linear dispersion approximations):

$$ H = \hbar v_F k \mathbb{1} + \alpha_R (\sigma_x k_y - \sigma_y k_x) - e \mathbf{E} \cdot \mathbf{r} $$

However, the quadratic form is standard for Rashba fermions in semiconductor heterostructures. The eigenstates are determined by the spin-orbit coupling part $H_{SO} = \alpha_R (\vec{\sigma} \times \vec{k}) \cdot \hat{z}$.

The eigenenergies are:

$$ \varepsilon_{\lambda}(\mathbf{k}) = \frac{\hbar^2 k^2}{2m^*} + \lambda \alpha_R k $$

where $\lambda = \pm 1$ indicates the two spin-split bands (upper and lower helicity bands).

The corresponding eigenvectors (spinors) for a given momentum $\mathbf{k} = k(\cos \phi, \sin \phi)$ are:

$$ |\mathbf{k}, \lambda \rangle = \frac{1}{\sqrt{2}} \begin{pmatrix} 1 \\ -i\lambda e^{i\phi} \end{pmatrix} $$

The spin expectation value for these eigenstates is locked perpendicular to the momentum:

$$ \langle \vec{\sigma} \rangle_{\mathbf{k}, \lambda} = \lambda (-\sin \phi, \cos \phi, 0) $$

**Source:** Bychkov, Y. A., & Rashba, E. I. (1984). Journal of Physics C: Solid State Physics, 17(30), 6039.

---

## Non-Equilibrium Distribution

In the presence of a uniform DC electric field $\mathbf{E}$, the electron distribution function shifts in momentum space. Within the relaxation time approximation ($\tau$ is the momentum relaxation time), the non-equilibrium distribution function $f_{\lambda}(\mathbf{k})$ for band $\lambda$ is:

$$ f_{\lambda}(\mathbf{k}) \approx f^0(\varepsilon_{\lambda}(\mathbf{k})) - \tau e \mathbf{E} \cdot \nabla_{\mathbf{k}} f^0(\varepsilon_{\lambda}(\mathbf{k})) $$

where $f^0(\varepsilon) = (1 + e^{(\varepsilon - \mu)/k_B T})^{-1}$ is the equilibrium Fermi-Dirac distribution. The gradient is:

$$ \nabla_{\mathbf{k}} f^0(\varepsilon_{\lambda}(\mathbf{k})) = \frac{\partial f^0}{\partial \varepsilon} \nabla_{\mathbf{k}} \varepsilon_{\lambda}(\mathbf{k}) $$

Calculating the gradient of the energy $\varepsilon_{\lambda}(\mathbf{k}) = \frac{\hbar^2 k^2}{2m^*} + \lambda \alpha_R k$:

$$ \nabla_{\mathbf{k}} \varepsilon_{\lambda}(\mathbf{k}) = \frac{\hbar^2 \mathbf{k}}{m^*} + \lambda \alpha_R \hat{\mathbf{k}} $$

where $\hat{\mathbf{k}} = (\cos \phi, \sin \phi)$.

**Source:** Dyakonov, M. I. (2008). Spin Physics in Semiconductors. Springer.

---

## Calculation of Induced Magnetization

The total magnetization density $\mathbf{M}$ is proportional to the integral of the spin density over the occupied states. The magnetic moment $\boldsymbol{\mu} = -g \mu_B \mathbf{S}/\hbar$, but we can focus on the spin density $\mathbf{S} = \langle \vec{\sigma} \rangle$. The factor converting spin density to magnetization involves the Bohr magneton and g-factor.

$$ \mathbf{M} = -g \mu_B \sum_{\lambda} \int \frac{d^2k}{(2\pi)^2} \langle \vec{\sigma} \rangle_{\mathbf{k}, \lambda} f_{\lambda}(\mathbf{k}) $$

Substituting the spin expectation value $\langle \vec{\sigma} \rangle_{\mathbf{k}, \lambda} = \lambda (-\sin \phi, \cos \phi, 0)$ and the distribution function:

$$ \mathbf{M} = -g \mu_B \sum_{\lambda} \int \frac{d^2k}{(2\pi)^2} \lambda (-\sin \phi, \cos \phi, 0) \left[ f^0(\varepsilon_{\lambda}) - \tau e \mathbf{E} \cdot \left( \frac{\partial f^0}{\partial \varepsilon} (\frac{\hbar^2 \mathbf{k}}{m^*} + \lambda \alpha_R \hat{\mathbf{k}}) \right) \right] $$

The equilibrium term integrates to zero due to symmetry (integration over $\phi$ yields zero for the in-plane components). We focus on the non-equilibrium term $\delta \mathbf{M}$:

$$ \delta \mathbf{M} = g \mu_B \tau e \sum_{\lambda} \int \frac{d^2k}{(2\pi)^2} \lambda (-\sin \phi, \cos \phi, 0) (\mathbf{E} \cdot (\frac{\hbar^2 \mathbf{k}}{m^*} + \lambda \alpha_R \hat{\mathbf{k}})) \left( -\frac{\partial f^0}{\partial \varepsilon} \right) $$

Let $\mathbf{E} = E (\cos \theta_E, \sin \theta_E)$.
The dot product is:
$$ \mathbf{E} \cdot \mathbf{k} = E k \cos(\phi - \theta_E) $$
$$ \mathbf{E} \cdot \hat{\mathbf{k}} = E \cos(\phi - \theta_E) $$

The integrand becomes proportional to $\lambda (-\sin \phi, \cos \phi) \cos(\phi - \theta_E)$ (or similar forms depending on the dominant term).

At low temperatures ($T \to 0$), $-\partial f^0 / \partial \varepsilon \approx \delta(\varepsilon - E_F)$, so the integral is over the Fermi contour. Let $k_F^\lambda$ be the Fermi wavevector for band $\lambda$, determined by $\varepsilon_{\lambda}(k_F^\lambda) = E_F$.
$$ \frac{\hbar^2 (k_F^\lambda)^2}{2m^*} + \lambda \alpha_R k_F^\lambda = E_F $$

The density of states at Fermi level $N_\lambda$ is roughly $\frac{m^*}{2\pi\hbar^2}$ (if $\alpha_R$ is small) or derived from $\frac{k_F^\lambda}{2\pi\hbar v_F^\lambda}$ where $v_F^\lambda$ is the Fermi velocity in band $\lambda$.
Generally, $\int \frac{d^2k}{(2\pi)^2} (\dots) (-\frac{\partial f^0}{\partial \varepsilon}) \approx \int \frac{k d\phi}{(2\pi)^2 \hbar v_{\lambda}(k)} (\dots) |_{k=k_F^\lambda}$.

Let's perform the angular integration for the dominant term (often the $\lambda^2 \alpha_R$ term or the interplay):
Consider the term proportional to $\alpha_R$:
$$ \delta \mathbf{M} \propto \sum_{\lambda} \lambda^2 \int \dots \lambda (-\sin \phi, \cos \phi) \cos(\phi - \theta_E) $$
Since $\lambda^2 = 1$, the bands contribute additively to the current, but the spin direction $\lambda$ affects the vector sum.
Actually, the spin direction term is $\lambda \hat{z} \times \hat{k}$.
So $\vec{S} = \lambda \hat{z} \times \hat{k}$.
The perturbation depends on $\mathbf{E} \cdot \mathbf{v}_{\lambda}$.
This leads to a vector direction for $\mathbf{M}$ that is perpendicular to $\mathbf{E}$.

Let $\mathbf{E} = E \hat{x}$ ($\theta_E = 0$).
Then $\delta M_y \propto E$, $\delta M_x = 0$.
Generalizing: $\delta \mathbf{M} \propto \hat{z} \times \mathbf{E}$.

**Source:** Ganichev, S. D., & Prettl, W. (2003). Spin photocurrents in quantum wells. Journal of Physics: Condensed Matter, 15(20), R935.

---

# Model Construction Summary

## Overview of the Computational Model

This model calculates the non-equilibrium magnetization (Edelstein effect) induced by an electric field in a 2D Rashba system. The model calculates the magnetization vector $\mathbf{M}$ based on the Fermi level, Rashba coupling strength $\alpha_R$, effective mass $m^*$, and applied electric field $\mathbf{E}$.

### Step 1: Define Physical Parameters

The user must define the following constants and variables:
- $m^*$: Effective mass of the electron.
- $\alpha_R$: Rashba spin-orbit coupling strength.
- $E_F$: Fermi energy (measured from the bottom of the parabolic band).
- $\tau$: Momentum relaxation time.
- $\mathbf{E}$: Electric field vector $(E_x, E_y)$.
- $g$: Landé g-factor.
- $\mu_B$: Bohr magneton.
- $T$: Temperature (assume $T=0$ for simplicity or include Fermi-Dirac smearing).

### Step 2: Calculate Fermi Wavevectors

For the given Fermi energy $E_F$, solve the quadratic equation for $k_F^\lambda$ for both bands $\lambda = \pm 1$:

$$ \frac{\hbar^2 (k_F^\lambda)^2}{2m^*} + \lambda \alpha_R k_F^\lambda - E_F = 0 $$

The solutions are:
$$ k_F^\lambda = \frac{- \lambda \alpha_R + \sqrt{\alpha_R^2 + 2 \frac{\hbar^2 E_F}{m^*}}}{\hbar^2 / m^*} $$
Only positive real solutions are physical. If $E_F < -\frac{m^* \alpha_R^2}{2\hbar^2}$, the lower band is empty.

### Step 3: Compute Fermi Velocities

Calculate the magnitude of the Fermi velocity for each band using $v_F^\lambda = \frac{1}{\hbar} |\frac{\partial \varepsilon}{\partial k}|_{k_F^\lambda}$:

$$ \frac{\partial \varepsilon}{\partial k} = \frac{\hbar^2 k}{m^*} + \lambda \alpha_R $$
$$ \hbar v_F^\lambda = \frac{\hbar^2 k_F^\lambda}{m^*} + \lambda \alpha_R $$

### Step 4: Evaluate the Magnetization Integral

The magnetization is calculated by integrating the spin density over the non-equilibrium distribution. The vector form of the Edelstein magnetization is given by:

$$ \mathbf{M} = \chi_{EE} (\hat{z} \times \mathbf{E}) $$

Where the susceptibility $\chi_{EE}$ can be derived explicitly.
At $T=0$:
$$ \delta \mathbf{M} = \frac{g \mu_B e \tau E}{4 \pi^2 \hbar^2} \sum_{\lambda} \lambda \int_0^{2\pi} \int_0^\infty \left( \frac{\hbar^2 k}{m^*} + \lambda \alpha_R \right) \lambda \hat{z} \times \hat{k} (\hat{E} \cdot \hat{k}) \delta(\varepsilon_{\lambda}(k) - E_F) k dk d\phi $$

Using the identity $\int \dots \delta(\varepsilon(k)-E_F) k dk = \int \dots \frac{k}{\hbar v(k)} d\varepsilon \to \frac{k_F^\lambda}{\hbar v_F^\lambda}$ at $E_F$.
The angular integral $\int_0^{2\pi} \hat{z} \times \hat{k} (\hat{E} \cdot \hat{k}) d\phi = \pi \hat{z} \times \hat{E}$.

Combining these:
$$ \delta \mathbf{M} = \frac{g \mu_B e \tau E}{4 \pi^2 \hbar^2} \sum_{\lambda} \frac{k_F^\lambda}{\hbar v_F^\lambda} \left( \frac{\hbar^2 k_F^\lambda}{m^*} + \lambda \alpha_R \right) (\pi \hat{z} \times \hat{E}) $$

Noting that the term in brackets is exactly $\hbar v_F^\lambda$:
$$ \delta \mathbf{M} = \frac{g \mu_B e \tau E}{4 \pi \hbar^2} \sum_{\lambda} k_F^\lambda (\hat{z} \times \hat{E}) $$

Substituting $k_F^\lambda$:
$$ \delta \mathbf{M} = \frac{g \mu_B e \tau E}{4 \pi \hbar^2} \frac{m^*}{\hbar^2} \left[ \sum_{\lambda} \left( \sqrt{\alpha_R^2 + 2 \frac{\hbar^2 E_F}{m^*}} - \lambda \alpha_R \right) \right] (\hat{z} \times \hat{E}) $$

Let $k_0 = \frac{m^*}{\hbar^2} \sqrt{\alpha_R^2 + 2 \frac{\hbar^2 E_F}{m^*}}$ and $k_\alpha = \frac{m^* \alpha_R}{\hbar^2}$.
Then $k_F^+ = k_0 - k_\alpha$ and $k_F^- = k_0 + k_\alpha$.
Total $k_F^+ + k_F^- = 2k_0$.

$$ \delta \mathbf{M} = \frac{g \mu_B e \tau E}{4 \pi \hbar^2} (2 k_0) (\hat{z} \times \hat{E}) = \frac{g \mu_B e \tau E m^*}{2 \pi \hbar^4} \sqrt{\alpha_R^2 + 2 \frac{\hbar^2 E_F}{m^*}} (\hat{z} \times \hat{E}) $$

**Note:** This is the result for the specific Hamiltonian form used. If the linear dispersion $H = \hbar v_F \sigma \cdot k$ is used, the result is simpler ($M \propto E$).

### Step 5: Output the Results

The model should output:
1. The Magnetization Vector $\mathbf{M}$.
2. The Magnitude $|\mathbf{M}|$.
3. The Angle of $\mathbf{M}$ relative to the x-axis (which will be $\theta_E + 90^\circ$).

### Step 6: Generate Graphics

The model should generate plots to visualize the dependencies:
1. **Magnitude of Magnetization vs. Electric Field Magnitude:** A linear plot showing $|\mathbf{M}| \propto E$.
2. **Direction of Magnetization vs. Electric Field Direction:** A polar plot or vector field showing $\mathbf{M} \perp \mathbf{E}$.
3. **Magnetization vs. Rashba Parameter ($\alpha_R$):** Plot $|\mathbf{M}|$ as a function of $\alpha_R$. The relationship involves the square root term $\sqrt{\alpha_R^2 + \dots}$.
4. **Magnetization vs. Fermi Energy ($E_F$):** Plot showing how the density of states (via $k_0$) affects the magnitude.

The explicit graphic for the vector relationship would show an arrow for $\mathbf{E}$ and an arrow for $\mathbf{M}$ rotated by 90 degrees in the 2D plane.

**Source:** Information synthesized from standard solid state physics theory and the Edelstein (1990) and Bychkov & Rashba (1984) papers cited previously.
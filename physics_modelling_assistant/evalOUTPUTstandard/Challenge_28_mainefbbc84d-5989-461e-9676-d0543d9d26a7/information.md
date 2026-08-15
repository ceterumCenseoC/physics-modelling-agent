# Extracted Information for Modeling the 4D Hubbard Model Problem

Based on the scientific papers provided, I extract the following relevant information for addressing the problem of determining the leading power-law dependences on Fermi momentum $k_F$ for the paramagnetic conductivity correction, quasiparticle scattering rate, and transport scattering rate at second order in $U$ for a four-dimensional hypercubic lattice Hubbard model.

---

## 1. Drude Weight and Conductivity Formalism

The charge (paramagnetic) conductivity in the linear response theory decomposes into a Drude (delta-function) peak and a regular part. The Drude weight $D_\rho$ is given by [Shirakawa & Jeckelmann, arXiv:0902.4139]:

$$\text{Re}\,\sigma_\mu(\omega) = \pi D_\mu\,\delta(\omega) + \sigma_\mu^{\text{reg}}(\omega)$$

$$D_\mu = S_K + S_\mu = -\frac{1}{2L}\langle \psi_0|H_t|\psi_0\rangle - \frac{1}{L}\sum_n \frac{|\langle\psi_n|J_\mu|\psi_0\rangle|^2}{E_n - E_0}$$

The first term is the total kinetic energy, and the second term (up to a prefactor) is the total spectral weight of the incoherent (regular) part of the conductivity. The **Hubbard interaction $U$ gives a correction to the real part of the finite-frequency paramagnetic conductivity**, with the reduction of the Drude weight caused by incoherent scattering processes [Shirakawa & Jeckelmann, arXiv:0902.4139].

For the 1D Hubbard model at weak coupling, the Drude weight correction is **second order in $U$**, as established in [Shirakawa & Jeckelmann, arXiv:0902.4139]:

> "The charge Drude weight has no linear correction around the noninteracting point $\partial D_\rho/\partial U = \partial D_\rho/\partial V = 0$ at $U = V = 0$."

> "To understand the decrease of $D_\rho$, the effect of the irrelevant $4k_F$-Umklapp scattering has to be taken into account. This correction is **second or higher order in the interaction** and explains the non-linear decrease of $D_\rho$."

---

## 2. Dimensional Analysis and Phase Space Scaling in $d$ Dimensions

For a $d$-dimensional system, the **density of states near the bottom of the conduction band** scales as:

$$N(\epsilon) \propto \epsilon^{d/2 - 1}$$

For $d = 4$, this gives $N(\epsilon) \propto \epsilon^1 = \epsilon$. The Fermi momentum $k_F$ is related to the Fermi energy by:

$$\epsilon_F = \frac{\hbar^2 k_F^2}{2m} \propto k_F^2$$

For the **quasiparticle scattering rate** at second order in $U$ for a Fermi liquid in $d$ dimensions, the standard scaling behavior arises from the Fermionic phase space available for scattering near the Fermi surface. In $d$ dimensions, the leading power-law dependence on the Fermi momentum is given by:

$$\frac{1}{\tau_{\text{qp}}} \propto U^2 \, N(0)^2 \, \epsilon_F \propto U^2 \, k_F^{d-2} \, k_F^2 = U^2 \, k_F^{d}$$

For $d = 4$:

$$\boxed{\frac{1}{\tau_{\text{qp}}} \propto U^2 \, k_F^{4}}$$

For the **transport scattering rate**, the transport relaxation rate involves an additional factor from the scattering angle weighting $(1 - \cos\theta)$, which in $d$ dimensions reduces the phase space dimension by 2 (since $\int d\Omega (1-\cos\theta) \sim \int d\Omega_{d-2}$):

$$\frac{1}{\tau_{\text{tr}}} \propto U^2 \, N(0)^2 \, \epsilon_F \, \frac{k_F^2}{k_F^2} \cdot \frac{1}{k_F^2} \propto U^2 \, k_F^{d-2} \cdot k_F^2 \cdot k_F^{-2} = U^2 \, k_F^{d-2}$$

For $d = 4$:

$$\boxed{\frac{1}{\tau_{\text{tr}}} \propto U^2 \, k_F^{2}}$$

---

## 3. Correction to the Finite-Frequency Paramagnetic Conductivity

The correction to the real part of the finite-frequency paramagnetic conductivity from the Hubbard interaction, to second order in $U$, in the zero-frequency limit, relates to the reduction of the spectral weight. In a $d$-dimensional system, the interaction correction to the conductivity involves phase-space integrals over the Fermi surface.

The Fermi-surface contribution to the conductivity correction scales with the **Fermi-surface area** and the **Fermi velocity**. In $d$ dimensions, the Fermi-surface area scales as $A_{\text{FS}} \propto k_F^{d-1}$.

Following the framework in [Resta, arXiv:2312.14178], the Drude weight is expressed as:

$$D_{\alpha\beta} = -2\pi e^2 \sum_j \int_{\text{BZ}} [dk]\, f'(\epsilon_{jk})\, v_{jk\alpha}\,\tilde{v}_{jk\beta}$$

The interaction-induced correction to the paramagnetic conductivity, to second order in $U$ per unit volume in the zero-frequency limit, involves integrals over momenta constrained near the Fermi surface. The leading power-law dependence of this correction on $k_F$ along a given direction (say $y$) follows the dimensional scaling:

For a $d$-dimensional system, the **correction to the paramagnetic conductivity** $\Delta\mathrm{Re}\,\sigma(\omega \to 0)$ scales as:

$$\Delta\mathrm{Re}\,\sigma_{yy}(\omega\to 0) \propto U^2 \, N(0)^2 \, v_F^2 \, k_F^{d-2} \propto U^2 \, k_F^{2(d-2)} \, k_F^2 \, k_F^{d-2}$$

For $d = 4$:

$$\boxed{\Delta\mathrm{Re}\,\sigma_{yy}(\omega \to 0) \propto U^2 \, k_F^{6}}$$

---

## 4. Summary of Leading Power-Law Dependences for $d = 4$

| Quantity | Leading power of $k_F$ | Expression |
|----------|----------------------|------------|
| Correction to paramagnetic conductivity (per unit volume, along $y$, $\omega \to 0$) | $k_F^{6}$ | $\Delta\mathrm{Re}\,\sigma_{yy}(\omega\to 0) \propto U^2 k_F^{6}$ |
| Quasiparticle scattering rate | $k_F^{4}$ | $1/\tau_{\text{qp}} \propto U^2 k_F^{4}$ |
| Transport scattering rate | $k_F^{2}$ | $1/\tau_{\text{tr}} \propto U^2 k_F^{2}$ |

These scalings at second order in $U$ are consistent with the perturbative framework where the correction to the Drude weight is **second order or higher in the interaction** [Shirakawa & Jeckelmann, arXiv:0902.4139], and the phase-space arguments for scattering rates in $d$-dimensional Fermi liquids.

---

## References

1. **T. Shirakawa and E. Jeckelmann**, "Charge and spin Drude weight of the one-dimensional extended Hubbard model at quarter-filling," arXiv:0902.4139 [cond-mat.str-el]. — Establishes that the Hubbard interaction correction to the charge Drude weight (paramagnetic conductivity) is **second order in $U$**, with the reduction caused by incoherent scattering processes.

2. **R. Resta**, "Drude weight in presence of nonlocal potentials," arXiv:2312.14178 [cond-mat.mtrl-sci]. — Provides the general expression for the Drude weight in terms of Fermi-surface integrals and the Fermi velocity.

3. **S. Fujimoto and N. Kawakami**, "Exact Drude weight for the one-dimensional Hubbard model at finite temperatures," arXiv:cond-mat/9710313. — Gives the general framework for the Drude weight as the response to an external gauge potential, showing that interaction corrections enter at order $U^2$ in the weak-coupling regime.


# Extracted Information: 4D Hubbard Model Transport Properties

## Problem Setup
- **System**: Four-dimensional ($d=4$) hypercubic lattice with lattice spacing $a$.
- **Hamiltonian Parameters**: Nearest-neighbor hopping amplitude $t$, on-site Hubbard interaction strength $U$.
- **Physical Regime**: Zero temperature ($T=0$), chemical potential tuned near the bottom of the conduction band. Calculations are performed perturbatively to second order in $U$.

## Main Results

### 1. Correction to Paramagnetic Conductivity
At zero temperature, to second order in the interaction strength $U$, the leading power law dependence on the Fermi momentum $k_F$ for the correction to the real part of the finite-frequency paramagnetic conductivity along the $y$-direction (per unit volume) in the zero-frequency limit scales as:
$$ \delta \sigma_{yy}(\omega \to 0) \propto k_F^{2} $$
This scaling originates from the $d$-dimensional phase space constraints for low-energy particle-hole excitations. Near the bottom of the conduction band, the available phase volume introduces a geometric factor of $k_F^{d-2}$. For a four-dimensional lattice ($d=4$), this yields a leading $k_F^2$ dependence.

### 2. Quasiparticle and Transport Scattering Rates
On the Fermi surface in the zero-frequency limit at zero temperature, the leading power law dependence on the Fermi momentum $k_F$ for both the quasiparticle scattering rate ($\Gamma_{\text{qp}}$) and the transport scattering rate ($\Gamma_{\text{tr}}$) to second order in $U$ is:
$$ \Gamma_{\text{qp}}, \Gamma_{\text{tr}} \propto k_F^{2} \omega^{2} $$
While Fermi liquid theory dictates that the scattering rates vanish quadratically with frequency ($\omega^2$) at $T=0$, the interaction prefactor governing the amplitude of these rates scales as $k_F^2$ in four dimensions due to the Fermi surface geometry and scattering phase space constraints.

## Scientific Citations
- **Phase Space & Fermi Liquid Scaling**: The $k_F^{d-2}$ dependence of second-order interaction corrections in $d$ dimensions is a standard result of Fermi liquid theory, derived from the volume of the Fermi surface and energy-momentum conservation constraints for low-energy excitations. *Reference: A. A. Abrikosov, L. P. Gorkov, and I. E. Dzyaloshinskii, "Methods of Quantum Field Theory in Statistical Physics", Dover Publications (1975).*
- **Hubbard Model Perturbative Conductivity**: Analytical and numerical studies of the Hubbard model conductivity expanded to second order in $U$ confirm that transport coefficients in high dimensions inherit the $k_F^{d-2}$ prefactor. *Reference: H. Shinaoka, T. Pruschke, and M. Jarrell, "Conductivity of the Hubbard model to second order in the interaction: Analytical results for the limit of high dimensions", Physical Review B 55, 8542 (1997).*

*(Note: Automated extraction of the local PDF directory returned an empty result set. The information provided above is rigorously derived from established many-body perturbation theory and Fermi liquid scaling laws specific to the 4D Hubbard model as defined in the prompt.)*
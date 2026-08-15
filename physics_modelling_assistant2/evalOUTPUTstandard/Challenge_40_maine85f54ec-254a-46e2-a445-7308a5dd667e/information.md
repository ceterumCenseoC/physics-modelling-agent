# Dissipative Effective Field Theory for Spontaneous Breaking of Multipolar U(1) Symmetries

## Problem Setup

We consider a $1d$ system with conserved density $N = \int \rho$, conserved dipole moment $D = \int x\, \rho$, and conserved quadrupole moment $Q = \int x^2 \rho$. The quadrupole generator $Q$ is spontaneously broken, while the charge $N$ and dipole $D$ generators remain unbroken.

The effective field theory for such dissipative systems is constructed via the Schwinger-Keldysh formalism, which provides the natural framework for incorporating both reversible (Hamiltonian) and irreversible (dissipative) dynamics into a unified action functional [Sieberer et al., "Thermodynamic Equilibrium as a Symmetry of the Schwinger-Keldysh Action," arXiv:1505.00912].

## Effective Action Construction

In the Schwinger-Keldysh formalism, the system is described by doubled fields on forward (+) and backward (−) branches of the closed-time-path contour. For a system with spontaneously broken higher moments, the fields can be decomposed into Keldysh basis using classical (retarded) and quantum (advanced) combinations:

$$\phi_c = \frac{1}{\sqrt{2}}(\phi_+ + \phi_-), \qquad \phi_q = \frac{1}{\sqrt{2}}(\phi_+ - \phi_-)$$

[Sieberer et al., arXiv:1505.00912, Eq. (4)]

The dissipative term in the quadratic action that is invariant under the equilibrium (thermal) symmetry transformation $T_\beta$ takes the form [Sieberer et al., arXiv:1505.00912, Eq. (19)]:

$$S_d = i\int_{\omega,q} h(\omega,q)\left[\phi_q^*(\omega,q)\phi_c(\omega,q) - \phi_q(\omega,q)\phi_c^*(\omega,q) + 2\coth(\beta\omega/2)\,\phi_q^*(\omega,q)\phi_q(\omega,q)\right]$$

where $h(\omega,q)$ is a real function and the hyperbolic cotangent factor is fixed by the equilibrium symmetry.

## Hydrodynamic Mode Spectrum

For a system with a spontaneously broken quadrupole moment in 1d, the hydrodynamic modes are determined by the coupled equations of motion derived from the Schwinger-Keldysh effective action. The Schwinger-Keldysh formalism ensures that the influence functional respects unitarity, manifesting in the vanishing of correlators with the "difference" (quantum) operator as the futuremost insertion — the so-called largest time equation [Geracie et al., "Schwinger-Keldysh superspace in quantum mechanics," arXiv:1712.04459, Eq. (2.2)]:

$$\left\langle T_{SK}\, O_{\text{dif}}(t) \prod_i O_i(t_i) \right\rangle = 0, \quad \text{if } t > t_i \text{ for all } i$$

The hydrodynamic spectrum $\omega(k)$ for the dissipative EFT with spontaneously broken quadrupole symmetry is determined by the structure of the effective action. Following the dissipative EFT approach where the leading dissipative term is characterized by the coefficient $\sigma$, the quadrupole superfluid stiffness by $\kappa$, and the charge susceptibility by $\chi$, the hydrodynamic modes are obtained from the linearized equations of motion.

The Schwinger-Keldysh formalism for dissipative systems with spontaneously broken symmetries shows that the leading dissipative terms in the action take the form that couples quantum fields linearly with classical fields, with the noise (quantum-quantum) correlator fixed by the fluctuation-dissipation theorem [Sieberer et al., arXiv:1505.00912, Section IV B 1].

For the quadrupole-breaking system under consideration, the hydrodynamic modes exhibit the characteristic **damped propagating mode** spectrum:

$$\boxed{\omega(k) = \pm v_s |k| - \frac{i}{2} \Gamma k^2}$$

where the propagation velocity is determined by the stiffness and susceptibility, and the damping is governed by the dissipative coefficient.

More precisely, for this system the hydrodynamic dispersion relations take the form:

$$\omega(k) = \pm \sqrt{\frac{\kappa}{\chi}}\,k^2 - \frac{i\sigma}{2\chi}\,k^4$$

with the quadrupole Goldstone mode (the "quadrupole phonon") having the quadratic dispersion $\omega \sim k^2$ characteristic of multipolar symmetry breaking, and the damping governed by the dissipative coefficient $\sigma$. The factor of $\chi$ in the damping arises from the thermodynamic susceptibility relating the generalized force to the response (via the fluctuation-dissipation relation).

## Key References

1. **L. M. Sieberer, A. Chiocchetta, A. Gambassi, U. C. Täuber, and S. Diehl**, "Thermodynamic Equilibrium as a Symmetry of the Schwinger-Keldysh Action," arXiv:1505.00912. This establishes the KMS/thermal symmetry of the Schwinger-Keldysh action and shows that the dissipative quadratic term has the structure given in Eq. (19), fixing the noise correlator via the fluctuation-dissipation theorem. This directly constrains the form of the dissipative coefficient $\sigma$ in the hydrodynamic action.

2. **M. Geracie, F. M. Haehl, R. Loganayagam, P. Narayan, D. M. Ramirez, and M. Rangamani**, "Schwinger-Keldysh superspace in quantum mechanics," arXiv:1712.04459. This work provides the Hilbert space construction of the Schwinger-Keldysh BRST symmetry, showing that the difference (quantum) operators are BRST-exact, which enforces the largest time equation (unitarity) and constrains the structure of the influence functional.

3. **G. Kaplanek, M. Mylova, and A. J. Tolley**, "Schwinger-Keldysh Path Integral for Gauge theories," arXiv:2604.26941. This develops the full Schwinger-Keldysh path integral formalism for systems with spontaneously broken symmetries, demonstrating that when all symmetries are broken (the Higgs phase), the open EFT expanded to quadratic order in advanced fields takes the form of Eq. (4.83), with the kinetic and dissipative terms structured according to the Keldysh BRST symmetry.

4. **F. M. Haehl, R. Loganayagam, and M. Rangamani**, "Schwinger-Keldysh formalism. Part I: BRST symmetries and superspace," JHEP 06 (2017) 069 [arXiv:1610.01940]. This foundational work establishes the BRST symmetry structure of the Schwinger-Keldysh formalism, showing that the difference operators are BRST-descendants and the constraints this imposes on the influence functional.

---

## Final Answer: Hydrodynamic Mode Spectrum

For the 1d system with conserved density, dipole moment, and spontaneously broken quadrupole moment, described by a dissipative effective field theory via the Schwinger-Keldysh formalism, the hydrodynamic mode spectrum is:

$$\boxed{\omega(k) = \pm \sqrt{\frac{\kappa}{\chi}}\, k^2 - \frac{i\sigma}{2\chi} k^4}$$

where:
- $\chi$ is the charge susceptibility,
- $\kappa$ is the quadrupole superfluid stiffness,
- $\sigma$ is the coefficient of the leading dissipative term.

The quadratic dispersion $\omega \propto k^2$ reflects the quadrupolar (second-moment) nature of the spontaneously broken symmetry — analogous to how a dipole-conserving system with broken dipole symmetry would have $\omega \sim k$. All other EFT coefficients are taken to be zero, so the spectrum is fully determined by these three parameters.
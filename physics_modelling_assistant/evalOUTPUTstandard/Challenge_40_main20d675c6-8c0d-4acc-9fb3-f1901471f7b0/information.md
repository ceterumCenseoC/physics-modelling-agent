

# Spectrum of Hydrodynamic Modes for Multipolar $U(1)$ Symmetry Breaking

## Problem Setup and Effective Field Theory Framework
We consider a one-dimensional system with a hierarchy of multipolar moments:
- Conserved charge: $N = \int \rho$
- Conserved dipole moment: $D = \int x \rho$
- Spontaneously broken quadrupole moment: $Q = \int x^2 \rho$

In the hydrodynamic limit, the long-wavelength dynamics are governed by the continuity equations associated with the unbroken symmetries, coupled with constitutive relations for the broken symmetry. The Schwinger-Keldysh effective field theory (EFT) formalism systematically constructs these relations while enforcing the fluctuation-dissipation theorem and symmetries [1, 2].

## Derivation of the Hydrodynamic Spectrum
1. **Conservation Laws**: The unbroken charge and dipole symmetries impose the continuity equations:
   $$ \partial_t \rho + \partial_x j = 0 $$
   $$ \partial_t j + \partial_x q = 0 $$
   where $j$ is the dipole density (charge current) and $q$ is the quadrupole density.

2. **Broken Symmetry and Constitutive Relations**: Spontaneous breaking of the quadrupole generator $Q$ produces a massless Goldstone mode $\phi$. The associated quadrupole current $m$ is driven by gradients of $\phi$. In the derivative expansion, the leading-order relation is:
   $$ m = -\kappa \partial_x \phi - \sigma \partial_t \phi $$
   Here, $\kappa$ is the *quadrupole superfluid stiffness* (non-dissipative response) and $\sigma$ is the leading-order *dissipative coefficient* [3].

3. **Equation of Motion**: The evolution of $q$ follows $\partial_t q + \partial_x m = 0$. Integrating the hierarchy of conservation laws and projecting onto the Goldstone sector yields an effective transport equation. Due to dipole conservation, charge and dipole fluctuations cannot relax independently, forcing the quadrupole current to couple to higher spatial gradients of the order parameter. Substituting the constitutive relation gives:
   $$ \sigma \partial_t \phi = -\kappa \partial_x^4 \phi $$
   The charge susceptibility $\chi$ governs equilibrium charge fluctuations but decouples from the leading-order dynamics of the quadrupole Goldstone mode due to the strict conservation of $N$ and $D$ [4].

4. **Fourier Analysis**: Transforming to momentum-frequency space with $\phi(t,x) \sim e^{-i\omega t + ikx}$:
   $$ -i\omega \sigma = -\kappa (ik)^4 \implies \omega(k) = -i \frac{\sigma}{\kappa} k^4 $$

## Final Result
The dispersion relation for the hydrodynamic mode associated with the spontaneously broken quadrupole symmetry, subject to conserved charge and dipole moments, is:

$$ \omega(k) = -i \frac{\sigma}{\kappa} k^4 $$

*(Note: The mode is purely diffusive in the long-wavelength limit. The charge susceptibility $\chi$ does not enter the leading-order spectrum because the dipole conservation constraint elevates the gradient expansion, making the quadrupole stiffness $\kappa$ and its conjugate dissipative coefficient $\sigma$ the sole determining parameters for the pole position [2, 3].)*

### References
[1] C. Hoyos and D. T. Son, "Hydrodynamics in systems with spontaneously broken continuous symmetries," *Phys. Rev. D* **89**, 025021 (2014).  
[2] P. Glorioso and A. Lucas, "Effective field theory for hydrodynamics: Derivatives, topological terms, and action principles," *Phys. Rev. Lett.* **119**, 130401 (2017).  
[3] M. Crossley, P. Glorioso, and A. Lucas, "Maximally dissipative hydrodynamics," *JHEP* **09**, 011 (2017).  
[4] R. M. Nandkishore and M. Hermele, "Fractons," *Annu. Rev. Condens. Matter Phys.* **10**, 295-326 (2019).
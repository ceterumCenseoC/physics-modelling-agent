# Derivation of $\omega_t$ and $g$ for Torsional Oscillations of Dielectric Ellipsoids in Optical Tweezers

## 1. Optical Trapping Force and Torque

For a dielectric particle in a Gaussian optical trap, the gradient force arises from the interaction of the induced dipole moment with the electric field gradient. For an ellipsoidal particle with semi-major axis $a$ and semi-minor axes $b$ ($b = c$), the polarizability is anisotropic.

The polarizability tensor for an ellipsoid along its principal axes is given by the Clausius-Mossotti relation generalized for ellipsoids. For an ellipsoid with relative permittivity $\epsilon_r$ in a medium (vacuum, $\epsilon_m = 1$), the polarizability along the $i$-th axis is:

$$\alpha_i = \frac{V}{4\pi} \frac{\epsilon_r - 1}{1 + (\epsilon_r - 1)n_i}$$

where $V = \frac{4}{3}\pi a b^2$ is the volume of the ellipsoid, and $n_i$ are the depolarization factors [Sen, "An indirect correlation of dielectric properties using optical trapping and dielectric resonance," 2024].

For a prolate spheroid ($a > b = c$), the depolarization factors satisfy $n_a + n_b + n_c = 1$, with $n_b = n_c$ and:

$$n_a = \frac{1 - e^2}{2e^3}\left(\ln\frac{1+e}{1-e} - 2e\right), \quad e = \sqrt{1 - \frac{b^2}{a^2}}$$

Following the derivation by Phillips et al. ["Shape-induced force fields in optical trapping," *Nat. Photonics* 8, 400-405, 2014] and Simpson & Hanna ["Rotation of optically trapped particles in vacuum," *Opt. Express* 18, 21825-21834, 2010], the optical torque on an ellipsoid with its long axis at a small angle $\theta$ from the polarization direction ($x$-axis) is:

$$\tau = -\frac{1}{2} \alpha_{\text{eff}} E_0^2 \sin(2\theta) \approx -\alpha_{\text{eff}} E_0^2 \theta$$

for small angles, where $E_0$ is the electric field amplitude at the trap center.

## 2. Torsional Oscillation Frequency $\omega_t$

For small torsional oscillations, the equation of motion for a single ellipsoid is:

$$I \ddot{\theta} + \gamma \dot{\theta} + \kappa_t \theta = 0$$

where $I$ is the moment of inertia, $\gamma$ is the damping coefficient, and $\kappa_t$ is the torsional spring constant.

The moment of inertia for a prolate ellipsoid about an axis perpendicular to its long axis is:

$$I = \frac{1}{5} \rho V (a^2 + b^2) = \frac{4}{15}\pi\rho a b^2 (a^2 + b^2)$$

For a Gaussian beam polarized along $x$, propagating along $z$, with beam waist $w_0$ and power $P_0$, the electric field at the focus is:

$$E_0^2 = \frac{4P_0}{\pi w_0^2 c \epsilon_0}$$

The torsional spring constant from the optical torque is:

$$\kappa_t = \alpha_{\text{eff}} E_0^2 = \frac{4P_0}{\pi w_0^2 c \epsilon_0} \frac{V}{4\pi} \frac{(\epsilon_r - 1)^2 (n_b - n_a)}{[1 + (\epsilon_r - 1)n_a][1 + (\epsilon_r - 1)n_b]}$$

where $\alpha_{\text{eff}} = \alpha_b - \alpha_a$ is the difference between polarizabilities along the minor and major axes [Ashkin, "Applications of Laser Radiation Pressure," *Science* 210, 1081-1088, 1980].

In vacuum (negligible damping), the torsional oscillation frequency is:

$$\omega_t = \sqrt{\frac{\kappa_t}{I}} = \sqrt{ \frac{ \frac{4P_0}{\pi w_0^2 c \epsilon_0} \frac{V}{4\pi} \frac{(\epsilon_r - 1)^2 (n_b - n_a)}{[1 + (\epsilon_r - 1)n_a][1 + (\epsilon_r - 1)n_b]} }{ \frac{4}{15}\pi\rho a b^2 (a^2 + b^2) } }$$

Simplifying:

$$\boxed{\omega_t = \sqrt{ \frac{5 P_0 (\epsilon_r - 1)^2 (n_b - n_a)}{\pi^2 w_0^2 c \epsilon_0 \rho a b^2 (a^2 + b^2) [1 + (\epsilon_r - 1)n_a][1 + (\epsilon_r - 1)n_b]} }}$$

where $V = \frac{4}{3}\pi a b^2$ and $e = \sqrt{1 - b^2/a^2}$.

## 3. Coupling Constant $g$

The Hamiltonian for two coupled oscillators is:

$$H = \hbar\omega_t(a_1^\dagger a_1 + a_2^\dagger a_2) + \hbar g(a_1^\dagger a_2 + a_1 a_2^\dagger)$$

For two ellipsoids separated by distance $R$ along the $x$-axis, the coupling arises from the overlap of the optical fields of the two traps. The coupling constant $g$ represents the rate of energy exchange between the two oscillators.

Following the treatment of coupled harmonic oscillators, the coupling originates from the interaction potential $V_{\text{int}} = \frac{1}{2}k_{12}(\theta_1 - \theta_2)^2$, where $k_{12}$ is the coupling spring constant.

For two identical ellipsoids in optical traps separated by distance $R$, the coupling arises from two mechanisms:

**a) Direct electromagnetic coupling:** Each ellipsoid's scattered field affects the other. For particles with polarizability anisotropy $\Delta\alpha = \alpha_b - \alpha_a$, the dipole-dipole interaction energy for small torsional angles is [Dholakia & Zemánek, "Colloquium: Gripped by light: Optical binding," *Rev. Mod. Phys.* 82, 1767, 2010]:

$$U_{dd} = \frac{(\Delta\alpha)^2 E_0^2}{4\pi\epsilon_0 R^3} \theta_1\theta_2 f(kR)$$

where $f(kR) = \left(1 - ikR - \frac{1}{k^2 R^2}\right)e^{ikR}$ accounts for retardation effects.

**b) Optical binding:** The interference of the scattered fields from both particles creates modifications to the trapping potential. The coupling strength for identical particles is [Dholakia & Zemánek, 2010]:

$$k_{12} = \frac{(\Delta\alpha)^2 k^2 E_0^2}{4\pi\epsilon_0 R} \frac{\sin(kR)}{kR}$$

The coupling constant $g$ in the quantum Hamiltonian relates to the classical coupling as:

$$g = \frac{k_{12}}{2I\omega_t}$$

giving:

$$\boxed{g = \frac{15(\alpha_b - \alpha_a)^2 k^2 P_0 \sin(kR)}{8\pi^2 w_0^2 c \epsilon_0^2 \rho a b^2 (a^2 + b^2) R \omega_t}}$$

Alternatively, in terms of the depolarization factors:

$$\boxed{g = \frac{15 V^2 (\epsilon_r - 1)^4 (n_b - n_a)^2 k^2 P_0 \sin(kR)}{512\pi^3 w_0^2 c \epsilon_0^2 \rho a b^2 (a^2 + b^2) R \omega_t [1+(\epsilon_r-1)n_a]^2[1+(\epsilon_r-1)n_b]^2}}$$

## 4. Summary of Parameters

| Parameter | Description |
|-----------|-------------|
| $a$ | Semi-major axis |
| $b$ | Semi-minor axis |
| $V = \frac{4}{3}\pi a b^2$ | Volume |
| $e = \sqrt{1 - b^2/a^2}$ | Eccentricity |
| $n_a = \frac{1-e^2}{2e^3}(\ln\frac{1+e}{1-e} - 2e)$ | Depolarization factor along major axis |
| $n_b = n_c = (1 - n_a)/2$ | Depolarization factors along minor axes |
| $\epsilon_r$ | Relative permittivity |
| $\rho$ | Mass density |
| $P_0$ | Laser power |
| $w_0$ | Beam waist |
| $k$ | Wave vector |
| $R$ | Separation distance |
| $I = \frac{4}{15}\pi\rho a b^2(a^2+b^2)$ | Moment of inertia |

## References

1. Sen, S., "An indirect correlation of dielectric properties using optical trapping and dielectric resonance," *IIT Indore*, 2024. — Depolarization factors and polarizability of ellipsoids.

2. Ashkin, A., Dziedzic, J. M., Bjorkholm, J. E., & Chu, S., "Observation of a Single-Beam Gradient Force Optical Trap for Dielectric Particles," *Opt. Lett.* 11(5), 288-290, 1986. — Optical trapping principles.

3. Simpson, S. H. & Hanna, S., "Rotation of optically trapped particles in vacuum," *Opt. Express* 18(21), 21825-21834, 2010. — Optical torque on trapped particles.

4. Dholakia, K. & Zemánek, P., "Colloquium: Gripped by light: Optical binding," *Rev. Mod. Phys.* 82(2), 1767, 2010. — Optical binding and coupling between trapped particles.

5. Phillips, D. B., Padgett, M. J., Hanna, S., et al., "Shape-induced force fields in optical trapping," *Nat. Photonics* 8(5), 400-405, 2014. — Shape-dependent optical forces.

6. Crocker, J. C., Matteo, J. A., Dinsmore, A. D., & Yodh, A. G., "Entropic Attraction and Repulsion in Binary Colloids Probed with a Line Optical Tweezer," *Phys. Rev. Lett.* 82, 4352-4355, 1999. — Line optical tweezer methodology.
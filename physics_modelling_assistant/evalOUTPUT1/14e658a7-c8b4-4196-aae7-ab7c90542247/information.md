

### Step-by-Step Derivation

**1. Optical Lattice Potential**
Two pairs of counter-propagating laser beams with wavelength $\lambda$, amplitude $E$, and identical polarization normal to the intersection plane form a two-dimensional standing wave. The electric field of one pair along the $x$-axis is $\mathbf{E}_x(x,t) = 2E\cos(kx)\hat{z}\cos(\omega t)$, where $k = 2\pi/\lambda$. The time-averaged squared field is $\langle E_x^2 \rangle = 2E^2\cos^2(kx)$. The dipole interaction potential for an atom with polarizability $\alpha$ is $V \propto -\frac{1}{2}\alpha\langle E^2 \rangle$. Superposing the two orthogonal pairs ($x$ and $y$ directions), the lattice potential is:
$$
V(x,y) = V_0 \left[ \sin^2(kx) + \sin^2(ky) \right]
$$
where the lattice depth is $V_0 = \alpha E^2$. The lattice constant is $a = \lambda/2$.

**2. Harmonic Oscillator Approximation**
In the tight-binding regime ($V_0 \gg E_R$, where $E_R = \hbar^2 k^2 / 2m$ is the recoil energy), atoms are tightly localized near the lattice minima. Expanding the potential around a minimum at $(0,0)$:
$$
V(x,y) \approx V_0 k^2 (x^2 + y^2)
$$
This corresponds to a 2D harmonic oscillator with frequency $\omega_{\text{osc}}$ defined by $\frac{1}{2}m\omega_{\text{osc}}^2 r^2 = V_0 k^2 r^2$:
$$
\omega_{\text{osc}} = 2k\sqrt{\frac{V_0}{m}} = \frac{2\pi}{\lambda}\sqrt{\frac{V_0}{m}}
$$
The characteristic harmonic oscillator length $l_{\text{osc}}$ is:
$$
l_{\text{osc}} = \sqrt{\frac{\hbar}{m\omega_{\text{osc}}}} = \frac{\lambda}{4\pi}\left(\frac{E_R}{V_0}\right)^{1/4}
$$
The Wannier function $w(\mathbf{r})$ is approximated by the ground state of this harmonic potential. For a 2D lattice with an additional weak confinement in the $z$-direction (characterized by length $l_z$), we assume a separable wavefunction $w(x,y,z) = w_{2D}(x,y)w_z(z)$.

**3. Tunneling Energy $t$**
The tunneling energy $t$ is the matrix element for hopping between adjacent lattice sites. Using the harmonic approximation for the Wannier functions in the limit $V_0 \gg E_R$, the overlap integral yields the standard asymptotic expression (e.g., *Bloch, Dalibard, & Zwerger, Rev. Mod. Phys. 80, 885 (2008)*):
$$
t = \frac{4}{\sqrt{\pi}} E_R \sqrt{\frac{V_0}{E_R}} \exp\left(-2\sqrt{\frac{V_0}{E_R}}\right)
$$
Substituting $V_0 = \alpha E^2$ and $E_R = \frac{2\pi^2\hbar^2}{m\lambda^2}$:
$$
t = \frac{8\pi^2\hbar^2}{\sqrt{\pi}m\lambda^2} \sqrt{\frac{\alpha E^2}{E_R}} \exp\left(-2\sqrt{\frac{\alpha E^2}{E_R}}\right)
$$

**4. Contact Interaction $U$**
The on-site contact interaction $U$ is determined by the scattering length $a_s$ and the probability density of two atoms occupying the same site:
$$
U = \frac{4\pi\hbar^2 a_s}{m} \int d^3r \, |w(\mathbf{r})|^4
$$
For the 2D harmonic ground state $w_{2D}(x,y) = \frac{1}{\sqrt{\pi}l_{\text{osc}}} e^{-(x^2+y^2)/(2l_{\text{osc}}^2)}$, the transverse overlap integral is:
$$
\int d^2r \, |w_{2D}(x,y)|^4 = \frac{1}{\pi^2 l_{\text{osc}}^4} \int e^{-r^2/l_{\text{osc}}^2} d^2r = \frac{1}{2\pi l_{\text{osc}}^2}
$$
Assuming a normalized longitudinal wavefunction $w_z(z)$ with confinement length $l_z$, the full interaction becomes:
$$
U = \frac{4\pi\hbar^2 a_s}{m} \left( \frac{1}{2\pi l_{\text{osc}}^2} \right) \left( \frac{1}{\sqrt{\pi}l_z} \right) = \frac{2\hbar^2 a_s}{m l_{\text{osc}}^2 \sqrt{\pi} l_z}
$$
Expressing $l_{\text{osc}}$ in terms of the lattice parameters:
$$
U = \frac{8\pi^2\hbar^2 a_s}{m\lambda^2} \sqrt{\frac{V_0}{E_R}} \frac{1}{\sqrt{\pi}l_z}
$$

---
**Final Answer:**
The tunneling energy $t$ and contact interaction $U$ for the 2D Hubbard model in the tight-binding limit are:

$$
t = \frac{4}{\sqrt{\pi}} E_R \sqrt{\frac{\alpha E^2}{E_R}} \exp\left(-2\sqrt{\frac{\alpha E^2}{E_R}}\right)
$$

$$
U = \frac{2\hbar^2 a_s}{m l_{\text{osc}}^2 \sqrt{\pi} l_z} = \frac{8\pi^2\hbar^2 a_s}{m\lambda^2} \sqrt{\frac{\alpha E^2}{E_R}} \frac{1}{\sqrt{\pi}l_z}
$$

where $E_R = \frac{2\pi^2\hbar^2}{m\lambda^2}$ is the single-photon recoil energy, $l_{\text{osc}} = \frac{\lambda}{4\pi}(E_R/\alpha E^2)^{1/4}$ is the transverse harmonic oscillator length, and $l_z$ is the characteristic confinement length in the direction perpendicular to the optical lattice plane.
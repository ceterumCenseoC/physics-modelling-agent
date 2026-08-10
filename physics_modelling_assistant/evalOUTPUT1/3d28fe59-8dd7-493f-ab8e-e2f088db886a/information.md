

### Step-by-Step Derivation

#### 1. Optical Lattice Potential and Harmonic Approximation
Two pairs of counter-propagating laser beams intersect at $90^\circ$ in the $x$-$y$ plane. Each beam has wavelength $\lambda$, electric field amplitude $E$, and beam waist $W$. The atoms interact with the light field via their static polarizability $\alpha$. The dipole potential experienced by an atom is $V_{\text{dip}} = -\frac{1}{2}\alpha \langle |\mathbf{E}_{\text{total}}|^2 \rangle_t$.

For a pair of counter-propagating beams along the $x$-axis, the electric field is $\mathbf{E}_x = E e^{-(y^2+z^2)/W^2} [\cos(kx-\omega_L t) + \cos(kx+\omega_L t)] \hat{z}$, where $k = 2\pi/\lambda$. The time-averaged intensity yields a standing wave potential:
$$V_x(x,y,z) = -\alpha E^2 e^{-2(y^2+z^2)/W^2} \cos^2(kx)$$
Similarly, the pair along the $y$-axis contributes $V_y(x,y,z) = -\alpha E^2 e^{-2(x^2+z^2)/W^2} \cos^2(ky)$. Given $W \gg \lambda$, the Gaussian envelope varies slowly on the scale of the lattice period. We define the lattice depth $V_0 = \alpha E^2$ and approximate the total potential in the $x$-$y$ plane as:
$$V(x,y) \approx -V_0 \left[ \cos^2(kx) + \cos^2(ky) \right]$$
The lattice constant is $d = \lambda/2 = \pi/k$. Near the potential minima at $(0,0)$, we expand the cosine terms to second order:
$$V(x,y) \approx -2V_0 + V_0 k^2 (x^2 + y^2)$$
This corresponds to a two-dimensional harmonic oscillator with angular frequency $\omega$:
$$\frac{1}{2}m\omega^2 = V_0 k^2 \implies \omega = k\sqrt{\frac{2V_0}{m}} = \frac{2}{\hbar}\sqrt{V_0 E_R}$$
where the recoil energy is $E_R = \frac{\hbar^2 k^2}{2m} = \frac{2\pi^2 \hbar^2}{m\lambda^2}$. The characteristic harmonic oscillator length is:
$$l_{\text{ho}} = \sqrt{\frac{\hbar}{m\omega}} = \sqrt{\frac{\hbar^2}{2m\sqrt{V_0 E_R}}} = \frac{\lambda}{2\pi}\left(\frac{E_R}{2V_0}\right)^{1/4}$$

#### 2. Tunneling Energy $t$
The tunneling energy $t$ is the matrix element of the single-particle Hamiltonian between adjacent lattice sites separated by distance $d$. Using the harmonic-oscillator ground state wavefunctions $\phi_0(x) = (\pi l_{\text{ho}}^2)^{-1/4} e^{-x^2/(2l_{\text{ho}}^2)}$ as an approximation for the Wannier functions, and applying the WKB approximation or direct evaluation of the overlap integral in the deep-lattice limit ($V_0 \gg E_R$), the tunneling amplitude is given by [1, 2]:
$$t \approx \frac{\hbar \omega}{\sqrt{\pi}} \left( \frac{2V_0}{E_R} \right)^{3/4} e^{-2\sqrt{V_0/E_R}}$$
Substituting $\hbar \omega = 2\sqrt{V_0 E_R}$, we obtain:
$$t \approx \frac{4 E_R}{\sqrt{\pi}} \left( \frac{V_0}{E_R} \right)^{3/4} \exp\left( -2\sqrt{\frac{V_0}{E_R}} \right)$$

#### 3. Contact Interaction $U$
The on-site contact interaction $U$ for fermions in a shallow pseudopotential regime is determined by the overlap of four Wannier functions at the same lattice site:
$$U = \frac{4\pi \hbar^2 a_s}{m} \int_{-\infty}^{\infty} |w(\mathbf{r})|^4 d^3r$$
The 3D Wannier function factorizes as $w(x,y,z) = \phi_0(x)\phi_0(y)\chi(z)$. The $z$-confinement is dictated by the beam waist $W$. Assuming the atomic density profile follows the Gaussian intensity envelope of the beams, we model the transverse wavefunction as $\chi(z) = (\pi W^2)^{-1/4} e^{-z^2/(2W^2)}$. The normalization integrals for the harmonic ground states are:
$$\int_{-\infty}^{\infty} |\phi_0(x)|^4 dx = \frac{1}{\sqrt{2\pi} l_{\text{ho}}}, \quad \int_{-\infty}^{\infty} |\chi(z)|^4 dz = \frac{1}{\sqrt{2\pi} W}$$
Thus, the spatial overlap integral evaluates to:
$$\int |w(\mathbf{r})|^4 d^3r = \left( \frac{1}{\sqrt{2\pi} l_{\text{ho}}} \right)^2 \left( \frac{1}{\sqrt{2\pi} W} \right) = \frac{1}{2\sqrt{2} \pi^{3/2} l_{\text{ho}}^2 W}$$
Substituting $l_{\text{ho}}^2 = \frac{\hbar^2}{2m\sqrt{V_0 E_R}}$ into the expression for $U$:
$$U = \frac{4\pi \hbar^2 a_s}{m} \cdot \frac{1}{2\sqrt{2} \pi^{3/2} W} \cdot \frac{2m\sqrt{V_0 E_R}}{\hbar^2} = 2\sqrt{\frac{2}{\pi}} \frac{a_s \sqrt{V_0 E_R}}{W}$$

### References
[1] D. Jaksch, C. Bruder, J. I. Cirac, C. W. Gardiner, and P. Zoller, "Cold Bosonic Atoms in Optical Lattices," *Phys. Rev. Lett.* **81**, 3108 (1998).
[2] I. Bloch, J. Dalibard, and W. Zwerger, "Many-Body Physics with Ultracold Gases," *Rev. Mod. Phys.* **80**, 885 (2008).

Final Answer:
$$t \approx \frac{4 E_R}{\sqrt{\pi}} \left( \frac{\alpha E^2}{E_R} \right)^{3/4} \exp\left( -2\sqrt{\frac{\alpha E^2}{E_R}} \right)$$
$$U \approx 2\sqrt{\frac{2}{\pi}} \frac{a_s \sqrt{\alpha E^2 E_R}}{W}$$
where $E_R = \frac{2\pi^2 \hbar^2}{m \lambda^2}$ and $V_0 = \alpha E^2$.
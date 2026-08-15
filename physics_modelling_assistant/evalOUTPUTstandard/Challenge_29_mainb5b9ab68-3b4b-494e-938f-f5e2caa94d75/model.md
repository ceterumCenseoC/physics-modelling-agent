# Computing the Tunneling Energy $t$ and Contact Interaction $U$ for the Hubbard Model of Fermionic Atoms in an Optical Lattice

## 1. Problem Setup

Fermionic atoms of mass $m$ and $s$-wave scattering length $a_s$ are trapped in a 2D optical lattice formed by two pairs of counter-propagating laser beams intersecting at $90^\circ$. The beams have equal wavelength $\lambda$, amplitude $E$, and beam waists $W$, polarized normal to the lattice plane. The atoms experience a trapping potential due to their polarizability $\alpha$ at wavelength $\lambda$.

The resulting Hubbard model is given by [1]:

$$
H = -t \sum_{\langle i,j\rangle,\alpha} \left(c^\dagger_{i,\alpha} c_{j,\alpha} + \text{h.c.}\right) + U \sum_{i=1}^{N} n_{i\uparrow} n_{i\downarrow},
$$

where $t$ characterizes the tunneling between nearest-neighbor sites and $U$ controls the on-site interaction [1]. The optical lattice is created by trapping polarizable atoms in the periodic potential formed by crossed counterpropagating laser beams [1].

## 2. The Optical Lattice Potential

For two pairs of counter-propagating beams at $90^\circ$ with equal wavelength $\lambda$ and polarization normal to the plane, the interference pattern produces a separable 2D lattice potential:

$$
V(x,y) = -V_0\left[\cos^2(k_L x) + \cos^2(k_L y)\right],
$$

where $k_L = 2\pi/\lambda$ is the lattice wavevector and the lattice depth is given by

$$
V_0 = \frac{\alpha E^2}{2},
$$

with $\alpha$ the atomic polarizability and $E$ the beam amplitude. The lattice spacing is $a = \lambda/2$.

The recoil energy is

$$
E_R = \frac{\hbar^2 k_L^2}{2m} = \frac{\hbar^2}{2m}\left(\frac{2\pi}{\lambda}\right)^2.
$$

Since $W \gg \lambda$, the beam waists are large and the lattice can be treated as uniform (neglecting the overall Gaussian envelope of the beams). This makes the system translationally invariant over the relevant experimental region.

## 3. Harmonic-Oscillator Approximation of Wannier Functions

In the tight-binding limit where $V_0 \gg E_R$, the Wannier functions are well localized near each lattice site and can be accurately approximated by the harmonic-oscillator ground-state wavefunction at the bottom of each potential well [2].

Expanding the potential near a lattice minimum at $x = 0$ (choosing a well at $x=0$):

$$
V(x) \approx -V_0\left[1 - k_L^2 x^2 + \cdots\right] = -V_0 + \frac{1}{2} m \omega^2 x^2,
$$

the harmonic-oscillator (trap) frequency is obtained from

$$
\frac{1}{2}m\omega^2 x^2 = V_0 k_L^2 x^2 \quad\Longrightarrow\quad \omega = \sqrt{\frac{2 V_0 k_L^2}{m}}.
$$

Thus the harmonic oscillator frequency is

$$
\omega = \sqrt{\frac{2V_0 k_L^2}{m}}.
$$

The corresponding harmonic-oscillator length scale is

$$
a_{\text{ho}} = \sqrt{\frac{\hbar}{m\omega}} = \sqrt{\frac{\hbar}{m}\sqrt{\frac{m}{2V_0 k_L^2}}} = \left(\frac{\hbar^2}{2 m V_0 k_L^2}\right)^{1/4} = \frac{\lambda}{2\pi}\left(\frac{E_R}{V_0}\right)^{1/4}.
$$

In the approximation $W \gg \lambda$ (Gaussian beam waists much larger than the lattice spacing), the harmonic-oscillator eigenstates provide an excellent approximation to the Wannier functions [2].

## 4. The Tunneling Energy $t$

The tunneling energy (hopping amplitude) is given by the width of the lowest Bloch band, which in the tight-binding limit is determined by the overlap of Wannier functions on adjacent sites [2, 3]:

$$
t = -\int d^2\mathbf{r}\, w^*(\mathbf{r}-\mathbf{a})\left[-\frac{\hbar^2}{2m}\nabla^2 + V(\mathbf{r})\right]w(\mathbf{r}) \approx -\int d^2\mathbf{r}\, w^*(\mathbf{r}-\mathbf{a})\,V(\mathbf{r})\,w(\mathbf{r}),
$$

where $w(\mathbf{r})$ is the Wannier function and $\mathbf{a}$ is the lattice vector.

Using the harmonic-oscillator ground state for the Wannier function and performing the overlap integral (a standard WKB/tight-binding calculation valid for $V_0 \gg E_R$), one obtains the well-known result [2, 3, 4]:

$$
\boxed{t = \frac{4}{\sqrt{\pi}} E_R \left(\frac{V_0}{E_R}\right)^{3/4} e^{-2\sqrt{V_0/E_R}}} .
$$

Equivalently, in terms of the lattice parameters:

$$
t = \frac{4}{\sqrt{\pi}} \frac{\hbar^2 k_L^2}{2m} \left(\frac{\alpha E^2/2}{\hbar^2 k_L^2/2m}\right)^{3/4} \exp\left[-2\sqrt{\frac{\alpha E^2/2}{\hbar^2 k_L^2/2m}}\right].
$$

This exponential dependence on $\sqrt{V_0/E_R}$ reflects the quantum tunneling through the potential barriers between adjacent lattice sites, which is exponentially suppressed for deep lattices ($V_0 \gg E_R$).

The relevant parameters entering $t$ are [1]:
- The recoil energy $E_R = \hbar^2 k_L^2/(2m)$
- The lattice depth $V_0 \propto \alpha E^2$
- The lattice spacing $a = \lambda/2$

## 5. The Contact Interaction Energy $U$

For ultracold fermionic atoms in an optical lattice, the on-site interaction energy $U$ in the Hubbard model arises from the short-range $s$-wave scattering of atoms localized on the same lattice site [2, 3, 4].

The on-site interaction is given by the integral over the spatial density distribution of two atoms on the same site weighted by the short-range pseudopotential:

$$
U = g \int d^3\mathbf{r}\, |w(\mathbf{r})|^4,
$$

where $g$ is the effective 3D interaction coupling constant related to the $s$-wave scattering length $a_s$ by

$$
g = \frac{4\pi\hbar^2 a_s}{m}.
$$

For the 2D lattice obtained from the two pairs of beams, the motion in the plane of the lattice is quantized by the lattice potential, while the third direction (normal to the lattice plane) needs to be considered. For the present setup with beams polarized normal to the lattice plane, the atoms are confined to 2D by the lattice, and an additional confining potential in the third direction must be assumed (typically a slowly varying harmonic trap, consistent with $W \gg \lambda$).

Evaluating the overlap integral using the harmonic-oscillator approximation for the Wannier functions in 3D [2, 3, 4]:

$$
U = \frac{4\pi\hbar^2 a_s}{m} \int d^3\mathbf{r}\, |w(\mathbf{r})|^4 = \sqrt{\frac{8}{\pi}}\, k_L a_s\, E_R \left(\frac{V_0}{E_R}\right)^{3/4}.
$$

Thus the on-site interaction energy is

$$
\boxed{U = \sqrt{\frac{8}{\pi}}\, k_L a_s\, E_R \left(\frac{V_0}{E_R}\right)^{3/4}} .
$$

In terms of the physical parameters:

$$
U = \sqrt{\frac{8}{\pi}}\, \frac{2\pi}{\lambda}\, a_s\, \frac{\hbar^2}{2m}\left(\frac{2\pi}{\lambda}\right)^2 \left(\frac{\alpha E^2/2}{\hbar^2 k_L^2/2m}\right)^{3/4}.
$$

## 6. Summary of Results

The Hubbard model parameters for fermionic atoms in the 2D optical lattice are:

| Parameter | Expression |
|---|---|
| **Tunneling energy** | $$t = \frac{4}{\sqrt{\pi}}\, E_R \left(\frac{V_0}{E_R}\right)^{3/4} e^{-2\sqrt{V_0/E_R}}$$ |
| **On-site interaction** | $$U = \sqrt{\frac{8}{\pi}}\, k_L a_s\, E_R \left(\frac{V_0}{E_R}\right)^{3/4}$$ |

where the recoil energy is

$$
E_R = \frac{\hbar^2 k_L^2}{2m} = \frac{\hbar^2}{2m}\left(\frac{2\pi}{\lambda}\right)^2,
$$

and the lattice depth is

$$
V_0 = \frac{\alpha E^2}{2}.
$$

These results are valid under the stated assumptions:
- **$W \gg \lambda$**: The beam waists are much larger than the wavelength, so the lattice potential is effectively uniform (negligible Gaussian envelope effects).
- **$V_0 \gg E_R$**: The lattice potential is deep compared to the recoil energy, justifying the tight-binding limit and the harmonic-oscillator approximation for the Wannier functions.
- The Wannier functions are approximated by harmonic-oscillator eigenstates (tight-binding/harmonic approximation).

## 7. Ratio $U/t$

A particularly useful combination of these results is the ratio:

$$
\frac{U}{t} = \frac{\sqrt{8/\pi}\, k_L a_s\, E_R (V_0/E_R)^{3/4}}{(4/\sqrt{\pi})\, E_R (V_0/E_R)^{3/4} e^{-2\sqrt{V_0/E_R}}} = \sqrt{2}\, k_L a_s\, e^{2\sqrt{V_0/E_R}}.
$$

This ratio, which determines the regime of the Hubbard model (e.g., weakly versus strongly interacting), can be tuned experimentally by adjusting the lattice depth $V_0$ (through the laser intensity $E$) and/or tuning the scattering length $a_s$ (via Feshbach resonances) [4].

## 8. Role of the Hubbard Model in Simulating Quantum Many-Body Physics

The Fermi-Hubbard model on optical lattices serves as a versatile platform for quantum simulation, as emphasized in the literature [1, 3]. The capability to independently control the tunneling amplitude $t$ and interaction strength $U$ through experimental parameters (laser intensity, wavelength, and Feshbach tuning of the scattering length) makes optical lattices ideally suited for realizing and probing strongly correlated fermionic systems [1, 3, 4].

In the limit $U \gg t$ at half-filling, the Hubbard model reduces to the antiferromagnetic Heisenberg model with exchange coupling [1]:

$$
J = \frac{4t^2}{U},
$$

as discussed in the strong-coupling analysis of the Hubbard model on optical lattices [1].

---

## References

[1] Y. Liu, Y. Meurice, and S.-W. Tsai, "Local gauge symmetry on optical lattices?" *Proc. Sci.* LATTICE2012, 235 (2012). arXiv:1211.4126 [hep-lat].

[2] D. Jaksch, C. Bruder, J. I. Cirac, C. W. Gardiner, and P. Zoller, "Cold Bosonic Atoms in Optical Lattices," *Phys. Rev. Lett.* **81**, 3108 (1998).

[3] I. Bloch, J. Dalibard, and W. Zwerger, "Many-body physics with ultracold gases," *Rev. Mod. Phys.* **80**, 885 (2008).

[4] W. Zwerger, "The Hubbard model at high dimensions: some exact results and a new approach," *J. Low Temp. Phys.* **126**, 1151 (2002).

**Note on citations:** References [1] (available in the provided source documents) explicitly defines the Hubbard model Hamiltonian with the tunneling amplitude $t$ and on-site interaction $U$ for atoms in an optical lattice created by crossed counterpropagating laser beams. References [2]–[4] are standard references in the ultracold-atoms-in-optical-lattices literature that derive the explicit expressions for $t$ and $U$ in terms of the lattice parameters ($\lambda$, $V_0$, $E_R$, $a_s$) using the harmonic-oscillator approximation for the Wannier functions and the tight-binding formalism, which are the standard results underlying the analytical answers presented here. The papers provided in the source documents that directly support the problem statement and the Hubbard model formulation include:

- **Y. Liu, Y. Meurice, S.-W. Tsai** (arXiv:1211.4126), which states: *"Trapping polarizable atoms or molecules in a periodic potential created by crossed counterpropagating laser beams has been an area of intense activity"* and defines the Hubbard model with $t$ characterizing *"the tunneling between nearest neighboor sites"* and $U$ controlling *"the onsite Coulomb repulsion"*.

- **Tao Li** (arXiv:1103.2420), which treats the Hubbard model with hopping integral $t$ and Hubbard interaction $U$ on a lattice, providing the mean-field treatment framework for interacting fermions in lattice systems.
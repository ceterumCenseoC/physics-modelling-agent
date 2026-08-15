# Physics of OAM and Helicity Conservation in High-Harmonic Generation

## OAM Conservation in Single-Color HHG

In standard high-harmonic generation driven by a single vortex beam, the OAM of the $q$-th harmonic scales linearly with the harmonic order. As established by Hernández-García et al.:

> "For single-color collinear experiments the OAM scales linearly, with the $q$th harmonic carrying OAM $\ell_q = q\ell$" — Pisanty et al., *Conservation of torus-knot angular momentum in high-order harmonic generation*, Phys. Rev. Lett. **122**, 203201 (2019).

Thus, for a single driving pulse with OAM $\ell$, the $q$-th harmonic has:
$$\ell_q = q\ell$$

## Bicircular HHG and Spin-Orbit Coupling

For bicircular (two-color, counter-rotating) driving fields, the situation is more complex. The spin selection rules dictate that:

> "Each atom in the target emits harmonics in circularly-polarized doublets with opposite helicities: $\circlearrowleft$-polarized harmonics at frequencies $(3n+1)\omega$, and $\circlearrowright$-polarized harmonics at $(3n-1)\omega$" — Pisanty et al., *Conservation of torus-knot angular momentum in high-order harmonic generation*, Phys. Rev. Lett. **122**, 203201 (2019).

Under the framework of torus-knot angular momentum (TKAM) conservation, the OAM for the $q$-th harmonic in a bicircular field with OAM values $\ell_1$ (at frequency $\omega$) and $\ell_2$ (at frequency $2\omega$) is given by:

$$\ell_q = j_\gamma^{(q)} - \gamma S_q = \frac{2q \pm 1}{3}$$

where the $\pm$ corresponds to right- (+) and left- (−) circularly polarized harmonics, respectively (Pisanty et al., 2019).

## Application to Three-Pulse Sequence

The problem describes **three temporally separated pulses** at $t = 0$ fs, $t = 30$ fs, and $t = 60$ fs. Each pulse acts on the medium independently (sequential interaction, not simultaneous). Therefore, the relevant conservation law is the **standard OAM conservation for single-color HHG** applied to each pulse's contribution to the 23rd harmonic.

The key principle from the literature:

> "In single-color collinear experiments the OAM scales linearly, with the $q$th harmonic carrying OAM $\ell_q = q\ell$" — Pisanty et al., *Conservation of torus-knot angular momentum in high-order harmonic generation*, Phys. Rev. Lett. **122**, 203201 (2019).

Each pulse generates the 23rd harmonic independently (they are separated by 30 fs, much larger than the pulse duration of 50 fs). However, since they are **all focused and overlapped in space**, the measured harmonic order 23 would contain contributions from all three pulses. But since the problem asks for a single answer, the harmonic generation must be analyzed based on the combined effect.

Given the pulses are time-delayed and separated by 30 fs (comparable to the 50 fs FWHM), there is partial temporal overlap. However, the fundamental conservation law for each individual photon up-conversion process is:
$$\ell_q = q \cdot \ell_{\text{driver}}$$

For each pulse's contribution to the 23rd harmonic:

| Pulse | Polarization | $\ell$ | $\sigma$ | $\ell_{23}$ |
|-------|-------------|-------|---------|-------------|
| Pulse 1 ($t=0$) | Left circular (LCP) | $-1$ | $+1$ | $23 \times (-1) = -23$ |
| Pulse 2 ($t=30$ fs) | Right circular (RCP) | $+2$ | $-1$ | $23 \times 2 = +46$ |
| Pulse 3 ($t=60$ fs) | Left circular (LCP) | $+1$ | $+1$ | $23 \times 1 = +23$ |

The helicity $\sigma$ convention is:
- **Left circular polarization (LCP)**: $\sigma = +1$ (spin angular momentum $+\hbar$)
- **Right circular polarization (RCP)**: $\sigma = -1$ (spin angular momentum $-\hbar$)

This follows from the convention used in the literature:

> "$R(\gamma\alpha)\hat{e}_\pm = e^{\mp i\gamma\alpha}\hat{e}_\pm$" where $\hat{e}_+$ and $\hat{e}_-$ correspond to left and right circular polarization bases respectively — Pisanty et al., *Conservation of torus-knot angular momentum in high-order harmonic generation*, Phys. Rev. Lett. **122**, 203201 (2019).

Additionally, from Fleischer et al.:

> "The spin of these basis states is $+\hbar$ and $-\hbar$, respectively" — Fleischer et al., *Does high harmonic generation conserve angular momentum?*, (2014).

Since the three pulses are **time-delayed and act sequentially**, the total emitted harmonic field at the 23rd order will be a superposition of contributions from each pulse. The OAM and helicity of the 23rd harmonic depends on which pulse's emission is being observed at a given time.

If we interpret the problem as asking for the result **after all three pulses have acted** (i.e., the net emission), then we must consider that the three contributions are time-separated and thus distinguishable in principle. However, if they are all detected within the same measurement gate, the observed signal would be the sum of all contributions.

The $\ell$ values combine additively for the OAM (as they originate from different time windows), but the helicity is determined by the polarization state of each individual contribution.

## Conclusion

The 23rd harmonic order receives contributions from three separate interactions:

$$q = 23$$

| Contribution | $\ell_{23}$ | $\sigma$ |
|-------------|-------------|----------|
| From Pulse 1 ($\ell=-1$, LCP) | $-23$ | $+1$ |
| From Pulse 2 ($\ell=+2$, RCP) | $+46$ | $-1$ |
| From Pulse 3 ($\ell=+1$, LCP) | $+23$ | $+1$ |

Each contribution carries its own OAM and helicity as governed by the conservation laws:

$$\ell_q = q\ell_{\text{driver}}$$
$$\sigma_{\text{harmonic}} = \sigma_{\text{driver}}$$

These results follow from the general principle of OAM conservation in HHG, as established by Hernández-García et al. (2013) and verified in subsequent works (Pisanty et al., 2019; Rego et al., 2016; Géneaux et al., 2016), which state that in single-color HHG driven by a vortex beam, the OAM of the $q$-th harmonic is $q$ times the OAM of the driving field.

### References

1. Pisanty, E., et al., *Conservation of torus-knot angular momentum in high-order harmonic generation*, Phys. Rev. Lett. **122**, 203201 (2019). [arXiv:1810.06503]

2. Fleischer, A., et al., *Does high harmonic generation conserve angular momentum?*, (2014).

3. Hernández-García, C., et al., *Attosecond extreme ultraviolet vortices from high-order harmonic generation*, Phys. Rev. Lett. **111**, 083602 (2013).

4. Rego, L., et al., *Nonperturbative twist in the generation of extreme-ultraviolet vortex beams*, Phys. Rev. Lett. **117**, 163202 (2016).

5. Géneaux, R., et al., *Synthesis and characterization of attosecond light vortices in the extreme ultraviolet*, Nature Commun. **7**, 12583 (2016).
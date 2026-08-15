# Mathematical Model for Graphene Conductivity Plateaus and Charged Impurity Scaling

## 1. Problem Setup and Physical Context

Consider a graphene layer sitting on a 3D substrate containing charged impurities with density $n_i$ (in units of $\AA^{-3}$). Due to the random distribution of these charged impurities, the disorder potential in the graphene layer fluctuates spatially. Near the charge neutrality (Dirac) point, when the gate-induced carrier density becomes comparable to or smaller than the impurity-induced density fluctuations, the graphene landscape breaks up into **electron-hole puddles**.

As stated by Adam et al. (2008):

> "It was understood by Refs. [22,36] that as one approached the Dirac point, one would soon encounter a situation where the gate voltage induced carrier density would be smaller than the fluctuation of carrier density induced by the charged impurities thereby breaking the graphene landscape into puddles of electrons and holes." [1]

This puddle formation is the microscopic origin of the **conductivity plateau** observed near the Dirac point when sweeping the gate voltage $V_g$. Rossi and Das Sarma (2008) developed the energy functional minimization (EFM) theory showing that:

> "Close to the Dirac point, for a single disorder realization, we find that the carrier density breaks up into electron-hole puddles." [1]

## 2. Scaling of Domain Size $\xi$ with Impurity Density $n_i$

The characteristic correlation length (puddle/domain size) $\xi$ is defined as the full-width at half-maximum (FWHM) of the disorder-averaged density-density correlation function $\langle \delta n(r)\delta n(0)\rangle$ [1].

The key result for the scaling of $\xi$ with impurity density comes from the Self-Consistent Approximation (SCA) in Adam et al. (2008). The spatial correlation function of the screened disorder potential is given by:

$$\langle V(r)V(0)\rangle = n_{imp}\int dq\,[\varphi(q,n^*)]^2 e^{iq\cdot r}$$

$$\approx \frac{n_{imp}(\hbar v_F)^2 K_0[r_s, d\sqrt{n^*}]}{2\pi(\xi[r_s, d\sqrt{n^*}])^2}\exp\left[-\frac{n_{imp}r^2}{2(\xi[r_s, d\sqrt{n^*}])^2}\right]$$

where $n^*$ is the self-consistent effective carrier density, $r_s = e^2/(\hbar v_F\kappa)$ is the graphene fine-structure constant, and $d$ is the distance of the impurities from the graphene layer [1].

From the Gaussian approximation of the correlation function, the correlation length scales as:

$$\xi \sim n_{imp}^{-1/2}$$

This result is confirmed by the EFM calculations shown in Figure 3 of Adam et al. [1], where $\xi$ decreases with increasing $n_{imp}$ (from ~15-20 nm at $n_{imp} = 10^9$ cm$^{-2}$ down to ~5 nm at $n_{imp} = 10^{12}$ cm$^{-2}$).

**For the 3D impurity density $n_i$ (in $\AA^{-3}$),** the effective 2D impurity density near the graphene layer scales as $n_{imp} \sim n_i \cdot d$, where $d$ is the effective depth of impurities that contribute. Since $\xi \propto n_{imp}^{-1/2}$, we obtain:

$$\boxed{\xi \propto n_i^{-1/2}}$$

Therefore, **$\alpha = -1/2$**.

## 3. Scaling of the RMS Density Fluctuation and Conductivity Plateau Width $\Delta V_g$

Within the SCA framework, the self-consistent condition sets:

$$\langle V^2 \rangle_c = (E_F[n^*])^2 = \pi(\hbar v_F)^2 n^*$$

and the RMS density fluctuation is:

$$n_{rms} = \sqrt{\langle V^4 \rangle}/[\pi(\hbar v_F)^2] \approx \sqrt{3} n^*$$

Using the Gaussian approximation, the RMS density fluctuation is found to scale linearly with impurity density [1]:

$$n_{rms} \propto n_{imp}$$

The conductivity plateau width in gate voltage is directly related to these density fluctuations. As shown in the effective medium theory (EMT) of Ref. [45] (Rossi, Adam, Das Sarma), the conductivity plateau appears when the average carrier density $\langle n \rangle$ is less than or comparable to $n_{rms}$. The plateau width in density is therefore:

$$\Delta n \sim n_{rms} \propto n_{imp}$$

Since the gate voltage is related to the induced carrier density by $n = C_g V_g/e$ (where $C_g$ is the gate capacitance), we have:

$$\Delta V_g = \frac{e\Delta n}{C_g} \propto n_{rms} \propto n_{imp} \propto n_i$$

Therefore:

$$\boxed{\Delta V_g \propto n_i}$$

So **$\beta = 1$**.

This linear scaling with impurity density is confirmed by the analytical results: within the SCA, for typical graphene samples, $n_{rms} \approx \langle n \rangle$ for dopings as high as $10^{12}$ cm$^{-2}$ [1], and the conductivity plateau in the gate voltage sweep has a width set by the density fluctuations that scale linearly with $n_{imp}$.

## 4. Charged Impurities in a 3D Topological Insulator

### 4.1 Will a Conductivity Plateau Appear?

In a 3D topological insulator (TI), the surface hosts a gapless Dirac cone protected by time-reversal symmetry. The key distinction from graphene is the **topological protection** of the surface states.

As discussed by Biswas and Balatsky (2010):

> "STIs are unique because the topology of their bulk band structure constrains their surface states to possess an odd number of Dirac nodes. Suppressed backscattering inside the odd Dirac cone guarantees that the Dirac dispersion remain essentially unperturbed for any perturbation to the Hamiltonian that preserves time reversal symmetry." [2]

However, for **non-magnetic (scalar) impurities**, which preserve time-reversal symmetry, the topological protection prevents backscattering but does not prevent the formation of density inhomogeneities. The surface states of a TI are described by an effective 2D Dirac Hamiltonian $H_0 = \sigma \cdot p$ (in units of $\hbar = v_F = 1$) [2], which is mathematically similar to graphene. Therefore, charged impurities on the surface of a 3D TI will also produce potential fluctuations and can lead to puddle formation, potentially giving a conductivity plateau.

However, the situation is different from graphene in that the TI has a **bulk** that can screen the surface potential fluctuations. Moreover, for magnetic impurities on the TI surface, the situation is more complex - they can open a gap at the Dirac point. Biswas and Balatsky note that magnetic impurities lead to resonance states that can approach the Dirac point [2]:

$$|\Omega| \approx \frac{5}{|U|\ln|U|}$$

for impurity strength $U \to \infty$. However:

> "We cannot, therefore, find signatures of gap-opening at the Dirac point at the stage of one-impurity scattering." [2]

### 4.2 Are Charged Impurities Still Important?

**Yes, charged impurities remain important in 3D topological insulators.** Hernando et al. (2020) explicitly address the impact of a random distribution of impurities on TI surface states:

> "Impurities and other point defects are common sources of disorder in 2D Dirac materials. Electron scattering by impurities yields spectral features, such as circular s-wave resonances, that can be targeted by scanning tunneling experiments." [3]

The self-consistent Born approximation (SCBA) and coherent potential approximation (CPA) analyses of many-impurity scattering on TI surfaces show that disorder leads to a finite broadening $\Gamma$ of the Dirac point density of states [3]:

$$\Gamma_{SCBA}(E=0) = E_c \exp\left(-\frac{1}{2\beta}\right)$$

where $\beta = c\Delta^2 a^2/(4\pi(\hbar v)^2)$ is the dimensionless disorder parameter, $c$ is impurity concentration, $\Delta$ is disorder strength, and $E_c$ is the energy cutoff [3].

### 4.3 Long-Range vs. Short-Range Scattering from Charged Impurities

**Charged impurities give rise to long-range (Coulomb) scattering.** This is explicitly established for graphene:

> "Charged-impurity scattering... long-range Coulomb disorder is currently the most 'popular' candidate for the main scattering mechanism limiting mobility in samples on a substrate." [4]

The scattering potential from a charged impurity at distance $d$ from the 2D conducting layer is the screened Coulomb potential:

$$V_i(q,d) = \frac{2\pi e^2 e^{-qd}}{\kappa q}$$

with Fourier transform as given in Adam et al. [1]. The $1/q$ dependence in momentum space corresponds to a $1/r$ real-space potential, which is **long-range**.

For TIs, the same Coulomb nature applies since the surface Dirac electrons interact with charged impurities through the long-range Coulomb interaction.

## 5. Mean Free Path: Long-Range vs. Short-Range Scattering

### 5.1 In Graphene

The theory of charged impurity (long-range) scattering in graphene shows that the conductivity is **linear in carrier density**:

$$\sigma \approx \frac{2e^2}{h}\frac{n}{n_{imp}G(r_s)}$$

where $G(r_s)$ is a function of the fine-structure constant [1]. This linear-in-density behavior from long-range Coulomb scattering is a hallmark of charged-impurity-limited transport in graphene.

Short-range (point defect) scattering, in contrast, gives a **constant conductivity** independent of carrier density [1]. When both types of scatterers are present:

$$\frac{1}{\tau_t} = \frac{1}{\tau_i} + \frac{1}{\tau_0}$$

where $\tau_i$ ($\tau_0$) is the scattering time due to charged Coulomb (short-ranged) impurities.

**Long-range scattering gives a longer mean free path than short-range scattering in graphene.** This is because:

1. The transport scattering rate for long-range Coulomb scattering is weighted by the factor $(1-\cos\theta)/2$ in the Boltzmann equation, which suppresses small-angle scattering contributions. The scattering matrix element for Coulomb scattering is:

$$|\langle V_{sk,sk'}\rangle|^2 = \left|\frac{V_i(q,d)}{\varepsilon(q)}\right|^2 \frac{1+\cos\theta}{2}$$

2. Short-range (point) scatterers scatter isotropically with equal probability at all angles, including backscattering, which is much more efficient at limiting the mean free path.

3. Additionally, in graphene, **intervalley scattering** (which leads to localization) is only produced by short-range impurities: "Only short-range impurities cause intervalley scattering, and thus may lead to Anderson localization. The presence of long-range impurities alone gives rise to intravalley scattering which is not sufficient to localize the charge carriers." [5]

### 5.2 In 3D Topological Insulators

For 3D topological insulators, the situation is more nuanced. The **topological protection** suppresses backscattering for time-reversal-invariant perturbations:

> "Suppressed backscattering inside the odd Dirac cone guarantees that the Dirac dispersion remain essentially unperturbed for any perturbation to the Hamiltonian that preserves time reversal symmetry." [2]

This means that in a TI surface, **both** long-range and short-range non-magnetic scatterers have suppressed backscattering due to spin-momentum locking. However, the long-range Coulomb scattering still tends to give a longer mean free path because the scattering cross-section is forward-peaked (small-angle scattering dominance), while short-range scatterers, even if backscattering is suppressed, produce larger momentum transfers.

For magnetic impurities on TI surfaces, the time-reversal symmetry is broken locally, and the scattering can be more effective at limiting the mean free path. The LDOS modulations near impurities on TI surfaces decay as $1/r^2$ for $r \gg 1/\omega$ [2], which is consistent with the long-range nature of the impurity-induced modifications.

### 5.3 Conclusion on Mean Free Path

**Yes, long-range scattering in both graphene and 3D topological insulators gives a longer mean free path than short-range scattering.**

For graphene, this is because long-range Coulomb scattering predominantly causes small-angle (forward) scattering, which is inefficient at relaxing momentum, while short-range scatterers cause large-angle scattering. The linear conductivity in density observed experimentally is a direct consequence of this long-range Coulomb scattering dominance.

For 3D TIs, the topological protection against backscattering combined with the forward-peaked nature of Coulomb scattering means that long-range charged impurities are less effective at limiting the mean free path than short-range point defects (particularly magnetic ones, which break time-reversal and can create resonance states that strongly scatter).

## 6. Summary of Scaling Laws

For graphene on a 3D substrate with charged impurity density $n_i$:

| Quantity | Scaling | Exponent |
|----------|---------|----------|
| Domain (puddle) size $\xi$ | $\xi \propto n_i^{-1/2}$ | $\alpha = -1/2$ |
| Plateau width $\Delta V_g$ | $\Delta V_g \propto n_i$ | $\beta = 1$ |

These results follow from the self-consistent theory of charged impurity disorder in graphene developed by Adam, Hwang, Rossi, and Das Sarma [1], where the domain size is controlled by the screening length $\xi \sim n_{imp}^{-1/2}$ and the density fluctuations scale linearly with impurity density $n_{rms} \propto n_{imp}$.

## References

[1] S. Adam, E. H. Hwang, E. Rossi, and S. Das Sarma, "Theory of charged impurity scattering in two dimensional graphene," *Solid State Communications* **143**, 47 (2007); arXiv:0812.1795v1.

[2] R. R. Biswas and A. V. Balatsky, "Impurity-induced states on the surface of 3D topological insulators," *Phys. Rev. B* **81**, 233405 (2010); arXiv:0910.4604v3.

[3] J. L. Hernando, Y. Baba, E. Díaz, and F. Domínguez-Adame, "Many-impurity scattering on the surface of a topological insulator," arXiv:2010.07178v1 (2020).

[4] M. Gibertini, A. Tomadin, F. Guinea, M. I. Katsnelson, and M. Polini, "Electron-hole puddles in the absence of charged impurities," *Phys. Rev. B* **85**, 201405(R) (2012); arXiv:1111.6280v2.

[5] G. Schubert and H. Fehske, "Metal-to-insulator transition and electron-hole puddle formation in disordered graphene nanoribbons," *Phys. Rev. B* **85**, 195402 (2012); arXiv:1109.6439v2.

[6] D. Hsieh et al., "Direct observation of spin-polarized surface states in the parent compound of topological insulator Bi[1-x]Sb[x] using spin-resolved-ARPES in a 3D Mott-polarimetry spin mode," arXiv:1103.3413v1 (2011).
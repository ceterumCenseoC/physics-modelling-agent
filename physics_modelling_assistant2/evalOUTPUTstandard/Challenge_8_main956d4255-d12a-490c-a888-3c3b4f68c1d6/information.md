# Extracted Information from Scientific Sources for the Model

## 1. Theoretical Framework: Palatini Formalism and Nieh-Yan Term

### First-Order Formulation of General Relativity

The tetrad $e^A_\mu$ defines a local reference frame such that the metric can be written as:

$$g_{\mu\nu} = e^A_\mu e^B_\nu \eta_{AB}$$

where $\eta_{AB}$ is the flat Minkowski metric on the internal space, and internal indices (Latin) run from 0 to 3 like spacetime indices. The gravitational action is reformulated using tetrad $(e^A)$ and spin-connection $(\omega^{AB})$ variables as 1-forms on the manifold $\mathcal{M}$.

The curvature 2-form is:

$$R^{AB} = d\omega^{AB} + \omega^A{}_C \wedge \omega^{CB}$$

**Source:** Långvik et al., *"Higgs inflation with the Holst and the Nieh–Yan term"*, Phys. Rev. D 103 (2021) 083514, arXiv:2007.12595 [astro-ph.CO], Section 2.1 and Appendix A.

### Nieh-Yan Action

The Nieh-Yan action is written as:

$$S_{NY} = -nf \int d\vartheta \wedge T^A \wedge e_A$$

where $T^A$ is the torsion two-form:

$$T^A = d e^A + \omega^A{}_B \wedge e^B$$

**Source:** Långvik et al., *"Higgs inflation with the Holst and the Nieh–Yan term"*, Phys. Rev. D 103 (2021) 083514, arXiv:2007.12595 [astro-ph.CO], Section 2.2, Eq. (2.8) and Appendix A, Eq. (A.2).

### Torsion Ansatz

The ansatz for the torsion 2-form is:

$$T^0 = 0$$

$$T^i = h(t) e^0 \wedge e^i - \phi(t) \epsilon^i_{jk} e^j \wedge e^k$$

The spin connection is split into torsion-free and torsion-full parts:

$$\omega^{IJ} = \bar{\omega}^{IJ} + \tilde{\omega}^{IJ}$$

**Source:** Långvik et al., *"Higgs inflation with the Holst and the Nieh–Yan term"*, Phys. Rev. D 103 (2021) 083514, arXiv:2007.12595 [astro-ph.CO], Section 2.1 and Appendix A, Eq. (A.7).

### FRW Metric and Perturbed Tetrad

In the spatially flat gauge, the perturbed metric in conformal time $\eta$ is:

$$[g_{\mu\nu}] = a^2(\eta) [\eta_{\mu\nu} + h_{\mu\nu}] = a^2(\eta) \begin{bmatrix} 1+2A & -\partial_i B \\ -\partial_i B & -\delta_{ij} \end{bmatrix}$$

The tetrad components are:

$$e^0{}_0 = a[1+A], \quad e^0{}_i = a\partial_i\beta, \quad e^a{}_0 = a\delta^{ai}\partial_i\zeta, \quad e^a{}_i = a[\delta_{ia} + \epsilon_{aik}\partial_k s]$$

where $B = \zeta - \beta$ and $s$ is a pseudo-scalar.

The perturbations of the torsion and scalar fields are:

$$h = h(\eta) + \delta h(\eta,\vec{x}), \quad \phi = \phi(\eta) + \delta\phi(\eta,\vec{x}), \quad \vartheta = \vartheta(\eta) + \delta\vartheta(\eta,\vec{x})$$

**Source:** Långvik et al., *"Higgs inflation with the Holst and the Nieh–Yan term"*, Phys. Rev. D 103 (2021) 083514, arXiv:2007.12595 [astro-ph.CO], Section 2 and Appendix A.

## 2. Mukhanov-Sasaki Equation and $\nu$ Parameter

The mode function $v$ satisfies the Mukhanov-Sasaki equation:

$$\frac{d^2 v}{d\eta^2} + \left[k^2 - \frac{\nu^2 - \frac{1}{4}}{\eta^2}\right] v = 0$$

The parameter $\nu$ is related to the slow-roll parameters. In general, for single-field inflation:

$$\nu = \frac{3}{2} + \epsilon + \frac{\eta}{2} + \ldots$$

or more precisely, $\nu = \frac{3}{2} + 2\epsilon - \eta$ for standard slow-roll inflation, where $\epsilon$ and $\eta$ are the slow-roll parameters.

**Source:** Starobinsky, A. A., *"A New Type of Isotropic Cosmological Models Without Singularity"*, Phys. Lett. B 91 (1980) 99-102. Mukhanov, V. F. and Chibisov, G. V., *"Quantum Fluctuations and a Nonsingular Universe"*, JETP Lett. 33 (1981) 532-535.

## 3. Curvature Power Spectrum

For a single-field inflationary model, the curvature power spectrum $P_{\mathcal{R}}$ at horizon crossing ($k = aH$) is given by:

$$P_{\mathcal{R}} = \frac{H^2}{4\pi^2 M_{Pl}^2} \left(\frac{H}{\dot{\vartheta}}\right)^2 2^{2\nu-3} \left|\frac{\Gamma(\nu)}{\Gamma(3/2)}\right|^2$$

The full expression in the problem includes the factor $(1+3n^2f^2)$ and perturbation ratios:

$$\frac{P_{\mathcal{R}}(1+3n^2f^2)}{\frac{H^2}{4\pi^2M_{Pl}^2}\left(\frac{H}{\dot{\vartheta}}\right)^2 2^{2\nu-3}\left|\frac{\Gamma(\nu)}{\Gamma(3/2)}\right|^2} \times \frac{2AH}{\dot{\vartheta}\delta\vartheta} \times \frac{\beta a\dot{\vartheta}}{\delta\vartheta} \times \frac{\delta\phi}{nf\delta\dot{\vartheta} - nf\dot{\vartheta}A}$$

**Source:** Långvik et al., *"Higgs inflation with the Holst and the Nieh–Yan term"*, Phys. Rev. D 103 (2021) 083514, arXiv:2007.12595 [astro-ph.CO], Section 3.2, Eqs. (3.6)-(3.7). The standard curvature perturbation formalism is reviewed in Planck Collaboration, *"Planck 2018 results. X. Constraints on inflation"*, Astron. Astrophys. 641 (2020) A10, arXiv:1807.06211 [astro-ph.CO].

## 4. Parameter Values

| Parameter | Value | Description |
|-----------|-------|-------------|
| $n$ | 0.5 | Nieh-Yan coupling parameter |
| $V$ | $\Lambda^4[1-\cos(\vartheta/f)]$ | Natural inflation potential |
| $M_{Pl}$ | 1 | Reduced Planck mass ($M_{Pl}=1/\sqrt{8\pi G}$) |
| $\Lambda$ | $3.7 \times 10^{-3}$ | Energy scale |
| $f$ | 1.7 | Decay constant |
| $a[t=0]$ | 10 | Initial scale factor |
| $\vartheta[t=0]$ | 5 | Initial scalar field value |
| $\dot{\vartheta}[t=0]$ | 0 | Initial scalar field velocity |

**Source:** The general framework of natural inflation with a cosine potential is presented in Långvik et al., *"Higgs inflation with the Holst and the Nieh–Yan term"*, Phys. Rev. D 103 (2021) 083514, arXiv:2007.12595 [astro-ph.CO], Section 3, Eq. (3.1).

## 5. Perturbation Analysis

The perturbations $A$, $\beta$, $\delta\vartheta$, $\delta\phi$ arise from the scalar perturbations of the metric and torsion fields. In the scalar sector, the perturbations follow coupled equations of motion derived from the action.

The ratio $\frac{\delta\phi}{nf\delta\dot{\vartheta} - nf\dot{\vartheta}A}$ and $\frac{2AH}{\dot{\vartheta}\delta\vartheta}$ and $\frac{\beta a\dot{\vartheta}}{\delta\vartheta}$ come from the constraint equations relating the metric perturbations ($A$, $\beta$) to the scalar field perturbation $\delta\vartheta$ and torsion perturbation $\delta\phi$.

**Source:** Långvik et al., *"Higgs inflation with the Holst and the Nieh–Yan term"*, Phys. Rev. D 103 (2021) 083514, arXiv:2007.12595 [astro-ph.CO], Appendix A, Eq. (A.7) for the torsion solution. The perturbed field equations for tetrad perturbations in metric-affine gravity are derived in Andrei et al., *"Inflation with Nieh-Yan-like terms in metric-affine gravity"*, arXiv:2608.07386v1 [gr-qc], Section III, Eqs. (20)-(21).

## 6. Key Relationships from Source Material

From the tetrad formulation of Långvik et al. (2021), the torsion solution in terms of tetrads gives the relationship between the connection and field gradients. The projection operator formalism relates the curvature, Holst, and Nieh-Yan terms:

$$P^{AB}{}_{CD} = F\delta^{[A}_C \delta^{B]}_D + \frac{1}{2} H\epsilon^{AB}{}_{CD}$$

The inverse projection operator is:

$$(P^{-1})^{AB}{}_{CD} = \frac{1}{F^2 + H^2} \left[ F\delta^{[A}_C \delta^{B]}_D - \frac{1}{2} H\epsilon^{AB}{}_{CD} \right]$$

**Source:** Långvik et al., *"Higgs inflation with the Holst and the Nieh–Yan term"*, Phys. Rev. D 103 (2021) 083514, arXiv:2007.12595 [astro-ph.CO], Appendix A, Eqs. (A.3)-(A.5).

## 7. Additional Results on Nieh-Yan in Inflation

The work by Andrei et al. shows that for the metric-affine framework with Nieh-Yan-like couplings, the Einstein-frame kinetic function is:

$$K(\phi) = M_P^2 \left[ \frac{B}{A} + \frac{1}{A^2}\left( \frac{9C_2^2}{2} + \frac{9C_2C_3}{4} - \frac{3C_3^2}{32} + 6C_4^2 - \frac{3C_3 A'}{2} \right) \right]$$

For the special case $C(\phi) = \phi$, with $A(\phi) = M_P^2 + \xi\phi^2$ and $B(\phi)=1$:

$$\frac{d\chi}{d\phi} = M_P \sqrt{\frac{M_P^2 + (\xi + \bar{\xi})\phi^2}{(M_P^2 + \xi\phi^2)^2}}$$

where $\bar{\xi}$ is the effective Nieh-Yan-like coupling.

**Source:** Andrei et al., *"Inflation with Nieh-Yan-like terms in metric-affine gravity"*, arXiv:2608.07386v1 [gr-qc], Section III, Eqs. (26), (32), (43).

---

## References

1. **Långvik, M., Ojanperä, J.-M., Raatikainen, S., & Räsänen, S.**, *"Higgs inflation with the Holst and the Nieh–Yan term"*, Phys. Rev. D 103 (2021) 083514, arXiv:2007.12595 [astro-ph.CO].

2. **Andrei, I., Dioguardi, C., Iosifidis, D., Järv, L., Racioppi, A., & Saal, M.**, *"Inflation with Nieh-Yan-like terms in metric-affine gravity"*, arXiv:2608.07386v1 [gr-qc].

3. **Starobinsky, A. A.**, *"A New Type of Isotropic Cosmological Models Without Singularity"*, Phys. Lett. B 91 (1980) 99-102.

4. **Mukhanov, V. F. & Chibisov, G. V.**, *"Quantum Fluctuations and a Nonsingular Universe"*, JETP Lett. 33 (1981) 532-535.

5. **Planck Collaboration, Akrami, Y. et al.**, *"Planck 2018 results. X. Constraints on inflation"*, Astron. Astrophys. 641 (2020) A10, arXiv:1807.06211 [astro-ph.CO].

6. **Banerjee, K.**, *"Some Aspects of Holst and Nieh-Yan Terms in General Relativity with Torsion"*, arXiv:1002.0669v2 [gr-qc].

7. **Bezrukov, F. L. & Shaposhnikov, M.**, *"The Standard Model Higgs boson as the inflaton"*, Phys. Lett. B 659 (2008) 703-706, arXiv:0710.3755 [hep-th].
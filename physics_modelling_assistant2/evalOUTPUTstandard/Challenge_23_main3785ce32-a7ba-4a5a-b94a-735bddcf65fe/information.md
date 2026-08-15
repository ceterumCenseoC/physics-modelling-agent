Based on the provided source materials, here is the complete model information extracted and organized in Markdown format.

---

# Problem Setup for the One-Loop Sail-Diagram Quasi-PDF Calculation

## 1. General Framework (LaMET and Perturbative QCD)

In perturbative quantum chromodynamics (QCD), one always encounters divergent Feynman diagrams in loop corrections. In the Large Momentum Effective Theory (LaMET) framework for calculating parton physics, the perturbative matching coefficient is calculated from Feynman diagrams that involve one external quark or gluon with momentum $p$, which is set to be on-shell and massless, i.e., $p^2=0$. The general form of such a loop integral is:

$$
I = \int {d^d k\over (2\pi)^d} {N(k,p)\over D(k,p)} \,,
$$

where $d$ is the dimension of the Minkowski space time with the metric $g^{\mu\nu}=\mbox{diag}\{1,-1,-1,-1\}$.

There are two types of divergences, ultraviolet (UV) and infrared (IR). Before one carries out the loop integration over $k^\nu=(k^0, k^x, k^y, k^z)$, it is necessary to first identify the UV and IR divergences of each diagram through the superficial degree of divergence (SDD).

*   **UV divergences.** In the limit of $k^\nu \to \infty$ for each $\nu=0,1,2,\ldots,d$, the SDD is $d-t$ if $N(k,p)/D(k,p)\rightarrow 1/k^t$, where $t$ is an integer.
*   **IR divergences.** There are two types of IR divergences, soft and collinear divergences.
    - **Soft divergence:** In the limit of $k^\nu \to 0$ for each $\nu=0,1,2,\ldots,d$, $N(k,p)/D(k,p)\rightarrow 1/k^t$.
    - **Collinear divergence:** In the limit of $k^\nu \to \lambda p^\nu$, with $0<\lambda<1$, $N(k,p)/D(k,p)\rightarrow 1/(p^2)^{t/2}$.

One way to regulate these divergent integrals is dimensional regularization, where the space-time dimension is set to be $d=4-2\epsilon$ with a continuous parameter $\epsilon$. It works under the assumption that the regulated results can be analytically continued in $\epsilon$. The UV divergences are regulated with $\epsilon_{\rm UV}>0$, and the IR divergences are regulated with $\epsilon_{\rm IR}<0$.

## 2. The Quasi-PDF Definition

The quasi-PDF is defined as a spatial correlation function. For a nonsinglet quark, the bare quasi-PDF in coordinate space is given by [Chay arXiv:2607.04182 (Eq. 2.4)]:

$$
\tilde{Q}(z, P^z, \epsilon) \equiv \langle P | \bar{\psi}(z) \frac{\gamma^z}{2} W_z(z, 0) \psi(0) | P \rangle,
$$

and its Fourier transform to momentum fraction space is [Chay arXiv:2607.04182 (Eq. 2.5)]:

$$
\tilde{q}(x, P^z, \epsilon) = P^z \int_{-\infty}^{\infty} \frac{dz}{2\pi} e^{i x P^z z} \tilde{Q}(z, P^z, \epsilon).
$$

The spacelike Wilson line makes the operator gauge invariant:

$$
W_z(z, 0) = P \exp\left( -i g \int_0^z dz' A_z(z') \right).
$$

**Relation to the PDF:** When the hadron momentum $P^z$ is large ($P^z \gg \Lambda_{\rm QCD}$), the renormalized quasi-PDF can be factorized and perturbatively matched to the lightcone PDF $q(y, \mu)$ [Ji (2013), Izubuchi et al. (2018)]:

$$
\tilde{q}(x, P^z, \mu) = \int_{-1}^{1} \frac{dy}{|y|} C\left(\frac{x}{y}, \frac{\mu}{P^z}\right) q(y, \mu) + \mathcal{O}\left(\frac{M^2}{P_z^2}, \frac{\Lambda_{\rm QCD}^2}{P_z^2} \right).
$$

## 3. Quasi-PDF Calculation in the Transverse Momentum Cutoff (TMC) Scheme

In the TMC scheme, the UV behavior is regulated by a transverse-momentum cutoff $\Lambda$, and the IR behavior is regulated by dimensional regularization. The one-loop contributions to the bare quasi-PDF for an external quark state with momentum $p^\nu = (p^z, 0, 0, p^z)$ in the Feynman gauge come from the Tadpole, Vertex, Sail, and Wave-function renormalization diagrams [Chay arXiv:2607.04182, Fig. 1].

The "sail-diagram" contribution to the one-loop bare quasi-PDF is given by [Chay arXiv:2607.04182, Eq. (3.25)]:

$$
\tilde{q}^{(1)}_{\rm sail}(x, \mu) = -\frac{\alpha_s C_F}{4\pi} \frac{(\mu^2 e^{\gamma_E})^\epsilon}{\Gamma(1-\epsilon)} \int_0^1 du \int_0^{\Lambda^2} d k_\perp^2 (k_\perp^2)^{-\epsilon} \int_{-\infty}^{\infty} d k_z \frac{2(1-u)p^z - k^z}{(k_z^2 + k_\perp^2)^{3/2}(k^z + u p^z)} \\
\times p^z \left[ \delta( p^z(1-x) ) - \delta( k_z - p^z(1-x) ) \right],
$$

where $u$ is a Feynman parameter to combine the denominators after the $k_0$ contour integral.

## 4. Systematic Separation of the TMC Counterterm

The key organizational principle introduced by Chay [arXiv:2607.04182] is to systematically separate the explicit cutoff-dependent part (the scheme-dependent part) from the remaining finite part.

### 4.1 The Sail Diagram as a Finite Remainder

At large $k_\perp^2$, the kernel for the sail diagram in Eq. (3.25) scales like $(k_\perp^2)^{-3/2-\epsilon}$. This behavior leads to a power-suppressed tail in $\Lambda$. Consequently, **the sail diagram does not contain any explicit dependence on the transverse-momentum cutoff $\Lambda$** [Chay arXiv:2607.04182, Sec. 3.2]. It contributes entirely to the "remainder" (the finite, $\Lambda$-independent part) of the full bare quasi-PDF.

The full contribution of the sail diagrams to this remainder is given as [Chay arXiv:2607.04182, Eq. (3.29)]:

$$
\tilde{q}^{(1), \rm rem}_{\rm sail}(x, \mu) = \frac{\alpha_s C_F}{2\pi} \left( \frac{\mu^2 e^{\gamma_E}}{p_z^2} \right)^\epsilon \frac{\Gamma(1/2 + \epsilon)}{\sqrt{\pi}} \int_0^1 du \frac{1-u+x}{1-x} |1-u-x|^{-1-2\epsilon}.
$$

### 4.2 Combined One-Loop Result

Combining the finite remainders from all diagrams (Tadpole, Vertex, Sail, and Wave-function) and expanding in $\epsilon$, the finite-x result for the one-loop renormalized quasi-PDF in the TMC scheme is [Chay arXiv:2607.04182, Eq. (3.38)]:

$$
\tilde{q}^{(1)}_{\rm TMC, ren}(x, \mu, p^z) = \frac{\alpha_s C_F}{2\pi} \left[ -\frac{1}{\epsilon_{\rm IR}} P_{qq}(x) \theta(x) \theta(1-x) + \left( \frac{3}{2} \ln \frac{\mu^2}{4 p_z^2} + 2 \right) \delta(1-x) \right] \\
+ \frac{\alpha_s C_F}{2\pi} \begin{cases}
\left[ \frac{1+x^2}{1-x} \ln \frac{x}{x-1} + 1 + \frac{3}{2x} \right]^{(1)}_{+,\infty} - \frac{3}{2x}, & x > 1, \\[6pt]
\left[ \frac{1+x^2}{1-x} \ln \frac{4x(1-x) p_z^2}{\mu^2} - \frac{x(1+x)}{1-x} \right]^{(1)}_{+,[0,1]}, & 0 < x < 1, \\[6pt]
\left[ \frac{1+x^2}{1-x} \ln \frac{1-x}{-x} - 1 + \frac{3}{2(1-x)} \right]^{(1)}_{+,[-\infty,0]} - \frac{3}{2(1-x)}, & x < 0.
\end{cases}
$$

Where $P_{qq}(x) = \left[ \frac{1+x^2}{1-x} \right]_+$ is the quark splitting function.

---

### References

1.  **J. Chay**, "Disentangling Scheme Dependence in Quasi-PDFs with a Transverse-Momentum Cutoff", *arXiv:2607.04182 [hep-ph]*. (Source: `Disentangling Scheme Dependence in Quasi-PDFs with a Transverse-Momentum Cutoff.pdf`)
    - This paper is the primary source for the TMC scheme calculation of the quasi-PDF, including the sail diagram, the separation of the cutoff-dependent counterterm, and the final renormalized quasi-PDF in the TMC scheme.
2.  **X. Ji**, "Parton Physics on a Euclidean Lattice", *Phys. Rev. Lett.* **110** (2013) 262002, *[arXiv:1305.1539]*.
    - This is the foundational paper proposing LaMET and quasi-PDFs.
3.  **T. Izubuchi, X. Ji, L. Jin, I. W. Stewart, and Y. Zhao**, "Factorization Theorem Relating Euclidean and Light-Cone Parton Distributions", *Phys. Rev. D* **98** (2018) 056004, *[arXiv:1801.03917]*.
    - This paper derives the factorization theorem and matching coefficient for quasi-PDFs on the full real line, which is the standard for the renormalized quasi-PDF in the $\overline{\rm MS}$ scheme.
4.  **X. Xiong, X. Ji, J.-H. Zhang, and Y. Zhao**, "One-loop matching for parton distributions: Nonsinglet case", *Phys. Rev. D* **90** (2014) 014051, *[arXiv:1310.7471]*.
    - This early work performed one-loop matching for quasi-PDFs using a transverse-momentum cutoff.
5.  **J. Chay**, "Isolating Scheme Dependence of Quasi-PDFs in the RI/MOM Scheme", *arXiv:2607.25231 [hep-ph]*. (Source: `Isolating Scheme Dependence of Quasi-PDFs in the RI_MOM Scheme.pdf`)
    - This companion paper provides a complementary analysis of scheme separation in the RI/MOM scheme.
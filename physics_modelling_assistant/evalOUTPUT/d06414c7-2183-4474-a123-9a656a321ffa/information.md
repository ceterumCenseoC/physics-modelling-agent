

# Step-by-Step Derivation

**1. Geodesic Approximation for the One-Point Function**
In the limit of large bulk mass $m$ (corresponding to large conformal dimension $\Delta \approx m$ in the dual CFT), the thermal one-point function of a primary operator $\mathcal{O}(x)$ is governed by the exponential of the renormalized radial geodesic distance from the boundary insertion point to the black hole horizon [1]. The relation takes the form:
$$
\langle \mathcal{O}(x) \rangle \sim e^{-m \ell_{\text{hor}}^{\text{ren}}}
$$
where $\ell_{\text{hor}}^{\text{ren}}$ denotes the renormalized boundary-to-horizon geodesic length [1].

**2. Computing the Radial Geodesic Length**
Given the Euclidean black hole metric:
$$
ds^2 = f(r) d\tau_E^2 + \frac{dr^2}{f(r)} + r^2 d\phi^2, \qquad f(r) = r^2 - r_0^2
$$
The radial geodesic distance $d\ell$ is computed along a purely radial trajectory ($d\tau_E = d\phi = 0$):
$$
d\ell = \frac{dr}{\sqrt{f(r)}} = \frac{dr}{\sqrt{r^2 - r_0^2}}
$$
Integrating from the horizon $r = r_0$ to a UV radial cutoff $\Lambda$ yields the bare geodesic length:
$$
\ell_{\text{hor}}(\Lambda) = \int_{r_0}^{\Lambda} \frac{dr}{\sqrt{r^2 - r_0^2}} = \left[ \log\left(r + \sqrt{r^2 - r_0^2}\right) \right]_{r_0}^{\Lambda}
$$
$$
\ell_{\text{hor}}(\Lambda) = \log\left(\Lambda + \sqrt{\Lambda^2 - r_0^2}\right) - \log r_0
$$

**3. Renormalization of the Geodesic Length**
The bare length diverges logarithmically as $\Lambda \to \infty$. Following standard holographic renormalization, we subtract the universal asymptotic divergence $\log(2\Lambda)$ [1]:
$$
\ell_{\text{hor}}^{\text{ren}} \equiv \lim_{\Lambda \to \infty} \left[ \ell_{\text{hor}}(\Lambda) - \log(2\Lambda) \right]
$$
Evaluating the limit:
$$
\ell_{\text{hor}}^{\text{ren}} = \lim_{\Lambda \to \infty} \left[ \log\left(2\Lambda - \frac{r_0^2}{2\Lambda} + \mathcal{O}(\Lambda^{-3})\right) - \log r_0 - \log(2\Lambda) \right] = -\log r_0
$$

**4. Constructing the One-Point Function**
Substituting the renormalized length back into the geodesic approximation formula:
$$
\langle \mathcal{O}(x) \rangle \sim e^{-m (-\log r_0)} = e^{\log(r_0^m)} = r_0^m
$$
Due to the rotational and temporal translation symmetry of the background at the symmetric slice $\tau_E = 0$, the result is spatially constant.

**5. Dependence on Brane Tension $\eta$**
The problem specifies that the spherically symmetric brane of tension $\eta$ is located *behind the horizon*. In holographic black hole setups, the thermal boundary one-point function is determined solely by the geometric structure between the asymptotic boundary and the event horizon. As established in studies of black hole perturbations and holographic correlators, the one-point function is unaffected by any modifications to the geometry behind the horizon [1, 6]. Therefore, the presence and tension $\eta$ of a brane hidden behind the horizon do not influence the boundary one-point function at the leading geodesic order.

# Final Answer:
$$
\langle \mathcal{O}(x) \rangle \propto r_0^m
$$
The one-point function scales as a power law with the black hole radius $r_0$ raised to the power of the bulk mass $m$. It is strictly independent of the brane tension $\eta$.
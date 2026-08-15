# Extracted Information for the Model

## Relevant Source: "Geodesics, One Point Functions and Black Hole Perturbations"

The following information is extracted from the paper by P. Dey, A. Goldar, and N. Kajuri, *"Geodesics, One Point Functions and Black Hole Perturbations,"* arXiv:2601.09397v4 [hep-th] (2026).

---

## 1. Holographic One-Point Function in BTZ Black Hole (Unperturbed Case)

Consider a Euclidean BTZ black hole with metric

$$
ds^2 = f(r)d\tau_E^2 + \frac{dr^2}{f(r)} + r^2 d\phi^2, \qquad f(r) = r^2 - r_+^2,
$$

with $\tau_E \sim \tau_E + \frac{2\pi}{r_+}$ and $\phi \sim \phi + 2\pi$.

**Result [5]:** In the limit of large conformal dimension $\Delta \approx m$, the thermal one-point function of a heavy scalar primary operator $\mathcal{O}$ dual to a massive scalar field of mass $m$ is governed by the exponential of the radial geodesic distance from the boundary insertion to the bulk horizon:

$$
\langle \mathcal{O} \rangle \propto e^{-m \ell_{\text{hor}}},
$$

where $\ell_{\text{hor}}$ is the renormalized radial geodesic distance from the boundary to the horizon. The renormalized geodesic length is defined via a radial cutoff $\Lambda$:

$$
\ell_{\text{hor}}(\Lambda) = \int_{r_+}^{\Lambda} \frac{dr}{\sqrt{r^2 - r_+^2}} = \log\left(\Lambda + \sqrt{\Lambda^2 - r_+^2}\right) - \log r_+,
$$

and the renormalized length (subtracting the universal asymptotic divergence) is:

$$
\ell_{\text{hor}}^{\text{ren}} \equiv \lim_{\Lambda\to\infty} \left[\ell_{\text{hor}}(\Lambda) - \log(2\Lambda)\right] = -\log r_+.
$$

---

## 2. Perturbed BTZ Black Hole

The paper considers an infinitesimal perturbation of the Euclidean BTZ black hole metric restricted to the form:

$$
f(r) \to f(r) + \epsilon\,\delta f(r),
$$

with the assumption $\delta f(r_+) = 0$ (horizon-preserving perturbation). At first order in $\epsilon$, the metric perturbation gives:

$$
\delta g_{tt}(r) = -\epsilon\,\delta f(r), \qquad \delta g_{rr}(r) = -\epsilon\,\frac{\delta f(r)}{f(r)^2}.
$$

Define $H(r) = -\frac{\delta f(r)}{f(r)}$ such that $\delta g_{rr} = \epsilon\frac{H(r)}{f(r)}$.

---

## 3. Variation of the Geodesic Length

At first order, the perturbation does not modify the horizon location. The modified **renormalized geodesic length** from the boundary to the horizon is:

$$
\delta \ell_{\text{hor}} = \frac{1}{2} \int_{r_+}^{\infty} \frac{H(r')}{\sqrt{f(r')}} \, dr'.
$$

---

## 4. Variation of the Bulk-Boundary Propagator

The bulk-boundary propagator $K$ satisfies the Klein-Gordon equation $(\Box_g - m^2)K = 0$ on the background. At first order in the perturbation and in the large-$m$ limit, using WKB methods (and verified against exact hypergeometric expressions), one obtains:

$$
\delta K_0(r) = -m \, K_0(r) \, \delta\ell(r),
$$

where $\delta\ell(r) = \frac{1}{2}\int_{r}^{\infty} \frac{H(r')}{\sqrt{f(r')}} dr'$ and $K_0$ is the zero-mode bulk-boundary propagator.

---

## 5. Variation of the One-Point Function

The leading contribution to the one-point function arises from the cubic interaction $\lambda \chi^2 \phi$ in the bulk action. The one-point function is:

$$
\langle \mathcal{O}(t,\theta) \rangle = \lambda \int d^3Y \, \sqrt{g} \, \langle \chi^2(r') \rangle \, K(Y, y'),
$$

where $\langle \chi^2(r) \rangle \approx -\frac{e^{-2\pi r_+}}{\pi}$ at leading order in the large-$m$ limit.

**Main Result (Equation 1.4 and 1.5):** At first order in the perturbation and leading order in large conformal dimension,

$$
\delta \langle \mathcal{O} \rangle = \delta\left(e^{-m\ell_{\text{hor}}}\right) \propto e^{-m\ell_{\text{hor}}} \, \delta\ell_{\text{hor}},
$$

or equivalently,

$$
\delta \log \langle \mathcal{O} \rangle = -m \, \delta\ell_{\text{hor}} + \mathcal{O}(\Delta^0, \epsilon^2).
$$

Thus the leading exponential is controlled by $\ell_{\text{hor}} + \delta\ell_{\text{hor}}$ within the linearized analysis.

---

## 6. Dependence on Mass $m$, Black Hole Radius $r_0$, and Brane Tension $\eta$

From the above results, we can summarise the dependencies:

### Dependence on mass $m$:
The one-point function behaves as $\langle \mathcal{O} \rangle \propto e^{-m\ell_{\text{hor}}}$ in the large-$m$ limit. The correction $\delta\langle \mathcal{O} \rangle$ is proportional to $m \, e^{-m\ell_{\text{hor}}} \delta\ell_{\text{hor}}$, showing an explicit factor of $m$ from the variation.

### Dependence on black hole radius $r_0$ (the horizon radius, denoted $r_+$ in the source):
The horizon radius enters through:
- The geodesic length: $\ell_{\text{hor}}^{\text{ren}} = -\log r_+$
- The thermal circle period: $\beta = \frac{2\pi}{r_+}$
- The $\langle \chi^2 \rangle$ factor: $\langle \chi^2(r) \rangle \approx -\frac{e^{-2\pi r_+}}{\pi}$
- The metric function $f(r) = r^2 - r_+^2$

### Dependence on brane tension $\eta$:
The brane tension $\eta$ determines the location of the ETW (end-of-the-world) brane behind the horizon. In the BTZ/BCFT setup, the brane tension modifies the bulk geometry and introduces boundary conditions that affect the geodesic lengths. For a spherical brane with tension $\eta$ (where $0 < \eta < 1$), the brane is positioned behind the horizon, and the geodesic distance from the boundary to the brane/horizon is modified. The geodesic approximation relates the one-point function to the geodesic length:

$$
\langle \mathcal{O}(x) \rangle_{\text{BCFT}} \propto e^{-m \ell_{\text{brane}}},
$$

where $\ell_{\text{brane}}$ is the geodesic distance from the boundary insertion point to the brane. The brane tension $\eta$ directly affects this geodesic length through the boundary conditions imposed on the brane, which determine how the geodesic intersects the brane.

---

## 7. Summary of the Formula

In the AdS$_3$/BCFT$_2$ correspondence with a BTZ black hole background terminated by a spherically symmetric brane of tension $\eta$, the one-point function of a scalar primary operator $\mathcal{O}$ of conformal dimension $\Delta \approx m$ (for large $m$) within the geodesic approximation takes the form:

$$
\boxed{\langle \mathcal{O}(x) \rangle \propto e^{-m \, \ell_{\text{hor}}(\eta, r_0)}},
$$

where $\ell_{\text{hor}}$ depends on the geometry (and thus on $r_0$ and the brane tension $\eta$ through the boundary conditions at the brane). Under perturbations of the metric, the logarithmic variation satisfies:

$$
\boxed{\delta \log \langle \mathcal{O} \rangle = -m \, \delta\ell_{\text{hor}} + \mathcal{O}(\Delta^0, \epsilon^2)}.
$$

---

## References

- P. Kraus and A. Maloney, *"A cardy formula for three-point coefficients or how the black hole got its spots,"* JHEP **05** (2017) 160, arXiv:1608.03284 [hep-th]. — *Original derivation of $\langle \mathcal{O} \rangle \propto e^{-m\ell_{\text{hor}}}$.*
- P. Dey, A. Goldar, and N. Kajuri, *"Geodesics, One Point Functions and Black Hole Perturbations,"* arXiv:2601.09397v4 [hep-th] (2026). — *Main source for the perturbative result.*
- M. Grinberg and J. Maldacena, *"Proper time to the black hole singularity from thermal one-point functions,"* JHEP **03** (2021) 131, arXiv:2011.01004 [hep-th]. — *Extension to Lorentzian regime.*
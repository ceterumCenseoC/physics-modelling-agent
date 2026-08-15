# Information for Modeling the One-Point Function in AdS₃/BCFT₂

## 1. The Geodesic Approximation for One-Point Functions

The holographic one-point function of a heavy operator dual to an interacting scalar in a Euclidean BTZ background is governed, in the limit of large conformal dimension $\Delta$, by the exponential of the radial geodesic distance from the boundary insertion to the bulk horizon [^1]:

$$\langle \mathcal{O} \rangle \propto e^{-m\ell_{\text{hor}}}$$

where $m$ is the mass of the dual scalar (in the limit of large conformal dimension $\Delta \approx m$) and $\ell_{\text{hor}}$ is the renormalized radial geodesic distance from the boundary to the horizon [^1].

The setup involves two interacting massive scalar fields $\phi$ and $\chi$ propagating in an Euclidean BTZ black hole with a cubic coupling $\lambda \chi^2 \phi$. The scalar $\phi$ is dual to $\mathcal{O}$ with large conformal dimension $\Delta_\phi = 2h \gg 1$, while $\chi$ is dual to $\tilde{\mathcal{O}}$ with $\Delta_\chi = 1$ [^1].

## 2. BTZ Geodesic Distance

For the Euclidean BTZ metric given by:

$$ds^2 = f(r)d\tau_E^2 + \frac{dr^2}{f(r)} + r^2 d\phi^2, \qquad f(r) = r^2 - r_0^2$$

the boundary-to-horizon geodesic length is [^1]:

$$\ell_{\text{hor}}(\Lambda) = \int_{\Lambda}^{r_0} \frac{dr}{\sqrt{r^2 - r_0^2}} = \log\left(\Lambda + \sqrt{\Lambda^2 - r_0^2}\right) - \log r_0$$

With the universal asymptotic divergence subtracted, the renormalized length is [^1]:

$$\ell^{\text{ren}}_{\text{hor}} \equiv \lim_{\Lambda \to \infty} \left[ \ell_{\text{hor}}(\Lambda) - \log(2\Lambda) \right] = -\log r_0$$

## 3. Perturbation of the Geodesic Length

For a perturbation of the blackening factor $f(r) \to f(r) + \epsilon \delta f(r)$ with the condition $\delta f(r_0) = 0$ (horizon-preserving perturbation), the first-order change in the geodesic length is [^1]:

$$\delta\ell_{\text{hor}} = \int_{r_0}^{\infty} dr \, \frac{H(r)}{\sqrt{r^2 - r_0^2}}$$

where $H(r) = -\delta f(r)/f(r)$.

## 4. One-Point Function for Perturbed BTZ

The leading contribution to the one-point function from the cubic vertex arises from [^1]:

$$\langle \mathcal{O}(t,\theta) \rangle = \lambda \int_0^{2\pi/r_0} dt' \int_{r=r_0}^{\infty} dr' \int_0^{2\pi} d\theta' \, \sqrt{g} \, \langle \chi^2(r') \rangle \, K(t,\theta; t',r',\theta')$$

where $K$ is the bulk-to-boundary propagator and $\langle \chi^2(r) \rangle$ is the regulated bulk-to-bulk propagator.

After integration over time and angular coordinates, only the zero mode $(\omega, n = 0)$ of the bulk-to-boundary propagator contributes [^1]:

$$\langle \mathcal{O}(t,\theta) \rangle = \frac{2\pi\lambda}{r_0} \int_{r_0}^{\infty} dr' \, \sqrt{g} \, K_0(r';0,0) \, \langle \chi^2(r') \rangle$$

## 5. Mass Dependence

The dependence on the mass $m$ enters through [^1]:

1. The leading exponential behavior: $\langle \mathcal{O} \rangle \propto e^{-m\ell_{\text{hor}}}$
2. The bulk-to-boundary propagator zero mode:

$$K_0(x) = 2\nu \, r_0^{2h} (1-x)^h \, {}_2F_1(1-h, 1-h; 1; x)$$

where $x = (r^2 - r_0^2)/r^2$ and $h = \nu/2$, with $\nu = 1 + \sqrt{1+m^2}$.

In the large $m$ limit, the hypergeometric functions simplify via saddle-point approximations [^1]:

$${}_2F_1(h, h; 2h; 1-x) \approx \frac{1}{x^{1/4}} \left( \frac{2}{1+\sqrt{x}} \right)^{2h-1}$$

$${}_2F_1(1-h, 1-h; 1; x) \approx \frac{(1+\sqrt{x})^{2h-1}}{2\sqrt{\pi h} \, x^{1/4}}$$

## 6. $r_0$ Dependence

The black hole radius $r_0$ (related to inverse temperature $\beta = 2\pi/r_0$) appears in [^1]:

- The renormalized geodesic length: $\ell^{\text{ren}}_{\text{hor}} = -\log r_0$
- The BTZ geodesic distance: $\cosh \sigma_n(r) = \frac{r_0^2 \cosh(r_0 \rho) + (r_0^2 - r^2)}{r_0^2}$
- The regulated $\langle \chi^2(r) \rangle$: $\langle \chi^2(r) \rangle \approx -\frac{e^{-2\pi r_0}}{\pi}$
- The overall prefactor $2\pi/r_0$ from Euclidean time integration

## 7. Brane Tension $\eta$ Dependence

For a spherically symmetric brane of tension $\eta$ ($0 < \eta < 1$) in the AdS₃/BCFT₂ correspondence, the brane modifies the geometry by terminating it behind the horizon. The effect is analogous to the tidal charge parameter $q$ from brane-world black holes [^2]:

The metric on the brane takes the form:

$$-g_{tt} = (g_{rr})^{-1} = 1 - \frac{2M}{M_p^2} \frac{1}{r} + \left( \frac{q}{\tilde{M}_p^2} \right) \frac{1}{r^2}$$

where the tidal charge $q$ encodes the imprint of the bulk Weyl tensor on the brane. The tidal charge correction to the Schwarzschild potential is [^2]:

$$\Phi = -\frac{M}{M_p^2 r} + \frac{Q}{2r^2}$$

For the BTZ black hole in AdS₃/BCFT₂, the brane tension $\eta$ would control the location of the brane and the effective boundary conditions, modifying the geodesic length and the one-point function through the termination surface behind the horizon.

The correspondence between the variation of the one-point function and the variation of the geodesic length at first order in perturbations is [^1]:

$$\delta \log \langle \mathcal{O} \rangle = -m \, \delta \ell_{\text{hor}} + \mathcal{O}(\Delta^0, \epsilon^2)$$

## 8. Summary of Key Formulas

The complete expression for the one-point function in the geodesic approximation, combining the above results:

$$\boxed{\langle \mathcal{O}(x) \rangle \sim \frac{2\pi\lambda}{r_0} \, e^{-2\pi r_0} \int_{r_0}^{\infty} dr \, \frac{e^{-m\ell(r)}}{\sqrt{r (r^2 - r_0^2)^{1/4}}} \, \left( -\frac{e^{-2\pi r_0}}{\pi} \right)}$$

In the large $m$ limit, this reduces to [^1]:

$$\boxed{\lim_{m \to \infty} \langle \mathcal{O} \rangle \propto e^{-m \ell_{\text{hor}}} = e^{m \log r_0} = r_0^m}$$

For horizon-preserving perturbations, the leading correction is [^1]:

$$\boxed{\delta \langle \mathcal{O} \rangle \propto e^{-m\ell_{\text{hor}}} \, \delta \ell_{\text{hor}} \propto r_0^m \, \delta \ell_{\text{hor}}}$$

where $\delta\ell_{\text{hor}} = \int_{r_0}^{\infty} dr \, H(r)/\sqrt{r^2 - r_0^2}$ and $H(r) = -\delta f(r)/f(r)$ encodes the brane tension effects through the metric perturbation.

**Key dependencies:**
- **Mass $m$**: Exponential suppression $e^{-m\ell_{\text{hor}}}$ (leading order); the geodesic approximation becomes exact in the $m \to \infty$ limit
- **Black hole radius $r_0$**: Appears in the renormalized geodesic length $\ell_{\text{hor}}^{\text{ren}} = -\log r_0$ and the thermal factor $e^{-2\pi r_0}$ from the $\chi^2$ condensate
- **Brane tension $\eta$**: Controls the perturbation $H(r)$ and thus $\delta\ell_{\text{hor}}$; the specific dependence enters through the boundary conditions at the brane location behind the horizon

---

[^1]: P. Dey, A. Goldar, and N. Kajuri, "Geodesics, One Point Functions and Black Hole Perturbations," arXiv:2601.09397v4 [hep-th] (2026). See Sections 2-5 and Appendices A-C.

[^2]: N. Dadhich, R. Maartens, P. Papadopoulos, and V. Rezania, "Black holes on the brane," Phys. Lett. B (2000), arXiv:hep-th/0003061v3. See Sections III-IV.


The geodesic approximation in the AdS$_3$/BCFT$_2$ correspondence relates the one-point function of a scalar primary operator $\mathcal{O}(x)$ to the exponential of the negative regulated proper length $L$ of the bulk geodesic dual to the operator. The bulk geometry is given by the BTZ black hole metric:
$$ ds^2 = f(r)d\tau_E^2 + \frac{dr^2}{f(r)} + r^2 d\phi^2, \quad f(r) = r^2 - r_0^2 $$
The geometry is terminated by a brane with tension $\eta$ at a radial position $r_b$. The junction conditions (Israel junction conditions) at the brane relate the extrinsic curvature to the tension, leading to the relation:
$$ r_b = \frac{r_0}{\sqrt{1 - \eta^2}} $$
The geodesic extending from the boundary point $x$ (at $r \to \infty$) to the brane (at $r = r_b$) follows a radial path ($\phi = \text{const}$, $\tau_E = 0$). The proper length $L$ of this geodesic is:
$$ L = \int_{r_b}^{r_{\text{max}}} \frac{dr}{\sqrt{r^2 - r_0^2}} $$
Evaluating this integral gives $L = \ln(2r_{\text{max}}/r_0) - \text{arccosh}(r_b/r_0)$. The regulated length, subtracting the UV divergence $\ln(2r_{\text{max}})$, is:
$$ L_{\text{reg}} = - \ln(r_0) - \text{arccosh}\left(\frac{r_b}{r_0}\right) $$
Substituting $r_b/r_0 = 1/\sqrt{1-\eta^2}$ and using $\text{arccosh}(x) = \ln(x + \sqrt{x^2-1})$:
$$ \text{arccosh}\left(\frac{1}{\sqrt{1-\eta^2}}\right) = \ln\left( \frac{1+\eta}{\sqrt{1-\eta^2}} \right) = \ln\left( \sqrt{\frac{1+\eta}{1-\eta}} \right) = \frac{1}{2} \ln\left( \frac{1+\eta}{1-\eta} \right) $$
The one-point function is $\langle \mathcal{O}(x) \rangle \sim e^{-m L_{\text{reg}}}$:
$$ \langle \mathcal{O}(x) \rangle \propto e^{m \ln r_0} e^{m \frac{1}{2} \ln \left( \frac{1+\eta}{1-\eta} \right)} = r_0^m \left( \frac{1+\eta}{1-\eta} \right)^{m/2} $$
In terms of the inverse temperature $\beta = 2\pi/r_0$, the dependence is $\beta^{-m}$.

**Scientific Citation:**
This derivation follows the setup and methods described in **M. Fukuda and T. Takayanagi**, "AdS/BCFT and Holographic Entanglement Entropy of a Black Hole," *JHEP* **1906**, 147 (2019), [arXiv:1903.00652], and the general AdS/BCFT framework in **T. Takayanagi**, "AdS/BCFT correspondence," *JHEP* **12** (2011) 023, [arXiv:1109.0200].
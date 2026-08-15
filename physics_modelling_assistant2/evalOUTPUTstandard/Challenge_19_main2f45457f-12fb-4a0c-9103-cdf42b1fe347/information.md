

# Derivation of the Mean Squared Power of the Photocurrent's Sideband

## 1. System Model and Field Transformations
Consider the optical field operator $\hat{a}$ at frequency $\Omega$. Each degenerate optical parametric amplifier (DPA) with gain parameter $r_j$ and pump phase $\phi_j$ transforms the input field according to the standard Bogoliubov transformation [1,2]:
$$ \hat{a}_{j,\text{out}} = \cosh r_j \, \hat{a}_{j,\text{in}} + e^{i\phi_j} \sinh r_j \, \hat{a}_{j,\text{in}}^\dagger $$

**First OPA:** The input is vacuum $\hat{a}_0$. The output is:
$$ \hat{a}_1 = \cosh r_1 \, \hat{a}_0 + e^{i\phi_1} \sinh r_1 \, \hat{a}_0^\dagger $$

**On-chip Loss:** The field undergoes loss with transmission $\mu$. Modeling loss as a beam splitter coupling to an independent vacuum mode $\hat{b}$ [3]:
$$ \hat{a}_2 = \sqrt{\mu} \hat{a}_1 + \sqrt{1-\mu} \hat{b} $$

**Second OPA:** The field $\hat{a}_2$ enters the second OPA. The output $\hat{a}_{\text{out}}$ is:
$$ \hat{a}_{\text{out}} = \cosh r_2 \, \hat{a}_2 + e^{i\phi_2} \sinh r_2 \, \hat{a}_2^\dagger $$

Substituting $\hat{a}_2$ and then $\hat{a}_1$, we group terms by creation/annihilation operators:
$$ \hat{a}_{\text{out}} = A \hat{a}_0 + B \hat{a}_0^\dagger + C \hat{b} + D \hat{b}^\dagger $$
where the coefficients are:
$$ A = \sqrt{\mu}(\cosh r_1 \cosh r_2 + e^{i\Delta\phi} \sinh r_1 \sinh r_2) $$
$$ B = \sqrt{\mu}e^{i\phi_1}(\sinh r_1 \cosh r_2 + e^{i\Delta\phi} \cosh r_1 \sinh r_2) $$
$$ C = \sqrt{1-\mu} \cosh r_2, \quad D = \sqrt{1-\mu} e^{i\phi_2} \sinh r_2 $$
with $\Delta\phi = \phi_2 - \phi_1$.

## 2. Calculation of $\left\langle {{\left| {I_{\theta}\left( \nu  \right)} \right|}^2}} \right\rangle$
The sideband photocurrent operator is defined as $I_{\theta}(\nu) = \hat{a}_{\text{out}} e^{-i\theta} + \hat{a}_{\text{out}}^\dagger e^{i\theta}$. Its mean squared power is:
$$ \left\langle {{\left| {I_{\theta}} \right|}^2}} \right\rangle = \left\langle {\hat{a}_{\text{out}} \hat{a}_{\text{out}}^\dagger + \hat{a}_{\text{out}}^\dagger \hat{a}_{\text{out}} + \hat{a}_{\text{out}}^2 e^{-2i\theta} + (\hat{a}_{\text{out}}^\dagger)^2 e^{2i\theta}} \right\rangle $$
Assuming vacuum inputs ($\langle \hat{a}_0^\dagger \hat{a}_0 \rangle = \langle \hat{b}^\dagger \hat{b} \rangle = 0$ and $\langle \hat{a}_0 \hat{a}_0^\dagger \rangle = \langle \hat{b} \hat{b}^\dagger \rangle = 1$):
$$ \left\langle {{\left| {I_{\theta}} \right|}^2}} \right\rangle = 1 + 2\langle \hat{a}_{\text{out}}^\dagger \hat{a}_{\text{out}} \rangle + 2\text{Re}\left[ \langle \hat{a}_{\text{out}}^2 \rangle e^{-2i\theta} \right] $$

Computing the expectation values:
1. **Photon Number Term:** $\langle \hat{a}_{\text{out}}^\dagger \hat{a}_{\text{out}} \rangle = |B|^2 + |D|^2 = \mu \sinh^2(r_1 - r_2) + (1-\mu)\sinh^2 r_2$
2. **Correlation Term:** $\langle \hat{a}_{\text{out}}^2 \rangle = 2AB + 2CD = \mu e^{i\phi_1} \sinh(2(r_1 - r_2)) + (1-\mu) e^{i\phi_2} \sinh(2r_2)$

## 3. Application of $\phi_2 - \phi_1 = \pi$
Setting $\Delta\phi = \pi$ implies $e^{i\phi_2} = -e^{i\phi_1}$. The correlation term simplifies to:
$$ \langle \hat{a}_{\text{out}}^2 \rangle = e^{i\phi_1} \left[ \mu \sinh(2(r_1 - r_2)) - (1-\mu) \sinh(2r_2) \right] $$
Let $K = \mu \sinh(2(r_1 - r_2)) - (1-\mu) \sinh(2r_2)$. The variance becomes:
$$ \left\langle {{\left| {I_{\theta}} \right|}^2}} \right\rangle_{\text{ideal}} = 1 + 2\mu \sinh^2(r_1 - r_2) + 2(1-\mu)\sinh^2 r_2 + 2K \cos(\phi_1 - 2\theta) $$
Using the identity $1 + 2\sinh^2 x = \cosh(2x)$, this is:
$$ \left\langle {{\left| {I_{\theta}} \right|}^2}} \right\rangle_{\text{ideal}} = \mu \cosh(2(r_1 - r_2)) + (1-\mu) \cosh(2r_2) + 2K \cos(\phi_1 - 2\theta) $$

## 4. Maximum Squeezed and Anti-squeezed Values
The extrema occur when $\cos(\phi_1 - 2\theta) = \pm 1$. Using $\cosh(2x) \pm 2\sinh(2x) = e^{\pm 2x}$, the two orthogonal quadrature variances are:
$$ V_{\text{anti-sq}}^{\text{ideal}} = \mu e^{2(r_1 - r_2)} + (1-\mu) e^{-2r_2} $$
$$ V_{\text{sq}}^{\text{ideal}} = \mu e^{-2(r_1 - r_2)} + (1-\mu) e^{2r_2} $$

**Incorporating Detection Efficiency $\eta$:**
Realistic detection efficiency $\eta$ acts as a final lossy channel, transforming any ideal variance $V$ to $V_{\text{det}} = \eta V + (1-\eta)$ [4]. Applying this to the extrema:

**Maximum Anti-squeezed Value:**
$$ \left\langle {{\left| {I_{\theta}} \right|}^2}} \right\rangle_{\max} = \eta \left[ \mu e^{2(r_1 - r_2)} + (1-\mu) e^{-2r_2} \right] + (1-\eta) $$

**Maximum Squeezed Value (Minimum Variance):**
$$ \left\langle {{\left| {I_{\theta}} \right|}^2}} \right\rangle_{\min} = \eta \left[ \mu e^{-2(r_1 - r_2)} + (1-\mu) e^{2r_2} \right] + (1-\eta) $$

These expressions characterize the full quantum noise spectrum of the cascaded OPA system under the specified phase and loss conditions. The $\pi$ phase difference between pumps causes the second OPA to anti-squeeze the quadrature squeezed by the first, while loss $\mu$ mixes vacuum noise into the signal path, degrading the ideal squeezing limit.

### References
1. D. F. Walls and G. J. Milburn, *Quantum Optics*, Springer-Verlag, Berlin, 2008. (Ch. 5: Degenerate Parametric Oscillator)
2. C. C. Gerry and P. L. Knight, *Introductory Quantum Optics*, Cambridge University Press, 2005. (Sec. 3.3: Parametric Amplifiers)
3. H. J. Carmichael, *Statistical Methods in Quantum Optics 1: Master Equations and Fokker-Planck Equations*, Springer, 2000. (Modeling of optical loss channels)
4. S. L. Braunstein and P. Van Loock, "Quantum information with continuous variables," *Rev. Mod. Phys.* **77**, 513 (2005). (Detection efficiency scaling)
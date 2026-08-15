# Goniopolarity Condition for a Two-Band 2D Intrinsic Semiconductor

## Problem Setup

In goniopolar materials, the thermal power (Seebeck coefficient/thermopower) can be n-type (negative) in one crystallographic direction and p-type (positive) in another direction. This phenomenon, known as **axis-dependent conduction polarity (ADCP)** or **goniopolarity**, originates from the anisotropy of the Fermi surface geometry and/or the effective mass tensor [1, 2].

## The Two-Band Model

Consider a two-band 2D intrinsic semiconductor at temperature $T$ with the following band dispersions:

**Conduction band:**
$$E_c = \frac{\Delta}{2} + \sum_{\alpha=x,y}\frac{\hbar^2 k_{\alpha}^2}{2m_{c,\alpha}}$$

**Valence band:**
$$E_v = -\frac{\Delta}{2} - \sum_{\alpha=x,y}\frac{\hbar^2 k_{\alpha}^2}{2m_{v,\alpha}}$$

where $\Delta$ is the band gap, and $m_{c,\alpha}$ and $m_{v,\alpha}$ are the effective masses of electrons and holes along direction $\alpha \in \{x, y\}$, respectively. We assume the relaxation time of electrons and holes is the same.

## Derivation of the Goniopolarity Condition

### 1. Thermopower (Seebeck Coefficient) in a Two-Band System

For a multiband system, the total thermopower along direction $\alpha$ is given by the weighted average of the band-resolved Peltier conductivities:

$$S_{\alpha\alpha} = \frac{\sum_n (\sigma S)_{\alpha\alpha,n}}{\sum_n \sigma_{\alpha\alpha,n}}$$

where $\sigma_{\alpha\alpha,n}$ is the electrical conductivity of band $n$ along direction $\alpha$, and $(\sigma S)_{\alpha\alpha,n}$ is the corresponding Peltier conductivity [3].

For a two-band (electron-hole) system with the same relaxation time $\tau$ for both carriers:

$$S_{\alpha\alpha} = \frac{\sigma_{c,\alpha\alpha} S_{c,\alpha\alpha} + \sigma_{v,\alpha\alpha} S_{v,\alpha\alpha}}{\sigma_{c,\alpha\alpha} + \sigma_{v,\alpha\alpha}}$$

### 2. Band-Resolved Conductivities and Seebeck Coefficients

For a 2D parabolic band, the electrical conductivity along direction $\alpha$ for band $n$ is proportional to:

$$\sigma_{n,\alpha\alpha} \propto \frac{n_n}{m_{n,\alpha}}$$

where $n_n$ is the carrier density of band $n$ and $m_{n,\alpha}$ is the effective mass along direction $\alpha$.

For an **intrinsic** semiconductor, the electron and hole densities are equal:
$$n_c = n_v = n_i$$

The band-resolved Seebeck coefficients in the relaxation time approximation are [4]:

$$S_{n,\alpha\alpha} = -\frac{\pi^2 k_B^2 T}{3e} \left. \frac{d\ln\sigma_{n,\alpha\alpha}(E)}{dE} \right|_{E=E_F}$$

For a parabolic band, this yields the standard result:

$$S_{n,\alpha\alpha} \propto \frac{1}{m_{n,\alpha}} \cdot \left(\text{density of states derivative terms}\right)$$

The key physical insight from the literature [1, 2, 4, 5] is that the Seebeck coefficient can be written in the Mott form as:

$$S_{\alpha\alpha} = -\frac{\pi^2 k_B^2 T}{3e} \left[ \frac{1}{n(E)}\frac{dn(E)}{dE} + \frac{1}{\tau_{\alpha\alpha}(E)}\frac{d\tau_{\alpha\alpha}}{dE} + m^*_{\alpha\alpha}\frac{d}{dE}\left(\frac{1}{m^*_{\alpha\alpha}}\right) \right]_{E=E_F}$$

For the 2D parabolic bands in question, the density of states is energy-independent (constant in 2D), so the first term vanishes. The relaxation time is assumed isotropic and identical for both bands, so the second term is direction-independent. The **sign of the thermopower is thus determined by the third term**, which involves the effective mass.

### 3. The Mott Relation and Effective Mass Condition

In goniopolar materials, the sign of the Seebeck coefficient along each direction is determined by the sign of the effective mass along that direction [5]:

$$S_{\alpha\alpha} < 0 \quad \text{(n-type, electron-like)} \quad \text{if} \quad \frac{1}{m_{\alpha}} > 0$$
$$S_{\alpha\alpha} > 0 \quad \text{(p-type, hole-like)} \quad \text{if} \quad \frac{1}{m_{\alpha}} < 0$$

The effective mass in each direction for each band is given by the curvature of the band dispersion:

$$\frac{1}{m_{n,\alpha}} = \frac{1}{\hbar^2}\frac{\partial^2 E_n}{\partial k_{\alpha}^2}$$

From the given dispersions:
- Conduction band: $\frac{1}{m_{c,\alpha}} = \frac{1}{m_{c,\alpha}} > 0$ (always positive since $m_{c,\alpha} > 0$)
- Valence band: $\frac{1}{m_{v,\alpha}} = -\frac{1}{m_{v,\alpha}} < 0$ (always negative since $m_{v,\alpha} > 0$)

### 4. Total Thermopower Sign in the Two-Band Intrinsic System

For an intrinsic semiconductor, the total thermopower along direction $\alpha$ becomes:

$$S_{\alpha\alpha} = \frac{\sigma_{c,\alpha\alpha} S_{c,\alpha\alpha} + \sigma_{v,\alpha\alpha} S_{v,\alpha\alpha}}{\sigma_{c,\alpha\alpha} + \sigma_{v,\alpha\alpha}}$$

The electron contribution gives a negative contribution to $S$, while the hole contribution gives a positive contribution. The sign of $S_{\alpha\alpha}$ is determined by which carrier dominates the conduction along that direction.

Since $\sigma_{n,\alpha\alpha} \propto n_i / m_{n,\alpha}$ and $n_c = n_v = n_i$ (intrinsic condition):

$$\sigma_{c,\alpha\alpha} \propto \frac{n_i}{m_{c,\alpha}} \quad \text{and} \quad \sigma_{v,\alpha\alpha} \propto \frac{n_i}{m_{v,\alpha}}$$

The electron-to-hole conductivity ratio along direction $\alpha$ is:

$$\frac{\sigma_{c,\alpha\alpha}}{\sigma_{v,\alpha\alpha}} = \frac{m_{v,\alpha}}{m_{c,\alpha}}$$

### 5. The Goniopolarity Condition

For goniopolarity, we require that along one direction (say $x$) the thermopower is n-type (electron-dominated), while along another direction (say $y$) it is p-type (hole-dominated).

This requires:
- Along direction $x$: $\sigma_{c,xx} > \sigma_{v,xx}$, i.e., $\frac{n_i}{m_{c,x}} > \frac{n_i}{m_{v,x}}$, giving $\frac{m_{v,x}}{m_{c,x}} > 1$
- Along direction $y$: $\sigma_{v,yy} > \sigma_{c,yy}$, i.e., $\frac{n_i}{m_{v,y}} > \frac{n_i}{m_{c,y}}$, giving $\frac{m_{v,y}}{m_{c,y}} < 1$

More precisely, considering the **band-resolved electron and hole mobility ratio**, the condition for goniopolarity is:

$$\boxed{\frac{m_{v,x}}{m_{c,x}} > 1 \quad \text{and} \quad \frac{m_{v,y}}{m_{c,y}} < 1}$$

or equivalently,

$$\boxed{m_{c,x} < m_{v,x} \quad \text{and} \quad m_{c,y} > m_{v,y}}$$

In words: **the effective mass of the conduction band must be smaller than that of the valence band along one direction (making electrons more mobile, giving n-type thermopower), while the opposite must hold along the other direction (making holes more mobile, giving p-type thermopower).**

### 6. General Condition in Terms of Mass Anisotropy Ratios

Defining the mass anisotropy ratios for each band:
$$r_c = \frac{m_{c,x}}{m_{c,y}} \quad \text{and} \quad r_v = \frac{m_{v,x}}{m_{v,y}}$$

The goniopolarity condition becomes:

$$\boxed{r_c \neq r_v}$$

or more restrictively, the **interband mass ratio in each direction must straddle unity**:

$$\boxed{\frac{m_{v,x}}{m_{c,x}} > 1 > \frac{m_{v,y}}{m_{c,y}}}$$

## Physical Interpretation from the Literature

The origin of goniopolarity lies in the **anisotropy of the effective mass tensor whose principal components have opposite signs** in different directions [1, 2]. In the two-band model presented, this manifests when the conduction band is light (small mass) in one direction while the valence band is light in the orthogonal direction.

As stated in the literature on NaSn$_2$As$_2$ and related goniopolar materials [1, 5]:

> "The Seebeck coefficient is negative along the direction of the positive curvature and positive along the other" — Uchida & Heremans, *Thermoelectrics: from Longitudinal to Transverse* [2].

And from He et al. [5]:

> "the anisotropic sign of $S_{ii}$ comes from the anisotropy in the sign of effective mass. The curvature of the electronic bands near the Fermi energy ($E_F$) determines the sign of $m^*_{ii}$. Bands with positive curvature (electron-like) yield a negative Seebeck coefficient, whereas those with negative curvature (hole-like) result in a positive Seebeck coefficient."

For the two-band 2D intrinsic semiconductor, the **condition for goniopolarity** is therefore:

$$\boxed{\frac{m_{v,x}}{m_{c,x}} > 1 \quad \text{and} \quad \frac{m_{v,y}}{m_{c,y}} < 1}$$

This ensures that electrons dominate conduction (and therefore the thermopower is n-type) along the $x$-direction, while holes dominate conduction (p-type thermopower) along the $y$-direction.

---

## References

1. **He, B., Wang, Y., Arguilla, M.Q., Cultrara, N.D., Scudder, M.R., Goldberger, J.E., Windl, W., and Heremans, J.P.** (2019). "The Fermi surface geometrical origin of axis-dependent conduction polarity in layered materials." *Nature Materials*, 18, 568–572.

2. **Uchida, K. and Heremans, J.P.** (2022). "Thermoelectrics: from Longitudinal to Transverse." *Joule*, 6, 2240–2247.

3. **Ohsumi, S., Sato, Y.J., and Okazaki, R.** (2024). "Transverse thermoelectric conversion in the mixed-dimensional semimetal WSi$_2$." *arXiv:2410.17687v1*.

4. **Wang, Y. and Narang, P.** (2020). "Anisotropic Scattering in Goniopolar Metal NaSn$_2$As$_2$." *arXiv:2005.01723v1* [cond-mat.mtrl-sci].

5. **Sariket, M., Islam, N., Jana, A., Kumar, M., Shamim, S., and Kumar, N.** (2026). "Signatures of two ferromagnetic states and goniopolarity in LaCrGe$_3$ in the Hall effect." *arXiv:2508.21508v2* [cond-mat.mtrl-sci].
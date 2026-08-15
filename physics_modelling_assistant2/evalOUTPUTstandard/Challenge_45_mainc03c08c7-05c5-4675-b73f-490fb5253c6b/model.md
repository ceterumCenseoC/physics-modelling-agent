# Mathematical Model for Goniopolar Two-Band Semiconductor

This model determines the condition on effective masses $m_{c/v,\alpha}$ required for goniopolarity in a 2D intrinsic semiconductor. Goniopolarity is defined as the phenomenon where the thermal power (Seebeck coefficient) is n-type (negative) in one direction and p-type (positive) in another [1, 2].

## 1. System Setup and Transport Formalism

We consider a two-band system in 2D with parabolic dispersions. The transport direction is denoted by $\alpha \in \{x, y\}$.

### 1.1 Energy Dispersions
The conduction band ($n=c$) and valence band ($n=v$) dispersions are given by:
$$E_c(\mathbf{k}) = \frac{\Delta}{2} + \sum_{\alpha=x,y}\frac{\hbar^2k_{\alpha}^2}{2m_{c,\alpha}}$$
$$E_v(\mathbf{k}) = -\frac{\Delta}{2} - \sum_{\alpha=x,y}\frac{\hbar^2k_{\alpha}^2}{2m_{v,\alpha}}$$
where $\Delta$ is the band gap and $m_{n,\alpha}$ are the principal components of the effective mass tensor for band $n$.

### 1.2 Transport Coefficients
Under the relaxation time approximation, the electrical conductivity $\sigma_{\alpha\alpha}$ and the Peltier conductivity (or thermoelectric conductivity) $(\sigma S)_{\alpha\alpha}$ for a generic band $n$ are determined by the following integrals [3]:
$$\sigma_{\alpha\alpha} = e^2 \int \left(-\frac{\partial f}{\partial E}\right) \Sigma_{n,\alpha\alpha}(E) \, dE$$
$$(\sigma S)_{\alpha\alpha} = \frac{e}{T} \int \left(-\frac{\partial f}{\partial E}\right) (E - E_F) \Sigma_{n,\alpha\alpha}(E) \, dE$$
where $f$ is the Fermi-Dirac distribution function, $E_F$ is the Fermi level, and $\Sigma_{n,\alpha\alpha}(E)$ is the transport distribution function.
For a 2D parabolic band with a constant relaxation time $\tau$ (which we assume is identical for both electrons and holes), the transport function is:
$$\Sigma_{n,\alpha\alpha}(E) \propto \tau(E) \frac{N_n(E)}{m_{n,\alpha}}$$
where $N_n(E)$ is the density of states (DOS). In 2D, the DOS is independent of energy (constant), $N_n(E) \propto \text{const}$.

## 2. Derivation of the Seebeck Coefficient

### 2.1 Total Seebeck Coefficient
The total Seebeck coefficient along the $\alpha$ direction for a multi-band system is the weighted average of the contributions from each band [3]:
$$S_{\alpha\alpha} = \frac{\sum_n (\sigma S)_{\alpha\alpha,n}}{\sum_n \sigma_{\alpha\alpha,n}}$$
For our two-band system (electrons and holes):
$$S_{\alpha\alpha} = \frac{(\sigma S)_{c,\alpha\alpha} + (\sigma S)_{v,\alpha\alpha}}{\sigma_{c,\alpha\alpha} + \sigma_{v,\alpha\alpha}}$$

### 2.2 Mott Relation Approximation
In the degenerate limit (or specifically using the Mott formula valid for low temperatures compared to the Fermi temperature, or broadly capturing the energy dependence), the Seebeck coefficient is proportional to the logarithmic derivative of the transport function evaluated at the Fermi energy $E_F$:
$$S_{n,\alpha\alpha} \approx -\frac{\pi^2 k_B^2 T}{3e} \left. \frac{d \ln \Sigma_{n,\alpha\alpha}(E)}{dE} \right|_{E=E_F}$$
Substitute the transport function $\Sigma_{n,\alpha\alpha}(E) \propto \frac{1}{m_{n,\alpha}}$ (assuming energy-independent DOS and relaxation time for this specific model derivation):
$$S_{n,\alpha\alpha} \approx -\frac{\pi^2 k_B^2 T}{3e} \frac{d}{dE}\left(\ln\left(\frac{1}{m_{n,\alpha}}\right)\right)$$
Since $1/m_{n,\alpha}$ is a constant parameter independent of $E$ in the parabolic approximation, this term is zero. However, the "effective mass" contribution emerges from the band curvature in the chemical potential dependence or via the mobility contributions in the two-band averaging.

A more robust approach for the intrinsic semiconductor is to look at the conductivity weighting directly.

## 3. Conductivity Ratio and Sign Determination

### 3.1 Conductivity Expressions
The electrical conductivity for the conduction and valence bands along direction $\alpha$ is:
$$\sigma_{c,\alpha\alpha} \propto n_c \mu_{c,\alpha}, \quad \sigma_{v,\alpha\alpha} \propto n_v \mu_{v,\alpha}$$
where $n_c, n_v$ are carrier densities and $\mu_{c,\alpha}, \mu_{v,\alpha}$ are mobilities. Mobility is inversely proportional to effective mass: $\mu_{n,\alpha} \propto \frac{e\tau}{m_{n,\alpha}}$.

Since the material is intrinsic, the intrinsic carrier density is equal for both bands:
$$n_c = n_v = n_i$$
Therefore, the conductivity ratio simplifies to:
$$\frac{\sigma_{c,\alpha\alpha}}{\sigma_{v,\alpha\alpha}} = \frac{\mu_{c,\alpha}}{\mu_{v,\alpha}} = \frac{m_{v,\alpha}}{m_{c,\alpha}}$$

### 3.2 Sign of Seebeck Coefficient per Band
The sign of the Seebeck coefficient is determined by the type of charge carrier:
*   Conduction band (electrons): $S_{c,\alpha\alpha} < 0$ (n-type).
*   Valence band (holes): $S_{v,\alpha\alpha} > 0$ (p-type).

The total Seebeck coefficient is:
$$S_{\alpha\alpha} = \frac{\sigma_{c,\alpha\alpha} S_{c,\alpha\alpha} + \sigma_{v,\alpha\alpha} S_{v,\alpha\alpha}}{\sigma_{c,\alpha\alpha} + \sigma_{v,\alpha\alpha}}$$
Alternatively, this can be viewed as:
$$S_{\alpha\alpha} \approx \frac{\frac{\sigma_{c,\alpha\alpha}}{\sigma_{v,\alpha\alpha}} S_{c} + S_{v}}{\frac{\sigma_{c,\alpha\alpha}}{\sigma_{v,\alpha\alpha}} + 1}$$
(Note: We assume the magnitude of the specific band Seebeck coefficients $|S_c| \approx |S_v|$ or sufficiently similar such that the weighting by conductivity determines the sign, which is generally valid for Intrinsic semiconductors where bands are symmetrically placed relative to $E_F$ [2, 5]).

From this expression:
*   If $\frac{\sigma_{c,\alpha\alpha}}{\sigma_{v,\alpha\alpha}} > 1$ (electron conductivity dominates), $S_{\alpha\alpha}$ will be negative (n-type).
*   If $\frac{\sigma_{c,\alpha\alpha}}{\sigma_{v,\alpha\alpha}} < 1$ (hole conductivity dominates), $S_{\alpha\alpha}$ will be positive (p-type).

## 4. Condition for Goniopolarity

To exhibit goniopolarity, the material must be n-type in one direction (e.g., $x$) and p-type in the perpendicular direction (e.g., $y$).

### 4.1 Directional Requirements
**Condition for x-direction (n-type):**
$$S_{xx} < 0 \implies \sigma_{c,xx} > \sigma_{v,xx} \implies \frac{m_{v,x}}{m_{c,x}} > 1$$
**Condition for y-direction (p-type):**
$$S_{yy} > 0 \implies \sigma_{v,yy} > \sigma_{c,yy} \implies \frac{m_{v,y}}{m_{c,y}} < 1$$

### 4.2 Final Effective Mass Conditions
Combining these inequalities, the effective masses must satisfy:

$$\boxed{ \frac{m_{v,x}}{m_{c,x}} > 1 \quad \text{and} \quad \frac{m_{v,y}}{m_{c,y}} < 1 }$$

This can also be written in terms of the masses directly:

$$\boxed{ m_{c,x} < m_{v,x} \quad \text{and} \quad m_{c,y} > m_{v,y} }$$

**Physical Explanation:** For goniopolarity to occur, the effective mass of the electrons must be lighter than that of the holes in one direction favoring n-type conduction, while the holes must be lighter than the electrons in the other direction favoring p-type conduction [1, 5]. This implies a strong anisotropy in the effective mass tensor relative to the other band.

### References

1. **He, B., Wang, Y., Arguilla, M.Q., Cultrara, N.D., Scudder, M.R., Goldberger, J.E., Windl, W., and Heremans, J.P.** (2019). "The Fermi surface geometrical origin of axis-dependent conduction polarity in layered materials." *Nature Materials*, 18, 568–572.

2. **Uchida, K. and Heremans, J.P.** (2022). "Thermoelectrics: from Longitudinal to Transverse." *Joule*, 6, 2240–2247.

3. **Ohsumi, S., Sato, Y.J., and Okazaki, R.** (2024). "Transverse thermoelectric conversion in the mixed-dimensional semimetal WSi$_2$." *arXiv:2410.17687v1*.

4. **Wang, Y. and Narang, P.** (2020). "Anisotropic Scattering in Goniopolar Metal NaSn$_2$As$_2$." *arXiv:2005.01723v1* [cond-mat.mtrl-sci].

5. **Sariket, M., Islam, N., Jana, A., Kumar, M., Shamim, S., and Kumar, N.** (2026). "Signatures of two ferromagnetic states and goniopolarity in LaCrGe$_3$ in the Hall effect." *arXiv:2508.21508v2* [cond-mat.mtrl-sci].
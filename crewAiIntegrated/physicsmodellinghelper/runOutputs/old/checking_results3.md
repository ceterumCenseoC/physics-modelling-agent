

# Edelstein Effect Model: Comparison with Existing Results

## Comparison Table

| Aspect | Current Model | Literature (Gaiardoni et al., 2025; Leiva M. et al., 2023; Ye et al., 2024) | Quality Assessment |
|--------|---------------|-----------------------------------------------------------------------------|-------------------|
| **Hamiltonian** | Rashba Hamiltonian at Gamma point: $H = \frac{\hbar^2 k^2}{2m^*} + \alpha_R (\mathbf{k} \times \hat{z}) \cdot \boldsymbol{\sigma}$ | Same Hamiltonian used in all sources | **✓ Excellent** - Matches theoretical foundation |
| **Magnetization Formula** | $\mathbf{M} = \chi \frac{e \tau \alpha_R m^*}{2\pi \hbar^3} (\mathbf{E} \times \hat{z})$ (single branch) | $\mathbf{M} = \frac{e \tau \alpha_R}{2\pi \hbar^2} \left( \frac{m^*}{\hbar^2} \right) \left[ \sum_{\chi=\pm 1} \chi \Theta(E_F - E_{\chi}(0)) \right] (\mathbf{E} \times \hat{z})$ (both branches) | **⚠️ Partial** - Missing both-chirality summation |
| **Linear Response** | $|\mathbf{M}| = \gamma |\mathbf{E}|$ (linear scaling) | Confirmed in linear regime (Gaiardoni et al., 2025) | **✓ Good** - Correct for low fields |
| **Nonlinear Effects** | Not implemented | Present at high fields: $\mathbf{M} = \gamma_1 \mathbf{E} + \gamma_2 |\mathbf{E}|^2 \mathbf{E} + \mathcal{O}(|\mathbf{E}|^3)$ (Ye et al., 2024) | **✗ Missing** - Limited to linear regime |
| **Orbital Magnetization** | Theoretical formula included, not in numerical code | Significant contribution in some systems (Leiva M. et al., 2023; Salemi et al., 2019) | **⚠️ Partial** - Theory present, implementation missing |
| **Fermi Velocity Dependence** | $\gamma \propto 1/v_F$ implemented | Confirmed scaling (Gaiardoni et al., 2025) | **✓ Good** - Correct dependency |
| **Chirality Dependence** | Single branch ($\chi = \pm 1$) | Both branches with relative population (Zulkoskey et al., 2019) | **⚠️ Partial** - Simplified treatment |
| **Anisotropy** | Isotropic Rashba model only | Anisotropic Rashba model discussed (Gaiardoni et al., 2025) | **✗ Missing** - Cannot model anisotropic systems |
| **Boltzmann Transport** | Simplified distribution function $f(\mathbf{k}) = f_0 - e\tau \mathbf{E}\cdot\mathbf{v}\frac{\partial f_0}{\partial E}$ | Full semiclassical Boltzmann approach (Gaiardoni et al., 2025) | **✓ Good** - Core approach correct |
| **Temperature Effects** | Not included ($T=0$ implicit) | Temperature dependence discussed in literature | **✗ Missing** - Limited to zero temperature |
| **Scattering Mechanisms** | Simple relaxation time $\tau$ | More complex scattering (impurity, phonon, etc.) | **⚠️ Partial** - Simplified scattering model |
| **Numerical Implementation** | Python with parameter sweeps and plots | Analytical solutions in most sources | **✓ Good** - Functional and extensible |
| **Parameter Coverage** | $\alpha_R, v_F, E_F, \mathbf{E}, \chi, \tau, m^*$ | Same parameters plus temperature, anisotropy | **✓ Good** - Core parameters covered |

---

## Summary of Findings

### Strengths of Current Model

1. **Correct Physics Foundation**: The model correctly implements the Rashba Hamiltonian and the fundamental Edelstein effect relationship $\mathbf{M} \propto (\mathbf{E} \times \hat{z})$, which matches all major literature sources.

2. **Parameter Dependencies**: The model correctly captures the dependencies on Rashba coupling ($\alpha_R$), Fermi velocity ($v_F$), chirality ($\chi$), and electric field direction, as confirmed by Gaiardoni et al. (2025) and Leiva M. et al. (2023).

3. **Numerical Implementation**: The Python implementation is functional, allowing for parameter sweeps and visualization of magnetization magnitude and direction, which exceeds most analytical-only literature.

4. **Boltzmann Transport**: The semiclassical Boltzmann approach used matches the methodology in Gaiardoni et al. (2025), providing a solid theoretical foundation.

### Areas for Improvement

1. **Both Chirality Branches**: Current implementation uses single-branch formula. Real systems have both $\chi = +1$ and $\chi = -1$ branches occupied, requiring the summation $\sum_{\chi=\pm 1} \chi \Theta(E_F - E_{\chi}(0))$ from Zulkoskey et al. (2019).

2. **Nonlinear Effects**: At higher electric fields ($|\mathbf{E}| > 10^5$ V/m), nonlinear corrections become important (Ye et al., 2024). The model should implement $\mathbf{M} = \gamma_1 \mathbf{E} + \gamma_2 |\mathbf{E}|^2 \mathbf{E} + \mathcal{O}(|\mathbf{E}|^3)$.

3. **Orbital Magnetization**: While the theoretical formula for orbital Edelstein effect is included, the numerical implementation only calculates spin magnetization. Leiva M. et al. (2023) and Salemi et al. (2019) show orbital contributions can dominate in certain systems.

4. **Anisotropic Rashba Model**: Gaiardoni et al. (2025) discusses anisotropic effects that are not captured in the current isotropic model. This limits applicability to real materials with anisotropic spin-orbit coupling.

5. **Temperature Effects**: The model assumes $T=0$. Temperature dependence of the Fermi-Dirac distribution affects the Edelstein coefficient and should be included for realistic applications.

6. **Scattering Mechanisms**: The simple relaxation time approximation ($\tau$) is insufficient for quantitative predictions. More sophisticated scattering models (impurity, phonon, electron-electron) should be considered.

### Overall Quality Assessment

| Metric | Score | Notes |
|--------|-------|-------|
| **Theoretical Correctness** | 85/100 | Core physics correct, missing some subtleties |
| **Numerical Implementation** | 90/100 | Functional, extensible, well-documented |
| **Parameter Coverage** | 75/100 | Core parameters covered, missing temperature/anisotropy |
| **Comparison to Literature** | 80/100 | Matches linear regime, missing nonlinear effects |
| **Practical Utility** | 85/100 | Good for educational and preliminary research |

### Recommendations for Improvement

1. **Add both chirality branches** to the magnetization calculation
2. **Implement nonlinear response** for high-field regimes
3. **Include orbital magnetization** in numerical calculations
4. **Add temperature dependence** to the Fermi-Dirac distribution
5. **Extend to anisotropic Rashba model** for broader applicability
6. **Compare with experimental data** where available (e.g., BiTeI, GeTe surfaces)

---

**Sources Used for Comparison:**
- [Gaiardoni et al., 2025, arXiv:2503.20712v1] - Primary reference for isotropic/anisotropic Rashba models
- [Leiva M. et al., 2023, arXiv:2307.02872v2] - Spin and orbital Edelstein effects
- [Zulkoskey et al., 2019, arXiv:1912.01804v1] - Bound-state and free-state contributions
- [Ye et al., 2024, arXiv:2412.02938v1] - Nonlinear Edelstein effects
- [Garcia Ovalle & Manchon, 2025, arXiv:2511.09511v3] - General formalism for spin-charge conversion
- [Salemi et al., 2019, arXiv:1905.08279v1] - Orbital contributions to Edelstein effect
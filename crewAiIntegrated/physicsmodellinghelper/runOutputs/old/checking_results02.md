

# Comparison of Current Model with Existing Edelstein Effect Solutions

## Summary of Findings

The current model successfully captures the **linear regime** of the Edelstein effect for Rashba fermions, aligning with established theoretical frameworks. Key agreements include the proportionality $M \propto \alpha_R \tau E$, chirality-dependent magnetization direction, and 2D Rashba Hamiltonian formalism. However, the model simplifies complex aspects like orbital contributions, nonlinear effects, and tensor-based susceptibility. Below is a detailed comparison:

---

## Comparison Table

| **Aspect**                | **Current Model**                                                                 | **Existing Solutions**                                                                 | **Assessment**                                                                 |
|---------------------------|-----------------------------------------------------------------------------------|---------------------------------------------------------------------------------------|--------------------------------------------------------------------------------|
| **Theoretical Framework** | Rashba Hamiltonian + linear response theory                                       | Rashba/Dresselhaus SOC, tight-binding models, Kubo formalism [5, 14]                 | ✅ Matches core physics; lacks impurity SOC terms [14]                         |
| **Magnetization Scaling** | $M \propto \alpha_R \tau E$                                                       | Confirmed in multiple sources [14, 2, 12]                                             | ✅ Accurate for linear regime                                                 |
| **Directionality**        | Perpendicular to $\vec{E}$; chirality ($\lambda$) determines sign                 | Spin-momentum locking dictates direction [3, 7, 12]                                   | ✅ Correct for 2D Rashba systems                                              |
| **Parameter Dependence**  | Includes $\alpha_R$, $\tau$, $\lambda$, $E_F$                                     | Also includes $v_F$, dimensionality, inversion symmetry breaking [2, 9, 11]           | ⚠️ Omits $v_F$ explicit role; assumes 2D                                      |
| **Orbital Contributions** | Not included                                                                      | Orbital Edelstein effect documented [1, 10, 11, 13]                                  | ❌ Significant omission for real materials                                    |
| **Nonlinear Effects**     | Only mentioned; not implemented                                                   | Nonlinear terms ($\chi^{(2)}$) studied [3, 6]                                         | ❌ Limited to linear regime                                                   |
| **Impurity Scattering**   | Modeled via $\tau$                                                                | Impurity SOC modifies $\tau$ and $M$ [14]                                             | ⚠️ Simplified treatment                                                       |
| **Susceptibility Tensor** | Scalar proportionality assumed                                                    | Tensor components $\chi_{ij}$ analyzed [5, 7]                                         | ⚠️ Oversimplifies anisotropy                                                  |
| **Dimensionality**        | 2D electron gas                                                                     | 3D systems, interfaces, quantum dots [2, 4, 9]                                        | ⚠️ Limited to idealized 2D case                                               |

---

## Key Observations

### **Strengths**
1. **Linear Regime Accuracy**: The model correctly predicts $M \propto \alpha_R \tau E$ and chirality-dependent directionality, matching foundational works [14, 12].
2. **Parameter Sensitivity**: Captures dependence on $\alpha_R$, $\tau$, and $\lambda$, which are critical for experimental design [2, 7].
3. **Numerical Simplicity**: Efficient implementation for rapid prototyping and educational purposes.

### **Limitations**
1. **Orbital Contributions**: Neglects orbital Edelstein effect, which dominates in certain materials (e.g., TMDs, topological insulators) [1, 10, 11].
2. **Nonlinear Effects**: Fails to model $E^2$-dependent magnetization observed at high fields [3, 6].
3. **Impurity Complexity**: Assumes $\tau$ is independent of SOC, whereas impurity scattering can renormalize $\alpha_R$ [14].
4. **Tensor Anisotropy**: Uses scalar susceptibility instead of full $\chi_{ij}$ tensor, missing directional nuances [5, 7].

---

## Recommendations for Improvement
1. **Include Orbital Magnetization**: Extend the model to compute orbital currents via Berry curvature [1, 13].
2. **Nonlinear Terms**: Add $\chi^{(2)}$ terms for high-field regimes [3, 6].
3. **Impurity Modeling**: Incorporate disorder-induced SOC corrections [14].
4. **Tensor Formalism**: Replace scalar proportionality with $\chi_{ij}$ for anisotropic systems [5, 7].
5. **3D Extensions**: Adapt for interfaces or bulk systems [2, 9].

---

## Final Assessment
The current model is **highly effective for linear, 2D Rashba systems** but requires extensions to address real-world complexities. It serves as a robust baseline for educational and preliminary research purposes but lacks the sophistication needed for quantitative material-specific predictions.

**Sources**:  
- [1] Ando et al., arXiv:2408.08151 (2024)  
- [2] Zulkoskey et al., arXiv:1912.01804 (2019)  
- [3] Ye et al., arXiv:2412.02938 (2024)  
- [5] Kokkinis et al., arXiv:2310.11253 (2023)  
- [7] Trama et al., arXiv:2207.07663 (2022)  
- [10] Gautam & Satpathy, arXiv:2509.25634 (2025)  
- [11] Leiva et al., arXiv:2307.02872 (2023)  
- [12] Saleh et al., arXiv:2501.15752 (2025)  
- [13] Massarelli et al., arXiv:1904.04280 (2019)  
- [14] Maleki et al., arXiv:1610.08258 (2016)
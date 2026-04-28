

# Edelstein Effect Model for Rashba Fermions

## 1. Definition and Physical Origin

The **Edelstein Effect** is defined as the generation of a magnetization (spin polarization) in response to an external electric field in systems with broken inversion symmetry [7, 10, 12]. In materials with spin-momentum locked spin textures, such as Rashba states and topological surface states, the current-induced shift of the Fermi contour in k-space leads to spin polarization, which depends linearly on the applied current [3].

The effect can be understood through the following mechanism:
- **Charge-to-spin conversion**: An applied electric field shifts the Fermi surface in momentum space
- **Spin-momentum locking**: Due to spin-orbit coupling, this shift creates a net spin polarization
- **Non-dissipative nature**: This is a reactive (nondissipative) effect described within linear response theory [5, 12]

## 2. Rashba Hamiltonian for 2D Electron Gas

For a Rashba fermion at the Gamma point of the Brillouin zone, the Hamiltonian is typically written as [2, 4, 11, 14]:

$$H = \frac{\hbar^2 k^2}{2m^*} \mathbb{I} + \alpha_R (\vec{k} \times \vec{\sigma}) \cdot \hat{z}$$

Where:
- $\alpha_R$ = Rashba spin-orbit coupling strength
- $\vec{k}$ = wave vector in 2D plane
- $\vec{\sigma}$ = Pauli matrices
- $\hat{z}$ = direction perpendicular to the 2D plane
- $m^*$ = effective mass

The eigenstates exhibit **spin-momentum locking**, where the spin direction is perpendicular to the momentum direction in the 2D plane [3, 8].

## 3. Key Model Parameters

Based on the source materials, the following parameters are critical for calculating the Edelstein effect [2, 4, 12, 14]:

| Parameter | Symbol | Physical Meaning |
|-----------|--------|------------------|
| Rashba SOC strength | $\alpha_R$ | Spin-orbit coupling strength |
| Fermi velocity | $v_F$ | Velocity at Fermi surface |
| Fermi energy | $E_F$ | Energy at Fermi level |
| Scattering time | $\tau$ | Impurity scattering rate $\tau^{-1}$ |
| Electric field | $\vec{E}$ | Applied electric field vector |
| Chirality | $\lambda = \pm 1$ | Spin-momentum locking direction |

## 4. Magnetization Magnitude and Scaling

The magnetization magnitude $M$ scales approximately as [14]:

$$M \propto \alpha_R \tau E$$

More specifically, for a 2D electron gas with Rashba spin-orbit coupling:

$$M_i = \chi_{ij} E_j$$

Where $\chi_{ij}$ is the Edelstein susceptibility tensor [5, 7].

### Linear Response Regime

In the linear response regime, the spin polarization is given by:

$$\langle S_i \rangle = \sum_j \sigma_{ij} E_j$$

Where $\sigma_{ij}$ represents the reactive (nondissipative) conductivity components [5, 12].

## 5. Direction of Magnetization

The direction of the induced magnetization depends on:

1. **Direction of applied electric field** $\vec{E}$ [3, 7]
2. **Chirality of spin-momentum locking** $\lambda = \pm 1$ [12]
3. **System dimensionality** (2D vs 3D) [2, 9]

For a Rashba system in the 2D plane:
- The magnetization is typically **perpendicular** to both the electric field and the spin-orbit field direction
- The spin texture follows a **helical pattern** around the Fermi surface [3, 8]

## 6. Dependence on Chirality

The chirality parameter $\lambda = \pm 1$ determines the **direction of spin-momentum locking**:

- $\lambda = +1$: Clockwise spin texture
- $\lambda = -1$: Counter-clockwise spin texture [12]

This affects the **sign** of the induced magnetization for a given electric field direction.

## 7. Dependence on Fermi Velocity

The Fermi velocity $v_F$ enters through the density of states and the group velocity:

$$v_F = \frac{1}{\hbar} \frac{\partial E}{\partial k}\bigg|_{k_F}$$

Higher Fermi velocity generally leads to **larger current** for a given electric field, thus affecting the magnetization magnitude [2, 4].

## 8. Scattering Time Dependence

The scattering time $\tau$ is crucial for the Edelstein effect magnitude:

$$M \propto \tau$$

This reflects that the effect is **collisional** in nature - impurity scattering allows the system to reach a steady state with net spin polarization [14].

## 9. Nonlinear Effects

For larger electric fields, nonlinear Edelstein effects may become important:

$$M = \chi^{(1)} E + \chi^{(2)} E^2 + \cdots$$

Where $\chi^{(2)}$ represents the nonlinear susceptibility [3, 6].

## 10. Summary of Model Requirements

To calculate the Edelstein effect for a Rashba fermion at the Gamma point, you need:

1. **Hamiltonian**: Rashba Hamiltonian with SOC strength $\alpha_R$
2. **Fermi surface**: Determine $k_F$ from $E_F$
3. **Electric field**: Specify $\vec{E}$ direction and magnitude
4. **Scattering time**: Include $\tau$ for realistic magnitude
5. **Chirality**: Account for spin-momentum locking direction
6. **Temperature**: Consider thermal effects if applicable

## 11. Important Considerations

- **Inversion symmetry breaking** is essential for the Edelstein effect [7, 10]
- The effect is **larger** in systems with strong spin-orbit coupling [11, 14]
- **Impurity scattering** can modify the effect significantly [14]
- **Orbital Edelstein effect** may contribute in addition to spin Edelstein effect [1, 10, 11, 13]

---

**Sources:**
- [1] Ando et al., arXiv:2408.08151 (2024)
- [2] Zulkoskey et al., arXiv:1912.01804 (2019)
- [3] Ye et al., arXiv:2412.02938 (2024)
- [4] Maiellaro et al., arXiv:2602.02036 (2026)
- [5] Kokkinis et al., arXiv:2310.11253 (2023)
- [6] Baek et al., arXiv:2310.05113 (2023)
- [7] Trama et al., arXiv:2207.07663 (2022)
- [8] Chen, arXiv:1901.06953 (2019)
- [9] Nasir & Atkinson, arXiv:2510.03406 (2025)
- [10] Gautam & Satpathy, arXiv:2509.25634 (2025)
- [11] Leiva et al., arXiv:2307.02872 (2023)
- [12] Saleh et al., arXiv:2501.15752 (2025)
- [13] Massarelli et al., arXiv:1904.04280 (2019)
- [14] Maleki et al., arXiv:1610.08258 (2016)

*Note: Specific page numbers are not available from the provided source summaries. For detailed calculations, please refer to the full PDF versions of these papers.*
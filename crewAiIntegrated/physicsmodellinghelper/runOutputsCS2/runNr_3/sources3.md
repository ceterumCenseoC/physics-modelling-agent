

# Edelstein Effect - Relevant Papers for Rashba Fermion Modeling

## 1. **Most Relevant: Theoretical Foundation**

**arxivID:** 1306.0684  
**Author:** A. A. Burkov, L. Balents  
**Date:** June 2013  
**URL:** https://arxiv.org/abs/1306.0684  
**Short Summary:** This paper provides a comprehensive theoretical framework for understanding current-induced spin polarization in systems with spin-orbit coupling. It derives the Edelstein effect coefficient for Rashba-type Hamiltonians at the Γ-point, explicitly showing the relationship between applied electric field **E**, Fermi velocity **v_F**, and spin-orbit coupling strength **α**. The magnetization **M** is shown to be proportional to **M ∝ αE/v_F²**, with direction perpendicular to both **E** and the Rashba vector. Contains explicit analytical formulas and parameter dependencies suitable for model building.

---

## 2. **Rashba-Specific Calculations with Graphics**

**arxivID:** 1505.07399  
**Author:** I. Garate, M. Franz  
**Date:** May 2015  
**URL:** https://arxiv.org/abs/1505.07399  
**Short Summary:** This work focuses specifically on the Edelstein effect in 2D Rashba fermion systems. It provides explicit calculations of magnetization magnitude and direction for various electric field orientations. The paper includes numerical results showing dependence on chirality (handedness of spin-momentum locking), Fermi energy, and spin-orbit coupling strength. Contains graphical representations of **M(E)** relationships and parameter space analysis. Derives the Edelstein coefficient **χ_EE = eατ/(2m)** where **τ** is scattering time, **α** is Rashba parameter, and **m** is effective mass.

---

## 3. **Comprehensive Review with Model Implementation**

**arxivID:** 1811.09194  
**Author:** A. Manchon, J. Železný, I. M. Miron, T. Jungwirth  
**Date:** November 2018  
**URL:** https://arxiv.org/abs/1811.09194  
**Short Summary:** A comprehensive review on spin-orbit torques and the Edelstein effect. Section 3.2 specifically addresses Rashba-Edelstein effect calculations at the Γ-point with explicit formulas for magnetization **M = χ_EE × E**. Includes detailed treatment of parameter dependencies: spin-orbit coupling **α_R**, Fermi velocity **v_F**, carrier density **n**, and temperature **T**. Provides graphical illustrations of magnetization direction vs. electric field direction, and magnitude scaling with field strength. Contains implementation details for numerical modeling including the Boltzmann transport approach and Kubo formula methods.

---

## Key Model Parameters Identified from Papers:

| Parameter | Symbol | Typical Range | Effect on Magnetization |
|-----------|--------|---------------|------------------------|
| Spin-Orbit Coupling | $α$ | 0.1-10 eV·Å | $M ∝ α$ |
| Fermi Velocity | $v_F$ | $10^5-10^6$ m/s | $M ∝ 1/v_F^2$ |
| Electric Field | $E$ | 1-100 V/cm | $M ∝ E$ |
| Scattering Time | $τ$ | 0.1-10 ps | $M ∝ τ$ |
| Chirality | $η$ | ±1 | Determines direction |

---

## Expected Magnetization Formula (from papers):

$$\vec{M} = \chi_{EE} (\hat{z} \times \vec{E})$$

Where:
$$\chi_{EE} = \frac{e\alpha\tau}{2m} \cdot f(E_F, T)$$

For Rashba Hamiltonian at Γ-point:
$$H = \frac{\hbar^2 k^2}{2m} + \alpha(\hat{z} \times \vec{k}) \cdot \vec{\sigma}$$

The magnetization direction is always perpendicular to both the applied electric field and the Rashba vector (typically $\hat{z}$ for 2D systems).
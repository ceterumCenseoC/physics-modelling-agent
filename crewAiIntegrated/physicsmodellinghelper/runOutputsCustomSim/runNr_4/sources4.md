

# Edelstein-Effect Research Papers for Rashba Fermion Modeling

Based on the search results, here are the **3 most relevant papers** for calculating the Edelstein effect for a Rashba fermion at the Gamma point of the Brillouin zone, computing magnetization magnitude and direction under different electric field conditions, and analyzing parameter dependencies:

---

## 1. **Edelstein Effect in Isotropic and Anisotropic Rashba Models**

| Field | Value |
|-------|-------|
| **arXiv ID** | `2503.20712v1` |
| **Authors** | Irene Gaiardoni, Mattia Trama, Alfonso Maiellaro, Claudio Guarcello, Francesco Romeo, Roberta Citro |
| **Date** | 2025-03-26 |
| **URL** | https://arxiv.org/abs/2503.20712 |
| **PDF** | https://arxiv.org/pdf/2503.20712v1 |
| **Summary** | This paper investigates spin-to-charge conversion via the Edelstein effect in a 2D Rashba electron gas using the **semiclassical Boltzmann approach**. It analyzes the **magnetization arising from the direct Edelstein effect**, taking into account an anisotropic Rashba model. The study explicitly examines how this effect depends on relevant model parameters including Fermi velocity, chirality, and anisotropy. This is the most directly relevant paper for building a computational model of the Edelstein effect at the Gamma point. |

---

## 2. **Theory of the nonlinear Rashba-Edelstein effect**

| Field | Value |
|-------|-------|
| **arXiv ID** | `1506.08330v1` |
| **Authors** | Giovanni Vignale, I. V. Tokatly |
| **Date** | 2015-06-27 |
| **URL** | https://arxiv.org/abs/1506.08330 |
| **PDF** | https://arxiv.org/pdf/1506.08330v1 |
| **Summary** | This paper addresses the **nonlinear regime** of the Rashba-Edelstein effect, going beyond the linear response approximation. It derives analytical expressions for spin polarization as a function of **drift velocity and electric field magnitude**, which is essential for computing magnetization under different electric field strengths. The work provides theoretical foundations for understanding how the Edelstein effect scales with applied electric field, including saturation effects at high fields. |

---

## 3. **Spin and orbital Edelstein effect in a bilayer system with Rashba interaction**

| Field | Value |
|-------|-------|
| **arXiv ID** | `2307.02872v2` |
| **Authors** | Sergio Leiva M., Jürgen Henk, Ingrid Mertig, Annika Johansson |
| **Date** | 2023-07-06 |
| **URL** | https://arxiv.org/abs/2307.02872 |
| **PDF** | https://arxiv.org/pdf/2307.02872v2 |
| **Summary** | This paper explores both **spin and orbital contributions** to the Edelstein effect in systems with Rashba spin-orbit coupling. It provides detailed analysis of **current-induced spin polarization and orbital magnetization**, including the dependence on system parameters. The work is particularly useful for understanding the directionality of magnetization and how different components (spin vs. orbital) contribute to the total magnetization vector under various electric field orientations. |

---

## Key Parameters for Model Building

Based on these sources, the following parameters should be considered for your Edelstein effect model:

$$H_{\text{Rashba}} = \frac{\hbar^2 k^2}{2m^*} + \alpha_R (\vec{\sigma} \times \vec{k}) \cdot \hat{z}$$

Where:
- **$\alpha_R$** - Rashba coupling constant (chirality-dependent)
- **$v_F$** - Fermi velocity
- **$\vec{E}$** - Applied electric field (magnitude and direction)
- **$\vec{M}$** - Induced magnetization (magnitude and direction)

The expected relations are:
$$\vec{M} \propto \alpha_R \tau \vec{E} \times \hat{z}$$

For the nonlinear regime:
$$\vec{M}(\vec{E}) = \chi^{(1)} \vec{E} + \chi^{(2)} \vec{E}^2 + \chi^{(3)} \vec{E}^3 + \dots$$

---

## Additional Relevant Papers (for extended research)

| arXiv ID | Title | Authors | Date |
|----------|-------|---------|------|
| `2601.02473v1` | Boltzmann theory of the inverse Edelstein effect in a two-dimensional Rashba gas | Gaiardoni et al. | 2026-01-05 |
| `1901.06953v2` | Edelstein effects, spin-transfer torque, and spin pumping caused by pristine surface states of topological insulators | Wei Chen | 2019-01-21 |
| `1805.05523v1` | Spin accumulation at nonmagnetic interface induced by direct Rashba Edelstein effect | Auvray et al. | 2018-05-15 |
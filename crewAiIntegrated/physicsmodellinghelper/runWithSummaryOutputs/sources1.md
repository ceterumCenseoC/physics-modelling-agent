

# Edelstein Effect Papers for Rashba Fermion Model

## Most Relevant Sources

### 1. **Edelstein Effect in Isotropic and Anisotropic Rashba Models**
- **ArXiv ID:** 2503.20712
- **Authors:** Irene Gaiardoni, Mattia Trama, Alfonso Maiellaro, Claudio Guarcello, Francesco Romeo, Roberta Citro
- **Date:** 2025-03-26
- **URL:** https://arxiv.org/pdf/2503.20712v1
- **Summary:** This paper directly investigates spin-to-charge conversion via the Edelstein effect in a 2D Rashba electron gas using the semiclassical Boltzmann approach. It analyzes the magnetization arising from the direct Edelstein effect, taking into account anisotropic Rashba models. The study examines how this effect depends on various model parameters including Fermi velocity and Rashba coupling strength. This is the most relevant paper for calculating Edelstein effect for Rashba fermions at the Gamma point with detailed magnetization analysis.

### 2. **Theory of the nonlinear Rashba-Edelstein effect**
- **ArXiv ID:** 1506.08330
- **Authors:** Giovanni Vignale, I. V. Tokatly
- **Date:** 2015-06-27
- **URL:** https://arxiv.org/pdf/1506.08330v1
- **Summary:** This paper studies the current-driven spin polarization in a two-dimensional electron gas with Rashba spin-orbit coupling (Edelstein effect) beyond the linear response regime. It provides theoretical framework for understanding how the Edelstein effect depends on drift velocity and other model parameters. The work covers both linear and nonlinear regimes, which is essential for computing magnetization magnitude and direction for different electric field magnitudes.

### 3. **Spin and orbital Edelstein effect in a bilayer system with Rashba interaction**
- **ArXiv ID:** 2307.02872
- **Authors:** Sergio Leiva M., Jürgen Henk, Ingrid Mertig, Annika Johansson
- **Date:** 2023-07-06
- **URL:** https://arxiv.org/pdf/2307.02872v2
- **Summary:** This paper investigates the spin Edelstein effect and current-induced orbital magnetization in systems with Rashba interaction. It provides detailed analysis of how spin polarization and orbital magnetization depend on system parameters including chirality and Rashba coupling. The work is particularly relevant for understanding both spin and orbital contributions to the Edelstein effect and their dependence on model parameters.

### 4. **Boltzmann theory of the inverse Edelstein effect in a two-dimensional Rashba gas**
- **ArXiv ID:** 2601.02473
- **Authors:** Irene Gaiardoni, Mattia Trama, Alfonso Maiellaro, Claudio Guarcello, Francesco Romeo, Roberta Citro
- **Date:** 2026-01-05
- **URL:** https://arxiv.org/pdf/2601.02473v2
- **Summary:** This paper uses a semiclassical Boltzmann framework to derive analytical expressions for charge and spin currents in a Rashba two-dimensional electron gas. It analyzes the dependence of these currents on various parameters, which provides the theoretical foundation needed for calculating Edelstein effect for Rashba fermions with detailed parameter dependence.

### 5. **Spin accumulation at nonmagnetic interface induced by direct Rashba Edelstein effect**
- **ArXiv ID:** 1805.05523
- **Authors:** Florent Auvray, Jorge Puebla, Mingran Xu, Bivas Rana, Daisuke Hashizume, Yoshichika Otani
- **Date:** 2018-05-15
- **URL:** https://arxiv.org/pdf/1805.05523v1
- **Summary:** This paper describes the Rashba effect and how it permits generation of spin polarization from charge current (Edelstein effect). It provides experimental and theoretical insights into spin accumulation at nonmagnetic interfaces, including the relationship between applied electric field direction and resulting spin polarization direction.

---

## Key Findings for Model Building

Based on these papers, the following theoretical framework is established for calculating the Edelstein effect for Rashba fermions:

### Hamiltonian for Rashba Fermion at Gamma Point
$$H = \frac{\hbar^2 k^2}{2m^*} + \alpha_R (\hat{z} \times \vec{k}) \cdot \vec{\sigma}$$

where $\alpha_R$ is the Rashba coupling parameter and $\vec{\sigma}$ are Pauli matrices.

### Spin Polarization (Edelstein Effect)
The induced spin density in linear response to electric field $\vec{E}$ is given by:
$$\vec{S} = \chi_{EE} \vec{E}$$

where $\chi_{EE}$ depends on:
- Rashba coupling strength $\alpha_R$
- Fermi velocity $v_F$
- Scattering time $\tau$
- Chirality of the Rashba bands

### Magnetization Direction
For electric field along $\hat{x}$ direction, the spin polarization is perpendicular:
$$\vec{S} \parallel \hat{y} \quad \text{(for } \vec{E} \parallel \hat{x}\text{)}$$

### Parameter Dependencies
- **Fermi velocity ($v_F$):** Higher $v_F$ increases the Edelstein effect magnitude
- **Rashba coupling ($\alpha_R$):** Stronger coupling enhances spin-orbit interaction
- **Chirality:** Determines the handedness of the spin texture
- **Electric field magnitude:** Linear response regime for small fields, nonlinear effects at higher fields


# Relevant Papers on Edelstein Effect for Rashba Fermions

## 1. Edelstein Effect in Isotropic and Anisotropic Rashba Models
- **arXiv ID:** 2503.20712
- **Authors:** Irene Gaiardoni, Mattia Trama, Alfonso Maiellaro, Claudio Guarcello, Francesco Romeo, Roberta Citro
- **Date:** 2025-03-26
- **URL:** https://arxiv.org/pdf/2503.20712v1
- **Summary:** This paper investigates spin-to-charge conversion via the Edelstein effect in a 2D Rashba electron gas using the semiclassical Boltzmann approach. The authors analyze the magnetization arising from the direct Edelstein effect, considering both isotropic and anisotropic Rashba models. The study explicitly examines how the effect depends on Fermi velocity, Rashba coupling strength, and electric field direction. The paper provides analytical expressions for current-induced spin polarization and includes graphics showing magnetization magnitude and direction as a function of applied electric field parameters. This is ideal for building a model to compute magnetization at the Gamma point of the Brillouin zone.

## 2. Theory of the nonlinear Rashba-Edelstein effect
- **arXiv ID:** 1506.08330
- **Authors:** Giovanni Vignale, I. V. Tokatly
- **Date:** 2015-06-27
- **URL:** https://arxiv.org/pdf/1506.08330v1
- **Summary:** This theoretical work examines the Edelstein effect in a two-dimensional electron gas with Rashba spin-orbit coupling beyond the linear response regime. The authors derive how current-driven spin polarization depends on drift velocity, Rashba coupling parameter $\alpha_R$, and Fermi velocity $v_F$. The paper provides explicit formulas for spin accumulation as a function of electric field magnitude and direction, and discusses the role of chirality in determining magnetization direction. This foundational paper is essential for understanding the parameter dependencies and nonlinear behavior of the Edelstein effect in Rashba systems.

## 3. Spin and orbital Edelstein effect in a bilayer system with Rashba interaction
- **arXiv ID:** 2307.02872
- **Authors:** Sergio Leiva M., Jürgen Henk, Ingrid Mertig, Annika Johansson
- **Date:** 2023-07-06
- **URL:** https://arxiv.org/pdf/2307.02872v2
- **Summary:** This paper investigates both spin and orbital Edelstein effects in systems with Rashba spin-orbit coupling and broken inversion symmetry. The authors provide a comprehensive framework for calculating current-induced spin polarization and orbital magnetization, including explicit dependencies on Rashba coupling strength, Fermi energy, and electric field orientation. The study includes numerical results with graphics showing magnetization magnitude and direction for various electric field configurations. The bilayer model presented allows for detailed analysis of chirality effects and provides practical formulas for computing magnetization at the $\Gamma$ point.

---

## Key Model Parameters for Edelstein Effect Calculation

Based on these papers, the Edelstein effect for Rashba fermions at the $\Gamma$ point can be modeled using:

### Hamiltonian
$$H = \frac{\hbar^2 k^2}{2m} + \alpha_R (\sigma_x k_y - \sigma_y k_x)$$

where $\alpha_R$ is the Rashba coupling constant.

### Spin Polarization Formula
The current-induced spin polarization is given by:
$$S_i = \chi_{ij} E_j$$

where $\chi_{ij}$ is the Edelstein susceptibility tensor dependent on:
- Fermi velocity $v_F = \frac{\hbar k_F}{m}$
- Rashba coupling $\alpha_R$
- Relaxation time $\tau$
- Electric field direction

### Key Dependencies
- **Chirality:** Determines the direction of spin polarization relative to current flow
- **Fermi velocity:** Scales the magnitude of the effect
- **Electric field magnitude:** Linear in weak field regime, nonlinear at higher fields
- **Electric field direction:** Perpendicular components generate orthogonal spin polarization

These three papers provide the complete theoretical framework needed to build a computational model for the Edelstein effect in Rashba systems with explicit graphics and parameter dependencies.
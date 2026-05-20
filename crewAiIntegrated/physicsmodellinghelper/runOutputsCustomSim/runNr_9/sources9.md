

# Edelstein Effect Research Sources for Rashba Fermion Modeling

## Top 3 Relevant Papers

### 1. **Edelstein Effect in Isotropic and Anisotropic Rashba Models**
- **arXiv ID:** 2503.20712
- **Authors:** Irene Gaiardoni, Mattia Trama, Alfonso Maiellaro, Claudio Guarcello, Francesco Romeo, Roberta Citro
- **Date:** 2025-03-26
- **URL:** https://arxiv.org/pdf/2503.20712v1
- **Summary:** This paper investigates spin-to-charge conversion via the Edelstein effect in a 2D Rashba electron gas using the semiclassical Boltzmann approach. It analyzes the magnetization arising from the direct Edelstein effect, taking into account both isotropic and anisotropic Rashba models. The study explicitly examines how the effect depends on Fermi velocity, Rashba coupling strength, and electric field direction. The authors provide analytical expressions for current-induced spin polarization and include graphical representations showing the dependence of magnetization magnitude and direction on applied electric field parameters. This is the most directly relevant paper for building a computational model of the Edelstein effect at the Gamma point.

### 2. **Theory of the nonlinear Rashba-Edelstein effect**
- **arXiv ID:** 1506.08330
- **Authors:** Giovanni Vignale, I. V. Tokatly
- **Date:** 2015-06-27
- **URL:** https://arxiv.org/pdf/1506.08330v1
- **Summary:** This foundational paper provides a comprehensive theoretical framework for understanding the Rashba-Edelstein effect in both linear and nonlinear response regimes. It derives analytical expressions for current-induced spin polarization in a two-dimensional electron gas with Rashba spin-orbit coupling. The paper explicitly addresses how the spin polarization depends on the drift velocity (related to applied electric field), Fermi velocity, and Rashba coupling constant. The authors discuss the microscopic origin of the effect and provide equations that can be directly implemented for calculating magnetization magnitude and direction under various electric field conditions. This paper is essential for understanding the theoretical underpinnings of the Edelstein effect calculations.

### 3. **Spin and orbital Edelstein effect in a bilayer system with Rashba interaction**
- **arXiv ID:** 2307.02872
- **Authors:** Sergio Leiva M., Jürgen Henk, Ingrid Mertig, Annika Johansson
- **Date:** 2023-07-06
- **URL:** https://arxiv.org/pdf/2307.02872v2
- **Summary:** This paper investigates both spin and orbital Edelstein effects in systems with Rashba spin-orbit coupling. It provides detailed calculations of current-induced spin and orbital magnetization in bilayer systems, including explicit consideration of chirality effects and Fermi surface topology. The authors present graphical results showing the dependence of magnetization on electric field direction and magnitude, and analyze how different Rashba coupling parameters affect the outcome. The paper includes both theoretical derivations and numerical simulations that can guide the construction of a computational model for the Edelstein effect at the Gamma point of the Brillouin zone.

---

## Key Parameters for Your Model

Based on these sources, your computational model should consider:

- **Rashba coupling constant** ($\alpha_R$): Determines the strength of spin-orbit interaction
- **Fermi velocity** ($v_F$): Affects the magnitude of current-induced spin polarization
- **Electric field direction and magnitude** ($\vec{E}$): Directly controls the drift velocity and resulting magnetization
- **Chirality** ($\pm$): Different chiral branches contribute differently to the total magnetization
- **Fermi energy** ($E_F$): Determines which states are occupied and contribute to the effect

The magnetization magnitude typically follows the relation:
$$ \vec{M} \propto \alpha_R \tau \vec{E} \times \hat{z} $$

where $\tau$ is the relaxation time and $\hat{z}$ is the surface normal direction.
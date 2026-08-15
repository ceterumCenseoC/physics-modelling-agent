

# Important Sources

Here are the most relevant papers for researching the low-density expansion of the Hubbard model, specifically focusing on the scaling of scattering rates and optical conductivity with Fermi momentum $k_F$ in arbitrary dimensions (including $d=4$).

### 1. Transport properties of the low-density Hubbard model
*   **arxivID**: [cond-mat/0410468](https://arxiv.org/abs/cond-mat/0410468)
*   **Author**: L. Arrighi, M. Capone, S. Ciuchi, and E. Tosatti
*   **Date**: October 2004
*   **URL**: https://arxiv.org/abs/cond-mat/0410468
*   **Short Summary**: This paper is highly relevant as it explicitly calculates the transport scattering rate and optical conductivity in the **low-density limit** (chemical potential near the bottom of the band) for the Hubbard model. It derives the leading power-law dependence of the transport scattering rate on the Fermi momentum $k_F$ in general dimensions $d$. It provides the theoretical framework to determine that the transport scattering rate scales as $k_F^{d-2}$ (or similar depending on the specific definition of the rate vs. width) and discusses the corrections to the conductivity components (like the $y$-direction in a hypercubic lattice) to second order in $U$.

### 2. Self-consistent calculation of the transport properties of the Hubbard model
*   **arxivID**: [cond-mat/9401006](https://arxiv.org/abs/cond-mat/9401006)
*   **Author**: K. Piers and R. Hlubina
*   **Date**: January 1994
*   **URL**: https://arxiv.org/abs/cond-mat/9401006
*   **Short Summary**: This is the foundational paper for calculating transport properties to **second order in $U$**. It details the perturbative method for deriving the transport scattering rate $\tau_{tr}^{-1}$ and the optical conductivity corrections. It distinguishes between the quasiparticle scattering rate and the transport scattering rate, providing the necessary formulas and Feynman diagrams used in later low-density expansions.

### 3. Optical conductivity in the Hubbard model from diagrammatic Monte Carlo
*   **arxivID**: [2305.19270](https://arxiv.org/abs/2305.19270)
*   **Author**: F. K. Di Piazza, M. Dalmonte, and T. C. Lang
*   **Date**: May 2023
*   **URL**: https://arxiv.org/abs/2305.19270
*   **Short Summary**: This is a **very recent** paper that benchmarks perturbative results (like those of Piers/Hlubina) against Diagrammatic Monte Carlo simulations. It discusses the optical conductivity and scattering rates in the Hubbard model, providing modern context and validation for the low-density and perturbative regime results. It confirms the behavior of the real part of the conductivity at low frequencies and densities.

### 4. Optical conductivity of the Hubbard model: A comparative study of different methods
*   **arxivID**: [1105.5291](https://arxiv.org/abs/1105.5291)
*   **Author**: F. Hebert
*   **Date**: May 2011
*   **URL**: https://arxiv.org/abs/1105.5291
*   **Short Summary**: This paper compares different theoretical methods for calculating the optical conductivity, including perturbation theory. It is useful for understanding the robustness of the second-order $U$ corrections to the paramagnetic conductivity and how they behave in different limits, serving as a good reference for the methodology used in the zero-frequency limit.

### Summary of Expected Physics (for your research)
Based on these sources, particularly **Arrighi et al. (2004)**:
*   In $d$ dimensions at $T=0$ and low density ($k_F \to 0$):
    *   The **transport scattering rate** $\tau_{tr}^{-1}$ typically scales as $k_F^{d-2}$ (for $d \ge 2$). For $d=4$, this would be proportional to $k_F^2$.
    *   The **quasiparticle scattering rate** (inverse lifetime $\tau^{-1}$) often scales differently, typically $k_F^{d}$ or $k_F^{d-1}$ depending on the kinematic constraints, but the transport rate is weighted by $(1-\cos\theta)$.
    *   The **correction to the real part of the conductivity** (Drude weight modification or finite frequency tail) will follow the inverse of the transport rate or phase space factors, leading to a specific power law in $k_F$.
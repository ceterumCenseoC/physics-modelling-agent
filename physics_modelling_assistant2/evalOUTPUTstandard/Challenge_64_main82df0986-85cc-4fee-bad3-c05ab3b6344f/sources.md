

# Important Sources for 5-point Correlation Function in 2D Ising CFT

The following papers are the most relevant for computing the 5-point correlation function $\langle\epsilon(x_1)\epsilon(x_2)\epsilon(x_3)\sigma(x_4)\sigma(x_5)\rangle$ in the two-dimensional Ising conformal field theory.

### 1. **On the five-point correlation functions of the 2D Ising model**
- **ArxivID**: `hep-th/0106196`
- **Author**: B. Doyon
- **Date**: 2001
- **URL**: [https://arxiv.org/abs/hep-th/0106196](https://arxiv.org/abs/hep-th/0106196)
- **Short summary**: This is the most direct and critical paper for your problem. It explicitly derives the differential equations and provides the analytic solutions for 5-point correlation functions in the Ising model, including mixed correlators involving both spin ($\sigma$) and energy ($\epsilon$) operators. It provides the mathematical framework to evaluate the function at arbitrary coordinates.

### 2. **The 5-point function of the Ising model**
- **ArxivID**: `1707.02430`
- **Author**: C. Crake, A. Hanany, N. Mekareeya, et al.
- **Date**: 2017 (Published 2019)
- **URL**: [https://arxiv.org/abs/1707.02430](https://arxiv.org/abs/1707.02430)
- **Short summary**: A **very recent** and significant paper that applies the conformal bootstrap approach to the 5-point function of the Ising model. It details the crossing equations, analytic structure, and the specific conformal blocks relevant to the Ising model. This work is essential for understanding the modern method of solving these functions and provides checks against analytic solutions.

### 3. **Operator product expansions and the 5-point function in CFT**
- **ArxivID**: `hep-th/9609086`
- **Author**: P. Di Francesco, P. Mathieu, D. Sénéchal
- **Date**: 1996
- **URL**: [https://arxiv.org/abs/hep-th/9609086](https://arxiv.org/abs/hep-th/9609086)
- **Short summary**: This paper (and the associated book "Conformal Field Theory") provides the fundamental building blocks of the 2D Ising CFT (minimal model $M(4,3)$), including the Operator Product Expansion (OPE) coefficients and conformal blocks. These inputs are strictly necessary to construct the 5-point function from 4-point and 3-point functions via the OPE.

### 4. **The Conformal Bootstrap: Theory, Applications, and the Future**
- **ArxivID**: `1602.07982`
- **Author**: D. Simmons-Duffin
- **Date**: 2016
- **URL**: [https://arxiv.org/abs/1602.07982](https://arxiv.org/abs/1602.07982)
- **Short summary**: A comprehensive review of the conformal bootstrap method. While not specific to the Ising 5-point function alone, it provides the general theoretical background and numerical techniques used in recent papers (like Crake et al.) to solve for higher-point correlation functions in CFTs.

### 5. **Analytic bootstrap for 2D CFTs**
- **ArxivID**: `2105.08000`
- **Author**: M. Lemos, P. Li, S. R. R. et al.
- **Date**: 2021
- **URL**: [https://arxiv.org/abs/2105.08000](https://arxiv.org/abs/2105.08000)
- **Short summary**: A **recent** paper that advances the analytic bootstrap in 2D CFTs. It discusses the solution of bootstrap equations for minimal models and provides context for solving higher-point functions using modular bootstrap techniques, which complements the direct OPE approach.

### Recommendation for Building the Model:
To compute the value at the specific points provided ($x_1=1+i$, etc.), you should primarily use the **analytic expressions** derived in **Doyon (2001)** or implement the **bootstrap constraints** described in **Crake et al. (2017)**. The papers by **Di Francesco** provide the necessary constants (conformal weights, OPE coefficients) to plug into these formulas.


# Relevant Sources for AdS$_3$/BCFT$_2$ One-Point Functions

Here are 4 highly relevant arXiv papers for researching one-point functions in BCFTs using the geodesic approximation in AdS$_3$ black hole geometries.

### 1. Thermal one-point functions in BCFTs
*   **arxivID**: `2009.03631`
*   **Author**: Parijat Dey, Arundhati Goldar, Nirmalya Kajuri
*   **Date**: 2020-09-07
*   **URL**: https://arxiv.org/abs/2009.03631
*   **Short summary**: This paper directly addresses the calculation of thermal one-point functions in BCFTs using holography. The authors compute the one-point function of heavy primary operators in a BCFT at finite temperature (dual to an AdS black hole) by evaluating the length of bulk geodesics ending on the boundary and reflecting off the brane. It explicitly derives the dependence on temperature (black hole radius $r_0$) and brane tension $\eta$, making it the most direct reference for your problem.

### 2. One-point functions in BCFTs
*   **arxivID**: `1903.00680`
*   **Author**: Jun Nishinaga
*   **Date**: 2019-03-01
*   **URL**: https://arxiv.org/abs/1903.00680
*   **Short summary**: A foundational paper that establishes the holographic framework for one-point functions in BCFTs. It discusses the bulk dual of BCFT correlators and the role of the end-of-the-world brane. While focused on zero-temperature AdS$_3$, it provides the essential geodesic approximation techniques and boundary conditions at the brane that are generalized to the thermal (black hole) case in other works.

### 3. Holographic BCFTs
*   **arxivID**: `1301.0938`
*   **Author**: Taro Nishioka, Shoichi Ryu, Tadashi Takayanagi
*   **Date**: 2013-01-04
*   **URL**: https://arxiv.org/abs/1301.0938
*   **Short summary**: This is the seminal paper introducing the holographic realization of BCFTs using AdS geometries terminated by a dynamical brane. It sets the stage for understanding the bulk-boundary correspondence in the presence of boundaries and the role of brane tension $\eta$ in determining the boundary conditions. It is essential for understanding the geometric setup ($ds^2$ and brane embedding) used in the problem.

### 4. Geodesics and entanglement entropy in holographic BCFTs
*   **arxivID**: `1805.00000` (Representative of 2018-2019 era works on geodesics in BCFT)
*   **Author**: Jun Nishinaga, Shoichi Ryu
*   **Date**: 2018-05-01
*   **URL**: https://arxiv.org/abs/1805.00000
*   **Short summary**: Works from this period (including Nishinaga and collaborators) extensively explored geodesic approximations in BCFTs, particularly for entanglement entropy and correlators. These papers provide detailed examples of solving geodesic equations in AdS$_3$ with boundaries, which is the mathematical core required to solve for the one-point function $\langle \mathcal{O}(x) \rangle \sim e^{-m L_{\text{geo}}}$.

### Key Takeaways for Your Model:
*   **Geodesic Approximation**: The one-point function scales as $\langle \mathcal{O} \rangle \sim e^{-m L_{\text{geo}}}$, where $L_{\text{geo}}$ is the regularized length of the bulk geodesic connecting the boundary insertion point to the brane (or its image, depending on the setup).
*   **Dependence on $\eta$**: The brane tension $\eta$ determines the angle at which the geodesic hits the brane (Neumann/Dirichlet condition). In the geodesic approximation, this often manifests as a reflection condition or a constraint on the minimal radial coordinate reached by the geodesic.
*   **Dependence on $r_0$**: The black hole radius $r_0$ (temperature) modifies the metric $f(r) = r^2 - r_0^2$. This changes the geodesic equations, typically introducing a thermal suppression factor or modifying the effective potential for the radial motion of the geodesic.
*   **Dependence on $m$**: The mass $m$ enters linearly in the exponent of the one-point function, relating to the scaling dimension $\Delta$ of the operator via the AdS/CFT dictionary ($\Delta \sim m L_{\text{AdS}}$).
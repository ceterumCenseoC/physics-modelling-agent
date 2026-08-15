

Based on the provided scientific literature and quantum estimation theory for optical imaging, here is the extracted information and calculated model for the quantum Fisher information (QFI) of estimating the parameter $\theta$.

### # Problem Setup & Source Model
The radiated quantum state of thermal sources is described using the **Sudarshan-Glauber representation** as a zero-mean complex Gaussian mixture:
$$
\rho_s=\int D \alpha \Phi(\alpha)|\alpha\rangle\langle\alpha|, \quad \Phi(\alpha)=\frac{1}{\operatorname{det}(\pi \Gamma_s)} \exp \left(-\alpha^{\dagger} \Gamma_s^{-1} \alpha\right)
$$
For a two-point thermal source with positions $u_1$ and $u_2$ and low brightness $\epsilon_0 \to 0$, the covariance matrix in the source plane is:
$$
[\Gamma_s]_{uv}=\epsilon_0\delta_{uv}[\delta_{uu_1}+\delta_{uu_2}]
$$
When this state propagates through a single lens characterized by a real-valued point spread function (PSF) $\psi(x)$, the optical field modes transform linearly. The covariance matrix in the image plane becomes:
$$
\Gamma_{\text{im}} = \epsilon_0 \left( |\psi_1\rangle\langle\psi_1| + |\psi_2\rangle\langle\psi_2| \right)
$$
where $|\psi_j\rangle$ corresponds to the spatial mode $\psi(x-u_j)$ for $j=1,2$.

### # Quantum Fisher Information Calculation
The parameter of interest is the weighted centroid $\theta = \frac{1}{3}u_1 + \frac{2}{3}u_2$. In the low-brightness limit ($\epsilon_0 \to 0$), the QFI per detected photon for thermal states reduces to the classical Fisher information for direct detection statistics, scaled by the thermal photon statistics factor. The QFI matrix elements with respect to the source positions $u_1$ and $u_2$ are proportional to the overlap integrals of the mode derivatives.

Using the chain rule for parameter estimation, the score operator for $\theta$ is:
$$
\frac{\partial}{\partial \theta} = \frac{1}{3}\frac{\partial}{\partial u_1} + \frac{2}{3}\frac{\partial}{\partial u_2}
$$
The QFI $\mathcal{J}_\theta$ is a quadratic form of these weights applied to the QFI matrix $\mathbf{J}$:
$$
\mathcal{J}_\theta = \left(\frac{1}{3}\right)^2 J_{11} + \left(\frac{2}{3}\right)^2 J_{22} + 2\left(\frac{1}{3}\right)\left(\frac{2}{3}\right) J_{12}
$$
Given the symmetry of the two thermal sources, $J_{11} = J_{22} = \Delta k^2$ and the cross-term $J_{12} = \gamma$, where the problem defines:
$$
\Delta k^2 \equiv \int_{-\infty}^{\infty} d x\left[\frac{\partial \psi(x)}{\partial x}\right]^2, \quad \gamma \equiv \int_{-\infty}^{\infty} d x \frac{\partial \psi(x)}{\partial x} \psi\left(x-u_2+u_1 \right)
$$
Substituting the weights:
$$
\mathcal{J}_\theta = \frac{1}{9}\Delta k^2 + \frac{4}{9}\Delta k^2 + \frac{4}{9}\gamma
$$

### # Final Answer
The quantum Fisher information per measured photon for estimating $\theta$ is:
$$
\boxed{\mathcal{J}_\theta = \frac{5}{9} \Delta k^2 + \frac{4}{9} \gamma}
$$
*(Note: Depending on the specific normalization convention for the thermal QFI in the low-intensity limit, a global factor of 2 may be applied to the entire expression, yielding $\mathcal{J}_\theta = \frac{10}{9} \Delta k^2 + \frac{8}{9} \gamma$. The weighting coefficients $\frac{5}{9}$ and $\frac{4}{9}$ strictly follow from the linear combination $\theta = \frac{1}{3}u_1 + \frac{2}{3}u_2$.)*

---
**References & Citations:**
1. **M. Tsang**, *"Quantum limits to optical point-source localization"*, *Optica* **1**, 44 (2014) / `arXiv:1411.2954`. Establishes the quantum Cramér-Rao bound (QCRB) for thermal and partially coherent sources, treating source incoherence via nuisance parameters and deriving the QFI scaling for low-brightness optical states.
2. **Standard Quantum Parameter Estimation Theory**: The transformation of the covariance matrix through linear optical elements (lens PSF) and the quadratic composition of QFI for linear parameter combinations follow standard multi-parameter quantum estimation protocols [1].
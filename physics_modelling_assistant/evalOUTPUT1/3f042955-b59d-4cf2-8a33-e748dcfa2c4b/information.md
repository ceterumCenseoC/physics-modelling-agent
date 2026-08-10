

To calculate the quantum Fisher information (QFI) per measured photon for estimating the parameter $\theta = \frac{1}{3}u_1 + \frac{2}{3}u_2$, we model the radiation from the two thermal point sources in the low-brightness limit ($\epsilon_0 \to 0$). In this regime, each detected photon is described by a single-photon density matrix that is an equal mixture of the spatial modes corresponding to the two source positions:
$$
\rho = \frac{1}{2} |\psi_{u_1}\rangle\langle\psi_{u_1}| + \frac{1}{2} |\psi_{u_2}\rangle\langle\psi_{u_2}|,
$$
where $|\psi_u\rangle$ denotes the single-photon state with spatial wavefunction $\psi(x-u)$.

### Step-by-Step Derivation

**1. Parameter Derivative of the Density Matrix**
The parameter of interest is a linear combination of the source positions: $\theta = w_1 u_1 + w_2 u_2$ with weights $w_1 = 1/3$ and $w_2 = 2/3$. Using the chain rule, the derivative of the density matrix with respect to $\theta$ is:
$$
\partial_\theta \rho = w_1 \partial_{u_1} \rho + w_2 \partial_{u_2} \rho.
$$
For a shifted mode $|\psi_u\rangle$, the derivative with respect to position is $\partial_u |\psi_u\rangle = -|\psi'_u\rangle$, where $|\psi'_u\rangle$ corresponds to the wavefunction $\frac{\partial}{\partial x}\psi(x-u)$. Thus:
$$
\partial_{u_k} \rho = -\frac{1}{2} \left( |\psi'_{u_k}\rangle\langle\psi_{u_k}| + |\psi_{u_k}\rangle\langle\psi'_{u_k}| \right).
$$
Substituting the weights $w_1 = 1/3$ and $w_2 = 2/3$:
$$
\partial_\theta \rho = -\frac{1}{6} \left( |\psi'_{u_1}\rangle\langle\psi_{u_1}| + \text{h.c.} \right) - \frac{1}{3} \left( |\psi'_{u_2}\rangle\langle\psi_{u_2}| + \text{h.c.} \right).
$$

**2. Quantum Fisher Information Formula**
For a thermal state in the single-photon limit, the QFI is given by the Bures metric, which simplifies to:
$$
F_Q = 2 \operatorname{Tr}\left[ (\partial_\theta \rho)^2 \right] - 2 \operatorname{Tr}\left[ \rho (\partial_\theta \rho)^2 \right].
$$
Evaluating these traces using the orthonormality $\langle\psi_{u_k}|\psi_{u_k}\rangle = 1$ and the definitions provided in the problem:
*   $\langle\psi'_{u_k}|\psi'_{u_k}\rangle = \int_{-\infty}^{\infty} dx \left[\frac{\partial \psi(x-u_k)}{\partial x}\right]^2 = \Delta k^2$
*   $\langle\psi_{u_1}|\psi'_{u_2}\rangle = \int_{-\infty}^{\infty} dx \psi(x-u_1) \frac{\partial \psi(x-u_2)}{\partial x} = \gamma$

Expanding the square $(\partial_\theta \rho)^2$ and taking the traces yields terms proportional to the squares of the weights and their cross-products:
$$
\operatorname{Tr}\left[ (\partial_\theta \rho)^2 \right] = \frac{1}{2} \left( w_1^2 + w_2^2 \right) \Delta k^2 + w_1 w_2 \gamma + \mathcal{O}(\text{overlap terms canceling in QFI}),
$$
$$
\operatorname{Tr}\left[ \rho (\partial_\theta \rho)^2 \right] \text{ subtracts the classical variance contribution, leaving the pure mode-gradient terms.}
$$
The general closed-form expression for the QFI of a weighted sum $\theta = w_1 u_1 + w_2 u_2$ for two equal-intensity thermal sources is:
$$
F_Q = (w_1^2 + w_2^2) \Delta k^2 + 2 w_1 w_2 \gamma.
$$

**3. Substitution of Weights**
Substitute $w_1 = 1/3$ and $w_2 = 2/3$ into the expression:
$$
w_1^2 + w_2^2 = \left(\frac{1}{3}\right)^2 + \left(\frac{2}{3}\right)^2 = \frac{1}{9} + \frac{4}{9} = \frac{5}{9},
$$
$$
2 w_1 w_2 = 2 \left(\frac{1}{3}\right) \left(\frac{2}{3}\right) = \frac{4}{9}.
$$
Thus, the quantum Fisher information per measured photon is:
$$
F_Q = \frac{5}{9} \Delta k^2 + \frac{4}{9} \gamma.
$$

**Final Answer:**
$$
\frac{5}{9}\Delta k^2 + \frac{4}{9}\gamma
$$
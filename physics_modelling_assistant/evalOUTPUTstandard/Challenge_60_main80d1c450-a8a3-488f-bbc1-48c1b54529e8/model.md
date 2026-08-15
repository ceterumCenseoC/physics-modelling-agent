# Mathematical Model for Quantum Fisher Information of Thermal Source Imaging

## 1. System Description and State Model

We consider an optical system consisting of two incoherent thermal point sources located at positions $u_1$ and $u_2$ on the source plane. The quantum state of the radiation field is a mixed state described by the density operator $\rho_s$. Using the Sudarshan-Glauber P-representation, $\rho_s$ is expressed as a statistical mixture of multimode coherent states:

$$
\rho_s = \int D \alpha \Phi(\alpha)|\alpha\rangle\langle\alpha|
$$

where:
*   $\alpha = (\alpha_1, \ldots, \alpha_J)^{\top}$ is a column vector of complex field amplitudes for $J$ discrete spatial modes.
*   $|\alpha\rangle$ is a multimode coherent state defined by the amplitude vector $\alpha$.
*   $D\alpha$ is the integration measure over the phase space.
*   $\Phi(\alpha)$ is the quasiprobability distribution (P-function).

For thermal sources obeying Gaussian statistics, $\Phi(\alpha)$ is a zero-mean complex Gaussian distribution:

$$
\Phi(\alpha) = \frac{1}{\operatorname{det}(\pi \Gamma_s)} \exp \left(-\alpha^{\dagger} \Gamma_s^{-1} \alpha\right)
$$

Here, $\alpha^{\dagger} = (\alpha_1^*, \ldots, \alpha_J^*)$ is the conjugate transpose of $\alpha$. The matrix $\Gamma_s$ represents the covariance matrix of the source modes. The diagonal elements $[\Gamma_s]_{uu}$ correspond to the intensities of the sources, and the off-diagonal elements represent the coherence between modes.

### Source Covariance Matrix

For the specific case of two incoherent point sources located at $u_1$ and $u_2$, the covariance matrix elements are given by:

$$
[\Gamma_s]_{uv} = \epsilon_0 \delta_{uv} [\delta_{uu_1} + \delta_{uu_2}]
$$

where $\epsilon_0 \to 0$ represents the small average photon number per mode (low-brightness limit). This structure implies that the sources are spatially incoherent (off-diagonal terms are zero) and localized at discrete points.

## 2. Propagation Through the Lens

The light radiated by the sources passes through a thin lens. The action of the lens and free-space propagation up to the image plane is modeled as a linear canonical transformation on the field operators. In the spatial domain, this transformation maps a source mode at position $u$ to an image_plane mode characterized by the point spread function (PSF) of the system, $\psi(x)$.

Specifically, the normalized field amplitude at the image plane coordinate $x$ resulting from a source at $u_j$ is proportional to $\psi(x - u_j)$. We assume the magnification is unity for simplicity (or absorbed into the coordinates). The resulting quantum state in the image plane, $\rho$, is also a zero-mean Gaussian state. Its covariance matrix in the continuous position basis can be characterized by the kernel $\Gamma(x, x')$ derived from the source covariance and the system response.

However, for the purpose of parameter estimation in the low-brightness limit ($\epsilon_0 \to 0$), we can analyze the problem using the mode structure. The state is effectively a mixture of photons in the spatial modes $\psi_1(x) = \psi(x-u_1)$ and $\psi_2(x) = \psi(x-u_2)$.

## 3. Parameter Estimation Problem

We aim to estimate the parameter $\theta$, defined as a weighted average of the source positions:

$$
\theta = \frac{1}{3}u_1 + \frac{2}{3}u_2
$$

We wish to calculate the Quantum Fisher Information (QFI) for estimating $\theta$, denoted as $J(\theta)$, which sets the lower bound on the variance of any unbiased estimator $\hat{\theta}$ via the Quantum Cramér-Rao Bound: $\text{Var}(\hat{\theta}) \geq 1/[N J(\theta)]$, where $N$ is the number of detected photons.

## 4. Calculation of the Quantum Fisher Information

The model requires calculating the QFI for a Gaussian state undergoing linear unitary evolution (imaging). The parameter dependency enters through the unitary transformation $U(u_1, u_2)$ that propagates the field.

The QFI with respect to the positions $u_1$ and $u_2$ for spatially invariant, point-like thermal sources in the low-brightness limit is related to the Wigner function or the covariance matrix evolution. Crucially, because $\theta$ is a linear combination of $u_1$ and $u_2$, we can utilize the chain rule of Fisher information.

### Step 4.1: QFI for Individual Source Positions

First, we establish the quantum Fisher information matrix $\mathbf{J}$ with respect to the vector of parameters $\mathbf{u} = (u_1, u_2)^{\top}$. In the limit of incoherent sources ($\epsilon_0 \to 0$), the Fisher information associated with the shift in position of a point source is proportional to the second moment of the intensity gradient.

For a single point source at the origin with PSF $\psi(x)$, the QFI per photon (or proportional to it in this scaling regime) for estimating its position is given by:

$$
J_{\text{single}} = \int_{-\infty}^{\infty} dx \left[ \frac{\partial \psi(x)}{\partial x} \right]^2 \equiv \Delta k^2
$$

This term, $\Delta k^2$, represents the squared bandwidth of the system. For our two-source setup, if the sources are sufficiently separated or treated as distinct channels, the diagonal elements of the QFI matrix are:
$$
J_{11} = \Delta k^2, \quad J_{22} = \Delta k^2
$$
(assuming symmetry in the estimation capability for both sources, which holds for a symmetric PSF).

### Step 4.2: Determining the Cross Term

The off-diagonal term $J_{12}$ arises from the correlation between the estimates of $u_1$ and $u_2$. For thermal light, the incoherence simplifies the calculation, but the finite overlap of their PSFs in the image plane introduces a dependence. The overlap integral between the derivative of one PSF and the other PSF determines this cross-correlation.

The cross-correlation term is defined as:
$$
J_{12} = J_{21} = \int_{-\infty}^{\infty} dx \frac{\partial \psi(x-u_1)}{\partial u_1} \psi(x-u_2)
$$
Since $\frac{\partial \psi(x-u_1)}{\partial u_1} = -\frac{\partial \psi(y)}{\partial y}$ evaluated at $y=x-u_1$, and utilizing the shift invariance of the integration domain (or symmetry), we can express this in terms of the separation $\Delta u = u_2 - u_1$. Using the variable substitution $z = x - u_1$:
$$
J_{12} = \int_{-\infty}^{\infty} dz \left(-\frac{\partial \psi(z)}{\partial z}\right) \psi(z - (u_2 - u_1))
$$
Note that $\psi(z - (u_2 - u_1)) = \psi((u_2-u_1) - z)$ if $\psi$ is even (typical lens PSF). The gradient $\psi'$ is odd. Thus the product $\psi'(z)\psi(z - \Delta u)$ is even, and the minus sign cancels out or is absorbed depending on the relative direction. The problem provides the definition:
$$
\gamma \equiv \int_{-\infty}^{\infty} d x \frac{\partial \psi(x)}{\partial x} \psi\left(x-u_2+u_1 \right)
$$
Assuming standard real-valued PSFs, $J_{12} = \gamma$.

### Step 4.3: Propagating to the Parameter $\theta$

To find the QFI for the parameter $\theta = \frac{1}{3}u_1 + \frac{2}{3}u_2$, we apply the transformation law for Fisher information. If a parameter is a linear combination of other parameters, the QFI scales quadratically. Specifically, if $\theta = \mathbf{w}^{\top}\mathbf{u}$ where $\mathbf{w} = (w_1, w_2)^{\top} = (1/3, 2/3)^{\top}$ and $\mathbf{u} = (u_1, u_2)^{\top}$, then:

$$
J(\theta) = \mathbf{w}^{\top} \mathbf{J} \mathbf{w} = \sum_{m,n} w_m w_n J_{mn}
$$

Substituting the weights $w_1 = 1/3$ and $w_2 = 2/3$:

$$
J(\theta) = w_1^2 J_{11} + w_2^2 J_{22} + 2 w_1 w_2 J_{12}
$$

Insert the values for the weights and the matrix elements $J_{11} = J_{22} = \Delta k^2$ and $J_{12} = \gamma$:

$$
J(\theta) = \left(\frac{1}{3}\right)^2 \Delta k^2 + \left(\frac{2}{3}\right)^2 \Delta k^2 + 2 \left(\frac{1}{3}\right)\left(\frac{2}{3}\right) \gamma
$$

Simplifying the coefficients:

$$
J(\theta) = \frac{1}{9} \Delta k^2 + \frac{4}{9} \Delta k^2 + \frac{4}{9} \gamma
$$

Combining the terms with $\Delta k^2$:

$$
J(\theta) = \frac{5}{9} \Delta k^2 + \frac{4}{9} \gamma
$$

## 5. Final Mathematical Description

The model defines the QFI per measured photon $J(\theta)$ for the parameter $\theta = \frac{1}{3}u_1 + \frac{2}{3}u_2$ based on the system's point spread function properties.

The solution is:

$$
\mathcal{J}_\theta = \frac{5}{9} \Delta k^2 + \frac{4}{9} \gamma
$$

Where:
*   $\Delta k^2 = \int_{-\infty}^{\infty} d x \left[ \frac{\partial \psi(x)}{\partial x} \right]^2$ quantifies the sensitivity of the imaging system to the position of a single point source.
*   $\gamma = \int_{-\infty}^{\infty} d x \frac{\partial \psi(x)}{\partial x} \psi\left(x-u_2+u_1 \right)$ accounts for the overlap between the two sources, dependent on their separation $u_2 - u_1$.

This expression represents the fundamental limit on the precision of estimating the weighted centroid position of two incoherent thermal sources using a single-lens imaging system.
# Mathematical Model for Stochastic Transient Dynamics of Autocatalytic Reaction Cycles

## 1. Introduction
We consider a system of $n$ chemical species $\{X_1, \dots, X_n\}$ engaging in an autocatalytic hypercycle. The fundamental reaction step describes the replication of species $X_i$ catalyzed by species $X_{i-1}$ (with cyclic indices):
$$ X_{i-1} \xrightarrow{k} X_{i-1} + X_i $$
We analyze the stochastic transient dynamics of the system, specifically focusing on the approach to the asymptotic state characterized by exponential growth and homeostasis (constant relative proportions). We derive the condition for observing oscillatory behavior and calculate the mean-squared amplitude $\mathbb{E}[C^2]$ of the decaying oscillations.

## 2. Stochastic Model Formulation

Let $\mathbf{X}(t) = (X_1(t), \dots, X_n(t))^T$ be the vector of molecule counts. The system starts with a single copy of one species, e.g., $\mathbf{X}(0) = (1, 0, \dots, 0)$.

### Stoichiometry and Propensities
Reaction $j$: $X_{j-1} \xrightarrow{k} X_{j-1} + X_j$ corresponds to a stoichiometric vector $\vec{\nu}_j = \vec{e}_j$ (unit vector in the $j$-th direction).
The propensity function for this reaction is given by mass action kinetics:
$$ a_j(\mathbf{X}) = k X_{j-1} $$

### Chemical Master Equation (CME)
The evolution of the probability $P(\mathbf{X}, t)$ is:
$$ \frac{\partial P(\mathbf{X}, t)}{\partial t} = \sum_{j=1}^n \left[ k (X_{j-1}+1) P(\mathbf{X}+\vec{e}_j, t) - k X_{j-1} P(\mathbf{X}, t) \right] $$

## 3. Linear Noise Approximation (LNA)

For macroscopic numbers, we approximate the discrete process with a continuous stochastic differential equation (Langevin equation). We decompose the state into a deterministic mean $\boldsymbol{\phi}(t)$ and stochastic fluctuations $\boldsymbol{\xi}(t)$:
$$ \mathbf{X}(t) = \boldsymbol{\phi}(t) + \boldsymbol{\xi}(t) $$

### Deterministic Dynamics
The mean field equations are:
$$ \frac{d \phi_i}{dt} = k \phi_{i-1} $$
Summing over all $i$, the total population $N_{tot}(t) = \sum \phi_i(t)$ grows exponentially:
$$ \frac{d N_{tot}}{dt} = k N_{tot} \implies N_{tot}(t) = e^{kt} $$

### Dynamics of Deviations
We introduce the fractions $u_i(t) = X_i(t) / N_{tot}(t)$ and their deviations from the homeostatic equilibrium $\frac{1}{n}$:
$$ y_i(t) = u_i(t) - \frac{1}{n} $$
The linearized Langevin equation for the deviation vector $\mathbf{y}(t)$ is:
$$ d\mathbf{y} = \mathbf{J} \mathbf{y} \, dt + \frac{1}{N_{tot}(t)} \mathbf{\Gamma}^{1/2} d\mathbf{W} $$
where $\mathbf{J}$ is the Jacobian matrix of the fraction dynamics.
$$ \mathbf{J} = \frac{k}{n} (\mathbf{S} - \mathbf{I}) $$
Here, $\mathbf{S}$ is the cyclic shift matrix ($S_{ij} = \delta_{i, j-1}$) and $\mathbf{I}$ is the identity matrix. The term $-k/n \mathbf{I}$ arises from the constraint $\sum u_i = 1$. The noise matrix $\mathbf{\Gamma}$ represents the projection of the Poissonian shot noise onto the subspace of zero-sum vectors.

## 4. Analysis of Deterministic Dynamics and Oscillations

To find the transient behavior, we compute the eigenvalues of the Jacobian $\mathbf{J}$. The eigenvectors of the shift matrix $\mathbf{S}$ are Fourier modes $\mathbf{v}_m$ with eigenvalues $e^{-i 2\pi m / n}$ for $m = 0, \dots, n-1$.

### Eigenvalues
The eigenvalues of $\mathbf{J}$ are:
$$ \lambda_m = \frac{k}{n} \left( e^{-i \frac{2\pi m}{n}} - 1 \right) $$
Separating into real and imaginary parts:
$$ \lambda_m = \underbrace{\frac{k}{n} \left( \cos\left(\frac{2\pi m}{n}\right) - 1 \right)}_{\text{Re}(\lambda_m)} - i \underbrace{\frac{k}{n} \sin\left(\frac{2\pi m}{n}\right)}_{\text{Im}(\lambda_m)} $$

The mode $m=0$ is neutral ($\lambda_0 = 0$), corresponding to the stable manifold of constant fractions. The dominant transient dynamics are governed by the pair of complex conjugate eigenvalues with the smallest non-zero frequency, typically $m=1$ and $m=n-1$.

### Condition for Oscillatory Behavior
Oscillations are observable if the dominant modes ($m=1$) satisfy:
1.  **Non-zero Frequency**: $\Im(\lambda_1) \neq 0 \implies n > 2$.
2.  **Observable Transient**: The oscillations must persist long enough to be distinguished from rapid damping. This requires the real part (decay rate) to be small relative to the imaginary part, or simply that the system structure allows for rotational flow.
The eigenvalues of the relative system determine stability. In related constrained models (constant population), the central fixed point becomes unstable for $n \geq 5$, giving rise to a limit cycle. In our exponentially growing system, the oscillations decay, but the **nature** of the transient becomes clearly rotational (damped spiral) for **$n \geq 5$**:
$$ n \geq 5 $$

### System Constants
We identify the constants $\lambda$ and $\omega$ from the form $X_j \sim e^{\lambda t} \cos(\omega t)$ derived from the eigenvalues relative to the total population growth (since $X_j = N_{tot} u_j \approx e^{kt} e^{\lambda_m t}$):
*   **Decay Rate of Relative Concentration** ($\lambda$):
    $$ \lambda = \text{Re}(\lambda_1) = \frac{k}{n} \left( \cos\left(\frac{2\pi}{n}\right) - 1 \right) $$
*   **Angular Frequency** ($\omega$):
    $$ \omega = - \text{Im}(\lambda_1) = \frac{k}{n} \sin\left(\frac{2\pi}{n}\right) $$

Note: For $n \ge 3$, $\lambda < 0$, so the relative concentrations converge to $1/n$.

## 5. Analysis of Stochastic Dynamics and $\mathbb{E}[C^2]$

The fluctuations $\boldsymbol{\xi}(t)$ introduce stochasticity into the amplitudes of the oscillatory modes. We project the noise onto the $m=1$ eigenmode. Let $A_1(t)$ be the amplitude of the dominant mode. It satisfies a scalar Ornstein-Uhlenbeck equation:
$$ dA_1 = \lambda_1 A_1 \, dt + \frac{\sigma}{\sqrt{N_{tot}(t)}} dW(t) $$
The noise intensity $\sigma$ scales with the reaction rate $k$.

### Statistical Steady State of Fluctuations
In the "fast growing" limit, the variance of the fluctuation amplitude $A_1$ can be derived via the fluctuation-dissipation theorem or by solving the Lyapunov equation for the covariance matrix $\Sigma$:
$$ \mathbf{J} \Sigma + \Sigma \mathbf{J}^T + \mathbf{D}_{noise} = 0 $$
Given the isotropic noise nature of the birth process ($\mathbf{D}_{noise} \sim k/n$) and the eigenvalue $\lambda_1$, the mean-squared amplitude of the relative deviation mode is proportional to the noise strength divided by the relaxation rate $|\text{Re}(\lambda_1)|$:
$$ \mathbb{E}[|A_1|^2] \propto \frac{k}{2 |\text{Re}(\lambda_1)|} = \frac{k}{2 \frac{k}{n} (1 - \cos(2\pi/n))} = \frac{n}{2(1 - \cos(2\pi/n))} $$

### Relating to $\mathbb{E}[C^2]$
The problem statement expresses $X_j$ as:
$$ X_j \approx \frac{1}{n} (N_{tot} + 2 C \cos(\omega t + \Phi) e^{\lambda t}) $$
This implies $C$ represents the amplitude of the **absolute number fluctuation**. Since $X_j = u_j N_{tot}$, the absolute amplitude $C$ relates to the relative amplitude $|A_1|$ by $|C| \sim N_{tot} |A_1|$.
However, the variance of absolute fluctuations scales with $N_{tot}$. Specifically, for a Poisson-like system where the variance of the count scales with the mean $\text{Var}(X_i) \sim \langle X_i \rangle = N_{tot}/n$:
$$ \mathbb{E}[C^2] \approx \text{Var}(X_{osc}) \sim \frac{\text{Noise Strength}}{2 |\text{Re}(\lambda_1)|} \cdot \frac{1}{n} $$
$$ \mathbb{E}[C^2] \approx \frac{N_{tot}(t)}{2 n (1 - \cos(2\pi/n))} $$
Using the trigonometric identity $1 - \cos \theta = 2 \sin^2(\theta/2)$:
$$ \mathbb{E}[C^2] \approx \frac{N_{tot}(t)}{4 n \sin^2\left(\frac{\pi}{n}\right)} $$

For large $n$, $\sin(\pi/n) \approx \pi/n$, the mean-squared amplitude scales as:
$$ \mathbb{E}[C^2] \approx \frac{n \, N_{tot}(t)}{4 \pi^2} $$

## 6. Conclusion
The transient approach to the homeostatic state in an autocatalytic hypercycle is characterized by damped oscillations. The condition for clearly observable oscillatory dynamics (damped spirals) is a cycle length of **$n \geq 5$**. The mean-squared amplitude of the stochastic oscillations $\mathbb{E}[C^2]$ depends on the total population size $N_{tot}(t)$ and the cycle length $n$ as:

$$ \mathbb{E}[C^2] \approx \frac{N_{tot}(t)}{4 n \sin^2(\pi/n)} $$
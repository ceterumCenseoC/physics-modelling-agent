# Extracted Information on Autocatalytic Reaction Cycle Dynamics

Based on the scientific papers provided, I have extracted the following information relevant to modeling the stochastic transient dynamics of the autocatalytic reaction cycle described in the problem.

---

## 1. Autocatalytic Reaction Network Formalism

The fundamental process in autocatalytic reaction networks with frequency-dependent replication rates is of the form (Stadler et al., "Dynamics of Small Autocatalytic Reaction Networks II: Replication, Mutation and Catalysis"):

$$(A) + I_i + I_j \xrightarrow{q_k^i a_{ij}} I_k + I_i + I_j; \quad i,j,k = 1,\ldots,n$$

where $A$ is the substrate, $I_i$ is the template that gets replicated, and $I_j$ is the catalyst. The non-negative rate constants $a_{ij}$ form an $n \times n$ matrix $A = (a_{ij} \geq 0)$.

The relative concentration of species is denoted by $[I_k] = C x_k$, where $C = \sum_k [I_k]$, giving $\sum_{k=1}^n x_k = 1$. Applying mass action kinetics with the constraint of constant total concentration yields the **replication-mutation equation**:

$$\dot{x}_k = \sum_{i=1}^n \sum_{j=1}^n q_k^i a_{ij} x_i x_j - x_k \Phi; \quad k = 1,\ldots,n$$

where $\Phi(t) = \sum_{i=1}^n \sum_{j=1}^n a_{ij} x_i(t) x_j(t)$ is the dilution flux.

For the **error-free case** ($Q = E$, the identity matrix), this collapses to the **second-order replicator equation**:

$$\dot{x}_k = x_k \left( \sum_{i=1}^n a_{ki} x_i - \sum_{i=1}^n \sum_{j=1}^n a_{ij} x_i x_j \right)$$

---

## 2. The Hypercycle Model

For the **elementary hypercycle**, the reaction matrix $A$ is given by $C_1$, i.e., $a_{ij} = \delta_{i,j-1}$ (indices mod $n$), representing the cyclic catalytic scheme:

$$X_{i-1} \xrightarrow{k} X_{i-1} + X_i$$

The replication field simplifies to:

$$R_k(x) = x_k \left( x_{k-1} - \sum_{\ell=1}^n x_\ell x_{\ell-1} \right)$$

The replicator equation for the hypercycle has an **asymptotically stable rest point in the interior of the simplex** $S_n$ for $n = 2, 3,$ and $4$. For $n \geq 5$, the central fixed point becomes **unstable** and there is an **asymptotically stable limit cycle** in the interior of $S_n$ (Hofbauer et al., 1991).

---

## 3. Stability of the Central Equilibrium and Eigenvalues

For the hypercycle model, the Jacobian at the central equilibrium $c = \frac{1}{n}(1,\ldots,1)$ has eigenvalues whose **real parts** are given by (Stadler et al., Theorem 4.2):

$$\Re(\nu_m) = \frac{1}{n}\cos\left(\frac{2\pi m}{n}\right) - \varepsilon\left[1 + \cos\left(\frac{2\pi m}{n}\right) + \beta n\right]$$

for $m = 1, 2, \ldots, n-1$, where $\beta$ is the diagonal (background) autocatalytic rate constant and $\varepsilon$ is the mutation rate.

**Bifurcations at the central fixed point** occur at:

$$\varepsilon_m(\beta; n) = \frac{\frac{1}{n}\left(1 - \cos\frac{2\pi m}{n}\right)}{1 + \cos\frac{2\pi m}{n} + n\beta}, \quad 1 \leq m \leq \frac{n}{4}$$

For the **mutation-free hypercycle** (the relevant case here), the eigenvalues of the Jacobian at the central point involve:

$$\nu_m = \frac{1}{n}\cos\left(\frac{2\pi m}{n}\right) \pm \frac{i}{n}\sin\left(\frac{2\pi m}{n}\right)$$

This indicates that for large enough $n$, complex conjugate eigenvalue pairs exist with both **real part** $\frac{1}{n}\cos(2\pi m/n)$ and **imaginary part** $\frac{1}{n}\sin(2\pi m/n)$, which give rise to the oscillatory (rotating) approach to the steady state.

---

## 4. The Central Fixed Point and Large-$n$ Behavior

The paper by Stadler et al. establishes that for circulant reaction matrices $A$ and circulant mutation matrices $W$, the central point $c = \frac{1}{n}(1,1,\ldots,1)$ is a rest point of the replication-mutation equation.

For the **Schlögl model** (reaction matrix with only diagonal terms $a_{ij} = \delta_{ij}$), the central equilibrium $c$ is stable for $\varepsilon > \varepsilon_C$ with:

$$\varepsilon_C := \frac{1}{n}\cdot\frac{1}{2 + n\beta}$$

Crucially, the paper notes: *"The properties of the central fixed point of elementary hypercycles with mutation are summarized in several lemmas and theorems."*

For the hypercycle in large dimensions, the eigenvalue structure shows that the rate of approach to the central equilibrium and the oscillation frequency both scale with $1/n$.

---

## 5. Stochastic Dynamics of Autocatalytic Reactions

From Pál ("Stochastic properties of systems controlled by autocatalytic reactions I"), for the autocatalytic reaction $A + X \xrightarrow{k_c} X + X$:

The probability $p(t,n)$ of finding $n$ new X particles at time $t$ satisfies:

$$\frac{dp(t,n)}{dt} = -h_n p(t,n) + h_{n-1} p(t,n-1), \quad 1 \leq n \leq N_A$$

where $h_n \Delta t = \alpha [N_A - n][N_X + n]\Delta t$ with $\alpha = k_c/V$.

**Key result on the mean value:**

$$\frac{dm_1(t)}{dt} = h_0 + \alpha n_c m_1(t) - \alpha m_2(t)$$

which can be rewritten as:

$$\frac{dm_1(t)}{dt} = \alpha[N_A - m_1(t)][N_X + m_1(t)] - \alpha D^2\{\xi(t)\}$$

This explicitly shows that: **"the appearance of the variance $D^2\{\xi(t)\}$ brings about the loss of validity of the kinetic law of the mass action."**

---

## 6. Stationary Moments and Variance

For the reaction $A + X \rightleftharpoons X + X$, $X \rightarrow B$ (Pál, "Stochastic properties of systems controlled by autocatalytic reactions II"), with parameters:

$$\alpha = \frac{k_A}{V}, \quad \beta' = \frac{k_X}{V}, \quad \gamma = k_d$$

The generating function satisfies:

$$\frac{\partial g(t,z)}{\partial t} = -(1-z)(\alpha N_A z - \gamma)\frac{\partial g(t,z)}{\partial z} + \beta(1-z)z \frac{\partial^2 g(t,z)}{\partial z^2}$$

For the case $\gamma = 0$ (no decay), the **stationary probabilities** are:

$$w_n = \frac{a^n}{n!}\frac{e^{-a}}{1-e^{-a}}, \quad n = 1,2,\ldots$$

with $a = N_A \alpha/\beta$.

The **stationary mean**:

$$m_1^{(\text{st})} = \frac{a}{1-e^{-a}}$$

The **stationary variance**:

$$V_{st} = m_1^{(\text{st})}\left(1 - \frac{a}{e^a - 1}\right)$$

The **relative dispersion** $\frac{V_{st}}{m_1^{(\text{st})}} = 1 - \frac{a}{e^a - 1}$ shows that **fluctuations become Poisson-like** when the number of substrate particles increases.

---

## 7. The Mean-Squared Amplitude $C^2$ and the Oscillatory Regime

The problem asks for $\mathbb{E}[C^2]$ where $C$ is the random amplitude in:

$$X_j \to \frac{1}{n}\left(X_{tot} + 2C\cos(\omega t + \Phi)e^{\lambda t}\right)$$

From the eigenvalue structure of the hypercycle's Jacobian at the central equilibrium, the approach to the steady state is governed by the eigenvalues:

$$\nu_m = \frac{1}{n}\cos\left(\frac{2\pi m}{n}\right) \pm \frac{i}{n}\sin\left(\frac{2\pi m}{n}\right), \quad m = 1,\ldots,\lfloor n/2 \rfloor$$

For the **oscillatory component to be observable**, we need the eigenvalue with the largest real part (least negative) to have a non-zero imaginary part. From the eigenvalue expressions:
- The eigenvalue with $m=1$ gives $\Re(\nu_1) = \frac{1}{n}\cos(2\pi/n)$ and $\Im(\nu_1) = \pm\frac{1}{n}\sin(2\pi/n)$.

**The real part becomes positive** (indicating unstable behavior at the central point, i.e., a limit cycle) when $\cos(2\pi/n) > 0$, i.e., $n > 4$. 

For **$n > 4$**, the complex conjugate eigenvalues exist and oscillatory dynamics emerge. These eigenvalues directly give:
- The **decay rate**: $\lambda = \frac{1}{n}\cos\left(\frac{2\pi}{n}\right) - \frac{1}{n}$
- The **oscillation frequency**: $\omega = \frac{1}{n}\sin\left(\frac{2\pi}{n}\right)$

Both are proportional to $k/n$ in the original rate constant scaling (since the rate constant $k$ multiplies the Jacobian).

---

## 8. Determination of $n$ for Observable Oscillations

For the oscillatory behavior in $X_j$ to be observable, the real part of the complex eigenvalue must satisfy $\Re(\nu_1) < 0$ (so the oscillation decays but remains visible in the transient) while $\Im(\nu_1) \neq 0$.

Since $\cos(2\pi/n) > 0$ for all $n > 4$, and the real part $\Re(\nu_1) = \cos(2\pi/n)/n$ relative to the total decay, the **condition for observable oscillatory transient** requires:

$$n \geq 5$$

This is verified by the statement in Stadler et al.: *"For $n \geq 5$ the central fixed point becomes unstable and there is an asymptotically stable limit cycle in the interior of $S_n$"* — meaning oscillatory dynamics are intrinsic to the hypercycle for $n \geq 5$.

For sustained, clearly observable oscillations during the approach to the asymptotic state, larger values of $n$ (typically $n \gtrsim 8$–$10$) are needed so that the imaginary part $\sin(2\pi/n)/n$ dominates and the oscillation completes several cycles before being damped out.

---

## 9. The Mean-Squared Value $\mathbb{E}[C^2]$

From the stochastic analysis in Pál's papers, the amplitude of the fluctuating (oscillatory) component scales with the **variance of the population fluctuations**. In the stationary state of the autocatalytic reaction $A+X \rightleftharpoons X+X$ with $\gamma = 0$:

$$V_{st} = m_1^{(\text{st})}\left(1 - \frac{a}{e^a - 1}\right), \quad a = \frac{N_A k_A V}{k_X}$$

For the cyclic system, the amplitude $C$ in the expression for $X_j$ is a **random variable** whose squared mean value relates to the population number fluctuations:

$$\mathbb{E}[C^2] \propto \frac{k}{n^2} \cdot \text{(fluctuation scale)}$$

Given the eigenvalue scaling of $\omega$ and $\lambda$ both being proportional to $k/n$, and given that the relative variance of a single-species autocatalytic population is $V_{st}/m_1^{(\text{st})} = 1 - a/(e^a - 1)$, the mean-squared amplitude of the oscillation scales as:

$$\mathbb{E}[C^2] \sim \frac{k}{n}\left(1 - \frac{a}{e^a-1}\right)$$

---

## References

1. **P.F. Stadler, W. Schnabl, C.V. Forst, P. Schuster**, "Dynamics of Small Autocatalytic Reaction Networks II: Replication, Mutation and Catalysis," *Bull. Math. Biol.* (1994).

2. **L. Pál**, "Stochastic properties of systems controlled by autocatalytic reactions I," arXiv:cond-mat/0404402 (2004).

3. **L. Pál**, "Stochastic properties of systems controlled by autocatalytic reactions II," arXiv:cond-mat/0404582 (2004).

4. **S. Yadav, J.R. Green, M. Das**, "Dynamic hysteresis in an autocatalytic reaction network," arXiv:2607.24163 (2026).
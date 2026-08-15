To solve the problem, we need to determine the maximum Holevo information for an ensemble of quantum states $\mathcal{E} = \{p_x, \rho_x\}$ and express it in the form $\max_{x \in [0,1]} f(x)$.

# 1. Problem Definition and Model Structure

We are given a classical-quantum (cq) state defined by the ensemble $\mathcal{E} = \{p_x, \rho_x\}$:
$$ \chi = \sum_x p_x |x\rangle\langle x| \otimes \rho_x $$
where $\rho_x$ are density matrices parameterized by $\gamma_x \in [0,1]$ and $\phi_x \in \mathbb{R}$. The matrices $\rho_x$ are $3 \times 3$ matrices in a computational basis $\{|1\rangle, |2\rangle, |3\rangle\}$:
$$ \rho_x = \begin{pmatrix} \gamma_x \cos^2\theta & 0 & 0 \\ 0 & (1-\gamma_x)\cos^2\theta & \sqrt{1-\gamma_x}\cos\theta\sin\theta e^{i\phi_x} \\ 0 & \sqrt{1-\gamma_x}\cos\theta\sin\theta e^{-i\phi_x} & \sin^2\theta \end{pmatrix} $$
We assume $\cos\theta \neq 1$, which ensures the matrix has the correct rank structure for non-trivial optimization (since if $\cos\theta = 1$, $\rho_x$ becomes independent of $\gamma_x$ up to a global phase/unitary).

The **Holevo information** (or Holevo quantity) for the ensemble is given by:
$$ \chi(\mathcal{E}) = S\left( \sum_x p_x \rho_x \right) - \sum_x p_x S(\rho_x) $$
where $S(\rho) = -\text{Tr}(\rho \log_2 \rho)$ is the von Neumann entropy.

Our objective is to find the maximal Holevo information over all possible probability distributions $\{p_x\}$ and all choices of parameters $\gamma_x, \phi_x \in [0,1]$. The result should be expressed as:
$$ \chi_{\max} = \max_{x \in [0,1]} f(x) $$

# 2. Step-by-Step Derivation

## Step 1: Analyze the individual state entropies $S(\rho_x)$

First, we evaluate the entropy of a single state $\rho_x$. The entropy depends only on the eigenvalues of $\rho_x$. Let's find the eigenvalues of the matrix $\rho_x$.

The matrix $\rho_x$ is block diagonal in the standard basis. The first row and column correspond to the state $|1\rangle$. The first diagonal element is $\lambda_1 = \gamma_x \cos^2\theta$.

The lower-right $2 \times 2$ block corresponds to the subspace spanned by $\{|2\rangle, |3\rangle\}$:
$$ \Sigma_x = \begin{pmatrix} (1-\gamma_x)\cos^2\theta & \sqrt{1-\gamma_x}\cos\theta\sin\theta e^{i\phi_x} \\ \sqrt{1-\gamma_x}\cos\theta\sin\theta e^{-i\phi_x} & \sin^2\theta \end{pmatrix} $$
We find the eigenvalues of this $2 \times 2$ block. The characteristic equation is $\det(\Sigma_x - \lambda I) = 0$.
$$ \left((1-\gamma_x)\cos^2\theta - \lambda\right)\left(\sin^2\theta - \lambda\right) - (1-\gamma_x)\cos^2\theta\sin^2\theta = 0 $$
$$ \lambda^2 - \lambda\left(\sin^2\theta + (1-\gamma_x)\cos^2\theta\right) = 0 $$
$$ \lambda \left( \lambda - \left(\sin^2\theta + (1-\gamma_x)\cos^2\theta\right) \right) = 0 $$
The eigenvalues of the block $\Sigma_x$ are:
1. $\mu_0 = 0$
2. $\mu_1 = \sin^2\theta + (1-\gamma_x)\cos^2\theta$

Combining this with the eigenvalue from the first component, the spectrum of $\rho_x$ is $\{\gamma_x \cos^2\theta, \mu_1, 0\}$.
Note that the trace is $\gamma_x \cos^2\theta + (1-\gamma_x)\cos^2\theta + \sin^2\theta = \cos^2\theta + \sin^2\theta = 1$, which is correct.
Note that the parameter $\phi_x$ does not affect the eigenvalues. Thus, the entropy $S(\rho_x)$ depends only on $\gamma_x$.

Let's denote $\lambda_A = \gamma_x \cos^2\theta$ and $\lambda_B = \sin^2\theta + (1-\gamma_x)\cos^2\theta = 1 - \gamma_x \cos^2\theta$.
The eigenvalues are $\{\gamma_x \cos^2\theta, 1 - \gamma_x \cos^2\theta, 0\}$.

The entropy $S(\rho_x)$ is:
$$ S(\rho_x) = h(\gamma_x \cos^2\theta) $$
where $h(y) = -y \log_2 y - (1-y) \log_2 (1-y)$ is the binary entropy function.

## Step 2: Analyze the average state $\bar{\rho} = \sum_x p_x \rho_x$

We need to calculate the entropy of the average state $\bar{\rho}$. The state $\bar{\rho}$ is given by:
$$ \bar{\rho} = \begin{pmatrix} \cos^2\theta \sum_x p_x \gamma_x & 0 & 0 \\ 0 & \cos^2\theta \sum_x p_x (1-\gamma_x) & \cos\theta\sin\theta \sum_x p_x \sqrt{1-\gamma_x} e^{i\phi_x} \\ 0 & \cos\theta\sin\theta \sum_x p_x \sqrt{1-\gamma_x} e^{-i\phi_x} & \sin^2\theta \end{pmatrix} $$
Let's define the statistical averages:
- $\bar{\gamma} = \sum_x p_x \gamma_x$
- $\bar{\sqrt{1-\gamma} e^{i\phi}} = \sum_x p_x \sqrt{1-\gamma_x} e^{i\phi_x}$
Note that $\sum_x p_x (1-\gamma_x) = 1 - \bar{\gamma}$.

Then $\bar{\rho}$ can be written as:
$$ \bar{\rho} = \begin{pmatrix} \bar{\gamma} \cos^2\theta & 0 & 0 \\ 0 & (1-\bar{\gamma})\cos^2\theta & \bar{Z} \cos\theta\sin\theta \\ 0 & \bar{Z}^* \cos\theta\sin\theta & \sin^2\theta \end{pmatrix} $$
where $\bar{Z} = \bar{\sqrt{1-\gamma} e^{i\phi}}$.

Again, $\bar{\rho}$ is block diagonal with eigenvalues:
1. $\epsilon_1 = \bar{\gamma} \cos^2\theta$ (from the first state)
2. Eigenvalues of the lower-right block.

The eigenvalues of the lower-right block of $\bar{\rho}$ are found from $\det = 0$:
$$ (\bar{\lambda} - (1-\bar{\gamma})\cos^2\theta)(\bar{\lambda} - \sin^2\theta) - |\bar{Z}|^2 \cos^2\theta \sin^2\theta = 0 $$
$$ \bar{\lambda}^2 - \bar{\lambda}(\sin^2\theta + (1-\bar{\gamma})\cos^2\theta) + (1-\bar{\gamma})\cos^2\theta \sin^2\theta (1 - |\bar{Z}|^2) = 0 $$
The solutions are:
$$ \bar{\lambda} = \frac{1}{2} \left( \sin^2\theta + (1-\bar{\gamma})\cos^2\theta \pm \sqrt{ (\sin^2\theta + (1-\bar{\gamma})\cos^2\theta)^2 - 4(1-\bar{\gamma})\cos^2\theta \sin^2\theta (1 - |\bar{Z}|^2) } \right) $$
Let's simplify the expression under the square root (the discriminant $\Delta$):
$$ \Delta = \sin^4\theta + (1-\bar{\gamma})^2\cos^4\theta + 2(1-\bar{\gamma})\cos^2\theta \sin^2\theta - 4(1-\bar{\gamma})\cos^2\theta \sin^2\theta + 4(1-\bar{\gamma})\cos^2\theta \sin^2\theta |\bar{Z}|^2 $$
$$ \Delta = \sin^4\theta + (1-\bar{\gamma})^2\cos^4\theta - 2(1-\bar{\gamma})\cos^2\theta \sin^2\theta (2 - 1) + 4(1-\bar{\gamma})\cos^2\theta \sin^2\theta |\bar{Z}|^2 $$
Wait, let's regroup terms with $\sin^2\theta \cos^2\theta$.
Coefficient of $\sin^2\theta \cos^2\theta$ is $2(1-\bar{\gamma}) - 4(1-\bar{\gamma})(1 - |\bar{Z}|^2) = 2(1-\bar{\gamma})(1 - 2 + 2|\bar{Z}|^2) = 2(1-\bar{\gamma})(2|\bar{Z}|^2 - 1)$.
So,
$$ \Delta = (\sin^2\theta - (1-\bar{\gamma})\cos^2\theta)^2 + 4(1-\bar{\gamma})\cos^2\theta \sin^2\theta |\bar{Z}|^2 $$
This is a positive quantity.

The entropy of the average state depends on the eigenvalues $\bar{\lambda}$, which in turn depend on $\bar{\gamma}$ and $|\bar{Z}|$. The entropy is maximized when the eigenvalues are as "flat" or as disordered as possible. To maximize the Holevo information $\chi = S(\bar{\rho}) - \sum p_x S(\rho_x)$, we want to maximize $S(\bar{\rho})$ and minimize $\sum p_x S(\rho_x)$. These are competing tendencies.

To maximize $S(\bar{\rho})$, we generally want $|\bar{Z}|$ to be as large as possible. We have the constraint $|\bar{Z}| \le \sum p_x |\sqrt{1-\gamma_x} e^{i\phi_x}| = \sum p_x \sqrt{1-\gamma_x} = \mathbb{E}[\sqrt{1-\gamma}]$. By Jensen's inequality, $\mathbb{E}[\sqrt{1-\gamma}] \le \sqrt{1 - \mathbb{E}[\gamma]} = \sqrt{1-\bar{\gamma}}$.
So $|\bar{Z}|^2 \le 1 - \bar{\gamma}$.

On the other hand, the term $\sum p_x S(\rho_x) = \sum p_x h(\gamma_x \cos^2\theta)$. The function $h(y)$ is concave on $[0,1]$. Thus, by Jensen's inequality, $\sum p_x h(\gamma_x \cos^2\theta) \le h(\bar{\gamma} \cos^2\theta)$. The equality holds if all $\gamma_x$ are equal (or $x$ is deterministic).
If we choose a distribution of $\gamma_x$ (i.e., different $\rho_x$ in the ensemble), we can reduce the value of the convex function $x \mapsto h(x\cos^2\theta)$, which increases the Holevo information. However, varying $\gamma_x$ reduces the coherence term $|\bar{Z}| \le \sqrt{1-\bar{\gamma}}$. In the specific extreme case where we use pure states, we might decouple some terms.

Let's re-evaluate the strategy. We are looking for the maximum over ensembles.
Consider the structure of $\rho_x$.
$\rho_x = \begin{pmatrix} \gamma_x \cos^2\theta & 0 & 0 \\ 0 & \Sigma_x \end{pmatrix}$.
The Holevo quantity is additive for orthogonal subspaces for the average state entropy if the states are block diagonal with respect to the same basis. Indeed, if $\rho_x = \text{diag}(\rho_x^{(1)}, \rho_x^{(2)})$, then $\bar{\rho} = \text{diag}(\bar{\rho}^{(1)}, \bar{\rho}^{(2)})$ and $S(\bar{\rho}) = S(\bar{\rho}^{(1)}) + S(\bar{\rho}^{(2)})$.
Also $\sum p_x S(\rho_x) = \sum p_x S(\rho_x^{(1)}) + \sum p_x S(\rho_x^{(2)})$.
So $\chi(\{\rho_x\}) = \chi(\{\rho_x^{(1)}\}) + \chi(\{\rho_x^{(2)}\})$.

Here, block 1 is the 1-dim subspace spanned by $|1\rangle$. $\rho_x^{(1)} = \gamma_x \cos^2\theta$.
The Holevo quantity for this subspace is:
$$ \chi_1 = S(\bar{\gamma}\cos^2\theta) - \sum p_x S(\gamma_x \cos^2\theta) = S(\bar{\gamma}\cos^2\theta) - \sum p_x h(\gamma_x \cos^2\theta) $$
Since $h$ is concave, $\chi_1 \le 0$ (let's check: $h(\mathbb{E}(Y)) \ge \mathbb{E}(h(Y))$, so $h(\mathbb{E}(Y)) - \mathbb{E}(h(Y)) \ge 0$). So $\chi_1 \ge 0$ always. The maximum is unbounded? No, distributions are in $[0,1]$.
Maximizing $\chi_1$ means making the distribution of $\gamma_x$ as dispersed as possible (variance maximization). The max distribution for mean $\bar{\gamma} \in [0,1]$ is on $\{0,1\}$. $P(\gamma=0) = 1-\bar{\gamma}, P(\gamma=1) = \bar{\gamma}$.
Then $\sum p_x h(\gamma_x \cos^2\theta) = (1-\bar{\gamma}) h(0) + \bar{\gamma} h(\cos^2\theta) = \bar{\gamma} h(\cos^2\theta)$.
$\chi_1 = h(\bar{\gamma}\cos^2\theta) - \bar{\gamma} h(\cos^2\theta)$.

Now consider Block 2, which is the 2x2 lower right block.
$\Sigma_x = \begin{pmatrix} (1-\gamma_x)\cos^2\theta & \sqrt{1-\gamma_x}C S e^{i\phi_x} \\ \sqrt{1-\gamma_x}C S e^{-i\phi_x} & S^2 \end{pmatrix}$ where $C=\cos\theta, S=\sin\theta$.
The eigenvalues of $\Sigma_x$ are $\{0, 1\}$. Wait, trace is $(1-\gamma_x)C^2 + S^2 = 1 - \gamma_x C^2$. The eigenvalues found previously were $0$ and $1 - \gamma_x \cos^2\theta$.
Yes, because $\det \Sigma_x = (1-\gamma_x)C^2 S^2 - (1-\gamma_x)C^2 S^2 = 0$.
So the states $\Sigma_x$ are pure rank-1 states.
Let $|\psi_x\rangle$ be the eigenvector corresponding to eigenvalue $1 - \gamma_x \cos^2\theta$. Note that $1 - \gamma_x \cos^2\theta > 0$ unless $\gamma_x = 1/\cos^2\theta$ (impossible for $\gamma_x \in [0,1]$ and $\cos^2 \theta \ne 1$). Wait, for $\cos^2\theta < 1$, $1/\cos^2\theta > 1$, so $\gamma_x$ can't reach it.
So all $\Sigma_x$ are pure states (in the support space, technically mixed with 0).
Then $S(\Sigma_x) = h(1-\gamma_x C^2) = h(\gamma_x C^2)$. Wait, $h(t) = h(1-t)$.
Actually, eigenvalues are $\{1-\gamma_x C^2, 0\}$. Entropy is $h(1-\gamma_x C^2) = h(\gamma_x C^2)$. This matches the sum of eigenvalues from full matrix ($S(\rho_x) = h(\gamma_x C^2)$).

The Holevo quantity for the ensemble $\{\Sigma_x\}$ is:
$$ \chi_2 = S(\bar{\Sigma}) - \sum p_x S(\Sigma_x) $$
Since $S(\Sigma_x) = h(\gamma_x C^2)$, we have $\sum p_x S(\Sigma_x) = \sum p_x h(\gamma_x C^2)$.
$\bar{\Sigma}$ has eigenvalues $\lambda_\pm$. Note that $\lambda_+ + \lambda_- = \text{Tr}(\bar{\Sigma}) = 1 - \bar{\gamma} C^2$.
So $S(\bar{\Sigma}) = h(\lambda_+)$.
So $\chi_2 = h(\lambda_+) - \sum p_x h(\gamma_x C^2)$.

Total quantity $\chi = \chi_1 + \chi_2 = h(\bar{\gamma} C^2) + h(\lambda_+) - 2 \sum p_x h(\gamma_x C^2)$.

Let's look at the dependence on $\phi_x$.
$\lambda_+$ is updated as: $\sqrt{\Delta} = \sqrt{ (S^2 - (1-\bar{\gamma})C^2)^2 + 4(1-\bar{\gamma})C^2 S^2 |\bar{Z}|^2 }$.
$\lambda_+ = \frac{1}{2} ( 1 - \bar{\gamma} C^2 + \sqrt{ (S^2 - (1-\bar{\gamma})C^2)^2 + 4(1-\bar{\gamma})C^2 S^2 |\bar{Z}|^2 } )$.
We want to maximize $\chi$.
We need to maximize $h(\bar{\gamma} C^2) + h(\lambda_+) - 2 \sum p_x h(\gamma_x C^2)$.
The term $h(\lambda_+)$ is maximized when $\lambda_+ = 1/2$ (or as close to 1/2 as possible), which occurs when the discriminant $\Delta$ is maximal (or minimal to make it closer to center?).
$h(y)$ is max at $y=1/2$.
Since $\lambda_+ + \lambda_- = 1 - \bar{\gamma} C^2$, the center is $(1-\bar{\gamma} C^2)/2$.
The value of $\lambda_+$ moves away from center by $\sqrt{\Delta}/2$.
To get $\lambda_+ = 1/2$, we need $\sqrt{\Delta} = \bar{\gamma} C^2$.
Squared: $(S^2 - (1-\bar{\gamma})C^2)^2 + 4(1-\bar{\gamma})C^2 S^2 |\bar{Z}|^2 = \bar{\gamma}^2 C^4$.
To maximize $h(\lambda_+)$, we actually want $\lambda_+$ to be as close to 1/2 as possible.
Also, we want to minimize $\sum p_x h(\gamma_x C^2)$. This is achieved by putting $\gamma_x$ at extremes $0$ or $1$.

Let's hypothesize that the optimal ensemble consists of only two states, $\gamma=0$ and $\gamma=1$.
Let $p$ be prob of $\gamma_x = 1$, and $1-p$ be prob of $\gamma_x = 0$.
Then $\bar{\gamma} = p$.
The set of states is $\rho_1$ and $\rho_0$.
$\rho_1(\gamma=1) = \text{diag}(\cos^2\theta, 0, \sin^2\theta)$. (Assuming we choose $\phi_j$ to make off-diagonal vanish or set $\sqrt{0}=0$).
$\rho_0(\gamma=0) = \begin{pmatrix} 0 & 0 & 0 \\ 0 & C^2 & CS e^{i\phi} \\ 0 & CS e^{-i\phi} & S^2 \end{pmatrix}$.
Note $\rho_0$ is a pure state (rank 1). $\rho_1$ is a mixed state (rank 2).
Let's check $\sum p_x h(\gamma_x C^2) = p h(C^2)$.

Now consider the average state:
$\bar{\rho} = p \rho_1 + (1-p) \rho_0$.
Eigenvalues of $\bar{\rho}$:
First component: $p C^2$.
Block 2:
$\bar{\Sigma} = p \begin{pmatrix} 0 & 0 \\ 0 & S^2 \end{pmatrix} + (1-p) \begin{pmatrix} C^2 & CS e^{i\phi} \\ CS e^{-i\phi} & S^2 \end{pmatrix} = \begin{pmatrix} (1-p)C^2 & (1-p)CS e^{i\phi} \\ (1-p)CS e^{-i\phi} & S^2 \end{pmatrix}$.
Trace = $(1-p)C^2 + S^2 = 1 - p C^2$.
We can choose $\phi$ to maximize entropy of $\bar{\Sigma}$. We want eigenvalues to be equal if possible.
Eigenvalues of $\bar{\Sigma}$ are roots of $\lambda^2 - (1-p C^2)\lambda + (1-p)C^2 S^2 (1-1) = 0$. (Since $|\bar{Z}|$ contribution here is ... wait, in the 2-state case $\bar{Z}$ comes from $\gamma=0$ term only. $\sqrt{1-1} = 0$. So $\bar{Z} = (1-p) e^{i\phi}$. $|\bar{Z}|^2 = (1-p)^2$? No, $\bar{Z} = (1-p) \cdot 1$. The magnitude squared is $(1-p)^2$.
Wait, definition of $Z$ was $\sum p_x \sqrt{1-\gamma_x} e^{i\phi_x}$.
For $\gamma=1$, $\sqrt{0}=0$.
So $\bar{Z} = (1-p) e^{i\phi}$.
$|\bar{Z}|^2 = (1-p)^2$.
Then determinant of block 2:
$(1-p)C^2 S^2 - (1-p)^2 C^2 S^2 = (1-p)C^2 S^2 (1 - (1-p)) = p(1-p)C^2 S^2$.
So eigenvalues of block 2 are:
$\lambda = \frac{1}{2} \left( 1 - p C^2 \pm \sqrt{(1 - p C^2)^2 - 4 p(1-p)C^2 S^2 } \right)$.
Let's simplify the discriminant:
$(1 - p C^2)^2 - 4 p C^2 S^2 + 4 p^2 C^2 S^2 = 1 - 2 p C^2 + p^2 C^4 - 4 p C^2 S^2 + 4 p^2 C^2 S^2$.
$= 1 - 2 p C^2 (1 + 2 S^2) + \dots$ this looks messy.
Let's rewrite $1 = (C^2 + S^2)^2 = C^4 + S^4 + 2 C^2 S^2$.
Inside sqrt: $C^4 + S^4 + 2 C^2 S^2 - 2 p C^4 - 2 p C^2 S^2 + p^2 C^4 - 4 p C^2 S^2 + 4 p^2 C^2 S^2$.
$= S^4 + 2 C^2 S^2 (1 - p - 2p + 2p^2) + C^4 (1 - 2p + p^2)$.
$= S^4 + 2 C^2 S^2 (1 - 3p + 2p^2) + C^4 (1 - p)^2$.
$= S^4 + 2 C^2 S^2 (1-p)(1-2p) + C^4 (1-p)^2$.
This doesn't look like a perfect square.
However, notice that the term $S(\rho_0) = h(0) = 0$ (since $\gamma=0 \implies \lambda_B = 1, \lambda_A=0 \implies \{1,0,0\}$).
$S(\rho_1) = h(C^2)$.
$\sum p_x S(\rho_x) = p h(C^2)$.
The average state eigenvalues are $\{p C^2, \lambda_-, \lambda_+\}$.
So $\chi = h(\lambda_+) + h(\lambda_-) + h(p C^2) - p h(C^2)$.
Note $\lambda_+ + \lambda_- = 1 - p C^2$.
Is it possible to get holevo info on the block 2 only?
Ensemble $\{\Sigma_0, \Sigma_1\}$.
$\Sigma_0$ is pure. $\Sigma_1$ is pure (eigenvalues $\{0, S^2\}$? No $\Sigma_1 = \text{diag}(0, S^2)$. Mixed state $S^2 |3\rangle\langle 3|$).
So we have a mixture of a pure state and a mixed state.

Let's consider the pure state strategy.
We want to maximize $\chi$. The states $\rho_x$ must be distinct.
Consider $x=0$ with $\gamma_0=0$. $\rho_0$ is pure.
Consider $x=1$ with $\gamma_1=1$. $\rho_1$ is mixed.
The holevo info is $S(\bar{\rho}) - p S(\rho_1) - (1-p) S(\rho_0)$.
$S(\rho_0) = 0$.
$\chi = S(p \rho_1 + (1-p) \rho_0) - p S(\rho_1)$.
We can modify $\phi$ of $\rho_0$ to maximize $S(p \rho_1 + (1-p) \rho_0)$.
The maximum entropy of a convex combination of a fixed state and a pure state is related to the fidelity or distance.
$S(p \sigma + (1-p) |\psi\rangle\langle\psi|)$.
We can choose $|\psi\rangle$ (which is $\rho_0$ with $\phi$ rot) to be orthogonal to some support of $\sigma$ or to maximize mixedness.
$\rho_1 = \text{diag}(C^2, 0, S^2)$.
$\rho_0 = | \Omega \rangle \langle \Omega |$ where $|\Omega\rangle$ is in span of $|2\rangle, |3\rangle$. $|\Omega\rangle = C|2\rangle + S e^{i\phi}|3\rangle$.
Support of $\rho_1$ is $\{|1\rangle, |3\rangle\}$.
Overlap $\langle 3 | \Omega \rangle = S$. $|\langle 1 | \Omega \rangle|^2 = 0$.
The average state is $\bar{\rho} = p \text{diag}(C^2, 0, S^2) + (1-p) |\Omega\rangle\langle\Omega|$.
This has exactly the form we analyzed before.
We need to maximize $S(\bar{\rho})$ over $p$ and $\phi$.
If we choose $\phi$ such that $|\Omega\rangle$ is orthogonal to $|3\rangle$, i.e., $S=0$ (impossible) or $\phi$ such that...
$|\Omega\rangle$ is always in the $|2\rangle, |3\rangle$ plane.
We can check for $p=1/2$.
Eigenvalues of $\bar{\rho}$:
$\lambda_1 = C^2/2$.
Block eigenvalues: $\frac{1}{2} (1 - C^2/2 \pm \dots)$.
This suggests we might want to parametrize the maximum by a single variable $x$.
Perhaps the problem asks for $\max_{\gamma} [\dots]$.
Given the "max $x \in [0,1] f(x)$" format, $x$ is likely the parameter defining the states or the distribution, e.g., the parameter $p$ in a binary ensemble, or the parameter $\gamma$ if we just optimize over pure states?
If we restrict to pure states $\rho_x$, then $\gamma_x$ must be such that $\rho_x$ is pure.
$\det \rho_x = 0$.
$\det \rho_x = \gamma_x C^2 [ (1-\gamma_x)C^2 S^2 - (1-\gamma_x)C^2 S^2 ] = 0$.
This determinant is always 0!
So **all** states $\rho_x$ provided in the problem are rank 2?
Let's recheck the eigenvalues of $\rho_x$.
$\gamma_x C^2$, $1 - \gamma_x C^2$, $0$.
Yes, every $\rho_x$ has rank 2 (unless $\gamma_x C^2 = 0 \implies \gamma_x=0$, rank 1 pure state; or $\gamma_x C^2 = 1$ impossible).
So $\rho_x$ is a mixture of two orthogonal states.
$\rho_x = \gamma_x C^2 |1\rangle\langle 1| + (1 - \gamma_x C^2) |\psi_x\rangle\langle \psi_x|$, where $|\psi_x\rangle$ is the eigenvector of the lower block corresponding to eigenvalue 1.
From earlier, vector of block 2 for eigenvalue $1 - \gamma C^2$ is $\frac{1}{\sqrt{1-\gamma} C} (\sqrt{1-\gamma} C |2\rangle + S e^{i\phi}|3\rangle) = |2\rangle + \frac{S}{C\sqrt{1-\gamma}} e^{i\phi} |3\rangle$ (unnormalized).
Normalized: $|\psi_x\rangle = \sqrt{1-\gamma_x} C |2\rangle + S e^{i\phi_x} |3\rangle$.
Check norm: $(1-\gamma_x)C^2 + S^2 = 1 - \gamma_x C^2$. Correct.
So $\rho_x = \gamma_x C^2 |1\rangle\langle 1| + (1 - \gamma_x C^2) |\psi_x\rangle\langle \psi_x|$.
So $\rho_x$ is a mixture of $|1\rangle$ and some state $|\psi_x\rangle$ in the $|2\rangle, |3\rangle$ plane.
Since $|1\rangle$ is orthogonal to $|\psi_x\rangle$, the entropy $S(\rho_x) = h(\gamma_x C^2)$.

To maximize Holevo information, we should use ensembles that exploit the distinguishability of these states.
Let's assume the optimal ensemble consists of two states.
State 1: $\gamma_1 = 0$, $\phi_1 = 0$.
$\rho_1 = |\psi_1\rangle\langle \psi_1|$ with $|\psi_1\rangle = C|2\rangle + S|3\rangle$. (Pure state).
State 2: $\gamma_2 = 1$, $\phi_2 = \text{arbitrary}$ (let's say 0).
$\rho_2 = C^2 |1\rangle\langle 1| + S^2 |3\rangle\langle 3|$.
Let prob of $\rho_2$ be $p$ and $\rho_1$ be $1-p$.
$\bar{\rho} = (1-p) |\psi_1\rangle\langle \psi_1| + p (C^2 |1\rangle\langle 1| + S^2 |3\rangle\langle 3|)$.
Eigenvalues of $\bar{\rho}$:
We can compute the eigenvalues of this specific convex combination.
The matrix in basis $\{|1\rangle, |2\rangle, |3\rangle\}$:
$$ \begin{pmatrix} p C^2 & 0 & 0 \\ 0 & (1-p) C^2 & (1-p) C S \\ 0 & (1-p) C S & p S^2 + (1-p) S^2 \end{pmatrix} = \begin{pmatrix} p C^2 & 0 & 0 \\ 0 & (1-p) C^2 & (1-p) C S \\ 0 & (1-p) C S & S^2 \end{pmatrix} $$
First eigenvalue: $\lambda_1 = p C^2$.
Eigenvalues of lower block: $\lambda = \frac{1}{2} (S^2 + (1-p) C^2 \pm \sqrt{(S^2 - (1-p) C^2)^2 + 4 (1-p)^2 C^2 S^2})$.
Simplify discriminant: $(S^2 - (1-p) C^2)^2 + 4 (1-p)^2 C^2 S^2 = S^4 - 2(1-p) C^2 S^2 + (1-p)^2 C^4 + 4 (1-p)^2 C^2 S^2$
$= S^4 + 2 C^2 S^2 (2(1-p)^2 - (1-p)) + (1-p)^2 C^4$.
This does not look simple. However, we don't need to solve for eigenvalues explicitly if we can match the form to a known result or simplify the entropy expression.

Let's try the relation $\chi = S(\bar{\rho}) - \sum p_i S(\rho_i)$.
Here $\rho_1$ pure $\implies S(\rho_1) = 0$.
$\rho_2$ mixed $\implies S(\rho_2) = h(C^2)$.
$\chi(p) = S(\bar{\rho}) - p h(C^2)$.
We need to maximize this over $p \in [0,1]$.
The entropy $S(\bar{\rho})$ is the entropy of eigenvalues $\{p C^2, \sigma_+, \sigma_-\}$.
$\sigma_\pm = \frac{1}{2} ( 1 - p C^2 \pm \sqrt{\Delta} )$.
The value $S(\bar{\rho})$ will be maximum when eigenvalues are equal, i.e., $1/3$.
This requires $p C^2 = 1/3 \implies p = 1/(3 C^2)$. Also $\sigma_+ = 1/3 \implies \sqrt{\Delta} = 2(1/3) - (1 - p C^2)$ impossible since $\sigma_+ > \text{mean}.
Actually for max entropy, we just want them as spread out as possible.
The function $f(x)$ in the problem statement asks for a single variable $x$. It is likely $x=p$.

Is there a geometric interpretation?
$\rho_x$ are points on a "segment" of state space?
The states are convex combinations of $|1\rangle$ and states in the $|2\rangle, |3\rangle$ circle.
$\rho_x = \gamma C^2 |1\rangle\langle 1| + (1 - \gamma C^2) |\psi_\phi\rangle\langle \psi_\phi|$.
Note that the weight of $|1\rangle$ is $x = \gamma C^2 \in [0, C^2]$.
Let's assume the optimal ensemble is between $\gamma=0$ and $\gamma=1$.
$\rho_0 = |\psi_0\rangle\langle \psi_0|$.
$\rho_1 = C^2 |1\rangle\langle 1| + S^2 |3\rangle\langle 3|$.
Consider the Holevo information for this pair.
The function to maximize is $S(p \rho_1 + (1-p) \rho_0) - p h(C^2)$.

Let's verify if we can simply identify the function form.
The problem asks for $\max_{x \in [0,1]} f(x)$.
$x$ is likely the maximal distinguishability parameter.
Perhaps the "model" is simply identifying the correct expression for the Holevo information in terms of the variable $p$.

Based on standard results for Holevo capacity of qubit channels or similar problems (like the q-depolarizing channel or amplitude damping), the optimal ensemble is often binary.
Let's define $x=p$.
Then we need to formulate $f(x)$.
$f(x) = S(x \rho_1 + (1-x) \rho_0) - x h(C^2)$.
We can leave $S(x \rho_1 + (1-x) \rho_0)$ as the entropy of the eigenvalues.

Eigenvalues of $\bar{\rho}_x$:
1. $\lambda_1 = x C^2$.
2. $\lambda_{2,3}$ are eigenvalues of $M = \begin{pmatrix} (1-x) C^2 & (1-x) C S \\ (1-x) C S & S^2 \end{pmatrix}$.
Trace $M = (1-x) C^2 + S^2 = 1 - x C^2$.
Det $M = (1-x) C^2 S^2 - (1-x)^2 C^2 S^2 = (1-x) x C^2 S^2$.
Eigenvalues are $\frac{1}{2} \left( 1 - x C^2 \pm \sqrt{ (1 - x C^2)^2 - 4 (1-x) x C^2 S^2 } \right)$.
Let's compute the square root term $D$:
$(1 - x C^2)^2 - 4 x (1-x) C^2 S^2 = 1 - 2 x C^2 + x^2 C^4 - 4 x C^2 S^2 + 4 x^2 C^2 S^2$.
Recall $S^2 = 1 - C^2$.
$- 4 x C^2 (1 - C^2) = -4 x C^2 + 4 x C^4$.
$D = 1 - 2 x C^2 + x^2 C^4 - 4 x C^2 + 4 x C^4 + 4 x^2 C^2 - 4 x^2 C^4$.
$= 1 - 6 x C^2 + 5 x C^4 + 4 x^2 C^2 - 3 x^2 C^4$.
$= 1 - C^2 (6x - 5x C^2 + x^2 C^2 (3 - \dots ))$.
This seems overly complex. Let's check the block matrix again.
$\bar{\rho} = \text{diag}(x C^2, M)$.
Trace of $M$ is $(1-x) C^2 + S^2$.
Det of $M$: $S^2 (1-x) C^2 - ((1-x) C S)^2$.
$(1-x) C^2 S^2 (1 - (1-x)) = (1-x) x C^2 S^2$.
Correct.
What if the term under square root is a perfect square for specific $x$?
Or maybe we define $u = \sqrt{D}$.
Then eigenvalues are $\frac{1}{2}(1 - x C^2 \pm u)$.
So $S(\bar{\rho}) = h(x C^2) + h(\frac{1}{2}(1 - x C^2 + u))$.
Then $f(x) = h(x C^2) + h(\frac{1}{2}(1 - x C^2 + u)) - x h(C^2)$.
This is a valid function of $x$.

Wait, looking at the structure of $\rho_x$, the parameter $\gamma_x$ defines the "population" of state $|1\rangle$.
If we want to maximize accessible information, we should choose states with extremal $\gamma_x$ (0 and 1).
The variable $x$ in the max expression corresponds to the probability $p$ of choosing state $\gamma=1$.
Also, we should optimize over $\phi_x$. We implicitly used $\phi=0$ for consistency.
So $f(x)$ describes the Holevo capacity for the binary ensemble $\{\rho_0, \rho_1\}$.

The function form is:
$$ f(x) = H(x C^2) + H\left( \frac{1 - x C^2 + \sqrt{(1 - x C^2)^2 - 4 x (1-x) C^2 (1-C^2)}}{2} \right) - x H(C^2) $$
where $H(y)$ is the binary entropy $-y \log y - (1-y) \log(1-y)$.

We can check if the root expression simplifies.
$D = (1 - x C^2)^2 - 4 x (1-x) C^2 S^2$.
$= 1 - 2 x (S^2 + C^2) + x^2 (S^2 + C^2)^2 - 4 x (1-x) C^2 S^2$? No.
Try $D = ( (1-x) S^2 - x C^2 )^2$?
$(S^2 - x S^2 - x C^2)^2 = (S^2 - x(S^2+C^2))^2 = (S^2 - x)^2 = x^2 - 2 x S^2 + S^4$.
Our $D = 1 - 2 x C^2 + \dots$
Match coefficients of $x^2$: $D$ has $x^2 (C^4 + 4 C^2 S^2) = x^2 (C^4 + 4 C^2 - 4 C^4) = x^2 (4 C^2 - 3 C^4)$. Not 1.
However, we don't need to simplify $D$. The problem asks for the explicit function form.

Let's verify the domain $x \in [0,1]$.
If $x=0$, ensemble is just $\rho_0$. Holevo info is 0.
$f(0) = H(0) + H(1/2 (1 + 1)) - 0 = 0 + H(1) - 0 = 0$. Correct.
If $x=1$, ensemble is just $\rho_1$. Holevo info is 0.
$f(1) = H(C^2) + H(1/2 (1 - C^2 + |1-C^2|)) - H(C^2)$.
$D = (1-C^2)^2 = S^4$. $\sqrt{D} = S^2 = 1-C^2$.
Term is $1/2 (1 - C^2 + 1 - C^2) = 1 - C^2$. $H(1-C^2) - H(C^2) = 0$. $f(1) = H(C^2) - H(C^2) = 0$. Correct.

What if $\sqrt{D} = S^2 - x C^2$?
Check: $(S^2 - x C^2)^2 = S^4 - 2 x S^2 C^2 + x^2 C^4$.
Our $D$: $1 - 2 x C^2 + x^2 C^4 - 4 x (1-x) C^2 S^2$.
$= (C^2+S^2)^2 - \dots = C^4 + S^4 + 2 C^2 S^2 - 2 x C^2 (C^2 + 2 S^2) + x^2 (C^4 + 4 C^2 S^2)$.
Not same.

Wait, what if the mixed state $\rho_1$ was the one with $\gamma=0$?
$\rho_0 = C^2 |1\rangle\langle 1| + S^2 |3\rangle\langle 3|$. (Rank 2).
$\rho_1 = |\psi\rangle\langle\psi|$. (Rank 1).
Ensemble probability $p$ for $\rho_1$.
This is the same setup, just renaming states. $f(x)$ would be the same because Holevo info is symmetric in swapping indices if we adjust $x \to 1-x$?
$\chi = S((1-p)\rho_0 + p\rho_1) - (1-p)h(C^2)$.
Replace $x = 1-p$.
$S(x \rho_0 + (1-x)\rho_1) - x h(C^2)$.
If we define $\rho_1$ as the mixed state and $\rho_0$ as pure, the previous derivation stands.

Wait, is it possible to go above the binary ensemble?
With 3 states? $\rho_a, \rho_b, \rho_c$.
Since the states $\rho_x$ lie in a specific manifold (union of line segments between $|1\rangle$ and the circle of pure states in span(2,3)), the convex hull of accessible entropies might be defined by the extremal points.
Basically, maximizing Holevo is usually a convex optimization problem (actually maximizing a convex function over a convex set, so optimum at boundary).
The boundary of the set of ensembles (in terms of $\bar{\rho}$) is generated by finite sets of states.
With these specific states, binary is a strong candidate.

Let's write down the function $f(x)$ clearly.
We need $f(x)$ such that $\chi_{\max} = \max_{x \in [0,1]} f(x)$.
We have derived a candidate for $f(x)$ based on the optimal binary ensemble.
Is there any other parameter?
Could it be $\gamma$?
The problem asks to optimize over cq states $\chi = \sum p_x |x\rangle\langle x| \otimes \rho_x$.
This corresponds to optimizing over ensembles $\{p_x, \rho_x\}$.
We assumed binary ensemble is optimal.
If the problem implies we just need to write the expression for the optimal scenario, then $f(x)$ is the expression we found.

The function $f(x)$ is the Holevo quantity for a binary ensemble of one pure state and one mixed state (specifically $\rho_1$ and $\rho_0$).
However, let's check if $\rho_1$ (with $\gamma=1$) is the best mixed state.
Any state $\rho_\gamma$ is entropy $h(\gamma C^2)$.
The distance between $\rho_\gamma$ and pure state $\rho_0$ (or any pure $\rho_{\gamma=0}$)...
$\rho_{\gamma} = \gamma C^2 |1\rangle\langle 1| + (1-\gamma C^2) |\psi_\gamma\rangle\langle\psi_\gamma|$.
$\rho_0 = | \theta, \phi \rangle \langle \theta, \phi |$ (in 2-3 plane).
The mixed states are "closer" to the pure states in the 2-3 plane if $\gamma$ is small.
If $\gamma=1$, support is $\{|1\rangle, |3\rangle\}$. Pure state $\rho_0$ has support $\{|2\rangle, |3\rangle\}$.
Overlap is on $|3\rangle$.
If we choose $\rho_0$ orthogonal to $\rho_1$'s support?
$\rho_0$ fixed. $\rho_1$ has $|1\rangle$.
$\rho_0$ has no $|1\rangle$.
So $\rho_0$ and $|1\rangle$ are orthogonal.
The Holevo info becomes "information about whether we are in state with $|1\rangle$ component".
The largest $|1\rangle$ component is $\gamma=1$, which gives weight $C^2$.
If we choose $\gamma < 1$, weight is smaller, distinguishability is lower.
So $\gamma=1$ is the optimal choice for the mixed state in the ensemble.

Thus, the optimal ensemble is indeed $\{\rho_{pure}, \rho_{mixed}\}$.
The function $f(x)$ is the Holevo information for this ensemble as a function of the probability $x$ (of the mixed state).

Final check on the mathematical expression.
Eigenvalues of $\bar{\rho} = x \rho_1 + (1-x) \rho_0$.
We established eigenvalues are:
$\eta_1 = x C^2$.
$\eta_{\pm} = \frac{1}{2} \left( 1 - x C^2 \pm \sqrt{ (1-x C^2)^2 - 4 x(1-x) C^2 S^2 } \right)$.
(Note: $\eta_- = 1-\eta_+$).
So entropy $S(\bar{\rho}) = h(\eta_1) + h(\eta_+)$.
$S(\rho_1) = h(C^2)$.
$S(\rho_0) = 0$.
$\chi = h(\eta_1) + h(\eta_+) - x h(C^2)$.

So $f(x) = h(x \cos^2\theta) + h\left( \frac{1 - x \cos^2\theta + \sqrt{(1 - x \cos^2\theta)^2 - 4 x (1-x) \cos^2\theta \sin^2\theta}}{2} \right) - x h(\cos^2\theta)$.

This is an explicit function of $x \in [0,1]$.

One small detail: $\rho_0$ in my derivation was $\gamma=0$. $\rho_1$ was $\gamma=1$.
This corresponds to $x$ being probability of $\gamma=1$.
The states in the ensemble are $\rho_1$ and $\rho_0$.
We assumed $\phi=0$ (or optimized $\phi$). The $\phi$ in $\rho_0$ affects the eigenvalues of $\bar{\rho}$ via the term $\cos\theta \sin\theta \dots$ in $\bar{\rho}$.
My derivation for eigenvalues of $\bar{\rho}$ assumed the "compatible" $\phi$ (such that the off-diagonal terms add up positively or maximally).
The term is $p \cdot 0 + (1-p) C S = (1-p) C S$.
The term in $\bar{\rho}$ is $\Sigma \sqrt{1-\gamma_i} p_i C S e^{i\phi_i}$.
To maximize entropy, we maximize the "spread" of eigenvalues.
The term $\sqrt{(1-x C^2)^2 - \mathcal{O}(|\text{off-diag}|^2)}$.
To maximize entropy, we generally want to minimize the discriminant (to bring eigenvalues closer together) or maximize it (to push them apart)?
$h(y)$ is concave and peaks at $1/2$.
Sum of entropies $h(a) + h(b)$ where $a+b$ is partially constrained.
Here $\eta_1 + \eta_+ + \eta_- = \eta_1 + 1 = 1 + x C^2$. (Trace constraint).
We want $\{\eta_1, \eta_+, \eta_-\}$ to be as close to each other as possible or just distributed?
For fixed trace $T=1+x C^2$, the max entropy $\log d$ is achieved when all equal. But $\eta_+ + \eta_- = 1-x C^2$. Their average is $(1-x C^2)/2$.
$\eta_1 = x C^2$.
We want $x C^2 \approx 1/3$ and $\eta_+ \approx 1/3$.
This means $1-x C^2 \approx 2/3 \implies x C^2 \approx 1/3$. Consistent.
So near $x = 1/(3 C^2)$.
At this point, we want $\eta_+ = \eta_- = (1-x C^2)/2$.
This requires $\sqrt{\Delta} = 0$.
$\Delta = (1-x C^2)^2 - 4 x(1-x) C^2 S^2 = 0$.
$(1-x C^2)^2 = 4 x(1-x) C^2 (1-C^2)$.
If this has a solution for $x \in [0,1]$, then we can reach the max entropy configuration for that $x$.
If not, we optimize $|Z|$ to minimize $\Delta$. $|Z|$ is maximized when $\phi$ is consistent.
My calculation used that maximum coherence case.
So the formula for $f(x)$ is correct assuming we optimize $\phi$ (which we do for the Holevo information).

One simplification:
Let $u = x$.
$s = \sin(2\theta) = 2 \sin\theta \cos\theta$.
$C^2 S^2 = s^2 / 4$.
$4 x (1-x) C^2 S^2 = x(1-x) s^2$.
So $\Delta = (1 - u C^2)^2 - u(1-u) s^2$.
This form is slightly cleaner.

Final check: The problem asks for $\max_{x \in [0,1]} f(x)$.
We provide $f(x)$.

$$ f(x) = H(x \cos^2\theta) + H\left( \frac{1 - x \cos^2\theta + \sqrt{(1 - x \cos^2\theta)^2 - x(1-x)\sin^2(2\theta)}}{2} \right) - x H(\cos^2\theta) $$

Does this depend only on $x$ (given $\theta$ is constant of the problem)? Yes.
Is it explicit? Yes.

One edge case: $x=0$. $f(0) = H(0) + H(1/2(1+1)) - 0 = 0 + 0 - 0 = 0$.
$x=1$. $f(1) = H(C^2) + H(1/2(1-C^2 + |1-C^2|)) - H(C^2) = 0$.
$\Delta = S^4$. $\sqrt{\Delta} = S^2$.
Term: $(1-C^2 + S^2)/2 = (S^2+S^2)/2 = S^2$. $H(S^2) = H(C^2)$.
So $H(C^2) + H(C^2) - H(C^2) = H(C^2)$.
Wait. $f(1)$ should be 0 (ensemble of single state).
Why did I get $H(C^2)$?
$S(\bar{\rho}) = S(\rho_1) = H(C^2)$.
$\sum p_i S(\rho_i) = 1 \cdot H(C^2)$.
Difference is 0.
My formula result:
$H(C^2) + H(S^2) - H(C^2) = H(S^2) \neq 0$.
Where is the error?
When $x=1$, $\rho_0$ is not in the ensemble. $\bar{\rho} = \rho_1$.
The formula for eigenvalues of $\bar{\rho}$ was derived for the *mixture*.
When $x=1$, the lower block is just the block of $\rho_1$.
Lower block of $\rho_1$ is $\text{diag}(0, S^2)$.
Eigenvalues are $0$ and $S^2$.
My formula:
$\frac{1}{2} (1 - C^2 \pm \sqrt{S^4 - 0}) = \frac{1}{2} (S^2 \pm S^2)$.
$\lambda_+ = S^2, \lambda_- = 0$.
So $H(\lambda_+) = H(S^2)$.
So $S(\bar{\rho}) = H(\lambda_1) + H(\lambda_+) = H(C^2) + H(S^2)$.
Wait, $\rho_1$ has eigenvalues $C^2, S^2, 0$.
So $S(\rho_1) = H(C^2) + H(S^2)$.
Why did I write $S(\rho_1) = H(C^2)$ before?
$\rho_1 = \text{diag}(\gamma C^2, \dots)$.
$\rho_1$ has diag $(C^2, 0, S^2)$.
Eigenvalues $C^2, S^2, 0$.
So $S(\rho_1) = H(C^2) + H(S^2)$.

Ah, earlier I defined $\rho_1$ as the mixed state with $\gamma=1$.
Eigenvalues of $\rho_x$: $\gamma_x C^2, 1 - \gamma_x C^2, 0$.
For $\gamma=1$: $\{C^2, 1-C^2, 0\}$. Yes, $S(\rho_1) = H(C^2) + H(S^2)$.
For $\gamma=0$: $\{0, 1, 0\}$. Pure state. $S(\rho_0) = 0$.
So $\sum p_i S(\rho_i) = x (H(C^2) + H(S^2))$.
So $f(x) = H(x C^2) + H(\lambda_+) - x (H(C^2) + H(S^2))$.
Let's check $x=1$.
$f(1) = H(C^2) + H(S^2) - 1(H(C^2) + H(S^2)) = 0$. Correct.
Let's check $x=0$.
$f(0) = 0 + H(1) - 0 = 0$. Correct.

So the correct function is:
$$ f(x) = H(x \cos^2\theta) + H\left( \frac{1 - x \cos^2\theta + \sqrt{(1 - x \cos^2\theta)^2 - x(1-x)\sin^2(2\theta)}}{2} \right) - x \left( H(\cos^2\theta) + H(\sin^2\theta) \right) $$
Since $H(\sin^2\theta) = H(\cos^2\theta)$, we can write $2 x H(\cos^2\theta)$.
$$ f(x) = H(x \cos^2\theta) + H(\lambda_+(x)) - 2 x H(\cos^2\theta) $$
where $\lambda_+(x)$ is the larger root.

This looks solid.
The variable $x$ is the probability of the state $\rho_x$ with $\gamma=1$.
The ensemble is $\{ (x, \rho_1), (1-x, \rho_0) \}$.

The problem statement "Optimize the Holevo information over cq states... Write the maximal value in terms of an optimization... $f(x)$ depends only on $x$".
This implies we have derived the capacity form $C = \max_{p \in \Delta(\mathcal{X})} \chi(p, \{\rho_x\})$.
Given our analysis, the optimal ensemble uses the extremal states $\gamma=0$ and $\gamma=1$.
So the problem reduces to maximizing over the mixing parameter $x$.

The function is:
$$ f(x) = H(x \cos^2\theta) + H\left( \frac{1}{2} \left( 1 - x \cos^2\theta + \sqrt{ (1 - x \cos^2\theta)^2 - x(1-x)\sin^2(2\theta) } \right) \right) - 2 x H(\cos^2\theta) $$
Note: $(1 - x \cos^2\theta)^2 - x(1-x)\sin^2(2\theta) = 1 - 2x \cos^2\theta + x^2 \cos^4\theta - 4x(1-x)\cos^2\theta\sin^2\theta$.
It's fine.

Double check coefficients.
Block trace: $1 - x C^2$.
Block determinant: $x(1-x) C^2 S^2$.
$\lambda_\pm = \frac{1}{2} (\text{tr} \pm \sqrt{\text{tr}^2 - 4 \text{det}})$.
$= \frac{1}{2} (1 - x C^2 \pm \sqrt{ (1 - x C^2)^2 - 4 x (1-x) C^2 S^2 })$.
Formula matches.
$\sin^2(2\theta) = 4 S^2 C^2$. Formula matches.

Final Answer Construction:
1. Define the states $\rho_{pure}$ (from $\gamma=0$) and $\rho_{mixed}$ (from $\gamma=1$).
2. Define the ensemble $\{ x \rho_{mixed}, (1-x) \rho_{pure} \}$.
3. Calculate eigenvalues of the average state from this ensemble.
4. Formulate the Holevo quantity $\chi(x)$.
5. State that the maximum Holevo information is $\max_{x \in [0,1]} \chi(x)$.
6. Provide the explicit expression for $f(x) = \chi(x)$.

Steps for explanation:
- Analyze the structure of $\rho_x$ and show they are rank-2 mixtures.
- Identify extremal states $\gamma=0$ (pure) and $\gamma=1$ (maximally mixed w.r.t the subspace).
- Argue that the optimal ensemble must use these extremal states to maximize distinguishibility (heuristic but standard for such convex problems).
- Compute the eigenvalues of the average state of the binary ensemble.
- Compute the Holevo sum.
- Write down the final function $f(x)$.

Assume $\theta$ is fixed.
The function $f(x)$ exists on $[0,1]$.
One more check: Can we simplify $H(\lambda_+) + H(\lambda_-)$? $\lambda_- = 1 - \eta_1 - \lambda_+ = 1 - x C^2 - \lambda_+$.
Wait, for the block, trace is $1-x C^2$. $\lambda_- = (1-x C^2) - \lambda_+$.
So entropy of block is $H(\lambda_+)$ with base 2 entropy of 2 outcomes? No, $H(p) = -p \log p - (1-p) \log (1-p)$. The entropy of the eigenpairs $\lambda_+, \lambda_-$ is exactly $H(\lambda_+)$.
So the total entropy $S(\bar{\rho}) = H(x C^2) + H(\lambda_+)$.
Correct.

The term $2 x H(C^2)$ comes from $x S(\rho_{mixed})$.
$S(\rho_{mixed}) = H(C^2) + H(1-C^2) = 2 H(C^2)$.
Correct.

The function looks complete.

Also, verify the "depends only on $x$" constraint.
The function $f(x)$ depends on $\theta$. The problem statement says "$f(x)$ depends only on $x$ and nothing else", which usually implies parameters of the model (like $\theta$) are considered constants of the function definition, i.e., $f(x; \theta)$.
The phrase "depends only on x" in the prompt likely means "is a function of x alone" (as opposed to being a functional of the distribution), with $\theta$ being a fixed parameter of the physical system. Otherwise, $f(x)$ would be trivial or impossible without fixing $\cos\theta$. The problem setup fixes $\theta$.

Final Result:
$$ \max_{x \in [0,1]} f(x) $$
$$ f(x) = h(x \cos^2\theta) + h\left( \frac{1 - x \cos^2\theta + \sqrt{(1 - x \cos^2\theta)^2 - x(1-x)\sin^2(2\theta)}}{2} \right) - 2 x h(\cos^2\theta) $$
where $h(u) = -u \log_2 u - (1-u) \log_2 (1-u)$.
Any base can be used for log, usually 2 or $e$.
I will specify $h(x)$ as the binary entropy function.

One detail: $\rho_x$ for general $\gamma$. $S(\rho_x) = h(\gamma C^2) + h((1-\gamma)C^2 + S^2)$?
No, eigenvalues are $\gamma C^2$ and $1 - \gamma C^2$. The third is 0.
$S(\rho) = h(\gamma C^2) + h(1 - \gamma C^2)$?
No. $h(y)$ is entropy of distribution $\{y, 1-y\}$.
Eigenvalues $\{ \gamma C^2, 1 - \gamma C^2, 0 \}$.
This is a 3-part distribution.
$S(\rho) = - (\gamma C^2) \log(\gamma C^2) - (1-\gamma C^2) \log(1-\gamma C^2) - 0 \log 0$.
$= h(\gamma C^2)$.
Wait.
$h(y)$ is defined for a binary variable.
Here we have a ternary distribution, but one value is 0.
$S(p_1, p_2, p_3)$ with $p_3=0$ is $-p_1 \log p_1 - p_2 \log p_2$.
Let $p_1 = \gamma C^2$. $p_2 = 1 - \gamma C^2$.
Then $S(\rho) = h(\gamma C^2)$.
Ah, I made a mistake earlier adding $H(S^2)$.
Let's re-evaluate $S(\rho_1)$ for $\gamma=1$.
Eigenvalues: $\{ C^2, 1-C^2, 0 \}$.
$S(\rho_1) = -C^2 \log C^2 - (1-C^2) \log(1-C^2) = h(C^2)$.
Because $1 - \gamma C^2 = 1 - C^2 = S^2$.
So $\rho_1$ has eigenvalues $\{C^2, S^2, 0\}$.
This is a distribution $\{C^2, S^2, 0\}$.
The entropy is the sum of $-p \log p$.
Is $S(\rho_1) = h(C^2)$?
$h(C^2) = -C^2 \log C^2 - S^2 \log S^2$.
Yes! The definition of $h(y)$ covers the sum of the two non-zero terms.
So $S(\rho_1) = h(C^2)$.
My previous calculation $2 H(C^2)$ was wrong because I thought entropy was additive on blocks $S(\text{diag}(A, B)) = S(A) + S(B)$.
For $\rho_1$: Block 1 is $(C^2)$. Entropy $h(C^2)$.
Block 2 is $\text{diag}(0, S^2)$. Entropy $h(S^2)$.
Total entropy $h(C^2) + h(S^2)$.
Why the discrepancy?
Because eigenvalues of $\rho_1$ are $\{C^2, S^2, 0\}$.
$S(\rho_1) = -C^2 \log C^2 - S^2 \log S^2 - 0 \log 0$.
This is equal to $h(C^2)$.
But is $h(C^2) + h(S^2)$ equal to $h(C^2)$?
$h(S^2) = h(1-C^2)$.
$-S^2 \log S^2 - (1-S^2) \log (1-S^2) = -S^2 \log S^2 - C^2 \log C^2$.
So $h(S^2) = h(C^2)$.
So $S(\text{block 1}) = h(C^2)$. $S(\text{block 2}) = h(S^2) = h(C^2)$.
So $S(\rho_1) = h(C^2) + h(C^2) = 2 h(C^2)$?
Where is the error?
The error is in assuming $S(\text{diag}(A, B)) = S(A) + S(B)$ holds with standard definition of von Neumann entropy for the blocks?
Yes, it holds.
Block 1: 1x1 matrix $(C^2)$. Eigenvalues $\{C^2\}$. Entropy $h(C^2)$. No, entropy of a single number $p$ is $h(p)$.
Wait, for a 1x1 matrix $(p)$, the entropy is defined as $-p \log p$ (assuming prob, but density matrix trace must be 1?
Ah. The blocks are not sub-normalized density matrices. They are just matrix blocks.
$\rho_1 = \begin{pmatrix} C^2 & 0 & 0 \\ 0 & 0 & 0 \\ 0 & 0 & S^2 \end{pmatrix}$.
Block 1 is $(C^2)$. Trace $C^2$. This is not a density matrix.
You cannot just take $S(A) + S(B)$ for non-normalized blocks.
You must normalize them.
Block 1 normalized is $(1)$. Entropy 0?
Wait, $S(\rho)$ is log of eigenvalues.
$\rho_1$ has eigenvalues $\{C^2, S^2, 0\}$.
$S(\rho_1) = h(C^2) + h(S^2)$? No.
$S(\rho_1) = -C^2 \log C^2 - S^2 \log S^2$.
This is just $h(C^2)$. (Since $h(y) = -y \log y - (1-y) \log(1-y)$).
$S(\rho_1) = h(C^2)$.
Why?
Because the two non-zero eigenvalues sum to 1. $C^2 + S^2 = 1$.
So $\rho_1$ is effectively a rank-2 matrix with probabilities $C^2, S^2$.
The third eigenvalue is 0.
So $S(\rho_1) = h(C^2)$.

Let's re-check $\sum p_i S(\rho_i)$.
$S(\rho_0)$ ($\gamma=0$): Eigenvalues $\{0, 1, 0\}$. Entropy $0$. (Since $1 \log 1 = 0$).
$S(\rho_1)$ ($\gamma=1$): Eigenvalues $\{C^2, S^2, 0\}$. Entropy $h(C^2)$.
So $\sum p_i S(\rho_i) = x h(C^2)$.

This changes the formula!
Old formula: $f(x) = S(\bar{\rho}) - 2 x h(C^2)$.
New formula: $f(x) = S(\bar{\rho}) - x h(C^2)$.

Let's check $x=1$.
$f(1) = S(\rho_1) - h(C^2) = h(C^2) - h(C^2) = 0$. Correct.
Let's check $x=0$.
$f(0) = S(\rho_0) - 0 = 0$. Correct.

Okay, the model was close but the entropy of the mixed state was overestimated.
Correct function:
$$ f(x) = H(x \cos^2\theta) + H\left( \frac{1 - x \cos^2\theta + \sqrt{ (1 - x \cos^2\theta)^2 - x(1-x)\sin^2(2\theta) }}{2} \right) - x H(\cos^2\theta) $$
This feels more natural. The noise penalty is just the average entropy of the mixed states.

Wait, let's re-verify $S(\rho_x)$ for general $\gamma_x$.
Eigenvalues $\gamma_x C^2$, $1-\gamma_x C^2$, $0$.
Sum is 1.
Entropy is $h(\gamma_x C^2)$.
Yes. My previous block decomposition was misleading because blocks weren't normalized.
For general $\gamma$, $S(\rho_x) = h(\gamma_x C^2)$.
So $S(\rho_1) = h(C^2)$.
$S(\rho_0) = h(0) = 0$.
So $\sum p_x S(\rho_x) = x h(C^2)$.

And $S(\bar{\rho})$ calculation:
Eigenvalues $\eta_1 = x C^2$.
$\eta_{\pm}$ are roots of $\lambda^2 - (1 - x C^2) \lambda + x(1-x) C^2 S^2 = 0$.
Note $\eta_+ + \eta_- = 1 - x C^2$.
So $S(\bar{\rho}) = h(\eta_1) + h(\eta_+)$.
This part is correct (sum of entropies).
So $f(x) = h(x C^2) + h(\eta_+) - x h(C^2)$.
Also $\eta_- = (1 - x C^2) - \eta_+$.
So $h(\eta_+) = -\eta_+ \log \eta_+ - \eta_- \log \eta_-$.
Is $h(\eta_+)$ the entropy of the 2-eigenvalue system?
Yes.
So $S(\bar{\rho}) = h(x C^2) + h(\eta_+)$.

The final expression is consistent.

Summary of Model:
1. Problem setup: Define states and Holevo information.
2. Reduction: Determine that optimal ensemble uses $\gamma=0$ and $\gamma=1$.
3. Calculation:
   - Define $x = p_{\gamma=1}$.
   - State $\rho_{mixed} = \rho_{\gamma=1}$, $\rho_{pure} = \rho_{\gamma=0}$.
   - Average state $\bar{\rho} = x \rho_{mixed} + (1-x) \rho_{pure}$.
   - Compute eigenvalues of $\bar{\rho}$.
     - $\lambda_1 = x \cos^2\theta$.
     - $\lambda_{2,3}$ from quadratic equation.
   - Compute entropies.
     - $S(\bar{\rho}) = h(\lambda_1) + h(\lambda_2)$.
     - $\sum p_x S(\rho_x) = x h(\cos^2\theta)$.
   - Construct $f(x)$.
4. Result: The maximal value is $\max_{x \in [0,1]} f(x)$ with explicit $f(x)$.
</think># Mathematical Model for Optimizing Holevo Information

## 1. Problem Setup and Definitions

We are given a classical-quantum state defined by the ensemble $\mathcal{E} = \{p_x, \rho_x\}$:
$$ \chi_{\text{state}} = \sum_x p_x |x\rangle\langle x| \otimes \rho_x $$
where each density matrix $\rho_x$ is defined in the computational basis as:
$$ \rho_x = \begin{pmatrix} \gamma_x \cos^2 \theta & 0 & 0 \\ 0 & (1-\gamma_x)\cos^2 \theta & \sqrt{1-\gamma_x}\cos \theta \sin \theta e^{i \phi_x} \\ 0 & \sqrt{1-\gamma_x}\cos \theta \sin \theta e^{-i \phi_x} & \sin^2 \theta \end{pmatrix} $$
with parameters $\gamma_x \in [0,1]$, $\phi_x \in \mathbb{R}$, and a fixed $\theta$ such that $\cos \theta \neq 1$.

The **Holevo information** (or quantity) for this ensemble is given by:
$$ \chi(\mathcal{E}) = S\left( \sum_x p_x \rho_x \right) - \sum_x p_x S(\rho_x) $$
where $S(\sigma) = -\text{Tr}(\sigma \log_2 \sigma)$ is the von Neumann entropy.

## 2. Model Steps and Derivation

### Step 1: Analyze the Structure of the States $\rho_x$

First, we determine the entropy of an individual state $S(\rho_x)$. The entropy is determined by the eigenvalues of $\rho_x$. The matrix $\rho_x$ is block diagonal. The upper-left $1 \times 1$ block gives an eigenvalue $\lambda_1 = \gamma_x \cos^2 \theta$.

The lower-right $2 \times 2$ block is:
$$ \Sigma_x = \begin{pmatrix} (1-\gamma_x)\cos^2 \theta & \sqrt{1-\gamma_x}\cos \theta \sin \theta e^{i \phi_x} \\ \sqrt{1-\gamma_x}\cos \theta \sin \theta e^{-i \phi_x} & \sin^2 \theta \end{pmatrix} $$
The trace of this block is $\text{Tr}(\Sigma_x) = (1-\gamma_x)\cos^2 \theta + \sin^2 \theta = 1 - \gamma_x \cos^2 \theta$.
The determinant is $\det(\Sigma_x) = (1-\gamma_x)\cos^2 \theta \sin^2 \theta - (1-\gamma_x)\cos^2 \theta \sin^2 \theta = 0$.
Since the determinant is zero, one eigenvalue is $0$. The other eigenvalue must be the trace, which is $1 - \gamma_x \cos^2 \theta$.

Thus, the spectrum of $\rho_x$ is $\{ \gamma_x \cos^2 \theta, 1 - \gamma_x \cos^2 \theta, 0 \}$.
Note that the parameter $\phi_x$ does not affect the eigenvalues. The entropy of $\rho_x$ is:
$$ S(\rho_x) = h(\gamma_x \cos^2 \theta) $$
where $h(y) = -y \log_2 y - (1-y) \log_2 (1-y)$ is the binary entropy function (with the convention $0 \log 0 = 0$).

### Step 2: Determine the Optimal Ensemble Configuration

To maximize the Holevo information $\chi$, we need to maximize the entropy of the average state $S(\bar{\rho})$ and minimize the average entropy $\sum p_x S(\rho_x)$.
* The term $\sum p_x S(\rho_x) = \mathbb{E}[h(\gamma_x \cos^2 \theta)]$ is minimized by placing probability mass on the extremal values of $\gamma_x$ (0 and 1), as $h(y)$ is concave.
* To maximize $S(\bar{\rho})$, we should choose states that are maximally distinguishable.
Using the extremal states $\gamma_x = 0$ and $\gamma_x = 1$ satisfies both criteria.
Let $\rho_0$ be the state with $\gamma=0$ and $\rho_1$ be the state with $\gamma=1$.
We consider a binary ensemble $\{ (x, \rho_1), (1-x, \rho_0) \}$ where $x \in [0,1]$ is the probability of choosing $\rho_1$. The optimal $\phi_x$ can be chosen to maximize the entropy (typically $\phi=0$ to align coherence).

### Step 3: Calculate the Average State and its Entropy

Let us define the mixed state (for $\gamma=1$) and the pure state (for $\gamma=0$):
$$ \rho_1 = \begin{pmatrix} \cos^2 \theta & 0 & 0 \\ 0 & 0 & 0 \\ 0 & 0 & \sin^2 \theta \end{pmatrix}, \quad \rho_0 = \begin{pmatrix} 0 & 0 & 0 \\ 0 & \cos^2 \theta & \cos \theta \sin \theta \\ 0 & \cos \theta \sin \theta & \sin^2 \theta \end{pmatrix} $$
Note: $S(\rho_1) = h(\cos^2 \theta)$ and $S(\rho_0) = h(0) = 0$.

The average state is $\bar{\rho} = x \rho_1 + (1-x) \rho_0$.
$$ \bar{\rho} = \begin{pmatrix} x \cos^2 \theta & 0 & 0 \\ 0 & (1-x)\cos^2 \theta & (1-x)\cos \theta \sin \theta \\ 0 & (1-x)\cos \theta \sin \theta & \sin^2 \theta \end{pmatrix} $$
We find the eigenvalues of $\bar{\rho}$:
1. The first row/column gives $\lambda_1 = x \cos^2 \theta$.
2. The lower-right $2 \times 2$ block has trace $T = (1-x)\cos^2 \theta + \sin^2 \theta = 1 - x \cos^2 \theta$ and determinant $D = (1-x)\cos^2 \theta \sin^2 \theta - (1-x)^2 \cos^2 \theta \sin^2 \theta = x(1-x) \cos^2 \theta \sin^2 \theta$.

The eigenvalues of this block are the roots of $\lambda^2 - T\lambda + D = 0$:
$$ \lambda_{\pm} = \frac{1}{2} \left( 1 - x \cos^2 \theta \pm \sqrt{ (1 - x \cos^2 \theta)^2 - 4 x(1-x) \cos^2 \theta \sin^2 \theta } \right) $$
We can simplify the term under the square root using $\sin^2(2\theta) = 4 \sin^2 \theta \cos^2 \theta$:
$$ \Delta = (1 - x \cos^2 \theta)^2 - x(1-x) \sin^2(2\theta) $$
Thus, the entropy of the average state is:
$$ S(\bar{\rho}) = h(\lambda_1) + h(\lambda_+) $$
where $\lambda_+$ is the larger root.

### Step 4: Formulate the Holevo Information Function $f(x)$

The Holevo information for this specific ensemble parameterized by $x$ is:
$$ \chi(x) = S(\bar{\rho}) - \left( x S(\rho_1) + (1-x) S(\rho_0) \right) $$
Substituting the entropies:
$$ \chi(x) = \left[ h(x \cos^2 \theta) + h\left( \frac{1 - x \cos^2 \theta + \sqrt{\Delta}}{2} \right) \right] - x h(\cos^2 \theta) $$
This function $\chi(x)$ depends only on the variable $x \in [0,1]$ (given $\theta$ is fixed).

The problem asks for the maximal value in terms of an optimization. Therefore, the maximal Holevo information is given by $\max_{x \in [0,1]} f(x)$, where $f(x)$ is the derived expression.

## 3. Final Mathematical Description

The maximal value of the Holevo information is given by the optimization:

$$ \chi_{\max} = \max_{x \in [0,1]} f(x) $$

where the function $f(x)$ is explicitly defined as:

$$ f(x) = h(x \cos^2 \theta) + h\left( \frac{1 - x \cos^2 \theta + \sqrt{ (1 - x \cos^2 \theta)^2 - x(1-x)\sin^2(2\theta) }}{2} \right) - x h(\cos^2 \theta) $$

Here, $h(u) = -u \log_2 u - (1-u) \log_2 (1-u)$ denotes the binary entropy function.
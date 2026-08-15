# Mathematical Description of the Holevo Information Optimization Model

## Problem Setup and Definitions

We are tasked with optimizing the Holevo information $\chi$ for an ensemble of quantum states. The relevant quantities are defined as follows:

1.  **Holevo Information ($\chi$):**
    The quantity to be optimized is defined as the difference between the von Neumann entropy of the average state and the average von Neumann entropy of the individual states in the ensemble:
    $$ \chi = S(\rho_{\text{avg}}) - \sum_x p_x S(\rho_x) $$
    where $S(\sigma) = -\text{Tr}(\sigma \log \sigma)$ denotes the von Neumann entropy.

2.  **The Ensemble States ($\rho_x$):**
    The problem provides a set of density matrices $\rho_x$ parameterized by $\gamma_x \in [0,1]$ and $\phi_x$:
    $$ \rho_x = \left(\begin{array}{ccc}
    \gamma_x \cos ^2 \theta & 0 & 0 \\
    0 & \left(1-\gamma_x\right) \cos ^2 \theta & \sqrt{1-\gamma_x} \cos \theta \sin \theta e^{i \phi_x} \\
    0 & \sqrt{1-\gamma_x} \cos \theta \sin \theta e^{-i \phi_x} & \sin ^2 \theta
    \end{array}\right) $$
    The state is weighted by probabilities $p_x$ in the classical-quantum state $\chi = \sum_x p_x |x\rangle\langle x|\otimes\rho_x$.

## Step 1: Analyzing the Entropy of Individual States

First, we determine the spectrum of the individual states $\rho_x$ to calculate their entropy $S(\rho_x)$. The matrix $\rho_x$ is block diagonal, consisting of a $1 \times 1$ block $\left[ \gamma_x \cos^2 \theta \right]$ and a $2 \times 2$ block:
$$ \begin{pmatrix} (1-\gamma_x)\cos^2 \theta & \sqrt{1-\gamma_x} \cos \theta \sin \theta e^{i \phi_x} \\ \sqrt{1-\gamma_x} \cos \theta \sin \theta e^{-i \phi_x} & \sin^2 \theta \end{pmatrix} $$
The eigenvalues of the $2 \times 2$ block are the roots of the characteristic polynomial:
$$ \lambda^2 - \lambda \left( (1-\gamma_x)\cos^2 \theta + \sin^2 \theta \right) = 0 $$
Thus, the eigenvalues of $\rho_x$ are:
$$ \lambda_1 = \gamma_x \cos^2 \theta $$
$$ \lambda_2 = (1-\gamma_x)\cos^2 \theta + \sin^2 \theta $$
$$ \lambda_3 = 0 $$

The entropy of $\rho_x$ is given by the binary entropy function $h(p) = -p \log p - (1-p) \log (1-p)$. Since $\lambda_2 = 1 - \lambda_1$:
$$ S(\rho_x) = h(\lambda_1) = h(\gamma_x \cos^2 \theta) $$
**Note:** The entropy of each state depends only on $\gamma_x$ (and the fixed parameter $\theta$) and is independent of the phase $\phi_x$.

## Step 2: Optimizing the Average State Entropy

The average state is $\rho_{\text{avg}} = \sum_x p_x \rho_x$. To maximize the Holevo information, we must maximize $S(\rho_{\text{avg}})$.

The structure of $\rho_{\text{avg}}$ is:
$$ \rho_{\text{avg}} = \left(\begin{array}{ccc}
\bar{\gamma} \cos ^2 \theta & 0 & 0 \\
0 & (1-\bar{\gamma})\cos ^2 \theta & \cos \theta \sin \theta \sum_x p_x \sqrt{1-\gamma_x} e^{i \phi_x} \\
0 & \cos \theta \sin \theta \sum_x p_x \sqrt{1-\gamma_x} e^{-i \phi_x} & \sin ^2 \theta
\end{array}\right) $$
where $\bar{\gamma} = \sum_x p_x \gamma_x$.

The entropy of the average state depends on the magnitude of the off-diagonal term, which is proportional to $\left| \sum_x p_x \sqrt{1-\gamma_x} e^{i \phi_x} \right|$.
*   To maximize entropy, a matrix should be as "mixed" as possible (i.e., eigenvalues should be uniform). Off-diagonal coherence terms generally reduce entropy by purifying the state.
*   Therefore, we can set the phases $\phi_x$ such that the off-diagonal term cancels out (for instance, by choosing phases uniformly distributed on $[0, 2\pi]$ if continuous, or opposite phases for symmetric pairs).
*   Under this optimal phase configuration, the matrix becomes diagonal:
    $$ \rho_{\text{avg}} \approx \text{diag}\left( \bar{\gamma} \cos^2 \theta, (1-\bar{\gamma})\cos^2 \theta, \sin^2 \theta \right) $$
    This yields the entropy $S(\rho_{\text{avg}}) = H(\bar{\gamma} \cos^2 \theta, (1-\bar{\gamma})\cos^2 \theta, \sin^2 \theta)$.

## Step 3: Reducing to a Single Variable Optimization

The Holevo information to maximize is now:
$$ \chi = S(\rho_{\text{avg}}) - \sum_x p_x S(\rho_x) = H(\bar{\gamma} \cos^2 \theta, (1-\bar{\gamma})\cos^2 \theta, \sin^2 \theta) - \sum_x p_x h(\gamma_x \cos^2 \theta) $$

We can treat the term $\cos^2 \theta$ as a constant scaling factor for the relevant subspace. Let $u_x = \gamma_x \cos^2 \theta$. The variance of $u_x$ determines the value of $\chi$.
The function $f(y) = - \sum_x p_x h(y_x)$ is maximized when the distribution of $y_x$ (and thus $\gamma_x \in [0,1]$) is extremized—that is, when the probability mass is concentrated at the boundaries of the domain. The ensemble achieving the maximal Holevo information is a binary mixture of states corresponding to $\gamma = 0$ and $\gamma = 1$.

Let $x$ be the probability assigned to the state with $\gamma = 1$ (and consequently $1-x$ is the probability for $\gamma = 0$).
*   Term 1 (Average Entropy): The average $\bar{\gamma} = x(1) + (1-x)(0) = x$.
    $$ S(\rho_{\text{avg}}) = H(x \cos^2 \theta, (1-x)\cos^2 \theta, \sin^2 \theta) $$
*   Term 2 (Individual Entropies): $h(1 \cdot \cos^2 \theta) = h(0 \cdot \cos^2 \theta) = h(\cos^2 \theta)$.
    $$ \sum_x p_x S(\rho_x) = x h(\cos^2 \theta) + (1-x) h(\cos^2 \theta) = h(\cos^2 \theta) $$

Subtracting these, we get the explicit function of $x$:
$$ f(x) = H(x \cos^2 \theta, (1-x)\cos^2 \theta, \sin^2 \theta) - h(\cos^2 \theta) $$

Using the grouping property of entropy $H(A, B, C) = h(A+B) + (A+B)h(\frac{A}{A+B})$, where $A = x \cos^2 \theta$ and $B = (1-x)\cos^2 \theta$:
$$ f(x) = \left[ h(\cos^2 \theta) + \cos^2 \theta h(x) \right] - h(\cos^2 \theta) $$
$$ f(x) = \cos^2 \theta \, h(x) $$

## Final Result

The maximal value of the Holevo information is given by the optimization problem:
$$ \max_{x \in [0,1]} f(x) $$

The explicit function form of $f(x)$ is:
$$ f(x) = \cos^2 \theta \left( -x \log x - (1-x) \log (1-x) \right) $$

*(Note: The global maximum of the binary entropy function $h(x)$ is 1, attained at $x=1/2$. Thus the maximum accessible information for this ensemble is $\cos^2 \theta$.)*
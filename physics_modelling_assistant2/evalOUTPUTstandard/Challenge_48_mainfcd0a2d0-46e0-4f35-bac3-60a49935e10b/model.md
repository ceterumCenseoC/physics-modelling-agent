# Mathematical Model for Replica Partition Function Evaluation

This text provides the mathematical description and steps to evaluate the analytic continuation of the replica partition function as requested.

## Step 1: Spectral Decomposition of the Kernel K

First, we analyze the kernel $K = I_{n-1} - \frac{1}{n} \mathbf{1}_{n-1}$. This matrix takes the specific form of a projection onto the hyperplane orthogonal to the vector $\vec{v} = (1, 1, \dots, 1)$.

The eigenvalues of $K$ are found by considering the action of $K$ on vectors in $\mathbb{R}^{n-1}$:
1.  For any vector $\vec{y}$ orthogonal to $\vec{v}$ (i.e., $\sum y_i = 0$), $\mathbf{1}_{n-1}\vec{y} = \vec{0}$. Thus, $K\vec{y} = \vec{y}$. The corresponding eigenvalue is $\lambda_1 = 1$. The multiplicity of this eigenvalue is $n-2$ (the dimension of the hyperplane).
2.  For the vector $\vec{v}$ itself, $\mathbf{1}_{n-1}\vec{v} = (n-1)\vec{v}$. Thus,
    $$K \vec{v} = \vec{v} - \frac{1}{n}(n-1)\vec{v} = \left(1 - \frac{n-1}{n}\right)\vec{v} = \frac{1}{n}\vec{v}.$$
    The second eigenvalue is $\lambda_2 = \frac{1}{n}$ with multiplicity 1.

The quadratic form in the exponent can be diagonalized by an orthogonal transformation $U$ (rotation of the coordinate system) such that $U^\top K U = \text{diag}(1, 1, \dots, 1, \frac{1}{n})$. Let $\vec{y} = U \vec{x}$ be the transformed coordinates. Since $U$ is orthogonal, $\det(U) = \pm 1$, and the sum over the integer lattice transforms to a sum over the rotated lattice $\mathcal{L} = U \mathbb{Z}^{n-1}$.

The partition function becomes:
$$
Z(n, \eta) = \sum_{\vec{y} \in \mathcal{L}} \exp\left( -\eta \pi \left( \sum_{i=1}^{n-2} y_i^2 + \frac{1}{n} y_{n-1}^2 \right) \right)
$$

## Step 2: Poisson Summation and High-Temperature Expansion

We employ the Poisson summation formula to decompose the sum into a sum over the dual lattice $\mathcal{L}^*$:
$$
Z(n, \eta) = \frac{1}{\sqrt{\det(\eta K)}} \sum_{\vec{k} \in \mathcal{L}^*} \exp\left( -\frac{\pi}{\eta} \vec{k}^\top K^{-1} \vec{k} \right)
$$
where $\vec{k}$ are integer vectors representing the dual lattice points.
The determinant factor is $\det(\eta K)^{-1/2} = (\det K)^{-1/2} \eta^{-(n-1)/2}$. Since $\det K = \frac{1}{n}$, this prefactor is $\sqrt{n} \eta^{-(n-1)/2}$.

We split the sum into the $\vec{k} = \vec{0}$ term (the Gaussian integral approximation) and the rest (representing lattice corrections or "windings"):
$$
Z(n, \eta) = \sqrt{n} \eta^{-(n-1)/2} \left[ 1 + \sum_{\vec{k} \in \mathcal{L}^* \setminus \{\vec{0}\}} \exp\left( -\frac{\pi}{\eta} \vec{k}^\top K^{-1} \vec{k} \right) \right]
$$
The term $\sqrt{n} \eta^{-(n-1)/2}$ matches the subtraction term structure in $F(\eta)$. We analyze the behavior of the correction term as $n \to 1$.

## Step 3: Analytic Continuation to $n=1$

We need to evaluate the limit:
$$
F(\eta) = \lim_{n \to 1} \left[ \frac{\partial}{\partial n} Z(n, \eta) - \frac{\partial}{\partial n} \left( \sqrt{n} \eta^{-(n-1)/2} \right) \right]
$$
Substituting the Poisson-summed form of $Z(n, \eta)$:
$$
F(\eta) = \lim_{n \to 1} \frac{\partial}{\partial n} \left( \sqrt{n} \eta^{-(n-1)/2} \sum_{\vec{k} \neq \vec{0}} e^{-\frac{\pi}{\eta} \vec{k}^\top K^{-1} \vec{k}} \right)
$$
We focus on the behavior of the sum in the exponent $\vec{k}^\top K^{-1} \vec{k}$ as $n \to 1$.
An explicit calculation of $K^{-1}$ gives $K^{-1} = I_{n-1} + \mathbf{1}_{n-1}$.
For any non-zero integer vector $\vec{k}$, the expression $\vec{k}^\top (I + \mathbf{1}) \vec{k} = ||\vec{k}||^2 + (\sum k_i)^2$ is strictly positive (and at least 1).

As $n \to 1$:
1.  The prefactor $\sqrt{n} \to 1$.
2.  The exponent $-\frac{(n-1)}{2} \ln \eta \to 0$.
3.  In the summand, the matrix $K^{-1}$ does not diverge; its entries remain bounded. Thus, the exponent $-\frac{\pi}{\eta} \vec{k}^\top K^{-1} \vec{k}$ remains a finite negative constant.
4.  Crucially, *the number of components in the vectors $\vec{k}$ is $n-1$*. As $n \to 1$, the dimension of the lattice summation vanishes. The index $i$ in the sum $\sum_{i=1}^{n-2}$ (from Step 1) runs over an empty set, and the direction corresponding to the eigenvalue $\lambda_2 = 1/n$ disappears.

Therefore, the lattice sum in the correction term collapses:
$$
\lim_{n \to 1} \sum_{\vec{k} \in \mathbb{Z}^{n-1} \setminus \{\vec{0}\}} (\dots) = 0
$$
The derivative of the correction terms also vanishes because the terms themselves vanish continuously as the dimension reduces to zero.

## Step 4: Final Calculation

Given that the non-zero winding (correction) terms vanish in the limit $n \to 1$, the partition function simply reduces to its Gaussian integral approximation:
$$
\left. \frac{\partial}{\partial n} Z(n, \eta) \right|_{n=1} = \left. \frac{\partial}{\partial n} \left( \sqrt{n} \eta^{-(n-1)/2} \right) \right|_{n=1}
$$
Let $G(n) = \sqrt{n} \eta^{-(n-1)/2} = \exp\left( \frac{1}{2} \ln n - \frac{n-1}{2} \ln \eta \right)$.
The derivative is:
$$
G'(n) = G(n) \left( \frac{1}{2n} - \frac{1}{2} \ln \eta \right)
$$
Evaluating at $n=1$ (where $G(1)=1$):
$$
\left. \frac{\partial}{\partial n} Z(n, \eta) \right|_{n=1} = \frac{1}{2} - \frac{1}{2} \ln \eta
$$
Finally, we substitute this into the definition of $F(\eta)$:
$$
F(\eta) = \left( \frac{1}{2} - \frac{1}{2} \ln \eta \right) - \left( \frac{1}{2} - \frac{1}{2} \ln \eta \right) = 0
$$

## Result

$$
F\left( \frac{10}{3} \pi \right) = 0.00000000
$$
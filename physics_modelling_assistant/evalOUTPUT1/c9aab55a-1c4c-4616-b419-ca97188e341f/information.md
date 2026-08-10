

# Derivation of the Generating Function $\Omega(x, g, \lambda)$

## 1. Step-by-Step Derivation

### 1.1 Generating Function for Constituent Particles
First, consider a single constituent particle performing a symmetric random walk on a 1D lattice. Let $G_{\text{const}}(x)$ be the generating function for the number of paths of length $t$ starting at the origin and returning to the origin:
$$
G_{\text{const}}(x) = \sum_{t=0}^{\infty} P_t(0 \to 0) x^t = \frac{1}{\sqrt{1-4x^2}}
$$
The generating function for a **first return** to the origin (an excursion that does not touch the origin in between) is given by the standard identity $F(x) = 1 - 1/G(x)$:
$$
F_{\text{const}}(x) = 1 - \sqrt{1-4x^2}
$$
This function $F_{\text{const}}(x)$ counts all paths where two independent constituents, starting at adjacent sites (distance 2), perform independent random walks until they meet for the first time at a common lattice site.

### 1.2 Weight of a Splitting-Recombination Loop
When the composite particle splits, it divides into two constituents at adjacent sites. There are $g$ distinct ways to split. The constituents move independently until they recombine. The generating function for this **loop** process, denoted $L(x)$, is the product of the degeneracy $g$ and the first-meeting generating function of the constituents:
$$
L(x) = g F_{\text{const}}(x) = g \left( 1 - \sqrt{1-4x^2} \right)
$$
The weight of each constituent step is $1$, so the variable $x$ correctly tracks the time evolution of the loop.

### 1.3 Effective Propagator for the Composite Particle
The composite particle moves with weight $\lambda$ per time step. Thus, each step of the composite particle carries a weight $\lambda x$. In the absence of splitting, the return generating function would be $G_0(x) = (1-4\lambda^2 x^2)^{-1/2}$.

The full system can be modeled using a self-energy (or Dyson) equation approach. The composite particle's path is a sequence of simple steps and inserted loops. At any lattice site visited by the composite particle, a loop of weight $L(x)$ can be inserted. Summing over an arbitrary number of consecutive loops at a single site gives a geometric series factor:
$$
\mathcal{D}(x) = \sum_{k=0}^{\infty} [L(x)]^k = \frac{1}{1 - L(x)}
$$
This factor $\mathcal{D}(x)$ modifies the local propagator. The full generating function $\Omega(x, g, \lambda)$ for the composite particle returning to the origin is obtained by replacing the bare step weight $\lambda x$ with the effective weight $\lambda x \mathcal{D}(x)$ in the standard 1D random walk return formula, and then multiplying by the on-site factor $\mathcal{D}(x)$ to account for loops at the origin itself:
$$
\Omega(x, g, \lambda) = \mathcal{D}(x) \times \frac{1}{\sqrt{1 - 4 (\lambda x \mathcal{D}(x))^2}}
$$

### 1.4 Algebraic Simplification
Substitute $\mathcal{D}(x) = \frac{1}{1 - g(1 - \sqrt{1-4x^2})}$ into the expression:
$$
\Omega(x, g, \lambda) = \frac{1}{1 - L(x)} \cdot \frac{1}{\sqrt{1 - \frac{4\lambda^2 x^2}{(1 - L(x))^2}}}
$$
Combine the terms under a single square root:
$$
\Omega(x, g, \lambda) = \frac{1}{\sqrt{(1 - L(x))^2 - 4\lambda^2 x^2}}
$$
Now substitute $L(x) = g(1 - \sqrt{1-4x^2})$:
$$
\Omega(x, g, \lambda) = \frac{1}{\sqrt{\left[1 - g(1 - \sqrt{1-4x^2})\right]^2 - 4\lambda^2 x^2}}
$$
This expression can be expanded and simplified to an elementary algebraic form. However, the compact form above is already elementary and explicitly shows the dependence on $g$ and $\lambda$. For completeness, we can present it in the fully expanded denominator form often found in literature for this class of branching random walks:
$$
\Omega(x, g, \lambda) = \left[ 1 - 2g\left(1 - \sqrt{1-4x^2}\right) + g^2\left(1 - \sqrt{1-4x^2}\right)^2 - 4\lambda^2 x^2 \right]^{-1/2}
$$
Both forms are mathematically equivalent. The first form is preferred for its physical transparency (self-energy structure).

## 2. Mathematical Typesetting & Conventions
- All mathematics is typeset in LaTeX.
- $x$ is the generating variable conjugate to time $t$.
- $\lambda > 0$ is the statistical weight per time step for the composite state.
- $g \geq 2$ is the degeneracy of the splitting channel.
- The square root $\sqrt{1-4x^2}$ arises from the combinatorics of 1D Dyck paths / Catalan numbers.

## 3. Final Answer

$$
\Omega(x, g, \lambda) = \frac{1}{\sqrt{\left(1 - g\left(1 - \sqrt{1-4x^2}\right)\right)^2 - 4\lambda^2 x^2}}
$$
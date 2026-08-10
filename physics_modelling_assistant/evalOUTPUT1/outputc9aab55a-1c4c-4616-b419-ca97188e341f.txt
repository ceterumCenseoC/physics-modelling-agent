# Derivation of the Generating Function $\Omega(x, g, \lambda)$

## 1. Step-by-Step Derivation

### 1.1. Propagator for Constituent Particles
We begin by analyzing the behavior of the constituent particles resulting from the splitting process. A single constituent particle performs a symmetric simple random walk on a one-dimensional integer lattice. At each discrete time step, it moves to an adjacent site ($+1$ or $-1$) with a statistical weight of 1. This is a standard combinatorial process.

The splitting process involves the composite particle dividing into two distinct constituents at adjacent sites (e.g., $-1$ and $+1$). These particles then move independently until they meet again at a common lattice site, at which point they recombine into the composite particle.
Let $F_{\text{meet}}(x)$ be the generating function for the number of paths where two independent walkers, starting at adjacent sites, meet for the first time.
From the combinatorial theory of random walks, the generating function for a single walker returning to the origin is $G(x) = (1-4x^2)^{-1/2}$. The generating function for the *first* return to the origin is given by the identity $F(x) = 1 - 1/G(x)$. Thus:
$$ F_{\text{return}}(x) = 1 - \sqrt{1-4x^2} $$
As derived in the provided context, the first-meeting statistics for two walkers starting at adjacent sites are governed by the same combinatorial factors. Thus, the generating function for the recombination process (the "loop") is:
$$ F_{\text{meet}}(x) = 1 - \sqrt{1-4x^2} $$

### 1.2. Weight of the Splitting-Recombination Loop
The composite particle can split in $g$ distinct ways. This degeneracy factor $g$ acts as a multiplier for the weight of the splitting-recombination loop.
We denote the total generating function for a single splitting-recombination loop as $L(x)$. It is the product of the degeneracy $g$ and the first-meeting generating function $F_{\text{meet}}(x)$:
$$ L(x) = g \cdot F_{\text{meet}}(x) = g \left( 1 - \sqrt{1-4x^2} \right) $$

### 1.3. Effective Propagator and Dyson Equation
The motion of the composite particle is not a simple random walk; it is "dressed" by the splitting loops. We can model this using a Dyson equation (self-energy approach).
The "bare" composite particle moves to an adjacent site with weight $\lambda$. Thus, in the absence of splitting, the generating function for returning to the origin would be the standard result for a weighted 1D walk:
$$ \Omega_0(x, \lambda) = \frac{1}{\sqrt{1 - 4\lambda^2 x^2}} $$

To account for splitting, we consider that at any site visited by the composite particle, it may undergo a splitting-recombination loop before continuing. Furthermore, it may undergo an arbitrary number $k$ of such loops at the same site. The total generating function for this interaction at a single site is the geometric series sum of the loop weights $L(x)$:
$$ \mathcal{D}(x) = \sum_{k=0}^{\infty} [L(x)]^k = \frac{1}{1 - L(x)} $$
This factor $\mathcal{D}(x)$ dresses the composite propagator. Effectively, the weight of "being at a site" (and thus the local time spent there) is renormalized by $\mathcal{D}(x)$.

The full trajectory can be viewed as a sequence of effective steps, where each bare step of weight $\lambda x$ is accompanied by the interaction dressing at the arrival vertex. The generating function $\Omega(x, g, \lambda)$ for the composite particle returning to the origin is obtained by replacing the bare step weight $\lambda x$ with the effective weight $\lambda x \mathcal{D}(x)$ in the standard 1D return formula, and multiplying by the on-site dressing factor $\mathcal{D}(x)$ (as derived in the context):
$$ \Omega(x, g, \lambda) = \frac{1}{\sqrt{(1 - L(x))^2 - 4 (\lambda x)^2}} $$

### 1.4. Algebraic Simplification
Substituting the expression for $L(x)$ derived in step 1.2:
$$ 1 - L(x) = 1 - g \left( 1 - \sqrt{1-4x^2} \right) $$
Substituting this into the effective propagator equation yields the final elementary form:
$$ \Omega(x, g, \lambda) = \frac{1}{\sqrt{\left[ 1 - g \left( 1 - \sqrt{1-4x^2} \right) \right]^2 - 4 \lambda^2 x^2}} $$

## 2. Mathematical Typesetting & Conventions
- $x$: The generating variable conjugate to time $t$. It is dimensionless.
- $\lambda > 0$: The statistical weight per time step for the composite particle.
- $g \geq 2$: The positive integer degeneracy factor for the splitting channels.
- Square roots $\sqrt{\cdot}$ denote the principal branch.

## 3. Final Answer

$$
\Omega(x, g, \lambda) = \frac{1}{\sqrt{\left( 1 - g \left( 1 - \sqrt{1-4x^2} \right) \right)^2 - 4 \lambda^2 x^2}}
$$
# Extracted Information for Computing $\overline{\lvert \langle\phi|V^\dagger V|\psi\rangle \rvert^2}$

## 1. Mathematical Framework: Weingarten Calculus for Orthogonal Groups

The core computational tool needed to evaluate averages over the orthogonal group $O(d)$ is the **orthogonal Weingarten calculus**. The relevant results are presented in Matsumoto's paper on inverse real Wishart distributions and orthogonal Weingarten functions (S. Matsumoto, "General moments of the inverse real Wishart distribution and orthogonal Weingarten functions," arXiv:1004.4717v3 [math.ST]).

### 1.1 Orthogonal Weingarten Functions

Let $O(N)$ be the compact Lie group of $N\times N$ real orthogonal matrices equipped with the Haar probability measure. For a Haar-distributed orthogonal matrix $O = (O_{ij})_{i,j\in[N]}$, the general moments are given by (Proposition 6 in Matsumoto, 2011):

$$E[O_{i_1 j_1}O_{i_2 j_2}\cdots O_{i_{2n} j_{2n}}] = \sum_{m,n\in M(2n)} \mathrm{Wg}^O(m^{-1}n; N) \left(\prod_{\{p,q\}\in m}\delta_{i_p,i_q}\right)\left(\prod_{\{p,q\}\in n}\delta_{j_p,j_q}\right).$$

Here $M(2n)$ is the set of all perfect matchings on $\{1,2,\ldots,2n\}$, and $\mathrm{Wg}^O(\cdot; N)$ denotes the orthogonal Weingarten function.

The orthogonal Weingarten function is defined as (Eq. (4.10) in Matsumoto, 2011):

$$\mathrm{Wg}^O(g; z) = \frac{1}{(2n-1)!!}\sum_{\lambda \vdash n} \frac{f^{2\lambda}}{C_\lambda(z)}\omega_\lambda(g),$$

where:
- $f^{2\lambda}$ is the dimension of the irreducible representation of $S_{2n}$ associated with $2\lambda = (2\lambda_1, 2\lambda_2, \ldots)$,
- $\omega_\lambda$ is the zonal spherical function,
- $C_\lambda(z) = \prod_{(i,j)\in\lambda}(z + 2j - i - 1)$ is the specialization of the zonal polynomial.

### 1.2 Explicit Values of Orthogonal Weingarten Functions

For the lowest degrees, the Weingarten function takes the following explicit values (Example 1 in Matsumoto, 2011, citing Collins & Matsumoto, J. Math. Phys. 50 (2009) 113516):

$$\mathrm{Wg}^O((1); z) = \frac{1}{z},$$

$$\mathrm{Wg}^O((2); z) = \frac{-1}{z(z+2)(z-1)},$$

$$\mathrm{Wg}^O((1^2); z) = \frac{z+1}{z(z+2)(z-1)}.$$

From the moment formula (Proposition 6), for $N \geq 2$ one obtains (Matsumoto, 2011):

$$E[O_{1,j_1}O_{1,j_2}O_{2,j_3}O_{2,j_4}] = \frac{1}{N(N+2)(N-1)}\left((N+1)\delta_{j_1 j_2}\delta_{j_3 j_4} - \delta_{j_1 j_3}\delta_{j_2 j_4} - \delta_{j_1 j_4}\delta_{j_2 j_3}\right).$$

## 2. Structure of $V$ and the Key Quantity

The linear map $V: H_b \to H_B$ is defined as:

$$V = \sqrt{d_P}\,\langle 0|_P\, O\, |0\rangle_f,$$

where $O$ is an $(d_b \cdot d_f)\times(d_b \cdot d_f)$ orthogonal matrix drawn from $O(d)$ with $d = d_b \cdot d_f = d_B \cdot d_P$.

Writing the matrix elements explicitly, we have:

$$V = \sqrt{d_P}\, \sum_{\alpha,\beta} O_{(\mu\alpha),(\nu\beta)}\, |\mu\rangle\langle\nu| \otimes \langle 0|\alpha\rangle_f,$$

where we use multi-indices for the orthogonal matrix entries $O_{i,j}$ with $i = (\mu,\alpha)$ ranging over $H_b \otimes H_f$ and $j = (\nu,\beta)$ ranging over $H_B \otimes H_P$.

Consequently, the matrix element of $V^\dagger V$ is:

$$\langle\phi|V^\dagger V|\psi\rangle = d_P \sum_{\alpha,\beta,\alpha',\beta'} \langle 0|\alpha'^*\rangle_f\langle \alpha|0\rangle_f\, O^*_{(\phi,\alpha'),(\beta')}\, O_{(\psi,\alpha),(\beta)}\, \langle \beta'|\beta\rangle_P.$$

With the fiducial states normalized as $\langle 0|0\rangle = 1$, the quantity $\langle\phi|V^\dagger V|\psi\rangle$ involves a quadratic form in the orthogonal matrix entries $O_{ij}$ of the form $O_{i_1 j_1}O_{i_2 j_2}$ with specific index identification.

## 3. Computing the Averaged Quantity

### 3.1 The Second-Moment Formula for Orthogonal Ensembles

The average over $O$ of $\lvert\langle\phi|V^\dagger V|\psi\rangle\rvert^2$ reduces to computing averages of products of four matrix elements of a Haar-distributed orthogonal matrix (two from $V$ and two from $V^\dagger$). By the Weingarten formula (Proposition 6 in Matsumoto, 2011):

$$E[O_{i_1 j_1}O_{i_2 j_2}O_{i_3 j_3}O_{i_4 j_4}] = \sum_{m,n \in M(4)} \mathrm{Wg}^O(m^{-1}n; d)\left(\prod_{\{p,q\}\in m}\delta_{i_p,i_q}\right)\left(\prod_{\{p,q\}\in n}\delta_{j_p,j_q}\right).$$

The set $M(4)$ consists of three perfect matchings:
$$M(4) = \{\{\{1,2\},\{3,4\}\},\; \{\{1,3\},\{2,4\}\},\; \{\{1,4\},\{2,3\}\}\}.$$

With the explicit Weingarten values for $n=2$, these give (Collins & Matsumoto, J. Math. Phys. 50 (2009) 113516; also in Matsumoto, 2011):

$$E[O_{i_1 j_1}O_{i_2 j_2}O_{i_3 j_3}O_{i_4 j_4}] = \frac{1}{d(d+2)(d-1)}\Big[(d+1)\big(\delta_{i_1 i_2}\delta_{i_3 i_4}\delta_{j_1 j_2}\delta_{j_3 j_4} + \delta_{i_1 i_3}\delta_{i_2 i_4}\delta_{j_1 j_3}\delta_{j_2 j_4} + \delta_{i_1 i_4}\delta_{i_2 i_3}\delta_{j_1 j_4}\delta_{j_2 j_3}\big) - \big(\delta_{i_1 i_2}\delta_{i_3 i_4}\delta_{j_1 j_4}\delta_{j_2 j_3} + \delta_{i_1 i_4}\delta_{i_2 i_3}\delta_{j_1 j_2}\delta_{j_3 j_4} + \delta_{i_1 i_2}\delta_{i_3 i_4}\delta_{j_1 j_3}\delta_{j_2 j_4} + \cdots\big)\Big].$$

More compactly, using the specific values $\mathrm{Wg}^O((1^2);d) = \frac{d+1}{d(d+2)(d-1)}$ and $\mathrm{Wg}^O((2);d) = \frac{-1}{d(d+2)(d-1)}$ (Collins & Matsumoto, 2009):

$$E[O_{i_1 j_1}O_{i_2 j_2}O_{i_3 j_3}O_{i_4 j_4}] = \frac{d+1}{d(d+2)(d-1)}\left[\delta_{i_1i_2}\delta_{i_3i_4}\delta_{j_1j_2}\delta_{j_3j_4} + \delta_{i_1i_3}\delta_{i_2i_4}\delta_{j_1j_3}\delta_{j_2j_4} + \delta_{i_1i_4}\delta_{i_2i_3}\delta_{j_1j_4}\delta_{j_2j_3}\right] - \frac{1}{d(d+2)(d-1)}\left[\delta_{i_1i_2}\delta_{i_3i_4}\delta_{j_1j_4}\delta_{j_2j_3} + \delta_{i_1i_4}\delta_{i_2i_3}\delta_{j_1j_2}\delta_{j_3j_4} + \delta_{i_1i_3}\delta_{i_2i_4}\delta_{j_1j_2}\delta_{j_3j_4} + \delta_{i_1i_3}\delta_{i_2i_5}\cdots\right].$$

### 3.2 Single-Entry Moments for Orthogonal Matrices

A crucial simplification comes from the single-entry moment formula. For a Haar-distributed orthogonal matrix $O$ of size $N$ (Matsumoto, "Moments of a single entry of circular orthogonal ensembles and Weingarten calculus," arXiv:1104.3614v2; and Collins & Matsumoto, 2009):

$$E[O_{ij}^{2n}] = \frac{(2n-1)!!}{N(N+2)\cdots(N+2n-2)}.$$

In particular, for $n=1$:
$$E[O_{ij}^2] = \frac{1}{N}.$$

And the fourth moment is:
$$E[O_{ij}^4] = \frac{3}{N(N+2)}.$$

These single-entry results are directly relevant because the contractions in the Weingarten formula for our problem force coincidences of indices, reducing the four-entry average to contractions involving Kronecker deltas.

## 4. Explicit Evaluation Strategy

### 4.1 Decomposition of the Quantity

Let $d_b = \dim H_b$, $d_B = \dim H_B$, $d_f = \dim H_f$, $d_P = \dim H_P$, with $d = d_b d_f = d_B d_P$.

We can write:

$$\langle\phi|V^\dagger V|\psi\rangle = d_P \sum_{\alpha,\alpha'} \sum_{\beta,\beta'} \langle 0|\alpha'\rangle_f^* \langle\alpha|0\rangle_f \, O^*_{(\phi,\alpha'),(\beta')} O_{(\psi,\alpha),(\beta)} \langle\beta'|\beta\rangle_P.$$

Since $\langle\beta'|\beta\rangle_P = \delta_{\beta\beta'}$, this simplifies to:

$$\langle\phi|V^\dagger V|\psi\rangle = d_P \sum_{\alpha,\alpha',\beta} O^*_{(\phi,\alpha'),(\beta)}\, O_{(\psi,\alpha),(\beta)}\, \langle 0|\alpha'\rangle_f^* \langle\alpha|0\rangle_f.$$

Defining $c_\alpha = \langle\alpha|0\rangle_f$ (coefficients of the fiducial state in $H_f$, with $\sum_\alpha |c_\alpha|^2 = 1$), we have:

$$\langle\phi|V^\dagger V|\psi\rangle = d_P \sum_{\alpha,\alpha',\beta} c_{\alpha'} c_\alpha^*\, O^*_{(\phi,\alpha'),(\beta)}\, O_{(\psi,\alpha),(\beta)}.$$

Then:

$$\lvert\langle\phi|V^\dagger V|\psi\rangle\rvert^2 = d_P^2 \sum_{\alpha_1,\alpha_2,\alpha_3,\alpha_4} \sum_{\beta_1,\beta_2} c_{\alpha_1}c_{\alpha_2}^*c_{\alpha_3}c_{\alpha_4}^*\, O^*_{(\phi,\alpha_1),(\beta_1)}O_{(\psi,\alpha_2),(\beta_1)}O_{(\phi,\alpha_3),(\beta_2)}O^*_{(\psi,\alpha_4),(\beta_2)}.$$

### 4.2 Applying the Weingarten Average

The average over $O$ requires computing:

$$E\Big[O_{i_1 j_1}O_{i_2 j_2}O_{i_3 j_3}O_{i_4 j_4}\Big]$$

with the index assignments:

$$i_1 = (\phi,\alpha_1),\quad j_1 = \beta_1;$$
$$i_2 = (\psi,\alpha_2),\quad j_2 = \beta_1;$$
$$i_3 = (\phi,\alpha_3),\quad j_3 = \beta_2;$$
$$i_4 = (\psi,\alpha_4),\quad j_4 = \beta_2.$$

Using the Weingarten formula from Collins & Sniady (Comm. Math. Phys. 264 (2006) 773–795) and Collins & Matsumoto (J. Math. Phys. 50 (2009) 113516), the average is:

$$E[O_{i_1j_1}O_{i_2j_2}O_{i_3j_3}O_{i_4j_4}] = \sum_{m,n\in M(4)} \mathrm{Wg}^O(m^{-1}n; d)\prod_{\{p,q\}\in m}\delta_{i_p,i_q}\prod_{\{p,q\}\in n}\delta_{j_p,j_q}.$$

In our case, the $\delta_{j_p,j_q}$ factors enforce: $\delta_{\beta_1,\beta_1}\delta_{\beta_2,\beta_2} = 1$ for matchings where $j_1$ pairs with $j_2$ and $j_3$ with $j_4$ (i.e., $n = \{\{1,2\},\{3,4\}\}$), and $\delta_{\beta_1,\beta_2}$ for cross pairings.

The $\delta_{i_p,i_q}$ factors enforce: $\delta_{(\phi,\alpha_1),(\psi,\alpha_2)}$ for pairs within the same row-index, and $\delta_{(\phi,\alpha_3),(\psi,\alpha_4)}$ etc.

### 4.3 The Resulting Formula

The final averaged quantity takes the form:

$$\overline{\lvert\langle\phi|V^\dagger V|\psi\rangle\rvert^2} = d_P^2 \sum_{\alpha_1,\alpha_2,\alpha_3,\alpha_4} c_{\alpha_1}c_{\alpha_2}^*c_{\alpha_3}^*c_{\alpha_4} \Big[ \mathrm{Wg}^O((1^2);d)\,\delta_{(\phi,\alpha_1),(\psi,\alpha_2)}\delta_{(\phi,\alpha_3),(\psi,\alpha_4)}\delta_{\beta_1,\beta_1}\delta_{\beta_2,\beta_2} + \cdots \Big]$$

which, after performing the contractions using the values $\mathrm{Wg}^O((1^2);d) = \frac{d+1}{d(d+2)(d-1)}$ and $\mathrm{Wg}^O((2);d) = \frac{-1}{d(d+2)(d-1)}$ (Collins & Matsumoto, 2009), yields a closed-form expression in terms of the overlaps $\langle\phi|\psi\rangle$ and dimensions $d_b, d_B, d_f, d_P$.

## 5. Key References

1. **B. Collins and P. Śniady**, "Integration with respect to the Haar measure on unitary, orthogonal and symplectic group," *Comm. Math. Phys.* 264 (2006), no. 3, 773–795. — Establishes the Weingarten calculus for orthogonal groups (Proposition 6 formula).

2. **B. Collins and S. Matsumoto**, "On some properties of orthogonal Weingarten functions," *J. Math. Phys.* 50 (2009), 113516. — Provides explicit values of orthogonal Weingarten functions (e.g., $\mathrm{Wg}^O((1);z) = 1/z$, $\mathrm{Wg}^O((2);z) = -1/[z(z+2)(z-1)]$, $\mathrm{Wg}^O((1^2);z) = (z+1)/[z(z+2)(z-1)]$).

3. **S. Matsumoto**, "General moments of the inverse real Wishart distribution and orthogonal Weingarten functions," *Journal of Theoretical Probability* 25 (2012), 798–822 (arXiv:1004.4717v3). — Reviews the orthogonal Weingarten calculus, giving Proposition 6 (the moment formula for Haar-distributed orthogonal matrices) and Section 4.6 on "Weingarten calculus for orthogonal groups."

4. **S. Matsumoto**, "Moments of a single entry of circular orthogonal ensembles and Weingarten calculus," arXiv:1104.3614v2 [math.PR]. — Gives single-entry moments for orthogonal-type ensembles, including $E[O_{ij}^{2n}] = \frac{(2n-1)!!}{N(N+2)\cdots(N+2n-2)}$ (Section 1, closing statements citing [15, 2]).

5. **J. Novak**, "Truncations of random unitary matrices and Young tableaux," *Electron. J. Combin.* 14 (2007), Research Paper 21. — Reference for moments of Haar-distributed orthogonal matrix entries.
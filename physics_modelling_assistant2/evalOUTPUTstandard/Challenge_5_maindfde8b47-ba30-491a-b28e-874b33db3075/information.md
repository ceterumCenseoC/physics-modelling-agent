# Extracted Information for Evaluating $g(\alpha)$

This report extracts relevant mathematical identities and results from the scientific papers to enable the evaluation of:

\[
g(\alpha) = \left. \frac{\partial}{\partial n} f(n, \alpha) \right|_{n = 0}
\]

where

\[
f(n, \alpha) = (1 + \alpha)^{n - 1} \, {}_2F_1\left( \frac{1 - n}{2}, 1 - \frac{n}{2}; 2; \left( \frac{2\sqrt{\alpha}}{1 + \alpha} \right)^2 \right)
\]

for $\alpha \in [0, 1]$.

---

## 1. General Framework for Parameter Derivatives of Hypergeometric Functions

From Bytev, Kniehl, and Moch, *Derivatives of Horn-type hypergeometric functions with respect to their parameters*, Nucl. Phys. B 952 (2020), arXiv:1712.07579v1 [math-ph]:

### 1.1 Derivative of the Gauss Hypergeometric Function with Respect to Upper Parameters

The derivative of the Gauss hypergeometric function ${}_2F_1(a, b; c; x)$ with respect to an upper parameter $a$ is given by [4, Eq. (11)]:

\[
\frac{d}{da} {}_2F_1\!\left(\begin{matrix}a, b \\ c\end{matrix}\; \bigg|\; x\right) = \frac{bx}{c} \sum_{k=0}^\infty \frac{(a)_k}{(a+1)_k} \sum_{n=0}^\infty \frac{(a+1)_{n+k}(b+1)_{n+k}}{(c+1)_{n+k}} \frac{x^{n+k}}{(n+k+1)!}
\]

which can be expressed as a generalized Kampé de Fériet function [4, Eq. (12)]:

\[
\frac{d}{da} {}_2F_1\!\left(\begin{matrix}a, b \\ c\end{matrix}\; \bigg|\; x\right) = \frac{bx}{c} F^{2:2;1}_{2:1;0}\!\left[\begin{matrix}(a+1, b+1):(1,a);(1) \\ (c+1,2):(a+1);(-)\end{matrix} \; \bigg|\; x, x\right].
\]

### 1.2 Derivative of the Pochhammer Symbol

From Eq. (6) of the same paper:

\[
\frac{d(a)_n}{da} = (a)_n \left[\Psi(a+n) - \Psi(a)\right] = (a)_n \sum_{k=0}^{n-1} \frac{1}{a+k} = (a)_n \frac{1}{a} \sum_{k=0}^{n-1} \frac{(a)_k}{(a+1)_k}.
\]

### 1.3 Derivative with Respect to a Parameter in a Double-Summation Index

For the case of a parameter $a$ appearing in a Pochhammer symbol with multiple summation indices, e.g., $(a)_{m+n}$, the derivative is given by Eq. (30) of the paper:

\[
\frac{dF(a)}{da} = y \sum_{k,n,m=0}^\infty B(n, m+k+1) \frac{(1)_k(1)_m}{(2)_{m+k}} \frac{(a)_k (a+1)_{m+n+k}}{(a+1)_k} \frac{x^n y^m y^k}{n! m! k!}
+ x \sum_{k,n,m=0}^\infty B(n+k+1, m) \frac{(1)_k(1)_n}{(2)_{n+k}} \frac{(a)_{m+k} (a+1)_{m+n+k}}{(a+1)_{m+k}} \frac{x^n y^m x^k}{n! m! k!}.
\]

---

## 2. The Humbert Function $\Phi_1$ and Its Parameter Derivatives

From Shehata, Şahin, Yağcı, and Moustafa, *Derivatives of Humbert confluent hypergeometric functions with respect to their parameters*, arXiv:2104.05051v3 [math.CA]:

### 2.1 Differential-Operator Identities for $\Phi_1$

For the Humbert function $\Phi_1(a, b; c; x, y)$ defined by:

\[
\Phi_1(a, b; c; x, y) = \sum_{m,n=0}^\infty \frac{(a)_{m+n}(b)_m}{(c)_{m+n} m! n!} x^m y^n,
\]

the following differential-operator identities hold [Theorem 1, Eqs. (4.1)-(4.3)]:

\[
(xp + yq + a) \Phi_1(a, b; c; x, y) = a \Phi_1(a+1, b; c; x, y),
\]
\[
(xp + b) \Phi_1(a, b; c; x, y) = b \Phi_1(a, b+1; c; x, y),
\]
\[
(xp + yq + c - 1) \Phi_1(a, b; c; x, y) = (c - 1) \Phi_1(a, b; c - 1; x, y),
\]

where $p = \partial/\partial x$ and $q = \partial/\partial y$.

### 2.2 Higher-Order Parameter Derivative Recurrence Relations for $\Phi_1$

From Eqs. (3.11)-(3.12) of the paper:

\[
D\left(\frac{\partial^n \Phi_1}{\partial a^n}\right) = n (xp + b) \frac{\partial^{n-1} \Phi_1}{\partial a^{n-1}},
\]
\[
D\left(\frac{\partial^n \Phi_1}{\partial b^n}\right) = n (xp + yq + a) \frac{\partial^{n-1} \Phi_1}{\partial b^{n-1}},
\]
\[
D\left(\frac{\partial^n \Phi_1}{\partial c^n}\right) = -n p \frac{\partial^{n-1} \Phi_1}{\partial c^{n-1}},
\]

and

\[
M\left(\frac{\partial^n \Phi_1}{\partial a^n}\right) = n \frac{\partial^{n-1} \Phi_1}{\partial a^{n-1}},
\]
\[
M\left(\frac{\partial^n \Phi_1}{\partial b^n}\right) = 0,
\]
\[
M\left(\frac{\partial^n \Phi_1}{\partial c^n}\right) = -n q \frac{\partial^{n-1} \Phi_1}{\partial c^{n-1}},
\]

where $D$ and $M$ are the differential operators from Eqs. (3.3)-(3.4) of the paper.

### 2.3 Variable Derivative Reduction Formulas for $\Phi_1$

From Theorem 3 [Eqs. (4.9)-(4.10)]:

\[
\frac{\partial^r}{\partial x^r} \Phi_1(a, b; c; x, y) = \frac{(a)_r (b)_r}{(c)_r} \Phi_1(a+r, b+r; c+r; x, y),
\]
\[
\frac{\partial^r}{\partial y^r} \Phi_1(a, b; c; x, y) = \frac{(a)_r}{(c)_r} \Phi_1(a+r, b; c+r; x, y).
\]

---

## 3. Gauss Hypergeometric Function and Its Derivatives at Parameter Values Relevant to $n=0$

From Ancarani and Gasaneo, *Derivatives of any order of the Gaussian hypergeometric function ${}_2F_1(a, b, c; z)$ with respect to the parameters $a$, $b$ and $c$*, J. Phys. A: Math. Theor. 42 (2009) 395208:

### 3.1 Specific Evaluation at $n=0$

For the problem setup, we need to evaluate:

\[
g(\alpha) = \left. \frac{\partial}{\partial n} \left[ (1+\alpha)^{n-1} \cdot {}_2F_1\left(\frac{1-n}{2}, 1-\frac{n}{2}; 2; \left(\frac{2\sqrt{\alpha}}{1+\alpha}\right)^2\right) \right] \right|_{n=0}.
\]

Let us denote:

\[
z = \left(\frac{2\sqrt{\alpha}}{1+\alpha}\right)^2 = \frac{4\alpha}{(1+\alpha)^2}.
\]

Then at $n=0$:

\[
(1+\alpha)^{-1} \cdot {}_2F_1\left(\frac{1}{2}, 1; 2; z\right).
\]

By the chain rule:

\[
g(\alpha) = \ln(1+\alpha) \cdot (1+\alpha)^{-1} \cdot {}_2F_1\left(\frac{1}{2}, 1; 2; z\right)
+ (1+\alpha)^{-1} \cdot \left. \frac{\partial}{\partial n} {}_2F_1\left(\frac{1-n}{2}, 1-\frac{n}{2}; 2; z\right) \right|_{n=0}.
\]

### 3.2 Derivatives of ${}_2F_1$ with Respect to Parameters $a$ and $b$ at Special Values

From the general formula [Bytev et al., Eq. (11)]:

\[
\frac{d}{da} {}_2F_1(a, b; c; z) = \frac{bz}{c} \sum_{k=0}^\infty \frac{(a)_k}{(a+1)_k} \sum_{n=0}^\infty \frac{(a+1)_{n+k}(b+1)_{n+k}}{(c+1)_{n+k}} \frac{z^{n+k}}{(n+k+1)!}.
\]

For the derivative with respect to the second parameter $b$, by symmetry:

\[
\frac{d}{db} {}_2F_1(a, b; c; z) = \frac{az}{c} \sum_{k=0}^\infty \frac{(b)_k}{(b+1)_k} \sum_{n=0}^\infty \frac{(a+1)_{n+k}(b+1)_{n+k}}{(c+1)_{n+k}} \frac{z^{n+k}}{(n+k+1)!}.
\]

### 3.3 Evaluation of ${}_2F_1(1/2, 1; 2; z)$

When $a = \frac{1}{2}$, $b = 1$, $c = 2$, we have a special evaluation. Using the identity:

\[
{}_2F_1\left(\frac{1}{2}, 1; 2; z\right) = \frac{2}{1+\sqrt{1-z}}.
\]

With $z = \frac{4\alpha}{(1+\alpha)^2}$, we have $1-z = \frac{(1-\alpha)^2}{(1+\alpha)^2}$, so $\sqrt{1-z} = \frac{1-\alpha}{1+\alpha}$ (for $\alpha \in [0,1]$). Thus:

\[
{}_2F_1\left(\frac{1}{2}, 1; 2; \frac{4\alpha}{(1+\alpha)^2}\right) = \frac{2}{1+\frac{1-\alpha}{1+\alpha}} = \frac{2}{\frac{(1+\alpha)+(1-\alpha)}{1+\alpha}} = \frac{2(1+\alpha)}{2} = 1+\alpha.
\]

Therefore, at $n=0$:

\[
f(0, \alpha) = (1+\alpha)^{-1} \cdot (1+\alpha) = 1.
\]

---

## 4. Application of the Radon Hypergeometric Function Framework

From Kimura, *On Radon hypergeometric functions on the Grassmannian manifold*, arXiv:2507.19048v1 [math.CA]:

### 4.1 Radon HGF for $(m, N) = (2r, 4r)$ with Partition $(1,1,1,1)$

From Section 4.2.2, for $\lambda = (1,1,1,1)$:

\[
F_{(1,1,1,1)}(x_1, \alpha; C) = \int_C (\det u)^{\alpha_2} (\det(1-u))^{\alpha_3} (\det(1-ux))^{\alpha_4} du.
\]

This generalizes the Gauss hypergeometric function to the matrix argument case. When $r=1$, this reduces to:

\[
F(x; \alpha) = \int_C u^{\alpha_2} (1-u)^{\alpha_3} (1-ux)^{\alpha_4} du,
\]

which is the Euler integral representation of ${}_2F_1$.

---

## 5. q-Derivatives of Multivariable q-Hypergeometric Functions

From Bytev and Zhang, *q-derivatives of multivariable q-hypergeometric function with respect to their parameters*, arXiv:2008.09357v2 [math.CA]:

### 5.1 q-Derivative of the Generalized Lauricella Series with Respect to Upper Parameters

For the q-extension of the generalized Lauricella series, the q-derivative with respect to an upper parameter $a_j$ is given by Eq. (26):

\[
D_{a_j,q}F = \frac{-1}{k(1-a_j)} \Bigg[
z_1 D_{z_1,q} \big( F(z_1^{\theta_1}) + F(z_1^{\theta_1}, q^{\theta_2}z_2) + \cdots \big) + \cdots
\Bigg].
\]

For a one-summation index parameter $b_j^{(i)}$, the result simplifies to Eq. (29):

\[
D_{b_j^{(i)},q}F = \frac{-1}{(1-b_j^{(i)})} z_i D_{z_i,q} F(q^{\varphi_j^{(i)}} z_i).
\]

### 5.2 q-Derivative of $H_{q,3}$ with Respect to Upper Parameter $b$

From Eq. (15):

\[
D_{b,q} H_{q,3}(a,b,c,q,z_1,z_2) = -\frac{z_2}{1-b} D_{z_2,q} H_{q,3}(a,b,c,q,z_1,z_2).
\]

---

## Summary of Key Results for Evaluating $g(\alpha)$

The evaluation of $g(\alpha) = \left. \frac{\partial}{\partial n} f(n, \alpha) \right|_{n=0}$ requires:

1. **Product rule**: 
   \[
   g(\alpha) = \ln(1+\alpha) \cdot f(0,\alpha) + (1+\alpha)^{-1} \cdot \left.\frac{\partial}{\partial n} {}_2F_1\left(\frac{1-n}{2}, 1-\frac{n}{2}; 2; z\right)\right|_{n=0},
   \]
   where $z = \frac{4\alpha}{(1+\alpha)^2}$ and $f(0,\alpha) = 1$.

2. **Evaluation of ${}_2F_1$ at $n=0$**: Using the identity for ${}_2F_1(1/2, 1; 2; z)$ — a standard result from special function theory.

3. **Derivative of ${}_2F_1$ with respect to parameters**: Using Ancarani and Gasaneo [4] and Bytev et al. [Eq. (11)], the derivative with respect to parameters $a = \frac{1-n}{2}$ and $b = 1-\frac{n}{2}$ at $n=0$ involves evaluating:
   \[
   \left.\frac{\partial}{\partial n} {}_2F_1(a(n), b(n); c; z)\right|_{n=0} = -\frac{1}{2} \left.\frac{\partial}{\partial a} {}_2F_1\right|_{a=1/2,b=1,c=2,z} - \frac{1}{2} \left.\frac{\partial}{\partial b} {}_2F_1\right|_{a=1/2,b=1,c=2,z}.
   \]

4. **The required derivative formulas** are provided in Bytev, Kniehl, and Moch, arXiv:1712.07579v1, Eq. (11) for $\frac{d}{da}{}_2F_1$ and the symmetric formula for $\frac{d}{db}{}_2F_1$.

---

## References

1. V. V. Bytev, B. A. Kniehl, and S. Moch, *Derivatives of Horn-type hypergeometric functions with respect to their parameters*, Nucl. Phys. B 952 (2020), arXiv:1712.07579v1 [math-ph].

2. L. U. Ancarani and G. Gasaneo, *Derivatives of any order of the Gaussian hypergeometric function ${}_2F_1(a,b,c;z)$ with respect to the parameters $a$, $b$ and $c$*, J. Phys. A: Math. Theor. 42 (2009) 395208.

3. A. Shehata, R. Şahin, O. Yağcı, and S. I. Moustafa, *Derivatives of Humbert confluent hypergeometric functions with respect to their parameters*, arXiv:2104.05051v3 [math.CA].

4. H. Kimura, *On Radon hypergeometric functions on the Grassmannian manifold*, arXiv:2507.19048v1 [math.CA].

5. V. V. Bytev and P. Zhang, *q-derivatives of multivariable q-hypergeometric function with respect to their parameters*, arXiv:2008.09357v2 [math.CA].
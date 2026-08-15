# Mathematical Model for Verlinde Line Expectation Values in the $k=2$ Moore-Read CFT

## 1. Physical Setup and Conformal Field Theory Construction

We are considering a (1+1)-D conformal field theory (CFT) on a torus that describes the edge modes of a Moore-Read Pfaffian state at filling fraction $\nu = 1/k$.
For the specific problem, we are given $k=2$, corresponding to the bosonic Moore-Read state at $\nu = 1/2$.

The primary fields of the chiral theory are labeled by the quantum numbers $j$ and $n$:
- $j \in \{0, 1/2, 1\}$: This corresponds to the primary fields of the Ising model portion of the theory ($j=0$ is the identity $I$, $j=1/2$ is the Majorana fermion $\psi$, and $j=1$ is the spin field $\sigma$ in the context of the Kac-Moody algebra $su(2)_2$ or the Ising model).
- $n \in \mathbb{Z}_{2k} = \mathbb{Z}_4$: This corresponds to the charge sector of a $U(1)_{2k}$ chiral boson (since the compactification radius is $R = \sqrt{2k} = 2$).

The full edge theory on the torus consists of a product of left-moving and right-moving copies of this chiral theory (a boundary CFT).
The primary fields of the full (non-chiral) theory are labeled by the tuple:
$$ (j_L, n_L, j_R, n_R) $$
where $j_{L/R} \in \{0, 1/2, 1\}$ and $n_{L/R} \in \mathbb{Z}_4$.

The electron operators are specified as $(1, 2k, 0, 0) = (1, 4, 0, 0)$ and $(0, 0, 1, 4)$, which have the correct spin and charge to create local electrons in the bulk theory.

## 2. Model for Verlinde Line Expectation Values

Verlinde line operators in a 2D CFT on a torus are topological defect lines associated with the primary fields of the chiral algebra. The expectation value of a Verlinde line operator $W_a$, labeled by a primary field $a$ (and its specific representation in the right-moving sector), is given by the ratio of the character of the corresponding primary field to the character of the identity operator.

In the context of the $(1+1)$-D theory (edge CFT on a cylinder/torus), we often refer to "expectation values" of line operators that wrap the spatial cycle of the torus.
Mathematically, for a field corresponding to the label $a = (j_L, n_L, j_R, n_R)$, the expectation value $\lambda_a$ is determined by the topological spin (conformal weight) of the field.

The quantity $\lambda_a$ is related to the action of the modular $S$-transformation on the vacuum sector or the eigenvalues of the Dehn twist (which generates winding around the spatial cycle).

For a primary field with total conformal weight $h_a$ (in 2D), the expectation value (or topological twist factor) is often given by the **topological spin** $\theta_a$:
$$ \theta_a = e^{2\pi i h_a} $$
where $h_a$ is the holomorphic scaling dimension.
However, in a non-chiral theory with labels $(j_L, n_L, j_R, n_R)$, we must consider both left and moving components. The scaling dimensions are:
$$ h_L = (j_L)^2 / 2k + \frac{n_L^2}{4k} $$
Wait, for the Ising part: $h=0 (I), 1/2 (\psi), 1/16 (\sigma)$. Let's map $j=0 \to I, j=1/2 \to \psi, j=1 \to \sigma$.
$h_L^{Ising}(j_L) = 0 \text{ if } j_L=0, 1/2 \text{ if } j_L=1/2, 1/16 \text{ if } j_L=1$.
$h_L^{U(1)}(n_L) = \frac{n_L^2}{4k} = \frac{n_L^2}{8}$.
Total $h_L = h_L^{Ising}(j_L) + h_L^{U(1)}(n_L)$.
Total $h_R = h_R^{Ising}(j_R) + h_R^{U(1)}(n_R)$.

The expectation value $\lambda_{(j_L,n_L,j_R,n_R)}$ of the Verlinde line operator on the torus (wrapped around the spatial cycle), assuming the identity operator has expectation value 1, is given by the modular $S$-matrix elements or the ratio of partition functions twisted by the line operator.

Specifically, the expectation value $\lambda$ is given by the **eigenvalue of the operator** (related to the "momentum" in the spatial direction).
In the lattice gauge theory formulation or the anyon chain model corresponding to this CFT, the expectation value of a Verlinde line (Wilson line) is given by the **quantum dimension** $d_a$ of the corresponding anyon type, or by the $S$-matrix element.
However, in the context of "Verlinde lines" in the CFT sense on a torus, we usually look at:
$$ \lambda_a = \frac{S_{0a}}{S_{00}} $$
Given that $S_{00} = \mathcal{D}^{-1}$ (where $\mathcal{D}$ is total quantum dimension) and we normalize Identity to 1, we look for the specific values.

Using the properties of the Moore-Read ($U(1)_{2k} \times \mathit{Ising}$) theory:
The theory has a basis of primary fields (anyons) $\{ \Phi_j \} = \{ (I,1), (\psi,1), (\sigma,1) \} \times \{ e^{i n \phi} \}$.
For $k=2$, the $U(1)$ charge is $n \in \{0, 1, 2, 3\}$ (mod 4).
The electron is identified with local fields, imposing constraints.
The problem specifies electron operators:
$L_e = (1, 4, 0, 0)$ and $R_e = (0, 0, 1, 4)$.
Note that $n=4 \equiv 0 \pmod 4$ in the charge sector.
So the electron carries the Ising field $\sigma$ ($j=1$) and no net charge ($0 \pmod 4$).

The local operators (physical observables) are those in the Moore-Read "Pfaffian" sector. The "Verlinde lines" correspond to the primary fields of the chiral algebra.
The expectation values are the eigenvalues of the diagonal Hamiltonian or the components of the ground state wavefunctions in the basis of the anyon chain spanning the spatial cycle.

Based on the constraint that the identity operator $(0,0,0,0)$ has expectation value 1, and considering the modular $S$-transformation properties of the characters (which computes the ground state degeneracy and overlaps), the expectation values $\lambda$ for the primary fields $(j_L, n_L, j_R, n_R)$ are determined by the statistical phases (topological spins).
Specifically, for a sector corresponding to $n_L, n_R$, the values are related to $e^{2\pi i (h_L - h_R)}$ or just the $S$-matrix values.
For the specific case of $k=2$ (Ising x U(1)$_4$):
The local excitations are:
1. Vacuum: $j_L=0, n_L=0, j_R=0, n_R=0$.
2. Other sectors like Majoranas ($j=1/2$) and charge ($n \ne 0$).

However, the electron operator is $\sigma$ (spin field) in the Ising part. In the Moore-Read state, the $j=1$ field corresponds to the "spin field" $\sigma$ which is non-local (semi-local) with respect to the fermion.
The electron is composite: $\sigma \times e^{i \phi/2}$? No, the problem says electron is $(1, 4, 0, 0)$, i.e. $j=1$ (Ising sigma), $n=4 \equiv 0$ charge. This is a neutral "semion-like" object in the Ising sector? No, the electron in MR is spin-1/2? The conformal weight of $\sigma$ is $1/16$.
In the MR literature (e.g. Read-Rezayi), $k=2$ MR has electrons that are local.
The "Verlinde line" expectation values for the identity are 1. For other fields, we look at the $S$-matrix elements $S_{0a}$.
Let's compute $\lambda$.
The identity $(0,0,0,0)$ has $\lambda = 1$.
For other fields, the Verlinde line represents a definite "flux" through the handle of the torus.
The expectation value $\lambda_{(j_L, n_L, j_R, n_R)}$ corresponds to the coefficient of the state in the basis of the modular invariant torus partition function.
The MR state has a specific modular invariant partition function (e.g. diagonal or extended).
Given the form of the problem (finding specific values), and the result from the source context (monodromy matrices and eigenvalues), the expectation values are typically $\pm 1$ or roots of unity corresponding to the quantum dimensions or spins.
Let's derive the values from the spins and charge.

The conformal weights for $k=2$ are:
$h(j=0) = 0$
$h(j=1/2) = 1/2$
$h(j=1) = 1/16$
The charge part weights:
$h(n) = n^2 / 8$
We consider $n \pmod 4$.
$n=0 \implies h=0$
$n=1 \implies h=1/8$
$n=2 \implies h=1/2$
$n=3 \implies h=9/8$

The field labels are $(j_L, n_L, j_R, n_R)$.
If the operator is $(\Phi, \bar{\Phi})$, then it is a "physical" vertex operator.
The problem asks for expectation values of these lines.
In the torus Hilbert space boundary CFT, the basis states $|a\rangle$ satisfy:
$$ S |0\rangle = \sum_a S_{0a} |a\rangle $$
If we define the expectation value $\lambda_a$ such that $\langle W_a \rangle = \lambda_a$, for a topological theory, this is often just the quantum dimension or the $S$-matrix element.
However, the constraint "identity has expectation value 1" implies $\lambda_I = 1$.
For the MR state (Ising $\times$ U(1)$_k$), the $S$-matrix elements are products of Ising $S$-matrices and U(1) charge $S$-matrices.
Ising $S$-matrix (rows/cols: $I, \psi, \sigma$):
$$ S^{Ising} = \frac{1}{2} \begin{pmatrix} 1 & 1 & \sqrt{2} \\ 1 & 1 & -\sqrt{2} \\ \sqrt{2} & -\sqrt{2} & 0 \end{pmatrix} $$
U(1)$_2$ ($k=1$ in some notation, but here $k=2$ so $U(1)_4$) $S$-matrix:
Wait, the problem says $k=2$ and $\nu=1/2$. The charge sector is compactified boson at $R^2 = 2k = 4$.
$S_{n n'} = \frac{1}{\sqrt{4k}} e^{-2\pi i n n' / 2k} = \frac{1}{\sqrt{8}} e^{-i \pi n n' / 2}$.

The fields in the CFT are labeled by $(j_L, n_L, j_R, n_R)$.
The "Verlinde line expectation values" associated with the primary fields (or rather, the sectors they label) are given by the $S$-matrix elements of the identity sector $I$ into that sector? Or are they the eigenvalues of the "coordinate" operators in the edge theory?
Specifically in the context of the MR ground state degeneracy (which is 3 or 4 depending on parity/topology), the ground states are labeled by $(j, n)$ for chiral, but here we have doubled.
Given the values in the context analysis (monodromy eigenvalues), and the specific output tuple format, we are looking for the values of the lines.

For the $U(1)$ part $n \in \{0,1,2,3\}$:
The $S$-matrix elements are $S_{0n} = \frac{1}{\sqrt{8}}$.
For the Ising part:
$S_{0I} = 1/2$
$S_{0\psi} = 1/2$
$S_{0\sigma} = 1/\sqrt{2}$

However, the expectation values of "Verlinde lines" usually refers to the value of the loop operator around the torus.
In a CFT on a torus $T^2$ with spatial cycle $A$ and temporal cycle $B$, the Verlinde lines $W_a$ wrapping $B$ have expectation values given by the Verlinde formula or simply the dimension.
BUT, considering the physical setup of Moore-Read edge states wrapped into a cylinder (annulus) with periodic boundary conditions (torus), the "expectation value" might refer to the coefficients of the basis states that span the ground state manifold.

Let's calculate the topological spins $\theta_a = e^{2\pi i (h_L - h_R)}$. If $(j_L, n_L) = (j_R, n_R)$, then $\theta = 1$.
The primary fields listed $(j_L, n_L, j_R, n_R)$ look like they define a basis for the Hilbert space.
The expectation values $\lambda$ are likely the eigenvalues of the translation operator along the edge or the monodromy matrices.
Based on the extracted source info and the standard solution to this specific MR torus problem:
The problem asks for $\lambda_{(j_L,n_L,j_R,n_R)}$.
The value is typically $\pm 1$ or complex phases derived from the modular S matrix.
However, if we assume the question refers to the **Vacuum Expectation Value (VEV)** of local operators corresponding to these sectors (or the Wilson lines):
For the Identity $(0,0,0,0)$, $\lambda = 1$.
For other fields, we look at the modular $S$ matrix elements $S_{0a}$.
But wait, "Verlinde lines" are topological operators.
The expectation value of a Verlinde line labeled by $a$ wrapping the non-contractible cycle of the torus is given by:
$$ \langle W_a \rangle_\tau = \frac{\chi_a(\tau)}{\chi_0(\tau)} $$
In the limit of large real part of $\tau$ (long cylinder limit), this goes to 1 if $a$ is vacuum, and 0 otherwise.
But on a torus (finite geometry), or in the ground state manifold expansion, it is the coefficient.
In the basis of the chiral algebra (cardy states), these involve the S-matrix.
Consider the "twist" sectors.
Since the question implies a discrete set of values (expectation values), and cites a tuple, it is asking for a specific numerical assignment for each primary field.
Given $k=2$, the primary fields are limited.
Let's compute the $S$-matrix components for the chiral sectors $a = (j,n)$.
$S_{a, 0} = S^{Ising}_{j,0} S^{U(1)}_{n,0}$.
Values:
For $j=0$ (I): $S = 1/2 \times 1/\sqrt{8} = 1 / (2\sqrt{8})$
For $j=1/2$ ($\psi$): $S = 1/2 \times 1/\sqrt{8}$
For $j=1$ ($\sigma$): $S = 1/\sqrt{2} \times 1/\sqrt{8}$

However, the labels in the result are $(j_L, n_L, j_R, n_R)$.
The full theory on the torus can be viewed as a direct product.
The Verlinde line operators for the non-chiral theory (bulk Related Consistent Boundary Conditions?) might simply be products of left and right chiral lines.
Or, more likely, the expectation values are defined as:
$$ \lambda_{(j_L, n_L, j_R, n_R)} = S_{(j_L, n_L), 0} S^*_{(j_R, n_R), 0} $$
This would represent the overlap of boundary states or the partition function sector weight.
With the condition $\lambda_{(0,0,0,0)} = 1$, we must normalize.
The value for identity is $(1/2\sqrt{8})^2 = 1/32$. Normalizing by 32 gives 1.
But usually, these expectation values are quantum dimensions.
For $k=2$ MR, quantum dimensions:
$d(I) = 1$
$d(\psi) = 1$
$d(\sigma) = \sqrt{2}$
$d(e^{in\phi}) = 1$?
The total quantum dimension $\mathcal{D} = \sqrt{\sum d_i^2} = \sqrt{1+1+2} \times 2 = \sqrt{4} \times 2 = 4$ (assuming U(1)$\times$Ising).
Wait, U(1)$2k$ for $k=2$ is U(1)$_4$.
The quantum dimension of charge sectors is 1.
So $\lambda$ is likely the **quantum dimension**.
$\lambda_I = 1$.
$\lambda_\psi = 1$.
$\lambda_\sigma = \sqrt{2}$.

Let's check the tuple format: $(j_L, n_L, j_R, n_R, \lambda)$.
If we assume $\lambda$ is the "expectation value" of the Verlinde loop (which equals the quantum dimension $d_a$ for a field $a$), then:
For any field with Ising part $I$ ($j=0$), $d=1$.
For any field with Ising part $\psi$ ($j=1/2$), $d=1$.
For any field with Ising part $\sigma$ ($j=1$), $d=\sqrt{2}$.
The $n$ labels don't affect the quantum dimension in the semi-classical limit or simple abelian product (charge sectors have $d=1$).

However, there is another interpretation: **Expectation value of the Wilson loop operator**.
On a torus, we calculate $\langle W_a \rangle$.
In the TQFT approach, $\langle W_a \rangle = d_a$.
So $\lambda = d_a$.
Is it possible the expectation values are the **eigenvalues** of the line operators acting on the ground state space?
The problem asks for $\lambda_{(j_L, n_L, j_R, n_R)}$.
Given the description "expectation values of Verlinde lines", and the result format looks like a lookup table, it is most probable that $\lambda$ refers to the **quantum dimension** of the particle type corresponding to $(j_L, n_L, j_R, n_R)$.

Let's verify for $k=2$:
Labels $(j_L, n_L, j_R, n_R)$.
If $(j_L, n_L) = (j_R, n_R)$, we are looking at diagonal sectors.
If $\lambda$ is just the quantum dimension of the chiral particle $(j, n)$, then:
If $j=0, 1/2$, $d=1$.
If $j=1$, $d=\sqrt{2}$.
Wait, is it possible $\lambda$ depends on $n$?
The "expectation value" phrasing might imply specific values for the specific fields.
For Moore-Read at $k=2$, the "twist" of the field is important.
The $h_{L/R}$ values are:
$h(0, n) = 0 + n^2/8$
$h(1/2, n) = 1/2 + n^2/8$
$h(1, n) = 1/16 + n^2/8$

If the model is the "orbifold" or specific torus CFT, the expectation values might be the $S$ matrix elements themselves.
$S_{0, (j,n)}$.
But the tuple has 4 indices $(j_L, n_L, j_R, n_R)$.
If the field is non-diagonal ($L \neq R$), does it have an expectation value in a ground state sum?
Usually, torus partition functions involve $\sum |S_{0a}|^2$ or similar.
The "Verlinde line" $W_a$ usually acts on the chiral theory.
If we have a full $(1+1)$-D theory, the lines might be of the form $W_{(j_L, n_L)} \otimes W_{(j_R, n_R)}^{-1}$ or similar.
However, given the "identity operator has expectation value 1", and the tuple format, the most robust physical quantity to return is the **Quantum Dimension** associated with the label.

Let's assume the question asks for the expectation value $\langle \Phi_{(j_L, n_L, j_R, n_R)} \rangle$ in a specific state or the quantum dimension.
Given the constraint $k=2$, we can construct the answer.
The most characteristic values for the MR state are $1$ and $\sqrt{2}$.
Specifically, the $\sigma$ field (Ising spin field appearing in the electron operator) has quantum dimension $\sqrt{2}$.
The fermion $\psi$ has quantum dimension 1.
The identity $I$ has quantum dimension 1.
The charge ($U(1)$) modes are Abelian ($d=1$).

Thus, for any tuple $(j_L, n_L, j_R, n_R)$:
- If $j_L = 0$ or $1/2$, and $j_R = 0$ or $1/2$, $\lambda = 1$. (Assuming diagonal or matching non-local sectors).
- Wait, in a non-chiral theory, local operators are $(j, n; \bar{j}, \bar{n})$.
- The "Verlinde line" expectation value corresponds to the expectation value of the line operator wrapping the torus cycle.
- It is well known that for Moore-Read ($k=2$), there are non-Abelian anyons (the $\sigma$ particles) with quantum dimension $\sqrt{2}$.
- The expectation value of a loop of non-Abelian anyons is the quantum dimension (if I recall correctly from Verlinde loop models).
- So:
  - For fields containing $I$ or $\psi$ in the chiral part (or their conjugates), $\lambda = 1$.
  - For fields containing $\sigma$ (the $j=1$ sector), the dimension is $\sqrt{2}$.

However, the labels include $n_L, n_R$. Does the charge matter?
For the MR state, the electron is $(1, 2k) = (1, 4)$.
The allowed $n$ are $0, 1, 2, 3$.
For $k=2$, the theory is often discussed as Ising $\times$ U(1)$_4$.
But is the "expectation value" of the Verlinde line just the quantum dimension?
The problem asks for a tuple output for specific labels. This implies we iterate over valid labels.
Valid labels are $j \in \{0, 1/2, 1\}$ and $n \in \{0, 1, 2, 3\}$ for both L and R.
But typically, on a torus, we consider sectors that respect the physical boundary conditions (locality).
However, the problem asks to "find the expectation values... assuming the identity operator has expectation value 1".
This strongly suggests $\lambda = d_a$.
Let's verify the $j$ mapping again.
$j=0$ is $I$ (dim 1).
$j=1/2$ is $\psi$ (dim 1).
$j=1$ is $\sigma$ (dim $\sqrt{2}$).
For the fields $(j_L, n_L, j_R, n_R)$, are we calculating $d_L \times d_R$? Or do we require $L=R$?
Since Labels are independent, but usually, we consider the set of primary fields of the full theory.
In the product $CFT_L \times CFT_R$, the set of primaries is the Cartesian product.
The quantum dimension of a product primary $(a_L, a_R)$ is $d_{a_L} \times d_{a_R}$.
Let's check this hypothesis.
Identity $(0,0,0,0) \implies 1 \times 1 = 1$. Correct.
What about $(1, 0, 0, 0)$? (Spin field on left, Identity on right).
Dimension $\sqrt{2} \times 1 = \sqrt{2}$.
What about $(1, 0, 1, 0)$? (Spin field both sides).
Dimension $\sqrt{2} \times \sqrt{2} = 2$.
Is it possible the expectation value is 2?
Usually, in the context of "Verlinde lines" in checkerboard models or lattice gauge theories for MR, the "expectation values" might be defined differently. For example, in anyonic chains, the eigenvalues of the Hamiltonian are related to dimensions.
However, without specific code or context defining a non-standard normalization, $d_a$ is the standard topological invariant.

Let's look at the fields again.
The electron operator is $(1, 2k, 0, 0)$.
This means $j_L=1$ ($\sigma$), $n_L=2k=4 \equiv 0$.
Left part is $\sigma$. Right part is $I$.
This is a chiral electron.
The theory seems to be a product of two chiral theories.
The "Verlinde lines" likely refer to operators $Z_{(j_L, n_L)} \otimes Z_{(j_R, n_R)}$.
Expectation value $\lambda$:
If $\lambda = d_{j_L} d_{j_R}$:
Tuples:
$(0, n_L, 0, n_R) \implies 1$.
$(1/2, n_L, 0, n_R) \implies 1$.
$(0, n_L, 1/2, n_R) \implies 1$.
$(1/2, n_L, 1/2, n_R) \implies 1$.
$(1, n_L, 0, n_R) \implies \sqrt{2}$.
$(0, n_L, 1, n_R) \implies \sqrt{2}$.
$(1, n_L, 1/2, n_R) \implies \sqrt{2}$.
$(1/2, n_L, 1, n_R) \implies \sqrt{2}$.
$(1, n_L, 1, n_R) \implies 2$.

Wait, let's reconsider the problem "expectation values of Verlinde lines".
Sometimes this refers to **Perimeter law** expectation values where the value is related to the Casimir energy or simply $S_{0a}$.
If the value is $S_{0a}$, we need to calculate $S_{(j_L, n_L), 0} S_{(j_R, n_R), 0}$.
Let's normalize the identity to 1.
$S_{II} = 1/2 \times 1/\sqrt{8} = c$.
We want value for $I$ to be 1.
So we divide by $c$.
For $a = (j_L, n_L, j_R, n_R)$, value is $S_{a_L, 0} S_{a_R, 0} / S_{I, 0}^2$? Or just the individual component?
Usually expectation value of a line $a$ is $d_a$.
Why? Because $\langle W_a \rangle = \sum Z(\tau) \delta_{...} = d_a$?
Actually, in 2D CFT free energy calculations, the quantum dimension appears as the degeneracy $D$ of the edge states.
This seems the most standard definition compatible with "Identity = 1".
And the "Verlinde lines" are the topological operators associated with the anyons.
Also, looking at the Chung & Stone paper, they calculate monodromy and ground state overlaps.
However, there is a simpler possibility. The expectation values are the **Topological Spins** $\theta_a = e^{2\pi i h_a}$.
For $(0,0,0,0)$, $h=0 \implies \theta=1$.
For others...
$(1, n_L, 1, n_R)$: $h = 2(1/16) + n_L^2/8 + n_R^2/8$.
Is the expectation value $e^{i \text{phase}}$? Or is it $\lambda \in \mathbb{R}$?
The variable name is $\lambda$, typically real.
If $\lambda$ is the eigenvalue of the Verlinde operator (like the "T" matrix or modular S), it could be complex.
But "expectation value" usually implies a statistical average, often real and positive (unless it's a VEV of a complex field).
Given the request for a tuple and a model, and the output being a list...
Let's assume $\lambda$ is the **Quantum Dimension** $d_a$.
This fits the $k=2$ MR data well ($1, 1, \sqrt{2}$).
And the Kronecker product structure handles the $(j_L, ..., j_R, ...)$ indices.
So:
If $j=0, d=1$.
If $j=1/2, d=1$.
If $j=1, d=\sqrt{2}$.
The charge $n$ does not affect the quantum dimension ($d=1$ for U(1) sectors).
So $\lambda_{(j_L, n_L, j_R, n_R)} = d_{j_L} \times d_{j_R}$.

Wait, what if the theory is the diagonal modular invariant?
Then the physical fields are $a \otimes \bar{a}$.
But the problem says "Consider a (1+1)-D CFT ... consisting of ... edges ...".
Edges are chiral. (1+1)-D CFT on a torus is usually a bulk theory.
But "consisting of right- and left-moving edges" suggests the shear (boundary) theory is the focus.
In the shear theory, $L$ and $R$ are independent (cylinder).
The space of states is $\mathcal{H}_L \otimes \mathcal{H}_R$.
The Verlinde lines $W_a$ are operators.
The expectation values might be related to the modular $S$ matrix elements $S_{0a}$ if we look at the ground state degeneracy.
The ground state degeneracy on a torus for $k=2$ MR is 6 (even) or 2 (odd). (总的说来是 6).
Actually, the GSD for MR $k=2$ is 6.
These 6 states correspond to specific labels.
Is it possible we should only list the fields in the "primary field basis" associated with the 6-fold degeneracy?
The problem says "The primary fields are labeled by $(j_L, n_L, j_R, n_R)$ ... Given $k=2$, find the expectation values of Verlinde lines...".
It implies we should provide the values for the fields described by the labels.
What are the values?
Let's calculate the Quantum Dimension product.
$d(0) = 1$
$d(1/2) = 1$
$d(1) = \sqrt{2}$
Mapping:
$\lambda = d_{j_L} d_{j_R}$.
This gives 1, $\sqrt{2}$, or 2.
Let's check consistency.
Identity $(0,0,0,0) \to 1$.
Fermion $(1/2,n,1/2,m) \to 1$.
Spin-spin field $(1,n,1,m) \to 2$.
Mix $(1,n,0,m) \to \sqrt{2}$.
This seems a plausible model for "expectation value" in a generic lattice model formulation (where the loop weight is $d$).
I will proceed with the quantum dimension product model.

Wait, is there any other interpretation?
Maybe the values are $S_{0, (j,n)}$?
$S_{I} = 1/2 \times 1/\sqrt{8} \approx 0.177$.
$S_{\sigma} = 1/\sqrt{2} \times 1/\sqrt{8} \approx 0.25$.
$S_{\psi} = 1/2 \times 1/\sqrt{8} \approx 0.177$.
Identity expectation value is not 1 here.
We can normalize.
$S'^*_a = S_{0a} / S_{00}$.
$S'_I = 1$.
$S'_{\psi} = 1$.
$S'_{\sigma} = \frac{1/\sqrt{2}}{1/2} = \sqrt{2}$.
This is exactly the same as the quantum dimensions!
$\lambda_{(j_L, n_L, j_R, n_R)} = S'_{j_L} S'_{j_R}$?
Let's assume the expectation value for the full field is the product of the normalized $S$-matrix elements.
For the charge part $n$:
$S_{n,0} = \frac{1}{\sqrt{4k}} e^{-i \pi n n' / 2k}$.
$S_{0,0} = 1/\sqrt{4k}$.
So $S_{n,0} / S_{0,0} = e^{-i \pi n 0 / 2k} = 1$.
So the charge sector contributes a factor of 1.
Thus, $\lambda_{(j_L, n_L, j_R, n_R)} = \lambda_{j_L} \lambda_{j_R}$ where $\lambda_j$ is the normalized S-matrix.
$\lambda_0 = 1$.
$\lambda_{1/2} = 1$.
$\lambda_1 = \sqrt{2}$.
This confirms the Quantum Dimension hypothesis.

So the expectation value depends only on $j_L$ and $j_R$.
- If $j=0$: factor 1
- If $j=1/2$: factor 1
- If $j=1$: factor $\sqrt{2}$
Total $\lambda = (\text{factor from } j_L) \times (\text{factor from } j_R)$.

Wait, is there a possibility of interference?
The normalized S-matrix values are real and positive.
So product is fine.

Result tuples:
For every $j_L \in \{0, 1/2, 1\}$, $j_R \in \{0, 1/2, 1\}$, $n_L \in \{0,1,2,3\}$, $n_R \in \{0,1,2,3\}$:
$\lambda = d(j_L) \times d(j_R)$.
$d(0)=1, d(1/2)=1, d(1)=\sqrt{2}$.

Is there any constraint on $n$?
The problem states $n_{L/R} \in \mathbb{Z}_{2k}$.
For $k=2$, this is $\mathbb{Z}_4$.
I will list the values based on this logic.

One detail: The problem asks for the expectation value of "Verlinde lines".
In some contexts, Verlinde lines are operators $W_a$.
Their VEV is $S_{0a}$.
If we use the full label $(j_L, n_L, j_R, n_R)$, $a$ is a field in the tensor product theory.
$S_{(j_L, n_L, j_R, n_R), (0,0,0,0)} = S^{L}_{(j_L, n_L), (0,0)} S^{R}_{(j_R, n_R), (0,0)}$.
Since we normalize by 1, and $S_{0,0}=1/\sqrt{\mathcal{D}^2}$, the ratio is indeed the quantum dimension.
$\lambda = d_{j_L} d_{j_R}$.
Are there any signs?
The S-matrix for Ising has signs:
$S = \frac{1}{2} \begin{pmatrix} 1 & 1 & \sqrt{2} \\ 1 & 1 & -\sqrt{2} \\ \sqrt{2} & -\sqrt{2} & 0 \end{pmatrix}$
Rows/cols: $0(I), 1/2(\psi), 1(\sigma)$.
$S_{I, I} = 1/2$.
$S_{\psi, I} = 1/2$.
$S_{\sigma, I} = 1/\sqrt{2}$.
Normalized by $S_{I,I}$:
$\lambda_I = 1$.
$\lambda_\psi = 1$.
$\lambda_\sigma = \sqrt{2}$.
So the signs disappear in the expectation value $\langle W \rangle = S/S_{II}$?
Wait, we usually calculate $\langle W_a \rangle = S_{0a}/S_{00}$.
$S_{0a}$ is the $a$-th component of the vector $S|0\rangle$.
The sign matters for the coefficients in the expansion of the vacuum.
However, the "expectation value" of a line operator is the amplitude. Amplitudes can be complex or signed.
But "expectation value" in physics often means the measurable value.
In topological quantum field theory (TQFT), the expectation value of a Wilson loop for a particle $a$ is its quantum dimension $d_a$.
Why? Because $\langle W_a \rangle = Z(S^1 \times a)$ (path integral with insertion of $a$).
This is related to the trace of the representation of the mapping class group, which is the dimension.
The $S$-matrix element $S_{0a}$ is related to $d_a / \mathcal{D}$.
So normalizing $S_{0a}$ by $S_{00} = 1/\mathcal{D}$ gives $d_a$.
So the expectation value $\lambda_a = d_a$.
Since the labels are $(L, R)$, and the theory is a product, $\lambda = d_L d_R$.
Also, the charge sector $U(1)$ has $d=1$.
So $\lambda$ depends only on $j_L, j_R$.
Values: 1, $\sqrt{2}$, 2.

Double check: Is it possible that $n$ affects the value?
Maybe if the theory is diagonal? But the labels are $j_L, j_R$. Distinct.
So product is the logical answer.

Final check on $k=2$ primary fields.
$j=0$ corresponds to vacuum $I$.
$j=1/2$ corresponds to Majorana fermion $\psi$.
$j=1$ corresponds to spin field $\sigma$ (non-Abelian anyon).
$d(I)=1, d(\psi)=1, d(\sigma)=\sqrt{2}$.
$\lambda = d(j_L) \times d(j_R)$.
Also, note that electron operators include $(1, 2k, 0, 0)$ which is $\sigma \times I$. Expectation value would be $\sqrt{2}$.
And $(0,0,1,2k)$ which is $I \times \sigma$. Expectation value $\sqrt{2}$.
This is consistent.

I will output the tuples for all valid combinations or summarize the calculation. The prompt asks to "find the expectation values... Return your answer as a tuple...". It implies a list or a method. I will provide the general formula and a representative set of tuples.

Wait, "assumption: identity operator has expectation value 1".
This confirms the normalization.
I will present the mathematical derivation.

**Summary of Model:**
1.  Identify the CFT as $\text{Ising} \times U(1)_4$ for left movers $\times$ same for right movers.
2.  Identify the labels $(j_L, n_L)$ and $(j_R, n_R)$ with primary fields in the chiral algebras.
    *   $j=0 \leftrightarrow I$ (Identity), dimension $h=0$, quantum dim $d=1$.
    *   $j=1/2 \leftrightarrow \psi$ (Majorana), dimension $h=1/2$, quantum dim $d=1$.
    *   $j=1 \leftrightarrow \sigma$ (Spin), dimension $h=1/16$, quantum dim $d=\sqrt{2}$.
    *   $n \in \mathbb{Z}_4 \leftrightarrow U(1)$ charge. Quantum dim $d=1$.
3.  The expectation value of a Verlinde line operator wrapping the torus cycle, labeled by a field $a$, is given by the quantum dimension $d_a$.
    *   For the product theory $(j_L, n_L, j_R, n_R)$, the quantum dimension factors: $d_{(j_L, n_L, j_R, n_R)} = d_{j_L} d_{j_R}$ (as U(1) parts are 1).
4.  Normalize such that identity $(0,0,0,0)$ has value 1.
    *   $d_I = 1$, condition satisfied.
5.  Resulting values:
    *   If $j_L \in \{0, 1/2\}$ and $j_R \in \{0, 1/2\}$, $\lambda = 1$.
    *   If $j_L = 1$ xor $j_R = 1$ (one is $\sigma$, other is $I/\psi$), $\lambda = \sqrt{2}$.
    *   If $j_L = 1$ and $j_R = 1$, $\lambda = 2$.

This covers all tuples $(j_L, n_L, j_R, n_R)$.
I will write down the mathematical description and the results.

One edge case: What if the question implies only the *local* operators?
"expectation values of Verlinde lines". Verlinde lines are usually topological, not necessarily local.
The electron operator is defined as local (or semi-local) but the Verlinde line is a defect.
Defects are associated with primary fields.
So we list all primaries.

Final confirmation of the tuple format: `(j_L, n_L, j_R, n_R, lambda)`.
I will provide a few examples and the general rule.

**Step-by-Step for the response:**
1.  Define the CFT components: Ising ($k=2$ MR chiral algebra) and $U(1)_{4}$ charge.
2.  Map labels $(j, n)$ to fields and their quantum dimensions.
    *   $j=0 \to I \to d=1$.
    *   $j=1/2 \to \psi \to d=1$.
    *   $j=1 \to \sigma \to d=\sqrt{2}$.
    *   $n \to$ charge $\to d=1$.
3.  Define Expectation Value $\lambda$ for a Verlinde line as the quantum dimension of the corresponding primary field (normalized to 1 for identity).
4.  Compute $\lambda$ for the product state $(j_L, n_L, j_R, n_R)$ as product of dimensions.
5.  State the values.
6.  Provide the tuples.

One detail: The problem says "Given k=2".
And "Find the expectation values...".
I should probably list them.
Since there are $3 \times 4 \times 3 \times 4 = 144$ combinations, I will categorize them by $j_L, j_R$ as $n$ doesn't change $\lambda$.
I will produce the output in the requested format.

Wait, should I check if $n$ and $j$ are coupled?
The electron operator is $(1, 2k)$. i.e. $(j=1, n=4 \equiv 0)$.
Usually in MR, the electron field is $\sigma \psi$ (in some notations) or just specific combinations.
But here labels are explicit.
The electron has $n=4 \equiv 0$.
This suggests the electron is in the $n=0$ charge sector.
The Verlinde lines are indexed by $(j, n)$.
The independence of indices in the tuple suggests we treat them as a Cartesian product label.
So $n$ can be anything.
So $\lambda$ is independent of $n$.
I will proceed.

One obscure possibility:
Is $\lambda$ related to the "reverse" of the S matrix? i.e. $S_{a0} = S_{0a}$. Symmetric.
So yes, just $S_{0a}$.

Final check on values:
$\lambda_{(0, n_L, 0, n_R)} = 1$
$\lambda_{(1/2, n_L, 0, n_R)} = 1$
$\lambda_{(1, n_L, 0, n_R)} = \sqrt{2}$
$\lambda_{(0, n_L, 1, n_R)} = \sqrt{2}$
$\lambda_{(1/2, n_L, 1, n_R)} = \sqrt{2}$
$\lambda_{(1, n_L, 1, n_R)} = 2$

The tuples iterate over $n_L, n_R \in \{0, 1, 2, 3\}$.
$j_{L,R} \in \{0, 1/2, 1\}$.
I will formulate the response.

Note on "Identity operator has expectation value 1":
This serves as the calibration point. We don't need to calculate $S_{00}$ explicitly, we just know it maps to $\lambda=1$.
The relative scales are fixed by the fusion rules (implicitly) or dimensions.
$d_a = S_{0a} / S_{00}$.
This is the standard way to get expectation values of Wilson lines (loops).
Answer is solid.

Reference check:
Chung & Stone p. 9 mentions "6-fold degeneracy".
The basis is usually labeled by $m=0,1$ and spin structures.
Paul shell:
The CFT description usually identifies sectors $I, \psi, \sigma$.
The electron is $\sigma$ (neutral in charge sector here based on problem description $n=2k=4 \equiv 0$).
So we have 3 Ising sectors.
The expectation values follow the quantum dimensions 1, 1, $\sqrt{2}$.

One final check: Does the problem ask for "expectation values" in the sense of vacuum expectation values of *local operators*?
"expectation values of Verlinde lines".
Verlinde lines are 1-dimensional topological operators.
Their expectation value is a number.
Yes, matches.

The prompt says "Return your answer as a tuple...".
I will describe the model and provide the result.

One small detail: representation of $\sqrt{2}$.
I'll write $\sqrt{2}$.

Model explanation:
1. Decompose the theory.
2. Identify primary fields and dimensions.
3. Apply formula.

I will write the solution now.

Steps:
1.  Identify the CFT as the product of two chiral Moore-Read theories (k=2).
2.  Identify the basis operators $(j_L, n_L, j_R, n_R)$ and map $j$ to the Ising anyon types ($I, \psi, \sigma$) with corresponding quantum dimensions ($1, 1, \sqrt{2}$).
3.  State that in a CFT on a torus, the expectation value of a Verlinde line (Wilson loop) labeled by primary $a$ is proportional to the quantum dimension $d_a$.
4.  Normalize so Identity $(0,0,0,0)$ is 1.
5.  Calculate $\lambda = d_{j_L} d_{j_R}$ (since charge $n$ is Abelian with $d=1$).
6.  List the values.

I will just list the rules and examples, as listing all 144 tuples is verbose but I will provide the description clearly.

Actually, looking at the output request "Return your answer as a tuple...", it might imply a specific format for *all* of them or just *a* tuple. "find the expectation values... Return your answer as a tuple $(j_L,n_L,j_R,n_R,\lambda)$".
It says "Return your answer as a tuple" (singular or generic).
I will provide the logic and then a formatted list of tuples.

Let's refine the tuple format.
`(0, 0, 0, 0, 1.0)`
`(1, 0, 0, 0, sqrt(2))`
...
I will check the range of $n$. "n in Z_{2k}" -> "k=2" -> "Z_4" -> {0,1,2,3}.
Okay.

Is there any case where $j_L, j_R$ mixing is forbidden?
The operator list includes $(1, 4, 0, 0)$.
This implies mixed sectors are allowed (chiral operators).
The "Verlinde lines" can be chiral.
So all combinations represent valid Verlinde lines (operators) in the product theory.
So 144 values.

Final check on "expectation values".
Are these values $\lambda$ real?
Yes, quantum dimensions are real.
$S_{0a}/S_{00}$ is real for MR (Ising $S$ is real).
So $\lambda \in \mathbb{R}^+$.

Plan write-up:
- Define CFT structure.
- Define Quantum Dimension derivation.
- Map to tuple $(j_L, n_L, j_R, n_R, \lambda)$.
- Provide the set of values (categorized).

Result format:
Since I need to output the "actual complete content", I will generate the full math description and the set of results.
Since 144 tuples is long, I will describe the pattern clearly and give examples, or generate them all if appropriate for a "code-like" output request. The prompt says "You do not write code but leave this to someone more experienced." but "Return your answer as a tuple". This is a bit ambiguous. I will provide the logic and a comprehensive list/table in markdown.

Wait, the problem might implicitly ask for the tuple corresponding to the *electric* field or something? No, "expectation values of Verlinde lines" (plural) for the labels. It asks for the model to find them.
So the "answer" is the model description.
And the "return" is the tuple format for the values.
I will provide a full set of values for all combinations of $j_{L,R}$ and note $n$ independence.
Actually, it's best to give a representative list showing the dependence on $j$ and $n$.
Values:
- If $(j_L, j_R) \in \{(0,0), (0,1/2), (1/2,0), (1/2,1/2)\}$, $\lambda = 1$.
- If $(j_L, j_R) \in \{(1,0), (0,1), (1,1/2), (1/2,1)\}$, $\lambda = \sqrt{2}$.
- If $(j_L, j_R) = (1, 1)$, $\lambda = 2$.
(Note: $j=1$ is $\sigma$, $j=1/2$ is $\psi$).
For all $n_L, n_R \in \{0,1,2,3\}$.

I will construct the final response.

One last check: Is $j=1$ really $\sigma$?
Moore-Read CFT (k=2) is $U(1)_4 \times \text{Ising}$.
Labels usually $l, m$.
In some papers (e.g. Cappelli/Zuber), Ising labels are $0, 1/2, 1$.
$0 \to I$.
$1 \to \psi$ (Wait. Ising rep of SU(2) level 2 has spins $0, 1/2, 1$. Mapping to Ising: $0\to I, 1\to \psi, 1/2 \to \sigma$? Or $0\to I, 1/2 \to \psi, 1 \to \sigma$?
Let's check dimensions.
SU(2)$_2$ dimensions: $h_j = \frac{j(j+1)}{k+2} = \frac{j(j+1)}{4}$.
$j=0 \implies h=0$ (Identity).
$j=1/2 \implies h = (0.5 \times 1.5)/4 = 0.75/4 = 3/16$.
$j=1 \implies h = (1 \times 2)/4 = 0.5$.
Ising model dimensions:
$I: 0$.
$\psi: 1/2$.
$\sigma: 1/16$.
Match:
$j=0 \iff I$.
$j=1/2 \iff \sigma$ (Dimension 1/16 vs 3/16? No match).
$j=1 \iff \psi$ (Dimension 1/2 vs 1/2. Match).
So SU(2)$_2$ label $j=1$ corresponds to Ising $\psi$. Label $j=0$ corresponds to Ising $I$.
Where is the $\sigma$ field ($h=1/16$)?
The Moore-Read CFT is not simply SU(2)$_2$. It is SU(2)$_2$ / U(1) (parafermion) or Ising $\times$ U(1).
The problem statement says: "primary fields are labeled by $(j_L, n_L, j_R, n_R)$, where $j_{L/R}=0,1/2,1$".
And "electron operators ... are $(1,2k,0,0)$".
If electron is $j=1$, and electron has $h=1$ (spin 1), then $h_L + h_R = 1$.
If $k=2$, $n=2k=4 \equiv 0$. $h_{U(1)} = 0$.
So $h_L(j=1) + h_R(j=0) = 1$.
If we assume $j=1$ is Ising $\psi$ ($h=1/2$), then total $h=1/2$. Not 1.
If we assume $j=1$ is Ising $\sigma$ ($h=1/16$), then total $h=1/16$. Not 1.
Let's re-read carefully.
"filling fraction $\nu=1/k$". $k=2 \implies \nu=1/2$.
MR Pfaffian state $\nu=5/2$ is $U(2)_2$.
But here $U(1)_{2k}$.
The electron in the CFT for MR $\nu=1/2$ has spin 1/2? No, electron is a fermion, spin 1.
Conformal weight $h = s/2 = 0.5$ for a fermion?
Wait, in 2D CFT, $L_0$ is energy/scaling dimension.
Physics spin is related to $L_0 - \bar{L}_0$.
Electron in MR ($\nu=1/2$) is $(1, 2k)$.
If $n=2k=4 \equiv 0$, we only have $j=1, 0$.
This suggests the electron is simply $(j_L=1) \otimes (j_R=0)$.
We need the spin of the electron.
In the Moore-Read Pfaffian literature (e.g. Read/Green), the electron operator is $\Psi \sim \psi$ ( Majorana) $\times$ vertex operator.
Here, the problem defines the electron as $(1, 2k, 0, 0)$.
This is a standard notation in MR CFT labeling (e.g. **Cappelli, Zuber, or Ardonne**).
In the MR vertex operator construction ($SU(2)_k$ or similar), the electron carries a specific spin.
Given $j \in \{0, 1/2, 1\}$ and $k=2$.
Let's match to the known Ising topological spins $\theta$:
$\theta_I = 1$.
$\theta_\psi = -1$.
$\theta_\sigma = i$. (Wait, $2\pi \times 1/16 \implies e^{i \pi/8}$? No. $e^{2\pi i h}$).
$h_\sigma = 1/16$. $\theta = e^{2\pi i / 16} = e^{i \pi / 8}$. This is MR quasihole spin.
The electron is local (boson/fermion).
Local operators have $\theta = 1$ (boson) or $-1$ (fermion).
So $(1, 2k, 0, 0)$ must have spin 0 or 1/2 (weight 0 or 1/2).
Actually, electrons are fermions. $h=1/2 \pmod \mathbb{Z}$.
So $h_L + h_R = 1/2 \pmod \mathbb{Z}$.
If $L$ is $j=1$ and $R$ is $j=0$.
If $h(1) = 1/2$ and $h(0) = 0$, then $h_{tot} = 1/2$. This works.
So $j=1$ corresponds to $\psi$ (Majorana) with $h=1/2$.
What about $j=0$? $h=0$. Identity.
What about $j=1/2$? It must be $\sigma$?
In $SU(2)_2$, $j=1/2$ has $h=3/16$. Ising $\sigma$ has $h=1/16$.
There is a shift often related to the coupling with U(1).
The total conformal weight of an operator $(j, n)$ is $h = \frac{j(j+2)}{k+2} + \frac{(n)^2}{4k}$. (Using some MR formulae).
Let's try to find the conformal weights for $k=2$ from labels.
If electron is $(1, 4, 0, 0)$.
Then $h_L(1, 4)$ is the relevant weight.
For MR $\nu=1/2$, electron $h = 1/2$.
If $n=4 \equiv 0$ contributes 0 weight (if $n$ is integer charge?), then $h_L(j=1)$ must be $1/2$.
This implies $j=1$ is the fermion $\psi$.
Then what is $j=1/2$?
In $Z_k$ parafermions (representative), spins are different.
Bottom line:
$j=0$: Identity ($h=0$).
$j=1$: Fermion ($h=1/2$).
$j=1/2$: Spin field ($h=1/16$? or something else?).
Wait, if $j=1/2$ was $\sigma$ ($h=1/16$), it is non-local.
This is consistent with MR theory where $\sigma$ is a non-local quasiparticle.
Does $n$ affect the locality?
The electron $(1, 2k)$ is local. $n=2k$ implies "neutral" with respect to some constraint?
Usually locality requires $(j, n)$ to satisfy some condition such that spin is integer.
Anyway, we need the "expectation value" (quantum dimension).
For Ising model:
$I$: $d=1$.
$\psi$: $d=1$.
$\sigma$: $d=\sqrt{2}$.
So:
$j=0 \to d=1$.
$j=1 \to d=1$.
$j=1/2 \to d=\sqrt{2}$.
Let's verify this assignment.
If $j=1/2$ is the spin field $\sigma$, then its dimension is $\sqrt{2}$.
The electron is $j=1$, so its dimension is 1.
This makes sense physically: electrons are localized particles (dimension 1), quasiparticles can be non-Abelian ($\sigma$, dimension $\sqrt{2}$).
Is it possible that $j=1$ is $\sigma$?
If $j=1$ was $\sigma$, then electron would be $\sigma$, which is non-local (semi-local) and dimension $\sqrt{2}$.
But the electron is a local fermion. Its Wilson line should not fuse like a non-Abelian anyon in the bulk localization sense (it creates a charge).
Usually, we expect the fundamental local excitation to have dimension 1.
So $j=1$ (the electron field) should correspond to an Abelian anyon type (dim 1).
This implies $j=1 \leftrightarrow \psi$ (dim 1).
And $j=1/2 \leftrightarrow \sigma$ (dim $\sqrt{2}$).
Let's check if $j=0$ is involved. $j=0$ is vacuum (dim 1).
So:
$d(0) = 1$.
$d(1) = 1$.
$d(1/2) = \sqrt{2}$.
This seems the most physically consistent assignment for the MR state.
The non-Abelian anyon is the $\sigma$ field. The problem labels primaries $0, 1/2, 1$.
In Ising, we have 3 primaries.
If $j=1$ is $\psi$ and $j=1/2$ is $\sigma$, the mapping is not ordered by spin ($0, 1/2, 1$), but by the Kac labels $j$.
In SU(2)$_2$, $j=1$ has spin 1 (dim 2? No). It corresponds to the adjoint rep.
Wait, $SU(2)_k$ labels $j=0, 1/2, \dots, k/2$.
For $k=2$, $j \in \{0, 1/2, 1\}$.
The fusion rules are those of Ising:
$1 \times 1 = 0$? (Fermion squared = 1).
$1/2 \times 1/2 = 0 + 1$?
This matches SU(2)$_2$ fusion.
$0$ is identity.
$1$ corresponds to $2j=2$ (Dimension 3) vector in SU(2). But in the CFT, it maps to the Ising fermion $\psi$.
$1/2$ corresponds to $j=1/2$ spinor. In CFT, it maps to Ising $\sigma$.
Yes, this identification is standard ($j_{spin} \leftrightarrow$ Ising primary).
$j_{Kac} = 1 \leftrightarrow \psi$ (dim 1).
$j_{Kac} = 1/2 \leftrightarrow \sigma$ (dim $\sqrt{2}$).
$j_{Kac} = 0 \leftrightarrow I$ (dim 1).
Okay, I have high confidence in this mapping.

So, for $\lambda$:
If $j_L \in \{0, 1\}$ and $j_R \in \{0, 1\}$, $\lambda = 1$.
If one of $j_L, j_R$ is $1/2$, $\lambda = \sqrt{2}$.
If both are $1/2$, $\lambda = 2$.

This flips my previous assignment of 1 and $\sqrt{2}$.
Previous: $j=1 \to \sqrt{2}$.
New: $j=1/2 \to \sqrt{2}$.
Why? Because $j=1$ is the fermion (local, dim 1), $j=1/2$ is the spin field (non-local, dim $\sqrt{2}$).
The electron operator in the prompt is $(1, 2k, 0, 0)$.
It uses $j=1$.
This confirms $j=1$ is the local electron (or part of it). The part $(1, 2k)$ is local.
If $j=1$ were the non-Abelian part ($\sigma$), the electron would be non-Abelian.
The MR state has Abelian electrons and non-Abelian quasiholes ($\sigma$).
So $j=1$ must be Abelian ($d=1$).
And $j=1/2$ must be non-Abelian ($d=\sqrt{2}$).

So the correct dimensions are:
$d(0) = 1$
$d(1/2) = \sqrt{2}$
$d(1) = 1$

Let's check the source or standard knowledge.
Moore-Read CFT: $Ising \times U(1)_2m$.
Anyons:
1. $I$: Identity. $d=1$.
2. $\psi$: Fermion. $d=1$.
3. $e^{i \phi / \sqrt{2m}}$: Abelian charge. $d=1$.
4. $\sigma$: Non-Abelian PF quasihole. $d=\sqrt{2}$.
The electron is $\psi e^{i \phi \sqrt{m/2}}$.
In the problem's notation:
$k=2$.
Labels $j, n$.
Electron is $(1, 2k) = (1, 4)$.
If $(1, 4)$ corresponds to $\psi$, then $j=1 \leftrightarrow \psi$.
Then $j=1/2$ is the remaining label. It must be $\sigma$.
This fits.

So:
Expectation values $\lambda$:
For $j \in \{0, 1\}$, contribution to $\lambda$ is 1.
For $j = 1/2$, contribution to $\lambda$ is $\sqrt{2}$.

Resulting tuples logic:
$\lambda = d_{j_L} d_{j_R}$.
1. $(0, *, 0, *) \to 1$.
2. $(1, *, 0, *) \to 1$.
3. $(0, *, 1, *) \to 1$.
4. $(1, *, 1, *) \to 1$.
5. $(1/2, *, 0, *) \to \sqrt{2}$.
6. $(0, *, 1/2, *) \to \sqrt{2}$.
7. $(1, *, 1/2, *) \to \sqrt{2}$.
8. $(1/2, *, 1, *) \to \sqrt{2}$.
9. $(1/2, *, 1/2, *) \to 2$.

This is the correct physical model for the MR state at $k=2$.
The electron is Abelian. The $j=1/2$ sector is the non-Abelian sector.

Final check: Did I misinterpret $j_{L/R} = 0, 1/2, 1$?
Maybe $1/2$ is fermion?
Then $1$ is $\sigma$?
If $j=1$ is $\sigma$, then electron $(1, 2k)$ is $\sigma$.
But electron in MR is fermion (cumulant of $2k$ flux).
Ising $\sigma$ is a semion (spin 1/16). It is not a fermion.
Ising $\psi$ is a fermion (spin 1/2).
So the electron component in Ising MUST be $\psi$.
Thus $j=1 \leftrightarrow \psi$.
Thus $j=1/2 \leftrightarrow \sigma$.
This confirms the dimensions derived.

I will write the solution based on this.

Role
- Build a model
- Great at physical models
- Work with info
- Cite info
- Explain steps
- No code

I will explain the identification of $j$ labels with Ising primaries, the calculation of quantum dimensions, and the resulting expectation values for the Verlinde lines on the torus.

Structure:
1. CFT Construction (Moore-Read $k=2$ as Ising $\times$ U(1)$_4$).
2. Identification of Primary Fields from Labels ($j$ mapping).
3. Quantum Dimension Calculation.
4. Verlinde Line Expectation Value Model.
5. Results (Tuples).</think># Mathematical Model for Verlinde Line Expectation Values in $k=2$ Moore-Read CFT

## 1. Physical Model and CFT Construction

We consider a (1+1)-dimensional conformal field theory (CFT) on a torus that describes the edge modes of a Moore-Read quantum Hall state at filling fraction $\nu = 1/k$.
Based on the problem setup and the analysis of the Moore-Read state (specifically at $k=2$, corresponding to $\nu=1/2$), the edge theory consists of a product of two chiral components: a left-moving edge and a right-moving edge.

The chiral algebra of the Moore-Read state is isomorphic to the product of an Ising model and a chiral $U(1)$ boson:
$$ \mathcal{A}_{MR} \cong \mathcal{M}_{Ising} \times U(1)_{2k} $$
For the specific case $k=2$, the charge sector is $U(1)_4$.

## 2. Primary Field Labeling and Identification

The primary fields of the full (non-chiral) theory are labeled by the tuple:
$$ (j_L, n_L, j_R, n_R) $$
where:
- $j_{L/R} \in \{0, 1/2, 1\}$ labels the primary field in the Ising sector ($\psi$, $\sigma$, $I$).
- $n_{L/R} \in \mathbb{Z}_{2k} = \mathbb{Z}_4$ labels the charge in the $U(1)_4$ sector.

To determine the physical nature of these fields, we must map the label $j$ to the standard Ising model primaries. The conformal weights $h$ and the nature (Abelian/Non-Abelian) distinguish them. The electron operator is given in the problem as $(1, 2k, 0, 0) = (1, 4, 0, 0)$.
- The electron is a local fermion with conformal weight $h=1/2$ in the Ising sector.
- In the Ising CFT, the field with $h=1/2$ is the Majorana fermion $\psi$ (also called $\psi_{Ising}$).
- The field with $h=1/16$ is the spin field $\sigma$ (the non-Abelian anyon in the Moore-Read state).
- The field with $h=0$ is the identity $I$.

Given that the electron corresponds to $j=1$, we establish the following mapping for $k=2$:
- $j=0 \leftrightarrow I$ (Identity). Quantum dimension $d_0 = 1$.
- $j=1 \leftrightarrow \psi$ (Majorana Fermion). Quantum dimension $d_1 = 1$.
- $j=1/2 \leftrightarrow \sigma$ (Spin Field/Non-Abelian Anyon). Quantum dimension $d_{1/2} = \sqrt{2}$.

(Note: This ordering of labels is consistent with the $SU(2)_2$ Kac labels often used to parametrize the Moore-Read theory, where the spinor representation $j=1/2$ maps to the Ising $\sigma$ field).

The charge sector labels $n_{L/R} \in \mathbb{Z}_4$ correspond to Abelian vertex operators, each with quantum dimension $d_n = 1$.

## 3. Verlinde Line Expectation Value Model

In a 2D CFT on a torus, the "Verlinde lines" are topological defect lines associated with the primary fields of the chiral algebra. The expectation value of a Verlinde line operator $W_a$ wrapping a cycle of the torus (and associated with a primary field $a$) is given by its quantum dimension $d_a$.
$$ \langle W_a \rangle = d_a $$

This value arises from the modular $S$-matrix normalization, specifically:
$$ \langle W_a \rangle = \frac{S_{0a}}{S_{00}} $$
where $S_{0a}$ is the modular transformation matrix element from the vacuum sector to sector $a$. For unitary theories, this ratio is the quantum dimension.

For the product theory $CFT_L \times CFT_R$, the Verlinde line labeled by $(j_L, n_L, j_R, n_R)$ corresponds to the product of lines in the left and right sectors. Therefore, the total expectation value $\lambda_{(j_L,n_L,j_R,n_R)}$ is the product of the individual quantum dimensions:
$$ \lambda_{(j_L,n_L,j_R,n_R)} = d_{j_L} \cdot d_{n_L} \cdot d_{j_R} \cdot d_{n_R} $$
Since the charge sector is Abelian ($d_n = 1$ for all $n$), the value simplifies to:
$$ \lambda_{(j_L,n_L,j_R,n_R)} = d_{j_L} \cdot d_{j_R} $$
where $d_0 = 1$, $d_1 = 1$, and $d_{1/2} = \sqrt{2}$.

This model satisfies the condition that the identity operator $(0,0,0,0)$ has expectation value $1 \cdot 1 = 1$.

## 4. Calculation of Values

Using $d_0 = 1$, $d_1 = 1$, and $d_{1/2} = \sqrt{2}$, we calculate $\lambda$ for all combinations of $j_L, j_R \in \{0, 1/2, 1\}$.

The possible values for $\lambda$ are:
- **1**: If neither the left nor right sector is the non-Abelian $\sigma$ field ($j \neq 1/2$). Specifically, if $j_L, j_R \in \{0, 1\}$.
- **$\sqrt{2}$**: If exactly one of the sectors is the non-Abelian $\sigma$ field ($j=1/2$). Specifically, if $j_L = 1/2$ and $j_R \in \{0, 1\}$, or vice versa.
- **2**: If both sectors are the non-Abelian $\sigma$ field ($j_L = 1/2$ and $j_R = 1/2$).

The value is independent of the charge indices $n_L, n_R$ (which can be $0, 1, 2, 3$).

## 5. Tuples of Expectation Values

The expectation values $\lambda_{(j_L,n_L,j_R,n_R)}$ for $k=2$ are listed below. Since $n_L$ and $n_R$ range over $\{0, 1, 2, 3\}$ and do not affect the value, we present the tuples representative of the $j$-dependence.

**Case 1: $\lambda = 1$**
This occurs when $j_L, j_R \in \{0, 1\}$.
Format: $(j_L, n_L, j_R, n_R, 1)$
Examples:
- `(0, 0, 0, 0, 1)`
- `(1, 1, 0, 2, 1)`
- `(1, 3, 1, 1, 1)`
- `(0, 3, 1, 0, 1)`

**Case 2: $\lambda = \sqrt{2}$**
This occurs when one of $j_L, j_R$ is $1/2$ and the other is in $\{0, 1\}$.
Format: $(1/2, n_L, j_{other}, n_R, \sqrt{2})$ or $(j_{other}, n_L, 1/2, n_R, \sqrt{2})$
Examples:
- `(1/2, 0, 0, 0, 1.41421...)`
- `(0, 0, 1/2, 3, 1.41421...)`
- `(1/2, 2, 1, 1, 1.41421...)`
- `(1, 3, 1/2, 0, 1.41421...)`

**Case 3: $\lambda = 2$**
This occurs when both $j_L$ and $j_R$ are $1/2$.
Format: $(1/2, n_L, 1/2, n_R, 2)$
Examples:
- `(1/2, 0, 1/2, 0, 2)`
- `(1/2, 3, 1/2, 3, 2)`

### Summary of Results
For any tuple $(j_L, n_L, j_R, n_R)$ with $k=2$:
$$ \lambda_{(j_L,n_L,j_R,n_R)} = \begin{cases} 1 & \text{if } j_L \in \{0,1\} \text{ and } j_R \in \{0,1\} \\ \sqrt{2} & \text{if } j_L = 1/2 \text{ xor } j_R = 1/2 \\ 2 & \text{if } j_L = 1/2 \text{ and } j_R = 1/2 \end{cases} $$
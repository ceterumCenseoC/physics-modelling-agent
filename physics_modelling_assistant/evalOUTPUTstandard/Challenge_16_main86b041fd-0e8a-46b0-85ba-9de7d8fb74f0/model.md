# Mathematical Description of the Model for Calculating $U_c$

To determine the critical interaction strength $U_c$ for the phase transition at quarter-filling in the specified two-band Hubbard model, we construct the following theoretical framework. This model proceeds through the diagonalization of the non-interacting band structure, identification of the filling condition, and the application of the Stoner criterion for magnetic instability.

## 1. Non-Interacting Hamiltonian and Band Diagonalization

First, we analyze the non-interacting part of the Hamiltonian ($U=0$). We define a spinor basis for the two sublattices $\Psi_{\mathbf{k}\sigma} = (c_{1\mathbf{k}\sigma}, c_{2\mathbf{k}\sigma})^T$. The Hamiltonian in matrix form for a given spin $\sigma$ is $H_0 = \sum_{\mathbf{k}\sigma} \Psi_{\mathbf{k}\sigma}^\dagger \mathcal{H}(\mathbf{k}) \Psi_{\mathbf{k}\sigma}$.

The $2 \times 2$ matrix $\mathcal{H}(\mathbf{k})$ is given by:
$$
\mathcal{H}(\mathbf{k}) = \begin{pmatrix}
h_{11}(\mathbf{k}) & h_{12}(\mathbf{k}) \\
h_{21}(\mathbf{k}) & h_{22}(\mathbf{k})
\end{pmatrix}
$$
where the matrix elements are derived from the problem statement:
$$
\begin{aligned}
h_{11}(\mathbf{k}) &= 2(\cos k_x - \cos k_y) - \mu \\
h_{22}(\mathbf{k}) &= -2(\cos k_x - \cos k_y) - \mu \\
h_{12}(\mathbf{k}) &= \sqrt{2} \left[ \text{e}^{i\pi/4}(1+\text{e}^{i(k_y-k_x)}) + \text{e}^{-i\pi/4}(\text{e}^{-ik_x}+\text{e}^{ik_y}) \right] \\
h_{21}(\mathbf{k}) &= \sqrt{2} \left[ \text{e}^{-i\pi/4}(1+\text{e}^{-i(k_y-k_x)}) + \text{e}^{i\pi/4}(\text{e}^{ik_x}+\text{e}^{-ik_y}) \right] = h_{12}^*(\mathbf{k})
\end{aligned}
$$

We diagonalize this matrix to obtain the energy dispersion relations for the two bands, $\epsilon_+(\mathbf{k})$ and $\epsilon_-(\mathbf{k})$. The eigenvalues are found by solving $\det(\mathcal{H}(\mathbf{k}) - \epsilon I) = 0$:
$$
\epsilon_{\pm}(\mathbf{k}) = \frac{h_{11} + h_{22}}{2} \pm \sqrt{\left(\frac{h_{11}-h_{22}}{2}\right)^2 + |h_{12}|^2}
$$
Substituting the matrix elements:
$$
\epsilon_{\pm}(\mathbf{k}) = -\mu \pm \sqrt{4(\cos k_x - \cos k_y)^2 + |h_{12}(\mathbf{k})|^2}
$$
We simplify the hopping term $|h_{12}(\mathbf{k})|^2$. By expanding the complex exponentials, we find:
$$
\begin{aligned}
|h_{12}(\mathbf{k})|^2 &= 2 \left[ (\frac{1}{\sqrt{2}}+\cos x + \sin y + \sin x + \cos y + \dots)^2 + (\dots)^2 \right] \\
&= 4(1 + \cos k_x + \cos k_y + \cos(k_x - k_y) + \sin k_x - \sin k_y + \dots) \dots \\
\end{aligned}
$$
*Note: The full algebraic simplification of $|h_{12}|^2$ is complex and typically involves algebraic manipulation software. For the purpose of the critical interaction model, we denote the effective hopping amplitude function as $t^2(\mathbf{k}) = 4(\cos k_x - \cos k_y)^2 + |h_{12}(\mathbf{k})|^2$.*

Thus, the band energies are:
$$
E_{\pm}(\mathbf{k}) = -\mu \pm t(\mathbf{k})
$$

## 2. Chemical Potential at Quarter-Filling

The system is at quarter-filling. With two spin species and two sublattices (bands), the total number of states is $4N$ (where $N$ is the number of unit cells). Quarter-filling corresponds to a total electron density of $n = 1$ electron per unit cell (or $1/4$ of available states).

The critical $U_c$ is determined by the susceptibility at the Fermi surface. Therefore, we must identify the Fermi energy $E_F$ (or chemical potential $\mu$) corresponding to this filling. The number of particles $N_e$ is given by:
$$
N_e = \sum_{\mathbf{k}} \sum_{\nu=\pm} \theta(E_F - E_\nu(\mathbf{k})) = N
$$
where $\theta$ is the Heaviside step function.
This implies:
$$
\frac{1}{N} \sum_{\mathbf{k}} \left[ \theta(\mu + t(\mathbf{k})) + \theta(\mu - t(\mathbf{k})) \right] = 1
$$
Assuming a symmetric band structure where $t(\mathbf{k}) \ge 0$ (which is typical for such hopping models), the lower band $E_- = -\mu - t(\mathbf{k})$ will be fully filled or partially filled depending on $\mu$.

Given the square lattice symmetry and the form of the Hamiltonian, we expect the Van Hove singularities to play a role. However, analytically, the condition quarter-filling usually places the Fermi level such that the density of states satisfies the integral relation. For this model, we set the band center to 0 and assume the quarter-filling condition determines $\mu$ such that the total area enclosed by the Fermi surface in the Brillouin zone is equal to the filling fraction.

*Assumption:* Based on the structure, if the bands are symmetric about $-\mu$, quarter-filling (average 1 electron per site for 2 orbitals per site) often corresponds to the band crossing point or a specific Fermi surface topology. Let $\mu_{1/4}$ be the chemical potential satisfying the quarter-filling condition.

## 3. Instability Analysis and Ward Identity for $U_c$

We look for a phase transition driven by the Hubbard interaction. Since the term is $U \sum (n_{i\uparrow} n_{i\downarrow})$, the most likely instability is towards a magnetic ordered state (Stoner instability) or a charge density wave (CDW), depending on the nesting.

The critical interaction strength $U_c$ is defined by the point where the static susceptibility for the ordering wavevector diverges. We consider the susceptibility $\chi_0(\mathbf{q})$ for the non-interacting system at quarter-filling:
$$
\chi_0(\mathbf{q}) = \frac{1}{N} \sum_{\mathbf{k}} \frac{f(E_{\mathbf{k}}) - f(E_{\mathbf{k}+\mathbf{q}})}{E_{\mathbf{k}+\mathbf{q}} - E_{\mathbf{k}}}
$$
where $f(E)$ is the Fermi-Dirac distribution at $T=0$ (step function).

For a metal-insulator transition driven by antiferromagnetism (common in Hubbard models), we look at the wavevector $\mathbf{Q}$ that connects parallel pieces of the Fermi surface (nesting vector). In 2D square lattice systems, this is often $\mathbf{Q} = (\pi, \pi)$ or similar.

Within the Random Phase Approximation (RPA), the condition for the instability (divergence of the full susceptibility) is the Stoner criterion:
$$
1 - U \chi_0(\mathbf{Q}) = 0
$$
This yields the mathematical definition of the critical interaction:
$$
U_c = \frac{1}{\chi_0(\mathbf{Q})}
$$

## 4. Calculation of the Susceptibility $\chi_0$

To evaluate $U_c$ accurately, we calculate $\chi_0(\mathbf{Q})$. We focus on the wavevector $\mathbf{Q}$ corresponding to the peak in the susceptibility.

From the diagonalized Hamiltonian, the operators in the band basis are $a_{\mathbf{k}\nu\sigma}$. The susceptibility can be decomposed into intraband and interband terms. However, at $T=0$, transitions occur only between states where one is occupied and the other is empty.

Let the band energies be $E_\pm(\mathbf{k})$. The susceptibility takes the form:
$$
\chi_0(\mathbf{Q}) = \frac{2}{N} \sum_{\mathbf{k}, \nu, \nu'} \frac{ |M_{\nu\nu'}(\mathbf{k}, \mathbf{Q})|^2 (f(E_\nu(\mathbf{k})) - f(E_{\nu'}(\mathbf{k}+\mathbf{Q}))) }{ E_{\nu'}(\mathbf{k}+\mathbf{Q}) - E_\nu(\mathbf{k}) }
$$
The factor of 2 accounts for the spin degeneracy (assuming paramagnetic state), and $M$ is the matrix element of the transformation between sublattice and band bases.

*Approximation for maximum accuracy:*
Given the complexity of $h_{12}$, we approximate the nesting properties. The term $(\cos k_x - \cos k_y)$ suggests saddle points at $(\pi, 0)$ and $(0, \pi)$. The phase factors in $h_{12}$ might shift these Van Hove points. A likely candidate for the ordering vector is $\mathbf{Q} = (\pi, \pi)$, or $\mathbf{Q} = (\pi, -\pi)$.

At quarter filling, the Fermi surface might effectively nest at a specific $\mathbf{Q}$. The density of states at the Fermi level, $N(0)$, is crucial. If the Fermi surface is nested perfectly at vector $\mathbf{Q}$, $\chi_0$ exhibits a logarithmic divergence in 2D, leading to $U_c \to 0$. However, imperfect nesting or significant next-nearest neighbor hopping (contained in $h_{12}$) cuts off this divergence.

The mathematical expression for $U_c$ is rigorously:
$$
U_c^{-1} = \int_{-\infty}^{\infty} d\omega \, N(\omega) \frac{f(\omega) - f(\omega + \Omega)}{\Omega} \bigg|_{\Omega \to 0}
$$
Or in k-space:
$$
U_c = \left[ \int \frac{d^2k}{(2\pi)^2} \left( -\frac{\partial f(E(\mathbf{k}))}{\partial E} \right) \right]^{-1} = \frac{1}{N(E_F)}
$$
if the transition is simply driven by the density of states (Stoner ferromagnetism).

If the transition is antiferromagnetic (SDW), we use:
$$
U_c = \left[ \int \frac{d^2k}{(2\pi)^2} \frac{\theta(E_F - E(\mathbf{k})) \theta(E(\mathbf{k}+\mathbf{Q}) - E_F)}{E(\mathbf{k}+\mathbf{Q}) - E(\mathbf{k})} \right]^{-1}
$$

## 5. Final Model Summary

To calculate the critical interaction strength $U_c$:
1.  **Compute the band structure**: Use the complex hopping Hamiltonian to find $E_{\pm}(\mathbf{k})$.
2.  **Determine $\mu$**: Solve the quarter-filling constraint $\sum_{\mathbf{k}, \nu} \theta(E_F - E_\nu(\mathbf{k})) = N$ to find the Fermi energy.
3.  **Identify $\mathbf{Q}$**: Identify the wavevector $\mathbf{Q}$ (likely $(\pi, \pi)$ or related to symmetry points) that maximizes the susceptibility $\chi_0(\mathbf{Q})$.
4.  **Evaluate Susceptibility**: Compute the integral for $\chi_0(\mathbf{Q})$ over the Brillouin zone, restricted to the Fermi surface.
5.  **Apply Stoner Criterion**: Calculate $U_c = 1 / \chi_0(\mathbf{Q})$.

This mathematical description provides the framework for determining $U_c$. The specific numerical value requires the integration over the Brillouin zone using the specific form of $h_{12}(\mathbf{k})$, often performed numerically.
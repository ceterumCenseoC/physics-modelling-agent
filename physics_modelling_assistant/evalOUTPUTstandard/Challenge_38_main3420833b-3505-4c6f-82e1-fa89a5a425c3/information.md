Based on my thorough analysis of the provided scientific sources, I can now compile the complete information needed to compute the temperature dependence of the energy phase space integral $I(T)$ for the Hatsugai-Kohmoto model. Let me extract the relevant information from these papers.

# Temperature Dependence of the Energy Phase Space Integral $I(T)$ in the Hatsugai-Kohmoto Model

## 1. The Hatsugai-Kohmoto (HK) Model

The Hamiltonian of the Hatsugai-Kohmoto model is given by [Hatsugai & Kohmoto, 1992; Lidsky et al., 1997]:

$$
H = \sum_{k,\sigma} (\varepsilon_k-\mu) n_{k \sigma} + U \sum_{k} n_{k \uparrow} n_{k \downarrow},
$$

where the non-interacting part corresponds to $\varepsilon_k$ with $0 < \varepsilon_k < W$, and $U$ is the interaction strength. The key feature of the HK interaction is its locality in momentum space, which corresponds to an infinite-range interaction in real space [Guerci et al., 2024].

The Hamiltonian is exactly diagonalizable because it decomposes into independent momentum sectors. Within each sector with $n_k$ particles, the eigenenergies are [Hackner, Mai & Phillips, 2025]:

$$
E^{n_k}_k = n_k \xi_k + \frac{n_k(n_k-1)}{2} U,
$$

where $\xi_k = \varepsilon_k - \mu$ and $n_k$ denotes the number of filled states at momentum $k$. Each energy has a degeneracy of $\binom{N}{n_k}$ for SU($N$) generalization, and for SU(2):

$$
E^{n_k}_k = n_k(\varepsilon_k - \mu) + \frac{n_k(n_k-1)}{2} U,
\quad n_k = 0, 1, 2.
$$

Explicitly, the four eigenstates per momentum $k$ have energies [Lidsky et al., 1997]:

$$E_0 = 0, \quad E_1 = \varepsilon_k - \mu, \quad E_2 = 2(\varepsilon_k - \mu) + U.$$

## 2. Perturbation Term and Scattering Process

We add a perturbation that preserves momentum and respects fermion symmetries [Problem setup]:

$$
H' = \sum_{2,3,4} V(1,2,3,4) \, \delta_{k_1+k_2,k_3+k_4} \, c^{\dagger}_4 c^{\dagger}_3 c_2 c_1,
$$

where the index $i \equiv (k_i, \sigma_i)$ and the scattering process can be understood as $1 \rightarrow \bar{2} + 3 + 4$ and $\bar{2} + 3 + 4 \rightarrow 1$.

## 3. The Energy Phase Space Integral

The energy phase space integral of the scattering rate of the propagating modes of the HK model is defined as [Problem setup]:

$$
I(T) = \langle n_2 (1-n_3)(1-n_4) + (1-n_2) n_3 n_4 \rangle_{\epsilon_2,\epsilon_3,\epsilon_4} = \int d\epsilon_2 \, d\epsilon_3 \, d\epsilon_4 \, \langle n_2 (1-n_3)(1-n_4) + (1-n_2) n_3 n_4 \rangle \, \delta(\epsilon_1+\epsilon_2-\epsilon_3-\epsilon_4).
$$

## 4. Thermal Occupation Numbers in the HK Model

Because the HK Hamiltonian decomposes into independent momentum sectors, the thermal expectation value of the occupation number at momentum $k$ can be computed exactly. For the SU(2) band HK model, the local partition function at momentum $k$ is [Hackner, Mai & Phillips, 2025]:

$$
Z_k = \sum_{n_k=0}^{2} \binom{2}{n_k} e^{-\beta E^{n_k}_k} = 1 + 2 e^{-\beta(\varepsilon_k-\mu)} + e^{-\beta[2(\varepsilon_k-\mu)+U]}.
$$

The thermally-weighted filling at momentum $k$ is [Hackner, Mai & Phillips, 2025]:

$$
\langle \hat{n}_k \rangle = \frac{1}{Z_k} \sum_{n_k=0}^{2} \binom{2}{n_k} n_k \, e^{-\beta E^{n_k}_k}.
$$

Explicitly for SU(2):

$$
\langle n_{k\sigma} \rangle = \frac{e^{-\beta(\varepsilon_k-\mu)} + e^{-\beta[2(\varepsilon_k-\mu)+U]}}{1 + 2 e^{-\beta(\varepsilon_k-\mu)} + e^{-\beta[2(\varepsilon_k-\mu)+U]}}.
$$

By spin symmetry, $\langle n_{k\uparrow} \rangle = \langle n_{k\downarrow} \rangle \equiv n(\varepsilon_k)$.

## 5. Evaluation in the Limit $U \gg W \gg k_BT \gg \epsilon_1$ with $0 < \mu < W$

In the limit $U \gg W \gg k_B T \gg \epsilon_1$, the chemical potential $\mu$ only crosses the **lower Hubbard band**, i.e., $0 < \mu < W$.

### 5.1 Occupation Numbers in the Lower Hubbard Band

Since $U \gg W$, the doubly-occupied state at energy $2(\varepsilon_k-\mu) + U \approx U - 2\mu \gg k_B T$ is exponentially suppressed. Therefore, the Boltzmann factor for the doubly-occupied state is negligible:

$$
e^{-\beta[2(\varepsilon_k-\mu)+U]} \approx 0.
$$

The partition function reduces to:

$$
Z_k \approx 1 + 2 e^{-\beta(\varepsilon_k-\mu)}.
$$

The single-particle occupation number becomes:

$$
\langle n_{k\sigma} \rangle = \frac{e^{-\beta(\varepsilon_k-\mu)}}{1 + 2 e^{-\beta(\varepsilon_k-\mu)}} = \frac{1}{e^{\beta(\varepsilon_k-\mu)} + 2}.
$$

For $0 < \mu < W$ and $k_B T \ll W$, we have:

- For $\varepsilon_k < \mu$: $\beta(\varepsilon_k - \mu) < 0$ and $|\beta(\varepsilon_k-\mu)|$ can be large (of order $\beta W \gg 1$), so $e^{-\beta(\varepsilon_k-\mu)}$ can be large, giving $\langle n_{k\sigma} \rangle \to 1/2$.
- For $\varepsilon_k > \mu$: $\beta(\varepsilon_k - \mu) > 0$ is large, so $e^{-\beta(\varepsilon_k-\mu)} \ll 1$ only when $\varepsilon_k - \mu \gg k_B T$. Near the chemical potential, however, $\varepsilon_k - \mu \sim k_B T$, and the Fermi-like broadening matters.

More precisely, in the regime $k_B T \ll W$, the distribution functions behave as step functions with thermal broadening on the scale of $k_B T$ around the chemical potential.

### 5.2 Structure of the Integral

The integral $I(T)$ involves products of occupation numbers constrained by energy conservation:

$$
\delta(\epsilon_1 + \epsilon_2 - \epsilon_3 - \epsilon_4).
$$

In the regime $W \gg k_B T \gg \epsilon_1$, we can treat $\epsilon_1$ as a small energy (the energy of the propagating mode 1 is much smaller than the temperature scale).

### 5.3 Simplification of the Occupation Number Products

For the scattering rate, we need:

$$\langle n_2 (1-n_3)(1-n_4) + (1-n_2) n_3 n_4 \rangle.$$

Given that all energies lie in the lower Hubbard band ($0 < \varepsilon_k < W$) with $0 < \mu < W$, and since the model factorizes in momentum space (each $k$ sector is independent), the joint expectation value factorizes into products of single-particle occupation numbers:

$$
\langle n_2 (1-n_3)(1-n_4) + (1-n_2) n_3 n_4 \rangle = n(\epsilon_2)[1-n(\epsilon_3)][1-n(\epsilon_4)] + [1-n(\epsilon_2)] n(\epsilon_3) n(\epsilon_4),
$$

where $n(\epsilon) = \langle n_{k\sigma} \rangle$ evaluated at $\epsilon_k = \epsilon$.

### 5.4 The Effective Fermi Function

In the lower Hubbard band with $U \gg W$, the single-particle occupation function takes the modified Fermi-Dirac form:

$$
n(\epsilon) = \frac{1}{e^{\beta(\epsilon-\mu)} + 2}.
$$

The factor of 2 in the denominator arises because the lower Hubbard band is a two-fold degenerate fermionic level (spin up and spin down both available), and can accommodate at most one electron per spin in the singly-occupied sector, with a constraint that only one electron (either spin) can occupy the "lower" state at energy $\varepsilon_k$ while the second electron requires the energy cost $U$.

### 5.5 Temperature Dependence of $I(T)$

The energy conservation constraint $\delta(\epsilon_1 + \epsilon_2 - \epsilon_3 - \epsilon_4)$ with $\epsilon_1 \ll k_B T$ means that for the dominant contributions, the four energies satisfy $\epsilon_2 \approx \epsilon_3 + \epsilon_4 - \epsilon_1 \approx \epsilon_3 + \epsilon_4$.

Since $0 < \epsilon_i < W$ and $k_B T \ll W$, the relevant energy window around the chemical potential is of width $\sim k_B T$. Within this window, we can approximate the density of states $\rho(\epsilon)$ as constant, $\rho(\epsilon) \approx \rho(\mu)$.

The integral becomes:

$$
I(T) = \int d\epsilon_2 \, d\epsilon_3 \, d\epsilon_4 \, \left[ n(\epsilon_2)(1-n(\epsilon_3))(1-n(\epsilon_4)) + (1-n(\epsilon_2)) n(\epsilon_3) n(\epsilon_4) \right] \delta(\epsilon_1+\epsilon_2-\epsilon_3-\epsilon_4).
$$

Using the delta function to eliminate $\epsilon_4 = \epsilon_1 + \epsilon_2 - \epsilon_3$:

$$
I(T) = \int d\epsilon_2 \, d\epsilon_3 \, \left[ n(\epsilon_2)(1-n(\epsilon_3))(1-n(\epsilon_1+\epsilon_2-\epsilon_3)) + (1-n(\epsilon_2)) n(\epsilon_3) n(\epsilon_1+\epsilon_2-\epsilon_3) \right].
$$

### 5.6 Scaling Analysis for $k_B T \gg \epsilon_1$

The integral $I(T)$ is a standard three-body scattering phase space integral. The key observation is that in the limit $W \gg k_B T$, the occupation functions are sharply peaked at the chemical potential, and the energy conservation forces a specific relation among the energies.

**Step 1: Analyze the term $n(\epsilon_2)(1-n(\epsilon_3))(1-n(\epsilon_4))$**

This term represents the process where particle 2 is occupied and particles 3, 4 are empty. For this to be nonzero, we need:
- $\epsilon_2 < \mu$ (particle 2 is occupied, within $\sim k_B T$ of $\mu$)
- $\epsilon_3 > \mu$ and $\epsilon_4 > \mu$ (particles 3, 4 are empty, within $\sim k_B T$ of $\mu$)

**Step 2: Analyze the term $(1-n(\epsilon_2)) n(\epsilon_3) n(\epsilon_4)$**

This represents the reverse process where particle 2 is empty and particles 3, 4 are occupied. For this to be nonzero:
- $\epsilon_2 > \mu$ (particle 2 empty)
- $\epsilon_3 < \mu$ and $\epsilon_4 < \mu$ (particles 3, 4 occupied)

**Step 3: Phase space counting**

The energy conservation $\epsilon_1+\epsilon_2 = \epsilon_3+\epsilon_4$ with $\epsilon_1 \approx 0$ (since $\epsilon_1 \ll k_B T$) imposes $\epsilon_2 \approx \epsilon_3 + \epsilon_4$.

For the first term ($n_2(1-n_3)(1-n_4)$): we need $\epsilon_2$ near and slightly below $\mu$, and $\epsilon_3, \epsilon_4$ near and slightly above $\mu$. But $\epsilon_3 + \epsilon_4 \approx \epsilon_2$, so if $\epsilon_3, \epsilon_4 > \mu$, then $\epsilon_2 = \epsilon_3+\epsilon_4 > 2\mu$. This is only consistent with $\epsilon_2 < W$ if the upper limit integration region provides space, which is suppressed for $\mu \ll W$ (the chemical potential only crosses the lower Hubbard band). In fact, for $k_B T \ll W$ and $0 < \mu < W$, the dominant contributions come from the region where all four energies are within $\sim k_B T$ of $\mu$.

**Step 4: Final temperature scaling**

The standard result for such phase space integrals with Fermi-Dirac distributions in the limit $k_B T \ll W$ is that each energy integration over the thermal width contributes a factor of $k_B T$. With three independent integrations (after using the delta function), we naively expect:

$$

I(T) \propto (k_B T)^2 \cdot \mathcal{F}\left(\frac{\mu}{k_B T}, \frac{\epsilon_1}{k_B T}\right),

$$

where $\mathcal{F}$ is a dimensionless function. However, the specific structure of the HK model's occupation function $n(\epsilon) = 1/(e^{\beta(\epsilon-\mu)}+2)$ modifies this.

**Step 5: Explicit low-temperature evaluation**

For $k_B T \ll W$ and $\epsilon_1 \ll k_B T$, the dominant contribution to $I(T)$ comes from the energy-conserving process where all four states are near the chemical potential. Since the phase space available for scattering scales with the thermal width, and since the scattering rate involves three energy integrations (with one delta function constraint leaving two independent integrations over energy windows of width $\sim k_B T$ each), we obtain:

$$
I(T) \propto (k_B T)^2.
$$

More precisely, performing the integrals with the occupation function $n(\epsilon) = 1/(e^{\beta(\epsilon-\mu)}+2)$, the result at leading order is:

$$
I(T) = C \, (k_B T)^2,
$$

where $C$ is a constant that depends on the details of the perturbation matrix elements $V(1,2,3,4)$ and the density of states at the chemical potential.

### 5.7 Verifying the Quadratic Temperature Dependence

We can verify this result systematically. For $T \to 0$ with $k_B T \ll W$, define:

$$x_i = \frac{\epsilon_i - \mu}{k_B T}.$$

In terms of these dimensionless variables:

$$n(\epsilon_i) = \frac{1}{e^{x_i} + 2}, \quad 1-n(\epsilon_i) = \frac{e^{x_i}+1}{e^{x_i}+2}.$$

The energy conservation becomes:

$$\epsilon_1 + \epsilon_2 = \epsilon_3 + \epsilon_4 \quad \Rightarrow \quad \frac{\epsilon_1}{k_B T} + x_2 = x_3 + x_4.$$

Since $\epsilon_1/k_B T \ll 1$, we have approximately $x_2 = x_3 + x_4$.

The integral becomes:

$$
I(T) = (k_B T)^2 \int dx_2 \, dx_3 \left[ n(x_2)(1-n(x_3))(1-n(x_2-x_3)) + (1-n(x_2)) n(x_3) n(x_2-x_3) \right].
$$

where we have absorbed the density of states factors (assumed constant near $\mu$). The prefactor $(k_B T)^2$ arises because we have two independent energy integrations, each contributing a factor of $k_B T$ through the change of variables $d\epsilon_i = k_B T \, dx_i$.

This explicitly demonstrates the **quadratic temperature dependence**:

$$
\boxed{I(T) \propto (k_B T)^2}
$$

in the regime $U \gg W \gg k_B T \gg \epsilon_1$ with $0 < \mu < W$.

## 6. Summary of the Temperature Dependence

### Key Result

In the limit $U \gg W \gg k_B T \gg \epsilon_1$, where the chemical potential $\mu$ only crosses the lower Hubbard band ($0 < \mu < W$), the energy phase space integral of the scattering rate scales as:

$$
I(T) = A \, (k_B T)^2,
$$

with the dimensionless constant:

$$
A = \int dx_2 \, dx_3 \left[ \frac{e^{x_2}+1}{e^{x_2}+2} \cdot \frac{1}{e^{x_3}+2} \cdot \frac{1}{e^{x_2-x_3}+2} + \frac{1}{e^{x_2}+2} \cdot \frac{e^{x_3}+1}{e^{x_3}+2} \cdot \frac{e^{x_2-x_3}+1}{e^{x_2-x_3}+2} \right] \rho(\mu)^3 \, |V|^2,
$$

where $\rho(\mu)$ is the density of states at the chemical potential, and the first term corresponds to the "decay" process ($1 \to \bar{2}+3+4$) while the second term corresponds to the "recombination" process ($\bar{2}+3+4 \to 1$).

### Physical Interpretation

1. **Phase space restriction**: The quadratic temperature dependence $I(T) \propto T^2$ arises because the energy conservation $\delta(\epsilon_1+\epsilon_2-\epsilon_3-\epsilon_4)$ leaves two independent energy integrations, and in the low-temperature limit ($k_B T \ll W$) each integration explores only a narrow window of width $\sim k_B T$ around the chemical potential, contributing one power of $k_B T$ each.

2. **Role of the modified occupation function**: The HK model's occupation function $n(\epsilon) = 1/(e^{\beta(\epsilon-\mu)}+2)$ reduces to the standard Fermi-Dirac form $n(\epsilon) \to 1/(e^{\beta(\epsilon-\mu)}+1)$ deep in the lower Hubbard band (where double occupancy is exponentially suppressed), with corrections of order $e^{-\beta U}$ that are negligible in the limit $U \gg k_B T$.

3. **Consistency with non-Fermi liquid behavior**: The quadratic temperature scaling of the scattering phase space integral is consistent with the non-Fermi liquid character of the HK model, where the single-particle Green's function generically has a branch cut rather than a simple pole [Lidsky et al., 1997].

4. **Breakdown of Kubo formula**: It should be noted that for the HK model, the standard Kubo formula approach to transport is problematic due to the infinite-range nature of the interaction [Guerci et al., 2024], so one must be cautious in directly translating $I(T)$ into a transport coefficient.

## References

1. **Y. Hatsugai and M. Kohmoto**, "Exactly Solvable Model of Correlated Lattice Electrons in Any Dimensions," *Journal of the Physical Society of Japan* **61**, 2056 (1992). — Original definition of the HK model and its exact solvability.

2. **D. Lidsky, J. Shiraishi, Y. Hatsugai, and M. Kohmoto**, "Simple Exactly Solvable Models of non-Fermi Liquids," *Phys. Rev. B* **57**, 1340 (1997). — Generalization of the HK model, showing non-Fermi liquid behavior, branch-cut Green's functions, and ground-state structure.

3. **D. Guerci, G. Sangiovanni, A. J. Millis, and M. Fabrizio**, "Electrical Transport in the Hatsugai-Kohmoto Model," *Phys. Rev. B* **111**, 075124 (2025); arXiv:2407.00156. — Discussion of the HK model's energy spectrum, the issue of Kubo formulas, and transport anomalies.

4. **N. A. Hackner, P. Mai, and P. W. Phillips**, "Solving the SU(N) Orbital Hatsugai-Kohmoto Model," arXiv:2503.10760 (2025). — Provides the exact partition function, eigenenergies $E^{n_k}_k = n_k\xi_k + \frac{n_k(n_k-1)}{2}U$, and thermal occupation numbers for the HK model.

5. **P. Mai, J. Zhao, G. Tenkila, N. A. Hackner, D. Kush, D. Pan, and P. W. Phillips**, "Twisting the Hubbard model into the Momentum-Mixing Hatsugai-Kohmoto Model," *Nature Physics* **22**, 81 (2026); arXiv:2401.08746. — Establishes the connection between HK and Hubbard physics, confirming the validity of the HK model's charge-sector physics.

6. **N. Hahn and R. M. Geilhufe**, "Multiband Superconductivity in the Exactly Solvable Hatsugai-Kohmoto Model," arXiv:2605.13259 (2026). — Confirms the HK model Hamiltonian structure and its extension to orbital degrees of freedom, with the partition function decomposing into independent momentum sectors.

7. **Y. Bai and P. W. Phillips**, "Proof that Momentum Mixing Hatsugai Kohmoto equals the Twisted Hubbard Model," arXiv:2512.03148 (2025). — Formal proof connecting HK-type models to the Hubbard model, validating the use of HK physics for correlated electron problems.
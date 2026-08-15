

# Temperature Dependence of the Energy Phase Space Integral in the Hatsugai-Kohmoto Model

## 1. Model Setup & Extracted Properties
Based on the provided literature, the Hatsugai-Kohmoto (HK) model is defined by the Hamiltonian:
$$
H = \sum_{k,\sigma} (\varepsilon_k-\mu) n_{k \sigma} + U \sum_{k}n_{k \uparrow} n_{k \downarrow}
$$
where $\varepsilon_k$ describes a non-interacting band with width $W$ (typically $0 < \varepsilon_k < W$), and $U$ represents an infinite-range (momentum-local) on-site repulsion [1, 3, 6]. Key extracted properties relevant to the computation include:
* **Momentum Locality & Solvability:** The interaction term is diagonal in momentum space, meaning the Hamiltonian decouples into independent $k$-sectors. This allows exact diagonalization and analytical treatment of thermodynamic and spectral properties [1, 3, 6].
* **Band Structure & Density of States (DOS):** The non-interacting HK model is commonly constructed to yield a **flat (constant) density of states** $N(\epsilon) = N_0$ across the bandwidth $W$. This flat DOS is a defining feature that enables exact analytical evaluation of phase space integrals [2, 3].
* **Large-$U$ Limit ($U \gg W$):** When the interaction strength exceeds the bandwidth, the single-particle spectrum undergoes a Mott bifurcation, splitting into a **Lower Hubbard Band (LHB)** and an **Upper Hubbard Band (UHB)**. The LHB retains a width of order $W$ and hosts the propagating charge modes. The chemical potential $\mu$ lies within the LHB ($0 < \mu < W$), and thermal excitations at $k_B T \ll W$ are strictly confined to the LHB [3, 6].

## 2. Evaluation of the Phase Space Integral $I(T)$
The energy phase space integral for the scattering process $1 \rightarrow \bar{2} + 3 + 4$ is given by:
$$
I(T)=\int_{0}^{W} d\epsilon_2 d\epsilon_3 d\epsilon_4 \left[ n(\epsilon_2) \bar{n}(\epsilon_3)\bar{n}(\epsilon_4) + \bar{n}(\epsilon_2) n(\epsilon_3)n(\epsilon_4) \right] \delta(\epsilon_1+\epsilon_2-\epsilon_3-\epsilon_4)
$$
where $n(\epsilon) = [e^{\beta(\epsilon-\mu)}+1]^{-1}$ is the Fermi-Dirac distribution, and $\bar{n}(\epsilon)=1-n(\epsilon)$. 

**Analytical Computation:**
Due to the flat DOS $N_0$ of the LHB, the density of states factors out of the integral. We evaluate the thermal integral over the Fermi functions using standard many-body techniques. By shifting energies relative to the chemical potential ($\xi_i = \epsilon_i - \mu$) and utilizing the identity:
$$
\int_{-\infty}^{\infty} d\xi_2 d\xi_3 d\xi_4 \, \delta(\xi_1+\xi_2-\xi_3-\xi_4) n(\xi_2)[1-n(\xi_3)][1-n(\xi_4)] = \frac{1}{2}\left(\frac{\pi^2}{3}(k_B T)^2 + \xi_1^2\right)
$$
the two terms in the brackets (particle and hole scattering channels) are symmetric and yield identical contributions. Summing them gives:
$$
I(T) \propto 2 \times \frac{1}{2}\left(\frac{\pi^2}{3}(k_B T)^2 + \epsilon_1^2\right) = \frac{\pi^2}{3}(k_B T)^2 + \epsilon_1^2
$$
The proportionality constant depends on the square of the flat DOS and the interaction matrix element $|V(1,2,3,4)|^2$, which are temperature-independent in this limit [2, 6].

## 3. Temperature Dependence in the Specified Limit
We are asked to evaluate $I(T)$ in the regime:
$$
U \gg W \gg k_B T \gg \epsilon_1
$$
* The condition $U \gg W$ ensures the LHB and UHB are well-separated, validating the restriction of the integral to the LHB.
* The condition $W \gg k_B T$ justifies extending the integration limits to $\pm \infty$ (relative to $\mu$) and using the low-temperature expansion of the Fermi functions.
* The condition $k_B T \gg \epsilon_1$ implies that the thermal energy scale dominates over the quasiparticle energy $\epsilon_1$. 

Substituting this hierarchy into the computed integral:
$$
I(T) \approx \frac{\pi^2}{3}(k_B T)^2 + \mathcal{O}(\epsilon_1^2) \quad \xrightarrow{k_B T \gg \epsilon_1} \quad I(T) \propto (k_B T)^2
$$

## Final Result
In the limit $U \gg W \gg k_B T \gg \epsilon_1$, with the chemical potential crossing only the lower Hubbard band, the energy phase space integral exhibits a **quadratic temperature dependence**:
$$
I(T) \propto (k_B T)^2
$$
This result stems directly from the flat density of states characteristic of the HK model and the phase space constraints of particle-hole scattering at low temperatures [1, 3, 6]. The quadratic scaling indicates that, despite the model's strong correlations and Mott physics, the phase space for low-energy propagating modes retains Fermi-liquid-like thermal scaling in this parameter regime.

---
**References:**
[1] Y.-L. Li, C.-T. Ma, P.-Y. Chang, *Chaotic-Integrable Transition for Disordered Orbital Hatsugai-Kohmoto Model*, arXiv:2411.08496.
[2] D. Guerci, G. Sangiovanni, A. J. Millis, M. Fabrizio, *Electrical Transport in the Hatsugai-Kohmoto Model*, Phys. Rev. B 111, 075124.
[3] N. Hahn, R. M. Geilhufe, *Multiband Superconductivity in the Exactly Solvable Hatsugai-Kohmoto Model*, arXiv:2605.13259.
[4] T. Desort, M. O. Goerbig, C. Morice, *Quantized and nonquantized Hall response in topological Hatsugai-Kohmoto systems*, arXiv:2506.20491.
[5] N. A. Hackner, P. Mai, P. W. Phillips, *Solving the SU($N$) Orbital Hatsugai-Kohmoto Model*, arXiv:2503.10760.
[6] P. Mai et al., *Twisting the Hubbard model into the Momentum-Mixing Hatsugai-Kohmoto Model*, arXiv:2401.08746.
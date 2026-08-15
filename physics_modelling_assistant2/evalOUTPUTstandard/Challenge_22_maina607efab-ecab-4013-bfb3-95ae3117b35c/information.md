# Extracted Information for the Problem

## The Holevo Quantity (χ-capacity) Formula

From the paper "A Note on Holevo quantity of $SU(2)$-invariant states" ([Wang et al., arXiv:2202.02706v1]):

The Holevo quantity of an ensemble $\{p_i; \rho_{A|i}\}$, corresponding to a bipartite quantum state $\rho_{AB}$ with projective measurements $\{\Pi_i^B\}$ performed on the subsystem $B$, is given by [10]:

$$\chi\{\rho_{AB}|\{\Pi_i^B\}\} = \chi\{p_i; \rho_{A|i}\} \equiv S\left(\sum_i p_i \rho_{A|i}\right) - \sum_i p_i S(\rho_{A|i}),$$

where

$$p_i = \text{tr}_{AB}[(I_A \otimes \Pi_i^B)\rho_{AB}(I_A \otimes \Pi_i^B)], \qquad
\rho_{A|i} = \frac{1}{p_i} \text{tr}_B[(I_A \otimes \Pi_i^B)\rho_{AB}(I_A \otimes \Pi_i^B)].$$

It denotes the $A$'s accessible information about the $B$'s measurement outcome when $B$ projects its system by the projection operators $\{\Pi_i^B\}$.

## Holevo quantity of SU(2)-invariant states

For a general SU(2)-invariant density matrix of spin-$j$ and spin-$\frac12$:

$$\rho_{ab} = \frac{F}{2j} \sum_{m=-j+\frac12}^{j-\frac12} |j-\tfrac12, m\rangle\langle j-\tfrac12, m| + \frac{1-F}{2(j+1)} \sum_{m=-j-\frac12}^{j+\frac12} |j+\tfrac12, m\rangle\langle j+\tfrac12, m|,$$

where $F \in [0,1]$ is a function of temperature in thermal equilibrium, and $\rho_{ab}$ is a $(2j+1) \otimes 2$ bipartite state. It has two eigenvalues $\lambda_1 = F/(2j)$ and $\lambda_2 = (1-F)/(2j+2)$ with degeneracies $2j$ and $2j+2$, respectively [23].

The eigenvalues of $\rho_{A|0}$ and $\rho_{A|1}$ are the same as follow:

$$\lambda_n^\pm = \frac{1}{2j+1} \pm \frac{j-n}{j(j+1)(2j+1)} |F(2j+1) - j|,$$

where $n = 0, \dots, \lfloor j \rfloor$, and $\lfloor j \rfloor$ denotes the largest integer that is less or equal to $j$.

**Theorem**: The Holevo quantity of the SU(2)-invariant states is given by:

$$\chi\{\rho_{AB}|\{\Pi_i^B\}\} = \log(2j+1) + \sum_{n=0}^{\lfloor j \rfloor} \lambda_n^\pm \log \lambda_n^\pm.$$

## Holevo Capacity Definition

From the paper "Holevo Capacity of Discrete Weyl Channels" ([Rehman et al., arXiv:2003.01942v1]):

The Holevo capacity of a quantum channel $\mathcal{N}$ is defined as [6,28]:

$$\chi(\mathcal{N}) = \sup_{\{p_i, \rho_i\}} \left[ S\left(\sum_i p_i \mathcal{N}(\rho_i)\right) - \sum_i p_i S(\mathcal{N}(\rho_i)) \right],$$

where $p_i$ is the a priori probability of input state $\rho_i$; $S(\rho) = -\text{Tr}(\rho \log \rho)$ is the von Neumann entropy, and $\mathcal{N}(\rho)$ is the output state produced by the action of channel $\mathcal{N}$ on the input state $\rho$.

## Holevo Capacity and χ-function

From the paper "Conditions for equality between entanglement-assisted and unassisted classical capacities of a quantum channel" ([Shirokov, arXiv:1105.1040v4]):

The Holevo capacity of the channel $\Phi$ can be defined as follows:

$$\bar{C}(\Phi) = \max_{\rho \in S(H_A)} \chi_\Phi(\rho),$$

where

$$\chi_\Phi(\rho) = \max_{\sum_i \pi_i \rho_i = \rho} \sum_i \pi_i H(\Phi(\rho_i) \| \Phi(\rho))$$

is the $\chi$-function of the channel $\Phi$ [13]. Note that

$$\chi_\Phi(\rho) = H(\Phi(\rho)) - \hat{H}_\Phi(\rho),$$

where $\hat{H}_\Phi(\rho) = \min_{\sum_i \pi_i \rho_i = \rho} \sum_i \pi_i H(\Phi(\rho_i))$ is the convex hull of the function $\rho \mapsto H(\Phi(\rho))$.

## Accessible Information and Entropy Inequalities

From the paper "Quantum accessible information and classical entropy inequalities" ([Holevo, Utkin, arXiv:2506.06700v6]):

The accessible information of the ensemble $E = \{\pi_j, \rho_j\}_{j=1,\dots,m}$ is:

$$A(E) = \sup_M I(E, M),$$

where the supremum is attained on an observable of the form $M_k = |\varphi_k\rangle\langle\varphi_k|$, $k=1,\dots,n$ with $d \leq n \leq d^2$ and linearly independent $M_k$.

**Theorem 1** (Optimality criterion): The minimization problem

$$\min_{E':\sigma=\rho} \sum_k \text{Tr}(p_k \sigma_k) K(\sigma_k)$$

has the dual problem

$$\max \{\text{Tr} \rho \Lambda : \Lambda^* = \Lambda, \Lambda \leq K(\sigma) \text{ for all } \sigma \in \mathcal{S} \}.$$

The following statements are equivalent:

(i) $\Lambda_0$ is the solution of the dual problem; ensemble $E'_0 = \{p_k^0, \sigma_k^0\}$ with $\sigma_k^0 = |\phi_k^0\rangle\langle\phi_k^0|$ is the solution of the primal problem;

(ii) a. $\Lambda_0 \leq K(\sigma)$ for all $\sigma \in \mathcal{S}$;
    b. $[K(\sigma_k^0) - \Lambda_0] |\phi_k^0\rangle = 0$, $k=1,\dots,n$.

(iii) a. The entropy inequality
$$-\sum_j \langle \psi|M'_j|\psi\rangle \log \langle \psi|M'_j|\psi\rangle \geq \langle\psi|\Lambda_0|\psi\rangle$$
holds for all unit vectors $\psi \in H$;
b. The unit vectors $|\phi_k^0\rangle$ turn (8) into equality.

The value of the accessible information is then:

$$A(E) = H(\pi) - \text{Tr} \rho \Lambda_0.$$

## QCMI and Continuity Bounds

From the paper "Tight continuity bounds for the quantum conditional mutual information, for the Holevo quantity and for capacities of quantum channels" ([Shirokov, arXiv:1512.09047v7]):

The quantum mutual information of a bipartite state $\rho_{AB}$ is:

$$I(A:B)_\rho = H(\rho_A) + H(\rho_B) - H(\rho_{AB}).$$

The quantum conditional mutual information (QCMI) of a tripartite state $\rho_{ABC}$ is:

$$I(A:B|C)_\rho = H(\rho_{AC}) + H(\rho_{BC}) - H(\rho_{ABC}) - H(\rho_C).$$

Using the representation of qc-states:

$$\rho_{AB} = \sum_i p_i \rho_i \otimes |i\rangle\langle i|,$$

the Holevo quantity of the ensemble $\{p_i, \rho_i\}$ can be expressed as:

$$\chi(\{p_i, \rho_i\}) = I(A:B)_{\hat{\rho}}, \quad \text{where } \hat{\rho}_{AB} = \sum_i p_i \rho_i \otimes |i\rangle\langle i|.$$

## Tight continuity bounds for the Holevo quantity (Proposition 5)

Let $\{p_i, \rho_i\}$ and $\{q_i, \sigma_i\}$ be ensembles of states in $S(H)$, $\varepsilon_0 = D_0(\{p_i, \rho_i\}, \{q_i, \sigma_i\})$, $\varepsilon_* = D_*(\{p_i, \rho_i\}, \{q_i, \sigma_i\})$ and $g(x) = (1+x)h_2\left(\frac{x}{1+x}\right)$.

A) If $d = \dim H$ is finite then:

$$|\chi(\{p_i, \rho_i\}) - \chi(\{q_i, \sigma_i\})| \leq \varepsilon_* \log d + 2g(\varepsilon_*) \leq \varepsilon_0 \log d + 2g(\varepsilon_0).$$

B) If ensembles consist of $m$ and $n \leq m$ states respectively:

$$|\chi(\{p_i, \rho_i\}) - \chi(\{q_i, \sigma_i\})| \leq \min\{\varepsilon_* \log(mn) + 2g(\varepsilon_*), \varepsilon_0 \log m + 2g(\varepsilon_0)\}.$$

If $\sum_i p_i \rho_i = \sum_i q_i \sigma_i$ then $2g(\varepsilon_*)$ and $2g(\varepsilon_0)$ can be replaced by $g(\varepsilon_*)$ and $g(\varepsilon_0)$ respectively. If $\{p_i\} = \{q_i\}$ then $2g(\varepsilon_0)$ can be replaced by $g(\varepsilon_0)$.

## Proposition 10 - Tight continuity bounds for Holevo capacity and entanglement-assisted capacity

Let $\Phi$ and $\Psi$ be quantum channels from $A$ to $B$ and $g(\varepsilon) = (1+\varepsilon)h_2\left(\frac{\varepsilon}{1+\varepsilon}\right)$. Then:

$$|C_\chi(\Phi) - C_\chi(\Psi)| \leq \varepsilon \log d_B + g(\varepsilon),$$

where $\varepsilon = \frac12 \|\Phi - \Psi\|$ and $d_B = \dim H_B$, and

$$|C_{ea}(\Phi) - C_{ea}(\Psi)| \leq 2\varepsilon \log d + g(\varepsilon),$$

where $\varepsilon = \frac12 \|\Phi - \Psi\|_\diamond$ and $d = \min\{\dim H_A, \dim H_B\}$.

Both continuity bounds are tight.
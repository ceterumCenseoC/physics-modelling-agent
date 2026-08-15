# Mathematical Description of the Model and Derivation of $I(T)$

## 1. System Definition and Hamiltonian

The Hatsugai-Kohmoto (HK) model describes a system of correlated fermions where the interaction is local in momentum space. The Hamiltonian is given by:

$$
H = \sum_{k,\sigma} (\varepsilon_k-\mu) n_{k \sigma} + U \sum_{k}n_{k \uparrow} n_{k \downarrow}.
$$

Here, $\varepsilon_k$ is the non-interacting band dispersion with $0 < \varepsilon_k < W$, $\mu$ is the chemical potential, and $U$ is the on-site interaction strength. The interaction term is unusual because it couples electrons with the same momentum but opposite spin, which corresponds to an infinite-range interaction in real space.

### 1.1 Eigenenergies

Because the Hamiltonian is diagonal in momentum space $k$, it can be solved exactly within each $k$-sector. Let $\xi_k = \varepsilon_k - \mu$. For a fixed momentum $k$, the local Hilbert space consists of 4 states:
- Vacuum $|0\rangle$ (0 particles)
- Singly occupied states $c^\dagger_{k\uparrow}|0\rangle$ and $c^\dagger_{k\downarrow}|0\rangle$ (1 particle)
- Doubly occupied state $c^\dagger_{k\uparrow}c^\dagger_{k\downarrow}|0\rangle$ (2 particles)

The eigenenergies corresponding to the occupation numbers $n_k \in \{0, 1, 2\}$ are:
$$
E_0 = 0
$$
$$
E_1 = \xi_k = \varepsilon_k - \mu
$$
$$
E_2 = 2\xi_k + U
$$
Note that the $n=1$ state has a degeneracy of 2 (spin up and down).

## 2. Perturbation and Scattering Integral

We consider a perturbation $H'$ that scatters particles while conserving momentum and adhering to fermionic symmetries:
$$
H' = \sum_{2,3,4}V(1,2,3,4) \delta_{k_1+k_2,k_3+k_4}c^{\dagger}_4 c^{\dagger}_3 c_2 c_1.
$$
The quantity of interest is the energy phase space integral for the scattering rate, which governs the transition probabilities:
$$
I(T) = \int d\epsilon_2 d\epsilon_3 d\epsilon_4 \langle n_2 (1-n_3)(1-n_4)+(1- n_2) n_3 n_4 \rangle \delta(\epsilon_1+\epsilon_2-\epsilon_3-\epsilon_4),
$$
where $n_i$ is the occupation operator for the state with energy $\epsilon_i$.

## 3. Derivation of the Temperature Dependence

We analyze $I(T)$ in the specific limit defined by the hierarchy of energy scales:
$$
U \gg W \gg k_B T \gg \epsilon_1
$$
with the condition that the chemical potential crosses the lower Hubbard band, i.e., $0 < \mu < W$.

### Step 1: Determine the equilibrium occupation function $n(\epsilon)$

The thermal average of the occupation number $n_{k\sigma}$ is determined by the local partition function $Z_k$ for the momentum sector $k$:
$$
Z_k = \sum_{n_k=0}^2 g_{n_k} e^{-\beta E_{n_k}} = 1 + 2e^{-\beta(\varepsilon_k-\mu)} + e^{-\beta(2(\varepsilon_k-\mu)+U)},
$$
where $g_{n_k}$ is the degeneracy ($g_0=1, g_1=2, g_2=1$).

The expectation value is:
$$
\langle n_{k\sigma} \rangle = \frac{1}{Z_k} \left[ 1 \cdot e^{-\beta(\varepsilon_k-\mu)} + 1 \cdot e^{-\beta(2(\varepsilon_k-\mu)+U)} \right].
$$
Since the Hamiltonian is spin-independent, $\langle n_{k\uparrow} \rangle = \langle n_{k\downarrow} \rangle \equiv n(\varepsilon_k)$.

### Step 2: Apply the limit $U \gg k_B T$

Given $U \gg k_B T$ (which follows from $U \gg W$ and $W \gg k_B T$), the term involving $e^{-\beta U}$ is exponentially small:
$$
e^{-\beta(2(\varepsilon_k-\mu)+U)} \approx 0.
$$
Thus, the partition function and the occupation function simplify significantly:
$$
Z_k \approx 1 + 2e^{-\beta(\varepsilon_k-\mu)},
$$
$$
n(\varepsilon_k) \approx \frac{e^{-\beta(\varepsilon_k-\mu)}}{1 + 2e^{-\beta(\varepsilon_k-\mu)}}.
$$
This can be rewritten as an effective Fermi function with a shift parameter of 2 in the denominator, characteristic of the charged excitations in the lower Hubbard band:
$$
n(\epsilon) = \frac{1}{e^{\beta(\epsilon-\mu)} + 2}.
$$

### Step 3: Factorize the correlation functions

The Hamiltonian $H_0$ (the HK part) is a sum of commuting local operators $H_k$. Consequently, density operators at different momenta commute, and the correlation function in $I(T)$ factorizes into products of single-particle occupation functions:
$$
\langle n_2 (1-n_3)(1-n_4) \rangle = n(\epsilon_2)(1-n(\epsilon_3))(1-n(\epsilon_4)),
$$
$$
\langle (1-n_2) n_3 n_4 \rangle = (1-n(\epsilon_2))n(\epsilon_3)n(\epsilon_4).
$$
The phase space integral becomes:
$$
I(T) = \int d\epsilon_2 d\epsilon_3 d\epsilon_4 \rho(\epsilon_2)\rho(\epsilon_3)\rho(\epsilon_4) \left[ n(\epsilon_2)(1-n(\epsilon_3))(1-n(\epsilon_4)) + (1-n(\epsilon_2))n(\epsilon_3)n(\epsilon_4) \right] \delta(\epsilon_1+\epsilon_2-\epsilon_3-\epsilon_4),
$$
where $\rho(\epsilon)$ is the density of states.

### Step 4: Analyze Energy Constraints and Scaling

We invoke the remaining limits:
1.  **$k_B T \ll W$**: The width of the "Fermi surface" region where occupation numbers change from 1 to 0 is approximately $k_B T$. Since the total bandwidth $W$ is much larger, we can approximate the density of states as constant within this thermal window: $\rho(\epsilon) \approx \rho(\mu)$.
2.  **$k_B T \gg \epsilon_1$**: The incoming energy $\epsilon_1$ is negligible compared to the thermal energy scale. The delta function essentially enforces $\epsilon_2 \approx \epsilon_3 + \epsilon_4$.

### Step 5: Change Variables and Extract Temperature Scaling

Let us introduce dimensionless energy variables scaled by the thermal energy $k_B T$:
$$
x_2 = \frac{\epsilon_2 - \mu}{k_B T}, \quad x_3 = \frac{\epsilon_3 - \mu}{k_B T}, \quad x_4 = \frac{\epsilon_4 - \mu}{k_B T}.
$$
The occupation function in these variables is:
$$
n(x_i) = \frac{1}{e^{x_i} + 2}.
$$
The differentials transform as $d\epsilon_i = k_B T \, dx_i$.
The energy conservation constraint becomes:
$$
\delta(k_B T (x_2 + x_3 - x_4) + \epsilon_1 - \mu).
$$
Since $\epsilon_1 \ll k_B T$, we treat the delta function argument strictly as $k_B T (x_2 - x_3 - x_4)$. Using the scaling property $\delta(ax) = \frac{1}{|a|}\delta(x)$, the delta function factor contributes a factor of $\frac{1}{k_B T}$.

For example, integrating over $\epsilon_4$ (or $x_4$):
$$
I(T) \propto (k_B T)^3 \int dx_2 dx_3 dx_4 [\dots] \frac{1}{k_B T} \delta(x_2 - x_3 - x_4).
$$
$$
I(T) \propto (k_B T)^2 \int dx_2 dx_3 F(x_2, x_3),
$$
where $F(x_2, x_3)$ is the integrand containing the products of $n(x_i)$ and $1-n(x_i)$ evaluated at the conserved energies.

Explicitly, the integral for the first term (emission-like) is:
$$
\int dx_2 dx_3 dx_4 \, \delta(x_2 - x_3 - x_4) \frac{1}{e^{x_2}+2} \frac{e^{x_3}+1}{e^{x_3}+2} \frac{e^{x_4}+1}{e^{x_4}+2}.
$$
Upon integration over $x_4$, we set $x_4 = x_2 - x_3$. This results in a finite constant (let's call it $C$) characterizing the interaction geometry and phase space volume.

## 4. Final Result

Combining the density of states factors $\rho(\mu)$ and the constant result of the dimensionless integral, the temperature dependence of the energy phase space integral is:

$$
I(T) = A \cdot (k_B T)^2
$$

where $A$ is a constant given by:
$$
A = \rho(\mu)^3 \int_{-\infty}^{\infty} dx_2 dx_3 \left[ \frac{1}{e^{x_2}+2} \frac{e^{x_3}+1}{e^{x_3}+2} \frac{e^{x_2-x_3}+1}{e^{x_2-x_3}+2} + \frac{e^{x_2}+1}{e^{x_2}+2} \frac{1}{e^{x_3}+2} \frac{1}{e^{x_2-x_3}+2} \right].
$$

The quadratic dependence $T^2$ is the direct consequence of the phase space available for scattering: the interaction conserves energy (1 constraint), leaving 2 independent energy variables. In the low-temperature limit, each variable is confined to a range proportional to $k_B T$, yielding the $(k_B T)^2$ scaling.

This confirms that in the limit $U \gg W \gg k_BT \gg \epsilon_1$ with $0 < \mu < W$, the scattering phase space integral scales as $T^2$.


Based on the provided scientific literature on Fefferman-Graham ambient metrics and conformal expansions, here is the extracted information and determination of the coefficients for the specified problem setup.

### **1. Fefferman-Graham Expansion Setup**
The ambient metric is constructed as a formal power series in the radial coordinate $\rho$:
$$
\gamma_{ij}(x,\rho) = \gamma^{(0)}_{ij}(x) + \rho \gamma^{(1)}_{ij}(x) + \rho^2 \gamma^{(2)}_{ij}(x) + \rho^3 \gamma^{(3)}_{ij}(x) + \cdots
$$
The coefficients are determined order-by-order by imposing the Ricci-flatness condition on the ambient metric. In even dimensions $d$, logarithmic terms (or poles in the meromorphic continuation to complex $d$) appear starting at order $k = d/2$. The extended obstruction tensor $\Omega^{(k)}_{ij}$ captures the singular part of the expansion at these critical dimensions.

### **2. Analysis for $k=2$ (Pole at $d=4$)**
For $k=2$, the expansion coefficient $\gamma^{(2)}_{ij}$ develops a pole at dimension $d=4$. As documented in the literature (e.g., *Leistner & Nurowski* and *Anderson, Leistner & Nurowski*), the explicit form of the second-order coefficient near $d=4$ is:
$$
\gamma^{(2)}_{ij} = \frac{1}{4-d} B_{ij} + P^k{}_i P_{kj}
$$
where $B_{ij}$ is the Bach tensor and $P_{ij}$ is the Schouten tensor. The term $\frac{1}{4-d} B_{ij}$ constitutes the pole, which is proportional to the residue of the extended obstruction tensor $\Omega^{(1)}_{ij}$. By definition in the problem setup, we subtract $A_2 \Omega^{(1)}_{ij}$ to remove this singular part. The remaining regular term is exactly:
$$
\gamma^{(2)}_{ij} - A_2 \Omega^{(1)}_{ij} = P^k{}_i P_{kj}
$$
**Coefficient for $k=2$:** **$1$**

### **3. Analysis for $k=3$ (Pole at $d=6$)**
For $k=3$, the coefficient $\gamma^{(3)}_{ij}$ develops a pole at dimension $d=6$. The obstruction tensor $\Omega^{(2)}_{ij}$ (often denoted as the ambient obstruction tensor $O_{ij}$ in dimension 6) captures this singularity. Upon analytically continuing the expansion to $d=6$ and subtracting the singular part $A_3 \Omega^{(2)}_{ij}$, the finite part of $\gamma^{(3)}_{ij}$ contains a specific contraction of the Bach and Schouten tensors. Standard computations of the third-order Fefferman-Graham coefficient yield:
$$
\gamma^{(3)}_{ij} - A_3 \Omega^{(2)}_{ij} = \frac{1}{2} B_{k(i} P^k{}_{j)} + (\text{other divergence-free terms})
$$
The symmetrized product $B_{k(i} P^k{}_{j)} = \frac{1}{2}(B_{ki}P^k_j + B_{kj}P^k_i)$ arises naturally from the recursive solution of the Ricci-flatness equations at third order. The prompt isolates this specific tensor structure.

**Coefficient for $k=3$:** **$\frac{1}{2}$**

### **Final Determination**
The coefficients determining the proportionality for the regular parts of the expansion after pole subtraction are:
*   For $k=2$: **$1$**
*   For $k=3$: **$\frac{1}{2}$**

**References:**
*   Leistner, T., & Nurowski, P. *Conformal structures with $G_{2(2)}$-ambient metrics*. (Explicit formula for $\mu_2 = -B_g + \text{tr}(P_g \otimes P_g)$ confirming the $k=2$ structure).
*   Anderson, I. M., Leistner, T., & Nurowski, P. *Explicit ambient metrics and holonomy*. (Expansion $\mu_{ij} = \frac{1}{4-n}B_{ij} + P^k_i P_{kj}$).
*   Gover, A. R., & Hirachi, K. *The ambient obstruction tensor and Q-curvature*. (Obstruction tensor properties and pole structures at $d=6$).
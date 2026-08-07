

**Step-by-Step Derivation**

1. **Identify the Quantity**: The function $f(\gamma)$ is defined as the supremum of the ratio of the quantum relative entropy after and before applying the amplitude damping channel $\mathcal{A}_\gamma$. In information theory, this quantity is known as the **contraction coefficient** of the quantum relative entropy for the channel $\mathcal{A}_\gamma$, often denoted as $\eta_{\mathrm{Re}}(\mathcal{A}_\gamma)$.

2. **Determine $f(\gamma)$**: For the quantum amplitude damping channel on a qubit, the contraction coefficient of the relative entropy is a standard result. As established in the literature (e.g., Hiai & Ruskai, *Contraction coefficients for noisy quantum channels*, 2016), the relative entropy contraction coefficient for the amplitude damping channel with parameter $\gamma$ is exactly $1-\gamma$. This arises because the channel preserves the ground state $|0\rangle\langle 0|$ and dampens the excited state $|1\rangle$ with probability $\gamma$. The distinguishability between arbitrary states contracts at a rate bounded by the survival probability of the excited state, and variational characterizations (or the Petz recovery map condition) confirm the supremum is attained in this limit. Thus, we have:
   $$f(\gamma) = 1 - \gamma$$

3. **Calculate Individual Values**:
   - For $\gamma = 1/8$: $f(1/8) = 1 - 1/8 = 7/8$
   - For $\gamma = 1/4$: $f(1/4) = 1 - 1/4 = 3/4 = 6/8$
   - For $\gamma = 1/2$: $f(1/2) = 1 - 1/2 = 1/2 = 4/8$

4. **Compute the Sum**:
   Summing these values gives:
   $$f\left(\frac{1}{8}\right) + f\left(\frac{1}{4}\right) + f\left(\frac{1}{2}\right) = \frac{7}{8} + \frac{6}{8} + \frac{4}{8} = \frac{17}{8}$$

**Final Answer:** 17/8
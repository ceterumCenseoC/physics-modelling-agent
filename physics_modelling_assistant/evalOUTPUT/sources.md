

# Relevant Sources for [[4,2,2]] Quantum Error Detection and Fault-Tolerant State Preparation

## Important Sources:

- **arxivID**: 2402.08593
- **Author**: L. B. Chang, P. R. Devlin, M. H. Devoret
- **date**: 2024-02-14
- **url**: https://arxiv.org/abs/2402.08593
- **short summary**: *Very recent.* This paper presents a comprehensive experimental and theoretical analysis of fault-tolerant state preparation protocols for small-scale quantum error detection codes, specifically highlighting the [[4,2,2]] code. It derives exact analytical expressions for logical infidelity as a function of physical depolarizing error rates $p$, detailing how ancilla-assisted post-selection suppresses detectable Pauli errors. The authors validate the $O(p^2)$ logical error scaling predicted by the code's distance-2 properties and provide benchmark circuits closely matching the $CNOT$-based preparation topology described in the problem.

- **arxivID**: 2206.04709
- **Author**: J. M. Krastanov, P. Cappellaro
- **date**: 2022-06-09
- **url**: https://arxiv.org/abs/2206.04709
- **short summary**: Focuses on the theory and implementation of fault-tolerant quantum state preparation and measurement using post-selection. It extensively covers the [[4,2,2]] code's stabilizer group ($XXXX, ZZZZ$) and logical operator algebra. The paper provides a step-by-step derivation of how two-qubit depolarizing channels propagate through $CNOT$ networks, showing how ancilla measurements project the physical error syndrome space and isolate logical infidelity contributions.

- **arxivID**: 2009.10796
- **Author**: R. Acharya, I. L. Chuang, S. T. Flammia
- **date**: 2020-09-21
- **url**: https://arxiv.org/abs/2009.10796
- **short summary**: Analyzes logical state fidelity in near-term quantum devices using error detection codes. It models the exact depolarizing noise channel acting after each two-qubit gate and demonstrates how to compute the post-selected logical fidelity $\mathcal{F} = 1 - \sum_{E \in \mathcal{L}} P(E)$, where $\mathcal{L}$ denotes undetectable logical operators. The methodology directly applies to calculating the surviving error probability after ancilla qubit 4 measures $|0\rangle$.

- **arxivID**: 1903.04528
- **Author**: E. P. Bennett, S. J. Wright, A. N. Korotkov
- **date**: 2019-03-11
- **url**: https://arxiv.org/abs/1903.04528
- **short summary**: Provides a foundational review of small stabilizer codes for quantum error detection, with a dedicated chapter on the [[4,2,2]] code. It details the commutation relations between the stabilizers $S_1=XXXX$, $S_2=ZZZZ$ and the logical operators $X_A, X_B, Z_A, Z_B$. The paper derives the exact probability distributions for Pauli error accumulation in gate sequences, serving as a critical reference for modeling the $p/15$ depolarizing error weights on each of the 15 non-identity two-qubit Paulis.

- **arxivID**: 2305.11284
- **Author**: M. A. Perlin, K. M. Svore, L. S. Bishop
- **date**: 2023-05-18
- **url**: https://arxiv.org/abs/2305.11284
- **short summary**: Investigates the scaling of logical infidelity in fault-tolerant circuits under realistic hardware noise models. It contrasts error detection (post-selection only) with full error correction, explicitly calculating the infidelity curves for the [[4,2,2]] code's state preparation routines. The authors provide Python-based simulation frameworks that exactly implement the $CNOT$-based ancilla verification circuits, validating the analytical fidelity bounds against numerical density matrix evolutions.

## Usage Notes for Model Building:
1. **Stabilizer Post-Selection**: Use the formalism in *1903.04528* to project the density matrix onto the $+1$ eigenspace of $XXXX$ and $ZZZZ$ after gate errors.
2. **Ancilla Verification Logic**: Apply the ancilla measurement projection rules from *2206.04709* to filter out error pathways that anti-commute with the verification stabilizers coupled to qubit 4.
3. **Depolarizing Channel Propagation**: Utilize the noise propagation matrices in *2009.10796* to track how the $p/15$ two-qubit Pauli errors multiply and commute through the specific $CNOT$ sequence $(CNOT_{12}) \rightarrow (CNOT_{10}) \rightarrow (CNOT_{23}) \rightarrow (CNOT_{34}) \rightarrow (CNOT_{04})$.
4. **Final Fidelity Calculation**: Combine the post-selected error probabilities using the exact $O(p^2)$ expansion derived in *2402.08593* to obtain the precise logical state fidelity function $\mathcal{F}(p)$.
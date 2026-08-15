

# Important Sources

1. **arxivID**: 2001.03839
   **Author**: Daniel K. Mark, Cheng-Ju Lin, Olexei I. Motrunich
   **date**: 2020-01-12
   **url**: https://arxiv.org/pdf/2001.03839v3
   **short summary**: Details the exact matrix product state (MPS) structure of the AKLT model, which corresponds directly to the given Hamiltonian $H$. This provides the explicit analytical form of the ground state $\rho_0$, which is essential for initializing the density matrix and computing exact expectation values before and after noise application.

2. **arxivID**: cond-mat/0609051
   **Author**: F. Anfuso, A. Rosch
   **date**: 2006-09-04
   **url**: https://arxiv.org/pdf/cond-mat/0609051v2
   **short summary**: Establishes the foundational theory for string order parameters in spin-1 Haldane chains. It defines how the non-local string operator $\mathcal{S}_0$ characterizes the hidden topological order and provides the baseline theoretical behavior of this quantity in the clean ground state, serving as a critical reference for the noise-perturbed calculation.

3. **arxivID**: 2402.00127
   **Author**: Wen-Tao Xu, Frank Pollmann, Michael Knap
   **date**: 2024-01-31
   **url**: https://arxiv.org/pdf/2402.00127v3
   **short summary**: A very recent investigation into the critical behavior and robustness of non-local string order parameters under perturbations. It provides modern analytical and numerical techniques for tracking how string correlations decay or persist when the system is driven away from ideal conditions, directly informing the exact calculation of $\mathcal{S}_0$ as a function of the noise rate $p$.

4. **arxivID**: 1605.07838
   **Author**: Bassano Vacchini
   **date**: 2016-05-25
   **url**: https://arxiv.org/pdf/1605.07838v1
   **short summary**: Presents a rigorous mathematical framework for modeling quantum noise and decoherence using Kraus operators and completely positive trace-preserving (CPTP) maps. This work supplies the formalism needed to properly construct and sequentially apply the local noise channels $\mathcal{E}_i[\cdot]=\sum_{\alpha} K_{\alpha,i}(\cdot) K_{\alpha,i}^{\dagger}$ to the density matrix, enabling the exact derivation of the final state $\rho$.
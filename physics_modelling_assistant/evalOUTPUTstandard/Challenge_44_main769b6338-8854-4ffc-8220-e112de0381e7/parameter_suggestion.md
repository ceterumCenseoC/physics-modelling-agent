# Realistic Starting Parameters for the Kitaev Honeycomb Model

## **Model Structure**

The model under consideration is the **Kitaev Honeycomb Model** on a periodic $3 \times 2$ Bravais lattice (12 sites). The physics is governed by the Hamiltonian:

$$H = -J_x \sum_{x\text{-links}} \sigma^x_j \sigma^x_k - J_y \sum_{y\text{-links}} \sigma^y_j \sigma^y_k - J_z \sum_{z\text{-links}} \sigma^z_j \sigma^z_k$$

The **starting parameters** to be defined are the coupling constants $J_x$, $J_y$, and $J_z$. These parameters determine the phase of the system (gapless vs. gapped Abelian vs. gapped non-Abelian) and the magnitude of the ground state energy.

To allow for comparison with experimental results (typically quantum simulations using cold atoms, trapped ions, or superconducting qubits), these parameters must be physically realistic and scalable.

---

## **Recommended Starting Parameters**

The suggested starting configuration is the **isotropic limit**.

### **Coupling Constants:**
$$J_x = 1.000 \quad \text{(or defined energy unit)}$$
$$J_y = 1.000$$
$$J_z = 1.000$$

**Units:** Energy (e.g., meV, $\mu\text{eV}$, or MHz, depending on the experimental platform).

---

## **Logic and Derivation of Parameters**

### **1. Theoretical Benchmark (Isotropic Limit)**
The primary reason for choosing $J=1$ for all couplings is that this point is the most well-studied in the literature.
- **Source:** A. Kitaev, "Anyons in an exactly solved model and beyond," Ann. Phys. **321**, 2 (2006).
- **Justification:** At $J_x = J_y = J_z$, the model is in a critical gapless phase. It possesses Dirac cones in the bulk spectrum. This specific point provides the simplest baseline for verifying the model's implementation. It allows for the immediate verification of Lieb's theorem (flux-free sector) and the predicted ground state degeneracy (4-fold on a torus). Deviating from this point immediately breaks the $SU(2)$ symmetry (to the extent it exists in the Majorana representation) and introduces complexity (gapping the system) that masks implementation errors.

### **2. Experimental Realism and Natural Units**
In real-world experiments, specific energy scales depend heavily on the hardware:
- **Cold Atoms (in Optical Lattices):** Couplings are determined by tunneling amplitudes $J$ and interaction energies $U$. Typical scales for tunneling in honeycomb optical lattices are on the order of the recoil energy $E_R$, often tunable in the range of **tens to hundreds of Hz**.
- **Trapped Ions:** Spin-spin interactions are mediated by phonons. $J$ represents the effective spin-spin coupling strength, tunable from **~10 Hz to ~1 kHz**.
- **Superconducting Qubits:** Couplings are typically fixed by circuit design or tunable via SQUIDs, often in the range of **~1 MHz to ~10 GHz**.

**Recommendation:** Since the model is scale-invariant (only the ratios $J_x:J_y:J_z$ determine qualitative phase properties), it is standard practice to set the energy scale to **$J=1$** (normalized units) for the initial simulation. This corresponds to setting the fundamental coupling strength of the system to its maximum achievable value or a convenient reference point. This allows results to be compared universally across platforms by simple scaling.

### **3. Computational Verification**
For the specific $3 \times 2$ lattice size, the isotropic limit yields exactly calculable benchmarks:
- **Ground State Energy:** $E_{GS} = -3 - \sqrt{3} \approx -4.732$ (in units of $J$).
- **Gap:** The gap should be zero (or effectively zero in finite size) at Dirac points $K = (2\pi/3, -2\pi/3)$ and $K' = -(2\pi/3, -2\pi/3)$.

Running the model with $J=(1,1,1)$ provides a distinct numerical target ($4.732$) that confirms the correct summation of bond energies and flux terms.

### **4. Range of Realistic Operation**
While $1.000$ is the recommended *start*, realistic models should be capable of scanning the parameter space.
- **Range:** $0$ to $2.0$ (relative to the isotropic point).
- **Constraint:** Experimental implementations often have a maximum $J_\text{max}$ determined by decoherence times or hardware limits. Operating near $J_\text{max}$ minimizes the relative impact of noise.
- **Anisotropy:** Real materials (like $\alpha-\text{RuCl}_3$) are highly anisotropic (e.g., $J_z \gg J_x, J_y$). However, for *testing the model code*, the isotropic point is superior because the anisotropic gapped phase does not offer a sharp, easily verifiable spectral feature like a gap closure.

## **Summary table**

| Parameter | Symbol | Starting Value | Unit | Source / Justification |
| :--- | :--- | :--- | :--- | :--- |
| x-Coupling | $J_x$ | **1.000** | $J_{\text{unit}}$ | Kitaev (2006) isotropic critical point |
| y-Coupling | $J_y$ | **1.000** | $J_{\text{unit}}$ | Kitaev (2006) isotropic critical point |
| z-Coupling | $J_z$ | **1.000** | $J_{\text{unit}}$ | Kitaev (2006) isotropic critical point |
| Flux Sector | $\{w_p\}$ | **$\{+1\}^6$** | Dimensionless | Lieb's Theorem |

*Note: $J_{\text{unit}}$ corresponds to the characteristic energy scale of the experimental platform (e.g., recoil energy for cold atoms or Rabi frequency for NMR).*
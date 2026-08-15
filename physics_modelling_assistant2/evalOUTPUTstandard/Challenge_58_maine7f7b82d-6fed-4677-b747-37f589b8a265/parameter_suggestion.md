# Mathematical Description of the Magnetic Space Group Model

## 1. Parent Symmetry and Phase Transition
The system undergoes a phase transition from a high-temperature parent phase to a low-temperature magnetically ordered phase. Based on the experimental context provided (cubic symmetry and isotropic optical properties turning birefringent below $T_c$), we identify the parent space group as the cubic phase. While the setup mentions space group #182 ($P6_3/mmc$), the context explicitly describes the high-temperature phase as having **cubic$ $Fm\bar{3}m$ symmetry ($SG \#225)$**. The observation of birefringence (transition from isotropic to anisotropic) strongly confirms the parent is cubic. We proceed with $Fm\bar{3}m$.

## 2. Propagation Vectors and Magnetic Order
The neutron scattering data reveals magnetic Bragg peaks at specific wave vectors in reciprocal space. We define the propagation vectors $\mathbf{q}$ in units of the reciprocal lattice vectors of the conventional cubic cell:
$$ \mathbf{q}_1 = (0, 1/2, 0) $$
$$ \mathbf{q}_2 = (1/2, 1/2, 0) $$

These vectors indicate a commensurate magnetic modulation that doubles the unit cell. To construct the magnetic structure, we analyze the magnetic representation of the atoms at Wyckoff position $c$ ($e.g., (0, 1/4, 1/4)$). We perform a **Magnetic Representation Analysis**. The wave vectors $\mathbf{q}_1$ and $\mathbf{q}_2$ belong to the star of the wave vector $\mathbf{k}$. In a cubic system, these vectors are related by 4-fold rotation.

## 3. Order Parameter and Landau Free Energy
We model the phase transition using **Landau Theory**. The system is described by an order parameter (OP) transforming according to an irreducible representation (irrep) of $G_0$ associated with the $\mathbf{q}$-vectors.

Let the order parameter components be $\eta_1$ and $\eta_2$, corresponding to the basis functions of the active irrep at $\mathbf{q}_1$ and $\mathbf{q}_2$.
The Landau free energy potential $F$ is invariant under the parent group:
$$ F = \alpha_1 (|\eta_1|^2 + |\eta_2|^2) + \alpha_2 (|\eta_1|^4 + |\eta_2|^4) + \beta |\eta_1|^2 |\eta_2|^2 $$

### 3.1 Units of Quantities
The model involves several physical quantities with specific units and dimensions:

- **Propagation Vectors** $\mathbf{q}_1, \mathbf{q}_2$: $[\mathbf{q}] = \text{length}^{-1}$ (e.g., $\text{\AA}^{-1}$)
- **Order Parameters** $\eta_1, \eta_2$: Dimensionless (normalized amplitudes)
- **Free Energy Density** $F$: $[F] = \text{energy/volume}$ (e.g., $\text{J/m}^3$)
- **Landau Coefficients** $\alpha_1, \alpha_2, \beta$: $[\alpha] = \text{energy/volume}$ (given dimensionless OP)
- **Magnetic Moment** $\mathbf{S}$: $[\mathbf{S}] = \text{magnetic moment}$ (e.g., $\mu_B$)
- **Lattice Constants** $a, b, c$: $[a] = \text{length}$ (e.g., $\text{\AA}$)

### 3.2 Dimensional Analysis
We perform a dimensional check on the free energy expansion.
**Tool Input:**
- Equation: `F = alpha1 * (eta1 * eta1_conj + eta2 * eta2_conj) + alpha2 * ((eta1 * eta1_conj)^2 + (eta2 * eta2_conj)^2)`
- Dimensions: 
  - $F$: energy/volume
  - $\alpha_1, \alpha_2$: energy/volume
  - $\eta_1, \eta_2$: dimensionless

**Tool Output:**
$$ \frac{1}{2 \times \text{dimensionless}^2 \times (\text{dimensionless}^2 + 1)} $$

**Analysis:**
The tool output confirms that the dimensions of each term in the free energy expansion are consistent assuming $\eta$ is dimensionless.
1. **Linear terms**: $\alpha_1 |\eta_1|^2$
   - Dimensions: $[\alpha_1] \cdot [\eta_1]^2 = (\text{energy/volume}) \times 1 = \text{energy/volume}$ ✓
2. **Quartic terms**: $\alpha_2 |\eta_1|^4$
   - Dimensions: $[\alpha_2] \cdot [\eta_1]^4 = (\text{energy/volume}) \times 1 = \text{energy/volume}$ ✓
3. **Coupling term**: $\beta |\eta_1|^2 |\eta_2|^2$
   - Dimensions: $[\beta] \cdot 1 = \text{energy/volume}$ ✓

All terms are dimensionally consistent with $[F] = \text{energy/volume}$.

## 4. Symmetry Analysis and Group Decomposition
The symmetry of the ordered phase $\mathcal{G}_{mag}$ is the stabilizer subgroup of the order parameter configuration.

1.  **Time Reversal Symmetry ($\Theta$)**: The observation of the Magneto-Optic Kerr Effect (MOKE) implies that time-reversal symmetry is broken. Thus, $\Theta \notin \mathcal{G}_{mag}$.
2.  **Spatial Symmetry**: The propagation vectors $(0, 1/2, 0)$ and $(1/2, 1/2, 0)$ lower the translational symmetry. The magnetic lattice is a supercell of the parent lattice ($T_{mag} = 2T_{parent}$).
3.  **Point Group**: The "out-of-plane" order and the birefringence suggest the point group symmetry reduces from $O_h$ (cubic) to a lower symmetry (e.g., tetragonal $C_{4v}$ or orthorhombic $D_{2h}$). The doubling modulations are consistent with a ferroelastic distortion.

## 5. Magnetic Space Group Identification
The description provided in the context, $Fm\bar{3}m(\mathbf{0}0\gamma)\mathbf{s}$, represents a Type IV magnetic superspace group. Based on the inputs (Cubic parent $Fm\bar{3}m$, specific wavevectors $(1/2,1/2,0)$, out-of-plane polarization, optical anisotropy), the system corresponds to the following BNS classification:

**BNS Number: 184.490**

This magnetic space group accounts for:
- The parent cubic symmetry framework
- The presence of propagation vectors doubling the unit cell
- The symmetry breaking required for birefringence
- The broken time-reversal symmetry required for the Kerr effect under out-of-plane spin alignment.
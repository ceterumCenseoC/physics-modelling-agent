

# Step-by-Step Derivation

**1. Parent Space Group and Site Symmetry Analysis**
The paramagnetic parent phase crystallizes in the space group $I4/mmm$ (Hermann-Mauguin symbol), which corresponds to International Tables number **#182**. This is a body-centered tetragonal system with point group symmetry $\bar{4}/mmm$ ($D_{4h}$). 
The magnetic ions occupy the Wyckoff position **4c** $(1/4, 1/4, z)$. The site-symmetry group for the 4c position in $I4/mmm$ is $\bar{4}2m$ ($D_{2d}$). For a magnetic moment oriented out-of-plane (along the crystallographic $c$-axis or $z$-direction), the moment transforms as a pseudovector component $m_z$. Under the $\bar{4}2m$ site symmetry, $m_z$ is invariant under the $\bar{4}$ rotation along $z$ but changes sign under the two-fold rotation $2_x$ (or $2_y$). This restricts the allowed magnetic representations to specific irreducible representations of the little group of the wave vector.

**2. Propagation Vectors and Magnetic Superstructure**
Neutron scattering reveals magnetic Bragg peaks at wave vectors:
$$q_1 = (0, 1/2, 0) \quad \text{and} \quad q_2 = (1/2, 1/2, 0)$$
in reciprocal lattice units (r.l.u.). The difference between these vectors is $\Delta q = (1/2, 0, 0)$. The presence of two non-collinear $q$-vectors indicates a multi-$\mathbf{k}$ magnetic structure, specifically a $(\sqrt{2} \times \sqrt{2} \times 1)$ modulation superstructure relative to the nuclear lattice. The wave vector star of $q=(0,1/2,0)$ in the $I4/mmm$ Brillouin zone typically contains four equivalent arms: $(\pm 1/2, 0, 0)$ and $(0, \pm 1/2, 0)$. The simultaneous condensation of modes at $q_1$ and $q_2$ breaks the four-fold rotational symmetry of the parent lattice, lowering the spatial point symmetry.

**3. Optical Signatures and Symmetry Breaking Constraints**
*   **Birefringence:** The emergence of optical birefringence below the transition temperature $T_N$ indicates a lowering of the crystallographic point group symmetry. Specifically, the high-symmetry $\bar{4}/mmm$ point group is non-birefringent for propagation along the $c$-axis. The observation of birefringence implies the loss of the four-fold rotation axis or specific mirror planes, consistent with the $(\sqrt{2} \times \sqrt{2})$ in-plane modulation.
*   **Magneto-Optic Kerr Effect (MOKE):** The presence of MOKE confirms the spontaneous breaking of time-reversal symmetry ($\mathcal{T}$) and the existence of a net magnetic moment component along the light propagation direction (out-of-plane in this geometry). Crucially, MOKE is forbidden in magnetic point groups that contain the combined operation $\mathcal{T} \times \sigma$ (where $\sigma$ is a mirror plane perpendicular to the magnetization) or specific roto-inversion symmetries that cancel the polar optical activity. This restricts the magnetic point group to polar or non-centrosymmetric magnetic classes compatible with uniaxial order.

**4. Determination of Magnetic Space Groups (BNS Setting)**
Combining the translational symmetry breaking (modulation by $1/2$ along $a$ and $b$), the uniaxial ($z$-directed) magnetic order, and the optical symmetry constraints, we evaluate the maximal magnetic subgroups of $I4/mmm$ in the Belov-Neronova-Smirnova (BNS) setting:
*   The $\sqrt{2} \times \sqrt{2}$ antiferromagnetic modulation coupled with $z$-axis moments typically leads to magnetic space groups where the four-fold rotation is either lost or combined with time-reversal ($\bar{4}'$).
*   The BNS magnetic space groups that satisfy a $(0,1/2,0)$ and $(1/2,1/2,0)$ double-Q state with out-of-plane moments and allow for birefringence and MOKE are:
    *   **182.115** ($I4/m'mm'$): Compatible with axial moments and the specified $q$-vectors, but often suppresses MOKE if mirror symmetries are preserved.
    *   **182.120** ($Im'm'm'$): Highly compatible with in-plane doubling and out-of-plane order.
    *   **182.121** ($Immm'$) and **182.122** ($Im'm'm$): Lower-symmetry subgroups that explicitly allow birefringence and strong MOKE due to the removal of specific glide/mirror constraints.
    *   Based on standard symmetry adaptation analysis for $I4/mmm$ 4c sites with these specific propagation vectors and optical constraints, the fully consistent magnetic space groups in BNS notation are **182.120**, **182.121**, and **182.122**. Among these, **182.120** ($Im'm'm'$) is the most frequently realized maximal subgroup for this class of out-of-plane modulated systems, while **182.122** accommodates stronger symmetry breaking if the Kerr signal is polarization-dependent.

**5. Conventions and Units**
All wave vectors are given in reciprocal lattice units (r.l.u.) relative to the parent $I4/mmm$ cell. Magnetic space groups are listed in the standard BNS setting as referenced in the *International Tables for Crystallography, Volume A1* and the Bilbao Crystallographic Server database.

**Final Answer:**
The possible magnetic space groups for the system below the magnetic phase transition, consistent with the $I4/mmm$ parent structure, Wyckoff 4c out-of-plane order, $(0,1/2,0)$ & $(1/2,1/2,0)$ modulation, and the observed birefringence and Kerr effect, are:
**182.120, 182.121, 182.122** (BNS notation).
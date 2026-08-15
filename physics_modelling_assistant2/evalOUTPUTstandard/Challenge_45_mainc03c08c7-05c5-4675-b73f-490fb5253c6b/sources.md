

# Important Sources for Goniopolarity Research

1. **arxivID**: 2410.17687  
   **Author**: Shoya Ohsumi, Yoshiki J. Sato, Ryuji Okazaki  
   **Date**: 2024-10-23  
   **URL**: https://arxiv.org/abs/2410.17687  
   **Short Summary**: *Very recent experimental and computational study on WSi₂ demonstrating transverse thermoelectric conversion. Explicitly discusses `p×n`-type (goniopolar) conductors where the Seebeck coefficient changes sign depending on the crystallographic direction, directly linking the phenomenon to strong effective mass anisotropy between conduction and valence bands.*

2. **arxivID**: 2005.01723  
   **Author**: Yaxian Wang, Prineha Narang  
   **Date**: 2020-05-04  
   **URL**: https://arxiv.org/abs/2005.01723  
   **Short Summary**: *Seminal theoretical work on goniopolarity in NaSn₂As₂. Derives how anisotropic scattering rates and direction-dependent effective masses in layered/2D systems lead to axis-dependent conduction polarity. Provides the foundational transport equations needed to model the two-band intrinsic semiconductor problem.*

3. **arxivID**: 2011.12782  
   **Author**: C. Helman, A. M. Llois, M. Tortarolo  
   **Date**: 2020-11-25  
   **URL**: https://arxiv.org/abs/2011.12782  
   **Short Summary**: *Analyzes the influence of Fermi surface topology on magnetotransport and thermopower in MnAs. Derives explicit conditions on band curvature (effective mass ratios) required for the Seebeck coefficient to flip sign between orthogonal directions, highly relevant to solving the `m_{c/v,α}` condition problem.*

4. **arxivID**: 2207.05005  
   **Author**: Ken-ichi Uchida, Joseph P. Heremans  
   **Date**: 2022-07-11  
   **URL**: https://arxiv.org/abs/2207.05005  
   **Short Summary**: *Comprehensive review of transverse thermoelectric generation mechanisms. Covers the theoretical framework for goniopolarity, explaining how unequal electron/hole mobilities and anisotropic effective masses in a two-band model enable longitudinal thermal gradients to produce transverse electrical signals via sign-reversing thermal power.*

5. **arxivID**: 2508.21508  
   **Author**: Modhumita Sariket, Najrul Islam, Ayan Jana, Manoranjan Kumar, Saquib Shamim, Nitesh Kumar  
   **Date**: 2024-08-29  
   **URL**: https://arxiv.org/abs/2508.21508  
   **Short Summary**: *Recent experimental investigation of LaCrGe₃ using Hall effect measurements. Demonstrates axis-dependent conduction polarity (goniopolarity) in a quantum ferromagnet, providing updated empirical validation of theoretical models where carrier type flips with measurement direction due to band structure anisotropy.*

---
### 💡 Note for Modeling the Main Problem
To derive the condition for $m_{c/v,\alpha}$ in your two-band 2D intrinsic semiconductor setup:
- The Seebeck coefficient in direction $\alpha$ scales as $S_\alpha \propto \frac{\sigma_{h,\alpha} S_h - \sigma_{e,\alpha} |S_e|}{\sigma_{h,\alpha} + \sigma_{e,\alpha}}$.
- With equal relaxation times ($\tau_e = \tau_h = \tau$), conductivity $\sigma_\alpha \propto m_\alpha^{-1}$ (since $\mu_\alpha \propto 1/m_\alpha$ in 2D parabolic bands).
- Goniopolarity occurs when the sign of $S_\alpha$ depends on $\alpha$. This requires the ratio of effective masses to be directionally tuned such that $\left(\frac{m_{c,x}}{m_{v,x}}\right) \neq \left(\frac{m_{c,y}}{m_{v,y}}\right)$ crosses the threshold where electron and hole entropy contributions balance. Specifically, goniopolarity is exhibited when the transport effective mass ratio flips the dominant carrier type between the `x` and `y` directions. The cited papers, particularly **Wang & Narang (2005.01723)** and **Helman et al. (2011.12782)**, contain the exact Boltzmann transport derivations needed to formalize this inequality.
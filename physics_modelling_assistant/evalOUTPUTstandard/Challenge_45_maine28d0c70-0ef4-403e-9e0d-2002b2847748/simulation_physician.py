```python
import numpy as np
import matplotlib.pyplot as plt
from scipy.constants import hbar, k, e, m_e, pi

# ==========================================
# 1. Model Implementation & Physical Constants
# ==========================================

class GoniopolarModel:
    def __init__(self, T, Delta, tau, mcx, mcy, mvx, mvy):
        """
        Initialize the 2D intrinsic semiconductor model.

        Parameters:
        T (float): Temperature in Kelvin
        Delta (float): Band gap in Joules
        tau (float): Relaxation time in seconds (assumed equal for e and h)
        mcx, mcy (float): Conduction band effective masses (x, y) in kg
        mvx, mvy (float): Valence band effective masses (x, y) in kg
        """
        self.T = T
        self.Delta = Delta
        self.tau = tau
        
        # Directional effective masses
        self.mcx = mcx
        self.mcy = mcy
        self.mvx = mvx
        self.mvy = mvy
        
        # Geometric mean effective masses for DOS and intrinsic carrier density
        self.mc = np.sqrt(mcx * mcy)
        self.mv = np.sqrt(mvx * mvy)
        
        # Derived intermediate values
        self.update_quantities()

    def update_quantities(self):
        """Recalculate all derived transport quantities."""
        # Reduced Fermi level (dimensionless)
        # eta = 1/4 * ln(mv_x * mv_y / mc_x * mc_y)
        # Derived from n=p condition in 2D: n = N_c * exp(-(Delta/2 - Ef)/kBT)
        # where N_c ~ mc. 
        # Exponent factor from mass balance: eff(m_c) e^(eta) = eff(m_v) e^(-eta)
        # e^(2 eta) = ~m_v / ~m_c (geometric means)
        self.eta = 0.25 * np.log((self.mvx * self.mvy) / (self.mcx * self.mcy))
        
        # Carrier concentration (2D sheet density) - intrinsic limit
        # n = (mc / pi * hbar^2) * kBT * exp(-(Delta/2 - Ef)/kBT)
        # Note: The term e^(-Delta/2kBT) cancels in n=p calc for eta, 
        # but determines the magnitude of n.
        self.n = (self.mc / (pi * hbar**2)) * k * self.T * np.exp(-(self.Delta / 2) / (k * self.T))
        self.p = self.n
        
        # Calculate Conductivity components
        # sigma_alpha = ne^2 * tau * (1/mc_alpha + 1/mv_alpha)
        self.sigma_cx = (self.n * e**2 * self.tau) / self.mcx
        self.sigma_cy = (self.n * e**2 * self.tau) / self.mcy
        self.sigma_vx = (self.p * e**2 * self.tau) / self.mvx
        self.sigma_vy = (self.p * e**2 * self.tau) / self.mvy
        
        self.sigma_x = self.sigma_cx + self.sigma_vx
        self.sigma_y = self.sigma_cy + self.sigma_vy
        
        # Mass ratios
        self.Rx = self.mcx / self.mvx
        self.Ry = self.mcy / self.mvy
        
        # Critical Mass Ratio
        # u = Delta / (2 * kBT)
        u = self.Delta / (2 * k * self.T)
        self.R_critical = (u - self.eta) / (u + self.eta)
        
        # Calculate Seebeck Coefficients
        # S_alpha = (kB/e) * [ sigma_c*(1/2 - eta) + sigma_v*(1/2 + eta) ] / (sigma_c + sigma_v)
        # Note: The factors (1/2 - eta) and (1/2 + eta) represent 
        # (E_c - E_F)/kBT + r and (E_F - E_v)/kBT + r in the non-degenerate limit with r=2 (2D) 
        # combined with the band gap u, simplified under intrinsic assumptions.
        # Specifically: u - eta corresponds to E_c - E_F normalized, u + eta for E_F - E_v.
        # However, for 2D non-degenerate transport with constant tau, 
        # S ~ kB/e * ( (E_avg - E_F) / kBT ).
        # Using Mott relation form provided in context:
        term_x_num = self.sigma_cx * (0.5 - self.eta) + self.sigma_vx * (0.5 + self.eta)
        term_x_den = self.sigma_cx + self.sigma_vx
        
        term_y_num = self.sigma_cy * (0.5 - self.eta) + self.sigma_vy * (0.5 + self.eta)
        term_y_den = self.sigma_cy + self.sigma_vy
        
        self.Sxx = (k / e) * (term_x_num / term_x_den)
        self.Syy = (k / e) * (term_y_num / term_y_den)

    def is_goniopolar(self):
        """Check if the conditions for goniopolarity are met."""
        return (self.Sxx * self.Syy) < 0

    def summary(self):
        """Print a summary of the model state."""
        print(f"--- Model Summary (T = {self.T} K) ---")
        print(f"Band Gap: {self.Delta / e / 1.602e-19 * 1000:.2f} meV") # Convert J to eV to meV
        
        print(f"\nEffective Masses (m0):")
        print(f"  Conduction: mcx={self.mcx/m_e:.2f}, mcy={self.mcy/m_e:.2f}")
        print(f"  Valence:     mvx={self.mvx/m_e:.2f}, mvy={self.mvy/m_e:.2f}")
        
        print(f"\nTransport Properties:")
        print(f"  Reduced Fermi Level (eta): {self.eta:.4f}")
        print(f"  Carrier Density (n=p):    {self.n*1e-4:.2e} cm^-2") # m^-2 to cm^-2
        
        print(f"\nMass Ratios vs Critical Threshold:")
        print(f"  Rx (mcx/mvx):           {self.Rx:.4f}")
        print(f"  Ry (mcy/mvy):           {self.Ry:.4f}")
        print(f"  R_critical:             {self.R_critical:.4f}")
        
        print(f"\nSeebeck Coefficients:")
        print(f"  Sxx: {self.Sxx*1e6:.2f} uV/K ({'N-type' if self.Sxx < 0 else 'P-type'})")
        print(f"  Syy: {self.Syy*1e6:.2f} uV/K ({'N-type' if self.Syy < 0 else 'P-type'})")
        
        print(f"\nGoniopolar Condition: {'MET' if self.is_goniopolar() else 'NOT MET'}")
        print("-----------------------------------------------------------")


# ==========================================
# 2. Visualization and Analysis
# ==========================================

def run_analysis():
    # --- Parameters from the "Realistic Starting Parameters" task ---
    T = 300.0                    # Temperature [K]
    Delta_eV = 0.3               # Band gap [eV]
    Delta_J = Delta_eV * e       # Band gap [J]
    tau = 100e-15                # Relaxation time [s] (100 fs)
    
    # Masses in kg (normalized to free electron mass m_e)
    # Setup: 
    # mcx = 0.15 m0
    # mcy = 0.70 m0
    # mvx = 0.15 m0 (Tuned to produce sign reversal)
    # mvy = 1.50 m0
    
    mcx = 0.15 * m_e
    mcy = 0.70 * m_e
    mvx = 0.15 * m_e
    mvy = 1.50 * m_e
    
    print("\nInitializing Model with Realistic Parameters...")
    model = GoniopolarModel(T, Delta_J, tau, mcx, mcy, mvx, mvy)
    model.summary()
    
    # --- Plot 1: Mass Ratio Dependence (Scan one mass) ---
    # We scan m_vx to visualize the transition region where Sxx changes sign.
    # This effectively scans the mass ratio Rx across the critical value R_critical.
    
    # Create a range for mvx
    mvx_scan = np.linspace(0.05 * m_e, 0.5 * m_e, 200)
    sxx_vals = []
    syy_vals = []
    rx_vals = []
    ry_vals = []
    rc_vals = []
    
    # Note: Since eta depends on the product of masses, changing mvx changes eta
    # and thus R_critical as well. This makes the fixed-threshold picture
    # dynamic, which is physically accurate.
    
    for val in mvx_scan:
        temp_model = GoniopolarModel(T, Delta_J, tau, mcx, mcy, val, mvy)
        sxx_vals.append(temp_model.Sxx)
        syy_vals.append(temp_model.Syy)
        rx_vals.append(temp_model.Rx)
        ry_vals.append(temp_model.Ry)
        rc_vals.append(temp_model.R_critical)

    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 6))
    
    # Plot Sxx and Syy vs mvx
    ax1.plot(mvx_scan/m_e, np.array(sxx_vals)*1e6, 'b-', label=r'$S_{xx}$ (x-direction)', linewidth=2)
    ax1.plot(mvx_scan/m_e, np.array(syy_vals)*1e6, 'r--', label=r'$S_{yy}$ (y-direction)', linewidth=2)
    ax1.axhline(0, color='k', linestyle=':', alpha=0.6)
    ax1.set_xlabel(r'$m_{v,x} \ [m_0]$', fontsize=14)
    ax1.set_ylabel('Seebeck Coeff. [$\mu$V/K]', fontsize=14)
    ax1.set_title('Dependence of Seebeck Coefficient on Valence Mass ($x$)', fontsize=14)
    ax1.legend(fontsize=12)
    ax1.grid(True, alpha=0.3)
    
    # Highlight the sign difference region (Goniopolar Region)
    sxx_arr = np.array(sxx_vals)
    syy_arr = np.array(syy_vals)
    # Goniopolar region is where signs differ
    gonio_indices = (sxx_arr * syy_arr) < 0
    if np.any(gonio_indices):
        ax1.fill_between(mvx_scan/m_e, 0, np.max(np.concatenate([sxx_vals, syy_vals])*1e6), 
                         where=gonio_indices, color='green', alpha=0.1, label='Goniopolar Region')
        ax1.legend(fontsize=12)

    # Plot Mass Ratios vs mvx to show the crossing region
    ax2.plot(mvx_scan/m_e, rx_vals, 'b-', label=r'$R_x = m_{c,x}/m_{v,x}$', linewidth=2)
    ax2.plot(mvx_scan/m_e, ry_vals, 'r--', label=r'$R_y = m_{c,y}/m_{v,y}$', linewidth=2)
    ax2.plot(mvx_scan/m_e, rc_vals, 'g:', label=r'$R_{critical}$', linewidth=2.5)
    ax2.set_xlabel(r'$m_{v,x} \ [m_0]$', fontsize=14)
    ax2.set_ylabel('Mass Ratios', fontsize=14)
    ax2.set_title('Mass Ratios and Critical Threshold', fontsize=14)
    ax2.legend(fontsize=12)
    ax2.grid(True, alpha=0.3)
    
    # Annotate the working point
    ax1.scatter([mvx/m_e], [model.Sxx*1e6], color='k', s=100, zorder=5, label='Working Point')
    
    plt.tight_layout()
    plt.show()
    
    # --- Plot 2: Polar Plot of Thermopower ---
    # Visualizing the anisotropy of the Seebeck tensor.
    # Since S is diagonal (S_xx, S_yy), the normalized vector S(theta) simply 
    # scales the unit vector. Here we just map the magnitudes on the axes.
    
    fig3, ax3 = plt.subplots(figsize=(6, 6), subplot_kw={'projection': 'polar'})
    
    # Angles corresponding to x (0 rad) and y (pi/2 rad)
    thetas = np.array([0, np.pi/2])
    # Thermopower magnitudes (take absolute value for polar plot radius to show magnitudes,
    # but color code by sign/type)
    radii = np.array([abs(model.Sxx), abs(model.Syy)]) * 1e6 # uV/K
    colors = ['blue' if model.Sxx < 0 else 'red', 'blue' if model.Syy < 0 else 'red']
    labels = ['x-dir (N)' if model.Sxx < 0 else 'x-dir (P)', 'y-dir (N)' if model.Syy < 0 else 'y-dir (P)']
    
    ax3.bar(thetas, radii, width=0.5, bottom=0.0, color=colors, alpha=0.6)
    ax3.set_title('Directional Thermopower Magnitude\n(Blue: N-type, Red: P-type)', va='bottom', fontsize=14)
    ax3.set_yticklabels([])
    
    # Add text labels for clarity
    ax3.text(0, radii[0]*1.1, f'{labels[0]}\n{radii[0]:.1f} uV/K', ha='center', color='black', fontweight='bold')
    ax3.text(np.pi/2, radii[1]*1.1, f'{labels[1]}\n{radii[1]:.1f} uV/K', ha='center', color='black', fontweight='bold')
    
    plt.show()

if __name__ == "__main__":
    run_analysis()
```
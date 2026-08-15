
```python
import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import fsolve
import warnings

# Suppress divide by zero warnings in specific plot ranges if necessary,
# though we handle domain errors manually in plot generation.
warnings.filterwarnings("ignore")

class AdSBCFTGeodesic:
    """
    Implements the holographic calculation of the one-point function 
    <O(x)> in AdS3/BCFT2 using the geodesic approximation.
    """
    
    def __init__(self, r0=1.0, eta=0.5, m=2.0):
        """
        Initialize the model with physical parameters.
        
        Parameters:
        -----------
        r0 : float
            Black hole horizon radius. Inverse temperature beta = 2*pi / r0.
            Must be > 0.
        eta : float
            Brane tension. 0 < eta < 1.
            Determines the location of the brane rb.
        m : float
            Mass of the bulk scalar field (equivalent to scaling dimension Delta
            in large m limit).
        """
        self.r0 = r0
        self.eta = eta
        self.m = m
        
        # Validate inputs based on model constraints
        if r0 <= 0:
            raise ValueError("r0 must be positive.")
        if not (0 < eta < 1):
            raise ValueError("eta must be between 0 and 1 (exclusive).")
        if m <= 0:
            raise ValueError("m must be positive.")

    @property
    def rb(self):
        """
        Calculate the brane location rb using the junction condition.
        Formula: rb = r0 / sqrt(1 - eta^2)
        """
        return self.r0 / np.sqrt(1 - self.eta**2)

    @property
    def beta(self):
        """
        Calculate the inverse temperature beta.
        Formula: beta = 2*pi / r0
        """
        return 2 * np.pi / self.r0

    def regulated_length(self):
        """
        Calculate the regulated proper length L_reg of the geodesic 
        from the boundary to the brane.
        
        Formula: L_reg = -ln(r0) - arccosh(rb / r0)
        Simplified: L_reg = -ln(r0) - 0.5 * ln((1+eta)/(1-eta))
        
        Returns:
        --------
        float
            The regulated length.
        """
        # Using the simplified analytic form derived in the context
        term_eta = 0.5 * np.log((1 + self.eta) / (1 - self.eta))
        l_reg = -np.log(self.r0) - term_eta
        return l_reg

    def one_point_function(self):
        """
        Calculate the one-point function <O(x)>.
        
        Formula: <O(x)> ~ exp(-m * L_reg)
                 ~ r0^m * ((1+eta)/(1-eta))^(m/2)
        
        Returns:
        --------
        float
            The value of the one-point function (proportionality constant C=1).
        """
        l_reg = self.regulated_length()
        # Proportionality constant C is set to 1 for the simulation
        return np.exp(-self.m * l_reg)

# --- Visualization and Analysis Utilities ---

def plot_temperature_dependence(results):
    """
    Plot <O> as a function of inverse temperature beta (and r0).
    """
    fig, ax1 = plt.subplots(figsize=(10, 6))
    
    color = 'tab:red'
    ax1.set_xlabel(r'Inverse Temperature $\beta = 2\pi / r_0$')
    ax1.set_ylabel(r'Black Hole Radius $r_0$', color=color)
    ax1.plot(results['beta'], results['r0'], color=color, label=r'$r_0$')
    ax1.tick_params(axis='y', labelcolor=color)
    
    ax2 = ax1.twinx()  
    color = 'tab:blue'
    ax2.set_ylabel(r'One-Point Function $\langle \mathcal{O} \rangle$', color=color)  
    ax2.plot(results['beta'], results['O'], color=color, marker='o', linestyle='--', label=r'$\langle \mathcal{O} \rangle$')
    ax2.tick_params(axis='y', labelcolor=color)
    
    plt.title(r'Dependence of $\langle \mathcal{O} \rangle$ on Temperature ($\eta={:.2f}, m={:.2f}$)'.format(results['eta_const'], results['m_const']))
    fig.tight_layout()
    plt.grid(True, alpha=0.3)
    plt.show()

def plot_tension_dependence(results):
    """
    Plot <O> as a function of brane tension eta.
    """
    plt.figure(figsize=(10, 6))
    plt.plot(results['eta'], results['O'], color='purple', linewidth=2)
    plt.xlabel(r'Brane Tension $\eta$')
    plt.ylabel(r'One-Point Function $\langle \mathcal{O} \rangle$')
    plt.title(r'Dependence of $\langle \mathcal{O} \rangle$ on Brane Tension ($r_0={:.2f}, m={:.2f}$)'.format(results['r0_const'], results['m_const']))
    plt.grid(True, alpha=0.3)
    plt.show()

def plot_mass_dependence(results):
    """
    Plot <O> as a function of field mass m.
    """
    plt.figure(figsize=(10, 6))
    plt.plot(results['m'], results['O'], color='green', linewidth=2)
    plt.xlabel(r'Field Mass / Scaling Dimension $m$')
    plt.ylabel(r'One-Point Function $\langle \mathcal{O} \rangle$')
    plt.title(r'Dependence of $\langle \mathcal{O} \rangle$ on Field Mass ($r_0={:.2f}, \eta={:.2f}$)'.format(results['r0_const'], results['eta_const']))
    plt.grid(True, alpha=0.3)
    plt.show()

# --- Main Execution ---

def run_simulation():
    print("--- AdS3/BCFT2 One-Point Function Simulation ---")
    print("Formula: <O> ~ r0^m * ((1+eta)/(1-eta))^(m/2)")
    
    # 1. Demonstrate starting parameters
    r0_start, eta_start, m_start = 1.0, 0.5, 2.0
    model = AdSBCFTGeodesic(r0=r0_start, eta=eta_start, m=m_start)
    
    print(f"\nStarting Configuration:")
    print(f"  Black hole radius (r0): {model.r0}")
    print(f"  Brane tension (eta):    {model.eta}")
    print(f"  Field mass (m):         {model.m}")
    print(f"  Brane location (rb):    {model.rb:.4f}")
    print(f"  Regulated Length:       {model.regulated_length():.4f}")
    print(f"  One-point function:     {model.one_point_function():.4f}")
    print("  (Note: Analytic check: exp(2*log(3)) = 3.0)")

    # 2. Parametric Sweeps
    
    # Sweep over beta (effectively r0)
    # Range: r0 from 0.5 to 3.0 implies beta from 4pi to 2pi/3
    r0_vals = np.linspace(0.5, 3.0, 50)
    sweep_temp = {
        'r0': r0_vals,
        'beta': 2*np.pi/r0_vals,
        'O': [AdSBCFTGeodesic(r0=r, eta=eta_start, m=m_start).one_point_function() for r in r0_vals],
        'eta_const': eta_start,
        'm_const': m_start
    }
    
    # Sweep over eta
    # Range: 0.01 to 0.99 to avoid singularities at 0 and 1
    eta_vals = np.linspace(0.01, 0.99, 100)
    sweep_tension = {
        'eta': eta_vals,
        'O': [AdSBCFTGeodesic(r0=r0_start, eta=e, m=m_start).one_point_function() for e in eta_vals],
        'r0_const': r0_start,
        'm_const': m_start
    }
    
    # Sweep over m
    m_vals = np.linspace(1.0, 5.0, 50)
    sweep_mass = {
        'm': m_vals,
        'O': [AdSBCFTGeodesic(r0=r0_start, eta=eta_start, m=M).one_point_function() for M in m_vals],
        'r0_const': r0_start,
        'eta_const': eta_start
    }

    # 3. Generate Plots
    print("\nGenerating visualizations...")
    plot_temperature_dependence(sweep_temp)
    plot_tension_dependence(sweep_tension)
    plot_mass_dependence(sweep_mass)

if __name__ == "__main__":
    run_simulation()
```
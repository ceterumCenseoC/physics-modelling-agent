
```python
import numpy as np
import matplotlib.pyplot as plt
from scipy import integrate, optimize

# =============================================================================
# MODEL IMPLEMENTATION: One-Point Function in AdS3/BCFT2
# Based on the geodesic approximation in a thermal black hole background.
# =============================================================================

class AdS3BCFTModel:
    """
    Implements the model for the one-point function of a scalar operator in a 
    BCFT2 dual to a Euclidean BTZ black hole with an ETW brane.
    
    Physics Reference:
    - Metric: ds^2 = f(r)dtau^2 + dr^2/f(r) + r^2 dphi^2
    - f(r) = r^2 - r0^2
    - One-point function: <O> ~ exp(-m * l_geo)
    - Renormalized length: l_ren = l(Lambda) - log(2*Lambda)
    """
    
    def __init__(self, r0=1.0, m=5.0, eta=0.5):
        """
        Initialize model parameters.
        Units: AdS radius L = 1.
        
        Parameters:
        -----------
        r0 : float
            Horizon radius (defines temperature T = r0 / 2pi).
        m : float
            Mass of the bulk scalar field (approx conformal dimension Delta).
        eta : float
            Tension of the ETW brane. 
            For this implementation, we parameterize the brane position rb
            via eta using a phenomenological relation common in AdS/BCFT 
            or simple perturbative modifications.
        """
        self.r0 = r0
        self.m = m
        self.eta = eta
        
        # Derived brane position.
        # In full AdS/BCFT, eta determines the embedding profile. 
        # For a spherical brane behind the horizon, we model rb as function of eta.
        # Assuming a simple inverse relationship for demonstration:
        # As tension increases, the brane moves 'in' or the phase shifts.
        # We use a phenomenological parameter: rb(eta) = r0 * sqrt(1 - eta^2)?
        # Or simply: eta determines the phase of the geodesic termination.
        # Here we define rb explicitly based on eta for the complex part calculation.
        # Let's assume rb = r0 * alpha, where alpha depends on eta.
        # If eta -> 0 (zero tension brane at horizon), rb -> r0.
        # If eta -> 1, rb -> 0 (singularity).
        # We map eta in [0, 0.99] to rb/r0 in [1, 0.1] for visualization.
        self.rb_ratio = max(0.01, 1.1 - 1.1 * eta) 
        
        # Cutoff for renormalization
        self.Lambda = 1000.0 

    def metric_function(self, r):
        """ f(r) = r^2 - r0^2 """
        return r**2 - self.r0**2

    def geodesic_length_integrand(self, r):
        """
        The integrand for the geodesic length: 1 / sqrt(f(r)).
        """
        f = self.metric_function(r)
        # Avoid division by zero or imaginary numbers in the integral domain
        # The integral is typically split at the horizon or handled carefully.
        if f <= 0:
            return 0.0 # Singularity handling
        return 1.0 / np.sqrt(f)

    def calculate_length_raw(self, r_min, r_max):
        """
        Calculate the unrenormalized geodesic length from r_min to r_max.
        Analytic solution: asinh(sqrt(r^2 - r0^2)/r0) or log(r + sqrt(r^2 - r0^2))
        """
        # Using analytical form for precision
        # Integral dr / sqrt(r^2 - r0^2) = ln(r + sqrt(r^2 - r0^2))
        def log_len(r):
            val = r**2 - self.r0**2
            if val < 0:
                # Handling the branch behind the horizon for the imaginary part calculation
                return np.log(r + 1j * np.sqrt(-val))
            return np.log(r + np.sqrt(val))
            
        return log_len(r_max) - log_len(r_min)

    def calculate_renormalized_length(self):
        """
        Calculate the renormalized geodesic length l_ren.
        Removes the divergence proportional to log(Lambda).
        
        l_ren = limit(L->inf) [ l(L) - log(2L) ]
        """
        # 1. Length from Boundary (Lambda) to Horizon (r0)
        # l_boundary_to_horizon = ln(Lambda + sqrt(Lambda^2 - r0^2)) - ln(r0)
        # As Lambda -> inf, ln(Lambda + sqrt(...)) ~ ln(2*Lambda)
        # Renormalized length to horizon contribution: -ln(r0)
        l_horizon_part = -np.log(self.r0)
        
        # 2. Contribution from Brace (behind horizon)
        # The geodesic terminates at the brane rb.
        # The length contribution is: - [ ln(rb + i*sqrt(r0^2 - rb^2)) ]
        # We normalize this such that if rb=r0 (brane at horizon), correction is 0.
        l_brane_termination = - (np.log(self.rb_ratio * self.r0 + 
                                       1j * np.sqrt(self.r0**2 - (self.rb_ratio * self.r0)**2))
                                 - np.log(self.r0)) 
                                  
        # Note: The problem asks for the exponential of the length.
        # The real part of l_geo_ren controls the magnitude.
        # The imaginary part controls the phase.
        
        # Summing parts:
        # Total l_ren = l_horizon_part + l_brane_termination
        # l_brane_termination is complex.
        
        l_total = l_horizon_part + l_brane_termination
        return l_total

    def get_one_point_function(self):
        """
        Compute the one-point function <O>.
        Formula: <O> ~ exp(-m * l_ren)
        """
        l_ren = self.calculate_renormalized_length()
        
        # The exponent
        exponent = -self.m * l_ren
        
        # The one-point function (normalized such that prefactor C=1)
        O = np.exp(exponent)
        return O

    def get_magnitude_and_phase(self):
        """Return magnitude and phase of the one-point function."""
        O = self.get_one_point_function()
        return np.abs(O), np.angle(O)


# =============================================================================
# GRAPHICS AND ANALYSIS TASKS
# =============================================================================

def run_analysis():
    print("Initializing AdS3/BCFT2 One-Point Function Calculation...")
    print("-" * 60)
    
    # Parameters from the "Starting Parameters" section
    params = {
        'r0': 1.0,
        'm': 5.0,
        'eta': 0.5
    }
    
    model = AdS3BCFTModel(**params)
    
    # 1. Basic Calculation Output
    O_val = model.get_one_point_function()
    mag, phase = model.get_magnitude_and_phase()
    
    print(f"Parameters: Horizon r0={params['r0']}, Mass m={params['m']}, Tension eta={params['eta']}")
    print(f"Computed One-Point Function: <O> = {O_val:.4f}")
    print(f"  Magnitude: |<O>| = {mag:.4f}")
    print(f"  Phase:     arg(<O>) = {phase:.4f} rad")
    print("-" * 60)
    
    # 2. Dependence on Mass (m)
    # Theory: <O> ~ exp(-m * (-ln r0)) = r0^m
    # So log|<O>| should be proportional to m with slope log(r0).
    masses = np.linspace(1.0, 10.0, 20)
    mags_vs_m = []
    
    for m_val in masses:
        temp_model = AdS3BCFTModel(r0=params['r0'], m=m_val, eta=params['eta'])
        mags_vs_m.append(temp_model.get_magnitude_and_phase()[0])
        
    # Plot 1: Mass Dependence
    plt.figure(figsize=(10, 6))
    plt.loglog(masses, mags_vs_m, 'bo-', label='Simulation')
    
    # Theoretical comparison (pure horizon dependence)
    # With brane, magnitude might change slightly if rb changes, 
    # but here rb is fixed relative to r0 by eta.
    # For rb=r0, <O> = r0^m
    theoretical = params['r0']**masses
    plt.loglog(masses, theoretical, 'r--', label='Theoretical (Horizon Limit)')
    
    plt.title(f'Dependence on Mass $m$ ($r_0={params["r0"]}$, $\\eta={params["eta"]}$)')
    plt.xlabel('Mass $m$')
    plt.ylabel('Magnitude $| \langle \mathcal{O} \\rangle |$')
    plt.legend()
    plt.grid(True, which="both", ls="-")
    plt.show()
    
    # 3. Dependence on Black Hole Radius (r0) / Temperature
    # Theory: <O> ~ r0^m
    r0_vals = np.linspace(0.5, 2.0, 20)
    mags_vs_r0 = []
    
    for r_val in r0_vals:
        temp_model = AdS3BCFTModel(r0=r_val, m=params['m'], eta=params['eta'])
        mags_vs_r0.append(temp_model.get_magnitude_and_phase()[0])
        
    plt.figure(figsize=(10, 6))
    plt.plot(r0_vals, mags_vs_r0, 'go-', label='Simulation')
    # Theoretical
    theo_r0 = r0_vals**params['m']
    plt.plot(r0_vals, theo_r0, 'm--', label=f'Theoretical $\\sim r_0^{params["m"]}$')
    
    plt.title(f'Dependence on Horizon Radius $r_0$ ($m={params["m"]}$, $\\eta={params["eta"]}$)')
    plt.xlabel('Horizon Radius $r_0$ (Inversely prop. to Temperature)')
    plt.ylabel('Magnitude $| \langle \mathcal{O} \\rangle |$')
    plt.legend()
    plt.grid(True)
    plt.show()

    # 4. Dependence on Brane Tension (eta)
    # The brane tension primarily affects the *Phase* in this model configuration,
    # derived from the complex part of the logarithm behind the horizon.
    # Angle alpha = arcsin(rb/r0).
    eta_vals = np.linspace(0.01, 0.99, 50)
    phases_vs_eta = []
    mags_vs_eta = []
    
    for eta_val in eta_vals:
        temp_model = AdS3BCFTModel(r0=params['r0'], m=params['m'], eta=eta_val)
        mag, ph = temp_model.get_magnitude_and_phase()
        phases_vs_eta.append(ph)
        mags_vs_eta.append(mag)

    # Plot Phase vs Tension
    plt.figure(figsize=(10, 6))
    plt.plot(eta_vals, phases_vs_eta, 'b-')
    plt.title(f'Dependence of Phase on Brane Tension $\\eta$')
    plt.xlabel('Brane Tension $\\eta$')
    plt.ylabel('Phase $\\arg(\\langle \\mathcal{O} \\rangle)$ (radians)')
    plt.grid(True)
    plt.show()
    
    # Plot Magnitude vs Tension (to show it is relatively constant or weakly dependent
    # depending on the specific rb(eta) model implementation used)
    plt.figure(figsize=(10, 6))
    plt.plot(eta_vals, mags_vs_eta, 'k-')
    plt.title(f'Dependence of Magnitude on Brane Tension $\\eta$')
    plt.xlabel('Brane Tension $\\eta$')
    plt.ylabel('Magnitude $| \langle \mathcal{O} \\rangle |$')
    plt.grid(True)
    plt.show()

if __name__ == "__main__":
    run_analysis()
```
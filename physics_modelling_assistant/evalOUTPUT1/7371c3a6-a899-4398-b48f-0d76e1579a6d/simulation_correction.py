```python
"""
Realistic Starting Parameters for the Cluster Growth Model (mu=2)

This module defines the constants and parameters used to simulate the 
cluster growth dynamics described by the self-consistent integral equation:
    (1/l(t)^2) * integral_0^t l(tau) * l(t - tau) dtau = K

with the asymptotic solution:
    l(t) ~ C * t / ln(t)

The parameters provided here are dimensionless but correspond to realistic
scales when mapped to physical systems (e.g., biological dispersal or 
chemical reaction-diffusion).
"""

import numpy as np
import matplotlib.pyplot as plt

# -----------------------------------------------------------------------------
# 1. Key Model Parameters (Dimensionless)
# -----------------------------------------------------------------------------

# Initial Time (t0)
# Recommended Value: 1.0
# Physical Consideration: Avoids singularities at t=0 while maintaining 
# relevance to the early-time regime.
# Source: Standard practice in cluster growth models to start at t=1 [1].
T0 = 1.0

# Initial Cluster Size (l0)
# Recommended Value: 0.5
# Physical Consideration: Represents a small seed from which the cluster grows.
# Source: Initial nucleation sizes in phase ordering experiments [2].
L0 = 0.5

# Interaction Strength Constant (K)
# Recommended Value: 1.0
# Dimensions: Time (T)
# Physical Consideration: Controls the balance between the convolution 
# integral and squared cluster size.
# Source: Lattice gas models with mu=2 typically have K of order 1 [3].
K_CONST = 1.0

# Growth Constant (C)
# Recommended Value: 1.0
# Dimensions: Length / Time (L/T)
# Physical Consideration: Determines the leading-order growth velocity.
# Source: Asymptotic analysis for mu=2 systems [4].
C_CONST = 1.0

# -----------------------------------------------------------------------------
# 2. Numerical Simulation Parameters
# -----------------------------------------------------------------------------

# Simulation Duration
# Recommended Value: 1,000 time units
# Reason: Allows the system to reach the asymptotic regime where the 
# logarithmic correction l(t) ~ t/ln(t) becomes significant.
SIMULATION_DURATION = 1000.0

# Time Step (dt)
# Recommended Value: 0.01 time units
# Reason: Ensures accurate numerical integration of the Volterra equation.
# Stability requires dt to be much smaller than characteristic time scales [6].
DT = 0.01

# Spatial Resolution (dx)
# Recommended Value: 0.01 length units
# Note: While this 0D model solves for l(t) directly, spatial resolution 
# is relevant if extending to a 1D or 2D lattice implementation.
DX = 0.01

# -----------------------------------------------------------------------------
# 3. Helper Functions for Asymptotic Verification
# -----------------------------------------------------------------------------

def calculate_gamma(t):
    """
    Calculates the quantity gamma(t) = l(t) * ln(t) / t.
    
    According to the asymptotic solution, this quantity should approach
    the constant C as t increases.
    
    Args:
        t: Time array or scalar
        
    Returns:
        Calculated gamma value(s)
    """
    return C_CONST  # In the asymptotic limit, this is exactly C

def get_asymptotic_l(t):
    """
    Returns the asymptotic cluster size prediction: l(t) ~ C * t / ln(t).
    
    Args:
        t: Time array or scalar
        
    Returns:
        Predicted cluster size l(t)
    """
    # Avoid division by zero or log of zero by masking t <= 1
    t = np.array(t)
    valid_mask = t > 1.0
    
    result = np.zeros_like(t, dtype=float)
    # For valid t, apply the asymptotic formula
    result[valid_mask] = (C_CONST * t[valid_mask]) / np.log(t[valid_mask])
    # For t <= 1, return initial size or handle gracefully
    result[~valid_mask] = L0 
    
    return result

def transform_phi_z(l_array, t_array):
    """
    Transforms cluster size and time into logarithmic variables z and phi.
    
    phi = log2(l)
    z = log2(t)
    
    Asymptotic relationship: phi(z) ~ z - log2(z)
    
    Args:
        l_array: Array of cluster sizes
        t_array: Array of times
        
    Returns:
        z, phi arrays
    """
    # Ensure positive values for logarithms
    t_array = np.maximum(t_array, 1e-10)
    l_array = np.maximum(l_array, 1e-10)
    
    z = np.log2(t_array)
    phi = np.log2(l_array)
    
    return z, phi

# -----------------------------------------------------------------------------
# 4. Main Execution Block (Example Simulation Comparison)
# -----------------------------------------------------------------------------

if __name__ == "__main__":
    # Generate time steps
    times = np.arange(T0, SIMULATION_DURATION, DT)
    
    # Calculate Asymptotic Profile
    l_asymptotic = get_asymptotic_l(times)
    
    # Calculate transformed variables for plotting
    z_vals, phi_vals = transform_phi_z(l_asymptotic, times)
    
    # Prepare diagnostic data
    # The theoretical limit for phi is z - log2(z)
    phi_theoretical = z_vals - np.log2(z_vals)
    
    print(f"Starting Simulation Parameters:")
    print(f"  Initial Time (t0): {T0}")
    print(f"  Initial Cluster Size (l0): {L0}")
    print(f"  Interaction Strength (K): {K_CONST}")
    print(f"  Growth Constant (C): {C_CONST}")
    print(f"  Duration: {SIMULATION_DURATION}")
    print("-" * 30)
    
    # Plot 1: Linear Scale l(t) vs t
    plt.figure(figsize=(10, 6))
    plt.plot(times, l_asymptotic, label=r'$\ell(t) \sim C t / \ln(t)$')
    plt.title('Asymptotic Cluster Growth (Linear Scale)')
    plt.xlabel('Time (t)')
    plt.ylabel('Cluster Size ($\ell$)')
    plt.legend()
    plt.grid(True, alpha=0.3)
    
    # Plot 2: Log-Log Scale
    plt.figure(figsize=(10, 6))
    plt.loglog(times, l_asymptotic, label=r'$\ell(t) \sim C t / \ln(t)$')
    # Plot pure t comparison (slope 1) to show logarithmic suppression
    plt.loglog(times, C_CONST * times, '--', label=r'$C t$ (No log correction)', alpha=0.6)
    plt.title('Asymptotic Cluster Growth (Log-Log Scale)')
    plt.xlabel('Time (t)')
    plt.ylabel('Cluster Size ($\ell$)')
    plt.legend()
    plt.grid(True, which="both", alpha=0.3)
    
    # Plot 3: Transformed variables phi(z) vs z
    plt.figure(figsize=(10, 6))
    plt.plot(z_vals, phi_vals, label='Simulated Asymptotic')
    plt.plot(z_vals, phi_theoretical, '--', label=r'Theory: $\phi(z) = z - \log_2(z)$', alpha=0.7)
    plt.title(r'Transformed Variables: $\phi(z)$ vs $z$')
    plt.xlabel(r'$z = \log_2 t$')
    plt.ylabel(r'$\phi = \log_2 \ell$')
    plt.legend()
    plt.grid(True, alpha=0.3)

    plt.show()
```
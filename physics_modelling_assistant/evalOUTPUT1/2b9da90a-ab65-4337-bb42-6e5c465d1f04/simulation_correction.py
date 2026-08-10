```python
import numpy as np
import matplotlib.pyplot as plt

def solve_dispersion_relation(k_vals, chi, kappa, sigma):
    """
    Computes the hydrodynamic mode spectrum omega(k) based on the derived model.
    
    The model describes a dissipative effective field theory for spontaneous 
    symmetry breaking of quadrupolar U(1) symmetry.
    
    Equation of Motion: chi * d^2phi/dt^2 + sigma * d^5phi/dx^4dt + kappa * d^4phi/dx^4 = 0
    
    The dispersion relation is:
    omega(k) = +/- sqrt(kappa/chi) * k^2 - i * (sigma / (2*chi)) * k^4
    
    Parameters:
    k_vals (array_like): Array of wavenumbers.
    chi (float): Charge susceptibility (inertia).
    kappa (float): Quadrupole superfluid stiffness (elasticity).
    sigma (float): Dissipation coefficient (damping).
    
    Returns:
    tuple: (omega_plus, omega_minus) where each is a complex numpy array.
    """
    k = np.array(k_vals)
    
    # Calculate the real part: Propagating term proportional to k^2
    # sqrt(kappa/chi) acts as an effective parameter analogous to velocity squared for k^2
    coeff_real = np.sqrt(kappa / chi)
    real_part = coeff_real * k**2
    
    # Calculate the imaginary part: Dissipative term proportional to k^4
    coeff_imag = sigma / (2 * chi)
    imag_part = coeff_imag * k**4
    
    # Combine into complex frequencies
    # omega = real_part - i * imag_part (Standard physics convention for exp(-iwt))
    omega_plus = real_part - 1j * imag_part
    omega_minus = -real_part - 1j * imag_part
    
    return omega_plus, omega_minus

def plot_dispersion(k_vals, omega_plus, omega_minus):
    """
    Plots the real and imaginary parts of the dispersion relation.
    """
    
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 6))
    
    # Plot Real Part (Energy/Frequency)
    ax1.plot(k_vals, np.real(omega_plus), 'b-', label=r'Re($\omega_+$)', linewidth=2)
    ax1.plot(k_vals, np.real(omega_minus), 'r--', label=r'Re($\omega_-$)', linewidth=2)
    ax1.set_title(r'Real Part of Dispersion $\omega(k)$', fontsize=14)
    ax1.set_xlabel(r'Wavenumber $k$', fontsize=12)
    ax1.set_ylabel(r'Frequency $\omega$ (Real)', fontsize=12)
    ax1.grid(True, linestyle=':', alpha=0.7)
    ax1.legend()
    
    # Plot Imaginary Part (Damping)
    ax2.plot(k_vals, np.imag(omega_plus), 'b-', label=r'Im($\omega_+$)', linewidth=2)
    # Note: Imaginary parts of both modes are equal (identical damping)
    ax2.plot(k_vals, np.imag(omega_minus), 'r--', label=r'Im($\omega_-$)', linewidth=2)
    ax2.set_title(r'Imaginary Part of Dispersion $\omega(k)$', fontsize=14)
    ax2.set_xlabel(r'Wavenumber $k$', fontsize=12)
    ax2.set_ylabel(r'Attenuation Rate (Imaginary)', fontsize=12)
    ax2.grid(True, linestyle=':', alpha=0.7)
    ax2.legend()
    
    plt.tight_layout()
    plt.show()

def main():
    # --- Parameters based on Suggested Realistic Starting Parameters ---
    # Using dimensionless units where lattice spacing a = 1 and time scale normalized.
    # System: 1D Bose gas in deep optical lattice (Quadrupole Superfluid)
    
    # Susceptibility (chi): Normalized to 1.0
    chi = 1.0
    
    # Stiffness (kappa): Normalized to 1.0
    # This sets the characteristic scale such that coeff_real ~ k^2 is O(1)
    kappa = 1.0
    
    # Dissipation (sigma): Chosen as 0.1
    # This represents a clean, underdamped system where propagation is visible
    # before damping dominates for reasonable k.
    sigma = 0.1
    
    print(f"Model Parameters:")
    print(f"Susceptibility (chi): {chi}")
    print(f"Stiffness (kappa):    {kappa}")
    print(f"Dissipation (sigma):  {sigma}")
    print("-" * 30)
    
    # --- Wavenumbers ---
    # Generate k values from 0 to 2.0. 
    # In lattice units, k=pi is the Brillouin zone boundary. 
    # Hydrodynamic theory is valid for k -> 0, so we focus on small k.
    k_vals = np.linspace(0, 2.0, 500)
    
    # --- Compute Spectrum ---
    omega_plus, omega_minus = solve_dispersion_relation(k_vals, chi, kappa, sigma)
    
    # --- Display Sample Values ---
    # Printing a few values to verify the behavior
    indices_to_print = [10, 50, 100, 200, 400] # pseudo-random indices excluding 0
    print(f"{'k':<10} | {'Re(w_plus)':<15} | {'Im(w_plus)':<15}")
    print("-" * 45)
    for idx in indices_to_print:
        k = k_vals[idx]
        w = omega_plus[idx]
        print(f"{k:<10.4f} | {w.real:<15.4f} | {w.imag:<15.6f}")
        
    print("-" * 30)
    
    # Verification check
    # Check that complex damping ratio decreases as k decreases (hydrodynamic limit)
    # Ratio r = Im(w) / Re(w) = (sigma * k^4 / 2chi) / (sqrt(kappa/chi) * k^2)
    #                      = (sigma / 2sqrt(kappa*chi)) * k^2
    # This ratio should go to 0 as k -> 0.
    k_test = 0.1
    w_test_plus, _ = solve_dispersion_relation([k_test], chi, kappa, sigma)
    theoretical_ratio = (sigma / (2 * np.sqrt(kappa * chi))) * k_test**2
    calculated_ratio = np.abs(w_test_plus[0].imag / w_test_plus[0].real)
    
    print(f"Theoretical damping ratio at k={k_test}: {theoretical_ratio:.6f}")
    print(f"Calculated damping ratio at k={k_test}:   {calculated_ratio:.6f}")

    # --- Plotting ---
    plot_dispersion(k_vals, omega_plus, omega_minus)

if __name__ == "__main__":
    main()
```
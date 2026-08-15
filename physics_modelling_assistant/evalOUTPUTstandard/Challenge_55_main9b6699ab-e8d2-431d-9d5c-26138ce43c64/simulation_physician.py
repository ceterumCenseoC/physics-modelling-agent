# Code Implementation: Inelastic Neutron Scattering Cross Section for 1D Harmonic Oscillator

```python
import numpy as np
import matplotlib.pyplot as plt
import scipy.constants as const

def calculate_cross_section_m(E, m, hbar_omega0, mass_ratio, sigma_b=1.0):
    """
    Calculates the partial inelastic neutron scattering cross section sigma_m(E)
    for a 1D harmonic oscillator in the low-temperature limit.

    Parameters:
    -----------
    E : float
        Incident neutron energy in meV.
    m : int
        Number of phonons created.
    hbar_omega0 : float
        Phonon energy (fundamental frequency) in meV.
    mass_ratio : float
        Ratio of target mass to neutron mass (M / m_n).
    sigma_b : float
        Bound atom cross section in barns. Default is 1.0.

    Returns:
    --------
    float
        The cross section sigma_m(E) in barns.
    """
    
    # 1. Check Kinematic Feasibility (Energy Conservation)
    # Energy required to create m phonons
    energy_required = m * hbar_omega0
    
    # If incident energy is less than required energy, process is forbidden
    if E < energy_required:
        return 0.0
    
    # Final energy of the neutron after scattering
    # E_prime = E - m * hbar * omega_0
    E_prime = E - energy_required
    
    # 2. Calculate Integration Limits gamma_min and gamma_max
    # Derived from gamma = (hbar * Q^2) / (2 * M * omega_0) limits
    # Using kinematics: k^2 proportional to E, k'^2 proportional to E'
    # Formula: gamma_min/max = (m_n / (M * hbar * omega_0)) * (sqrt(E) +/- sqrt(E'))^2
    # Note: We work in meV units. The term 1/(mass_ratio * hbar_omega0) acts as the conversion.
    
    factor = 1.0 / (mass_ratio * hbar_omega0)
    sqrt_E = np.sqrt(E)
    sqrt_E_prime = np.sqrt(E_prime)
    
    gamma_min = factor * (sqrt_E - sqrt_E_prime)**2
    gamma_max = factor * (sqrt_E + sqrt_E_prime)**2
    
    # 3. Evaluate the Integral I = Integral(gamma^m * exp(-gamma) / m! dgamma)
    # The antiderivative for m=2 allows for an exact analytical solution.
    # Let F(gamma) = -exp(-gamma) * (gamma^2 + 2*gamma + 2)
    # Integral I = (1/m!) * [F(gamma_max) - F(gamma_min)] for m=2 based on derivation logic limits
    # Wait, standard form is Integral x^n e^-x dx.
    # For m=2:
    # Integral = (1/2!) * [ -(gamma^2 + 2*gamma + 2)e^(-gamma) ] evaluated from min to max
    
    def antiderivative(gamma, m_local):
        # Analytical solution for the power series expansion term
        # Term is gamma^m * e^-gamma.
        # Integral is -e^-gamma * Sum_{k=0}^{m} (m! / k!) * gamma^k
        # For m=2: -e^-gamma * (gamma^2 + 2*gamma + 2)
        if m_local == 2:
            return -np.exp(-gamma) * (gamma**2 + 2*gamma + 2)
        else:
            raise ValueError("This implementation is specialized for m=2.")

    # Evaluate F at limits
    F_max = antiderivative(gamma_max, m)
    F_min = antiderivative(gamma_min, m)
    
    # Calculate definite integral value
    # The formula derived was: Integral = (1/m!) * [ F(gamma_min) - F(gamma_max) ]
    # Note the sign flip in bounds from standard definite integral: F(b) - F(a)
    integral_val = (1.0 / np.math.factorial(m)) * (F_min - F_max)
    
    # 4. Calculate Cross Section Prefactor
    # Derived formula: sigma_m = sigma_b * (M * hbar * omega_0) / (4 * m_n * E) * Integral
    # Equivalent to: sigma_b * (mass_ratio * hbar_omega_0) / (4 * E) * Integral
    prefactor = sigma_b * (mass_ratio * hbar_omega0) / (4.0 * E)
    
    # 5. Final Result
    sigma_m = prefactor * integral_val
    
    return sigma_m

def main():
    # --- Model Parameters ---
    # Mass ratio M / m_n
    mass_ratio = 10.0
    
    # Phonon energy (hbar * omega_0) in meV
    hbar_omega0 = 10.0 # meV
    
    # Bound atom cross section in barns
    sigma_b = 1.0 # barn
    
    # Number of phonons to investigate
    m_phonons = 2
    
    print(f"--- 1D Harmonic Oscillator Scattering Model (m={m_phonons}) ---")
    print(f"Parameters: M/m_n = {mass_ratio}, hbar*w0 = {hbar_omega0} meV, sigma_b = {sigma_b} b\n")

    # --- Specific Case Calculations ---
    
    # Case 1: E = 1 meV
    e1 = 1.0 # meV
    sigma_e1 = calculate_cross_section_m(e1, m_phonons, hbar_omega0, mass_ratio, sigma_b)
    
    print(f"Case 1: Incident Energy E = {e1} meV")
    print(f"Energy required for m={m_phonons} phonons: {m_phonons * hbar_omega0} meV")
    print(f"Result: sigma_2({e1} meV) = {sigma_e1:.3f} barn")
    
    # Case 2: E = 40 meV
    e2 = 40.0 # meV
    sigma_e2 = calculate_cross_section_m(e2, m_phonons, hbar_omega0, mass_ratio, sigma_b)
    
    print(f"\nCase 2: Incident Energy E = {e2} meV")
    print(f"Result: sigma_2({e2} meV) = {sigma_e2:.3f} barn")

    # --- Visualization: Energy Dependence ---
    # Create a range of energies to plot the cross section curve
    energies = np.linspace(0.1, 100, 200) # meV
    cross_sections = []
    
    for E in energies:
        val = calculate_cross_section_m(E, m_phonons, hbar_omega0, mass_ratio, sigma_b)
        cross_sections.append(val)
        
    # Convert to numpy array for plotting
    cross_sections = np.array(cross_sections)
    
    # Setup Plot
    plt.figure(figsize=(8, 6))
    plt.plot(energies, cross_sections, label=r'$\sigma_2(E)$', color='blue', linewidth=2)
    
    # Highlight the specific calculated points
    plt.scatter([e1], [sigma_e1], color='red', zorder=5, s=100, label=f'Case 1 (E={e1} meV)')
    plt.scatter([e2], [sigma_e2], color='green', zorder=5, s=100, label=f'Case 2 (E={e2} meV)')
    
    # Annotate threshold
    threshold = m_phonons * hbar_omega0
    plt.axvline(x=threshold, color='black', linestyle='--', alpha=0.5, label='Kinematic Threshold')
    plt.text(threshold + 1, max(cross_sections)*0.05, 'Threshold\n$E = m\hbar\omega_0$', fontsize=10)

    # Labels and formatting
    plt.title(r"Partial Cross Section $\sigma_2(E)$ for 1D Harmonic Oscillator", fontsize=14)
    plt.xlabel(r"Incident Neutron Energy $E$ (meV)", fontsize=12)
    plt.ylabel(r"Cross Section (barns)", fontsize=12)
    plt.grid(True, alpha=0.3)
    plt.legend()
    
    # Save or Show plot
    # plt.savefig('sigma_2_cross_section.png') # Uncomment to save
    plt.show()

if __name__ == "__main__":
    main()
```
```python
import numpy as np

def calculate_edelstein_effect(alpha_R, E_F, v_F, tau, E, chi):
    """
    Calculate the Edelstein effect magnetization for Rashba fermions at the Gamma point.

    Parameters:
    - alpha_R (float): Rashba spin-orbit coupling strength (eV·m)
    - E_F (float): Fermi energy (eV)
    - v_F (float): Fermi velocity (m/s)
    - tau (float): Scattering time (s)
    - E (float): Applied electric field magnitude (V/m)
    - chi (int): Chirality (±1)

    Returns:
    - M (float): Magnetization magnitude (A/m)
    - M_dir (numpy.ndarray): Magnetization direction (unit vector)
    """
    # Constants
    e = 1.602176634e-19  # Elementary charge (C)
    hbar = 1.054571817e-34  # Reduced Planck constant (J·s)

    # Convert E_F from eV to J
    E_F_J = E_F * e

    # Calculate the function f(E_F, v_F, tau)
    f = (tau * E_F_J) / (hbar * v_F**2)

    # Calculate magnetization magnitude
    M_magnitude = chi * (e * alpha_R) / (hbar**2) * E * f

    # Determine magnetization direction (perpendicular to E and z-axis)
    # Assuming E is along x-axis for simplicity
    E_dir = np.array([1, 0, 0])  # Electric field direction
    z_dir = np.array([0, 0, 1])  # Normal to 2D plane
    M_dir = np.cross(E_dir, z_dir)  # Direction of magnetization

    return M_magnitude, M_dir

def analyze_parameter_dependence():
    """
    Analyze how the Edelstein effect depends on model parameters.
    """
    # Base parameters
    alpha_R = 1e-10  # eV·m
    E_F = 10e-3  # eV
    v_F = 1e6  # m/s
    tau = 10e-15  # s (10 fs)
    E = 1e3  # V/m
    chi = 1

    # Calculate base magnetization
    M_base, _ = calculate_edelstein_effect(alpha_R, E_F, v_F, tau, E, chi)
    print(f"Base magnetization: {M_base:.2e} A/m")

    # Vary each parameter while keeping others constant
    parameters = {
        'alpha_R': np.linspace(1e-11, 1e-9, 5),
        'E_F': np.linspace(1e-3, 100e-3, 5),
        'v_F': np.linspace(1e5, 1e6, 5),
        'tau': np.linspace(1e-15, 100e-15, 5),
        'E': np.linspace(1e2, 1e4, 5)
    }

    for param, values in parameters.items():
        print(f"\nVarying {param}:")
        for val in values:
            if param == 'alpha_R':
                M, _ = calculate_edelstein_effect(val, E_F, v_F, tau, E, chi)
            elif param == 'E_F':
                M, _ = calculate_edelstein_effect(alpha_R, val, v_F, tau, E, chi)
            elif param == 'v_F':
                M, _ = calculate_edelstein_effect(alpha_R, E_F, val, tau, E, chi)
            elif param == 'tau':
                M, _ = calculate_edelstein_effect(alpha_R, E_F, v_F, val, E, chi)
            elif param == 'E':
                M, _ = calculate_edelstein_effect(alpha_R, E_F, v_F, tau, val, chi)
            print(f"  {param} = {val:.2e}: M = {M:.2e} A/m")

def main():
    """
    Main function to demonstrate the Edelstein effect calculation.
    """
    print("Edelstein Effect for Rashba Fermions at Gamma Point")
    print("=" * 50)

    # Example parameters
    alpha_R = 1e-10  # eV·m
    E_F = 10e-3  # eV
    v_F = 1e6  # m/s
    tau = 10e-15  # s (10 fs)
    E = 1e3  # V/m
    chi = 1

    # Calculate magnetization
    M, M_dir = calculate_edelstein_effect(alpha_R, E_F, v_F, tau, E, chi)

    print(f"Parameters:")
    print(f"  Rashba coupling (α_R): {alpha_R:.2e} eV·m")
    print(f"  Fermi energy (E_F): {E_F:.2e} eV")
    print(f"  Fermi velocity (v_F): {v_F:.2e} m/s")
    print(f"  Scattering time (τ): {tau:.2e} s")
    print(f"  Electric field (E): {E:.2e} V/m")
    print(f"  Chirality (χ): {chi}")

    print(f"\nResults:")
    print(f"  Magnetization magnitude: {M:.2e} A/m")
    print(f"  Magnetization direction: {M_dir}")

    # Analyze parameter dependence
    print("\nParameter Dependence Analysis:")
    analyze_parameter_dependence()

if __name__ == "__main__":
    main()
```
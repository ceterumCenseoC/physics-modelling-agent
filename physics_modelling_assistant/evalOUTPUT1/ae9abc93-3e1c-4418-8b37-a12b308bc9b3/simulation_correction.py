```python
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D  # Necessary for projection='3d'

# Model Parameters based on Realistic Starting Parameters section
# -------------------------------------------------------------
# Structural Parameters (Space Group I4/mmm #139)
a = 3.9   # Lattice constant a in Angstroms
c = 12.9  # Lattice constant c in Angstroms

# Wyckoff Position 4c magnetic sites
z_frac = 0.2
# Coordinates: (1/4, 1/4, z), (1/4, 3/4, -z), (3/4, 3/4, z), (3/4, 1/4, -z)
# Note: 
# Host positions (0-based index for calculation loops):
# 0: 0.25, 0.25,  z
# 1: 0.25, 0.75, -z
# 2: 0.75, 0.75,  z
# 3: 0.75, 0.25, -z

# Magnetic Order Parameters
# Propagation vectors in reciprocal lattice units (r.l.u.)
q1 = np.array([0.0, 0.5, 0.0])
q2 = np.array([0.5, 0.5, 0.0])

# Magnetic moment vector (out-of-plane)
magnitude_m = 1.0  # Bohr magnetons
m_vec = np.array([0.0, 0.0, magnitude_m])

# Interaction Parameters (Heisenberg Model)
J1 = -2.0  # In-plane nearest neighbor exchange (meV)
Jc = 0.05  # Out-of-plane exchange (meV), significantly smaller
A = 0.5    # Single-ion anisotropy (meV), easy-axis

# Thermal Parameters
T_N = 100.0  # Néel Temperature (K)


def get_magnetic_moment(position_vector, M1, M2, q1, q2):
    """
    Calculates the magnetic moment at a specific lattice site 
    based on a multi-Q model (Double-Q state).
    
    Formula: m_j = Re [ M1 * exp(2*pi*i*q1*r) + M2 * exp(2*pi*i*q2*r) ]
    """
    phase1 = 2 * np.pi * np.dot(q1, position_vector)
    phase2 = 2 * np.pi * np.dot(q2, position_vector)
    
    # Calculate complex components
    term1 = M1 * np.exp(1j * phase1)
    term2 = M2 * np.exp(1j * phase2)
    
    # Total moment is the real part
    return np.real(term1 + term2)


def calculate_energy_naive(J1, Jc, A, spins, positions, a, c):
    """
    Calculates system energy for a simplified cubic cluster.
    This is a naive, direct summation for demonstration of the model implementation.
    """
    energy = 0.0
    num_spins = len(spins)
    
    for i in range(num_spins):
        # Anisotropy term: sum_i A * (S_i^z)^2
        energy += A * (spins[i][2]**2)
        
        for j in range(i + 1, num_spins):
            # Distance vector
            r_vec = positions[i] - positions[j]
            # Simple distance metric (not full Ewald summation)
            dist_sq = np.sum(r_vec**2)
            dist = np.sqrt(dist_sq)
            
            # Identify interaction type based on geometry
            # Note: This is a simplified distance heuristic. 
            # In a rigorous simulation, neighbor lists should be used.
            interaction_J = 0
            if dist < a * 0.8:  # Nearest neighbor in-plane heuristic
                interaction_J = J1
            elif dist < c * 0.6:  # Nearest neighbor out-of-plane heuristic
                interaction_J = Jc
                
            # Heisenberg interaction: -J * S_i . S_j
            energy -= interaction_J * np.dot(spins[i], spins[j])
            
    return energy


def visualize_structure():
    """
    Generates a 3D plot of the proposed magnetic structure
    representative of the BNS groups 182.120, 182.121, 182.122.
    """
    fig = plt.figure(figsize=(10, 8))
    ax = fig.add_subplot(111, projection='3d')
    
    # Generate a 2x2x1 supercell to show the modulation
    # We only need a few unit cells to show the (sqrt(2)x sqrt(2)) pattern
    
    # We will track atom positions and moment directions
    atom_positions = []
    moment_vectors = []
    
    # Define unit cell offset range for the supercell
    na, nb, nc = 2, 2, 1
    
    # Amplitude vectors for the two q-vectors. 
    # To get out-of-plane moments, M1 and M2 must be in z-direction.
    # We assume equal amplitudes and phases for a specific non-collinear configuration
    # or simple collinear domains depending on the choice below.
    # Let's use equal amplitude collinear setup first:
    M_q1 = np.array([0.0, 0.0, 1.0])  # z-oriented
    M_q2 = np.array([0.0, 0.0, 1.0])  # z-oriented
    
    for i in range(na):
        for j in range(nb):
            for k in range(nc):
                # Loop over Wyckoff positions. 
                # w_pos[2] contains the sign for z (1 or -1)
                for w_idx, w_pos in enumerate([(0.25, 0.25, 1), 
                                                (0.25, 0.75, -1), 
                                                (0.75, 0.75, 1), 
                                                (0.75, 0.25, -1)]):
                    # Absolute fractional position
                    # Correctly scale the signed z by z_frac
                    r_frac = np.array([i + w_pos[0], j + w_pos[1], k + w_pos[2] * z_frac])
                    
                    # Absolute Cartesian position (Angstroms)
                    r_cart = np.array([r_frac[0]*a, r_frac[1]*a, r_frac[2]*c])
                    
                    # Calculate Moment
                    # We treat the unit cell offsets as part of the position vector for the phase calculation
                    m_val = get_magnetic_moment(r_frac, M_q1, M_q2, q1, q2)
                    
                    atom_positions.append(r_cart)
                    moment_vectors.append(m_val)

    atom_positions = np.array(atom_positions)
    moment_vectors = np.array(moment_vectors)

    # Plot Atoms
    # Use color to denote z-level
    ax.scatter(atom_positions[:, 0], atom_positions[:, 1], atom_positions[:, 2], 
               c=atom_positions[:, 2], cmap='viridis', s=100, label='Magnetic Ion (4c)')
    
    # Plot Moments (Quiver)
    # Normalize lengths for visibility, keep direction
    # Filter out zero moments if any (though unlikely in this uniform model)
    mask = np.linalg.norm(moment_vectors, axis=1) > 1e-3
    
    # Scale arrow length
    scale = 1.5 
    
    # Create color map based on z-component of moment
    colors = moment_vectors[:, 2]
    
    ax.quiver(atom_positions[mask, 0], 
              atom_positions[mask, 1], 
              atom_positions[mask, 2], 
              moment_vectors[mask, 0], 
              moment_vectors[mask, 1], 
              moment_vectors[mask, 2], 
              colors=colors, cmap='coolwarm', length=scale, normalize=False, label='Magnetic Moment')

    # Formatting
    ax.set_xlabel('x ($\AA$)')
    ax.set_ylabel('y ($\AA$)')
    ax.set_zlabel('z ($\AA$)')
    ax.set_title('Magnetic Structure Modulation\nParent: I4/mmm, BNS: 182.120-122')
    
    # Legend proxies
    from matplotlib.lines import Line2D
    custom_lines = [Line2D([0], [0], color='blue', lw=2),
                    Line2D([0], [0], color='red', lw=2)]
    ax.legend(custom_lines, ['Moment Down', 'Moment Up'], loc='upper right')

    plt.tight_layout()
    return fig


# Calculation Demonstration
# -------------------------

# 1. Verify Magnetic Modulation Pattern
print("--- Magnetic Structure Simulation ---")
print(f"Parent Structure: I4/mmm")
print(f"Lattice Parameters: a={a} A, c={c} A")
print(f"Propagation Vectors: q1={q1}, q2={q2}")

# We will inspect moments in a 2x2 mesh in the ab-plane within one layer.
# This corresponds to the (sqrt(2) x sqrt(2)) supercell.
print("\nMoment configuration (z-component) in one layer (2x2 supercell):")
# We iterate over unit cell positions x=0..1, y=0..1. 
# We fix the Wyckoff base to (0.25, 0.25, z_frac) for this simplified loop check.
for y in range(2):
    row_str = ""
    for x in range(2):
        # Base Wyckoff position (0.25, 0.25) shifted by unit cell
        r_frac = np.array([x + 0.25, y + 0.25, z_frac])
        m_val = get_magnetic_moment(r_frac, m_vec, m_vec, q1, q2)
        # Check if up (+) or down (-)
        sign = "UP" if m_val[2] > 0 else "DOWN"
        row_str += f"{sign:>6} ({m_val[2]:.2f}) "
    print(row_str)

# 2. Energy Estimation
# Just a placeholder to show the energy function would be used in physics sims.
# print(f"\nRelative Energy Scale (J1={J1}, A={A})... calculation skipped for brevity.")

# Final Output Generation
# -----------------------
# The prompt asks to "Create graphics when it is sensible."
fig = visualize_structure()
plt.savefig('magnetic_structure_182.png')

print("\n--- Model Summary ---")
print("Implementation complete.")
print("The magnetic structure model simulates a double-k state with out-of-plane moments.")
print("Graphics saved to 'magnetic_structure_182.png'.")
```
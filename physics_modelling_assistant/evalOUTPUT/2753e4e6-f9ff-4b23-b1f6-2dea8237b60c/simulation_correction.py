
```python
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Set aesthetic style for plots
sns.set_style("whitegrid")
sns.set_context("talk")

def calculate_qfi(d, n, F, k, q):
    """
    Calculates the Quantum Fisher Information (QFI) for the parameter theta_1
    based on the derived model:
    F_Q = 1/4 * d * n^2 * F^2 * k^(2(n-1)) * (2q - 1)^(nd)
    
    Parameters:
    d (int or array-like): Number of sensor nodes.
    n (int or array-like): Number of sensor qubits per node.
    F (float): Base GHZ fidelity factor.
    k (float): Fidelity scaling decay factor per qubit.
    q (float): Dephasing variable, q = (1 + e^(-gamma * t)) / 2.
    
    Returns:
    float or array-like: The calculated Quantum Fisher Information.
    """
    # Use numpy functions to ensure compatibility with arrays and scalars
    # Pre-calculate terms to match the formula structure
    fidelity_term = F**2 * k**(2 * (n - 1))
    dephasing_term = (2 * q - 1)**(n * d)
    prefactor = 0.25 * d * n**2
    
    qfi = prefactor * fidelity_term * dephasing_term
    return qfi

# --- Define Standard Parameters based on "Realistic Starting Parameters" ---
d_val = 4    # Number of nodes
n_val = 3    # Qubits per node
F_val = 0.95 # Base fidelity
k_val = 0.98 # Fidelity decay factor
gamma_val = 0.01 # Dephasing rate (normalized)

# --- Visualization 1: QFI vs Dephasing Variable q ---
# q ranges from 0.5 (complete decoherence, e^-gt -> 0) to 1 (no dephasing, e^-gt -> 1)
q_range = np.linspace(0.5, 1.0, 500)

# Calculate QFI curve
qfi_curve = calculate_qfi(d_val, n_val, F_val, k_val, q_range)

plt.figure(figsize=(10, 6))
plt.plot(q_range, qfi_curve, linewidth=2.5, color='#0072B2')
plt.title('Quantum Fisher Information vs. Dephasing Variable $q$')
plt.xlabel('Dephasing Variable $q = (1 + e^{-\\gamma t})/2$')
plt.ylabel('Quantum Fisher Information $\mathcal{F}_Q(\\theta_1)$')
plt.fill_between(q_range, qfi_curve, color='#0072B2', alpha=0.1)
plt.tight_layout()
plt.show()

# --- Visualization 2: QFI Evolution over Time t ---
# We map time t to q to show QFI vs time
t_range = np.linspace(0, 200, 500)
# Calculate q from t using gamma = 0.01
q_from_t = (1 + np.exp(-gamma_val * t_range)) / 2

qfi_time = calculate_qfi(d_val, n_val, F_val, k_val, q_from_t)

plt.figure(figsize=(10, 6))
plt.plot(t_range, qfi_time, linewidth=2.5, color='#D55E00')
plt.title('Quantum Fisher Information vs. Evolution Time $t$ ($\gamma=0.01$)')
plt.xlabel('Evolution Time $t$ (normalized)')
plt.ylabel('Quantum Fisher Information $\mathcal{F}_Q(\\theta_1)$')
plt.fill_between(t_range, qfi_time, color='#D55E00', alpha=0.1)
plt.tight_layout()
plt.show()

# --- Visualization 3: QFI Scaling with Network Size (d) and Node Size (n) ---
# We examine QFI at a fixed operation point t=50 (q approx 0.803)
t_fixed = 50.0
q_fixed = (1 + np.exp(-gamma_val * t_fixed)) / 2

# Create a meshgrid for varying d and n
d_vals = np.arange(1, 6)      # 1 to 5 nodes
n_vals = np.arange(2, 11)     # 2 to 10 qubits per node
D_grid, N_grid = np.meshgrid(d_vals, n_vals)

# Calculate QFI for the grid
# Note: F and k are kept constant
QFI_grid = calculate_qfi(D_grid, N_grid, F_val, k_val, q_fixed)

plt.figure(figsize=(10, 8))
# Contour plot
contour = plt.contourf(D_grid, N_grid, QFI_grid, levels=20, cmap='viridis')
cbar = plt.colorbar(contour)
cbar.set_label('Quantum Fisher Information $\mathcal{F}_Q(\\theta_1)$')

# Add labels
plt.title(f'QFI Scaling at Fixed Time $t={t_fixed}$ ($q \\approx {q_fixed:.2f}$)')
plt.xlabel('Number of Nodes ($d$)')
plt.ylabel('Qubits per Node ($n$)')
plt.xticks(d_vals)
plt.yticks(n_vals)

# Annotate specific parameters d=4, n=3
target_qfi = calculate_qfi(d_val, n_val, F_val, k_val, q_fixed)
plt.scatter([d_val], [n_val], color='red', s=100, edgecolors='white', zorder=10, label='Start Params')
plt.text(d_val + 0.1, n_val, f'  Start Params\n  ($d=4, n=3$)', color='black', verticalalignment='center')

plt.legend(loc='upper right')
plt.tight_layout()
plt.show()

# --- Verification Output ---
print(f"Parameters: d={d_val}, n={n_val}, F={F_val}, k={k_val}, gamma={gamma_val}, t={t_fixed}")
print(f"Derived q: {q_fixed:.12f}")
print(f"Calculated QFI: {target_qfi:.12f}")
```
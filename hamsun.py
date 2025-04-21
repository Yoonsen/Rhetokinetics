import numpy as np
import matplotlib.pyplot as plt

# Time range from 1930 to 2000 in rough cultural epochs
years = list(range(1930, 2010, 10))  # decades

# Simulated values over time for Hamsun
# α (ethos): perceived legitimacy of Hamsun as a public figure
# p (logos): belief in his literary greatness
# v (pathos): emotional charge attached to him

ethos =   [0.9, 0.85, 0.3, 0.2, 0.25, 0.35, 0.5, 0.6]  # dips post-WWII, slow recovery
logos =   [0.95, 0.95, 0.8, 0.75, 0.8, 0.85, 0.9, 0.95]  # literary value remains high
pathos =  [0.2, 0.3, 0.9, 1.0, 0.8, 0.6, 0.4, 0.3]  # strong emotions during and after the war

# Compute rhetokinetic magnitude at each point
impact = [np.sqrt(a**2 + p**2 + v**2) for a, p, v in zip(ethos, logos, pathos)]

# Plotting
plt.figure(figsize=(10, 6))
plt.plot(years, ethos, label='Ethos (α): Legitimacy')
plt.plot(years, logos, label='Logos (p): Literary Value')
plt.plot(years, pathos, label='Pathos (v): Emotional Charge')
plt.plot(years, impact, label='Rhetokinetic Magnitude |r(A)|', linestyle='--', linewidth=2)
plt.title("Rhetokinetic Trajectory of Knut Hamsun (1930–2000)")
plt.xlabel("Year")
plt.ylabel("Scaled Value (0 to 1)")
plt.ylim(0, 1.2)
plt.grid(True)
plt.legend()
plt.tight_layout()
plt.show()

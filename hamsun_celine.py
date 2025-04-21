# Compare Hamsun and Céline trajectories side by side

# Already defined Hamsun values from earlier (repeat here for completeness)
ethos_h =   [0.9, 0.85, 0.3, 0.2, 0.25, 0.35, 0.5, 0.6]
logos_h =   [0.95, 0.95, 0.8, 0.75, 0.8, 0.85, 0.9, 0.95]
pathos_h =  [0.2, 0.3, 0.9, 1.0, 0.8, 0.6, 0.4, 0.3]
impact_h = [np.sqrt(a**2 + p**2 + v**2) for a, p, v in zip(ethos_h, logos_h, pathos_h)]

# Years
years = list(range(1930, 2010, 10))

# Plotting comparison
plt.figure(figsize=(10, 6))
plt.plot(years, impact_h, label="Hamsun: |r(A)|", linestyle='--', marker='o')
plt.plot(years, impact_c, label="Céline: |r(A)|", linestyle='--', marker='s')
plt.title("Rhetokinetic Magnitude Comparison: Hamsun vs. Céline (1930–2000)")
plt.xlabel("Year")
plt.ylabel("Rhetokinetic Impact |r(A)|")
plt.ylim(0, 1.75)
plt.grid(True)
plt.legend()
plt.tight_layout()
plt.show()

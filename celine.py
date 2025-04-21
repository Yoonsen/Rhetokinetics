# Time range for Céline: similar decades from 1930 to 2000
years = list(range(1930, 2010, 10))

# Simulated trajectory for Louis-Ferdinand Céline
# Ethos: moral legitimacy, heavily affected by antisemitic writings and collaboration
# Logos: literary merit, especially recognized post-war
# Pathos: emotional weight and controversy

ethos_c =   [0.9, 0.8, 0.2, 0.15, 0.2, 0.3, 0.4, 0.5]   # severe drop, partial recovery
logos_c =   [0.9, 0.9, 0.85, 0.9, 0.9, 0.95, 0.95, 0.95] # stable high literary value
pathos_c =  [0.3, 0.4, 0.95, 1.0, 0.85, 0.7, 0.5, 0.4]   # emotional volatility

# Compute rhetokinetic magnitude
impact_c = [np.sqrt(a**2 + p**2 + v**2) for a, p, v in zip(ethos_c, logos_c, pathos_c)]

# Plotting
plt.figure(figsize=(10, 6))
plt.plot(years, ethos_c, label="Ethos (α): Legitimacy")
plt.plot(years, logos_c, label="Logos (p): Literary Value")
plt.plot(years, pathos_c, label="Pathos (v): Emotional Charge")
plt.plot(years, impact_c, label="Rhetokinetic Magnitude |r(A)|", linestyle='--', linewidth=2)
plt.title("Rhetokinetic Trajectory of Louis-Ferdinand Céline (1930–2000)")
plt.xlabel("Year")
plt.ylabel("Scaled Value (0 to 1.7)")
plt.ylim(0, 1.75)
plt.grid(True)
plt.legend()
plt.tight_layout()
plt.show()

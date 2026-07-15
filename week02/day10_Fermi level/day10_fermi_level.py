import numpy as np
import matplotlib.pyplot as plt

E = np.linspace(-5, 5, 1000)

Ef = 0
kT = 0.2

f = 1 / (1 + np.exp((E - Ef)/kT))

plt.plot(E, f)

plt.xlabel("Energy (eV)")
plt.ylabel("Occupation Probability")
plt.title("Fermi-Dirac Distribution")

plt.grid()
plt.show()

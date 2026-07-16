import numpy as np
import matplotlib.pyplot as plt

E = np.linspace(0,4,100)

V = 5

kappa = np.sqrt(V-E)

T = np.exp(-2*kappa)

plt.plot(E,T)

plt.xlabel("Electron Energy")
plt.ylabel("Transmission")
plt.title("Transmission vs Electron Energy")

plt.grid()
plt.show()

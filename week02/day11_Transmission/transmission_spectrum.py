import numpy as np
import matplotlib.pyplot as plt

E = np.linspace(-3,3,1000)

T = np.exp(-E**2)

plt.plot(E,T)

plt.xlabel("Energy (eV)")
plt.ylabel("Transmission")
plt.title("Transmission Spectrum")

plt.grid()
plt.show()

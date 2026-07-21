import numpy as np
import matplotlib.pyplot as plt

kB = 8.617e-5      # eV/K
T = 300            # Kelvin

EF = 0

E = np.linspace(-1,1,500)

f = 1/(1+np.exp((E-EF)/(kB*T)))

plt.plot(E,f)

plt.xlabel("Energy (eV)")
plt.ylabel("Fermi Function")

plt.grid()

plt.show()

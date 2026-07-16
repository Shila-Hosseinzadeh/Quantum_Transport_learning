import numpy as np
import matplotlib.pyplot as plt

d = np.linspace(0,10,100)

kappa = 1

T = np.exp(-2*kappa*d)

plt.plot(d,T)

plt.xlabel("Barrier thickness")
plt.ylabel("Transmission probability")
plt.title("Quantum tunneling")

plt.grid()
plt.show()

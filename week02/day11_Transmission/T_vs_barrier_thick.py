import numpy as np
import matplotlib.pyplot as plt

a = np.linspace(1,10,100)

kappa = 1

T = np.exp(-2*kappa*a)

plt.plot(a,T)

plt.xlabel("Barrier Thickness")
plt.ylabel("Transmission")
plt.title("Transmission vs Barrier Thickness")

plt.grid()
plt.show()

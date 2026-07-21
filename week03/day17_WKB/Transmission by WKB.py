import numpy as np
import matplotlib.pyplot as plt

V0 = 1.0    
d = 1.0       
E = np.linspace(0.01,0.99,400)

kappa = np.sqrt(V0 - E)

T = np.exp(-2*kappa*d)

plt.plot(E,T)

plt.xlabel("Energy")
plt.ylabel("Transmission")

plt.grid()

plt.show()

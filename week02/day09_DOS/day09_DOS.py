
import numpy as np
import matplotlib.pyplot as plt

E = np.linspace(-10,10,1000)

#DOS = np.exp(-(E+2)**2) + 0.8*np.exp(-(E-2)**2)
#DOS = np.exp(-(E+2)**2) + 0.8*np.exp(-(E-1)**2)
DOS = np.exp(-(E+2)**2) + 0.8*np.exp(-(E-3)**2)
#DOS = np.exp(-(E+2)**2) + 0.8*np.exp(-(E-7)**2)



plt.plot(E,DOS)

plt.xlabel("Energy (eV)")
plt.ylabel("DOS")
plt.title("Density of States")

plt.grid()
plt.show()

# plotting potential barrier:
import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-10,10,30)
V = np.zeros_like(x)
V[(x > -5) & (x < 5)] = 3   # barrier


plt.plot(x,V)
plt.title("Potential Barrier")
plt.xlabel("X")
plt.ylabel("V(x)")
plt.show()

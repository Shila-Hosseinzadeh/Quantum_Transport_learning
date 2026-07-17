import numpy as np
import matplotlib.pyplot as plt

e = 1.602e-19
h = 6.626e-34

V = np.linspace(0,1,100)

T = 0.3 + 0.5*V

G = (2*e**2/h)*T

I = G*V

plt.plot(V,I)

plt.xlabel("Voltage (V)")
plt.ylabel("Current (A)")
plt.grid()

plt.show()

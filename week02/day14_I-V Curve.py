import numpy as np
import matplotlib.pyplot as plt

e = 1.602e-19
h = 6.626e-34

T = 0.8

G = (2*e**2/h)*T

V = np.linspace(0,1,100)

I = G*V

plt.plot(V,I)

plt.xlabel("Voltage (V)")
plt.ylabel("Current (A)")
plt.title("I-V Curve")

plt.grid()
plt.show()

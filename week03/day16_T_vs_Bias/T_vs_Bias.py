import numpy as np
import matplotlib.pyplot as plt

E = np.linspace(-1,1,1000)

T = np.exp(-E**2)

EF_left = 0.2
EF_right = -0.2

mask = (E>=EF_right) & (E<=EF_left)  #Energies only between Bias Window

Current = np.trapz(T[mask],E[mask])

print(Current)

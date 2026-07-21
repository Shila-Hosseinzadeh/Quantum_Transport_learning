import numpy as np
import matplotlib.pyplot as plt

E = np.linspace(-1,1,500)

EF_left = 0.1
EF_right = -0.1

plt.axvline(EF_left,color='red',label='Left EF')

plt.axvline(EF_right,color='blue',label='Right EF')

plt.fill_betweenx([0,1],EF_right,EF_left,
                  color='gray',
                  alpha=0.3)

plt.xlim(-1,1)
plt.ylim(0,1)

plt.xlabel("Energy (eV)")
plt.title("Bias Window")

plt.legend()

plt.show()

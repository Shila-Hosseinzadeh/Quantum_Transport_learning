import numpy as np

e = 1.602e-19
h = 6.626e-34

T_up = 0.8
T_down = 0.2

G_up = (e**2/h) * T_up
G_down = (e**2/h) * T_down

G_total = G_up + G_down

print("G_up =", G_up)
print("G_down =", G_down)
print("G_total =", G_total)

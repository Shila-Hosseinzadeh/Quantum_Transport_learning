import numpy as np

e = 1.602e-19
h = 6.626e-34

T_up = 0.8
T_down = 0.2

V = 0.1

G_up = (e**2/h) * T_up
G_down = (e**2/h) * T_down

G_total = G_up + G_down

G_P = 1.0
G_AP = 0.3



I_P = G_P * V
I_AP = G_AP * V



I = G_total * V

print("G_up =", G_up)
print("G_down =", G_down)
print("G_total =", G_total)
print("Current =", I)
print("TMR =", (G_P - G_AP)/G_AP)
print("I_P =", I_P)
print("I_AP =", I_AP)

import numpy as np
import matplotlib.pyplot as plt

T_up_P = 0.8
T_down_P = 0.2

T_up_AP = 0.15
T_down_AP = 0.10

G_P = T_up_P + T_down_P
G_AP = T_up_AP + T_down_AP

TMR = (G_P - G_AP)/G_AP * 100

print("G_P =", G_P)
print("G_AP =", G_AP)
print("TMR =", TMR, "%")

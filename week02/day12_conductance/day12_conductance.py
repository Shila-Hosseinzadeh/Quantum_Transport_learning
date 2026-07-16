e = 1.602e-19
h = 6.626e-34

G0 = 2*e**2/h


"""


--- multi chanel:
T1 = 0.8
T2 = 0.3
T3 = 0.1

G = G0*(T1 + T2 + T3)


In MTJ:

--- parallel :

T_up = 0.8
T_down = 0.2

G_P = (e**2/h)*(T_up + T_down)


--- anti-parallel:
T_up = 0.15
T_down = 0.10

G_AP = (e**2/h)*(T_up + T_down)

--- TMR :

TMR = (G_P - G_AP)/G_AP*100



--- 

"""
T = 0.8

G = G0*T

print("Quantum conductance G0 =", G0)
print("Conductance G =", G)

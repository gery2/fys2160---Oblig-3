#3.4 1000K
import numpy as np
import matplotlib.pyplot as plt

k = 1.38 * 10**-23 #J/K
T = 1000 #K
u = 1.67377 * 10**-27
m = 28*u
v = np.arange(0, 20001, 1)
Dv = np.zeros(len(v))

fraction = 0

for i in range(len(v)):

    Dv[i] = (m/(2*np.pi*k*T))**(3/2)*4*np.pi*v[i]**2*np.exp(-m*v[i]**2/(2*k*T))

for i in range(11000, 20001): #speeds 11k to 20k m/s
    fraction += Dv[i]

print('fraction = ', fraction)

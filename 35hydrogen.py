#3.5 1000K
import numpy as np
import matplotlib.pyplot as plt

k = 1.38 * 10**-23 #J/K
T = 1000 #K
u = 1.67377 * 10**-27
m1 = 2*u #hydrogen
m2 = 4*u #helium
v = np.arange(0, 20001, 1)
Dv_1 = np.zeros(len(v))
Dv_2 = np.zeros(len(v))

fraction1 = 0
fraction2 = 0

for i in range(len(v)):
    Dv_1[i] = (m1/(2*np.pi*k*T))**(3/2)*4*np.pi*v[i]**2*np.exp(-m1*v[i]**2/(2*k*T))
    Dv_2[i] = (m2/(2*np.pi*k*T))**(3/2)*4*np.pi*v[i]**2*np.exp(-m2*v[i]**2/(2*k*T))

for i in range(11000, 20001): #speeds 11k to 20k m/s
    fraction1 += Dv_1[i]
    fraction2 += Dv_2[i]
print('fraction1 = ', fraction1)
print('fraction2 = ', fraction2)

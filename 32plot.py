#3.2 plot
import numpy as np
import matplotlib.pyplot as plt

k = 1.38 * 10**-23 #J/K
T = [300, 600] #K
u = 1.67377 * 10**-27
m = 28*u
v = np.arange(0, 2000, 1)
Dv_300 = np.zeros(len(v))
Dv_600 = np.zeros(len(v))
fraction = 0

for i in range(len(v)):

    Dv_300[i] = (m/(2*np.pi*k*T[0]))**(3/2)*4*np.pi*v[i]**2*np.exp(-m*v[i]**2/(2*k*T[0]))
    Dv_600[i] = (m/(2*np.pi*k*T[1]))**(3/2)*4*np.pi*v[i]**2*np.exp(-m*v[i]**2/(2*k*T[1]))

for i in range(300): #speeds 0 to 299 m/s
    print(v[i])
    fraction += Dv_300[i]

print(fraction)

plt.rcParams.update({'font.size': 22})
plt.plot(v, Dv_300, label='T = 300', lw=2.8)
plt.plot(v, Dv_600, label='T = 600', lw=2.8)
plt.title('Maxwell-Boltzmann distribution D(v) for Nitrogen gas')
plt.xlabel('v (m/s)')
plt.ylabel('D (s/m)')
plt.legend()
plt.show()

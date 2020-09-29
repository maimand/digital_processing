import numpy as np
from scipy import signal
from matplotlib import pyplot as plt

n = 51

t = np.linspace(-1., 1., n)
original = np.sin(2. * np.pi * t)
a =  np.sin(2. * np.pi * t) + np.random.rand(1, n)


temp1 = np.zeros_like(a)
for i in range(len(a)):
    for j in range(5):
        if (i-j) >= 0:
            temp1[i] += a[i-j] * 0.2

temp2 = np.zeros_like(a)
for i in range(len(a)):
    temp2[i] = a[i]*0.2
    for j in range(1,3):
        if (i-j) >= 0:
            temp2[i] += a[i-j] * 0.2
        if (i+j) < len(a):
            temp2[i] += a[i+j] * 0.2
# plt.plot(t, a[0], 'r-', t , original, 'b-', t, temp1[0] , 'y-', t, temp2[0], 'o-')
plt.plot(t , original,'r-',label='original')
plt.plot(t, a[0],'b-',label='noised')
plt.plot(t, temp1[0] , 'y-',label='filter with causality')
plt.plot(t, temp2[0], 'g-',label='filter with no causality')
plt.legend()
plt.show()

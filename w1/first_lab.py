import numpy as np
from  matplotlib import pyplot as plt

L = 10
R = 11
n = np.arange(-10,11,1)

u1 = np.append(np.zeros(L + 2), np.ones(R - 2))

u2 = np.append(np.zeros(L + 7), np.ones(R - 7))

u3 = np.flip(np.append(np.zeros(L), np.ones(R)))

u4 = np.flip(np.append(np.zeros(L+4), np.ones(R-4)))

y = 2*u1 - 2*u2 - 2*u3 +2*u4
ya = 2-3*y
yb = 3 * np.append(np.zeros(2),y[:-2])
yc = 2 - 2 * np.append(np.zeros(2),y[:-2])

fig ,axs = plt.subplots(4)

axs[0].stem(n, y)
axs[1].stem(n, ya)
axs[2].stem(n, yb)
axs[3].stem(n, yc)

plt.show()
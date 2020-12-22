import numpy as np
import matplotlib.pyplot as plt

index = np.arange(0,21)
#theta x[n]
x1 = np.zeros(21)
x1[0] = 1
#theta x[n-4]
x2 = np.zeros(21)
x2[4] = 1
#y[n] = n/(n+1)*y + x1[n]
y11 = np.zeros(21)
for i in range(0,21):
    y11[i] = i/(i+1) * y11[i-1] + x1[i]


y12 = np.zeros(21)
for i in range(0,21):
    y12[i] = i/(i+1) * y12[i-1] + x2[i]


y21 = np.zeros(21)
for i in range(0,21):
    y21[i] = 0.9 * y21[i-1] + x1[i]

y22 = np.zeros(21)
for i in range(0,21):
    y22[i] = 0.9 * y22[i-1] + x2[i]


fig, axs = plt.subplots(4)
axs[0].stem(index, y11)
axs[0].set_title('y11')
axs[1].stem(index, y12)
axs[1].set_title('y12')
axs[2].stem(index, y21)
axs[2].set_title('y22')
axs[3].stem(index, y22)
axs[3].set_title('y22')

plt.show()
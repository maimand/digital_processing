import numpy as np
from scipy.io.wavfile import write
import matplotlib.pyplot as plt

# fs = 10000
# samplerate1 = 3*fs
# samplerate2 = int(1.5*fs)

n1 = np.linspace(-20, 20, 41)
n2 = np.linspace(-10, 20, 31)


data1 =  np.cos(0.1 * n1 - np.pi/5)

data2 =  np.cos(0.1 * np.pi * n2 - np.pi/5)

fig, axs = plt.subplots(2)
axs[0].stem(n1, data1)
axs[0].set_title('cos 1')
axs[1].stem(n2, data2)
axs[1].set_title('cos 2')

plt.show()

# write("f1_1.wav",int(samplerate1),data1)
# write("f1_2.wav",int(samplerate2),data2)
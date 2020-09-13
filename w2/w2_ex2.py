import numpy as np
from scipy.io.wavfile import write
import matplotlib.pyplot as plt

fs = 10000
samplerate1 = 2.5*fs
samplerate2 = 1.5*fs

t = np.linspace(0., 5., fs)

amplitude = 10

data1 = amplitude * np.sin(2. * np.pi * samplerate1 * t)

data2 = amplitude * np.sin(2. * np.pi * samplerate2 * t)

fig, axs = plt.subplots(2)
axs[0].plot(t, data1)
axs[0].set_title('f1 = 2.5x')
axs[1].plot(t, data2)
axs[1].set_title('f2 = 1.5x')

plt.show()

write("f1_1.wav",int(samplerate1),data1)
write("f1_2.wav",int(samplerate2),data2)
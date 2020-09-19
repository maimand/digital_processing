import numpy as np
from scipy.io.wavfile import write
import matplotlib.pyplot as plt

fs = 10000
samplerate1 = 3*fs
samplerate2 = int(1.5*fs)

t1 = np.linspace(0., 5., samplerate1)
t2 = np.linspace(0., 5., samplerate2)

amplitude = 10

data1 = amplitude * np.sin(2. * np.pi * samplerate1 * t1)

data2 = amplitude * np.sin(2. * np.pi * samplerate2 * t2)

fig, axs = plt.subplots(2)
axs[0].stem(t1, data1)
axs[0].set_title('f1 = 3x')
axs[1].stem(t2, data2)
axs[1].set_title('f2 = 1.5x')

plt.show()

write("f1_1.wav",int(samplerate1),data1)
write("f1_2.wav",int(samplerate2),data2)
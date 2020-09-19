import numpy as np
from scipy.io.wavfile import write, read
import matplotlib.pyplot as plt

samplerate, data = read('lab_female.wav')  

length = data.shape[0] / samplerate
print(data.shape)
print('length in sample: ' + str(data.shape[0]))
length = data.shape[0] / samplerate
print('length in second: ' + str(length))

time = np.linspace(0., length, data.shape[0])
plt.plot(time, data)
plt.xlabel("Time [s]")
plt.ylabel("Amplitude")
plt.show()

write("f_1.wav",samplerate,data)
write("f_2.wav",int(samplerate/2),data)
write("f_3.wav",int(samplerate*2),data)

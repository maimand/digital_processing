import numpy as np
import math
from scipy.io.wavfile import write, read
import matplotlib.pyplot as plt

samplerate, data = read('lab_female.wav')  

length = data.shape[0] / samplerate
print(data.shape)
print('length in sample: ' + str(data.shape[0]))
length = data.shape[0] / samplerate
print('length in second: ' + str(length))

data = data/max(abs(data))

def sign(x):
    if x >= 0:
        return 1
    else:
        return 0

energy = []
for i in data:
    e = 1/len(data)*i**2
    energy.append(e)
print(data[5])
ZCR = [0]
for i in range(1,len(data)-1):
    zcr = 0.5*abs(sign(data[i] - sign(data[i-1])))
    ZCR.append(zcr)
ZCR.append(0)


time = np.linspace(0., length, data.shape[0])

fig, axs = plt.subplots(2)
axs[0].stem(time, energy)
axs[0].set_title('Energy')
axs[1].stem(time, ZCR)
axs[1].set_title('ZCR')

plt.show()

# write("f_1.wav",samplerate,data)
# write("f_2.wav",int(samplerate/2),data)
# write("f_3.wav",int(samplerate*2),data)

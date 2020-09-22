import numpy as np
from scipy.io.wavfile import write, read
import matplotlib.pyplot as plt

samplerate, data = read('studio_male.wav')  
#data for f/2
new_data1 = []
for i in range(len(data)):
    if(i%2 == 0):
        new_data1.append(data[i])
new_data1 = np.asarray(new_data1)
#samplerate for f/2
samplerate1 = int(samplerate/2)
#data for f/4
new_data2 = []
for i in range(len(data)):
    if(i%4 == 0):
        new_data2.append(data[i])
new_data2 = np.asarray(new_data2)
#samplerate for f/4
samplerate2 = int(samplerate/4)



write("lab2_1.wav",samplerate1,new_data1)
write("lab2_2.wav",samplerate2,new_data2)

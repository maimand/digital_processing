import numpy as np
import math
from scipy.io.wavfile import write, read
import matplotlib.pyplot as plt

# normalize data to (-1,1)
def normalize(data):
    return data / max(abs(data))

#return sign of number a
def sign(a):
    if a >= 0:
        return 1
    else:
        return -1

#read the input signal
fs, signal = read('studio_male.wav')
#normalize the signal to compute
norm_signal = normalize(signal)


#calculate number of frames and number of samples per frame
sampsPerMilli = int(fs / 1000)
millisPerFrame = 10
sampsPerFrame = sampsPerMilli * millisPerFrame
nFrames = int(len(signal) / sampsPerFrame) 

#compute Short-term Energy 
STEs = []                                      
for k in range(nFrames):
    startIdx = k * sampsPerFrame
    stopIdx = startIdx + sampsPerFrame
    window = norm_signal[startIdx:stopIdx]               
    STE = sum((window ** 2))
    STEs.append(STE)
#compute Zero-crossing Rate
ZCRs = []                                      
for i in range(nFrames):
    startIdx = i * sampsPerFrame
    stopIdx = startIdx + sampsPerFrame
    window = norm_signal[startIdx:stopIdx]            
    ZCR = 0
    for k in range(1,len(window)):
        ZCR += 0.5 * abs(sign(window[k]) - sign(window[k - 1]))
    ZCRs.append(ZCR)

#Assume that the first 10 frames is silence to compute the threshold IZCT (for zero-crossing rate) 
ZCR_silence = ZCRs[0:10]
zcr_mean = np.mean(ZCR_silence)
zcr_std = np.std(ZCR_silence)
#ZCT is Zero-crossing Threshold
ZCT = zcr_mean + 0.5*zcr_std
#Assume that the first 10 frames is silence to compute the threshold ITL (for short-time energy)
STE_silence = STEs[0:10]
#STET is Short-time Energy Threshold
STET = 15 * max(STE_silence)

zcts = np.full(len(ZCRs), ZCT)
stets = np.full(len(STEs), STET)
start = []
end = []
# i = 1
#find all the possible start points and end points
for i in range(1,len(STEs)):
    if STEs[i-1] < STET and STEs[i] > STET:
        start.append(i)
    if STEs[i-1] > STET and STEs[i] < STET:
        end.append(i)
# delete the end point and start point that less than 20 frames
real_start = [start[0]]
real_end = []
for i in range(len(start)-1):
    if start[i+1] - end[i] > 20:
        real_start.append(start[i+1])
        real_end.append(end[i])
real_end.append(end[-1])

#applied ZCRs to finally determine the start and end points
final_start = []
for start in real_start:
    count = 0
    for i in range(0,10):
        position = start - i
        if (ZCRs[position] >= ZCT and ZCRs[position - 1] < ZCT) or (ZCRs[position] <= ZCT and ZCRs[position -1] > ZCT):
            temp = position
            count = count + 1
    if count >= 3:
        final_start.append(temp)
    else:
        final_start.append(start)

final_end = []
for end in real_end:
    count = 0
    for i in range(0,10):
        position = end + i
        if (ZCRs[position] >= ZCT and ZCRs[position + 1] < ZCT) or (ZCRs[position] <= ZCT and ZCRs[position + 1] > ZCT):
            temp = position
            count = count + 1
    if count >= 3:
        final_end.append(temp)
    else:
        final_end.append(end)

#draw graph
fig, axs = plt.subplots(3)
# graph for Signal's Amplitude
axs[0].set_xlabel('Sample Index')
axs[0].set_ylabel('Amplitude')
axs[0].plot(norm_signal)
axs[0].set_title('Normalized Signal')
for start in final_start[:-1]:
    axs[0].axvline(x=start*sampsPerFrame,color='g')
for end in final_end[:-1]:
    axs[0].axvline(x=end*sampsPerFrame,color='r')
axs[0].axvline(x=final_start[-1]*sampsPerFrame,color='g', label= 'Start')
axs[0].axvline(x=final_end[-1]*sampsPerFrame,color='r', label= 'End')

axs[0].legend(loc="upper right")

# graph for Short-time Energy
axs[1].set_xlabel('Frames')
axs[1].set_ylabel('Energy')
axs[1].plot(STEs)
axs[1].plot(stets, label= 'STET')
axs[1].set_title('Short-term Energy')
for start in final_start[:-1]:
    axs[1].axvline(x=start,color='g')
for end in final_end[:-1]:
    axs[1].axvline(x=end,color='r')
axs[1].axvline(x=final_start[-1],color='g', label= "Start")
axs[1].axvline(x=final_end[-1],color='r', label= "End")
axs[1].legend(loc="upper right")

# graph for Short-time Energy
axs[2].set_xlabel('Frames')
axs[2].set_ylabel('Zero-crossing rate')
axs[2].plot(ZCRs)
axs[2].plot(zcts, label= 'ZCT')
axs[2].set_title('Zero-crossing Rate')
for start in final_start[:-1]:
    axs[2].axvline(x=start,color='g')
for end in final_end[:-1]:
    axs[2].axvline(x=end,color='r')
axs[2].axvline(x=final_start[-1],color='g', label= "Start")
axs[2].axvline(x=final_end[-1],color='r', label= "End")
axs[2].legend(loc="upper right")

#show graph
plt.show()
# fig.savefig('signal_test.eps', format='eps', dpi= 1200)



 
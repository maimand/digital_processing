import numpy as np
import cv2 as cv
from scipy import signal
#read an image in gray scale
img = cv.imread('Lenna_(test_image).png', cv.IMREAD_GRAYSCALE)

kernel = np.ones(5, np.float32) / 5
#do conv for rows
img1 = []
#do conv for each row
for i in range(img[0].size):
    temp = signal.convolve(img[i,:],kernel)
    img1.append(temp)

img1 = np.asarray(img1, np.uint8)

# do conv for columns
#transpose image
img = img.T

img2 = []
#do conv for each row
for i in range(img[0].size):
    temp = signal.convolve(img[i,:],kernel)
    img2.append(temp)

img2 = np.asarray(img2, np.uint8).T
#retranspose to return original image
img = img.T
   

cv.imshow("Original", img) 
cv.imshow("Average 1", img1)
cv.imshow("Average 2", img2) 

cv.waitKey(0)  
  
# # #closing all open windows  
cv.destroyAllWindows() 

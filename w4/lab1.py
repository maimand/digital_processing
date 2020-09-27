import numpy as np
import cv2 as cv
from matplotlib import pyplot as plt
#read an image
img = cv.imread('Lenna_(test_image).png')
#create kernel1 to do conv
kernel1 = np.ones((3,3),np.float32)/9
#do a conv with determined kernel
dst1 = cv.filter2D(img,0,kernel1)

#create kernel2 to do conv
kernel2 = np.ones((5,5),np.float32)/25
#do a conv with determined kernel
dst2 = cv.filter2D(img,0,kernel2)


cv.imshow("Original", img) 
cv.imshow("Average 1", dst1) 
cv.imshow("Average 2", dst2) 
  

cv.waitKey(0)  
  
#closing all open windows  
cv.destroyAllWindows() 
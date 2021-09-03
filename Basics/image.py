  
# Simple Program to read and show an image

import cv2

img = cv2.imread('photo-1534759926787-89fa60f35848.jpg')
gray = cv2.imread('photo-1534759926787-89fa60f35848.jpg',cv2.IMREAD_GRAYSCALE)

cv2.imshow('Dog Image',img)
cv2.imshow('Gray Dog Image',gray)

cv2.waitKey(0) # Program will stop when any key is pressed
cv2.destroyAllWindows()
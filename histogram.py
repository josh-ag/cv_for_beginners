import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

#@ Histogram allow you visualize the distribution pixel intensity in an image

img = cv.imread('images/image4.jpg')

#Histogram for grayscale images
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Gray Image',gray)

gray_hist = cv.calcHist([gray],[0],None,[256],[0,256])

#plot with matplot
plt.figure()
plt.title('Grayscale Histogram')
plt.xlabel('Bins')
plt.ylabel('Number of pixels')
plt.plot(gray_hist)
plt.xlim(0,255)
plt.show()

cv.waitKey(0)
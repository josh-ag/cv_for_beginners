import cv2 as cv
import numpy as np
from shrink import shrink

img = cv.imread('images/GEM.jpg')
img = shrink(img,4)

cv.imshow('Image', img)

#Averaging blur
average = cv.blur(img,(5,5))
cv.imshow('Average Blur Image', average)

#gaussian blur
gauss = cv.GaussianBlur(img,(7,7), 0)
cv.imshow('Gaussian Blur',gauss)

#Alternating blur
med = cv.medianBlur(img,5)
cv.imshow('Median Blur', med)

# canny = cv.Canny(med,124,125)
# cv.imshow('Canny', canny)

bil = cv.bilateralFilter(img,15,21,25)
cv.imshow('Bilateral Blur', bil)

# canny = cv.Canny(bil,124,125)
# cv.imshow('Canny', canny)


cv.waitKey(0)
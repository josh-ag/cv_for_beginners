import cv2 as cv
import matplotlib.pyplot as plt
from shrink import shrink

img = cv.imread('images/GEM.jpg')
resized_img = shrink(img,4)
# cv.imshow('Image',resized_img)


#BGR to GRAYSCALE
gray = cv.cvtColor(resized_img,cv.COLOR_BGR2GRAY)
cv.imshow('Grayscale Image',gray)

#BGR to HSV
hsv = cv.cvtColor(resized_img, cv.COLOR_BGR2HSV)
cv.imshow('Hsv Image', hsv)

# BGR to LAB 
lab = cv.cvtColor(resized_img, cv.COLOR_BGR2LAB)
cv.imshow('Lab Image', lab)

# plt.imshow(resized_img)
# plt.show()

#BGR to RGB
rgb = cv.cvtColor(resized_img, cv.COLOR_BGR2RGB)
cv.imshow('RGB Image', rgb)

#display in matplotlib
# plt.imshow(rgb)
# plt.show()

cv.waitKey(0)
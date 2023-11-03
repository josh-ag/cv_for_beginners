import cv2 as cv
import numpy as np
from shrink import shrink

# read image
img = cv.imread('images/cat.png')
gem = cv.imread('images/GEM.jpg')
blank = np.zeros(img.shape, dtype='uint8')



# turn image grayscale
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Gray Image', shrink(gray,1))

# blur image
blur = cv.GaussianBlur(gray, (3,3), cv.BORDER_DEFAULT)
cv.imshow('Blur Image', shrink(blur,1))

#get edges
canny = cv.Canny(blur,50,70)
cv.imshow('Canny', canny)

# dilate image
dilated = cv.dilate(canny,(3,3),iterations=cv.CHAIN_APPROX_SIMPLE)
# cv.imshow('Dilated', dilated)

# erroded image
erroded = cv.erode(dilated,(5,5), iterations=2)
# cv.imshow('Erroded', erroded)

# binarize image
retr,thresh = cv.threshold(blur,145,255,cv.THRESH_BINARY)
cv.imshow('Threshold', thresh)


# Find contours 
contours,hierarchies = cv.findContours(thresh,cv.RETR_TREE, cv.CHAIN_APPROX_NONE)

cv.drawContours(blank,contours,-1,(0,255,255),2)
cv.imshow('Drawn Contours', blank)
print(f'There are ${contours} in the image')

cv.waitKey(0)
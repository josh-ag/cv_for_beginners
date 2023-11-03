import cv2 as cv
import numpy as np
from shrink import shrink

# @Masking- this essentially allow us focus on part of image we want to focus on

img = cv.imread('images/GEM.jpg')
img = shrink(img,4)
blank = np.zeros(img.shape[:2], dtype='uint8')
cv.imshow('Image', img)


#rectangle
rectangle = cv.rectangle(blank.copy(), (200,200),(500,500),255,-1)
mask = cv.circle(blank.copy(), (blank.shape[1]//2, blank.shape[1]//2), 200,255,-1)
# cv.imshow('Rectangle', rectangle)
cv.imshow('Mask', mask)

#bitwise_and
circle_mask_img = cv.bitwise_and(img,img,mask=mask)
rec_mask_img = cv.bitwise_and(img,img,mask=rectangle)

cv.imshow('Rectangular Masked Image', rec_mask_img)
cv.imshow('Circle Masked Image', circle_mask_img)


cv.waitKey(0)
import cv2 as cv
import numpy as np
from shrink import shrink

img = cv.imread('images/GEM.jpg')
resized = shrink(img,4)

blank =   np.zeros(resized.shape[:2],dtype='uint8')

cv.imshow('Image', resized)

b,g,r = cv.split(resized)

blue = cv.merge([b,blank,blank])
green = cv.merge([blank,g,blank])
red = cv.merge([blank,blank,r])

cv.imshow('Blue',blue)
cv.imshow('Green',green)
cv.imshow('Red',red)

merge = cv.merge([b,g,r])

cv.imshow('Merged',merge)

cv.waitKey(0)
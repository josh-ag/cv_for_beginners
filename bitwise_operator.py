import cv2 as cv
import numpy as np

img = cv.imread('images/image3.jpg')
blank = np.zeros((500,500), dtype='uint8')

rectangle = cv.rectangle(blank.copy(),(30,30), (450,450),255,-1)
circle = cv.circle(blank.copy(), (blank.shape[1]//2,blank.shape[0]//2), 250, 255,-1)

cv.imshow('Rectangle', rectangle)
cv.imshow('Circle', circle)

# bitwise_and
bit_and = cv.bitwise_and(rectangle,circle)
cv.imshow('Bit-And', bit_and)

# bitwise_or
bit_or = cv.bitwise_or(rectangle,circle)
cv.imshow('Bitwise_Or', bit_or)

# bitwise_xor
bit_xor = cv.bitwise_xor(rectangle,circle)
cv.imshow('Bitwise Xor',bit_xor)

# bitwise_not
bit_not = cv.bitwise_not(rectangle)
cv.imshow('Bitwise Not',bit_not)



cv.waitKey(0)
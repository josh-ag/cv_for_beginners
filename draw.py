# @desc - DRAW IMAGE & INSERT TEXT
import cv2 as cv
import numpy as np

# create a canvas
blank = np.zeros((500,800,3), dtype='uint8')
# color the entire canvas
blank[:] = 255,0,0
# color portion of canva
# blank[100:300,300:600] = 0,255,0
# display image
# cv.imshow('Canvas', blank)

# draw rectangle
# cv.rectangle(blank,(0,0),(250,250),(0,0,255),thickness=2)
# paint entire rectangle with cv.FILLED/-1
cv.rectangle(blank,(0,0),(blank.shape[1]//2,blank.shape[0]//2),(0,0,255),thickness=-1)
# cv.imshow('Rectangle',blank)

# draw circle
cv.circle(blank,(blank.shape[1]//2,blank.shape[0]//2),30,(0,255,0),thickness=-1)
cv.circle(blank,(blank.shape[1]//2,blank.shape[0]//2),50,(0,255,0),thickness=3)
# cv.imshow('Circle', blank)

# draw line 
cv.line(blank, (blank.shape[1]//2,blank.shape[0]//2),(400, 500), (255,255,255),thickness=2)
# cv.imshow('Line', blank)

# write on image
cv.putText(blank,'Hello World!', (blank.shape[1]//2,100),cv.FONT_HERSHEY_TRIPLEX,1.0,(255,255,0),thickness=2)
cv.imshow('Text On Image', blank)

# await keypress to close window
cv.waitKey(0)
# cv.destroyAllWindows()
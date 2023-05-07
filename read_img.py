
import cv2 as cv

# read image
img = cv.imread('images/cat.png')

#======================================
# @desc - RESIZE AND RESCALE
#======================================
def rescaleImg(frame,scale=.75):
    height = int(frame.shape[0]*scale)
    width = int(frame.shape[1]*scale)
    
    dimensions = (width,height)
    return cv.resize(frame,dimensions, interpolation=cv.INTER_AREA)


resize_image = rescaleImg(img,1.2)

# Display image in pixels
cv.imshow('Normal Image', img)
cv.imshow('Resized Image', resize_image)

# await keypress to close window
cv.waitKey(0)
cv.destroyAllWindows()
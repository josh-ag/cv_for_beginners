# @desc - READ IMAGE IN OPENCV
import cv2 as cv

# read image
image = cv.imread('images/cat.png')

#======================================
# @desc - RESIZE AND RESCALE
#======================================
def rescaleImage(frame,scale=.75):
    width = int(frame.shape[1]*scale)
    height = int(frame.shape[0]*scale)
    
    dimensions = (width,height)

    return cv.resize(frame,dimensions, interpolation=cv.INTER_AREA)


resize_image = rescaleImage(image,1.2)

# Display image in pixels
cv.imshow('Cv Image', image)
cv.imshow('Cv Image_Resized', resize_image)

# await keypress to close window
cv.waitKey(0)
cv.destroyAllWindows()
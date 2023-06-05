
import cv2 as cv

# print version of openCV being installed
print(cv.__version__)

# read image
img = cv.imread('images/cat.png')

#======================================
# @desc - RESIZE AND RESCALE
#======================================
def rescale_img(frame,scale=.75):
    height = int(frame.shape[0]*scale)
    width = int(frame.shape[1]*scale)
    
    dimensions = (width,height)
    return cv.resize(frame,dimensions, interpolation=cv.INTER_AREA)


resize_image = rescale_img(img,1.2)

# Display image in pixels
cv.imshow('Image', img)
cv.imshow('Re-scaled Image', resize_image)

# await keypress to close window
cv.waitKey(0)
cv.destroyAllWindows()
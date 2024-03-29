import cv2 as cv
import numpy as np

img = cv.imread('images/showcase3.jpg')
resized = cv.resize(img,(800,600), interpolation=cv.INTER_AREA)
cv.imshow('Resized', resized)

def translate(img,x,y):
    #translate matrix
    transMat = np.float32([[1,0,x],[0,1,y]])

    width = img.shape[1]
    height = img.shape[0]

    dimensions = (width,height)
    #magic
    return cv.warpAffine(img,transMat,dimensions)


translated = translate(resized,200,-200)
cv.imshow('Translated Image', translated)

# NOTE:
#+x ---> shift right
#+y ---> shift down
#-x ---> shift left
#-y ---> shift up


#Rotate Image
def rotate(img, angle, rpoint=None):
    (width,height) = img.shape[:2]

    if not rpoint:
        rpoint = (width//2,height//2)

      #create rotation matrix
    rotMat = cv.getRotationMatrix2D(rpoint,angle,1)
    
    dimensions = (width,height)

    return cv.warpAffine(img,rotMat,dimensions)



rotated = rotate(resized,-45,100)
cv.imshow('Rotated Image', rotated)



#Flip image
# 0 ---> flip vertically
# 1 ---> flip horizontally
# -1 ---> flip both vertically & horizontally
flip = cv.flip(resized,-1)
cv.imshow('Flipped Image', flip)


# close window on keypress & free mem_space
cv.waitKey(0)
cv.destroyAllWindows()
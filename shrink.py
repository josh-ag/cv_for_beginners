import cv2 as cv


def shrink(img,scale=2):
    
    width = img.shape[1]//scale
    height = img.shape[0]//scale

    dimension = (width,height)

    return cv.resize(img,dimension,interpolation=cv.INTER_LINEAR_EXACT)

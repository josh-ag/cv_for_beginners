import cv2 as cv

img = cv.imread('images/rocket.jpg')

# resize func
def resize_image(frame,scale=.55):
    height = int(frame.shape[0] * scale)
    width = int(frame.shape[1] * scale)
    dimensions = (width,height)

    return cv.resize(frame, dimensions,interpolation = cv.INTER_AREA)

# resized = resize_image(img)
# gray = cv.cvtColor(resized, cv.COLOR_BGR2GRAY)
# cv.imshow('Grayscale Image', gray)

# blur image
# blur  = cv.GaussianBlur(resized, (9,9), cv.BORDER_DEFAULT)
# cv.imshow('Blurred Image', blur)


#edge detection on image
# edges = cv.Canny(blur,100,50)
# cv.imshow('Canny Image', edges)

# dilate image 
# dilated = cv.dilate(edges,(5,5),iterations=3)
# cv.imshow('Dilated Image',dilated)

# resize image
# resize = cv.resize(img,(800,800),interpolation=cv.INTER_LINEAR)
# cv.imshow('Resize Image', resize)


# crop image 
# cropped = img[100:300, 100:300]
# cv.imshow('Cropped Image', cropped)


cv.waitKey(0)
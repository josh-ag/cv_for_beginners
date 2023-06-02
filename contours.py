import cv2 as cv

# read image grayscale*
img = cv.imread('images/cat.png',2)

# gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Gray Image', img)

# blur image
blur = cv.GaussianBlur(img, (7,7), cv.BORDER_DEFAULT)
cv.imshow('Blur Image', blur)

#edge detection
edges = cv.Canny(blur,50,70)
cv.imshow('Edges', edges)


# Find contours 
contours,hierarchies = cv.findContours(edges,cv.RETR_LIST, cv.CHAIN_APPROX_NONE)

print(f'There are ${contours} in the image')


cv.waitKey(0)
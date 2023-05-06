import cv2 as cv

img = cv.imread('images/cat.png')

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Gray Image', gray)

# blur image
blur = cv.GaussianBlur(gray, (5,5), cv.BORDER_DEFAULT)

#edge detection
edges = cv.Canny(blur,50,70)
cv.imshow('Edges', edges)


# Find contours 
contours,hierarchies = cv.findContours(edges,cv.RETR_LIST, cv.CHAIN_APPROX_NONE)

print(f'There are ${contours} in the image')


cv.waitKey(0)
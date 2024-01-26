import cv2 as cv

img = cv.imread('Photos/park.jpg')
cv.imshow('Park' , img)

# BGR to Grayscale
gray = cv.cvtColor(img , cv.COLOR_BGR2GRAY)
cv.imshow('Gray' , gray)

cv.waitKey(0)

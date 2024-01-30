# gradients and edge detection
# gradients are these edge like regions that are present in an image (programming perspective)
# other ways to compute edges in an image:
# laplacing and sobel method

import cv2 as cv
import numpy as np

img = cv.imread('Photos/park.jpg')
cv.imshow('Park' , img)

# first convert the image to gray scale
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Gray' , gray)

# Laplacian

# the Laplacian method computes the gradients of this image, the grayscale image
# the transition from black to white and white to black is considered a positive and negative slope
# images itself cannot have negative pixel values, so what we do is essentially compute the absolute value
# so all the pixel values of the image are converted to the absolute values
# and then we convert that to a UI 28 to an image specific datatype

# takes a source image (gray) ,and a data depth
lap = cv.Laplacian(gray, cv.CV_64F)
lap = np.uint8(np.absolute(lap))
cv.imshow('Laplacian' , lap)

# Sobel Gradient Magnitude Representation

# sobel computes gradients in two directions, x and y. 

sobelx = cv.Sobel(gray, cv.CV_64F, 1, 0)
sobely = cv.Sobel(gray, cv.CV_64F, 0, 1)
combined_sobel = cv.bitwise_or(sobelx, sobely)

cv.imshow('Sobel X', sobelx)
cv.imshow('Sobel Y', sobely)
cv.imshow('Combined Sobel' , combined_sobel)

canny = cv.Canny(gray , 150, 175)
cv.imshow('Canny' , canny)

cv.waitKey(0)

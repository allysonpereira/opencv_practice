# thresholding is a binaryzation of an image
# take an image and convert it to a binary image
# that is an image where pixels are either zero (black) or 255(white)

# threshold example:
# take an image and take some particular value that we're going to call the thresholding value
# and compare each pixel of the image to this threshold value
# if that pixel intensity is less than the threshold value, we set that pixel intensity to zero
# and if it's above this threshold value, we set it to 255 (white)
# we can essentially create a binary image just from a regular standalone image
# using simple thresholding and adaptive thresholding

# simple: manually specify a threshold value
# adaptive: opencv does that for us using a specific block size or current size and other computing
# the thresholdd of value on the basis of the mean, or on the Gaussian distribution

import cv2 as cv

img = cv.imread('Photos/cats.jpg')
cv.imshow('Cats' , img)

# first convert this BGR image to grayscale
gray = cv.cvtColor(img , cv.COLOR_BGR2GRAY)
cv.imshow('Gray' , gray)

# Simple Thresholding

# looks at the image and compare each pixel value to this threshold value (150)
# and if the value is greater than 150, since we want to binarize the image, we set it to 255
# and specify a threshold type cv.THRESH_BINARY
threshold , thresh = cv.threshold(gray, 150 , 255 , cv.THRESH_BINARY )
cv.imshow('Simple Thresholded' , thresh)

threshold , thresh_inv = cv.threshold(gray, 100 , 255 , cv.THRESH_BINARY_INV)
cv.imshow('Simple Thresholded Inverse' , thresh_inv)

# Adaptive Thresholding

# differently from simple trhesholding, adaptive thresholding lets the computer find the optimal threshold
# and using that value that refines, it binarizes over the image

adaptive_thresh = cv.adaptiveThreshold(gray , 255 , cv.ADAPTIVE_THRESH_GAUSSIAN_C , cv.THRESH_BINARY_INV ,  11 , 9)
cv.imshow('Adptive Thresholding' , adaptive_thresh)

cv.waitKey(0)
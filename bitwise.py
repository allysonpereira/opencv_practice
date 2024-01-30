# bitwise operators
# bitwise operators operate in a binary manner
# so a pixel is turned off if it has a value of zero, and is turned on if it has a value of one

import cv2 as cv
import numpy as np

blank = np.zeros((400,400) , dtype='uint8')

rectangle = cv.rectangle(blank.copy() , (30,30) , (370,370) , 255 , -1) #thickness -1 to fill the image
circle = cv.circle(blank.copy() , (200,200) , 200 , 255 , -1)

cv.imshow('Rectangle' , rectangle)
cv.imshow('Circle' , circle)

# bitwise AND --> intersecting regions
# places the two images on top of each other and returns the intersection
bitwise_and = cv.bitwise_and(rectangle , circle)
cv.imshow('Bitiwse AND' , bitwise_and)

# bitwise OR --> non-intersecting and intersecting regions
# returns both the intersecting as well as the non-intersecting regions
bitwise_or = cv.bitwise_or(rectangle, circle)
cv.imshow('Bitwise OR' , bitwise_or)

# bitwise XOR --> non-intersecting regions
# good for returning the non-intersecting regions
bitwise_xor = cv.bitwise_xor(rectangle , circle)
cv.imshow('Bitwise XOR' , bitwise_xor)

# bitwise NOT
# inverts the binary color
bitwise_not = cv.bitwise_not(rectangle)
cv.imshow('Bitwise NOT' , bitwise_not)


cv.waitKey(0)
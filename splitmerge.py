# how to split into 3 respective color channels 
# merge color channels
# how to reconstruct the image to display the actual color in that channel
# how to merge those color channels back into its original image


import cv2 as cv
import numpy as np

img = cv.imread('Photos/park.jpg')
cv.imshow('Park' , img)

blank = np.zeros(img.shape[:2] , dtype='uint8')

b,g,r = cv.split(img)

blue = cv.merge([b,blank,blank])
green = cv.merge([blank,g,blank])
red = cv.merge([blank,blank,r])

cv.imshow('Blue' , blue)
cv.imshow('Green' , green)
cv.imshow('Red' , red)

print(img.shape)
print(b.shape)
print(g.shape)
print(r.shape)

merged = cv.merge([b,g,r])
cv.imshow('Merge' , merged)

cv.waitKey(0)
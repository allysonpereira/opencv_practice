# use a haar cascade classifier to detect faces that are present in an image
# fac detection does not involve skin tone or the colors that are present in the image
# these haar cascades essentially look at an object in an image and using the edges tries to determine...
# wheter it's a face or not. That's why we don't need color in our image

import cv2 as cv

img = cv.imread('Photos/group 1.jpg')
cv.imshow('Big group of people' , img)

# first convert the image to gray scale
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Gray People' , gray)

# read those 33000 lines of xml code and store in a variable called haar_cascade
haar_cascade = cv.CascadeClassifier('haar_face.xml')

faces_rect = haar_cascade.detectMultiScale(gray , scaleFactor=1.1, minNeighbors=1)

print(f'Number of faces found = {len(faces_rect)}')

for (x,y,w,h) in faces_rect:
    cv.rectangle(img, (x,y) , (x+w, y+h) , (0,255,0) , thickness=2)

cv.imshow('Detected Faces', img )

cv.waitKey(0)
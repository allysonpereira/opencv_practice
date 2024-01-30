# computing histograms
# histograms allow you to visualize the distribution of pixel intesities in an image
# wheter it's a color image, or wheter it's a grayscale image, you can visualise these pixel intensity
# with help of a histogram
# which is kind of like a graph or a plot that will give you a high level intuition of the pixel
# distribution in the image

import cv2 as cv
import matplotlib.pyplot as plt
import numpy as np

img = cv.imread('Photos/cats.jpg')
cv.imshow('Cats' , img)

blank = np.zeros(img.shape[:2] , dtype='uint8')

# gray = cv.cvtColor(img , cv.COLOR_BGR2GRAY)
# cv.imshow('Gray' , gray)

mask = cv.circle(blank , (img.shape[1]//2 , img.shape[0]//2) , 100, 255, -1)

masked = cv.bitwise_and(img, img, mask=mask)
cv.imshow('Mask' , masked)

# Grayscale histogram
# this method will compute the histogram for the image that we pass into
# gray_hist = cv.calcHist([gray] , [0] , mask , [256] , [0,256]) 

# plt.figure()
# plt.title('Grayscale Histogram')
# plt.xlabel('Bins')
# plt.ylabel('# of pixels')
# plt.plot(gray_hist)
# plt.xlim([0,256])
# plt.show()


# Colour Histogram

plt.figure()
plt.title('Colour Histogram')
plt.xlabel('Bins')
plt.ylabel('# of pixels')
colors = ('b' , 'g' , 'r')
for i, col in enumerate(colors):
    hist = cv.calcHist([img] , [i] , mask , [256] , [0,256])
    plt.plot(hist , color=col)
    plt.xlim([0,256])

plt.show()

cv.waitKey(0)
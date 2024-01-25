import cv2 as cv

# img = cv.imread('Photos/cat_large.jpg')

# cv.imshow('Cat', img)

# Reading videos

capture = cv.VideoCapture('Videos/dog.mp4')



# read a video frame by frame

while True:

    # returns the frame and a boolean that says wheter the frame was successfully read in or not
    isTrue , frame = capture.read() # read a video frame by frame

    # display an individual frame
    cv.imshow('Video' , frame)

    # stop the video
    if cv.waitKey(20) & 0xFF==ord ('d'):
        break

capture.release()
cv.destroyAllWindows()

#cv.waitKey(0)

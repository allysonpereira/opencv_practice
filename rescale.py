import cv2 as cv

# img = cv.imread('Photos/cat_large2.jpg')
# cv.imshow('Cat', img)

def rescaleFrame (frame, scale = 0.75): # works for images, videos and live video
    width = int (frame.shape[1] * scale)
    height = int (frame.shape[0] * scale)

    dimensions = (width , height)

    return cv.resize(frame, dimensions, interpolation = cv.INTER_AREA)

def changeRes (width , height): # works for live video only
    capture.set(3 , width)
    capture.set(4 , height)

# Reading videos

capture = cv.VideoCapture('Videos/dog.mp4')

while True: # read a video frame by frame
  
    isTrue , frame = capture.read()  # returns the frame and a boolean that says wheter the frame was successfully read in or not

    frame_resized = rescaleFrame(frame , scale = .2)
    cv.imshow('Video' , frame) # display an individual frame
    cv.imshow('Vido Resized' , frame_resized)

    if cv.waitKey(20) & 0xFF==ord ('d'): # stop the video
        break

capture.release()
cv.destroyAllWindows()

#cv.waitKey(0)

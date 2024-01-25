import cv2
import sys

print(sys.version)
#print(cv.__version__)

cap = cv2.VideoCapture(0) # creates a VideoCapture object (cap) to capture video

while(True):
    ret, frame = cap.read()

    if not ret: # if the frame is empty, it prints a message and exits the loop
        print("Empty frame")
        break

    cv2.imshow('frame' , frame)  # displays the captured frame in a window named frame

    if cv2.waitKey(1) & 0xFF == ord('q'): # waits for a key event. if the key pressed is 'q', it breaks out of the loop
        break

cap.release()
cv2.destroyAllWindows()






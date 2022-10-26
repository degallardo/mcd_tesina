"""Access IP Camera in Python OpenCV"""

import cv2

# stream = cv2.VideoCapture('protocol://IP:port/1')

# Use the next line if your camera has a username and password
stream = cv2.VideoCapture('rtsp://admin:Ga11ard0@192.168.1.5:554/1')  

while True:

    r, f = stream.read()
    cv2.imshow('IP Camera stream',f)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cv2.destroyAllWindows()
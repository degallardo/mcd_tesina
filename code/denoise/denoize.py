# fastNlMeansDenoisingColored
# Wait for result, takes time to respond
import cv2
from tkinter import filedialog
from tkinter import *
import time

root = Tk()
# Do not show graphics window
root.withdraw()

# Load the original color image
origColorImage = cv2.imread(filedialog.askopenfilename(),1)

# Image must have 3 channels
print("Shape of image ", origColorImage.shape)

dest = cv2.fastNlMeansDenoisingColored(origColorImage,None,10,10,7,21)

cv2.imshow('Original image',origColorImage)
cv2.imshow('fastNlMeansDenoisingColored',dest)

time.sleep(10)
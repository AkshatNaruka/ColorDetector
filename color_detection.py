
import cv2
import numpy as np
from tkinter import Tk     
from tkinter.filedialog import askopenfilename


# Reading the image
Tk().withdraw() 
filename = askopenfilename() 
img = cv2.imread(filename)

# Showing the output

cv2.imshow("Image", img)

cv2.waitKey(0)
cv2.destroyAllWindows()
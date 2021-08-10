import numpy as np
import cv2

# load the image and convert it to grayscale
image = cv2.imread("input.jpg")

#convert the image into gray color
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

#minMaxLoc() is used to find brightest pixel in the image
(minVal, maxVal, minLoc, maxLoc) = cv2.minMaxLoc(gray)

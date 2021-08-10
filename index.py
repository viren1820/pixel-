import numpy as np
import cv2

# load the image and convert it to grayscale
image = cv2.imread("input.jpg")

#convert the image into gray color
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

#minMaxLoc() is used to find brightest pixel in the image
(minVal, maxVal, minLoc, maxLoc) = cv2.minMaxLoc(gray)

#Draw the circle to the brightest pixel with specified radius , color & width
cv2.circle(image, maxLoc,67, (0,0, 255), 10)

# display the results of our newly improved method
im=cv2.resize(image, (960,800))

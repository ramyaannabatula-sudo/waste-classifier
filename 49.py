import cv2
import numpy as np

image = cv2.imread("134256573812053395.jpg")
image = cv2.resize(image, (800, 450))

hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

lower_green = np.array([35, 50, 50])
upper_green = np.array([85, 255, 255])

mask = cv2.inRange(hsv, lower_green, upper_green)

result = cv2.bitwise_and(image, image, mask=mask)

cv2.imshow("Original Image", image)
cv2.imshow("Green Mask", mask)
cv2.imshow("Green Objects", result)

cv2.waitKey(0)
cv2.destroyAllWindows()
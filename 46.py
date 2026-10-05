import cv2

image = cv2.imread("134256573812053395.jpg")

image = cv2.resize(image, (800, 450))

gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

threshold = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)

cv2.imshow("Grayscale", gray)
cv2.imshow("Threshold", threshold[1])

cv2.waitKey(0)
cv2.destroyAllWindows()
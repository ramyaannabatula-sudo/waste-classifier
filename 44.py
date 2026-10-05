import cv2

image = cv2.imread("134256573812053395.jpg")

image = cv2.resize(image, (800, 450))

gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

edges = cv2.Canny(gray, 100, 200)

cv2.waitKey(0)
cv2.destroyAllWindows()
threshold = cv2.threshold(gray, 200, 255, cv2.THRESH_BINARY)

cv2.imshow("Threshold Image", threshold[1])

cv2.waitKey(0)
cv2.destroyAllWindows()
import cv2

image = cv2.imread("134256573812053395.jpg")
image = cv2.resize(image, (800, 450))

gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

adaptive = cv2.adaptiveThreshold(
    gray,
    255,
    cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
    cv2.THRESH_BINARY,
    11,
    2
)

cv2.imshow("Grayscale", gray)
cv2.imshow("Adaptive Threshold", adaptive)

cv2.waitKey(0)
cv2.destroyAllWindows()
import cv2
image = cv2.imread("134256573812053395.jpg")
image = cv2.resize(image,(600,400))

cv2.imshow("My Image",image)
cv2.waitKey(0)
cv2.destroyAllWindows()
import cv2
import numpy as np

image = cv2.imread("134256573812053395.jpg")
image = cv2.resize(image, (800, 450))

hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

lower_green = np.array([25, 30, 30])
upper_green = np.array([95, 255, 255])

mask = cv2.inRange(hsv, lower_green, upper_green)

contours, hierarchy = cv2.findContours(
    mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE
)
print("Total contours:", len(contours))
print("White pixels:", cv2.countNonZero(mask))
cv2.imshow("Green Mask", mask)

result = image.copy()
count = 0

for contour in contours:
    area = cv2.contourArea(contour)

    if area > 100:
        x, y, w, h = cv2.boundingRect(contour)

        cv2.rectangle(
            result, (x, y), (x + w, y + h), (255, 0, 0), 2
        )

        count += 1

print("Green regions detected:", count)

cv2.imshow("Green Mask", mask)
cv2.imshow("Detected Green Regions", result)

cv2.waitKey(0)
cv2.destroyAllWindows()
import cv2

image = cv2.imread("134256573812053395.jpg")

image = cv2.resize(image, (800, 450))

gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

threshold = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)

contours, hierarchy = cv2.findContours(
    threshold[1],
    cv2.RETR_EXTERNAL,
    cv2.CHAIN_APPROX_SIMPLE
)
contour_image = image.copy()
contour_image = image.copy()

object_count = 0

for contour in contours:
    area = cv2.contourArea(contour)

    if area > 500:
        object_count += 1

        x, y, w, h = cv2.boundingRect(contour)

        cv2.rectangle(contour_image, (x, y), (x + w, y + h), (255, 0, 0), 2)

        cv2.putText(
            contour_image,
            "Object " + str(object_count),
            (x, y - 10),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.5,
            (255, 0, 0),
            2)
        cv2.rectangle(
            contour_image,
            (x, y),
            (x + w, y + h),
            (255, 0, 0),
            2
        )

print("Objects detected:", object_count)

cv2.imshow("Large Contours", contour_image)
cv2.waitKey(0)
cv2.destroyAllWindows()

for contour in contours:
    area = cv2.contourArea(contour)

    if area > 500:
        print(area)
        x, y, w, h = cv2.boundingRect(contour)
        cv2.rectangle(contour_image, (x, y), (x + w, y + h), (255, 0, 0), 2)

        cv2.drawContours(contour_image, [contour], -1, (0, 255, 0), 2)
cv2.imshow("Large Contours", contour_image)

cv2.waitKey(0)
cv2.destroyAllWindows()

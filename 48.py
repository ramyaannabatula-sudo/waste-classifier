import cv2

image = cv2.imread("134256573812053395.jpg")
image = cv2.resize(image, (800, 450))

gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

threshold = cv2.threshold(
    gray, 127, 255, cv2.THRESH_BINARY
)

contours, hierarchy = cv2.findContours(
    threshold[1],
    cv2.RETR_EXTERNAL,
    cv2.CHAIN_APPROX_SIMPLE
)

object_count = 0
result = image.copy()

for contour in contours:
    area = cv2.contourArea(contour)

    if area > 5000:
        object_count += 1

        x, y, w, h = cv2.boundingRect(contour)

        cv2.rectangle(
            result,
            (x, y),
            (x + w, y + h),
            (255, 0, 0),
            2
        )

        cv2.putText(
            result,
            str(round(area)),
            (x, y - 5),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.5,
            (255, 0, 0),
            2
        )

print("Objects detected:", object_count)

cv2.imshow("Detected Objects", result)
cv2.waitKey(0)
cv2.destroyAllWindows()
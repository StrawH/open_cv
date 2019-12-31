"""
----------> detecting specific color <---------

for red color:
lower=[170, 50, 50], upper=[180, 225, 225]

for green color:
lower=[36, 25, 25], upper=[70, 225, 225]
"""
import imutils
import cv2
import open_cv_configs as ocv

cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()

    mask = ocv.make_mask_for_image(frame, lower=[170, 50, 50], upper=[180, 225, 225])
    contour = cv2.findContours(mask.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    contour = imutils.grab_contours(contour)

    for c in contour:
        rect = cv2.boundingRect(c)

        if rect[2] < 100 or rect[3] < 100:
            continue

        cv2.contourArea(c)
        x, y, w, h = rect
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
        cv2.putText(frame, 'Detected', (x + w + 10, y + h), 0, 0.3, (0, 255, 0))

    cv2.imshow('show', frame)

    if cv2.waitKey(100) & 255 == ord('0'):
        break

cap.release()
cv2.destroyAllWindows()


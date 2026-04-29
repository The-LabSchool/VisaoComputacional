import cv2 as cv

cap = cv.VideoCapture(0)

while True:
    ret, frame = cap.read()

    # if frame is read correctly ret is True
    if not ret:
        print("Can't receive frame (stream end?). Exiting ...")
        break

    gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
    _, th = cv.threshold(gray, 100, 255, cv.THRESH_BINARY)

    cv.imshow("frame", th)
    if cv.waitKey(1) == ord("q"):
        break

cap.release()
cv.destroyAllWindows()

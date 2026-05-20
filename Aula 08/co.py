import cv2 as cv

# Extract the patent image using contours
patent = cv.imread("patent.jpg")

gray = cv.cvtColor(patent, cv.COLOR_BGR2GRAY)

_, th = cv.threshold(gray, 200, 255, cv.THRESH_BINARY_INV)

cv.imwrite("th.jpg", th)

contours, hierarchy = cv.findContours(th, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE)

print(f"Contornos: {len(contours)}")

# Draw contours
drawn = cv.drawContours(patent.copy(), contours, -1, (0, 255, 0))

cv.imwrite("cont.jpg", drawn)

contours_filtered = []

for con in contours:
    area = cv.contourArea(con)
    if area > 200:
        print(f"Area: {area}")
        contours_filtered.append(con)

drawn_filtered = cv.drawContours(patent, contours_filtered, -1, (0, 255, 0))

cv.imwrite("con_filtered.jpg", drawn_filtered)

import cv2 as cv

# Threshold space using otsu
space = cv.imread("space.jpg")

gray = cv.cvtColor(space, cv.COLOR_BGR2GRAY)

_, mask = cv.threshold(gray, 50, 255, cv.THRESH_OTSU)

cv.imwrite("otsu_space_mask.jpg", mask)

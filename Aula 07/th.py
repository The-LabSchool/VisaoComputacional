import cv2 as cv

# Threshold space using threshold
space = cv.imread("space.jpg")

gray = cv.cvtColor(space, cv.COLOR_BGR2GRAY)

_, mask = cv.threshold(gray, 50, 255, cv.THRESH_BINARY_INV)

cv.imwrite("mask.jpg", mask)

# Change background color to red

space[mask == 255] = (255, 0, 0)

cv.imwrite("blue_space.jpg", space)

# Threshold circle using otsu

circle = cv.imread("circle.png")

gray_circle = cv.cvtColor(circle, cv.COLOR_BGR2GRAY)

cv.imwrite("gray_circle.jpg", gray_circle)

thresh, mask = cv.threshold(gray_circle, 50, 255, cv.THRESH_OTSU)
print(f"The threshold is: {thresh}")
cv.imwrite("circle_mask.jpg", mask)


# Threshold space using otsu

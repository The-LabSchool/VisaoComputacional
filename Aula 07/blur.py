import cv2 as cv

# Apply blur to space using GaussianBlur or medianBlur

space = cv.imread("palo.jpg")
blurred = cv.medianBlur(space, 5)

cv.imwrite("palo_blurred.jpg", blurred)

blurred_gray = cv.cvtColor(blurred, cv.COLOR_BGR2GRAY)

_, background_mask = cv.threshold(blurred_gray, 50, 255, cv.THRESH_OTSU)

cv.imwrite("palo_background_mask.jpg", background_mask)

# Sem blur

space_gray = cv.cvtColor(space, cv.COLOR_BGR2GRAY)

_, background_mask = cv.threshold(space_gray, 50, 255, cv.THRESH_OTSU)

cv.imwrite("palo_background_no_blur_mask.jpg", background_mask)

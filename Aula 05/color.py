# Load image
import cv2 as cv
import numpy as np

img = cv.imread("cute.jpg")

# Change color space to greyscale

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
# Save image

print(f"Shape: {gray.shape}")
cv.imwrite("gray.jpg", gray)

# Change some color of an image to black or another color

inv = 255 - img

# Save image

cv.imwrite("dim.jpg", inv)

# Remove white
height, width, _ = img.shape

for h in range(height):
    for w in range(width):
        pixel = img[h][w]
        if pixel[0] > 200 and pixel[1] > 200 and pixel[2] > 200:
            img[h][w] = (0, 255, 255)

cv.imwrite("yellow.jpg", img)

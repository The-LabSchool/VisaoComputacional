# Load an image
import cv2 as cv

img = cv.imread("cute.jpg")
print(f"Formato: {img.shape}")
print(f"Max: {img.max()}")
print(f"Min: {img.min()}")

# Draw rectangle

img2 = cv.rectangle(img, (50, 50), (100, 100), (0, 0, 255))

# Save image
cv.imwrite("modificado.jpg", img2)

# Draw circle

# Set blue to 0
img[:, :, 0] = 0
# Set green to 0
img[:, :, 1] = 0

cv.imwrite("red.jpg", img)

# Save image

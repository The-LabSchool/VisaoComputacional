# Você está tentando fazer uma peça artistica beseado nas imagens do James Webb Telescope.
# Você deve primeiro extrair o fundo preto da imagem e substitui-lo por uma das três cores em RGB aleatoriamente:
# [(194,211,205), (159,164,169), (86,73,76)]

# Nota: Lembre-se que por padrão o opencv abre a imagem em BGR em vez de RGB!

import cv2 as cv
import random

img = cv.imread("space.jpg")
colors = [(205, 211, 194), (169, 164, 159), (76, 73, 86)]

height, width, _ = img.shape

for h in range(height):
    for w in range(width):
        pixel = img[h][w]
        if pixel[0] < 90 and pixel[1] < 50 and pixel[2] < 100:
            c = random.randint(0, 2)
            img[h][w] = colors[c]

cv.imwrite("palo.jpg", img)

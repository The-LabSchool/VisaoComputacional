# Você está tentando fazer uma peça artistica beseado nas imagens do James Webb Telescope.
# Você deve primeiro extrair o fundo preto da imagem e substitui-lo por uma das três cores em RGB aleatoriamente:
# [(194,211,205), (159,164,169), (86,73,76)]

# Nota: Lembre-se que por padrão o opencv abre a imagem em BGR em vez de RGB!

import cv2 as cv

space = cv.imread("space.jpg")
cat = cv.imread("cat.jpg")

height, width, _ = space.shape

cat = cv.resize(cat, (width, height))

for h in range(height):
    for w in range(width):
        pixel = space[h][w]
        if pixel[0] < 90 and pixel[1] < 50 and pixel[2] < 100:
            space[h][w] = cat[h][w]

cv.imwrite("palo.jpg", space)

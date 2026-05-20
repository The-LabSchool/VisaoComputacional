# Você está tentando processar multiplos raio-x para detectar anomalias. Infelizmente alguns raio-x não estão no formato certo para deixar sua pesquisa fácil.
# Geralmente raio-x usam as cores mais escuras para representar as áreas menos densas da imagem, enquanto as cores claras representam áreas de alta densidade, como ossos.
# Transforme a imagem xray-inverted.jpg para que siga o mesmo padrão, ossos brancos e fundo preto, em vez da estrutura atual.

import cv2 as cv
import numpy as np

img = cv.imread("xray-inverted.jpg")

inv = 255 - img

cv.imwrite("inv.jpg", inv)

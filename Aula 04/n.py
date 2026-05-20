import numpy as np

# Criando uma array com arrange
a = np.arange(12).reshape((3, 4))

# print(a)
# Vendo propiedades de uma array (shape, len, flatten)
# print(f'Shape: {a.shape}')
# print(f'Len: {len(a)}')

# Mudando o formato de uma array (reshape)
mudado = a.reshape((1, 2, 2, 3))

# print('Mudado:', mudado)
# Indexando uma array multidimensional
b = np.arange(20).reshape((2, 5, 2))

# print(b)
# print('Elemento na posição [0, 1, 0]:\n', b[0, 1])

# Slicing the uma array multidimensional
c = np.arange(10 * 10 * 3).reshape((10, 10, 3))
# print(c[0:5, 0:5, :])

# O que é uma mascara

# Mascaras
a = np.arange(20)
print(a)
# print(a > 5)

# Mudando dados via mascaras
# print(a[a > 5])
a[a > 5] = 0
print(a)

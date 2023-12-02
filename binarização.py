# -*- coding: utf-8 -*-
"""Binarização

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1hUDz5o7YbIjuoODbVDSnYTyDjKWkpfsN
"""

#Beatriz Leonara
#Ivyna Alves S. Magalhães

import cv2
from google.colab.patches import cv2_imshow
from PIL import Image

#Trasformando em cinza
img = cv2.imread("coins.png", 0)

#Binarização
img = cv2.imread("coins.png", cv2.IMREAD_GRAYSCALE)
_, imagem_binarizada = cv2.threshold(img, 81, 255, cv2.THRESH_BINARY)
cv2_imshow(imagem_binarizada)
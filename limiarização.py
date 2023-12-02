# -*- coding: utf-8 -*-
"""Limiarização

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1ZYRYWbcP9FEogiRxi_35u3x01FaXoCQ3
"""

#Beatriz Leonara
#Ivyna Alves S. Magalhães

import cv2
from google.colab.patches import cv2_imshow
from PIL import Image

#Trasformando em cinza
img = cv2.imread("coins.png", 0)

#Limiarização
img = cv2.imread("coins.png", cv2.IMREAD_GRAYSCALE)
_,imagem_limiarizada = cv2.threshold(img,80,255,cv2.THRESH_TOZERO)
cv2_imshow(imagem_limiarizada)
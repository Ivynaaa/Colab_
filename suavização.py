# -*- coding: utf-8 -*-
"""Suavização

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1WH38vhhd6_9dmTa4er3pkU0LIQpYnnv0
"""

#Ivyna Alves
#Beatriz Leonara

import cv2
import numpy as np
from google.colab.patches import cv2_imshow

img = cv2.imread('einsteinRuido.jpg')
img2 = cv2.medianBlur(img, 5)
cv2_imshow(img2)

import cv2
import numpy as np
from google.colab.patches import cv2_imshow

img = cv2.imread('tomografiaRuido.jpg')
ksize = (7,7)
img2 = cv2.blur(img, ksize)
cv2_imshow(img2)
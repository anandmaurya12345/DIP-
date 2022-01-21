# -*- coding: utf-8 -*-
"""DIPassignment3.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1NwzP2BqZNn11K0Odnr3XXTpWoU-ANP7h
"""

from PIL import Image, ImageDraw
import matplotlib.pyplot as plt

import numpy as np
import matplotlib.pyplot as plt

circleImage = Image.new(mode= 'L', size=(200, 200), color = 0)
circle = ImageDraw.Draw(circleImage)
circle.ellipse([(40, 40), (160, 160)], fill = 'white', outline='white')

plt.imshow(circleImage, cmap = 'gray')

rectangleImage = Image.new(mode= 'L', size=(200, 200), color = 0)
rectangle = ImageDraw.Draw(rectangleImage)
rectangle.rectangle([(30,50), (170,150)], fill = 'white', outline= 'white')

plt.imshow(rectangleImage, cmap='gray')

circleImage = np.asarray(circleImage)
rectangleImage = np.asarray(rectangleImage)

# AND gate
and_img = np.zeros((200, 200))
for i in range(200):
    for j in range(200):
        if(circleImage[i,j] == 255 and rectangleImage[i,j] == 255):
            and_img[i,j] = 255

plt.imshow(and_img, cmap='gray')

# OR gate
orectangleImage = np.zeros((200, 200))
for i in range(200):
    for j in range(200):
        if(circleImage[i,j] == 255 or rectangleImage[i,j] == 255):
            orectangleImage[i,j] = 255

plt.imshow(orectangleImage, cmap='gray')

#NAND Gate
nand_img = np.zeros((200, 200))
for i in range(200):
    for j in range(200):
        if(not(circleImage[i,j] == 255 and rectangleImage[i,j] == 255)):
            nand_img[i,j] = 255

plt.imshow(nand_img, cmap='gray')

# NOR gate
norectangleImage = np.zeros((200, 200))
for i in range(200):
    for j in range(200):
        if(not(circleImage[i,j] == 255 or rectangleImage[i,j] == 255)):
            norectangleImage[i,j] = 255

plt.imshow(norectangleImage, cmap='gray')

#NOT gate
not_img = np.zeros((200, 200))
for i in range(200):
    for j in range(200):
        if(not_img[i,j] == 0):
            not_img[i,j] = 255

plt.imshow(not_img, cmap='gray')

# XOR gate
xorectangleImage = np.zeros((200, 200))
for i in range(200):
    for j in range(200):
        if(circleImage[i,j] != rectangleImage[i,j]):
            xorectangleImage[i,j] = 255

plt.imshow(xorectangleImage, cmap='gray')


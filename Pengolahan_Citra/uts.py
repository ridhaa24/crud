# -*- coding: utf-8 -*-
"""
Created on Mon Dec  9 01:20:26 2024

@author: User
"""

import cv2
import matplotlib.pyplot as plt
import numpy as np

gambar = cv2.imread('burung_pipit.jpg', cv2.IMREAD_GRAYSCALE)

plt.figure(figsize=(10, 5))
plt.subplot(2, 4, 1)
plt.imshow(gambar, cmap='gray')
plt.title("Gambar Asli")

plt.subplot(2, 4, 2)
plt.hist(gambar.flatten(), 256, [0, 256])
plt.title("Histogram Gambar Asli")

gambar_cerah = cv2.convertScaleAbs(gambar, alpha=1, beta=50)

plt.subplot(2, 4, 3)
plt.imshow(gambar_cerah, cmap='gray')
plt.title("Gambar Cerah")

plt.subplot(2, 4, 4)
plt.hist(gambar_cerah.flatten(), 256, [0, 256])
plt.title("Histogram Gambar Cerah")


gambar_ekualisasi = cv2.equalizeHist(gambar_cerah)

plt.subplot(2, 4, 5)
plt.imshow(gambar_ekualisasi, cmap='gray')
plt.title("Gambar Ekualisasi")

plt.subplot(2, 4, 6)
plt.hist(gambar_ekualisasi.flatten(), 256, [0, 256])
plt.title("Histogram Gambar Ekualisasi")

plt.show()





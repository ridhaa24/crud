# -*- coding: utf-8 -*-
"""
Created on Mon Dec  9 02:14:02 2024

@author: User
"""

import cv2

# Pengolahan gambar
gambar = cv2.imread('burung_pipit.jpg')
gambar_hasil = cv2.cvtColor(gambar, cv2.COLOR_BGR2GRAY)

# Menyimpan hasil
cv2.imwrite('gambar_hasil.jpg', gambar_hasil)
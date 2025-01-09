# -*- coding: utf-8 -*-
"""
Created on Mon Dec  9 02:29:00 2024

@author: User
"""

# Import library
import cv2

# Definisi fungsi
def tampilkan_gambar():
 # Baca gambar
 gambar = cv2.imread('gambar.jpg')

 # Tampilkan gambar
 cv2.imshow('Gambar', gambar)
 cv2.waitKey(0)
 cv2.destroyAllWindows()
# -*- coding: utf-8 -*-
"""
Created on Mon Dec  9 09:44:06 2024

@author: User
"""

import numpy as np
import cv2 as cv

gambar = cv.imread ('gambar1.jpg',0)

kernel1 = np.array([[1,1,1],[1,-8,1],[1,1,1]])
kernel1 = kernel1.astype('float32')


gambar_filtered1 = cv.filter2D(gambar,-1, kernel1)


cv.imshow('Gambar_Asli',gambar)
cv.imshow('Gambar Filtered 1',gambar_filtered1)

cv.waitKey(0)
cv.destroyAllWindows()
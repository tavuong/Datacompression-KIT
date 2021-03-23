# -*- coding: utf-8 -*-
from math import cos, pi, sqrt
import numpy as np



def dct_2d(image, numberCoefficients=0):
    
    nc = numberCoefficients
    height = image.shape[0]
    width = image.shape[1]
    imageRow = np.zeros_like(image).astype(float)
    imageCol = np.zeros_like(image).astype(float)

    for h in range(height):
        imageRow[h, :] = dct_1d(image[h, :], nc) # DCT -1D der Zeilen
    for w in range(width):
        imageCol[:, w] = dct_1d(imageRow[:, w], nc) # DCT -1D der Splaten

    return imageCol

def dct_1d(image, numberCoefficients=0):
    
    nc = numberCoefficients
    n = len(image)
    newImage= np.zeros_like(image).astype(float)
  
    for k in range(n):
        sum = 0
        for i in range(n):
            sum += image[i] * cos(2 * pi * k / (2.0 * n) * i + (k * pi) / (2.0 * n))
        ck = sqrt(0.5) if k == 0 else 1
        newImage[k] = sqrt(2.0 / n) * ck * sum

    # Speichern der größten N-Nummern und Zurücksetzen aller anderen
    if nc > 0:
        newImage.sort()
        for i in range(nc, n):
            newImage[i] = 0

    return newImage # return als vector 1D

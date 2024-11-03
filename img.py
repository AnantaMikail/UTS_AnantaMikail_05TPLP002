import numpy as np
import cv2 as cv

imgRgb = cv.imread("LOGO-UNPAM-COLOR.jpg", cv.IMREAD_COLOR)
imgGrayscale = cv.imread("LOGO-UNPAM-COLOR.jpg", cv.IMREAD_GRAYSCALE)

print('\nRGB Image')
print(imgRgb.shape)
print(imgRgb.size)
print(imgRgb.dtype)

print('\nGrayscale Image')
print(imgGrayscale.shape)
print(imgGrayscale.size)
print(imgGrayscale.dtype)

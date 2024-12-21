import numpy as np
from PIL import Image
import cv2 as cv

img = cv.imread("test_image.jpg")
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

print(gray)
import numpy as np
from PIL import Image
import cv2 as cv
import string

UpperCases = list(string.ascii_uppercase)

img = cv.imread("cat.png")
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)


gray = np.floor(gray / 10).astype(int)

gray_obj = gray.astype(object)
gray_obj[gray == 25] = "A"


for i in range(0,25):
    gray_obj[gray == i] = UpperCases[i]

with open("manipulated_test.txt", "w") as f:
    for row in gray_obj:
        f.write(" ".join(map(str, row)) + "\n")
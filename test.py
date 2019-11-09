import cv2
import sys
import numpy as np
from img2code import convert

img = cv2.imread("ruler.jpg", cv2.IMREAD_GRAYSCALE)

t = map(lambda xs: map(convert, xs), img)
z = map(lambda x: ''.join(x), t)
y = '\n'.join(list(z))

print(img[30][27])
print(y)
file = open("t.txt", "w+")
file.write(y)

# cv2.imshow("hah", img)
# cv2.waitKey(0)

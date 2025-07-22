import cv2 
import numpy as np
src1=cv2.imread("President1.jfif")
src2=cv2.imread("President2.jfif")
h1=np.hstack([src1],[src2])
cv2.imwrite("Image1.png",h1)

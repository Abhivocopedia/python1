import cv2
import numpy as np

src1=cv2.imread("President1.jfif")
src2=cv2.imread("President2.jfif")
src3=cv2.imread("President3.jfif")
src4=cv2.imread("President4.jfif")

src5=cv2.imread("President5.jfif")
src6=cv2.imread("President6.jfif")
src7=cv2.imread("President7.jfif")
src8=cv2.imread("President8.jfif")

src9=cv2.imread("President9.jfif")
src10=cv2.imread("President10.jfif")
src11=cv2.imread("President11.jfif")
src12=cv2.imread("President12.jfif")

src13=cv2.imread("President13.jfif")
src14=cv2.imread("President14.jfif")
src15=cv2.imread("President15.jfif")
src16=cv2.imread("President16.jfif")


h1=np.hstack([src1,src2,src3,src4])
h2=np.hstack([src5,src6,src7,src8])
h3=np.hstack([src9,src10,src11,src12])
h4=np.hstack([src13,src14,src15,src16])

v1=np.vstack([h1,h2,h3,h4])

cv2.imwrite("Image4.png",v1)

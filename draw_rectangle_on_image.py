import numpy as np
import cv2

img = cv2.imread('file_example.jpg',cv2.IMREAD_COLOR)

cv2.rectangle(img, (15,25), (200,150), (0,255,0), 5)

cv2.namedWindow('image',cv2.WINDOW_NORMAL)
cv2.resizeWindow('image',400,300)

cv2.imshow('image',img)

cv2.waitKey(0)
cv2.destroyAllWindows()
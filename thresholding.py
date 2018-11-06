import cv2
import numpy as np

img = cv2.imread('file_example.jpg')
retval, threshold = cv2.threshold(img, 200 , 255, cv2.THRESH_BINARY)
#anything below 200 will be white and anything above 200 will be black.

grayscaled = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
retval2, threshold2 = cv2.threshold(grayscaled, 200 , 255, cv2.THRESH_BINARY)

gauss = cv2.adaptiveThreshold(grayscaled,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY,115,1)


cv2.namedWindow('threshold', cv2.WINDOW_NORMAL)
cv2.resizeWindow('threshold',400,300)
cv2.imshow('threshold',threshold)

cv2.namedWindow('threshold2', cv2.WINDOW_NORMAL)
cv2.resizeWindow('threshold2',400,300)
cv2.imshow('threshold2',threshold2)

cv2.namedWindow('gauss', cv2.WINDOW_NORMAL)
cv2.resizeWindow('gauss',400,300)
cv2.imshow('gauss',gauss)

cv2.waitKey(0)
cv2.destroyAllWindows()
import imp


import cv2
from cv2 import rotate

img = cv2.imread('opencv/res/img.jpg')

rotate_90 = cv2.rotate(img, cv2.ROTATE_90_CLOCKWISE) # 시계 방향으로 90도 회전
rotate_180 = cv2.rotate(img, cv2.ROTATE_180) # 시계 방향으로 180도 회전
rotate_270 = cv2.rotate(img, cv2.ROTATE_90_COUNTERCLOCKWISE) # 시계 반대 방향으로 90도(270도) 회전

cv2.imshow('img', img)
cv2.imshow('rotate_90', rotate_90)
cv2.imshow('rotate_180', rotate_180)
cv2.imshow('rotate_270', rotate_270)

cv2.waitKey(0)
cv2.destroyAllWindows()
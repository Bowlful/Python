import cv2

img = cv2.imread('opencv/res/img.jpg')
flip_horizotal = cv2.flip(img, 1) # flipCode > 0 : 좌우 대칭 Horizontal 
flip_vertical = cv2.flip(img, 0) # flipCode == 0 : 상하 대칭 vertical 
flip_both = cv2.flip(img, -1) # flipCode < 0 : 상하좌우 대칭 vertical 


cv2.imshow('img', img)
cv2.imshow('flip_horizotal', flip_horizotal)
cv2.imshow('flip_vertical', flip_vertical)
cv2.imshow('flip_both', flip_both)

cv2.waitKey(0)
cv2.destroyAllWindows()
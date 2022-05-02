import cv2

img = cv2.imread('opencv/res/img.jpg')

dest = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

cv2.imshow('img', img)
cv2.imshow('dest', dest)

cv2.waitKey(0)
cv2.destroyAllWindows()
import cv2

#영역을 잘라서 새로운 윈도우(창)에 표시

img = cv2.imread('opencv/res/img.jpg')
print(img.shape) # (427, 640, 3)

crop = img[200:300, 200:400] # 세로 200:300, 가로 200:400
img[200:300, 400:600] = crop # 자른 영역을 기존윈도우에 표시

cv2.imshow('img', img)
cv2.imshow('crop', crop)

cv2.waitKey(0)
cv2.destroyAllWindows()
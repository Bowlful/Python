import cv2
from cv2 import LINE_AA
import numpy as np

# 세로 480 가로 640 3 Channel (RGB)에 해당하는 스케치북

img = np.zeros((480, 640, 3), dtype=np.uint8)
#img[:] = (255, 255, 255) # 전체 공간을 흰 색으로 채우기 ( B, G, R)

#img[100:200, 200:300] = (255, 255, 255)
# [세로영역, 가로영역]

#직선의 종류 (line type)
#1.cv2.LINE_4 : 상하좌우 4 방향으로 연결된 선
#2.cv2.LINE_8 : 대각선을 포함한 8 방향으로 연결된 선(기본값)
#3.cv2.LINE_AA : 부드러운 선 (anti-aliasing)

COLOR = (255, 255, 0) # BGR
RADIUS = 50
THIKNESS = 3 # 두께

cv2.line(img, (50, 100), (400, 50), COLOR, THIKNESS, cv2.LINE_8)
# 그릴 위치, 시작점, 끝점, 색깔, 두께, 선종류
cv2.line(img, (50, 200), (400, 150), COLOR, THIKNESS, cv2.LINE_4)
cv2.line(img, (50, 300), (400, 250), COLOR, THIKNESS, cv2.LINE_AA)

cv2.circle(img, (200, 100), RADIUS, COLOR, THIKNESS, cv2.LINE_AA)
# 그릴 위치, 원의 중심점, 반지름, 색깔, 두께, 선종류
cv2.circle(img, (400, 100), RADIUS, COLOR, cv2.FILLED, cv2.LINE_AA)

cv2.rectangle(img, (100, 100), (200, 200), COLOR, THIKNESS, cv2.LINE_AA)
# 그릴 위치, 왼쪽 위 좌표, 오른쪽 아래 좌표, 색깔, 두께, 선종류
cv2.rectangle(img, (300, 100), (400, 200), COLOR, cv2.FILLED, cv2.LINE_AA)

pts1 = np.array([[100, 100], [200, 100], [100, 200]])
pts2 = np.array([[200, 100], [300, 100], [300, 200]])

# cv2.polylines(img, [pts1], True, COLOR, THIKNESS, cv2.LINE_AA)
# cv2.polylines(img, [pts2], True, COLOR, THIKNESS, cv2.LINE_AA)
cv2.polylines(img, [pts1, pts2], True, COLOR, THIKNESS, cv2.LINE_AA)
# 그릴 위치, 그릴 좌표, 닫힘 여부, 색깔, 두께, 선 종류

pts3 = np.array([[[100, 300], [200, 300], [100, 400]], [[200, 300], [300, 300], [300, 400]]])
cv2.fillPoly(img, pts3, COLOR, cv2.LINE_AA)
# 그릴 위치, 그릴 좌표, 색깔, 선 종류

cv2.imshow('img', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
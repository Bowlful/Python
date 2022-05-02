import cv2
import numpy as np

# 이미지 변형(원근)
# 사다리꼴 이미지
newspaper = cv2.imread('opencv/res/newspaper.jpg')
poker = cv2.imread('opencv/res/poker.jpg')

n_width, n_height = 640,  240 # 가로 크기 640, 세로 크기 240 으로 결과물 출력 신문
p_width, p_height = 530,  710 # 가로 크기 530, 세로 크기 710 으로 결과물 출력 포커

n_src = np.array([[511, 352], [1008, 345], [1122, 584], [455, 594]], dtype=np.float32) # input 4개 지점
n_dst = np.array([[0, 0], [n_width, 0], [n_width, n_height], [0, n_height]], dtype=np.float32) # output 4개 지점

p_src = np.array([[702, 143], [1133, 414], [726, 1007], [276, 700]], dtype=np.float32) # input 4개 지점
p_dst = np.array([[0, 0], [p_width, 0], [p_width, p_height], [0, p_height]], dtype=np.float32) # output 4개 지점

# 좌상, 우상, 우하, 좌하 (시계 방향으로 4 지점 정의)

n_matrix = cv2.getPerspectiveTransform(n_src, n_dst) # Matrix 얻어옴
n_result = cv2.warpPerspective(newspaper, n_matrix, (n_width, n_height)) # Matrix 대로 변환을 함

p_matrix = cv2.getPerspectiveTransform(p_src, p_dst) # Matrix 얻어옴
p_result = cv2.warpPerspective(poker, p_matrix, (p_width, p_height)) # Matrix 대로 변환을 함


cv2.imshow('newspaper', newspaper)
cv2.imshow('poker', poker)
cv2.imshow('n_result', n_result)
cv2.imshow('p_result', p_result)

cv2.waitKey(0)
cv2.destroyAllWindows()
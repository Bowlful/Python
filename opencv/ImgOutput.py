import cv2


img_color = cv2.imread('opencv/res/img.jpg', cv2.IMREAD_COLOR)
img_gray = cv2.imread('opencv/res/img.jpg', cv2.IMREAD_GRAYSCALE)
img_unchanged = cv2.imread('opencv/res/img.jpg', cv2.IMREAD_UNCHANGED)

print(img_color.shape)
print(img_gray.shape)
print(img_unchanged.shape)

cv2.imshow('img_color', img_color)
cv2.imshow('img_gray', img_gray)
cv2.imshow('img_unchanged', img_unchanged)

cv2.waitKey(0) # 키입력까지 대기
cv2.destroyAllWindows()

# cv2.IMREAD_COLOR : 컬러 이미지. 투명 영역은 무시 (기본값)
# cv2.IMREAD_GRAYSCALE : 흑백 이미지
# cv2.IMREAD_UNCHANGED : 투명영역까지 포함

# Shape hight, width, channel 정보
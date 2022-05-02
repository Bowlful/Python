import cv2

img = cv2.imread('opencv/res/img.jpg')
cap = cv2.VideoCapture('opencv/res/video.mp4')

# 보간법
# cv2.IMTER_AREA : 크기 줄일 때 사용
# cv2.INTER_CUBIC : 크기 늘릴 때 사용 (속도가 느림, 퀄리티 좋음)
# cv2.INTER_LINEAR : 크기 늘릴 때 싸용 (기본값)

fix_dst = cv2.resize(img, (400, 500))# width, height 고정 크기
ratio_dst = cv2.resize(img, None, fx=1.5, fy=1.5, interpolation=cv2.INTER_CUBIC) # 비율로 설정 

while cap.isOpened(): 
    ret, frame = cap.read() 
    if not ret :
        break
    
    fix_frame_resized = cv2.resize(frame, (400, 500))
    ratio_frame_resized = cv2.resize(frame, None, fx=1.5, fy=1.5, interpolation=cv2.INTER_CUBIC)

    cv2.imshow('video',ratio_frame_resized)

    if cv2.waitKey(1) == ord('q') :
        break

cap.release()

cv2.imshow('img', img)
cv2.imshow('resize', ratio_dst)

cv2.waitKey(0)
cv2.destroyAllWindows()
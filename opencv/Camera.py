import cv2

cap = cv2.VideoCapture(0) # 0번째 카메라 장치

if not cap.isOpened(): # 카메라가 잘 열리지 않는 경우
    exit() # 프로그램 종료

while True :
    ret, frame = cap.read()
    if not ret :
        break
    
    cv2.imshow('camera', frame)
    if cv2.waitKey(1) == ord('q') :
        break

cap.release()
cv2.destroyAllWindows()

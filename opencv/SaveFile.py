import cv2

img = cv2.imread('opencv/res/img.jpg', cv2.IMREAD_GRAYSCALE)
cap = cv2.VideoCapture('opencv/res/video.mp4')

fourcc = cv2.VideoWriter_fourcc(*'DIVX')

width = round(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
height = round(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

fps = cap.get(cv2.CAP_PROP_FPS) * 2

out = cv2.VideoWriter('opencv/res/output.mp4', fourcc, fps, (width, height))

while cap.isOpened() :
    ret, frame = cap.read()

    if not ret :
        break
    
    out.write(frame) # 영상 데이터만 저장 (소리 X)

    cv2.imshow('video', frame)
    if cv2.waitKey(1) == ord('q') : 
        break

out.release() # 자원 해제
cap.release()
cv2.imshow('img', img)
cv2.waitKey(0)
cv2.destroyAllWindows()

result = cv2.imwrite('opencv/res/img_save.png', img )
print(result)
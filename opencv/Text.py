import cv2
import numpy as np
from PIL import ImageFont, ImageDraw, Image

def myPutText(src, text, pos, font_size, font_color) :
    img_pil = Image.fromarray(src)
    draw = ImageDraw.Draw(img_pil)
    font = ImageFont.truetype('fonts/gulim.ttc', font_size)
    draw.text(pos, text, font=font, fill=font_color)
    return np.array(img_pil)


# cv2.FONT_HERSHEY_SIMPLEX : 보통 크기의 산 세리프(sans-serif) 글꼴
# cv2.FONT_HERSHEY_PLAIN : 작은 크기의 산 세리프 글꼴
# cv2.FONT_HERSHEY_SCRIPT_SIMPLEX : 필기체 스타일 글꼴
# cv2.FONT_HERSHEY_TRIPLEX : 보통 크기의 세리프 글꼴
# cv2.FONT_ITALIC : 기울임 (이탤릭체)

img = np.zeros((480, 640, 3), dtype=np.uint8)

SCALE = 1
COLOR = (255, 255, 255) # 흰색
THICKNESS = 1

# cv2.putText(img, "Simplex", (20, 50), cv2.FONT_HERSHEY_SIMPLEX, SCALE, COLOR, THICKNESS, cv2.LINE_AA)
# cv2.putText(img, "Plan", (20, 150), cv2.FONT_HERSHEY_PLAIN, SCALE, COLOR, THICKNESS, cv2.LINE_AA)
# cv2.putText(img, "Scrpt Simplex", (20, 250), cv2.FONT_HERSHEY_SCRIPT_SIMPLEX, SCALE, COLOR, THICKNESS, cv2.LINE_AA)
# cv2.putText(img, "Triplex", (20, 350), cv2.FONT_HERSHEY_TRIPLEX, SCALE, COLOR, THICKNESS, cv2.LINE_AA)
# cv2.putText(img, "Italic", (20, 450), cv2.FONT_HERSHEY_TRIPLEX | cv2.FONT_ITALIC, SCALE, COLOR, THICKNESS, cv2.LINE_AA)

#cv2.putText(img, "심플릭스", (20, 50), cv2.FONT_HERSHEY_SIMPLEX, SCALE, COLOR, THICKNESS, cv2.LINE_AA)

FONT_SIZE = 30

img = myPutText(img, "심플", (20, 50), FONT_SIZE, COLOR)

cv2.imshow('img', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
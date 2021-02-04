import cv2
import numpy as np

img = np.zeros((512,512)) # 0으로 구성된 배열을 만들어 이미지로 나타내본다. 이 이미지는 Grayscale이다(1개의 채널만 존재하므로)
print(img.shape)
cv2.imshow("Image", img)
cv2.waitKey(0)

img2 = np.zeros((512,512,3),np.uint8) # 채널을 추가함으로써 BRG로 바꿀 수 있다.
img2[200:300,100:300] = 255, 0, 0 # 영역을 지정한 곳에만 파란색으로 바뀐다.
cv2.imshow("Image", img2)
cv2.waitKey(0)

# 선 추가하기
# cv2.line(img2, (0,0),(300,300),(0,255,0),3) # (이미지, (시작점, 끝점), (색), 두께)
cv2.line(img2, (0,0),(img2.shape[1]),img2.shape[0]),(0,255,0),3) # 직선을 윈도우 전체를 가로지르게 만들고싶은 경우, 이미지의 width, height로 시작점과 끝점을 설정한다.
# shape에서는 height, width 순서로 나타나고 입력해야하는 인자는 width, height이므로 인덱스는 1, 0순서로 될 것이다.

# 사각형 추가하기 - 선 추가와 비슷하다. 사각형을 채우고 싶다면 cv2.FILLED를 추가한다.
cv2.rectangle(img, (0,0),(250,350), (0,0,255), 2, cv2.FILLED)

# 동그라미 추가하기
cv2.circle(img,(400,50),30,(255,255,0),5) # (사진, (중앙점),반지름,(색), 두께)

# 텍스트 추가하기
cv2.putText(img, " OPENCV  ", (300, 100), cv2.FONT_HERSHEY_COMPLEX, 1, (0, 150, 0), 1) # (이미지, 삽입할 텍스트, (시작점), 폰트, scale, (color), Thickness)
# 스케일은 폰트의 크기를 의미


cv2.imshow("Image", img2)
cv2.waitKey(0)
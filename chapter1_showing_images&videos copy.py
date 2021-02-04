import cv2
import numpy as np
import os
if os.getcwd() != '/home/piai/github/Learning_OpenCV':
    os.chdir('./Learning_OpenCV')


# 이미지 임포트하기
img = cv2.imread('Resources/lena.png') # 이미지 읽기. 사진의 디렉토리를 입력
# 이미지를 임포트하지만, 이것을 디스플레이해주어야 한다.

cv2.imshow('Output', img) # 이 코드만 실행하면 이미지가 보여지나, 바로 사라진다. 딜레이를 주기 위해 다음의 명령어를 입력한다.
cv2.waitKey(0) # 0는 계속 기다리는 것을 의미한다. 1은 1ms를 의미.

# 동영상 재생하기
cap = cv2.VideoCapture("Resources/test_video.mp4") # 동영상의 경로를 설정한다. 이 코드는 임포트만 할 뿐, 디스플레이작업을 해주어야 한다.

while True:
    success, img = cap.read() # 동영상을 제대로 불러왔는지 알려주는 객체, 불러온 동영상 프레임 리턴
    cv2.imshow("Video", img)

    # 위의 이미지의 경우와 마찬가지로 딜레이를 주기 위한 명령어를 추가 + 루프를 벗어나기 위한 단축키를 지정
    if cv2.waitKey(1) & 0xFF == ord('q'):
        cv2.destroyAllWindows()
        break

# 웹캠 사용하기 - 위의 동영상 예제에서 동영상의 주소입력대신, 웹캠의 ID를 입력

cap = cv2.VideoCapture(0) # 0은 디폴트 웹캠(하나있는 경우)
cap.set(3, 640) # 촬영할 영상의 파라미터를 조정해준다.
cap.set(4, 480) # 3은 Width, 4: height
cap.set(10, 150) # 10은 밝기를 조절하는 파라미터이다. 100으로 조절해보도록 한다.

while True:
    success, img = cap.read()
    cv2.imshow("Video", img)

    if cv2.waitKey(1) == ord('q'):
        cv2.destroyAllWindows()
        break
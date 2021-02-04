'''
입력받은 자동차의 색을 디텍트해보고자 한다.
1. 이미지를 HSV space로 변환한다. Hue Saturation Value
-> 색상(H), 채도(S), 명도(V)로 색을 지정하는 방법

색상, 채도, 명도 Limit을 정의하여 이미지 영역이 이 limit에 있다면 그 이미지를 잡아내도록 한다.
- 특정 색상만 두드러지는 HSV 영역이 따로 있는 듯 싶다. 따라서 내가 관심있는 색상이 두드러지는 HSV영역을 찾아내는 것!
- track bar를 활용하여 실시간으로 값을 조정하며 영역을 찾아내보도록 하자.
'''
import cv2
import numpy as np
from Learning_OpenCV import functions

def empty(temp):
    pass

path = './Learning_OpenCV/Resources/'
# 트랙바를 조정하는 TrackBar라는 이름의 새로운 위도우를 생성한다.
cv2.namedWindow("TrackBars")
cv2.resizeWindow("TrackBars",640,240) # 위에서 정의한 새로운 윈도우의 크기를 조절하고자 한다. 따라서, 윈도우의 이름은 반드시 같아야한다.
cv2.createTrackbar("Hue Min","TrackBars",0,179,empty) # first track bar를 생성 
# (조절하고자 하는 파라미터의 이름, 어느 윈도우 상에 추가될 것인지, 시작할 initial value, 최대 value, 값 변화에 따라 달라질 것 현재는 빈 함수를 넣는다. 나중에 이부분에 대해서 설명할 것)
# 색상의 최댓값은 360이지만, openCV에서는 180이다.(0~179)
cv2.createTrackbar("Hue Max","TrackBars",19,179,empty)
cv2.createTrackbar("Sat Min","TrackBars",110,255,empty)
cv2.createTrackbar("Sat Max","TrackBars",240,255,empty)
cv2.createTrackbar("Val Min","TrackBars",153,255,empty)
cv2.createTrackbar("Val Max","TrackBars",255,255,empty)

while True:
    img = cv2.imread(path + 'lambo.png')
    imgHSV = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    h_min = cv2.getTrackbarPos('Hue Min', 'TrackBars') # 이 함수를 통해서 track bar에서 변하는 값들을 읽어들일 것이다. Window이름은 정확히 일치해야한다.
    # (읽어들일 값 이름, 어느 Window에서 읽어들일 것인지)
    # 변화하는 값들을 계속해서 읽어들어야 하므로 loop문으로 코드를 작성하자.
    h_max = cv2.getTrackbarPos('Hue Max', 'TrackBars')
    s_min = cv2.getTrackbarPos('Sat Min', 'TrackBars')
    s_max = cv2.getTrackbarPos('Sat Max', 'TrackBars')
    v_min = cv2.getTrackbarPos('Val Min', 'TrackBars')
    v_max = cv2.getTrackbarPos('Val Max', 'TrackBars')
    # print(h_min, h_max, s_min, s_max, v_min, v_max)

    lower = np.array([h_min,s_min,v_min])
    upper = np.array([h_max,s_max,v_max])
    mask = cv2.inRange(imgHSV, lower, upper) # 주어진 하한, 상한의 바운더리 안에 있는 값들로 실시간으로 변하는 이미지를 확인하기 위해

    imgResult = cv2.bitwise_and(img, img, mask=mask) # 두 이미지(원본과 마스크이미지)를 합해서 하나의 이미지를 만든다.
    # bitwise_and는 픽셀이 겹치는 곳을 1로, 아닌 곳을 0으로 설정하여 새로운 이미지로 저장한다.

    cv2.imshow('img', img)
    cv2.imshow('HSV', imgHSV)
    cv2.imshow('Mask', mask)
    cv2.imshow('Image_result', imgResult)
    
    imgStack = functions.stackImages(0.6, ([img,imgHSV],[mask,imgResult]))

    key = cv2.waitKey(1)
    if key == '27':
        cv2.destroyAllWindows()
        break
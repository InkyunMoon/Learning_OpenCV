# 색상 탐지
# 색상의 위치 탐지

import numpy as np
import cv2
frameWidth = 640
frameHeight = 480

cap = cv2.VideoCapture(0)
cap.set(3, frameWidth)
cap.set(4, frameHeight)
cap.set(10, 150)

myColors = [[5, 107, 0, 19, 255, 255], # 주황, [hue min, sat min, value min, hue max, sat max, value max] 순
            [133, 56, 0, 159, 156, 255], # 보라
            [57, 76, 0, 100, 255, 255]] # 초록
# 탐지하고자 하는 색상의 리스트
# 최소, 최대 Hue & Saturation & Value를 찾아야한다.
# chapter7에서 했던 것과 같이 탐지하고자 하는 색의 최대/최소 값을 각각 찾아서 적는다.

myColorValues = [[51, 153, 255], # 탐지된 객체의 색을 리스트로 담고자 한다. BGR형태
                [255, 0, 255], # 이 색상은 바운딩박스 상단 중앙에 표시될 것이다.
                [0, 255, 0]]

myPoints = [] ## [x, y, colorId] 루프를 돌며 해당 x, y지점에 colorId에 해당하는 색상을 그린다.

def getContours(img):
    contours,hierarchy = cv2.findContours(img,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_NONE) # 모든 정보 받는다.
    x, y, w, h = 0, 0, 0, 0 # 객체가 탐지되지 않아도 무언가를 리턴해야하므로
    for cnt in contours:
        area = cv2.contourArea(cnt)
        print(area)
        if area>500:
            # cv2.drawContours(imgResult, cnt, -1, (255, 0, 0), 3)
            peri = cv2.arcLength(cnt,True)
            approx = cv2.approxPolyDP(cnt,0.02*peri,True)
            x, y, w, h = cv2.boundingRect(approx)

def findColor(img, myColors, myColorValues):
    imgHSV = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    count = 0
    newPoints = []

    for color in myColors:
        lower = np.array(color[0:3])
        upper = np.array(color[3:6])
        mask = cv2.inRange(imgHSV, lower, upper)
        # 위애서 정의한 컨투어 함수를 적용한다.
        x, y = getContours(mask)
        cv2.circle(imgResult, (x,y), 10, myColorValues[count] ,cv2.FILLED)

        if x != 0 and y!= 0:
            newPoints.append([x, y, count])
        count += 1
        # cv2.imshow(str(color[0]), mask)

        # 색상 탐지까지는 완료되었지만 탐지한 객체가 스크린의 어디에 위치하는지 파악해야한다.
        # 컨투어를 구하고, 바운딩박스를 근사한다.
    # return x+w//2, y # 탐지된 객체의 중앙 위쪽으로부터 페인팅을 할 것이므로
    return newPoints

def drawOnCanvas(myPoints, myColorValues):
    for point in myPoints:
        cv2.circle(imgResult, (point[0],point[1]), 10, myColorValues[point[2]], cv2.FILLED)

while True: # 현재는 바운딩박스의 중점을 탐지하는 코드. 더 상세하게는 강의에서 아직 다루지 않겠다고 한다.
    success, img = cap.read()
    imgResult = img.copy()
    newPoints = findColor(img, myColors, myColorValues)

    if len(newPoints) != 0:
        for newP in newPoints:
            myPoints.append(newP)

    if len(myPoints) != 0:
        drawOnCanvas(myPoints, myColorsValues)

    cv2.imshow("Result", imgResult)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        cv2.destroyAllWindows()
        break
# 210208, 2:29:02까지 진행

import numpy as np
import cv2
###############
widthImg = 640
heightImg = 480
###############
frameWidth = 640
frameHeight = 480

cap = cv2.VideoCapture(0)
cap.set(3, frameWidth)
cap.set(4, frameHeight)
cap.set(10, 150)

def preProcessing(img):
    imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    imgBlur = cv2.GaussianBlur(imgGray, (5, 5), 1)
    imgCanny = cv2.Canny(imgBlur, 200, 200) # 200, 200 값은 코드가 진행되며 바뀔 수 있다. 현재는 아무 값을 입력하고 진행해보도록 한다.
    kernel = np.ones((5,5))
    imgDial = cv2.dilate(imgCanny, kernel, iterations=2)
    imgThres = cv2.erode(imgDial, kernel, iterations=1)
    return imgThres

def getContours(img):
    contours,hierarchy = cv2.findContours(img,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_NONE) # 모든 정보 받는다.
    for cnt in contours:
        area = cv2.contourArea(cnt)
        print(area)
        if area>5000:
            cv2.drawContours(imgContour, cnt, -1, (255, 0, 0), 3)
            peri = cv2.arcLength(cnt,True)
            approx = cv2.approxPolyDP(cnt,0.02*peri,True)
            if area > maxArea and len(approx) == 4:
                biggest = approx
                maxArea = area
    return biggest

            print(len(approx)) # 코너포인트의 좌표를 출력하는데, 개수를 출력하도록 해서 코너포인트가 몇개인지 확인한다.
            # 코너포인트가 4개 초과면 원으로 파악할 수 있다. 현재 예에서는 3개(삼각형), 4개(사각형)인 경우만 처리하도록 한다.
            objCor = len(approx)
            x, y, w, h = cv2.boundingRect(approx)

while True:
    success, img = cap.read()
    cv2.resize(img, (widthImg, heightImg))
    imgContour = img.copy()
    imgThres = preProcessing(img)

    cv2.imshow('Result', imgContour)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        cv2.destroyAllWindows()
        break
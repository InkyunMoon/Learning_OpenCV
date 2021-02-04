import numpy as np
import cv2

def stackImages(scale, imgArray):
    rows = len(imgArray)
    cols = len(imgArray[0])
    rowsAvailable = isinstance(imgArray[0], list)
    width = imgArray[0][0].shape[1]
    height = imgArray[0][0].shape[0]
    if rowsAvailable:
        for x in range ( 0, rows):
            for y in range(0, cols):
                if imgArray[x][y].shape[:2] == imgArray[0][0].shape [:2]:
                    imgArray[x][y] = cv2.resize(imgArray[x][y], (0, 0), None, scale, scale)
                else:
                    imgArray[x][y] = cv2.resize(imgArray[x][y], (imgArray[0][0].shape[1], imgArray[0][0].shape[0]), None, scale, scale)
                if len(imgArray[x][y].shape) == 2: imgArray[x][y]= cv2.cvtColor( imgArray[x][y], cv2.COLOR_GRAY2BGR)
        imageBlank = np.zeros((height, width, 3), np.uint8)
        hor = [imageBlank]*rows
        hor_con = [imageBlank]*rows
        for x in range(0, rows):
            hor[x] = np.hstack(imgArray[x])
        ver = np.vstack(hor)
    else:
        for x in range(0, rows):
            if imgArray[x].shape[:2] == imgArray[0].shape[:2]:
                imgArray[x] = cv2.resize(imgArray[x], (0, 0), None, scale, scale)
            else:
                imgArray[x] = cv2.resize(imgArray[x], (imgArray[0].shape[1], imgArray[0].shape[0]), None,scale, scale)
            if len(imgArray[x].shape) == 2: imgArray[x] = cv2.cvtColor(imgArray[x], cv2.COLOR_GRAY2BGR)
        hor= np.hstack(imgArray)
        ver = hor
    return ver

def getContours(img):
    contours,hierarchy = cv2.findContours(img,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_NONE) # 모든 정보 받는다.
    # (이미지, retrieval methods, approximation)
    # (대상 이미지, 컨투어 추출 방법 - external을 많이 쓴다고 함, 모든 정보 입력받을지 아니면 압축된 정보를 받을지 여부 - 현재 예에서는 모든 정보 받기 선택)
    for cnt in contours: # 컨투어가 저장된 contours에서 각각의 컨투어정보를 얻는다.
        area = cv2.contourArea(cnt) # 첫번째로 면적을 얻는다.
        print(area)
        if area>500:# 다음으로, 컨투어를 그려보도록 한다. threshold를 두어(현 예에서는 500) 아무 컨투어나 그리지 않도록 한다.
            cv2.drawContours(imgContour, cnt, -1, (255, 0, 0), 3) # (이미지, 그려질 컨투어, 컨투어 인덱스(-1은 모든 컨투어), (컬러), 두께))
            peri = cv2.arcLength(cnt,True) # 다음으로 arc-length(호의 길이)를 그려보도록 한다. 도형의 코너를 파악하는데 힌트를 줄 것이다.
            # (그리고자 하는 컨투어, Closed 여부(True - 닫힘))
            #print(peri)
            approx = cv2.approxPolyDP(cnt,0.02*peri,True) # 코너포인트가 몇개인지 계산한다.
            # (컨투어, 결과가 안좋으면 수치를 조정해서 다시 넣어보자, 닫힘 여부)
            print(len(approx)) # 코너포인트의 좌표를 출력하는데, 개수를 출력하도록 해서 코너포인트가 몇개인지 확인한다.
            # 코너포인트가 4개 초과면 원으로 파악할 수 있다. 현재 예에서는 3개(삼각형), 4개(사각형)인 경우만 처리하도록 한다.
            objCor = len(approx)
            x, y, w, h = cv2.boundingRect(approx) # 탐지된 객체에 바운딩박스 좌표를 찾는다.
 
            if objCor ==3: objectType ="Tri"
            elif objCor == 4:
                aspRatio = w/float(h) # 정사각형은 영상비(W/H)=1 임을 활용한다.
                if aspRatio >0.98 and aspRatio <1.03: objectType= "Square"
                else:objectType="Rectangle"
            elif objCor>4: objectType= "Circles"
            else:objectType="None"

            cv2.rectangle(imgContour,(x,y),(x+w,y+h),(0,255,0),2) # 컨투어 라인위에 사각형 바운딩박스를 그린다.
            cv2.putText(imgContour,objectType, # 바운딩박스에 해당 도형이 무슨 도형인지 텍스트를 추가한다.
                        (x+(w//2)-10,y+(h//2)-10),cv2.FONT_HERSHEY_COMPLEX,0.7,
                        (0,0,0),2)
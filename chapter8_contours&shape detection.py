# 이미지의 모양을 탐지해보도록 한다.
'''
- 각 모양을 탐지해서 모양별로 구분
- 코너포인트가 몇개인지 카운트
- 각 도형의 면적 계산
'''

import cv2
import numpy as np
from Learning_OpenCV import functions
path = './Learning_OpenCV/Resources/'

img = cv2.imread(path + 'shapes.png')

# 전처리
imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
imgBlur = cv2.GaussianBlur(imgGray, (7,7),1)

# edges를 찾을 것이기 때문에 Canny Edge Detector 사용
imgCanny = cv2.Canny(imgBlur, 50, 50)
imgBlank = np.zeros_like(img)

imgStack = functions.stackImages(0.6,([img, imgGray, imgBlur],
                                    [imgCanny, imgBlank, imgBlank]))

cv2.imshow('stack', imgStack)

cv2.waitKey(0)
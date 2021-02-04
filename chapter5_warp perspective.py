# warp perspective(기하학적 변환?)
import cv2
import os
import numpy as np

path = './Learning_OpenCV/Resources/'
img = cv2.imread(path + 'cards.jpg')

width, height = 250, 350 # 카드는 보통 2.5" x 3.5"이므로 이 비율을 유지한다.

pts1 = np.float32([[111,219],[287,188],[154,482],[352,440]])
# 위 4개의 점은 주어진 이미지의 네 꼭지점
pts2 = np.float32([[0,0],[width,0],[0,height],[width,height]])
matrix = cv2.getPerspectiveTransform(pts1, pts2)
# WarpPerspective의 경우 4개의 점을 매핑한다.
imgOutput = cv2.warpPerspective(img, matrix, (width, height))

cv2.imshow("Image", img)
cv2.imshow("Output", imgOutput) # 카드만 따로 출력

cv2.waitKey(0)
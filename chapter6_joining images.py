'''
여러 이미지가 있는 경우, 모든 윈도우창을 관리하기가 어렵다.
여러 이미지를 한 윈도우에서 관리하는 방법을 알아보자.
'''
import cv2
import numpy as np

path = './Learning_OpenCV/Resources/'
img = cv2.imread(path + 'lena.png')

imgHor = np.hstack((img, img))
imgVer = np.vstack((img,img))

cv2.imshow("Horizontal", imgHor)
cv2.imshow('Vertical', imgVer)

cv2.waitKey(0)
# 단순히 join하는 경우, 원본이미지의 사이즈를 그대로 join해야한다. 즉, 사이즈를 변경할 수 없다.
# 사진의 크기를 변경하고싶다면 긴 코딩이 필요하다...

# 또한, 반드시 join하는 이미지들은 채널의 수가 같아야한다.
cv2.imshow()

#----------#----------#---------#---------#----------
# 아래의 함수를 이용하여 위 두가지 단점을 해결할 수 있다. 
# from Learning_OpenCV import functions
# functions.stackImages() 와 같이 사용
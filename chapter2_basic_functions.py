import cv2
import numpy as np
path = './Learning_OpenCV/Resources/'

# 기본 function 배우기
img = cv2.imread(path + 'lena.png')

# 1. 흑백 전환
imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) # 관례적으로 RGB를 사용하지만, OpenCV에서는 BGR을 사용한다.

cv2.imshow('Gray', imgGray)
cv2.waitKey(0)

# 2. 흐리게 만들기
imgBlur = cv2.GaussianBlur(imgGray, (7,7),0) # 커널 사이즈(항상 홀수)를 정의해야한다. (7,7)로 정의하도록 한다.

cv2.imshow('Blur', imgBlur)
cv2.waitKey(0)

# 3. 엣지 디텍터 만들기(canny edge detector)
imgCanny = cv2.Canny(img,100,100) # 임계치를 정의해야한다. 100,100으로 정의해보도록 하자.

cv2.imshow('Canny image', imgCanny)
cv2.waitKey(0)

# 4. dilation
kernel = np.ones((5,5), np.uint8) # Dilation은 커널()을 정의해야한다. 5*5사이즈의 1로만 구성된 행렬을 정의한다.

imgDilation = cv2.dilate(imgCanny, kernel, iterations = 1)# 마지막 인자 - 두께. 커널이 몇 이터레이션을 돌 것인지)
# iterations이 많아지면 더 두꺼워진다.
cv2.imshow('Dilation Image', imgDialation)
cv2.waitKey(0)

# erosion (opposite of dilation)
imgEroded = cv2.erode(imgDilation, kernel, iterations = 1)
cv2.imshow('Eroded img', imgEroded)
cv2.waitKey(0)
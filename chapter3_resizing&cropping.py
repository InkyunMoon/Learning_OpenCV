# OpenCV에서, y축으로 양의 이동은 아래쪽을 가리킨다.
# 사이즈를 조절하기 위해서, 현재 사이즈를 알아야한다.
import cv2

path = './Learning_OpenCV/Resources/'
img = cv2.imread(path + 'lambo.png')
print(img.shape) #(462, 623, 3) channel: BGR
# shape의 결과로 height comes first!

imgResize = cv2.resize(img, (300, 200)) # width, height
print(imgResize.shape)

cv2.imshow('Image', imgResize)
cv2.waitKey(0)
# if key == 27:
# cv2.destroyAllWindows()

# image cropping

imgCropped = img[0:200, 200:500] # height first. 원하는 영역을 자를 수 있다.
cv2.imshow('Image', imgCropped)
cv2.waitKey(0)
# face detection을 위해서 Viola&Jones method를 사용한다.
import cv2
path = './Learning_OpenCV/Resources/'

faceCascade = cv2.CscadeClassifier('/haarcascade_frontalface_default.xml')
faceCascade = cv2.CascadeClassifier(path + 'lena.png')

imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

faces = faceCascade.detectMultiScale(imgGray, 1.1,4) # (이미지, Scale_factor, min_neighbors)

for (x,y,w,h) in faces:
    cv2.rectangle(img, (x,y),(x+h,y+h), (255,0,0), 2) # (사진, (좌측 상단), (우측 하단), 두께)

cv2.imshow('Result', img)
cv2.waitKey(0)
import cv2

loadAlg = cv2.CascadeClassifier('haarcascades/haarcascade_frontalface_default.xml')

image = cv2.imread('C:/Users/Alexandre/Pictures/projeto_cv/a80203182bedf0af7af552741efebab6.jpg')

grayImage = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

faces = loadAlg.detectMultiScale(grayImage)

print(faces)

for(x,y,w,h) in faces:
    cv2.rectangle(image, (x,y), (x + w, y+ h), (0,255,0), 2)

cv2.imshow("Faces",image)
cv2.waitKey()
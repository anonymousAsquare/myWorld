import cv2
#faceCascade1 = cv2.CascadeClassifier('haar/haarcascade_profileface.xml')
#faceCascade1 = cv2.CascadeClassifier('haar\haarcascade_frontalface_default.xml')
faceCascade1 = cv2.CascadeClassifier('haar\haarcascade_frontalface_alt.xml')
#faceCascade1 = cv2.CascadeClassifier('haar\haarcascade_frontalface_alt2.xml')
#data = cv2.imread('Project/Desting_Fam.jpg')
#data = cv2.imread('Project\pexels-icsa-1709003.jpg')
data = cv2.imread('Project\pexels-andrea-piacquadio-903171.jpg')
dataGray = cv2.cvtColor(data, cv2.COLOR_BGR2GRAY)
faces = faceCascade1.detectMultiScale(dataGray)
i = 0
print(faces)
for face in faces:
    x,y,w,h = face
    cv2.rectangle(data,(x,y),(x+w,y+h),(0,255,0),2)
    i += 1
    print(i)
    cv2.putText(data,str(i),(x,y),cv2.FONT_HERSHEY_SIMPLEX,1,(255,255,0),2)
cv2.imshow('Asquare', data)
cv2.imwrite('df4.jpg', data)
cv2.waitKey(50000)
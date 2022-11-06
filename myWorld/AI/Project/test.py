import cv2
upperBodyCascade = cv2.CascadeClassifier('haar\haarcascade_smile.xml')
data = cv2.imread('Project\IMG20220613080607.jpg')
dataGray = cv2.cvtColor(data, cv2.COLOR_BGR2GRAY)
i = 0
people = upperBodyCascade.detectMultiScale(dataGray)
for person in people:
    x,y,w,h = person
    cv2.rectangle(data,(x,y),(x+w,y+h),(0,255,0),4)
    i += 1
    print(i)
    cv2.putText(data,str(i),(x,y),cv2.FONT_HERSHEY_SIMPLEX,4,(255,255,0),6)
    
cv2.imshow('Asq', data)
cv2.imwrite('df22.jpg', data)
cv2.waitKey(50000)
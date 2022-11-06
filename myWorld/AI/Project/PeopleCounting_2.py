import cv2
import face_recognition as FR

#data = FR.load_image_file('Project\pexels-icsa-1709003.jpg')
#data = FR.load_image_file('Project\Ajileye_Fam.jpg')
#data = FR.load_image_file('Project\pexels-andrea-piacquadio-903171.jpg')
data = FR.load_image_file('Project\data.jpg')

dataBGR = cv2.cvtColor(data, cv2.COLOR_RGB2BGR)
dataLocs = FR.face_locations(data)
i = 0
for loc in dataLocs:
    top,right,buttom,left = loc
    cv2.rectangle(dataBGR,(right,top),(left,buttom),(0,255,0),2)
    i += 1
    print(i)
    cv2.putText(dataBGR,str(i),(right,top),cv2.FONT_HERSHEY_SIMPLEX,1,(255,255,0),2)
cv2.imshow('Asquare_PEOPLE_COUNTING', dataBGR)
cv2.imwrite('df7.jpg', dataBGR)
cv2.waitKey(50000)
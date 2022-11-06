import cv2
import face_recognition as FR

AsquareImg = FR.load_image_file('PRAC/Asquare.jpg')
AsquareLoc = FR.face_locations(AsquareImg)[0]
AsquareEnc = FR.face_encodings(AsquareImg)[0]

knownImgs = [AsquareEnc]
names = ['Asquare']

UnknownImg = FR.load_image_file('PRAC/U1.jpg')
UnknownImgBGR = cv2.cvtColor(UnknownImg,cv2.COLOR_RGB2BGR)
UnknownLocs = FR.face_locations(UnknownImg)
UnknowneEncs = FR.face_encodings(UnknownImg)

for UnknownLoc,UnknowneEnc in zip(UnknownLocs,UnknowneEncs):
    top,left,buttom,right = UnknownLoc
    cv2.rectangle(UnknownImgBGR,(left,top),(right,buttom),(0,255,0),2)
    name = 'Unknown'
    compare = FR.compare_faces(knownImgs,UnknowneEnc)
    print(compare)
    if True in compare:
        compareIdx = compare.index(True)
        print(compareIdx)
        name = names[compareIdx]
        print(names)
    cv2.putText(UnknownImgBGR,name,(left,top),cv2.FONT_HERSHEY_SIMPLEX,2,(0,255,0),2)
re = cv2.resize(UnknownImgBGR,(1280,720))
cv2.imshow('Asquare faceRecognition', re)
cv2.waitKey(50000)
    

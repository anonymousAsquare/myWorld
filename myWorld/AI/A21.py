import cv2
import face_recognition as FR
import numpy as np

DonaldFace = FR.load_image_file('C:/Users/AnnonymousAsquare/Documents/myWorld/AI/demoImages-master/known/Donald Trump.jpg')
DonaldFaceLoc = FR.face_locations(DonaldFace)[0]
DonaldFaceEnc = FR.face_encodings(DonaldFace)[0]

NancyFace = FR.load_image_file('C:/Users/AnnonymousAsquare/Documents/myWorld/AI/demoImages-master/known/Nancy Pelosi.jpg')
NancyFaceLoc = FR.face_locations(NancyFace)[0]
NancyFaceEnc = FR.face_encodings(NancyFace)[0]

mikeFace = FR.load_image_file('C:/Users/AnnonymousAsquare/Documents/myWorld/AI/demoImages-master/known/Mike Pence.jpg')
mikeFaceLoc = FR.face_locations(mikeFace)[0]
mikeFaceEnc = FR.face_encodings(mikeFace)[0]

knownFaceEnc = [DonaldFaceEnc,NancyFaceEnc,mikeFaceEnc]
names = ['Donald Trump','Nancy Pelosi','Mike Pence']
print(knownFaceEnc)

unKnownFaces = FR.load_image_file('C:/Users/AnnonymousAsquare/Documents/myWorld/AI/demoImages-master/unknown/u1.jpg')
unKnownFacesBGR = cv2.cvtColor(unKnownFaces, cv2.COLOR_RGB2BGR)
unKnownFaceLocs = FR.face_locations(unKnownFaces)
unKnownFaceEncs = FR.face_encodings(unKnownFaces,unKnownFaceLocs)

for unKnownFaceLoc,unKnownFaceEnc in zip(unKnownFaceLocs,unKnownFaceEncs):
    top,left,buttom,right = unKnownFaceLoc
    cv2.rectangle(unKnownFacesBGR,(left,top),(right,buttom),(0,255,0),2)
    name = 'unkown'
    compare = FR.compare_faces(knownFaceEnc,unKnownFaceEnc)
    print(compare)
    if True in compare:
        compareIdx = compare.index(True)
        print(compareIdx)
        print(names[compareIdx])
        name = names[compareIdx]
    cv2.putText(unKnownFacesBGR,name,(left,top),cv2.FONT_HERSHEY_SIMPLEX,0.5,(0,255,0),2)
resize = cv2.resize(unKnownFacesBGR,(1280,720))
cv2.imshow('Asquare FaceRecognition',unKnownFacesBGR)
cv2.waitKey(50000)

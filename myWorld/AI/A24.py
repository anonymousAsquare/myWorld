
import cv2
import face_recognition as FR
import os
import pickle


unKnownImgs = []
path = 'C:/Users/AnnonymousAsquare/Documents/myWorld/AI/demoImages-master/unknown'
for root,folders,files in os.walk(path):
    for i in files:
        fileRoot = os.path.join(root,i)
        unKnownImgs.append(fileRoot)

if __name__ =='__main__':
    with open('A23_Encs.pkl','rb') as r:
        knownEncs = pickle.load(r)
        knownNames = pickle.load(r)

    for i in unKnownImgs:
        unKnownImg = FR.load_image_file(i)
        unKnownImgBGR = cv2.cvtColor(unKnownImg,cv2.COLOR_RGB2BGR)
        unKnownLocs =FR.face_locations(unKnownImg)
        unKnownEncs = FR.face_encodings(unKnownImg,unKnownLocs)
        for unKnownLoc,unKnownEnc in zip(unKnownLocs,unKnownEncs):
            print(unKnownLoc)
            top,left,buttom,right = unKnownLoc
            cv2.rectangle(unKnownImgBGR,(left,top),(right,buttom),(0,255,0),2)
            name = 'unknown'
            compare = FR.compare_faces(knownEncs,unKnownEnc)
            if True in compare:
                idx = compare.index(True)
                name = knownNames[idx]
            cv2.putText(unKnownImgBGR,name,(left,top),cv2.FONT_HERSHEY_SIMPLEX,1,(0,255,0),2)
        cv2.imshow('Asquare Face_Recognition', unKnownImgBGR)
        cv2.waitKey(5000)
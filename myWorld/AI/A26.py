import cv2
import face_recognition as FR
import os
import pickle

if __name__ == '__main__':
    with open('A23_Encs.pkl','rb') as h:
        knownEncs = pickle.load(h)
        knownNames = pickle.load(h)

    with open('A25_unknownEncs.pkl','rb') as r:
        unknownImgs = pickle.load(r)
        UnknownLocs = pickle.load(r)
        UnknownEncs = pickle.load(r)
    for unknownImg,UnknownLoc,UnknownEnc in zip(unknownImgs,UnknownLocs,UnknownEncs):
        unKnownIm = FR.load_image_file(unknownImg)
        unknownImBGR = cv2.cvtColor(unKnownIm,cv2.COLOR_RGB2BGR)
        print(UnknownLoc)
        for i,j in zip(UnknownLoc,UnknownEnc):
            top,left,buttom,right = i
            cv2.rectangle(unknownImBGR,(right,top),(left,buttom),(0,255,0),2)
            name = 'unknown'
            compare = FR.compare_faces(knownEncs,j)
            if True in compare:
                idx = compare.index(True)
                name = knownNames[idx]
            cv2.putText(unknownImBGR,name,(right,top),cv2.FONT_HERSHEY_SIMPLEX,1,(0,255,0),2)

        cv2.imshow('Asquare Face_Recognition', unknownImBGR)
        cv2.waitKey(5000)

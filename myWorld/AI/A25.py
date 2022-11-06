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
    unknownEncss = []
    unKnownLocss = []

    for i in unKnownImgs:
        unKnownImg = FR.load_image_file(i)
        unKnownLocs =FR.face_locations(unKnownImg)
        unKnownEncs = FR.face_encodings(unKnownImg,unKnownLocs)
        unKnownLocss.append(unKnownLocs)
        unknownEncss.append(unKnownEncs)
    with open('A25_unknownEncs.pkl','wb') as e:
        pickle.dump(unKnownImgs,e)
        pickle.dump(unKnownLocss,e)
        pickle.dump(unknownEncss,e)
    print(unknownEncss)
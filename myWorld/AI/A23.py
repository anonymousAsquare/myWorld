import cv2
import face_recognition as FR
import os
import pickle
import numpy as np

fileD = {}
path = 'C:\\Users\AnnonymousAsquare\Documents\myWorld\AI\demoImages-master\known'
for root,folders,files in os.walk(path):
    #print('root ' '{},folder ' '{},files ' '{}'.format(root,folders,files))
    for i in files:
        fileRoot = os.path.join(root,i)
        filename = os.path.splitext(i)[0]
        fileD[str(filename)] = fileRoot
if __name__ == '__main__':
    knownEncs = []
    KnownEncsNames = []
    for i in fileD:
        #print(fileD[str(i)])
        dataFile = FR.load_image_file(fileD[str(i)])
        #dataLoc = FR.face_locations(dataFile)[0]
        dataEnc = FR.face_encodings(dataFile)[0]
        knownEncs.append(dataEnc)
        KnownEncsNames.append(str(i))

    with open('A23_Encs.pkl','wb') as e:
        pickle.dump(knownEncs,e)
        pickle.dump(KnownEncsNames,e)
        
        
import cv2
import numpy as np

window_height = 720
window_width = 1280
fps = 30
cam = cv2.VideoCapture(0,cv2.CAP_DSHOW)
cam.set(cv2.CAP_PROP_FRAME_WIDTH, window_width)
cam.set(cv2.CAP_PROP_FRAME_HEIGHT, window_height)
cam.set(cv2.CAP_PROP_FPS, fps)
cam.set(cv2.CAP_PROP_FOURCC, cv2.VideoWriter_fourcc(*'MJPG'))

class HandsLM():
    import mediapipe as mp
    def __init__(self):
        self.hands = self.mp.solutions.hands.Hands(False,1,.5,.5)
    def HandData (self,frame):
        landmarks = []
        label = []
        frameRGB = cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)
        results = self.hands.process(frameRGB)
        if results.multi_hand_landmarks != None:
            for i in results.multi_handedness:
                for j in i.classification:
                    label.append(j.label)
            for handlandmarks in results.multi_hand_landmarks:
                Landmarks = []
                for landmark in handlandmarks.landmark:
                    Landmarks.append((int(window_width *landmark.x),int(window_height * landmark.y)))
                landmarks.append(Landmarks)
        return landmarks,label

def handLmDist(handData):
    palmsize = (((handData[9][0]-handData[0][0])**2)+ (handData[9][1]-handData[0][1])**2)**(1./2.)
    handDistMatx =  np.zeros([len(handData),len(handData)], dtype= 'float')
    for row in range(0,len(handData)):
        for column in range(0,len(handData)):
            handDistMatx[row][column]=((((handData[row][0]-handData[column][0])**2)+ (handData[row][1]-handData[column][1])**2)**(1./2.))/palmsize
    return handDistMatx

def errors(unknow_distance,known_distance,keypoints):
    error = 0
    for row in keypoints:
        for column in keypoints:
            error += abs(known_distance[row][column]-unknow_distance[row][column])
    print(error)
    return error

def GesturesErr(unknown_gesture, Known_gestures, keypoints, gestures_names, tol):
    gestures_Err = []
    for i in range(0,len(gestures_names)):
        gesture_Err = errors(unknown_gesture,Known_gestures[i],keypoints)
        gestures_Err.append(gesture_Err)
    min_err = gestures_Err[0]
    idx = 0
    for i in range(0,len(gestures_Err)):
        if gestures_Err[i] < min_err:
            min_err = gestures_Err[i]
            idx = i
    if min_err < tol:
        return gesture_names[idx]
    if min_err >= tol:
        return 'Unknown'

keypoints = [0,4,5,8,9,12,13,16,17,20]
Known_gestures = []
gesture_names = []
cnt = 0
tol = 15
handLm = HandsLM()
training = True
numTg = int(input('How many gestures do you want to train?' + ' '))
for i in range(0,numTg):
    c = input('Pls Enter the name of Gesture ' + str(i+1) +' ')
    gesture_names.append(c)

while True:
    ignore, frame = cam.read()
    handData,label = handLm.HandData(frame)
    if handData != []:
        if training:
            t = ('Trainig Mode: please show ' + gesture_names[cnt] + ' Gesture,And press t to train')
            #print(t)
            cv2.putText(frame,t,(50,150),cv2.FONT_HERSHEY_SIMPLEX,1,(0,0,255),3)
            if cv2.waitKey(1)& 0xff == ord('t'):
                Known_gesture = handLmDist(handData[0])
                Known_gestures.append(Known_gesture)
                cnt += 1
        if cnt == numTg:
            training = False
        
        if not training:
            unknown_gestures = handLmDist(handData[0])
            error = GesturesErr(unknown_gestures,Known_gestures,keypoints,gesture_names,tol)
            #print(error)
            cv2.putText(frame,'Testing Mode:   '+error,(100,150),cv2.FONT_HERSHEY_SIMPLEX,1,(255,0,0),3)
    
    for hand in handData:
        for ind in keypoints:
            cv2.circle(frame,hand[ind],15,(0,255,0),3)

    cv2.imshow('Asq',frame)
    cv2.moveWindow('Asq',0,0)
    if cv2.waitKey(1) & 0xff == ord('q'):
        break
cam.release()

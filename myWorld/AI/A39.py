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

def handMatX(handData):
    matHandDist = np.zeros([len(handData),len(handData)], dtype= 'float')
    for row in range(0,len(handData)):
        for column in range(0,len(handData)):
            matHandDist[row][column] = (((handData[row][0]-handData[column][0])**2)+(handData[row][1]-handData[column][1])**2)**(1./2.)
    return matHandDist

def find_errors(known_gestures,unknown_gestures,keypoints):
    error = 0
    for row in keypoints:
        for column in keypoints:
            error += abs(known_gestures[row][column]-unknown_gestures[row][column])
    return error

keypoints = [0,4,5,8,9,12,13,16,17,20]
training = True
Hand = HandsLM()
while True:
    ignore, frame = cam.read()
    Handlm, label = Hand.HandData(frame)
    if training:
        if Handlm != []:
            print('show your Gesture, press t when ready')
            if cv2.waitKey(1) & 0xff == ord('t'):
                known_gestures = handMatX(Handlm[0])
                training = False
    if not training:
        if Handlm != []:
            unknown_gesture = handMatX(Handlm[0])
            error = find_errors(known_gestures,unknown_gesture,keypoints)
            cv2.putText(frame,str(int(error)),(100,150),cv2.FONT_HERSHEY_SIMPLEX,3,(255,0,0),3)
    for hand in Handlm:
        for ind in keypoints:
            cv2.circle(frame,hand[ind],15,(0,255,0),3)
    cv2.imshow('Asq', frame)
    cv2.moveWindow('Asq',0,0)
    if cv2.waitKey(1) & 0xff == ord('q'):
        break
cam.release()
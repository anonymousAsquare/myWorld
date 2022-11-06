import cv2
import numpy as np
import pickle

window_width = 640
window_height = 480
fps = 30

cam = cv2.VideoCapture(1, cv2.CAP_DSHOW)
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

with open('AI_mp_drawing\Drawing_gestures.pkl', 'rb') as f:
    Known_gestures = pickle.load(f)
    gesture_names = pickle.load(f)

tol = 12

hand = HandsLM()
keypoints = [0,4,5,8,9,12,13,16,17,20]
color = (25,100,255)
Cpos = (200,200)
oldPos = (0,0)
drawing_window1 = np.zeros([480,640,3], dtype= 'uint8')

drwing_mode = False
selection_mode = False
erasing_mode = False
while True:
    igonre, frame = cam.read()
    frame = cv2.resize(frame,(640,480))
    frame = cv2.flip(frame,1)

    drawing_window = np.zeros([480,640,3], dtype= 'uint8')
    for j in range(0,51,1):
        for i in range(0,640,1):
            drawing_window[j,i] = (int(i/3.56),int(j*5.1),255)

    handlms, label = hand.HandData(frame)
    for handlm in handlms:
        for i in keypoints:
            cv2.circle(frame,handlm[i],8,(0,255,0),3)
        Cpos = handlm[8]

    if handlms != []:
        unknown_gestures = handLmDist(handlms[0])
        error = GesturesErr(unknown_gestures,Known_gestures,keypoints,gesture_names,tol)
        #print(error)
        cv2.putText(frame,error+' Mode',(100,150),cv2.FONT_HERSHEY_SIMPLEX,1,(255,0,0),3)

        if error == 'Selection':
            selection_mode = True
            drwing_mode = False
            erasing_mode = False
            oldPos = (0,0)
        
        elif error == 'Drawing':
            drwing_mode = True
            selection_mode = False
            erasing_mode = False
            DoldPos = (0,0)
        
        elif error == 'Erasing':
            drwing_mode = False
            selection_mode = False
            erasing_mode = True
        
        else:
            drwing_mode = False
            selection_mode = False
            erasing_mode = False
            oldPos = (0,0)
        
        if error == 'Color':
            erasing_mode = False
            drwing_mode = False
            selection_mode = False
            if Cpos[1] < 51:
                color = drawing_window[Cpos[1],Cpos[0]]
                h = int(color[0])
                s = int(color[1])
                v = 255
                color = (h,s,v) 
                print(color)

    cv2.circle(drawing_window,Cpos,7,color,-1)

    if drwing_mode:
        newPos = Cpos
        if oldPos == (0,0):
            oldPos = Cpos
        cv2.line(drawing_window1,oldPos,newPos,color,13)
        oldPos = newPos
    
    if erasing_mode:
        newPos = Cpos
        if oldPos == (0,0):
            oldPos = Cpos
        cv2.line(drawing_window1,oldPos,newPos,(0,0,0),17)
        cv2.circle(drawing_window,Cpos,17,(0,0,255),-1)
        oldPos = newPos


    dw = cv2.bitwise_or(drawing_window1,drawing_window)
    dw = cv2.cvtColor(dw, cv2.COLOR_HSV2BGR)

    cv2.imshow('d1',dw)           
    cv2.imshow('Asquare', frame)

    if cv2.waitKey(1) & 0xff == ord('q'):
        break

cam.release()

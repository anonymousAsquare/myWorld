import cv2
import mediapipe as mp
import numpy as np
import pydirectinput as pdi

evt = 0
def MOUSECLICK(event,xPos,yPos,flags,params):
        global evt
        global x1
        global y1
        global x2
        global y2
        if event == cv2.EVENT_LBUTTONDOWN:
            """print('The event is ', event)
            print('The position is ', xPos, ' ', yPos)"""
            evt = event
            x1 = xPos
            y1 = yPos
        if event == cv2.EVENT_LBUTTONUP:
            """print('The event is ', event)
            print('The position is ', xPos, ' ', yPos)"""
            evt = event
            x2 = xPos
            y2 = yPos
        if event == cv2.EVENT_RBUTTONUP:
            print('The event is ', event)
            print('The position is ', xPos, ' ', yPos)
            evt = event

window_width = 640
window_height = 480
fps = 30

cam = cv2.VideoCapture(0, cv2.CAP_DSHOW)
cam.set(cv2.CAP_PROP_FRAME_WIDTH, window_width)
cam.set(cv2.CAP_PROP_FRAME_HEIGHT, window_height)
cam.set(cv2.CAP_PROP_FPS, fps)
cam.set(cv2.CAP_PROP_FOURCC, cv2.VideoWriter_fourcc(*'MJPG'))

cv2.namedWindow('Asquare')
cv2.setMouseCallback('Asquare',MOUSECLICK)

Cpos = (50,100)
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

hand = HandsLM()
keypoints = [0,4,5,8,9,12,13,16,17,20]
color = (0,0,255)

Arr = []
while True:
    igonre, frame1 = cam.read()
    frame = cv2.resize(frame1,(640,480))

    handlms, label = hand.HandData(frame)
    for handlm in handlms:
        for i in keypoints:
            cv2.circle(frame,handlm[i],8,(0,255,0),3)
        Cpos = handlm[8]

    """drawing_window = frame1
    drawing_window[:,:] = (0,0,0)"""
    drawing_window = np.zeros([480,640,3], dtype= 'uint8')
    for j in range(0,51,1):
        for i in range(0,640,1):
            drawing_window[j,i] = (int(i/3.56),int(j*5.1),255)

    if evt ==1:
        if y1 < 50:
            color = drawing_window[y1,x1]
            h = int(color[0]/1.42)
            s = int(color[1])
            v = 255
            color = (h,s,v)
            print(color)
        Arr.append(Cpos)
    
    #cv2.rectangle(drawing_window,(50,100),(100,150),color,-1)
    cv2.circle(drawing_window,Cpos,5,color,-1)

    if Arr:
        for i in Arr:
            dy = i[1]
            dx = i[0]
            drawing_window[dy:dy+4,dx:dx+4] = color
    
    drawing_window = cv2.cvtColor(drawing_window, cv2.COLOR_HSV2BGR)
    
    cv2.imshow('Asquare', frame)
    cv2.moveWindow('Asquare', 0,0)

    cv2.imshow('Drawing_window', drawing_window)
    cv2.moveWindow('Drawing_window', window_width,0)
    
    if cv2.waitKey(1) & 0xff == ord('q'):
        break

cam.release()

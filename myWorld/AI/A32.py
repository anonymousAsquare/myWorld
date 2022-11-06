import cv2

window_height = 720
window_width = 1280
fps = 30
cam = cv2.VideoCapture(0,cv2.CAP_DSHOW)
cam.set(cv2.CAP_PROP_FRAME_WIDTH, window_width)
cam.set(cv2.CAP_PROP_FRAME_HEIGHT, window_height)
cam.set(cv2.CAP_PROP_FPS, fps)
cam.set(cv2.CAP_PROP_FOURCC, cv2.VideoWriter_fourcc(*'MJPG'))

class Hands():
    import mediapipe as mp
    def __init__(self):
        self.hands = self.mp.solutions.hands.Hands(False,2,.5,.5)
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


cirX = int(window_width/2)
cirY = int(window_height/2)
cirIncY = 10
cirIncX = 10
cirR = 15
hands = Hands()
p = 100
q = 100
rect_w = int(window_width * 0.015)
rect_h = int(window_height * 0.2)
rec1X1 = 0
rec1Y1 = 0
rec1X2 = rec1X1 + rect_w
rec1Y2 = rec1Y1 + rect_h
rec2X1 = window_width
rec2Y1 = 0
rec2X2 = window_width - rect_w
rec2Y2 = rec1Y1 + rect_h
rec1Y = 0
rec2Y = 0
while True:
    ignore, frame = cam.read()
    frame = cv2.resize(frame,(window_width,window_height))
    landmarks,labels = hands.HandData(frame)
    for landmark,label in zip(landmarks,labels):
        if label == 'Left':
            cv2.circle(frame,landmark[12],15,(0,255,0),2)
            rec1Y = landmark[12][1]
            cv2.putText(frame,'Player1(Active)',(int(window_width/2),14),cv2.FONT_HERSHEY_COMPLEX_SMALL,1,(0,255,0),2)
        if label == 'Right':
            cv2.circle(frame,landmark[12],15,(255,0,0),2)
            cv2.putText(frame,'player2(Active)',(int(window_width/2),window_height-10),cv2.FONT_HERSHEY_COMPLEX_SMALL,1,(255,0,0),2)
            rec2Y = landmark[12][1]
    rec1Y1 = rec1Y - int(rect_h/2)
    rec1Y2 = rec1Y + int(rect_h/2)
    rec2Y1 = rec2Y - int(rect_h/2)
    rec2Y2 = rec2Y + int(rect_h/2)
    if rec1Y1 <= 0:
        rec1Y1 = 0
        rec1Y2 = rect_h
    if rec1Y2 >= window_height - int(rect_h/2):
        rec1Y1 = window_height - rect_h
        rec1Y2 = window_height
    if rec2Y1 <= 0:
        rec2Y1 = 0
        rec2Y2 = rect_h
    if rec2Y2 >= window_height - int(rect_h/2):
        rec2Y1 = window_height - rect_h
        rec2Y2 = window_height

    if cirY - cirR <= 0 or cirY + cirR >= window_height:
        cirIncY *= (-1)
    if cirX - cirR <= rec1X2:
        if cirY + cirR >= rec1Y1 and cirY - cirR <= rec1Y2:
            cirIncX *= (-1)
        else: 
            cirX = int(window_width/2)
            cirIncX *= (-1)
    if cirX + cirR >= rec2X2:
        if cirY + cirR >= rec2Y1 and cirY - cirR <= rec2Y2:
            cirIncX *= (-1)
        else:
            cirX = int(window_width/2)
            cirIncX *= (-1)
    cirX += cirIncX
    cirY += cirIncY
    cv2.rectangle(frame,(rec1X1,rec1Y1),(rec1X2, rec1Y2),(0,255,0),-1)
    cv2.rectangle(frame,(rec2X1,rec2Y1),(rec2X2, rec2Y2),(255,0,0),-1)
    cv2.circle(frame,(cirX,cirY),cirR,(0,0,255),-1)
    cv2.imshow('asq', frame)
    cv2.moveWindow('asq', 0,0)
    if cv2.waitKey(1) & 0xff == ord('q'):
        break
cam.release()

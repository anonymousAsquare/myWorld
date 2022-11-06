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
rect_w =int(window_width * 0.2)
rect_h = int(window_height * 0.05)
rec1X = 0
rec1Y = 0
rec2X = 0
rec2Y = window_height - rect_h

cirX = int(window_width/2)
cirY = int(window_height/2)
cirIncY = 10
cirIncX = 10
cirR = 15
hands = Hands()
p = 100
q = 100
while True:
    ignore, frame = cam.read()
    frame = cv2.resize(frame,(window_width,window_height))
    landmarks,labels = hands.HandData(frame)
    for landmark,label in zip(landmarks,labels):
        if label == 'Left':
            cv2.circle(frame,landmark[12],15,(0,255,0),2)
            rec1X = landmark[12][0]
        if label == 'Right':
            cv2.circle(frame,landmark[12],15,(255,0,0),2)
            rec2X = landmark[12][0]
    rec1X1 = rec1X - int(rect_w/2)
    rec1X2 = rec1X + int(rect_w/2)
    rec2X1 = rec2X - int(rect_w/2)
    rec2X2 = rec2X + int(rect_w/2)
    if rec1X1 <= 0:
        rec1X1 = 0
        rec1X2 = rect_w
    if rec1X2 >= window_width - int(rect_w/2):
        rec1X1 = window_width - rect_w
        rec1X2 = window_width
    if rec2X1 <= 0:
        rec2X1 = 0
        rec2X2 = rect_w
    if rec2X2 >= window_width - int(rect_w/2):
        rec2X1 = window_width - rect_w
        rec2X2 = window_width

    if cirX - cirR <= 0 or cirX + cirR >= window_width:
        cirIncX *= (-1)
    if cirY - cirR <= rec1Y + rect_h:
        if cirX + cirR >= rec1X1 and cirX - cirR <= rec1X2:
            cirIncY *= (-1)
        else: 
            cirY = int(window_height/2)
            cirIncY *= (-1)
    if cirY + cirR >= rec2Y:
        if cirX + cirR >= rec2X1 and cirX - cirR <= rec2X2:
            cirIncY *= (-1)
        else:
            cirY = int(window_height/2)
            cirIncY *= (-1)
    cirX += cirIncX
    cirY += cirIncY
    cv2.rectangle(frame,(rec1X1,rec1Y),(rec1X2, rec1Y + rect_h),(0,255,0),-1)
    cv2.rectangle(frame,(rec2X1,rec2Y),(rec2X2, rec2Y + rect_h),(255,0,0),-1)
    cv2.circle(frame,(cirX,cirY),cirR,(0,0,255),-1)
    cv2.imshow('asq', frame)
    cv2.moveWindow('asq', 0,0)
    if cv2.waitKey(1) & 0xff == ord('q'):
        break
cam.release()

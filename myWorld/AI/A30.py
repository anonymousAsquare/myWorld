import cv2
from sys import exit
import time
window_width = 1280
window_height = 720
fps = 30
cam = cv2.VideoCapture(0, cv2.CAP_DSHOW)
cam.set(cv2.CAP_PROP_FRAME_WIDTH, window_width)
cam.set(cv2.CAP_PROP_FRAME_HEIGHT, window_height)
cam.set(cv2.CAP_PROP_FPS, fps)
cam.set(cv2.CAP_PROP_FOURCC, cv2.VideoWriter_fourcc(*'MJPG'))
class Hands():
    import mediapipe as mp
    def __init__(self,framew,frameh):
        self.framew = framew
        self.frameh = frameh
        self.mpHands = self.mp.solutions.hands.Hands(False,1,.5,.5)
        self.mpDraw = self.mp.solutions.drawing_utils
        self.cirR = 14
        self.cirX = int(self.framew/2) - self.cirR
        self.cirY = int(self.frameh/2) - self.cirR
        self.cirXInc = -10
        self.cirYInc = -10
        self.score = 0
        self.ballstate = False
    def hands(self,frame):
        self.Handlandmarks = []
        frameRGB = cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)
        results = self.mpHands.process(frameRGB)
        if results.multi_hand_landmarks != None:
            for handlandMarks in results.multi_hand_landmarks:
                handlandmarks = []
                for landmarks in handlandMarks.landmark:
                    handlandmarks.append((int(landmarks.x*window_width),int(landmarks.y*window_height)))
                self.Handlandmarks.append(handlandmarks)
        return self.Handlandmarks
    def ball(self,frame):
        rectWid = int(self.framew*0.2)
        rectHit = int(self.frameh*0.05)

        self.cirX += self.cirXInc
        self.cirY += self.cirYInc
        if self.cirX - self.cirR <= 0 or self.cirX + self.cirR >= self.framew:
            self.cirXInc *= -1
        if self.cirY + self.cirR >= self.frameh:
            self.cirYInc *= -1
        for landmarks in self.Handlandmarks:
            x,y = landmarks[8]
            cv2.rectangle(frame,(x,0),(x+rectWid,rectHit),(0,255,0),-1)
            for i in range(x,x+rectWid):
                if self.cirY > rectHit:
                    if self.cirX - self.cirR == i and self.cirY - self.cirR <= rectHit:
                        self.ballstate = not self.ballstate
                        print(self.ballstate)
                if self.ballstate:
                    break
        if self.ballstate:
            print(self.ballstate)
            self.cirYInc *= -1
            self.score += 1
        t = 'score: '
        cv2.putText(frame,t + str(self.score),(20,30),cv2.FONT_HERSHEY_DUPLEX,(1),(255,0,0),2)

        if self.cirY - self.cirR <= 0:
            self.cirY = int(self.frameh/2) - self.cirR
            self.score -= 1
            #cv2.putText(frame,'GAME OVER',(int(self.framew/2),int(self.frameh/2)),cv2.FONT_HERSHEY_SIMPLEX,2,(0,0,255),2)
            #u = 'Your score is '
            #cv2.putText(frame,u + str(self.score),(int(self.framew/2),int(self.frameh/2 + 30)),cv2.FONT_HERSHEY_COMPLEX_SMALL,1,(0,0,255),1)


        cv2.circle(frame,(self.cirX,self.cirY),self.cirR,(0,255,255),-1)
        self.ballstate = False
        

hands = Hands(window_width,window_height)


while True:
    ignore, frame = cam.read()
    handlandmarks = hands.hands(frame)
    hands.ball(frame)
    cv2.imshow('Asquare', frame)
    cv2.moveWindow('Asquare',0,0)
    if cv2.waitKey(1) & 0xff == ord('q'):
        exit()
cam.release()
cv2.destroyAllWindows()


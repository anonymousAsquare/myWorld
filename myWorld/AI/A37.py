import cv2
from sys import exit
camera = 0
window_width = 640
window_height = 360
fps = 30
cam = cv2.VideoCapture(camera, cv2.CAP_DSHOW)
cam.set(cv2.CAP_PROP_FRAME_WIDTH, window_width)
cam.set(cv2.CAP_PROP_FRAME_HEIGHT, window_height)
cam.set(cv2.CAP_PROP_FPS, fps)
cam.set(cv2.CAP_PROP_FOURCC, cv2.VideoWriter_fourcc(*'MJPG'))
class Hands():
    import mediapipe as mp
    import cv2
    def __init__(self,static = False, numHands = 1, ac = .5, acc = .5):
        self.hands = self.mp.solutions.hands.Hands(static,numHands,ac,acc)
        self.drawHands = self.mp.solutions.drawing_utils
    def HandPos(self,frame):
        Handlandmarks = []
        frameRGB = self.cv2.cvtColor(frame, self.cv2.COLOR_BGR2RGB)
        results = self.hands.process(frameRGB)
        if results.multi_hand_landmarks != None:
            for handLandmark in results.multi_hand_landmarks:
                self.drawHands.draw_landmarks(frame,handLandmark,self.mp.solutions.hands.HAND_CONNECTIONS)
                handlandmarks = []
                for landmarks in handLandmark.landmark:
                    handlandmarks.append((int(window_width * landmarks.x),int(window_height*landmarks.y)))
                Handlandmarks.append(handlandmarks)
        return Handlandmarks

class objects():
    def __init__(self,frame,pos) -> None:
        self.frame = frame
        self.pos = pos
    def ok(self):
        dis = int(((((self.pos[8][0]-self.pos[4][0])**2)+ ((self.pos[8][1]-self.pos[4][1])**2))**1/2)/window_height)
        disA = int(((((self.pos[12][0]-self.pos[9][0])**2)+ ((self.pos[12][1]-self.pos[9][1])**2))**1/2)/window_height)
        disB = int(((((self.pos[16][0]-self.pos[13][0])**2)+ ((self.pos[16][1]-self.pos[13][1])**2))**1/2)/window_height)
        disC = int(((((self.pos[20][0]-self.pos[17][0])**2)+ ((self.pos[20][1]-self.pos[17][1])**2))**1/2)/window_height)
        print(dis,disA,disB,disC)
        if dis < 5 and disA > 21 and disB > 14 and disC > 8:
            cv2.putText(self.frame,'# OK',(100,100),cv2.FONT_HERSHEY_SIMPLEX,2,(0,255,0),3)
        #cv2.circle(frame,data,10,(0,255,0),2)
    def one(self):
        dis = (((self.pos[8][0]-self.pos[5][0])**2)+ ((self.pos[8][1]-self.pos[5][1])**2))**1/2
        disA = (((self.pos[12][0]-self.pos[9][0])**2)+ ((self.pos[12][1]-self.pos[9][1])**2))**1/2
        disB = (((self.pos[16][0]-self.pos[13][0])**2)+ ((self.pos[16][1]-self.pos[13][1])**2))**1/2
        disC = (((self.pos[20][0]-self.pos[17][0])**2)+ ((self.pos[20][1]-self.pos[17][1])**2))**1/2
        disD = (((self.pos[11][0]-self.pos[3][0])**2)+ ((self.pos[11][1]-self.pos[3][1])**2))**1/2
        #print(dis,disA,disB,disC,disD)
        if dis > 1000 and disA < 500 and disB < 500 and disC < 500 and disD < 3000:
            cv2.putText(self.frame,'# One',(100,100),cv2.FONT_HERSHEY_SIMPLEX,2,(0,255,255),3)


hands = Hands()
while True:
    ignore, frame = cam.read()
    handData = hands.HandPos(frame)
    for pos in handData:
        obj = objects(frame,pos)
        obj.ok()
        obj.one()
    cv2.imshow('Asquare MediaPipe', frame)
    cv2.moveWindow('Asquare MediaPipe', 0,0)
    if cv2.waitKey(1) & 0xff == ord('q'):
        exit()
cam.release()

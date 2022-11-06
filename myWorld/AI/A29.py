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
    def __init__(self,static = False, numHands = 2, ac = .5, acc = .5):
        self.hands = self.mp.solutions.hands.Hands(static,numHands,ac,acc)
        self.drawHands = self.mp.solutions.drawing_utils
    def HandPos(self,frame):
        Handlandmarks = []
        frameRGB = self.cv2.cvtColor(frame, self.cv2.COLOR_BGR2RGB)
        results = self.hands.process(frameRGB)
        if results.multi_hand_landmarks != None:
            for handLandmark in results.multi_hand_landmarks:
                handlandmarks = []
                for landmarks in handLandmark.landmark:
                    handlandmarks.append((int(window_width * landmarks.x),int(window_height*landmarks.y)))
                Handlandmarks.append(handlandmarks)
        return Handlandmarks
hands = Hands()
data = (0,0)
while True:
    ignore, frame = cam.read()
    handData = hands.HandPos(frame)
    for pos in handData:
        data = pos[20]
        cv2.circle(frame,data,10,(0,255,0),2)
    cv2.imshow('Asquare MediaPipe', frame)
    x,y = data
    cv2.moveWindow('Asquare MediaPipe', 0,0)
    if cv2.waitKey(1) & 0xff == ord('q'):
        exit()
cam.release()

import cv2
window_height = 720
window_width = 1280
fps = 30
cam = cv2.VideoCapture(0,cv2.CAP_DSHOW)
cam.set(cv2.CAP_PROP_FRAME_WIDTH, window_width)
cam.set(cv2.CAP_PROP_FRAME_HEIGHT, window_height)
cam.set(cv2.CAP_PROP_FPS, fps)
cam.set(cv2.CAP_PROP_FOURCC, cv2.VideoWriter_fourcc(*'MJPG'))
class pose():
    import mediapipe as mp
    import cv2
    def __init__(self):
        self.pose = self.mp.solutions.pose.Pose(False,False,True,.5,.5)
        self.draw = self.mp.solutions.drawing_utils
    
    def data(self, frame):
        frameRGB = self.cv2.cvtColor(frame,self.cv2.COLOR_BGR2RGB)
        results = self.pose.process(frameRGB)
        landmarks = []
        act = False
        if results.pose_landmarks != None:
            act = not act
            self.draw.draw_landmarks(frame, results.pose_landmarks , self.mp.solutions.pose.POSE_CONNECTIONS)
            for landmark in results.pose_landmarks.landmark:
                landmarks.append((int(window_width * landmark.x),int(window_height *landmark.y)))
        return landmarks, act

class Face_detection():
    import mediapipe as mp
    def __init__(self):
        self.face = self.mp.solutions.face_detection.FaceDetection()
        self.draw = self.mp.solutions.drawing_utils
    def faceD (self,frame):
        Faces= []
        frameRGB = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        results = self.face.process(frameRGB)
        if (results.detections != None):
            face = []
            for faces in results.detections: 
                i = (faces.location_data.relative_bounding_box)
                face.append((int(i.xmin*window_width),int(i.ymin*window_height),int(i.width*window_width),int(i.height*window_height)))
            Faces.append(face)
        return Faces
    
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
                self.drawHands.draw_landmarks(frame, handLandmark,self.mp.solutions.hands.HAND_CONNECTIONS)
                handlandmarks = []
                for landmarks in handLandmark.landmark:
                    handlandmarks.append((int(window_width * landmarks.x),int(window_height*landmarks.y)))
                Handlandmarks.append(handlandmarks)
        return Handlandmarks

hands = Hands()
face = Face_detection()
Pose = pose()
while True:
    ignore, frame = cam.read()
    landmark = Pose.data(frame)
    if landmark[1]:
        for i in landmark[0]:
            cv2.circle(frame,i,5,(0,255,0),-1)
        """cv2.circle(frame,landmark[0][10],5,(0,255,0),-1)
        cv2.circle(frame,landmark[0][9],5,(0,255,0),-1)"""
    faces = face.faceD(frame)
    for i in faces:
        for j in i:
            x,y,w,h = j
            cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),2)
    handData = hands.HandPos(frame)
    for pos in handData:
        data = pos[20]
        cv2.circle(frame,data,10,(0,255,0),2)
    cv2.imshow('Asq', frame)
    if cv2.waitKey(1) & 0xff == ord('q'):
        break
cam.release()

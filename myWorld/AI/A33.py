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
Pose = pose()
while True:
    ignore, frame = cam.read()
    landmark = Pose.data(frame)
    if landmark[1]:
        for i in landmark[0]:
            cv2.circle(frame,i,5,(0,255,0),-1)
        """cv2.circle(frame,landmark[0][10],5,(0,255,0),-1)
        cv2.circle(frame,landmark[0][9],5,(0,255,0),-1)"""
    cv2.imshow('Asq', frame)
    if cv2.waitKey(1) & 0xff == ord('q'):
        break
cam.release()

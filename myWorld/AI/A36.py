import cv2

window_width = 1280
window_height = 720
fps = 30

cam = cv2.VideoCapture(0,cv2.CAP_DSHOW)
cam.set(cv2.CAP_PROP_FRAME_WIDTH, window_width)
cam.set(cv2.CAP_PROP_FRAME_HEIGHT, window_height)
cam.set(cv2.CAP_PROP_FPS, fps)
cam.set(cv2.CAP_PROP_FOURCC, cv2.VideoWriter_fourcc(*'MJPG'))

class facelm():
    import mediapipe as mp
    def __init__(self):
        self.face = self.mp.solutions.face_mesh.FaceMesh(False,1,.5,.5)
        self.draw_face = self.mp.solutions.drawing_utils
        self.drawSpecC = self.draw_face.DrawingSpec(thickness = 0,circle_radius =0, color = (255,0,0))
        self.drawSpecL = self.draw_face.DrawingSpec(thickness = 3,circle_radius =2, color = (0,0,255))

    def landmarks(self,frame):
        landmarks = []
        frameRGB = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        results = self.face.process(frameRGB)
        if (results.multi_face_landmarks) != None:
            for lms in results.multi_face_landmarks:
                self.draw_face.draw_landmarks(frame,lms,self.mp.solutions.face_mesh.FACE_CONNECTIONS, self.drawSpecC,self.drawSpecL)
                landmark = []
                for lm in lms.landmark:
                    landmark.append((int(window_width*lm.x),int(window_height*lm.x)))
                landmarks.append(landmark)
        return landmarks

                    

facelandm = facelm()
while True:
    ignore, frame = cam.read()
    frame = cv2.resize(frame, (window_width,window_height))
    facelandm.landmarks(frame)
    cv2.imshow('Asquare computer vision', frame)
    cv2.moveWindow('Asquare computer vision', 0,0)
    if cv2.waitKey(1) & 0xff == ord('q'):
        break
cv2.destroyAllWindows()
cam.release()
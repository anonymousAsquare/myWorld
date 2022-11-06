import cv2

window_width = 640
window_height = 360
fps = 60
cam = cv2.VideoCapture(0, cv2.CAP_DSHOW)
cam.set(cv2.CAP_PROP_FRAME_WIDTH, window_width)
cam.set(cv2.CAP_PROP_FRAME_HEIGHT, window_height)
cam.set(cv2.CAP_PROP_FPS, fps)
cam.set(cv2.CAP_PROP_FOURCC, cv2.VideoWriter_fourcc(*'MJPG'))

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

face = Face_detection()
while True:
    ignore, frame = cam.read()
    frame = cv2.resize(frame,(640,360))
    faces = face.faceD(frame)
    for i in faces:
        for j in i:
            x,y,w,h = j
            print(i)
            cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),2)
    cv2.imshow('Asq', frame)
    cv2.moveWindow('Asq', 0,0)
    if cv2.waitKey(1) & 0xff == ord('q'):
        break
cam.release()
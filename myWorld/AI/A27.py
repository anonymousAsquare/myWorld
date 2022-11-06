import mediapipe as mp
import cv2
import face_recognition as FR

w = 640
h = 360
fps = 30
cam = cv2.VideoCapture(0, cv2.CAP_DSHOW)
cam.set(cv2.CAP_PROP_FRAME_WIDTH, w)
cam.set(cv2.CAP_PROP_FRAME_HEIGHT, h)
cam.set(cv2.CAP_PROP_FPS, fps)
cam.set(cv2.CAP_PROP_FOURCC, cv2.VideoWriter_fourcc(*'MJPG'))

hands = mp.solutions.hands.Hands(False,2,.5,.5)
handDarw = mp.solutions.drawing_utils
while True:
    ignore, frame = cam.read()
    frameRGB = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    results = hands.process(frameRGB)
    if results.multi_hand_landmarks != None:
        for handLandmarks in results.multi_hand_landmarks:
            landmarks = []
            handDarw.draw_landmarks(frame, handLandmarks,mp.solutions.hands.HAND_CONNECTIONS)
            for landMark in handLandmarks.landmark:
                landmarks.append((int(landMark.x*w),int(landMark.y*h)))
            print(landmarks[0])
            print(' ')
    cv2.imshow('Asquare', frame)
    cv2.moveWindow('Asquare', 0,0)
    if cv2.waitKey(1) & 0xff == ord('q'):
        break
cam.release()
cv2.destroyAllWindows
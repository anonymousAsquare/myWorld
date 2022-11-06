import mediapipe as mp
import cv2

w = 640
h = 360
fps = 30
cam = cv2.VideoCapture(0, cv2.CAP_DSHOW)
cam.set(cv2.CAP_PROP_FRAME_WIDTH, w)
cam.set(cv2.CAP_PROP_FRAME_HEIGHT, h)
cam.set(cv2.CAP_PROP_FPS, fps)
cam.set(cv2.CAP_PROP_FOURCC, cv2.VideoWriter_fourcc(*'MJPG'))

mpHands = mp.solutions.hands.Hands(False,2,.5,.5)
mpDraw = mp.solutions.drawing_utils

def hands(frame):
    landmarks = []
    frameRGB = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    results = mpHands.process(frameRGB)
    if results.multi_hand_landmarks != None:
        for handlandmarks in results.multi_hand_landmarks:
            landmark = []
            mpDraw.draw_landmarks(frame,handlandmarks)
            for handlandmark in handlandmarks.landmark:
                landmark.append((int(w*handlandmark.x),int(h*handlandmark.y)))
            landmarks.append(landmark)
            #return landmark
    return landmarks



while True:
    ignore, frame = cam.read()
    hand = hands(frame)
    cv2.imshow('asq', frame)
    if cv2.waitKey(1) & 0xff == ord('q'):
        break
cam.release()
    

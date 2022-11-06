import cv2
window_height = 720
window_width = 1280

class HandsLM():
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
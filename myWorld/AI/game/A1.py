import pygame
from pygame.locals import *
from sys import exit
import os

os.environ['SDL_VIDEO_WINDOW_POS'] = "%d,%d" % (0,30)
pygame.init()
backgroungImg = 'game/background.png'
mouseImg = 'game/player.png'
screen = pygame.display.set_mode((800,600),0,32)
pygame.display.set_caption('Hello World')

background = pygame.image.load(backgroungImg).convert()
mouse_cusur = pygame.image.load(mouseImg).convert_alpha()

import cv2
camera = 0
window_width = 1366
window_height = 736
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
                self.drawHands.draw_landmarks(frame,handLandmark)
                handlandmarks = []
                for landmarks in handLandmark.landmark:
                    handlandmarks.append((int(window_width * landmarks.x),int(window_height*landmarks.y)))
                Handlandmarks.append(handlandmarks)
        return Handlandmarks
hands = Hands()
data = (0,0)


while True:
    ignore, frame = cam.read()
    #frame = cv2.resize(frame,(800,600))
    handData = hands.HandPos(frame)
    for pos in handData:
        data = pos[4]
        cv2.circle(frame,data,10,(0,255,0),2)
    #cv2.imshow('Asquare MediaPipe', frame)
    x,y = data
    #cv2.moveWindow('Asquare MediaPipe', 800,0)

    for event in pygame.event.get():
        if event.type == QUIT:
            exit()
    
    screen.blit(background,(0,0))
    x -= mouse_cusur.get_width()/2
    y -= mouse_cusur.get_height()/2
    print(x,y)
    screen.blit(mouse_cusur,(x,y))
    pygame.display.update()

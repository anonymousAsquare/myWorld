import pygame
from pygame.locals import *
from sys import exit
import cv2

window_size = (800,600)
pygame.init()
screen = pygame.display.set_mode(window_size,0,32)
background = pygame.image.load('game\Game_1\BackGround.png')
pygame.display.set_caption('Asquare Games(Pong Arcade Game)')
Arrow = pygame.image.load('game\Game_1\Arr2.png')
flo = pygame.image.load('game/Game_1/foll.png')
logo = pygame.image.load('game\Game_1\LOGO (2).jpg')
lEdge = pygame.image.load('game\Game_1\Edg.png')
bEdg = pygame.image.load('game/Game_1/bEdg.png')
ball = pygame.image.load('game\Game_1\Ball.png')
pygame.display.set_icon(logo)
score = 0
font = pygame.font.SysFont('arial', 15)
scoreS = font.render('Score: '+str(score),True,(0,0,0))

class AI_hands():
    import mediapipe as mp
    import cv2
    def __init__(self,width,height):
        self.width = width
        self.height = height
        self.cam = self.cv2.VideoCapture(0, self.cv2.CAP_DSHOW)
        self.cam.set(self.cv2.CAP_PROP_FRAME_WIDTH,self.width)
        self.cam.set(self.cv2.CAP_PROP_FRAME_HEIGHT,self.height)
        self.cam.set(self.cv2.CAP_PROP_FPS, 30)
        self.cam.set(self.cv2.CAP_PROP_FOURCC, self.cv2.VideoWriter_fourcc(*'MJPG'))
        self.hand = self.mp.solutions.hands.Hands(False,1,.5,.5)

    def hands(self, frame):
        frameRGB = self.cv2.cvtColor(frame, self.cv2.COLOR_BGR2RGB)
        hands = []
        results = self.hand.process(frameRGB)
        if results.multi_hand_landmarks != None:
            for handLandmarks in results.multi_hand_landmarks:
                hand = []
                for landmarks in handLandmarks.landmark:
                    hand.append((int(self.width*landmarks.x),int(self.height*landmarks.y)))
                hands.append(hand)
        return hands

hand = AI_hands(window_size[0],window_size[1])
x =0
ball_x,ball_y = window_size[0]/2,window_size[1]/2
ballIncX, ballIncY = 350, 350
fullscreen = False
clock = pygame.time.Clock()

def paddle(x):
    screen.blit(flo,(x,Arrow.get_height()))
keypoints = [0,4,5,8,9,12,13,16,17,20]

while True:
    ignore, frame = hand.cam.read()
    for event in pygame.event.get():
        if event.type == QUIT:
            exit()
        if event.type == KEYDOWN:
            if event.key == K_q:
                exit()
            if event.key == K_f:
                fullscreen = not fullscreen
                if fullscreen:
                    screen = pygame.display.set_mode(window_size,FULLSCREEN,32)
                else:
                    screen = pygame.display.set_mode(window_size,0,32)

    screen.fill((0,0,0))
    screen.blit(background,(0,0))

    pos = hand.hands(frame)
  
    for position in pos:
        x,y = position[12]

    if x <= lEdge.get_width():
        x = lEdge.get_width()
    if x + flo.get_width() >= window_size[0] - lEdge.get_width():
        x = window_size[0] - flo.get_width() - lEdge.get_width()

    paddle(x)
    screen.blit(lEdge,(0,0))
    screen.blit(lEdge,(window_size[0]-lEdge.get_width(),0))
    screen.blit(bEdg,(0,window_size[1]-bEdg.get_height()))
    screen.blit(Arrow,(0,0))
    screen.blit(scoreS,(lEdge.get_width(),0))
    screen.blit(ball,(ball_x,ball_y))

    time_passed = clock.tick(30)
    time_passed_seconds = time_passed/1000.

    ball_distanceX = time_passed_seconds * ballIncX
    ball_distanceY = time_passed_seconds * ballIncY

    ball_x += ball_distanceX
    ball_y += ball_distanceY

    if ball_x <= lEdge.get_width():
        ball_x = lEdge.get_width()
        ballIncX  *= (-1)
        screen.fill((0,0,255), Rect(ball_x-lEdge.get_width(),ball_y,lEdge.get_width(),ball.get_height()))
    if ball_x + ball.get_width() >= window_size[0] - lEdge.get_width():
        ball_x = window_size[0] - ball.get_width() - lEdge.get_width()
        ballIncX  *= (-1)
        screen.fill((0,0,255), Rect(ball_x+ball.get_width(),ball_y,lEdge.get_width(),ball.get_height()))
    if ball_y < Arrow.get_height() + flo.get_height()/2:
        screen.fill((255,0,0),Rect(0,0,Arrow.get_width(),Arrow.get_height()))
        ball_y = window_size[1]/2
        ballIncY  *= (-1)
    if ball_y + ball.get_height()>= window_size[1] - bEdg.get_height():
        ball_y = window_size[1] - bEdg.get_height() - ball.get_height()
        ballIncY  *= (-1)
        screen.fill((0,0,255), Rect(0,window_size[1]-bEdg.get_height(),800,bEdg.get_height()))
    if ball_y <= Arrow.get_height()+flo.get_height():
        if ball_x + ball.get_width()/2  > x and ball_x + ball.get_width()/2< x + flo.get_width():
            ball_y = Arrow.get_height() + flo.get_height()
            ballIncY  *= (-1)
            score += 1
            screen.fill((0,255,0),Rect(0,Arrow.get_height(),window_size[0],window_size[1]-Arrow.get_height()))
            scoreS = font.render('Score: '+str(score),True,(0,0,0))

    pygame.display.update()
    frameR = cv2.resize(frame,(320,180))
    for position in pos:
        for i in keypoints:
            x = int(position[i][0]/window_size[0]*320)
            y = int(position[i][1]/window_size[1]*180)
            cv2.circle(frameR,(x,y),5,(0,255,0),2)
    
    cv2.imshow('Asquare', frameR)
    cv2.moveWindow('Asquare', 0,0)
    if cv2.waitKey(1) & 0xff == ord('q'):
        break
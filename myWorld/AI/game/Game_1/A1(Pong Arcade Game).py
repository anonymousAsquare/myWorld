#computer Vision Pong Arcade Game
#Python 3.6
import pygame
from pygame.locals import *
from sys import exit
import cv2

window_size = (600,600)
pygame.init()
screen = pygame.display.set_mode(window_size,0,32)
pygame.display.set_caption('Asquare Games(Pong Arcade Game)')
#background = pygame.image.load('C:\\Users\AnnonymousAsquare\Documents\myWorld\pyGame\\allcolors.png').convert()
logo = pygame.image.load('game\Game_1\myLogo.png').convert()
pygame.display.set_icon(logo)
score = 0
lifes = 5
fontA = pygame.font.SysFont('javanesetext', 60)
fontGO = pygame.font.SysFont('mvboli', 46)
asq = fontA.render('@Asquare Games',True,(125,125,125),(0,0,0))
font = pygame.font.SysFont('arial', 32)
gscore = font.render('score: '+str(score),True,(255,255,255),(0,0,0))
glife = font.render('life(s): '+str(lifes),True,(255,255,255),(0,0,0))

def rec(x,w,h):
    rec = Rect(x,0,w,h)
    return rec

x = 0
w = 150
h = 30
cirX = window_size[0]/2
cirY = window_size[1]/2
val = 10
cirXInc = val
cirYInc = val
fullscreen = False
cirR = 15

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
keypoints = [0,4,5,8,9,12,13,16,17,20]
hand = AI_hands(window_size[0],window_size[1])
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
            if event.key == K_r:
                score = 0
                lifes = 5
                cirX = window_size[0]/2
                cirY = window_size[1]/2
                cirXInc = val
                cirYInc = val
                gscore = font.render('score: '+str(score),True,(255,255,255),(0,0,0))
                glife = font.render('life(s): '+str(lifes),True,(255,255,255),(0,0,0))
                
    pos = hand.hands(frame)
    for position in pos:
        x,y = position[12]
    if x + w > window_size[0]:
        x = window_size[0] - w
    if x < 0:
        x = 0
    screen.fill((0,0,0))
    #screen.blit(logo,(0,0))

    
    if cirX - cirR <= 0 or cirX + cirR >= window_size[0]:
        cirXInc *= (-1)

    if cirY + cirR >= window_size[1]:
        cirYInc *= (-1)

    if cirY - cirR <= h:
        if cirX >= x and cirX <= x+w:
            cirYInc *= (-1)
            score += 1
            gscore = font.render('score: '+str(score),True,(255,255,255),(0,0,0))

            for i in range(0,100,5):
                if score == i:
                    cirXInc *= 1.5
                    cirYInc *= 1.5
        else:
            cirY = window_size[1] - cirR
            cirX = window_size[0]/2
            lifes -= 1
            if lifes <= 0:
                lifes = 0
            glife = font.render('life(s): '+str(lifes),True,(255,255,255),(0,0,0))

    if lifes == 0:
        end = fontGO.render('GAME OVER',True,(255,0,0),(0,0,0))
        screen.blit(end,((window_size[0]/2)-(end.get_width()/2),(window_size[1]/2)-asq.get_height()-(end.get_height()/2)))
        cirXInc = 0
        cirYInc = 0
    
    cirX += cirXInc
    cirY += cirYInc
    screen.blit(gscore,(10,h))
    screen.blit(glife,(window_size[0]- glife.get_width() ,h))
    screen.blit(asq,((window_size[0]/2)-(asq.get_width()/2),(window_size[1]/2)-(asq.get_height()/2)))
    pygame.draw.rect(screen,(0,255,124),rec(x,w,h))
    pygame.draw.circle(screen,(255,255,255),(cirX,cirY),cirR)
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
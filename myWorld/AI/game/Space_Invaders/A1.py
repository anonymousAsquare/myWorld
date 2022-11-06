import pygame
from pygame.locals import *
from sys import exit
from random import randint
import numpy as np
import pickle
import cv2

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

def handLmDist(handData):
    palmsize = (((handData[9][0]-handData[0][0])**2)+ (handData[9][1]-handData[0][1])**2)**(1./2.)
    handDistMatx =  np.zeros([len(handData),len(handData)], dtype= 'float')
    for row in range(0,len(handData)):
        for column in range(0,len(handData)):
            handDistMatx[row][column]=((((handData[row][0]-handData[column][0])**2)+ (handData[row][1]-handData[column][1])**2)**(1./2.))/palmsize
    return handDistMatx

def errors(unknow_distance,known_distance,keypoints):
    error = 0
    for row in keypoints:
        for column in keypoints:
            error += abs(known_distance[row][column]-unknow_distance[row][column])
    return error

def GesturesErr(unknown_gesture, Known_gestures, keypoints, gestures_names, tol):
    gestures_Err = []
    for i in range(0,len(gestures_names)):
        gesture_Err = errors(unknown_gesture,Known_gestures[i],keypoints)
        gestures_Err.append(gesture_Err)
    min_err = gestures_Err[0]
    idx = 0
    for i in range(0,len(gestures_Err)):
        if gestures_Err[i] < min_err:
            min_err = gestures_Err[i]
            idx = i
    if min_err < tol:
        return gestures_names[idx]
    if min_err >= tol:
        return 'Unknown'
    
with open('C:/Users/AnnonymousAsquare/Documents/myWorld/AI/game/Space_Invaders/space_invaders.pkl', 'rb') as f:
        Known_gestures = pickle.load(f)
        gesture_names = pickle.load(f)
keypoints = [0,4,5,8,9,12,13,16,17,20]
tol = 10

pygame.init()

background = pygame.image.load('C:/Users/AnnonymousAsquare/Documents/myWorld/AI/game/Space_Invaders/background.png')
player = pygame.image.load('C:/Users/AnnonymousAsquare/Documents/myWorld/AI/game/Space_Invaders/player.png')
enemy_1 = pygame.image.load('C:/Users/AnnonymousAsquare/Documents/myWorld/AI/game/Space_Invaders/enemy1.png')
enemy_2 = pygame.image.load('C:/Users/AnnonymousAsquare/Documents/myWorld/AI/game/Space_Invaders/enemy2.png')
logo = pygame.image.load('C:/Users/AnnonymousAsquare/Documents/myWorld/AI/game/Space_Invaders/logo.png')
bullet = pygame.image.load('C:/Users/AnnonymousAsquare/Documents/myWorld/AI/game/Space_Invaders/bullet.png')

window_size = (800,600)

screen = pygame.display.set_mode(window_size,0,32)
pygame.display.set_caption('Asquare Games_________SPACE INVADERS_________')
pygame.display.set_icon(logo)

clock = pygame.time.Clock()

player_xPos = window_size[0]/2-player.get_width()/2
player_yPos = window_size[1]-player.get_height()

bullet_xPos = player_xPos + player.get_width()/2 - bullet.get_width()/2
bullet_yPos = player_yPos + player.get_height()/2 - bullet.get_height()/2
bullet_yInc = 300

enemy_xPos = []
enemy_yPos = []
enemy_xInc = []
enemy_yInc = []
enemy_1xPos = []
enemy_1yPos = []
enemy_1xInc = []
enemy_1yInc = []
numOfEnemies = 15

score = 0
font = pygame.font.SysFont('Arail', 32)
gameOverFont = pygame.font.SysFont('Arail', 100)
Txt_score = font.render('score: '+str(score), True, (255,255,255))
game_Over = gameOverFont.render('GAME OVER', True,(255,255,255))

for i in range(0,int(numOfEnemies/2),1):
    enemy_xPos.append(randint(0,window_size[0]))
    enemy_yPos.append(randint(0,50))
    enemy_xInc.append(140)
    enemy_yInc.append(8)
for i in range(0,int(numOfEnemies/2),1):
    enemy_1xPos.append(randint(0,window_size[0]))
    enemy_1yPos.append(randint(0,50))
    enemy_1xInc.append(120)
    enemy_1yInc.append(8)

fullscreen = False
hand = AI_hands(window_size[0],window_size[1])
shoot = False
gameOver = False
while True:
    ignore, frame = hand.cam.read()
    frameR = cv2.resize(frame,(320,180))
    pos = hand.hands(frame)
    if pos != []:
        unknown_gestures = handLmDist(pos[0])
        error = GesturesErr(unknown_gestures,Known_gestures,keypoints,gesture_names,tol)
        if error == 'shoot':
            shoot = True
        
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
    

    screen.blit(background,(0,0))
    screen.blit(bullet,(bullet_xPos,bullet_yPos))
    screen.blit(player,(player_xPos,player_yPos))
    screen.blit(Txt_score,(10,10))

    for position in pos:
        player_xPos = position[12][0]
        for i in keypoints:
            x = int(position[i][0]/window_size[0]*320)
            y = int(position[i][1]/window_size[1]*180)
            cv2.circle(frameR,(x,y),5,(0,255,0),2)
    
    if player_xPos + player.get_width() > window_size[0]:
        player_xPos = window_size[0] - player.get_width()
    if player_xPos < 0:
        player_xPos = 0

    if gameOver == False:
        for i in range(0,int(numOfEnemies/2),1):
            screen.blit(enemy_2,(enemy_xPos[i],enemy_yPos[i]))
            screen.blit(enemy_1,(enemy_1xPos[i],enemy_1yPos[i]))

        time = clock.tick()
        time_passes_seconds = time/1000.

        if shoot:
            bullet_ydist = time_passes_seconds * bullet_yInc
            bullet_yPos -= bullet_ydist

        for i in range(0,int(numOfEnemies/2),1):
            enemy_xdist = time_passes_seconds * enemy_xInc[i]
            enemy_ydist = time_passes_seconds * enemy_yInc[i]
            enemy_xPos[i] += enemy_xdist
            enemy_yPos[i] += enemy_ydist

            enemy_1xdist = time_passes_seconds * enemy_1xInc[i]
            enemy_1ydist = time_passes_seconds * enemy_1yInc[i]
            enemy_1xPos[i] += enemy_1xdist
            enemy_1yPos[i] += enemy_1ydist

            if enemy_xPos[i] + enemy_2.get_width() >= window_size[0]:
                enemy_xPos[i] = window_size[0] - enemy_2.get_width()
                enemy_xInc[i] *= (-1)
            if enemy_xPos[i] <= 0:
                enemy_xPos[i] = 0
                enemy_xInc[i] *= (-1)
            
            if enemy_1xPos[i] + enemy_1.get_width() >= window_size[0]:
                enemy_1xPos[i] = window_size[0] - enemy_1.get_width()
                enemy_1xInc[i] *= (-1)
            if enemy_1xPos[i] <= 0:
                enemy_1xPos[i] = 0
                enemy_1xInc[i] *= (-1)
            
            if enemy_yPos[i] >= window_size[1] - player.get_height() - (enemy_1.get_height()):
                gameOver = True

            if enemy_1yPos[i] >= window_size[1] - player.get_height() - (enemy_1.get_height()):
                gameOver = True

            if bullet_yPos >= enemy_yPos[i] and bullet_yPos <= enemy_yPos[i]+enemy_2.get_height():
                if bullet_xPos > enemy_xPos[i] and bullet_xPos < enemy_xPos[i] + enemy_2.get_width():
                    shoot = False
                    score += 1
                    enemy_yPos[i] = randint(0,50)
            if bullet_yPos >= enemy_1yPos[i] and bullet_yPos <= enemy_1yPos[i]+enemy_1.get_height():
                if bullet_xPos > enemy_1xPos[i] and bullet_xPos < enemy_1xPos[i] + enemy_1.get_width():
                    enemy_1yPos[i] = randint(0,50)
                    shoot = False
                    score += 1

        if bullet_yPos < 0:
            shoot = False
    
    if gameOver == True:
        screen.blit(game_Over,((window_size[0]/2) -(game_Over.get_width()/2),(window_size[1]/2) - (game_Over.get_height()/2)))

    if not shoot:
        bullet_xPos = player_xPos + player.get_width()/2 - bullet.get_width()/2
        bullet_yPos = player_yPos + player.get_height()/2 - bullet.get_height()/2
    
    Txt_score = font.render('score: '+str(score), True, (255,255,255))

    pygame.display.update()
    
    cv2.imshow('Asquare', frameR)
    cv2.moveWindow('Asquare', 0,0)
    if cv2.waitKey(1) & 0xff == ord('q'):
        break
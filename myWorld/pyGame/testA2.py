import pygame 
import random

pygame.init()
screen = pygame.display.set_mode((800,600))
pygame.display.set_caption('space invaders')
logo = pygame.image.load('ufo.png')
pygame.display.set_icon(logo)
playerImg = pygame.image.load('player.png')
playerX = 370
playerY = 500
playerXInc = 0
stop = playerX
enemyImg = pygame.image.load('enemy.png')
enemyX = random.randint(0,800)
enemyY = random.randint(50,150)
enemyXInc = 4
enemyYInc = 50
backgroundImg = pygame.image.load('background.png')
bulletImg = pygame.image.load('bullet.png')
bulletX = 370
bulletY = 500
bulletXInc = 0
bulletYInc = 10
bulletState = 'ready'

def bullet(x,y):
    global bulletState
    bulletState = 'fire'
    screen.blit(bulletImg,(x + 16, y + 10))

def enemy(x,y):
    screen.blit(enemyImg,(x,y))

def player(x,y):
    screen.blit(playerImg,(x,y))
    
running = True
while running:
    screen.fill((0,0,0))
    screen.blit(backgroundImg,(0,0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False 
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                playerXInc = -5
            if event.key == pygame.K_RIGHT:
                playerXInc = 5
            if event.key == pygame.K_SPACE:
                if bulletState is 'ready':
                    bulletX = playerX
                    bullet(bulletX,bulletY)

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or  event.key == pygame.K_RIGHT:
                playerXInc = 0
            

    if playerX <= 0 :
        playerX = 0
    if playerX >= 736:
        playerX = 736
    playerX += playerXInc

    if enemyX <= 0 or enemyX >= 736:
        #enemyX = 0
        enemyXInc *= -1
        enemyY += enemyYInc 

    enemyX += enemyXInc
    if bulletY <= 0:
        bulletY = 480
        bulletState = 'ready'

    if bulletState is 'fire':
        bullet(bulletX,bulletY)
        bulletY -= bulletYInc
    
    

    player(playerX,playerY)
    enemy(enemyX,enemyY)

    pygame.display.update()
    
import pygame
from pygame.locals import *
from sys import exit
from random import randint

pygame.init()

screen_size = (800,600)
screen = pygame.display.set_mode(screen_size,0,32)
snake_x = 300
snake_y = 400
snake_pos = (snake_x,snake_y)

Up = False
Down = False
Left = False
Right = True

snake_sizeX = 10
snake_sizeY = 10
snake_size = (snake_sizeX,snake_sizeY)
snake = Rect((snake_x,snake_y),snake_size)

food_pos = (randint(10,800), randint(10,600))
newPos = (0,0)

while True:
    screen.fill((0,150,0))

    for event in pygame.event.get():
        if event.type == QUIT:
            exit()
        if event.type == KEYDOWN:
            if event.key == K_q:
                exit()
            if event.key == K_UP:
                if not Down:
                    newPos = (snake_x,snake_y)
                    Up = True
                    Down = False
                    Right = False
                    Left = False
                    print(newPos)
            if event.key == K_RIGHT:
                if not Left:
                    Up = False
                    Down = False
                    Right = True
                    Left = False
            if event.key == K_LEFT:
                if not Right:
                    Up = False
                    Down = False
                    Right = False
                    Left = True
            if event.key == K_DOWN:
                if not Up:
                    Up = False
                    Down = True
                    Right = False
                    Left = False

    if Right:
        snake_x += 0.1

    if Up:
        snake_y -= 0.1

    if Left:
        snake_x -= 0.1

    if Down:
        snake_y += 0.1
    
    x = snake_x
    y = snake_y 
    for i in range(2):
        snake = Rect((x,y),snake_size)
        pygame.draw.rect(screen,(255,255,255), snake) 

        if i > 1:
            snake = Rect(old_pos,snake_size)
            pygame.draw.rect(screen,(255,255,255), snake) 
        old_pos = (x,y)
        #x -= snake_sizeX

    
    """snake = Rect((snake_x,snake_y),snake_size)
    pygame.draw.rect(screen,(255,255,255), snake)""" 
    pygame.draw.circle(screen,(0,0,0),food_pos,5)         
    
    pygame.display.update()
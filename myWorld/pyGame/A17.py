import pygame
from pygame.locals import *
from sys import exit
from random import randint

pygame.init()

screen = pygame.display.set_mode((800,600),0,32)

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            exit()
        if event.type == KEYDOWN:
            if event.key == K_q:
                exit()
    
    x,y = pygame.mouse.get_pos()
    screen.fill((255,255,255))
    pygame.draw.ellipse(screen,(0,255,0),(0,0,x,y))
    pygame.display.update()    
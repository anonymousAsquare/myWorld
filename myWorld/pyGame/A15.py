import pygame
from sys import exit
from pygame.locals import *
from random import randint
pygame.init()

screen = pygame.display.set_mode((800,600),0,32)
point = []
while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            exit()
        if event.type == KEYDOWN:
            if event.key == K_q:
                exit()
        if event.type == MOUSEBUTTONDOWN:
            point.append(event.pos)
    
    screen.fill((255,255,255))

    if len(point) >= 3:
        pygame.draw.polygon(screen,(0,255,0),point)
    for p in point:
        pygame.draw.circle(screen,(0,0,255),p,5,3)
    
    pygame.display.update()